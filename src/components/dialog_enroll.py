import streamlit as st
from src.database.db import enroll_student_to_subject
from src.database.config import supabase
from postgrest.exceptions import APIError
import time
import textwrap


def _md(markup: str):
    st.markdown(textwrap.dedent(markup).strip(), unsafe_allow_html=True)


@st.dialog("Enroll in Subject")
def enroll_dialog():
    _md("""
        <div style="display:flex;align-items:center;gap:10px;padding:0.5rem 0 1rem 0;border-bottom:1px solid rgba(88,101,242,0.12);margin-bottom:1rem;">
        <div style="width:40px;height:40px;background:linear-gradient(135deg,#5865F2,#7B4FE8);border-radius:50%;display:flex;align-items:center;justify-content:center;font-size:1.2rem;box-shadow:0 4px 12px rgba(88,101,242,0.3);flex-shrink:0;">🎓</div>
        <div>
        <p style="margin:0;color:#1A2260;font-weight:700;font-size:0.95rem;">Join a Subject</p>
        <p style="margin:0;color:#8B92C8;font-size:0.8rem;">Ask your teacher for the subject code</p>
        </div>
        </div>
    """)

    join_code = st.text_input(
        'Subject Code',
        placeholder='e.g. CS101'
    )

    st.space()

    if st.button('Enroll now', type='primary', width='stretch', icon=':material/school:'):

        if not join_code:
            st.warning('Please enter a subject code')
            return

        try:
            res = (
                supabase.table('subjects')
                .select('subject_id, name, subject_code')
                .eq('subject_code', join_code.strip())
                .execute()
            )

            # Subject code not found
            if not res.data:
                st.warning('No subject found for this code')
                return

            subject = res.data[0]
            student_id = st.session_state.student_data['student_id']

            check = (
                supabase.table('subject_students')
                .select('*')
                .eq('subject_id', subject['subject_id'])
                .eq('student_id', student_id)
                .execute()
            )

            if check.data:
                st.warning('You are already enrolled in this subject')
            else:
                enroll_student_to_subject(
                    student_id,
                    subject['subject_id']
                )

                st.success('Successfully enrolled!')
                time.sleep(1)
                st.rerun()

        except APIError:
            st.error('Invalid subject code or subject does not exist')

        except Exception as e:
            print(e)  # debug in terminal
            st.error('Something went wrong. Please try again.')