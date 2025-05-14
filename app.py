import streamlit as st

st.set_page_config(page_title="File Viewer", layout="wide")
st.markdown(
    "<h1 style='text-align: center;'>📄 DMIA #2</h1>",
    unsafe_allow_html=True
)

# Daftar file PDF dan OneDrive embed link
pdf_files = {
    "Manual Book": "https://1drv.ms/b/c/07b3a549f2721615/IQRXg1J09mayT5PBNRPcxHdSAZoWwzcAionujvu6iI48e_k",
}

# Pilih file dari dropdown
selected_title = st.selectbox("📚 Pilih file", list(pdf_files.keys()))
embed_url = pdf_files[selected_title]

# Tampilkan di iframe dengan ukuran penuh dan terpusat
st.subheader(f"📖 Menampilkan: {selected_title}")
st.components.v1.html(
    f"""
    <div style="display: flex; justify-content: center;">
        <iframe src="{embed_url}" width="100%" height="800px" frameborder="0" style="border: none;" allowfullscreen></iframe>
    </div>
    """,
    height=800,
)
