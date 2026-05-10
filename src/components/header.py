import streamlit as st
import textwrap
import base64
import os


def _get_logo_b64() -> str:
    """Read local logo.png and return a base64 data URI."""
    logo_path = os.path.join(os.path.dirname(__file__), "..", "assets", "logo.png")
    with open(logo_path, "rb") as f:
        data = base64.b64encode(f.read()).decode("utf-8")
    return f"data:image/png;base64,{data}"


def header_home():
    logo_url = _get_logo_b64()

    st.markdown(textwrap.dedent(f"""
        <div style="display:flex;flex-direction:column;align-items:center;justify-content:center;margin-bottom:2rem;margin-top:1.5rem;">
        <img src='{logo_url}' style='height:110px;width:110px;border-radius:50%;object-fit:cover;margin-bottom:12px;box-shadow:0 8px 32px rgba(0,0,0,0.2),0 0 0 4px rgba(255,255,255,0.15);display:block;' />
        <div style='text-align:center;color:#ffffff;font-size:2rem;font-weight:800;line-height:1;letter-spacing:2px;margin:8px 0 4px 0;text-shadow:0 2px 12px rgba(0,0,0,0.2);font-family:Outfit,sans-serif;'>Echo Vision</div>
        <p style='color:rgba(255,255,255,0.7);font-size:0.95rem;margin:0;letter-spacing:0.08em;text-transform:uppercase;font-weight:500;'>AI-Powered Attendance</p>
        </div>
    """).strip(), unsafe_allow_html=True)


def header_dashboard():
    logo_url = _get_logo_b64()

    st.markdown(textwrap.dedent(f"""
        <div style="display:flex;align-items:center;justify-content:flex-start;gap:12px;padding:4px 0;">
        <img src='{logo_url}' style='height:62px;width:62px;border-radius:50%;object-fit:cover;flex-shrink:0;box-shadow:0 4px 12px rgba(88,101,242,0.25);display:block;' />
        <div>
        <div style='text-align:left;color:#5865F2;font-size:1.4rem;font-weight:800;line-height:0.95;margin:0;letter-spacing:1px;font-family:Outfit,sans-serif;'>Echo Vision</div>
        <span style='font-size:0.7rem;color:#8B92C8;letter-spacing:0.1em;text-transform:uppercase;font-weight:600;font-family:Outfit,sans-serif;'>AI Attendance</span>
        </div>
        </div>
    """).strip(), unsafe_allow_html=True)
