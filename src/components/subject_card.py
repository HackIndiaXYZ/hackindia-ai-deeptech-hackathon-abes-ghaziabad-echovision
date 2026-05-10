import streamlit as st

def subject_card(name, code, section, stats=None, footer_callback=None):
    stats_html = ""
    if stats:
        stat_items = "".join([
            f'<div style="background:linear-gradient(135deg,rgba(235,69,158,0.07),rgba(88,101,242,0.06));border:1px solid rgba(235,69,158,0.15);padding:5px 13px;border-radius:999px;font-size:0.82rem;font-weight:600;color:#1A2260;display:flex;align-items:center;gap:5px;">{icon} <b>{value}</b>&nbsp;<span style="color:#6B73B0;font-weight:500;">{label}</span></div>'
            for icon, label, value in stats
        ])
        stats_html = f'<div style="display:flex;gap:8px;flex-wrap:wrap;margin-bottom:0.5rem;">{stat_items}</div>'

    html = (
        '<div style="background:rgba(255,255,255,0.88);backdrop-filter:blur(12px);-webkit-backdrop-filter:blur(12px);border-radius:1.25rem;border:1px solid rgba(88,101,242,0.12);box-shadow:0 4px 20px rgba(88,101,242,0.08),0 1px 4px rgba(0,0,0,0.04);margin-bottom:1.1rem;overflow:hidden;">'
        '<div style="height:5px;background:linear-gradient(90deg,#5865F2,#EB459E);border-radius:1.25rem 1.25rem 0 0;"></div>'
        '<div style="padding:1.25rem 1.4rem 1rem 1.4rem;">'
        f'<h3 style="margin:0 0 0.4rem 0;color:#1A2260;font-size:1.2rem;font-weight:700;line-height:1.3;">{name}</h3>'
        '<div style="display:flex;align-items:center;gap:8px;flex-wrap:wrap;margin-bottom:0.85rem;">'
        f'<span style="background:linear-gradient(135deg,rgba(88,101,242,0.12),rgba(88,101,242,0.07));color:#5865F2;padding:3px 10px;border-radius:999px;font-size:0.8rem;font-weight:700;border:1px solid rgba(88,101,242,0.2);letter-spacing:0.04em;">{code}</span>'
        f'<span style="color:#8B92C8;font-size:0.82rem;font-weight:500;">Section {section}</span>'
        '</div>'
        + stats_html +
        '</div>'
        '</div>'
    )

    st.markdown(html, unsafe_allow_html=True)

    if footer_callback:
        footer_callback()


def _md(html: str):
    """Render HTML via st.markdown without indentation-triggered code blocks."""
    import textwrap
    st.markdown(textwrap.dedent(html).strip(), unsafe_allow_html=True)
