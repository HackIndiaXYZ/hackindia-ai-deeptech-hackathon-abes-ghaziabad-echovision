import streamlit as st
from src.database.db import enroll_student_to_subject
from src.database.config import supabase
import time
import textwrap


def _md(markup: str):
    st.markdown(textwrap.dedent(markup).strip(), unsafe_allow_html=True)


@st.dialog("Quick Enrollment")
def auto_enroll_dialog(subject_code):
    student_id = st.session_state.student_data['student_id']

    res = supabase.table('subjects').select('subject_id, name').eq('subject_code', subject_code).execute()
    if not res.data:
        _md("""
            <div style="text-align:center;padding:1.5rem 0;">
            <div style="font-size:2.5rem;margin-bottom:0.75rem;">❌</div>
            <p style="color:#1A2260;font-weight:700;font-size:1rem;margin:0 0 4px 0;">Subject Not Found</p>
            <p style="color:#8B92C8;font-size:0.85rem;margin:0;">The subject code in this link is invalid or has been removed.</p>
            </div>
        """)
        if st.button('Close', width='stretch', type='tertiary'):
            st.query_params.clear()
            st.rerun()
        return

    subject = res.data[0]

    check = supabase.table('subject_students').select('*').eq('subject_id', subject['subject_id']).eq('student_id', student_id).execute()
    if check.data:
        _md(f"""
            <div style="text-align:center;padding:1.5rem 0;">
            <div style="font-size:2.5rem;margin-bottom:0.75rem;">✅</div>
            <p style="color:#1A2260;font-weight:700;font-size:1rem;margin:0 0 4px 0;">Already Enrolled</p>
            <p style="color:#8B92C8;font-size:0.85rem;margin:0;">You're already enrolled in <b>{subject['name']}</b>.</p>
            </div>
        """)
        if st.button('Got it!', type='primary', width='stretch'):
            st.query_params.clear()
            st.rerun()
        return

    _md(f"""
        <div style="text-align:center;padding:1rem 0 1.25rem 0;">
        <div style="display:inline-flex;align-items:center;justify-content:center;width:56px;height:56px;background:linear-gradient(135deg,#5865F2,#7B4FE8);border-radius:50%;margin-bottom:14px;box-shadow:0 6px 20px rgba(88,101,242,0.35);font-size:1.6rem;">🎓</div>
        <p style="margin:0 0 4px 0;color:#1A2260;font-weight:800;font-size:1.15rem;">You've been invited!</p>
        <p style="margin:0;color:#8B92C8;font-size:0.88rem;">Would you like to join</p>
        <p style="margin:8px 0 0 0;color:#5865F2;font-weight:800;font-size:1.2rem;">{subject['name']}</p>
        </div>
    """)

    col1, col2 = st.columns(2)

    with col1:
        if st.button('No thanks', width='stretch', type='tertiary'):
            st.query_params.clear()
            st.rerun()
    with col2:
        if st.button('Yes, enroll now!', type='primary', width='stretch', icon=':material/school:'):
            enroll_student_to_subject(student_id, subject['subject_id'])
            st.success('Joined successfully!')
            st.query_params.clear()
            time.sleep(2)
            st.rerun()
