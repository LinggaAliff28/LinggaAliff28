import streamlit as st
import base64
import os

# Data profile
PROFILE = {
    "name": "Lingga Aliffansyah",
    "role": "Cybersecurity, Network and IoT Engineer",
    "location": "Ciparay, Kab.Bandung, Indonesia",
    "socials": {
        "Instagram": "https://www.instagram.com/lingga_aliffansyah?igsh=MXU1aDIybWhtOHU1Ng==",
        "LinkedIn": "https://www.linkedin.com/in/lingga-aliff-431702376/",
    },
    "experience": [
        {
            "role": "Asisten Praktikum Cloud Computing",
            "company": "Telkom University",
            "year": "2024-2025",
            "desc": "Membimbing mahasiswa dalam memahami konsep dasar dan implementasi layanan cloud computing (IaaS, PaaS, SaaS). Memberikan arahan penggunaan platform cloud seperti AWS, Google Cloud, atau Azure untuk kebutuhan praktikum. Membantu dalam troubleshooting, debugging, serta optimalisasi infrastruktur cloud mahasiswa. Serta berkontribusi dalam penyusunan modul praktikum dan evaluasi hasil praktikan.",
        },
        {
            "role": "Asisten Algoritma dan bengkel pemograman",
            "company": "Telkom University",
            "year": "2024-2025",
            "desc": "Membantu mahasiswa dalam memahami konsep dasar algoritma, struktur data, serta implementasinya menggunakan bahasa pemrograman (C/Python). Membimbing praktikum pemecahan masalah, logika pemrograman, dan efisiensi algoritma. Memberikan umpan balik dan membantu debugging kode program mahasiswa. Serta Berperan aktif dalam evaluasi dan pengembangan modul praktikum.",
        },
        {
            "role": "Intern - Hardware Engineer",
            "company": "Telkom University",
            "year": "2025",
            "desc": "Terlibat dalam perancangan, pengujian, dan analisis rangkaian elektronik berbasis mikrokontroler. Membantu proses debugging dan troubleshooting perangkat keras untuk memastikan sistem berjalan stabil. Melakukan dokumentasi hasil uji coba, analisis performa, dan perbaikan hardware. Mendukung tim dalam integrasi perangkat keras dengan sistem IoT dan jaringan telekomunikasi. Berkontribusi pada penelitian dan pengembangan (R&D) untuk meningkatkan kinerja perangkat.",
        },
    ],
    "projects": [
        {
            "title": "Radio FM RDS",
            "year": "2025",
            "tags": ["IoT", "Raspberry Pi", "FM Radio"],
            "desc": "Proyek ini merupakan implementasi sistem Radio FM dengan layanan Radio Data System (RDS) menggunakan Raspberry Pi sebagai pemancar (transmitter) dan ESP32 sebagai penerima (receiver). Raspberry Pi diprogram untuk menghasilkan sinyal audio yang disisipkan dengan data RDS (seperti judul lagu, nama stasiun, atau informasi tambahan), kemudian dipancarkan melalui modulasi FM. Di sisi penerima, ESP32 digunakan untuk menangkap sinyal FM sekaligus membaca data RDS yang terkandung di dalamnya. Hasil decoding dari ESP32 dapat ditampilkan pada layar LCD/OLED, atau dikirim melalui komunikasi serial ke komputer/antarmuka monitoring.",
            "images": ["pengujian 2.JPG", "pengujian 1.JPG"],
        },
    ],
    "contact": {
        "name": "Lingga Aliffansyah",
        "email": "linggaalifansyah2003@gmail.com",
        "phone number": "085643788546",
        "message": "Halo, saya tertarik bekerja sama dalam pengembangan IoT.",
    }
}

# 🔹 Daftar file sertifikat (JPG format) di folder assets
CERTIFICATES = [
    "sertifikat_asprak1.JPG",
    "sertifikat_asprak2.JPG",
    "sertifikat_asprak3.JPG",
    "sertifikat_cisco1.JPG",
    "sertifikat_cisco2.JPG",
    "sertifikat magang.JPG",
]

# Sidebar
with st.sidebar:
    st.image("assets/foto buat ijazah.jpg", caption=PROFILE["name"], use_container_width=True)
    st.markdown(f"### {PROFILE['name']}")
    st.markdown(f"**{PROFILE['role']}**")
    st.caption(f"📍 {PROFILE['location']}")

    st.markdown("---")
    st.markdown("#### 🌐 Social")
    for label, url in PROFILE["socials"].items():
        st.markdown(f"- [{label}]({url})")

# Main content
st.title("💼 Portofolio Saya")
st.write("Selamat datang di portofolio online saya!")
st.write("Saya Lingga Aliffansyah, Ahli Madya Teknik Telekomunikasi Telkom University tahun 2025. Aktivitas terakhir saat ini aktif sebagai pencari kerja dan selama kuliah menguasai ilmu telekomunikasi seperti Fiber Optik, Algoritma Pemograman, Cloud Computing, Internet of Things, Jaringan Telekomunikasi, Elektronika Telekomunikasi dan Cyber Security. ")

# Bagian Skills
st.header("🔧 Keterampilan")

skills = {
    "Cybersecurity": {"level": 0.8, "icon": "🛡️"},
    "IoT & Embedded System": {"level": 0.85, "icon": "📡"},
    "Networking": {"level": 0.75, "icon": "🌐"},
    "Cloud Computing": {"level": 0.8, "icon": "☁️"},
    "Programming (Python, C, JS)": {"level": 0.75, "icon": "💻"},
    "Hardware Engineering": {"level": 0.90, "icon": "🔩"},
}

for skill, data in skills.items():
    st.write(f"{data['icon']} **{skill}**")
    st.progress(data["level"])
st.markdown("---")

# Bagian Experience
st.header("👨‍💻 Pengalaman")
for exp in PROFILE["experience"]:
    st.subheader(f"{exp['role']} - {exp['company']}")
    st.caption(exp['year'])
    st.write(exp['desc'])
    st.markdown("---")

# Bagian Proyek
st.header("📂 Proyek")
for p in PROFILE["projects"]:
    st.subheader(f"{p['title']} ({p['year']})")

    if "images" in p:
        for img in p["images"]:
            st.image(f"assets/{img}", use_container_width=True)
    elif "image" in p:
        st.image(f"assets/{p['image']}", use_container_width=True)

    st.write(f"**Tags:** {', '.join(p['tags'])}")
    st.write(p["desc"])
    st.markdown("---")

# Bagian Sertifikat (format JPG)
st.header("📑 Sertifikat Saya")
st.write("Berikut sertifikat resmi saya:")

if CERTIFICATES:
    for i, cert in enumerate(CERTIFICATES, start=1):
        path = f"assets/{cert}"
        if os.path.exists(path):
            st.subheader(f"Sertifikat {i}")
            st.image(path, use_container_width=True)

            with open(path, "rb") as img_file:
                st.download_button(
                    label=f"⬇️ Download Sertifikat {i}",
                    data=img_file,
                    file_name=f"sertifikat_{i}.jpg",
                    mime="image/jpeg"
                )
            st.markdown("---")
        else:
            st.warning(f"⚠️ File {cert} tidak ditemukan.")
else:
    st.info("Belum ada file sertifikat ditemukan.")

# Bagian Kontak
st.header("📞 Kontak")
contact = PROFILE["contact"]

st.write(f"**Nama:** {contact['name']}")
st.write(f"**Email:** {contact['email']}")
st.write(f"**Phone Number:** {contact['phone number']}")
st.write(f"**Pesan:** {contact['message']}")

