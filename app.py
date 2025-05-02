# https://drive.google.com/file/d/1YNxu_bLeftHjwAJGbczNZ6HGcRVqV8FQ/view?usp=sharing
# https://drive.google.com/file/d/1cT0Ndwustu_g0eIlW0IPrIkGoeIWYO7M/view?usp=sharing
import streamlit as st

st.set_page_config(page_title="Google Drive PDF Viewer", layout="wide")
st.title("📄 PDF Viewer dari Google Drive")

# Daftar file PDF dengan nama tampilannya dan ID Google Drive-nya
pdf_files = {
    "Modul 1": "1YNxu_bLeftHjwAJGbczNZ6HGcRVqV8FQ",
    "Modul 2": "1cT0Ndwustu_g0eIlW0IPrIkGoeIWYO7M",
}

# Pilih file dari dropdown
selected_title = st.selectbox("📚 Pilih PDF", list(pdf_files.keys()))
selected_file_id = pdf_files[selected_title]

# URL embed Google Drive
embed_url = f"https://drive.google.com/file/d/{selected_file_id}/preview"

# Tampilkan di iframe
st.subheader(f"📖 Menampilkan: {selected_title}")
st.components.v1.html(
    f"""
    <iframe src="{embed_url}" width="100%" height="800px" style="border:none;"></iframe>
    """,
    height=800,
)

