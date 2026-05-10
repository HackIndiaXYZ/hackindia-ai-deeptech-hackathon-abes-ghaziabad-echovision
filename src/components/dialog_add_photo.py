import streamlit as st
from src.database.db import enroll_student_to_subject
from src.database.config import supabase
from PIL import Image
import time
import textwrap


def _md(markup: str):
    st.markdown(textwrap.dedent(markup).strip(), unsafe_allow_html=True)


@st.dialog("Capture or Upload Photos")
def add_photos_dialog():

    _md("""
        <div style="display:flex;align-items:center;gap:10px;padding:0.5rem 0 1rem 0;border-bottom:1px solid rgba(88,101,242,0.12);margin-bottom:1rem;">
        <div style="width:40px;height:40px;background:linear-gradient(135deg,#5865F2,#7B4FE8);border-radius:50%;display:flex;align-items:center;justify-content:center;font-size:1.2rem;box-shadow:0 4px 12px rgba(88,101,242,0.3);flex-shrink:0;">📸</div>
        <div>
        <p style="margin:0;color:#1A2260;font-weight:700;font-size:0.95rem;">Add Classroom Photos</p>
        <p style="margin:0;color:#8B92C8;font-size:0.8rem;">Use camera or upload files to scan for attendance</p>
        </div>
        </div>
    """)

    if 'photo_tab' not in st.session_state:
        st.session_state.photo_tab = 'camera'

    t1, t2 = st.columns(2)

    with t1:
        type_camera = "primary" if st.session_state.photo_tab == 'camera' else 'tertiary'
        if st.button('📷 Camera', type=type_camera, width='stretch'):
            st.session_state.photo_tab = 'camera'

    with t2:
        type_upload = "primary" if st.session_state.photo_tab == 'upload' else 'tertiary'
        if st.button('📁 Upload Photos', type=type_upload, width='stretch'):
            st.session_state.photo_tab = 'upload'

    st.space()

    if st.session_state.photo_tab == 'camera':
        cam_photo = st.camera_input('Take Snapshot', key='dialog_cam')
        if cam_photo:
            st.session_state.attendance_images.append(Image.open(cam_photo))
            st.toast('Photo Captured ✅')
            st.rerun()

    if st.session_state.photo_tab == 'upload':
        uploaded_files = st.file_uploader('Choose image files', type=['jpg', 'png', 'jpeg'], accept_multiple_files=True, key='dialog_upload')

        if uploaded_files:
            for f in uploaded_files:
                st.session_state.attendance_images.append(Image.open(f))
            
            st.toast('Photos Uploaded Successfully ✅')
            st.rerun()

    st.divider()

    photo_count = len(st.session_state.get('attendance_images', []))
    btn_label = f"Done  ({photo_count} photo{'s' if photo_count != 1 else ''} added)" if photo_count else "Done"
    if st.button(btn_label, type='primary', width='stretch', icon=':material/check_circle:'):
        st.rerun()
