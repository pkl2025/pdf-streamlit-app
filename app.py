import streamlit as st

st.set_page_config(page_title="PDF Viewer", layout="wide")
st.title("📄 PDF Viewer - Embedded View")

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

# Tampilkan daftar PDF yang bisa dipilih
st.subheader("📚 Pilih PDF untuk ditampilkan")
selected_pdf = st.selectbox("Pilih file PDF:", pdf_files)

# Encode spasi dan buat URL
encoded_pdf = selected_pdf.replace(" ", "%20")
full_url = base_url + encoded_pdf

# Tampilkan PDF dengan iframe
st.subheader("📖 Tampilan PDF")
pdf_display = f"""
<iframe src="{full_url}" width="100%" height="800px" style="border: none;"></iframe>
"""
st.markdown(pdf_display, unsafe_allow_html=True)
