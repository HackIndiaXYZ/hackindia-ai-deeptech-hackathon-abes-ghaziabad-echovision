import streamlit as st
from src.database.db import create_subject
import textwrap


def _md(markup: str):
    st.markdown(textwrap.dedent(markup).strip(), unsafe_allow_html=True)


@st.dialog("Create New Subject")
def create_subject_dialog(teacher_id):
    _md("""
        <div style="display:flex;align-items:center;gap:10px;padding:0.5rem 0 1rem 0;border-bottom:1px solid rgba(88,101,242,0.12);margin-bottom:1rem;">
        <div style="width:40px;height:40px;background:linear-gradient(135deg,#5865F2,#7B4FE8);border-radius:50%;display:flex;align-items:center;justify-content:center;font-size:1.2rem;box-shadow:0 4px 12px rgba(88,101,242,0.3);flex-shrink:0;">📚</div>
        <div>
        <p style="margin:0;color:#1A2260;font-weight:700;font-size:0.95rem;">New Subject Details</p>
        <p style="margin:0;color:#8B92C8;font-size:0.8rem;">Fill in the details below to create your subject</p>
        </div>
        </div>
    """)

    sub_id = st.text_input("Subject Code", placeholder="CS101")
    sub_name = st.text_input("Subject Name", placeholder="Introduction to Computer Science")
    sub_section = st.text_input("Section", placeholder="A")

    st.space()

    if st.button("Create Subject Now", type='primary', width='stretch', icon=':material/add_circle:'):
        if sub_id and sub_name and sub_section:
            try:
                create_subject(sub_id, sub_name, sub_section, teacher_id)
                st.toast("Subject Created Succesfully!")
                st.rerun()
            except Exception as e:
                st.error(f"Error: {str(e)}")
        else:
            st.warning("Please fill all the fields")
