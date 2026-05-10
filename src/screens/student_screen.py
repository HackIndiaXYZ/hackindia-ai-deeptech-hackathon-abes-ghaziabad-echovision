import streamlit as st
import textwrap

from src.ui.base_layout import style_background_dashboard, style_base_layout

from src.components.header import header_dashboard
from src.components.footer import footer_dashboard
from PIL import Image
import numpy as np
from src.pipelines.face_pipeline import predict_attendance, get_face_embeddings, train_classifier
from src.pipelines.voice_pipeline import get_voice_embedding
from src.database.db import get_all_students, create_student, get_student_subjects, get_student_attendance, unenroll_student_to_subject
import time

from src.components.dialog_enroll import enroll_dialog
from src.components.subject_card import subject_card


def _md(markup: str):
    st.markdown(textwrap.dedent(markup).strip(), unsafe_allow_html=True)


def student_dashboard():
    student_data = st.session_state.student_data
    student_id = student_data['student_id']

    c1, c2 = st.columns([3,1], vertical_alignment='center', gap='large')
    with c1:
        header_dashboard()
    with c2:
        _md(f"""
            <p style='color:#6B73B0;font-size:0.82rem;font-weight:600;text-align:right;margin:0 0 4px 0;letter-spacing:0.04em;text-transform:uppercase;'>Signed in as</p>
            <p style='color:#1A2260;font-size:1rem;font-weight:700;text-align:right;margin:0;'>{student_data['name']}</p>
        """)
        if st.button("Logout", type='secondary', key='loginbackbtn', shortcut="control+backspace"):
            st.session_state['is_logged_in'] = False
            del st.session_state.student_data 
            st.rerun()

    st.divider()

    col1, col2 = st.columns([2, 1], vertical_alignment='center')
    with col1:
        _md("""
            <div style="display:flex;align-items:center;gap:10px;margin-bottom:1rem;">
            <div style="width:5px;height:28px;border-radius:3px;background:linear-gradient(180deg,#5865F2,#EB459E);flex-shrink:0;"></div>
            <h3 style="margin:0;color:#1A2260;font-size:1.4rem;font-weight:700;">Your Enrolled Subjects</h3>
            </div>
        """)
    with col2:
        if st.button('＋ Enroll in Subject', type='primary', width='stretch'):
            enroll_dialog()

    st.space()

    with st.spinner('Loading your enrolled subjects..'):
        subjects = get_student_subjects(student_id)
        logs = get_student_attendance(student_id)

    stats_map = {}

    for log in logs:
        sid = log['subject_id']

        if sid not in stats_map:
            stats_map[sid] = {"total": 0, "attended": 0}

        stats_map[sid]['total'] += 1

        if log.get('is_present'):
            stats_map[sid]['attended'] += 1

    if not subjects:
        _md("""
            <div style="text-align:center;padding:3rem 2rem;background:rgba(255,255,255,0.55);backdrop-filter:blur(12px);border-radius:1.5rem;border:1.5px dashed rgba(88,101,242,0.25);margin:1rem 0;">
            <div style="font-size:3rem;margin-bottom:0.75rem;">🎓</div>
            <h4 style="color:#1A2260;font-size:1.2rem;font-weight:700;margin:0 0 0.4rem 0;">No Subjects Enrolled</h4>
            <p style="color:#6B73B0;font-size:0.95rem;margin:0;">Click <b>Enroll in Subject</b> above and enter your subject code to join a class.</p>
            </div>
        """)
    else:
        cols = st.columns(2)
        for i, sub_node in enumerate(subjects):
            sub = sub_node['subjects']
            sid = sub['subject_id']

            stats = stats_map.get(sid, {"total": 0, "attended": 0})
            def unenroll_button():
                    if st.button("Unenroll from this course", type='tertiary', width='stretch', icon=':material/delete_forever:'):
                        unenroll_student_to_subject(student_id, sid)
                        st.toast(f'Unenrolled from {sub["name"]} successfully!')
                        st.rerun()

            with cols[i % 2]:

                subject_card(
                    name=sub['name'],
                    code=sub['subject_code'],
                    section=sub['section'],
                    stats=[
                        ('📅', 'Total', stats['total']),
                        ('✅', 'Attended', stats['attended']),
                    ],
                    footer_callback=unenroll_button
                )
    footer_dashboard()


def student_screen():

    style_background_dashboard()
    style_base_layout()

    if "student_data" in st.session_state:
        student_dashboard()
        return
    
    c1, c2 = st.columns([3,1], vertical_alignment='center', gap='large')
    with c1:
        header_dashboard()
    with c2:
        if st.button("← Home", type='secondary', key='loginbackbtn', shortcut="control+backspace"):
            st.session_state['login_type'] = None
            st.rerun()

    st.divider()

    _md("""
        <div style="text-align:center;margin:0.5rem 0 1.25rem 0;">
        <div style="display:inline-flex;align-items:center;justify-content:center;width:56px;height:56px;background:linear-gradient(135deg,#5865F2,#7B4FE8);border-radius:50%;margin-bottom:12px;box-shadow:0 6px 20px rgba(88,101,242,0.35);">
        <span style="font-size:1.6rem;">👤</span>
        </div>
        <h2 style="text-align:center;margin:0 0 4px 0;font-family:Outfit,sans-serif;font-size:1.75rem;font-weight:800;color:#1A2260;letter-spacing:-0.3px;">Login with Face ID</h2>
        <p style="color:#8B92C8;font-size:0.92rem;margin:0;">Position your face in the center of the frame</p>
        </div>
    """)

    show_registration = False
    photo_source = st.camera_input("Position your face in the center")

    if photo_source:
        img = np.array(Image.open(photo_source))

        with st.spinner('AI is scanning..'):
            detected, all_ids, num_faces = predict_attendance(img)

            if num_faces == 0:
                st.warning('Face not found! Make sure your face is clearly visible.')
            elif num_faces > 1:
                st.warning('Multiple faces detected. Please ensure only one face is visible.')
            else:
                if detected:
                    student_id = list(detected.keys())[0]
                    all_students = get_all_students()
                    student = next((s for s in all_students if s['student_id'] == student_id), None)

                    if student:
                        st.session_state.is_logged_in = True
                        st.session_state.user_role = 'student'
                        st.session_state.student_data = student
                        st.toast(f'Welcome Back {student["name"]}')
                        time.sleep(1)
                        st.rerun()
                else:
                    st.info('Face not recognized! You might be a new student.')
                    show_registration = True

    if show_registration:
        _md("""
            <div style="margin-top:1rem;">
            <div style="display:flex;align-items:center;gap:10px;margin-bottom:1rem;">
            <div style="width:5px;height:28px;border-radius:3px;background:linear-gradient(180deg,#5865F2,#EB459E);flex-shrink:0;"></div>
            <h3 style="margin:0;color:#1A2260;font-size:1.2rem;font-weight:700;">Register New Profile</h3>
            </div>
            </div>
        """)

        with st.container(border=True):
            new_name = st.text_input("Your full name", placeholder='E.g. Hamza Rizvi')

            _md("""
                <div style="display:flex;align-items:center;gap:8px;margin:0.75rem 0 0.25rem 0;">
                <span style="font-size:1.1rem;">🎙️</span>
                <span style="font-weight:700;color:#1A2260;font-size:0.95rem;">Voice Enrollment</span>
                <span style="background:linear-gradient(135deg,rgba(88,101,242,0.1),rgba(123,79,232,0.1));color:#5865F2;font-size:0.7rem;font-weight:700;padding:2px 8px;border-radius:999px;border:1px solid rgba(88,101,242,0.2);letter-spacing:0.05em;">OPTIONAL</span>
                </div>
                <p style="color:#8B92C8;font-size:0.85rem;margin:0 0 0.5rem 0;">Record a short phrase for voice-only attendance recognition</p>
            """)

            audio_data = None

            try:
                audio_data = st.audio_input('Record a short phrase like "I am present, My name is Akash."')
            except Exception:
                st.error('Audio Data failed!')

            st.space()

            if st.button('Create Account', type='primary', icon=':material/person_add:'):
                if new_name:
                    with st.spinner('Creating profile..'):
                        img = np.array(Image.open(photo_source))
                        encodings = get_face_embeddings(img)
                        if encodings:
                            face_emb = encodings[0].tolist()

                            voice_emb = None
                            if audio_data:
                                voice_emb = get_voice_embedding(audio_data.read())

                            response_data = create_student(new_name, face_embedding=face_emb, voice_embedding=voice_emb)

                            if response_data:
                                train_classifier()
                                st.session_state.is_logged_in = True
                                st.session_state.user_role = 'student'
                                st.session_state.student_data = response_data[0]
                                st.toast(f'Profile Created! Hi {new_name}!')
                                time.sleep(1)
                                st.rerun()
                        else:
                            st.error("Couldn't capture your facial features for registration")

                else:
                    st.warning('Please enter your name!')

    footer_dashboard()