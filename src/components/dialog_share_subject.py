import streamlit as st
import textwrap
import segno
import io


def _md(markup: str):
    st.markdown(textwrap.dedent(markup).strip(), unsafe_allow_html=True)


@st.dialog("Share Class Link")
def share_subject_dialog(subject_name, subject_code):
    app_domain = "echovision-main.streamlit.app"
    join_url = f"{app_domain}/?join-code={subject_code}"

    _md(f"""
        <div style="display:flex;align-items:center;gap:10px;padding:0.5rem 0 1rem 0;border-bottom:1px solid rgba(88,101,242,0.12);margin-bottom:1rem;">
        <div style="width:40px;height:40px;background:linear-gradient(135deg,#EB459E,#C9368A);border-radius:50%;display:flex;align-items:center;justify-content:center;font-size:1.2rem;box-shadow:0 4px 12px rgba(235,69,158,0.3);flex-shrink:0;">📡</div>
        <div>
        <p style="margin:0;color:#1A2260;font-weight:700;font-size:0.95rem;">{subject_name}</p>
        <p style="margin:0;color:#8B92C8;font-size:0.8rem;">Share this link or QR code with your students</p>
        </div>
        </div>
    """)

    qr = segno.make(join_url)

    out = io.BytesIO()

    qr.save(out, kind='png', scale=10, border=1)

    col1, col2 = st.columns(2)

    with col1:
        st.markdown('<p style="font-weight:700;color:#1A2260;font-size:0.95rem;margin-bottom:0.5rem;">🔗 Copy Link</p>', unsafe_allow_html=True)
        st.code(join_url, language="text")
        st.markdown('<p style="font-weight:700;color:#1A2260;font-size:0.95rem;margin:0.75rem 0 0.5rem 0;">🏷️ Subject Code</p>', unsafe_allow_html=True)
        st.code(subject_code, language="text")
        st.info('Share via WhatsApp or Email', icon="💬")

    with col2:
        st.markdown('<p style="font-weight:700;color:#1A2260;font-size:0.95rem;margin-bottom:0.5rem;">📱 Scan to Join</p>', unsafe_allow_html=True)
        st.image(out.getvalue(), caption='QR Code for class joining')
