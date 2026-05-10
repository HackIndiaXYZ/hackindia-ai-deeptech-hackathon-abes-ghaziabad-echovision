import streamlit as st
from src.database.db import enroll_student_to_subject
from src.database.config import supabase
import time
import textwrap

from src.database.db import create_attendance


def _md(markup: str):
    st.markdown(textwrap.dedent(markup).strip(), unsafe_allow_html=True)


def show_attendance_result(df, logs):
    _md("""
        <p style="color:#6B73B0;font-size:0.88rem;margin:0 0 0.75rem 0;">Review the results below before confirming. This will be saved to the attendance records.</p>
    """)
    st.dataframe(df, hide_index=True, width='stretch')

    st.space()

    col1, col2 = st.columns(2)

    with col1:
        if st.button('✕  Discard', width='stretch', type='tertiary'):
            st.session_state.voice_attendance_results = None
            st.session_state.attendance_images = []
            st.rerun()

    with col2:
        if st.button('✓  Confirm & Save', width='stretch', type='primary'):
            try:
                create_attendance(logs)
                st.toast("Attendance saved ✅")
                st.session_state.attendance_images = []
                st.session_state.voice_attendance_results = None
                st.rerun()
            except Exception as e:
                st.error('Sync failed!')


@st.dialog("Attendance Report")
def attendance_result_dialog(df, logs):
    _md("""
        <div style="display:flex;align-items:center;gap:10px;padding:0.5rem 0 1rem 0;border-bottom:1px solid rgba(88,101,242,0.12);margin-bottom:1rem;">
        <div style="width:40px;height:40px;background:linear-gradient(135deg,#22C55E,#16A34A);border-radius:50%;display:flex;align-items:center;justify-content:center;font-size:1.2rem;box-shadow:0 4px 12px rgba(34,197,94,0.3);flex-shrink:0;">📋</div>
        <div>
        <p style="margin:0;color:#1A2260;font-weight:700;font-size:0.95rem;">AI Analysis Complete</p>
        <p style="margin:0;color:#8B92C8;font-size:0.8rem;">Review attendance before confirming</p>
        </div>
        </div>
    """)
    show_attendance_result(df, logs)
