import streamlit as st

st.set_page_config(page_title="PDF Viewer", layout="wide")
st.markdown(
    "<h1 style='text-align: center;'>📄 PDF Viewer</h1>",
    unsafe_allow_html=True
)

# Daftar file PDF dan link OneDrive yang sudah dikonversi
pdf_files = {
    "AgendaPKL": "https://onedrive.live.com/embed?resid=7B3A549F2721615%21135&authkey=!AEczkJm7jWlRFi9",
    "TestPCCR": "https://onedrive.live.com/embed?resid=7B3A549F2721615%21138&authkey=!Ad7lr_Ht_fBCp2r",
}

# Pilih file dari dropdown
selected_title = st.selectbox("📚 Pilih PDF", list(pdf_files.keys()))
embed_url = pdf_files[selected_title]

# Tampilkan di iframe yang dipusatkan
st.subheader(f"📖 Menampilkan: {selected_title}")
st.components.v1.html(
    f"""
    <div style="display: flex; justify-content: center;">
        <iframe src="{embed_url}" width="100%" height="800px" style="border:none;"></iframe>
    </div>
    """,
    height=800,
)
