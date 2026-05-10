import streamlit as st
import textwrap


def footer_home():
    st.markdown(textwrap.dedent("""
        <div style="margin-top:2.5rem;padding-top:1.25rem;border-top:1px solid rgba(255,255,255,0.18);display:flex;gap:8px;justify-content:center;align-items:center;">
        <p style="font-weight:600;color:rgba(255,255,255,0.65);margin:0;font-size:0.85rem;letter-spacing:0.02em;">Created with ❤️ by</p>
        <span style="font-weight:700;color:#ffffff;font-size:0.9rem;letter-spacing:0.05em;font-family:Outfit,sans-serif;">Echo Vision Team</span>
        </div>
    """).strip(), unsafe_allow_html=True)


def footer_dashboard():
    st.markdown(textwrap.dedent("""
        <div style="margin-top:2.5rem;padding-top:1.25rem;border-top:1px solid rgba(88,101,242,0.12);display:flex;gap:8px;justify-content:center;align-items:center;">
        <p style="font-weight:600;color:#8B92C8;margin:0;font-size:0.85rem;letter-spacing:0.02em;">Created with ❤️ by</p>
        <span style="font-weight:700;color:#5865F2;font-size:0.9rem;letter-spacing:0.05em;font-family:Outfit,sans-serif;">Echo Vision Team</span>
        </div>
    """).strip(), unsafe_allow_html=True)
