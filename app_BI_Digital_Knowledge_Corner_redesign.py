
import streamlit as st
import pandas as pd
from pathlib import Path
from datetime import datetime

# =========================================================
# BI DIGITAL KNOWLEDGE CORNER
# Prototype - bukan aplikasi resmi Bank Indonesia
# =========================================================

st.set_page_config(
    page_title="BI Digital Knowledge Corner",
    page_icon="🏦",
    layout="wide",
    initial_sidebar_state="expanded",
)

# -------------------------
# Theme / CSS
# -------------------------
st.markdown("""
<style>
    :root {
        --bi-blue: #0057A8;
        --bi-dark: #003B73;
        --bi-navy: #062B52;
        --bi-light: #EAF4FF;
        --bi-red: #E31E24;
        --text: #18324A;
        --muted: #63758A;
        --card: #FFFFFF;
        --border: #DCE7F2;
    }

    #MainMenu, footer {visibility: hidden;}

    .stApp {
        background: #F5F8FC;
        color: var(--text);
    }

    section[data-testid="stSidebar"] {
        background: linear-gradient(180deg, #003B73 0%, #0057A8 55%, #0875C9 100%);
        border-right: 0;
    }

    section[data-testid="stSidebar"] * {
        color: white !important;
    }

    section[data-testid="stSidebar"] .stRadio label {
        border-radius: 10px;
        padding: 8px 10px;
        transition: .2s ease;
    }

    section[data-testid="stSidebar"] .stRadio label:hover {
        background: rgba(255,255,255,.12);
    }

    .brand {
        padding: 6px 2px 18px 2px;
        border-bottom: 1px solid rgba(255,255,255,.20);
        margin-bottom: 18px;
    }

    .brand-mark {
        width: 46px;
        height: 46px;
        border-radius: 50%;
        display: inline-flex;
        align-items: center;
        justify-content: center;
        background: white;
        color: #0057A8;
        font-weight: 800;
        font-size: 17px;
        margin-bottom: 8px;
        box-shadow: 0 8px 20px rgba(0,0,0,.12);
    }

    .brand-title {
        font-size: 21px;
        font-weight: 800;
        line-height: 1.15;
    }

    .brand-subtitle {
        font-size: 12px;
        opacity: .82;
        margin-top: 5px;
        line-height: 1.4;
    }

    .hero {
        position: relative;
        overflow: hidden;
        padding: 42px 46px;
        border-radius: 24px;
        background:
            radial-gradient(circle at 85% 20%, rgba(255,255,255,.18), transparent 24%),
            linear-gradient(135deg, #003B73 0%, #0057A8 58%, #1185D4 100%);
        color: white;
        box-shadow: 0 16px 40px rgba(0,59,115,.16);
        margin-bottom: 28px;
    }

    .hero:after {
        content: "";
        position: absolute;
        width: 260px;
        height: 260px;
        border: 1px solid rgba(255,255,255,.13);
        border-radius: 50%;
        right: -75px;
        top: -90px;
    }

    .hero-kicker {
        font-size: 13px;
        font-weight: 700;
        letter-spacing: .08em;
        text-transform: uppercase;
        opacity: .88;
        margin-bottom: 10px;
    }

    .hero h1 {
        font-size: 42px;
        line-height: 1.08;
        margin: 0;
        color: white;
    }

    .hero p {
        font-size: 17px;
        line-height: 1.6;
        max-width: 760px;
        margin: 15px 0 0;
        color: rgba(255,255,255,.92);
    }

    .section-title {
        font-size: 27px;
        font-weight: 800;
        color: #123B60;
        margin: 8px 0 5px;
    }

    .section-subtitle {
        color: #6B7D90;
        margin-bottom: 18px;
    }

    .topic-card {
        background: white;
        border: 1px solid var(--border);
        border-radius: 18px;
        padding: 22px;
        min-height: 175px;
        box-shadow: 0 7px 24px rgba(30,70,110,.06);
        transition: transform .2s ease, box-shadow .2s ease;
    }

    .topic-card:hover {
        transform: translateY(-3px);
        box-shadow: 0 12px 30px rgba(30,70,110,.12);
    }

    .topic-icon {
        font-size: 30px;
        margin-bottom: 8px;
    }

    .topic-title {
        color: #064D87;
        font-size: 21px;
        font-weight: 800;
        margin-bottom: 7px;
    }

    .topic-desc {
        color: #607387;
        font-size: 14px;
        line-height: 1.55;
    }

    .quick-card {
        background: linear-gradient(180deg, #FFFFFF 0%, #F5FAFF 100%);
        border: 1px solid #D7E7F5;
        border-radius: 16px;
        padding: 20px;
        height: 100%;
    }

    .quick-icon {
        font-size: 25px;
    }

    .quick-title {
        font-weight: 800;
        color: #123B60;
        font-size: 17px;
        margin-top: 7px;
    }

    .quick-text {
        color: #6B7D90;
        font-size: 13px;
        line-height: 1.5;
        margin-top: 4px;
    }

    .info-strip {
        background: #EAF4FF;
        border: 1px solid #CFE4F8;
        border-left: 5px solid #0057A8;
        padding: 17px 20px;
        border-radius: 12px;
        color: #174B78;
        margin: 20px 0 28px;
    }

    .footer {
        margin-top: 45px;
        padding: 22px 0 10px;
        border-top: 1px solid #DCE7F2;
        color: #718297;
        font-size: 12px;
        line-height: 1.6;
    }

    .source-badge {
        display: inline-block;
        padding: 5px 9px;
        background: #EAF4FF;
        color: #0057A8;
        border-radius: 999px;
        font-size: 12px;
        font-weight: 700;
    }

    div.stButton > button {
        border-radius: 10px;
        border: 1px solid #C9DDED;
        font-weight: 700;
    }

    div.stButton > button:hover {
        border-color: #0057A8;
        color: #0057A8;
    }

    @media (max-width: 768px) {
        .hero { padding: 30px 24px; border-radius: 18px; }
        .hero h1 { font-size: 30px; }
        .hero p { font-size: 15px; }
        .section-title { font-size: 23px; }
    }
</style>
""", unsafe_allow_html=True)

# -------------------------
# Data
# -------------------------
TOPICS = {
    "Rupiah": {
        "icon": "💰",
        "desc": "Mengenal Rupiah, Cinta Bangga Paham Rupiah, dan pengelolaan uang Rupiah.",
        "detail": "Rupiah merupakan mata uang Republik Indonesia. Pada halaman ini, pengunjung diarahkan ke materi edukasi resmi mengenai Rupiah dan CBP Rupiah.",
        "url": "https://www.bi.go.id/id/rupiah/default.aspx",
    },
    "Sistem Pembayaran": {
        "icon": "💳",
        "desc": "Mengenal QRIS, BI-FAST, dan perkembangan sistem pembayaran Indonesia.",
        "detail": "Informasi pengantar mengenai sistem pembayaran, digitalisasi pembayaran, serta berbagai infrastruktur pembayaran yang diselenggarakan atau diatur Bank Indonesia.",
        "url": "https://www.bi.go.id/id/fungsi-utama/sistem-pembayaran/default.aspx",
    },
    "Stabilitas Ekonomi": {
        "icon": "📈",
        "desc": "Pengantar mengenai inflasi, moneter, nilai tukar, dan stabilitas ekonomi.",
        "detail": "Topik ini membantu pengunjung memahami hubungan kebijakan moneter, inflasi, nilai tukar, dan stabilitas ekonomi secara sederhana.",
        "url": "https://www.bi.go.id/id/fungsi-utama/moneter/default.aspx",
    },
    "Ketahanan Pangan": {
        "icon": "🌾",
        "desc": "Informasi dan edukasi mengenai pengendalian inflasi pangan serta sinergi daerah.",
        "detail": "Materi dapat dikembangkan dengan konten daerah, publikasi TPIP/TPID, dan sumber resmi terkait pengendalian inflasi pangan.",
        "url": "https://www.bi.go.id/id/fungsi-utama/moneter/pengendalian-inflasi/default.aspx",
    },
    "Data & Publikasi": {
        "icon": "📊",
        "desc": "Akses cepat menuju statistik, laporan, kajian, dan publikasi Bank Indonesia.",
        "detail": "Pengunjung dapat menggunakan Digital Knowledge Corner sebagai pintu masuk menuju data dan publikasi resmi BI.",
        "url": "https://www.bi.go.id/id/statistik/default.aspx",
    },
    "Kebanksentralan": {
        "icon": "🏦",
        "desc": "Mengenal fungsi, tugas, sejarah, dan peran Bank Indonesia sebagai bank sentral.",
        "detail": "Materi pengantar mengenai kelembagaan, fungsi utama, sejarah, dan peran Bank Indonesia.",
        "url": "https://www.bi.go.id/id/tentang-bi/default.aspx",
    },
}

LIBRARY_URL = "https://www.bi.go.id/id/bi-institute/Default.aspx"

# -------------------------
# Sidebar
# -------------------------
st.sidebar.markdown("""
<div class="brand">
    <div class="brand-mark">BI</div>
    <div class="brand-title">Digital Knowledge Corner</div>
    <div class="brand-subtitle">Akses cepat informasi kebanksentralan</div>
</div>
""", unsafe_allow_html=True)

menu = st.sidebar.radio(
    "Menu",
    ["🏠 Beranda", "🔎 Cari Informasi", "📚 Jelajah Topik",
     "📖 Perpustakaan BI", "📝 Feedback", "📊 Dashboard Evaluasi", "ℹ️ Tentang"],
)

st.sidebar.markdown("---")
st.sidebar.caption("Prototype untuk kebutuhan pengembangan dan pengujian. Bukan aplikasi resmi Bank Indonesia.")

# -------------------------
# Helper
# -------------------------
def footer():
    st.markdown("""
    <div class="footer">
        <b>BI Digital Knowledge Corner</b><br>
        Prototype media diseminasi informasi kebanksentralan berbasis web.<br>
        Konten dan tautan perlu diverifikasi serta disetujui sebelum digunakan sebagai layanan resmi.
    </div>
    """, unsafe_allow_html=True)

# -------------------------
# Beranda
# -------------------------
if menu == "🏠 Beranda":
    st.markdown("""
    <div class="hero">
        <div class="hero-kicker">Digital Knowledge Corner</div>
        <h1>Kenali Ekonomi,<br>Rupiah, dan Kebanksentralan.</h1>
        <p>
            Satu pintu akses untuk menemukan informasi kebanksentralan secara
            lebih ringkas, terarah, dan mudah dijelajahi.
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown('<div class="section-title">Jelajahi Informasi</div>', unsafe_allow_html=True)
    st.markdown('<div class="section-subtitle">Pilih topik yang ingin kamu kenali.</div>', unsafe_allow_html=True)

    cols = st.columns(3)
    for i, (name, item) in enumerate(TOPICS.items()):
        with cols[i % 3]:
            st.markdown(f"""
            <div class="topic-card">
                <div class="topic-icon">{item["icon"]}</div>
                <div class="topic-title">{name}</div>
                <div class="topic-desc">{item["desc"]}</div>
            </div>
            """, unsafe_allow_html=True)
            st.write("")
            if st.button(f"Pelajari {name}", key=f"home_{name}", use_container_width=True):
                st.session_state["selected_topic"] = name
                st.session_state["menu_target"] = "📚 Jelajah Topik"
                st.rerun()

    st.markdown('<div class="section-title" style="margin-top:28px;">Akses Cepat</div>', unsafe_allow_html=True)
    st.markdown('<div class="section-subtitle">Fitur utama untuk membantu perjalanan informasi pengunjung.</div>', unsafe_allow_html=True)

    qcols = st.columns(4)
    quick = [
        ("🔎", "Cari Informasi", "Temukan topik berdasarkan kata kunci."),
        ("📚", "Jelajah Topik", "Belajar berdasarkan kategori."),
        ("📖", "Perpustakaan BI", "Lanjutkan ke sumber literatur BI."),
        ("📝", "Berikan Feedback", "Bantu evaluasi dan pengembangan."),
    ]
    for c, (icon, title, text) in zip(qcols, quick):
        with c:
            st.markdown(f"""
            <div class="quick-card">
                <div class="quick-icon">{icon}</div>
                <div class="quick-title">{title}</div>
                <div class="quick-text">{text}</div>
            </div>
            """, unsafe_allow_html=True)

    st.markdown("""
    <div class="info-strip">
        <b>💡 Cara menggunakan:</b> pilih topik → baca ringkasan → buka sumber resmi →
        lanjutkan eksplorasi melalui Perpustakaan BI.
    </div>
    """, unsafe_allow_html=True)

    footer()

# -------------------------
# Cari
# -------------------------
elif menu == "🔎 Cari Informasi":
    st.markdown('<div class="section-title">🔎 Cari Informasi</div>', unsafe_allow_html=True)
    st.markdown('<div class="section-subtitle">Cari topik kebanksentralan dengan kata kunci sederhana.</div>', unsafe_allow_html=True)

    query = st.text_input("Masukkan kata kunci", placeholder="Contoh: QRIS, Rupiah, inflasi, BI-FAST...")
    if query:
        q = query.lower()
        results = [
            (name, item) for name, item in TOPICS.items()
            if q in name.lower() or q in item["desc"].lower() or q in item["detail"].lower()
        ]
        if results:
            for name, item in results:
                st.markdown(f"""
                <div class="topic-card">
                    <div class="topic-icon">{item["icon"]}</div>
                    <div class="topic-title">{name}</div>
                    <div class="topic-desc">{item["detail"]}</div>
                </div>
                """, unsafe_allow_html=True)
                st.write("")
                st.link_button("Buka sumber resmi BI", item["url"])
        else:
            st.info("Topik belum ditemukan. Coba kata kunci lain.")
    else:
        st.info("Masukkan kata kunci untuk memulai pencarian.")

    footer()

# -------------------------
# Jelajah Topik
# -------------------------
elif menu == "📚 Jelajah Topik":
    st.markdown('<div class="section-title">📚 Jelajah Topik</div>', unsafe_allow_html=True)
    st.markdown('<div class="section-subtitle">Pilih kategori untuk membaca ringkasan dan menuju sumber resmi.</div>', unsafe_allow_html=True)

    default_topic = st.session_state.get("selected_topic", list(TOPICS.keys())[0])
    topic = st.selectbox("Pilih topik", list(TOPICS.keys()), index=list(TOPICS.keys()).index(default_topic))

    item = TOPICS[topic]
    st.markdown(f"""
    <div class="hero" style="margin-top:18px;">
        <div class="hero-kicker">{item["icon"]} Topik Pilihan</div>
        <h1>{topic}</h1>
        <p>{item["detail"]}</p>
    </div>
    """, unsafe_allow_html=True)

    st.link_button("🌐 Buka sumber resmi Bank Indonesia", item["url"])
    st.markdown('<span class="source-badge">Sumber resmi</span>', unsafe_allow_html=True)

    footer()

# -------------------------
# Library
# -------------------------
elif menu == "📖 Perpustakaan BI":
    st.markdown('<div class="section-title">📖 Perpustakaan BI</div>', unsafe_allow_html=True)
    st.markdown('<div class="section-subtitle">Lanjutkan pencarian literatur dan sumber pengetahuan melalui kanal BI.</div>', unsafe_allow_html=True)

    st.markdown("""
    <div class="hero">
        <div class="hero-kicker">Knowledge & Literature</div>
        <h1>Temukan Literatur<br>dan Referensi BI.</h1>
        <p>
            Digital Knowledge Corner berfungsi sebagai pintu masuk informasi.
            Untuk penelusuran koleksi yang lebih mendalam, pengunjung dapat
            melanjutkan ke kanal Perpustakaan/BI Institute.
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.link_button("📚 Buka Perpustakaan / BI Institute", LIBRARY_URL)

    st.info("Catatan: tautan perpustakaan dapat diganti dengan URL katalog/aplikasi perpustakaan yang digunakan oleh unit BI setempat.")

    footer()

# -------------------------
# Feedback
# -------------------------
elif menu == "📝 Feedback":
    st.markdown('<div class="section-title">📝 Feedback Pengunjung</div>', unsafe_allow_html=True)
    st.markdown('<div class="section-subtitle">Pendapat pengunjung digunakan sebagai bahan evaluasi prototype.</div>', unsafe_allow_html=True)

    feedback_file = Path("data/feedback.csv")
    feedback_file.parent.mkdir(exist_ok=True)

    with st.form("feedback_form"):
        nama = st.text_input("Nama (opsional)")
        topik = st.selectbox("Topik yang paling menarik", list(TOPICS.keys()))
        kemudahan = st.slider("Kemudahan menggunakan website", 1, 5, 4)
        pencarian = st.slider("Kemudahan menemukan informasi", 1, 5, 4)
        pemahaman = st.slider("Kemudahan memahami informasi", 1, 5, 4)
        manfaat = st.slider("Manfaat website", 1, 5, 4)
        tampilan = st.slider("Tampilan website", 1, 5, 4)
        rekomendasi = st.slider("Kemungkinan merekomendasikan", 1, 5, 4)
        komentar = st.text_area("Saran atau komentar", placeholder="Apa yang perlu diperbaiki?")

        submitted = st.form_submit_button("Kirim Feedback", use_container_width=True)

    if submitted:
        row = pd.DataFrame([{
            "waktu": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "nama": nama,
            "topik": topik,
            "kemudahan": kemudahan,
            "kemudahan_mencari": pencarian,
            "kemudahan_memahami": pemahaman,
            "manfaat": manfaat,
            "tampilan": tampilan,
            "rekomendasi": rekomendasi,
            "komentar": komentar,
        }])

        if feedback_file.exists():
            old = pd.read_csv(feedback_file)
            new = pd.concat([old, row], ignore_index=True)
        else:
            new = row

        new.to_csv(feedback_file, index=False)
        st.success("Terima kasih. Feedback berhasil disimpan.")

    footer()

# -------------------------
# Dashboard
# -------------------------
elif menu == "📊 Dashboard Evaluasi":
    st.markdown('<div class="section-title">📊 Dashboard Evaluasi</div>', unsafe_allow_html=True)
    st.markdown('<div class="section-subtitle">Ringkasan feedback pengguna yang tersimpan pada aplikasi.</div>', unsafe_allow_html=True)

    feedback_file = Path("data/feedback.csv")
    if not feedback_file.exists():
        st.info("Belum ada data feedback. Silakan isi form Feedback terlebih dahulu.")
    else:
        df = pd.read_csv(feedback_file)

        numeric_cols = [
            "kemudahan", "kemudahan_mencari", "kemudahan_memahami",
            "manfaat", "tampilan", "rekomendasi"
        ]

        c1, c2, c3, c4 = st.columns(4)
        c1.metric("Responden", len(df))
        c2.metric("Rata-rata Manfaat", f"{df['manfaat'].mean():.2f}/5")
        c3.metric("Rata-rata Kemudahan", f"{df['kemudahan'].mean():.2f}/5")
        c4.metric("Rata-rata Tampilan", f"{df['tampilan'].mean():.2f}/5")

        st.markdown("### Rata-rata Penilaian")
        averages = df[numeric_cols].mean().sort_values(ascending=False)
        st.bar_chart(averages)

        st.markdown("### Topik yang Dipilih")
        st.bar_chart(df["topik"].value_counts())

        st.markdown("### Komentar Pengunjung")
        comments = df[df["komentar"].fillna("").astype(str).str.strip() != ""]
        if len(comments):
            st.dataframe(comments[["waktu", "topik", "komentar"]], use_container_width=True)
        else:
            st.info("Belum ada komentar.")

        st.download_button(
            "⬇️ Download Data Feedback (CSV)",
            df.to_csv(index=False).encode("utf-8"),
            "feedback.csv",
            "text/csv",
            use_container_width=True,
        )

    footer()

# -------------------------
# Tentang
# -------------------------
else:
    st.markdown('<div class="section-title">ℹ️ Tentang Digital Knowledge Corner</div>', unsafe_allow_html=True)
    st.markdown("""
    <div class="topic-card">
        <div class="topic-title">Apa itu Digital Knowledge Corner?</div>
        <div class="topic-desc">
            Digital Knowledge Corner adalah prototype media berbasis web yang dirancang
            sebagai pintu masuk cepat untuk menemukan informasi kebanksentralan.
            Konsep ini tidak menggantikan aplikasi perpustakaan, tetapi mengarahkan
            pengunjung dari topik populer menuju sumber dan literatur yang lebih lengkap.
        </div>
        <br>
        <div class="topic-desc">
            <b>Alur:</b> QR Code → Digital Knowledge Corner → Jelajah Topik →
            Sumber Resmi → Perpustakaan → Feedback → Evaluasi.
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="info-strip">
        <b>Catatan:</b> Aplikasi ini merupakan prototype untuk kebutuhan tugas akhir,
        pengujian, dan pengembangan. Nama, logo, identitas visual, konten, dan tautan
        resmi perlu mendapatkan persetujuan/validasi sebelum digunakan sebagai layanan resmi.
    </div>
    """, unsafe_allow_html=True)

    footer()
