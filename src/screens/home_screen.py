import streamlit as st
from src.components.header import header_home
from src.components.footer import footer_home
from src.ui.base_layout import style_base_layout, style_background_home
import textwrap

def home_screen():

    header_home()
    style_background_home()
    style_base_layout()

    st.markdown(textwrap.dedent("""
        <p style="text-align:center;color:rgba(255,255,255,0.7);font-size:1rem;margin:0 0 1.75rem 0;font-weight:500;letter-spacing:0.03em;">Who are you today?</p>
    """).strip(), unsafe_allow_html=True)

    col1, col2 = st.columns(2, gap="large")

    with col1:
        st.header("I'm a Student")
        st.markdown('<p style="color:rgba(255,255,255,0.7);font-size:0.9rem;margin-top:-0.25rem;">Log in with Face ID &amp; manage your courses</p>', unsafe_allow_html=True)
        st.markdown('<img src="https://i.ibb.co/844D9Lrt/mascot-student.png" style="width:130px;display:block;margin:0.5rem auto 1rem auto;filter:drop-shadow(0 8px 24px rgba(0,0,0,0.25));" />', unsafe_allow_html=True)
        if st.button('Student Portal', type='primary', icon=':material/arrow_outward:', icon_position='right'):
            st.session_state['login_type']='student'
            st.rerun()

    with col2:
        st.header("I'm a Teacher")
        st.markdown('<p style="color:rgba(255,255,255,0.7);font-size:0.9rem;margin-top:-0.25rem;">Take AI attendance &amp; manage your subjects</p>', unsafe_allow_html=True)
        st.markdown('<img src="https://i.ibb.co/CsmQQV6X/mascot-prof.png" style="width:155px;display:block;margin:0.5rem auto 1rem auto;filter:drop-shadow(0 8px 24px rgba(0,0,0,0.25));" />', unsafe_allow_html=True)
        if st.button('Teacher Portal', type='primary', icon=':material/arrow_outward:', icon_position='right'):
            st.session_state['login_type']='teacher'
            st.rerun()

    footer_home()