import streamlit as st

st.set_page_config(page_title="PDF Viewer", layout="wide")
st.title("📄 PDF Viewer - Open in New Tab")

# Username dan repo GitHub kamu
GITHUB_USERNAME = "pkl2025"
GITHUB_REPO = "pdf-streamlit-app"
GITHUB_BRANCH = "main"

# Daftar file PDF yang ada di folder "pdfs" di GitHub
pdf_files = [
    "test1 - Copy (2).pdf",
    "test1 - Copy (3).pdf",
    "test1 - Copy (4).pdf",
    "test1 - Copy (5).pdf",
    "test1 - Copy.pdf",
    "test1.pdf"
]

# URL dasar ke folder raw PDF di GitHub
base_url = f"https://raw.githubusercontent.com/{GITHUB_USERNAME}/{GITHUB_REPO}/{GITHUB_BRANCH}/pdfs/"

# Tampilkan daftar link ke PDF
st.subheader("📚 Daftar PDF")
for pdf_file in pdf_files:
    full_url = base_url + pdf_file.replace(" ", "%20")  # encode spasi untuk URL valid
    # Bersihkan nama file untuk ditampilkan
    display_name = pdf_file.replace(".pdf", "").replace("-", " ").replace("Copy", "").replace("(", "").replace(")", "").strip().title()
    st.markdown(
        f'<a href="{full_url}" target="_blank" style="text-decoration: none; font-size: 18px;">📄 {display_name}</a>',
        unsafe_allow_html=True
    )
