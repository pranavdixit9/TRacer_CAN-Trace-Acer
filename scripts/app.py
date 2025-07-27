import streamlit as st
from parsor import parse_streamed_trace
from utils import download_pdf

st.set_page_config(layout="wide")
st.title("🚗 TRacer - CAN Trace Acer 🚚")

# Custom CSS
st.markdown("""
    <style>
    .colored-text {
        font-family: monospace;
        font-size: 15px;
        white-space: pre-wrap;
    }
    </style>
""", unsafe_allow_html=True)

# Initialize session state
if "trace_text" not in st.session_state:
    st.session_state.trace_text = ""
if "explanation_sections" not in st.session_state:
    st.session_state.explanation_sections = []

# Upload + Text Area Row
with st.container():
    cols = st.columns([8, 1])

    with cols[0]:
        trace_input = st.text_area(
            label="Paste your CAN trace or upload a .txt/.asc file →",
            value=st.session_state.trace_text,
            height=100,
            key="trace_text_box"
        )
        st.session_state.trace_text = trace_input.strip()

    with cols[1]:
        uploaded_file = st.file_uploader(" ", type=["txt", "asc"], label_visibility="collapsed")
        if uploaded_file:
            file_text = uploaded_file.read().decode("utf-8")

            if uploaded_file.name.endswith(".asc"):
                # Handle ASC format
                asc_lines = file_text.splitlines()
                filtered_lines = []
                for line in asc_lines:
                    line = line.strip()
                    if line == "" or line.startswith(("date", "base", "Begin", "End")):
                        continue
                    if " Rx " in line or " Tx " in line:
                        filtered_lines.append(line)
                st.session_state.trace_text = "\n".join(filtered_lines)
            else:
                st.session_state.trace_text = file_text.strip()

# ✅ Always visible start button
if st.session_state.trace_text:
    st.subheader("📄 CAN Trace Preview")
    st.code(st.session_state.trace_text, language="text")

    if st.button("▶️ Start Analyzing"):
        st.session_state.explanation_sections.clear()
        with st.spinner("Analyzing..."):
            response_container = st.container()
            for section in parse_streamed_trace(st.session_state.trace_text):
                st.session_state.explanation_sections.append(section)
                response_container.markdown(
                    f"<div class='colored-text' style='color:{section['color']}'>"
                    f"{section['content']}</div>",
                    unsafe_allow_html=True
                )

# ✅ Export PDF always shown if explanations exist
if st.session_state.explanation_sections:
    if st.button("📄 Export Explanation to PDF"):
        download_pdf(st.session_state.explanation_sections)
        st.success("PDF exported successfully.")
