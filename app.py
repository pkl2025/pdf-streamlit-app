import streamlit as st
import base64
import os

st.title("📄 PDF Viewer Online")

pdf_dir = "pdfs"
pdf_files = [f for f in os.listdir(pdf_dir) if f.endswith(".pdf")]

selected_pdf = st.selectbox("Pilih PDF:", pdf_files)

if selected_pdf:
    file_path = os.path.join(pdf_dir, selected_pdf)
    with open(file_path, "rb") as f:
        base64_pdf = base64.b64encode(f.read()).decode("utf-8")
        pdf_display = f'<iframe src="data:application/pdf;base64,{base64_pdf}" width="700" height="1000"></iframe>'
        st.markdown(pdf_display, unsafe_allow_html=True)
