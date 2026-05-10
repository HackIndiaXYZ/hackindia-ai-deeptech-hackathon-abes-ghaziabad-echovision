import streamlit as st
import textwrap


def html(markup: str):
    """
    Render HTML via st.markdown safely.
    Strips common leading whitespace first so that indented triple-quoted
    strings don't accidentally trigger Markdown code-block mode (4-space rule).
    """
    st.markdown(textwrap.dedent(markup).strip(), unsafe_allow_html=True)
