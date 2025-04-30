import streamlit as st

st.set_page_config(page_title="PDF Viewer", layout="wide")
st.title("📄 PDF Viewer - Open in New Tab")

# Ganti ini dengan username dan nama repo kamu
GITHUB_USERNAME = "pkl2025"
GITHUB_REPO = "pdf-streamlit-app"
GITHUB_BRANCH = "main"  # biasanya 'main' atau 'master'

# Daftar file PDF yang ada di folder "pdfs" di GitHub
pdf_files = [
    "test1 - Copy (2).pdf",
    "test1 - Copy (3).pdf",
    "test1 - Copy (4).pdf",
    "test1 - Copy (5).pdf",
    "test1 - Copy.pdf",
    "test1.pdf"
]

# Base URL untuk raw PDF dari GitHub
base_url = f"https://raw.githubusercontent.com/{GITHUB_USERNAME}/{GITHUB_REPO}/{GITHUB_BRANCH}/pdfs/"

st.subheader("📚 Daftar PDF")
for pdf_file in pdf_files:
    full_url = base_url + pdf_file
    file_name_display = pdf_file.replace("-", " ").replace(".pdf", "").title()
    st.markdown(f'<a href="{full_url}" target="_blank">📄 {file_name_display}</a>', unsafe_allow_html=True)
