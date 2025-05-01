import streamlit as st
import os

# Set page configuration
st.set_page_config(page_title="Sego Gampil Patitik", layout="wide")

# Load CSS
def load_css():
    with open("style.css") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

load_css()

# Header Section
st.markdown("<h1 style='text-align: center;'>Sego Gampil Patitik</h1>", unsafe_allow_html=True)
st.video("assets\Paket sego gampil 1.mp4")

# About Us Section
st.header("Tentang Produk")
st.write("""
    Sego Gampil Patitik merupakan hidangan tradisional khas Jawa yang kaya akan sejarah dan 
    cita rasa. Asal usulnya dapat ditelusuri kembali ke era kerajaan Mataram Islam, di mana 
    hidangan ini biasa disajikan untuk para bangsawan dan tamu istimewa. Seiring waktu, Sego 
    Gampil Patitik mulai dinikmati oleh masyarakat luas dan menjadi bagian dari budaya kuliner 
    Jawa yang digemari banyak orang.
""")

# Products Section
st.header("Produk Terbaru")
products = [
    {"name": "Paket sego gampil 1", "description": "Nasi + Telur + Es Teh/ Es Nutrisari", "price": "Rp. 15.000", "image": "assets/Paket sego gampil 1.webp"},
    {"name": "Paket sego gampil 2", "description": "Nasi + Ayam + Es Teh/ Es Nutrisari", "price": "Rp. 15.000", "image": "assets/Paket sego gampil 2.webp"},
    {"name": "Paket sego gampil 3", "description": "Nasi + Ayam + Es Teh/ Es Nutrisari", "price": "Rp. 15.000", "image": "assets/Paket sego gampil 3.webp"},
    {"name": "Patitik Ayam Asam Manis", "description": "Nasi + Ayam Asam Manis + Es Teh/ Es Nutrisari", "price": "Rp. 12.000", "image": "assets/patitik ayam asam manis.webp"},
    {"name": "Patitik Ayam Kari", "description": "Nasi + Ayam Kari + Es Teh/ Es Nutrisari", "price": "Rp. 12.000", "image": "assets/Patitik Ayam Kari.webp"},
    {"name": "Patitik Ayam Pedas Manis", "description": "Nasi + Ayam Pedas Manis + Es Teh/ Es Nutrisari", "price": "Rp. 12.000", "image": "assets/Patitik ayam pedas manis.webp"},
    {"name": "Patitik Ayam Sambal Matah", "description": "Nasi + Ayam Sambal Matah + Es Teh/ Es Nutrisari", "price": "Rp. 12.000", "image": "assets/Patitik ayam sambal matah.webp"},
    {"name": "Patitik Telur Asam Manis", "description": "Nasi + Telur Asam Manis + Es Teh/ Es Nutrisari", "price": "Rp. 10.000", "image": "assets/Patitik Telur Asam Manis.webp"},
    {"name": "Patitik Telur Kari", "description": "Nasi + Telur Kari + Es Teh/ Es Nutrisari", "price": "Rp. 40.000", "image": "assets/Patitik Telur Kari.webp"},
    {"name": "Patitik Telur Sambal Matah", "description": "Nasi + Telur Sambal Matah + Es Teh/ Es Nutrisari", "price": "Rp. 10.000", "image": "assets/Patitik Telur Sambal Matah.webp"},
    {"name": "Patitik Mix 2 Lauk", "description": "Nasi + Ayam + Telur + Es Teh/ Es Nutrisari", "price": "Rp. 17.000", "image": "assets/Patitik mix 2 lauk.webp"},
    {"name": "Patitik Mix 3 Lauk", "description": "Nasi + Ayam + Cumi + Telur + Es Teh/ Es Nutrisari", "price": "Rp. 20.000", "image": "assets/Patitik mix 3 lauk.webp"},
]

# Membuat kolom untuk menampilkan produk
num_columns = 3
cols = st.columns(num_columns)  # Membuat 3 kolom

for i, product in enumerate(products):
    with cols[i % num_columns]:  # Menggunakan modulus untuk mengatur produk ke dalam kolom
        st.image(product["image"], use_container_width=True)  # Menampilkan gambar produk
        st.subheader(product["name"])  # Menampilkan nama produk
        st.write(product["description"])  # Menampilkan deskripsi produk
        st.write(product["price"])  # Menampilkan harga produk
        if st.button("Tambahkan", key=product["name"]):
            st.success(f"{product['name']} telah ditambahkan ke keranjang.")


# Team Section
st.header("Our Team")
team_members = [
    {"name": "Dimas", "role": "Programmer", "image": "assets/tim2.jpg"},
    {"name": "Kevin", "role": "Marketing", "image": "assets/tim3.jpg"},
    {"name": "M Dimas", "role": "Owner", "image": "assets/tim4.jpg"},
]

# Membuat kolom untuk menampilkan anggota tim
cols = st.columns(3)  # Membuat 3 kolom

for i, member in enumerate(team_members):
    with cols[i % 3]:  # Menggunakan modulus untuk mengatur anggota tim ke dalam kolom
        st.image(member["image"], use_container_width=True)  # Menampilkan gambar anggota tim
        st.subheader(member["name"])  # Menampilkan nama anggota tim
        st.markdown(f"<h5 style='text-align: center;'>{member['role']}</h5>", unsafe_allow_html=True)  # Menampilkan peran anggota tim di tengah


# Contact Section
st.markdown("<h1 style='text-align: center;'>Contact</h1>", unsafe_allow_html=True)
st.markdown("<h6 style='text-align: center;'>Instagram: @sego.gampilpatitik</h6>", unsafe_allow_html=True)
st.markdown("<h6 style='text-align: center;'>WhatsApp: 081-234-567-890</h6>", unsafe_allow_html=True)
st.markdown("<h6 style='text-align: center;'>Email: segogampilpatitik@gmail.com</h6>", unsafe_allow_html=True)