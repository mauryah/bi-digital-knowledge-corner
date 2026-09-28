import streamlit as st
import pandas as pd
from pathlib import Path
from datetime import datetime
import io

# ============================================================
# BI DIGITAL KNOWLEDGE CORNER
# Prototype Tugas Akhir Magang - Perpustakaan Bank Indonesia
# ============================================================

st.set_page_config(
    page_title="BI Digital Knowledge Corner",
    page_icon="🏦",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ---------------------------
# CSS
# ---------------------------
st.markdown("""
<style>
    .stApp { background: #f5f8fb; }

    .hero {
        padding: 2.5rem 2.7rem;
        border-radius: 22px;
        background: linear-gradient(135deg, #083b5c 0%, #176b87 100%);
        color: white;
        margin-bottom: 1.5rem;
    }
    .hero h1 { font-size: 2.5rem; margin-bottom: .5rem; }
    .hero p { font-size: 1.05rem; margin: 0; opacity: .94; }

    .section-title {
        color: #083b5c;
        margin-top: 1rem;
    }

    .topic-card {
        background: white;
        border: 1px solid #e4eaf0;
        border-radius: 18px;
        padding: 1.3rem;
        min-height: 180px;
        box-shadow: 0 4px 15px rgba(0,0,0,.04);
    }
    .topic-card h3 { color: #083b5c; }

    .info-box {
        background: #eef7fa;
        border-left: 5px solid #176b87;
        padding: 1rem 1.2rem;
        border-radius: 8px;
        margin: 1rem 0;
    }

    .small-note {
        color: #667085;
        font-size: .88rem;
    }

    .footer {
        text-align: center;
        color: #667085;
        padding: 2rem 0 1rem;
        font-size: .85rem;
    }

    [data-testid="stMetric"] {
        background: white;
        border: 1px solid #e4eaf0;
        border-radius: 14px;
        padding: 1rem;
    }
</style>
""", unsafe_allow_html=True)

# ---------------------------
# Data konten
# ---------------------------
TOPICS = {
    "💰 Rupiah": {
        "short": "Mengenal Rupiah, CBP Rupiah, dan penggunaan Rupiah.",
        "keywords": ["rupiah", "cbp", "cinta", "bangga", "paham", "uang"],
        "content": [
            "Cinta Rupiah berkaitan dengan mengenali, merawat, dan menggunakan Rupiah dengan baik.",
            "Bangga Rupiah menempatkan Rupiah sebagai simbol kedaulatan negara.",
            "Paham Rupiah mencakup pemahaman terhadap fungsi dan karakteristik Rupiah."
        ],
        "source": "https://www.bi.go.id/"
    },
    "💳 Sistem Pembayaran": {
        "short": "Mengenal QRIS, BI-FAST, dan perkembangan sistem pembayaran.",
        "keywords": ["qris", "bi-fast", "pembayaran", "digital", "transaksi"],
        "content": [
            "QRIS merupakan standar QR Code pembayaran yang dikembangkan untuk mendukung interoperabilitas pembayaran.",
            "BI-FAST merupakan infrastruktur pembayaran ritel yang mendukung transaksi secara cepat dan efisien.",
            "Literasi sistem pembayaran juga mencakup penggunaan layanan digital secara aman."
        ],
        "source": "https://www.bi.go.id/"
    },
    "📈 Stabilitas Ekonomi": {
        "short": "Pengantar mengenai inflasi, moneter, dan stabilitas ekonomi.",
        "keywords": ["inflasi", "moneter", "stabilitas", "ekonomi", "harga"],
        "content": [
            "Inflasi berkaitan dengan perubahan tingkat harga barang dan jasa secara umum.",
            "Kebijakan moneter merupakan salah satu instrumen dalam kerangka menjaga stabilitas ekonomi.",
            "Data ekonomi perlu dibaca berdasarkan periode dan sumber resmi."
        ],
        "source": "https://www.bi.go.id/"
    },
    "🌾 Ketahanan Pangan": {
        "short": "Hubungan ketahanan pangan, harga pangan, dan stabilitas ekonomi.",
        "keywords": ["pangan", "gnpip", "harga pangan", "pasokan"],
        "content": [
            "Ketersediaan pasokan dan kelancaran distribusi berhubungan dengan stabilitas harga pangan.",
            "Pengendalian inflasi pangan membutuhkan sinergi lintas pihak.",
            "Materi wilayah dapat ditambahkan sesuai program Bank Indonesia setempat."
        ],
        "source": "https://www.bi.go.id/"
    },
    "📊 Data & Publikasi": {
        "short": "Pintu masuk ke statistik, laporan, kajian, dan publikasi BI.",
        "keywords": ["data", "statistik", "publikasi", "laporan", "kajian"],
        "content": [
            "Statistik ekonomi dan keuangan dapat digunakan untuk memahami perkembangan ekonomi.",
            "Publikasi BI menyediakan informasi, kajian, dan analisis ekonomi serta kebanksentralan.",
            "Gunakan periode dan definisi indikator yang tepat ketika membaca data."
        ],
        "source": "https://www.bi.go.id/"
    },
    "🏦 Kebanksentralan": {
        "short": "Mengenal fungsi, tugas, dan isu utama kebanksentralan.",
        "keywords": ["kebanksentralan", "bank indonesia", "moneter", "makroprudensial"],
        "content": [
            "Topik kebanksentralan dapat dipelajari melalui sumber resmi Bank Indonesia.",
            "Informasi dapat dikelompokkan berdasarkan kebijakan moneter, makroprudensial, dan sistem pembayaran.",
            "Halaman ini merupakan pengantar sebelum pengguna membaca sumber yang lebih lengkap."
        ],
        "source": "https://www.bi.go.id/"
    }
}

# ---------------------------
# Feedback storage
# ---------------------------
DATA_DIR = Path("data")
DATA_DIR.mkdir(exist_ok=True)
FEEDBACK_FILE = DATA_DIR / "feedback.csv"

def save_feedback(row):
    df_new = pd.DataFrame([row])
    if FEEDBACK_FILE.exists():
        df_old = pd.read_csv(FEEDBACK_FILE)
        df = pd.concat([df_old, df_new], ignore_index=True)
    else:
        df = df_new
    df.to_csv(FEEDBACK_FILE, index=False)

def load_feedback():
    if FEEDBACK_FILE.exists():
        return pd.read_csv(FEEDBACK_FILE)
    return pd.DataFrame()

# ---------------------------
# Sidebar
# ---------------------------
st.sidebar.title("🏦 BI Knowledge Corner")
st.sidebar.caption("Prototype Digital Knowledge Corner")

menu = st.sidebar.radio(
    "Menu",
    [
        "🏠 Beranda",
        "🔎 Cari Informasi",
        "📚 Jelajah Topik",
        "📖 Perpustakaan BI",
        "📝 Feedback",
        "📊 Dashboard Evaluasi",
        "ℹ️ Tentang"
    ]
)

# ---------------------------
# Beranda
# ---------------------------
if menu == "🏠 Beranda":
    st.markdown("""
    <div class="hero">
        <h1>BI Digital Knowledge Corner</h1>
        <p>
        Satu pintu akses untuk mengenal ekonomi, Rupiah,
        sistem pembayaran, dan kebanksentralan.
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.subheader("🎯 Jelajahi Informasi")

    cols = st.columns(3)
    for i, (topic, data) in enumerate(TOPICS.items()):
        with cols[i % 3]:
            st.markdown(f"""
            <div class="topic-card">
                <h3>{topic}</h3>
                <p>{data['short']}</p>
            </div>
            """, unsafe_allow_html=True)

    st.divider()
    st.subheader("Mengapa Digital Knowledge Corner?")
    st.markdown("""
    <div class="info-box">
    Website ini dirancang sebagai <b>quick access point</b> untuk membantu
    pengunjung menemukan informasi kebanksentralan secara lebih terarah,
    ringkas, dan mudah diakses. Website tidak menggantikan aplikasi
    perpustakaan yang telah tersedia.
    </div>
    """, unsafe_allow_html=True)

    c1, c2, c3 = st.columns(3)
    with c1:
        st.metric("Topik", len(TOPICS))
    with c2:
        st.metric("Media", "Digital")
    with c3:
        st.metric("Fokus", "Literasi")

# ---------------------------
# Search
# ---------------------------
elif menu == "🔎 Cari Informasi":
    st.title("🔎 Cari Informasi")
    q = st.text_input(
        "Ketik kata kunci",
        placeholder="Contoh: QRIS, Rupiah, inflasi, BI-FAST..."
    ).strip().lower()

    if q:
        results = []
        for topic, data in TOPICS.items():
            text = " ".join([
                topic,
                data["short"],
                " ".join(data["keywords"]),
                " ".join(data["content"])
            ]).lower()
            if q in text:
                results.append((topic, data))

        if results:
            st.success(f"{len(results)} topik ditemukan.")
            for topic, data in results:
                with st.expander(topic, expanded=True):
                    st.write(data["short"])
                    for x in data["content"]:
                        st.markdown(f"- {x}")
                    st.link_button("Buka sumber resmi BI", data["source"])
        else:
            st.warning("Belum ditemukan. Coba kata kunci lain.")

# ---------------------------
# Browse
# ---------------------------
elif menu == "📚 Jelajah Topik":
    st.title("📚 Jelajah Topik")
    selected = st.selectbox("Pilih topik", list(TOPICS.keys()))
    data = TOPICS[selected]

    st.subheader(selected)
    st.write(data["short"])

    st.markdown("### Materi Pengantar")
    for x in data["content"]:
        st.markdown(f"- {x}")

    st.markdown("### 🔗 Sumber Resmi")
    st.link_button("Bank Indonesia", data["source"])

# ---------------------------
# Library
# ---------------------------
elif menu == "📖 Perpustakaan BI":
    st.title("📖 Perpustakaan Bank Indonesia")

    st.markdown("""
    <div class="info-box">
    <b>Digital Knowledge Corner bukan pengganti aplikasi perpustakaan.</b>
    Fungsinya adalah menjadi pintu masuk informasi dan mengarahkan pengguna
    ke sumber/koleksi yang lebih lengkap.
    </div>
    """, unsafe_allow_html=True)

    st.write("Silakan hubungkan tombol di bawah dengan URL aplikasi/katalog perpustakaan BI yang sebenarnya.")

    LIBRARY_URL = "https://www.bi.go.id/"
    st.link_button("📚 Buka Aplikasi/Katalog Perpustakaan BI", LIBRARY_URL)

    st.caption("Ganti LIBRARY_URL di kode setelah memperoleh URL resmi dari unit terkait.")

# ---------------------------
# Feedback
# ---------------------------
elif menu == "📝 Feedback":
    st.title("📝 Evaluasi Pengguna")
    st.write("Form ini digunakan untuk mengukur pengalaman pengguna setelah mencoba prototype.")

    with st.form("feedback"):
        role = st.selectbox(
            "Kategori pengguna",
            ["Mahasiswa", "Pelajar", "Pegawai", "Umum", "Lainnya"]
        )

        topic = st.selectbox(
            "Topik yang paling menarik",
            list(TOPICS.keys())
        )

        ease = st.slider("Website mudah digunakan", 1, 5, 4)
        find_info = st.slider("Informasi mudah ditemukan", 1, 5, 4)
        understand = st.slider("Informasi mudah dipahami", 1, 5, 4)
        useful = st.slider("Website bermanfaat", 1, 5, 4)
        appearance = st.slider("Tampilan mudah dipahami", 1, 5, 4)
        recommendation = st.slider("Saya bersedia merekomendasikan website ini", 1, 5, 4)

        comment = st.text_area("Saran/komentar")

        submit = st.form_submit_button("Kirim Feedback")

    if submit:
        row = {
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "kategori_pengguna": role,
            "topik_menarik": topic,
            "kemudahan": ease,
            "kemudahan_mencari": find_info,
            "kemudahan_memahami": understand,
            "manfaat": useful,
            "tampilan": appearance,
            "rekomendasi": recommendation,
            "komentar": comment
        }
        save_feedback(row)
        st.success("Feedback berhasil disimpan.")
        st.balloons()

# ---------------------------
# Dashboard
# ---------------------------
elif menu == "📊 Dashboard Evaluasi":
    st.title("📊 Dashboard Evaluasi")

    df = load_feedback()

    if df.empty:
        st.info("Belum ada data feedback. Lakukan uji coba terlebih dahulu.")
    else:
        metric_cols = [
            "kemudahan",
            "kemudahan_mencari",
            "kemudahan_memahami",
            "manfaat",
            "tampilan",
            "rekomendasi"
        ]

        means = df[metric_cols].mean()

        c1, c2, c3 = st.columns(3)
        with c1:
            st.metric("Jumlah Responden", len(df))
        with c2:
            st.metric("Rata-rata Kemudahan", f"{means['kemudahan']:.2f}/5")
        with c3:
            st.metric("Rata-rata Manfaat", f"{means['manfaat']:.2f}/5")

        st.subheader("📌 Rata-rata Penilaian")
        chart = means.rename({
            "kemudahan": "Kemudahan",
            "kemudahan_mencari": "Pencarian",
            "kemudahan_memahami": "Pemahaman",
            "manfaat": "Manfaat",
            "tampilan": "Tampilan",
            "rekomendasi": "Rekomendasi"
        })
        st.bar_chart(chart)

        st.subheader("👥 Distribusi Pengguna")
        st.bar_chart(df["kategori_pengguna"].value_counts())

        st.subheader("🔥 Topik yang Paling Menarik")
        st.bar_chart(df["topik_menarik"].value_counts())

        st.subheader("💬 Feedback Pengguna")
        if "komentar" in df.columns:
            comments = df[df["komentar"].fillna("").astype(str).str.strip() != ""]
            if comments.empty:
                st.write("Belum ada komentar.")
            else:
                for _, row in comments.iterrows():
                    st.write(f"**{row['kategori_pengguna']}** — {row['komentar']}")

        csv = df.to_csv(index=False).encode("utf-8")
        st.download_button(
            "⬇️ Download Data Feedback (CSV)",
            data=csv,
            file_name="feedback_digital_knowledge_corner.csv",
            mime="text/csv"
        )

# ---------------------------
# About
# ---------------------------
elif menu == "ℹ️ Tentang":
    st.title("ℹ️ Tentang Prototype")

    st.markdown("""
    ### Tujuan
    Digital Knowledge Corner dikembangkan sebagai prototype media pendukung
    diseminasi informasi kebanksentralan di lingkungan perpustakaan.

    ### Konsep
    **Koleksi → Kurasi → Akses Digital → Pemahaman → Eksplorasi**

    ### Batasan
    Prototype ini bukan aplikasi resmi Bank Indonesia dan tidak menggantikan
    sistem perpustakaan yang telah tersedia. Konten dan tautan harus diverifikasi
    sebelum digunakan secara resmi.

    ### Konsep evaluasi
    Pengguna mencoba website → memberikan penilaian → data disimpan → dashboard
    menampilkan hasil → hasil digunakan sebagai bahan evaluasi dan makalah.
    """)

st.markdown("""
<div class="footer">
BI Digital Knowledge Corner — Prototype Tugas Akhir Magang<br>
Media pendukung diseminasi informasi kebanksentralan
</div>
""", unsafe_allow_html=True)
