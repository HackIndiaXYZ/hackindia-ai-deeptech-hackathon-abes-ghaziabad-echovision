import streamlit as st
import textwrap

from src.pipelines.voice_pipeline import process_bulk_audio

from src.database.config import supabase

import pandas as pd


from src.components.dialog_attendance_results import show_attendance_result
from datetime import datetime


def _md(markup: str):
    st.markdown(textwrap.dedent(markup).strip(), unsafe_allow_html=True)


@st.dialog('Voice Attendance')
def voice_attendance_dialog(selected_subject_id):
    _md("""
        <div style="display:flex;align-items:center;gap:10px;padding:0.5rem 0 1rem 0;border-bottom:1px solid rgba(88,101,242,0.12);margin-bottom:1rem;">
        <div style="width:40px;height:40px;background:linear-gradient(135deg,#EB459E,#C9368A);border-radius:50%;display:flex;align-items:center;justify-content:center;font-size:1.2rem;box-shadow:0 4px 12px rgba(235,69,158,0.3);flex-shrink:0;">🎙️</div>
        <div>
        <p style="margin:0;color:#1A2260;font-weight:700;font-size:0.95rem;">Voice Attendance</p>
        <p style="margin:0;color:#8B92C8;font-size:0.8rem;">AI will identify students from their voice</p>
        </div>
        </div>
    """)

    _md("""
        <p style="background:linear-gradient(135deg,rgba(88,101,242,0.07),rgba(123,79,232,0.05));border:1px solid rgba(88,101,242,0.15);border-radius:0.8rem;padding:10px 14px;color:#3A4280;font-size:0.85rem;margin-bottom:1rem;">
        💡 Ask students to say <b>"I am present"</b> or their name aloud. Record the full classroom audio below.
        </p>
    """)

    audio_data = None

    audio_data = st.audio_input("Record classroom audio")

    st.space()

    if st.button('Analyze Audio', width='stretch', type='primary', icon=':material/graphic_eq:'):
        if audio_data is None:
            st.warning('⚠️ Please record audio first before analyzing.')
            st.stop()
        with st.spinner('Processing audio data...'):
            enrolled_res = supabase.table('subject_students').select("*, students(*)").eq('subject_id', selected_subject_id).execute()
            enrolled_students = enrolled_res.data

            if not enrolled_students:
                st.warning('No students enrolled in this course')
                return
            candidates_dict = {
                s['students']['student_id']: s['students']['voice_embedding'] 
                for s in enrolled_students if s['students'].get('voice_embedding')
            }

            if not candidates_dict:
                st.error('No enrolled students have voice profiles registered')
                return
            
            audio_bytes = audio_data.read()

            detected_scores = process_bulk_audio(audio_bytes, candidates_dict)

            results, attendance_to_log = [], []

            current_timestamp = datetime.now().strftime("%Y-%m-%dT%H:%M:%S")

            for node in enrolled_students:
                student = node['students']
                score = detected_scores.get(student['student_id'], 0.0)
                is_present = bool(score > 0)

                results.append({
                    "Name": student['name'],
                    "ID": student['student_id'],
                    "Source": score if is_present else "-",
                    "Status": "✅ Present" if is_present else "❌ Absent"
                })

                attendance_to_log.append({
                    'student_id': student['student_id'],
                    'subject_id': selected_subject_id,
                    'timestamp': current_timestamp,
                    'is_present': bool(is_present)
                })
            st.session_state.voice_attendance_results = (pd.DataFrame(results), attendance_to_log)

    if st.session_state.get('voice_attendance_results'):
        st.divider()
        df_results, logs = st.session_state.voice_attendance_results
        show_attendance_result(df_results, logs)
