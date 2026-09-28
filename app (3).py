import streamlit as st
import pandas as pd
from pathlib import Path
from datetime import datetime
import re

# ============================================================
# BI DIGITAL KNOWLEDGE CORNER
# FINAL MODERN LANDING PAGE
# Prototype Tugas Akhir Magang - Perpustakaan Bank Indonesia
# ============================================================

st.set_page_config(
    page_title="BI Digital Knowledge Corner",
    page_icon="🏦",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ============================================================
# CONFIG
# ============================================================

BI_URL = "https://www.bi.go.id/"
LIBRARY_URL = "https://web-ibilibrary.moco.co.id/"

DATA_DIR = Path("data")
DATA_DIR.mkdir(exist_ok=True)

FEEDBACK_FILE = DATA_DIR / "feedback.csv"
USAGE_FILE = DATA_DIR / "usage.csv"

# ============================================================
# CUSTOM CSS
# ============================================================

st.markdown("""
<style>
/* ---------- GLOBAL ---------- */
.stApp {
    background: #f4f8fc;
}

.main .block-container {
    max-width: 1380px;
    padding-top: 1.25rem;
    padding-bottom: 2.5rem;
}

section[data-testid="stSidebar"] {
    background: #ffffff;
    border-right: 1px solid #e6edf4;
}

section[data-testid="stSidebar"] > div {
    padding-top: 1.5rem;
}

/* ---------- SIDEBAR ---------- */
.sidebar-brand {
    padding: 0.35rem 0.3rem 1.1rem 0.3rem;
}

.sidebar-brand .bi-mark {
    width: 46px;
    height: 46px;
    border-radius: 50%;
    background: linear-gradient(145deg,#073f70,#0d7ca7);
    color: white;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 1.35rem;
    font-weight: 800;
    margin-bottom: .75rem;
}

.sidebar-brand h2 {
    color: #073f70;
    font-size: 1.35rem;
    line-height: 1.2;
    margin: 0;
    font-weight: 800;
}

.sidebar-brand p {
    color: #7a8795;
    font-size: .82rem;
    margin: .45rem 0 0 0;
}

/* ---------- TOP BAR ---------- */
.topbar {
    display: flex;
    justify-content: flex-end;
    align-items: center;
    margin-bottom: .5rem;
}

.prototype-pill {
    background: #e7f2fb;
    color: #124f7e;
    border-radius: 999px;
    padding: .45rem .85rem;
    font-size: .76rem;
    font-weight: 700;
}

/* ---------- HERO ---------- */
.hero {
    position: relative;
    overflow: hidden;
    min-height: 425px;
    border-radius: 28px;
    padding: 3.2rem 3.4rem;
    background:
        radial-gradient(circle at 82% 25%, rgba(91,205,235,.35), transparent 24%),
        radial-gradient(circle at 95% 85%, rgba(19,119,168,.35), transparent 30%),
        linear-gradient(118deg, #063c68 0%, #075d8d 53%, #1285aa 100%);
    color: white;
    box-shadow: 0 18px 45px rgba(10,73,112,.17);
}

.hero:after {
    content: "";
    position: absolute;
    width: 430px;
    height: 430px;
    right: -110px;
    bottom: -190px;
    border-radius: 50%;
    border: 1px solid rgba(255,255,255,.18);
    box-shadow:
        0 0 0 38px rgba(255,255,255,.04),
        0 0 0 76px rgba(255,255,255,.025);
}

.hero-content {
    position: relative;
    z-index: 2;
    max-width: 760px;
}

.eyebrow {
    font-size: .76rem;
    font-weight: 800;
    letter-spacing: .16em;
    opacity: .78;
    margin-bottom: .75rem;
}

.hero h1 {
    font-size: clamp(2.25rem, 4.2vw, 4rem);
    line-height: 1.04;
    margin: 0;
    font-weight: 850;
    letter-spacing: -.03em;
}

.hero .tagline {
    font-size: 1.3rem;
    font-weight: 750;
    margin: 1rem 0 .55rem;
}

.hero p {
    font-size: 1rem;
    line-height: 1.7;
    max-width: 760px;
    margin: 0;
    color: rgba(255,255,255,.92);
}

/* decorative skyline */
.skyline {
    position: absolute;
    right: 3.3rem;
    bottom: 0;
    width: 370px;
    height: 260px;
    opacity: .92;
    z-index: 1;
}

.building {
    position: absolute;
    bottom: 0;
    background: linear-gradient(180deg, rgba(235,249,255,.95), rgba(174,218,235,.75));
    border-radius: 5px 5px 0 0;
    box-shadow: 0 0 25px rgba(0,0,0,.08);
}

.building:before {
    content: "";
    position: absolute;
    inset: 18px 12px 12px;
    background:
        repeating-linear-gradient(
            to bottom,
            rgba(17,88,128,.26) 0 7px,
            transparent 7px 17px
        ),
        repeating-linear-gradient(
            to right,
            rgba(17,88,128,.20) 0 7px,
            transparent 7px 17px
        );
}

.b1 { left: 8px; width: 95px; height: 155px; }
.b2 { left: 92px; width: 75px; height: 205px; }
.b3 { left: 156px; width: 135px; height: 240px; background: linear-gradient(180deg,#f4fbff,#b6d9e7); }
.b4 { right: 8px; width: 70px; height: 175px; }

.bi-sign {
    position: absolute;
    z-index: 5;
    left: 194px;
    bottom: 137px;
    width: 60px;
    height: 60px;
    border-radius: 50%;
    background: #0a5481;
    border: 3px solid white;
    display: flex;
    align-items: center;
    justify-content: center;
    color: white;
    font-weight: 900;
    font-size: 1.25rem;
    box-shadow: 0 8px 20px rgba(0,0,0,.18);
}

/* ---------- SEARCH ---------- */
.search-wrap {
    position: relative;
    z-index: 5;
    margin-top: 1.5rem;
    max-width: 760px;
}

/* ---------- QUICK BENEFITS ---------- */
.quick-strip {
    margin-top: -1.9rem;
    position: relative;
    z-index: 8;
    background: rgba(255,255,255,.94);
    border: 1px solid #dbe7f0;
    border-radius: 17px;
    box-shadow: 0 10px 30px rgba(16,65,95,.11);
    padding: .75rem 1rem;
}

.quick-item {
    display: flex;
    gap: .65rem;
    align-items: center;
    min-height: 54px;
    color: #123f60;
}

.quick-item .icon {
    font-size: 1.45rem;
}

.quick-item b {
    display: block;
    font-size: .82rem;
}

.quick-item span {
    color: #758391;
    font-size: .72rem;
}

/* ---------- SECTIONS ---------- */
.section-heading {
    margin: 2rem 0 .25rem;
    color: #073f70;
    font-size: 1.55rem;
    font-weight: 850;
}

.section-sub {
    color: #71808e;
    margin-bottom: 1rem;
}

/* ---------- TOPIC CARDS ---------- */
.topic-card {
    background: #fff;
    border: 1px solid #e2ebf3;
    border-radius: 20px;
    padding: 1.15rem;
    min-height: 220px;
    box-shadow: 0 6px 20px rgba(18,67,98,.045);
    transition: transform .2s ease, box-shadow .2s ease;
}

.topic-card:hover {
    transform: translateY(-2px);
    box-shadow: 0 10px 28px rgba(18,67,98,.09);
}

.topic-art {
    height: 76px;
    border-radius: 15px;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 2.35rem;
    margin-bottom: .85rem;
}

.topic-card h3 {
    margin: 0 0 .35rem;
    color: #073f70;
    font-size: 1.08rem;
}

.topic-card p {
    margin: 0;
    color: #687785;
    font-size: .84rem;
    line-height: 1.5;
    min-height: 52px;
}

/* ---------- INFO PANELS ---------- */
.panel {
    background: white;
    border: 1px solid #e2ebf3;
    border-radius: 20px;
    padding: 1.35rem 1.45rem;
    min-height: 165px;
    box-shadow: 0 5px 18px rgba(18,67,98,.045);
}

.panel h3 {
    color: #073f70;
    margin-top: 0;
}

.panel p {
    color: #667684;
    line-height: 1.55;
    font-size: .9rem;
}

.fact-panel {
    background: linear-gradient(135deg,#eaf5ff,#f7fbff);
}

.library-panel {
    background: linear-gradient(135deg,#e8f7f7,#f8ffff);
}

.how-panel {
    background: linear-gradient(135deg,#edf5ff,#f9fbff);
}

/* ---------- BUTTONS ---------- */
div.stButton > button,
div[data-testid="stLinkButton"] > a {
    border-radius: 11px !important;
    font-weight: 750 !important;
    min-height: 2.7rem !important;
}

.primary-btn {
    margin-top: .2rem;
}

/* ---------- FOOTER ---------- */
.footer {
    margin-top: 2.5rem;
    padding: 1.4rem 0 .5rem;
    border-top: 1px solid #dfe8ef;
    color: #7a8792;
    text-align: center;
    font-size: .78rem;
    line-height: 1.6;
}

/* ---------- MOBILE ---------- */
@media (max-width: 900px) {
    .hero {
        padding: 2.2rem 1.5rem;
        min-height: 480px;
    }

    .skyline {
        right: 50%;
        transform: translateX(50%);
        width: 310px;
        opacity: .48;
    }

    .hero-content {
        max-width: 100%;
    }

    .quick-strip {
        margin-top: 1rem;
    }
}
</style>
""", unsafe_allow_html=True)

# ============================================================
# DATA
# ============================================================

TOPICS = {
    "💰 Rupiah": {
        "short": "Mengenal Rupiah sebagai alat pembayaran dan simbol kedaulatan negara.",
        "intro": "Rupiah merupakan mata uang negara Indonesia. Pelajari fungsi, karakteristik, dan pentingnya Rupiah dalam kehidupan sehari-hari.",
        "fact": "Rupiah bukan hanya alat pembayaran, tetapi juga merupakan simbol kedaulatan negara.",
        "keywords": ["rupiah", "uang", "cbp", "cinta", "bangga", "paham"],
        "content": [
            "Cinta Rupiah berkaitan dengan mengenali, merawat, dan menggunakan Rupiah dengan baik.",
            "Bangga Rupiah menempatkan Rupiah sebagai salah satu simbol identitas dan kedaulatan negara.",
            "Paham Rupiah mencakup pemahaman terhadap fungsi, karakteristik, dan penggunaan Rupiah."
        ],
        "icon_bg": "#e9f4ff",
        "source": BI_URL
    },
    "💳 Sistem Pembayaran": {
        "short": "Mengenal QRIS, BI-FAST, dan perkembangan sistem pembayaran Indonesia.",
        "intro": "Sistem pembayaran merupakan bagian penting dari aktivitas ekonomi. Kenali berbagai layanan dan infrastruktur pembayaran.",
        "fact": "QRIS dikembangkan untuk mendukung interoperabilitas pembayaran berbasis QR.",
        "keywords": ["qris", "bi-fast", "pembayaran", "digital", "transaksi"],
        "content": [
            "QRIS merupakan standar QR Code pembayaran yang dikembangkan untuk mendukung interoperabilitas pembayaran.",
            "BI-FAST merupakan infrastruktur pembayaran ritel yang mendukung transaksi secara cepat dan efisien.",
            "Literasi sistem pembayaran juga mencakup penggunaan layanan digital secara aman."
        ],
        "icon_bg": "#fff1e7",
        "source": BI_URL
    },
    "📈 Stabilitas Ekonomi": {
        "short": "Memahami inflasi, kebijakan moneter, dan stabilitas ekonomi.",
        "intro": "Pelajari konsep dasar yang membantu memahami perkembangan harga dan kondisi ekonomi.",
        "fact": "Inflasi perlu dilihat berdasarkan periode, indikator, dan sumber data yang digunakan.",
        "keywords": ["inflasi", "moneter", "stabilitas", "ekonomi", "harga"],
        "content": [
            "Inflasi berkaitan dengan perubahan tingkat harga barang dan jasa secara umum.",
            "Kebijakan moneter merupakan salah satu bagian penting dalam kerangka menjaga stabilitas ekonomi.",
            "Data ekonomi perlu dibaca berdasarkan periode dan sumber resmi."
        ],
        "icon_bg": "#e8f8f1",
        "source": BI_URL
    },
    "🌾 Ketahanan Pangan": {
        "short": "Memahami hubungan pasokan pangan, harga pangan, dan stabilitas ekonomi.",
        "intro": "Kenali bagaimana pasokan, distribusi, dan harga pangan berkaitan dengan stabilitas ekonomi.",
        "fact": "Pengendalian inflasi pangan melibatkan sinergi berbagai pihak karena dipengaruhi oleh pasokan dan distribusi.",
        "keywords": ["pangan", "gnpip", "harga pangan", "pasokan", "distribusi"],
        "content": [
            "Ketersediaan pasokan dan kelancaran distribusi berhubungan dengan stabilitas harga pangan.",
            "Pengendalian inflasi pangan membutuhkan sinergi lintas pihak.",
            "Informasi harga dan kondisi pangan sebaiknya dibaca berdasarkan data dan periode yang jelas."
        ],
        "icon_bg": "#fff8df",
        "source": BI_URL
    },
    "📊 Data & Publikasi": {
        "short": "Akses awal menuju statistik, laporan, kajian, dan publikasi BI.",
        "intro": "Gunakan data dan publikasi untuk memahami perkembangan ekonomi dan kebanksentralan berdasarkan sumber yang terdokumentasi.",
        "fact": "Saat membaca data ekonomi, perhatikan periode, definisi indikator, satuan, dan sumber data.",
        "keywords": ["data", "statistik", "publikasi", "laporan", "kajian"],
        "content": [
            "Statistik ekonomi dan keuangan dapat digunakan untuk memahami perkembangan ekonomi.",
            "Publikasi BI menyediakan informasi, kajian, dan analisis ekonomi serta kebanksentralan.",
            "Gunakan periode dan definisi indikator yang tepat ketika membaca data."
        ],
        "icon_bg": "#fff0f1",
        "source": BI_URL
    },
    "🏦 Kebanksentralan": {
        "short": "Mengenal peran, tugas, dan bidang utama Bank Indonesia.",
        "intro": "Kenali konsep dasar kebanksentralan sebelum melanjutkan ke sumber dan publikasi yang lebih lengkap.",
        "fact": "Informasi kebanksentralan dapat dipelajari lebih lanjut melalui berbagai sumber resmi dan publikasi Bank Indonesia.",
        "keywords": ["kebanksentralan", "bank indonesia", "moneter", "makroprudensial"],
        "content": [
            "Topik kebanksentralan dapat dipelajari melalui sumber resmi Bank Indonesia.",
            "Informasi dapat dikelompokkan berdasarkan kebijakan moneter, makroprudensial, dan sistem pembayaran.",
            "Halaman ini merupakan pengantar sebelum pengguna membaca sumber yang lebih lengkap."
        ],
        "icon_bg": "#f1edff",
        "source": BI_URL
    }
}

# ============================================================
# DATA FUNCTIONS
# ============================================================

def save_row(path, row):
    new_df = pd.DataFrame([row])
    if path.exists():
        old_df = pd.read_csv(path)
        df = pd.concat([old_df, new_df], ignore_index=True)
    else:
        df = new_df
    df.to_csv(path, index=False)

def load_csv(path):
    if path.exists():
        return pd.read_csv(path)
    return pd.DataFrame()

def log_usage(action, topic="", query=""):
    save_row(
        USAGE_FILE,
        {
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "action": action,
            "topic": topic,
            "query": query
        }
    )

def safe_key(text):
    return re.sub(r"[^a-zA-Z0-9]+", "_", text).strip("_").lower()

# ============================================================
# SESSION
# ============================================================

MENU = [
    "🏠 Beranda",
    "🔎 Cari Informasi",
    "📚 Jelajah Topik",
    "📖 Perpustakaan BI",
    "📝 Feedback",
    "📊 Dashboard Evaluasi",
    "ℹ️ Tentang"
]

if "menu" not in st.session_state:
    st.session_state.menu = "🏠 Beranda"

if "selected_topic" not in st.session_state:
    st.session_state.selected_topic = list(TOPICS.keys())[0]

# ============================================================
# SIDEBAR
# ============================================================

st.sidebar.markdown("""
<div class="sidebar-brand">
    <div class="bi-mark">BI</div>
    <h2>BI Digital<br>Knowledge Corner</h2>
    <p>Prototype Digital Knowledge Corner</p>
</div>
""", unsafe_allow_html=True)

menu = st.sidebar.radio(
    "Navigasi",
    MENU,
    index=MENU.index(st.session_state.menu)
)

st.session_state.menu = menu

st.sidebar.divider()
st.sidebar.caption(
    "Media pendukung diseminasi informasi kebanksentralan."
)

# ============================================================
# HOME
# ============================================================

if menu == "🏠 Beranda":

    st.markdown("""
    <div class="topbar">
        <div class="prototype-pill">🎓 Prototype Tugas Akhir Magang</div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="hero">
        <div class="hero-content">
            <div class="eyebrow">DIGITAL KNOWLEDGE CORNER</div>
            <h1>BI Digital<br>Knowledge Corner</h1>
            <div class="tagline">Temukan. Pahami. Jelajahi.</div>
            <p>
                Satu pintu akses untuk mengenal Rupiah, sistem pembayaran,
                stabilitas ekonomi, ketahanan pangan, data dan publikasi,
                serta informasi kebanksentralan.
            </p>

            <div class="search-wrap">
                <div style="
                    background:white;
                    border-radius:15px;
                    padding:1rem 1.1rem;
                    color:#637281;
                    font-size:.92rem;
                    box-shadow:0 8px 25px rgba(0,0,0,.12);
                ">
                    🔎 &nbsp; Apa yang ingin kamu cari?
                    <div style="font-size:.73rem;color:#91a0ad;margin-top:.25rem;">
                        Contoh: QRIS, inflasi, BI-FAST, Rupiah, kebanksentralan...
                    </div>
                </div>
            </div>
        </div>

        <div class="skyline">
            <div class="building b1"></div>
            <div class="building b2"></div>
            <div class="building b3"></div>
            <div class="building b4"></div>
            <div class="bi-sign">BI</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Real search input placed immediately below hero
    search = st.text_input(
        "Cari informasi",
        placeholder="Ketik kata kunci untuk mencari...",
        label_visibility="collapsed",
        key="home_search"
    ).strip().lower()

    if search:
        results = []

        for topic, data in TOPICS.items():
            searchable = " ".join([
                topic,
                data["short"],
                data["intro"],
                data["fact"],
                " ".join(data["keywords"]),
                " ".join(data["content"])
            ]).lower()

            if search in searchable:
                results.append(topic)

        log_usage("search", query=search)

        if results:
            st.success(f"Ditemukan {len(results)} topik yang relevan.")

            for topic in results:
                st.write(f"• **{topic}** — {TOPICS[topic]['short']}")

        else:
            st.warning("Informasi belum ditemukan. Coba kata kunci lain.")

    # Quick strip
    st.markdown("""
    <div class="quick-strip">
        <div style="display:grid;grid-template-columns:repeat(4,1fr);gap:.5rem;">
            <div class="quick-item">
                <div class="icon">📖</div>
                <div><b>Ringkasan Informasi</b><span>Singkat & terarah</span></div>
            </div>
            <div class="quick-item">
                <div class="icon">📄</div>
                <div><b>Sumber Resmi</b><span>Dari Bank Indonesia</span></div>
            </div>
            <div class="quick-item">
                <div class="icon">📚</div>
                <div><b>Akses Langsung</b><span>Ke iBI Library</span></div>
            </div>
            <div class="quick-item">
                <div class="icon">💡</div>
                <div><b>Mudah Dipahami</b><span>Untuk semua pengguna</span></div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Topics
    st.markdown(
        '<div class="section-heading">Jelajahi berdasarkan topik</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="section-sub">Pilih topik yang ingin kamu pelajari dan temukan informasi pentingnya secara ringkas dan terarah.</div>',
        unsafe_allow_html=True
    )

    cols = st.columns(3)

    for i, (topic, data) in enumerate(TOPICS.items()):

        with cols[i % 3]:

            st.markdown(
                f"""
                <div class="topic-card">
                    <div class="topic-art" style="background:{data['icon_bg']};">
                        {topic.split(" ")[0]}
                    </div>
                    <h3>{topic[2:]}</h3>
                    <p>{data['short']}</p>
                </div>
                """,
                unsafe_allow_html=True
            )

            if st.button(
                "Jelajahi →",
                key=f"topic_{safe_key(topic)}",
                use_container_width=True
            ):
                st.session_state.selected_topic = topic
                st.session_state.menu = "📚 Jelajah Topik"
                log_usage("open_topic", topic=topic)
                st.rerun()

    # Bottom information panels
    st.markdown("")

    c1, c2, c3 = st.columns(3)

    with c1:
        st.markdown("""
        <div class="panel fact-panel">
            <h3>💡 Tahukah Kamu?</h3>
            <p>
                Rupiah bukan hanya alat pembayaran, tetapi juga merupakan
                simbol kedaulatan negara.
            </p>
        </div>
        """, unsafe_allow_html=True)

    with c2:
        st.markdown("""
        <div class="panel library-panel">
            <h3>📚 Ayo Baca Lebih Lanjut</h3>
            <p>
                Ingin mendalami topik tertentu? Lanjutkan eksplorasi
                koleksi digital melalui iBI Library.
            </p>
        </div>
        """, unsafe_allow_html=True)

        st.link_button(
            "Buka iBI Library →",
            LIBRARY_URL,
            use_container_width=True
        )

    with c3:
        st.markdown("""
        <div class="panel how-panel">
            <h3>📱 Cara Menggunakan</h3>
            <p>
                <b>1.</b> Scan QR Code<br>
                <b>2.</b> Pilih topik<br>
                <b>3.</b> Baca ringkasan<br>
                <b>4.</b> Kunjungi sumber resmi / iBI Library
            </p>
        </div>
        """, unsafe_allow_html=True)

# ============================================================
# SEARCH
# ============================================================

elif menu == "🔎 Cari Informasi":

    st.markdown(
        '<div class="section-heading">🔎 Cari Informasi</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="section-sub">Temukan informasi berdasarkan kata kunci.</div>',
        unsafe_allow_html=True
    )

    q = st.text_input(
        "Kata kunci",
        placeholder="Contoh: QRIS, Rupiah, inflasi, BI-FAST...",
        label_visibility="collapsed"
    ).strip().lower()

    if q:

        results = []

        for topic, data in TOPICS.items():

            searchable = " ".join([
                topic,
                data["short"],
                data["intro"],
                data["fact"],
                " ".join(data["keywords"]),
                " ".join(data["content"])
            ]).lower()

            if q in searchable:
                results.append((topic, data))

        log_usage("search", query=q)

        if results:

            st.success(f"{len(results)} topik ditemukan.")

            for topic, data in results:

                with st.container(border=True):

                    st.subheader(topic)
                    st.write(data["short"])

                    c1, c2 = st.columns(2)

                    with c1:

                        if st.button(
                            "📖 Lihat topik",
                            key=f"search_{safe_key(topic)}",
                            use_container_width=True
                        ):

                            st.session_state.selected_topic = topic
                            st.session_state.menu = "📚 Jelajah Topik"
                            log_usage("open_topic", topic=topic)
                            st.rerun()

                    with c2:

                        st.link_button(
                            "🏦 Sumber resmi BI",
                            data["source"],
                            use_container_width=True
                        )

        else:
            st.warning("Belum ditemukan. Coba kata kunci lain.")

# ============================================================
# TOPIC
# ============================================================

elif menu == "📚 Jelajah Topik":

    st.markdown(
        '<div class="section-heading">📚 Jelajah Topik</div>',
        unsafe_allow_html=True
    )

    topic_list = list(TOPICS.keys())

    selected = st.selectbox(
        "Pilih topik",
        topic_list,
        index=topic_list.index(st.session_state.selected_topic)
    )

    st.session_state.selected_topic = selected

    data = TOPICS[selected]

    log_usage("view_topic", topic=selected)

    st.markdown(
        f"""
        <div class="hero" style="min-height:240px;padding:2.4rem;">
            <div class="hero-content">
                <div class="eyebrow">TOPIK PILIHAN</div>
                <h1 style="font-size:2.7rem;">{selected}</h1>
                <p>{data['short']}</p>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

    c1, c2 = st.columns([1.2, 1])

    with c1:

        st.markdown("### 📌 Ringkasan")
        st.write(data["intro"])

        st.markdown("### 📖 Materi Pengantar")

        for item in data["content"]:
            st.markdown(f"- {item}")

    with c2:

        st.markdown(
            f"""
            <div class="panel fact-panel">
                <h3>💡 Tahukah Kamu?</h3>
                <p>{data['fact']}</p>
            </div>
            """,
            unsafe_allow_html=True
        )

        st.markdown("### 🔗 Lanjutkan")

        st.link_button(
            "🏦 Sumber Resmi Bank Indonesia",
            data["source"],
            use_container_width=True
        )

        st.link_button(
            "📚 Buka iBI Library",
            LIBRARY_URL,
            use_container_width=True
        )

# ============================================================
# LIBRARY
# ============================================================

elif menu == "📖 Perpustakaan BI":

    st.markdown(
        '<div class="section-heading">📖 Perpustakaan Bank Indonesia</div>',
        unsafe_allow_html=True
    )

    st.markdown("""
    <div class="hero" style="min-height:260px;padding:2.5rem;">
        <div class="hero-content">
            <div class="eyebrow">DIGITAL LIBRARY</div>
            <h1 style="font-size:2.5rem;">Ayo Baca Lebih Lanjut</h1>
            <p>
                Digital Knowledge Corner menjadi pintu masuk informasi.
                Untuk mencari koleksi dan membaca sumber yang lebih lengkap,
                lanjutkan ke iBI Library.
            </p>
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.link_button(
        "📚 Buka iBI Library",
        LIBRARY_URL,
        use_container_width=True
    )

    log_usage("open_ibi_library")

    st.markdown("### 🔄 Alur Akses")

    a, b, c = st.columns(3)

    for col, num, title, desc in [
        (a, "01", "Temukan", "Pilih topik yang ingin kamu pelajari."),
        (b, "02", "Pahami", "Baca ringkasan dan informasi pengantar."),
        (c, "03", "Dalami", "Lanjutkan ke iBI Library dan sumber resmi.")
    ]:
        with col:
            st.markdown(
                f"""
                <div class="panel">
                    <div style="color:#0b6b93;font-weight:800;font-size:.78rem;">{num}</div>
                    <h3>{title}</h3>
                    <p>{desc}</p>
                </div>
                """,
                unsafe_allow_html=True
            )

# ============================================================
# FEEDBACK
# ============================================================

elif menu == "📝 Feedback":

    st.markdown(
        '<div class="section-heading">📝 Feedback Pengguna</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="section-sub">Pendapat pengguna digunakan sebagai bahan evaluasi prototype.</div>',
        unsafe_allow_html=True
    )

    with st.form("feedback_form"):

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
        recommendation = st.slider(
            "Saya bersedia merekomendasikan website ini",
            1, 5, 4
        )

        comment = st.text_area(
            "Saran atau komentar",
            placeholder="Apa yang menurut Anda perlu dipertahankan atau diperbaiki?"
        )

        submit = st.form_submit_button(
            "Kirim Feedback",
            use_container_width=True
        )

    if submit:

        save_row(
            FEEDBACK_FILE,
            {
                "timestamp": datetime.now().strftime(
                    "%Y-%m-%d %H:%M:%S"
                ),
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
        )

        st.success("Terima kasih. Feedback berhasil dicatat.")
        st.balloons()

# ============================================================
# DASHBOARD
# ============================================================

elif menu == "📊 Dashboard Evaluasi":

    st.markdown(
        '<div class="section-heading">📊 Dashboard Evaluasi</div>',
        unsafe_allow_html=True
    )

    feedback = load_csv(FEEDBACK_FILE)
    usage = load_csv(USAGE_FILE)

    if feedback.empty:

        st.info(
            "Belum ada data feedback. Lakukan uji coba terlebih dahulu."
        )

    else:

        metric_cols = [
            "kemudahan",
            "kemudahan_mencari",
            "kemudahan_memahami",
            "manfaat",
            "tampilan",
            "rekomendasi"
        ]

        means = feedback[metric_cols].mean()

        c1, c2, c3, c4 = st.columns(4)

        c1.metric("Responden", len(feedback))
        c2.metric("Kemudahan", f"{means['kemudahan']:.2f}/5")
        c3.metric("Manfaat", f"{means['manfaat']:.2f}/5")
        c4.metric("Rekomendasi", f"{means['rekomendasi']:.2f}/5")

        st.divider()

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

        c1, c2 = st.columns(2)

        with c1:
            st.subheader("👥 Distribusi Pengguna")
            st.bar_chart(
                feedback["kategori_pengguna"].value_counts()
            )

        with c2:
            st.subheader("🔥 Topik yang Paling Menarik")
            st.bar_chart(
                feedback["topik_menarik"].value_counts()
            )

        if not usage.empty:

            st.subheader("📈 Aktivitas Penggunaan")

            st.bar_chart(
                usage["action"].value_counts()
            )

            u1, u2, u3 = st.columns(3)

            u1.metric("Aktivitas Tercatat", len(usage))
            u2.metric(
                "Pencarian",
                int((usage["action"] == "search").sum())
            )
            u3.metric(
                "Akses iBI Library",
                int(
                    (
                        usage["action"]
                        == "open_ibi_library"
                    ).sum()
                )
            )

        st.subheader("💬 Feedback Pengguna")

        comments = feedback[
            feedback["komentar"]
            .fillna("")
            .astype(str)
            .str.strip() != ""
        ]

        if comments.empty:
            st.write("Belum ada komentar.")
        else:
            for _, row in comments.iterrows():
                st.markdown(
                    f"**{row['kategori_pengguna']}** — "
                    f"{row['komentar']}"
                )

        st.divider()

        feedback_csv = feedback.to_csv(index=False).encode("utf-8")

        st.download_button(
            "⬇️ Download Data Feedback",
            data=feedback_csv,
            file_name="feedback_digital_knowledge_corner.csv",
            mime="text/csv",
            use_container_width=True
        )

        if not usage.empty:

            usage_csv = usage.to_csv(index=False).encode("utf-8")

            st.download_button(
                "⬇️ Download Data Aktivitas",
                data=usage_csv,
                file_name="aktivitas_digital_knowledge_corner.csv",
                mime="text/csv",
                use_container_width=True
            )

# ============================================================
# ABOUT
# ============================================================

elif menu == "ℹ️ Tentang":

    st.markdown(
        '<div class="section-heading">ℹ️ Tentang Digital Knowledge Corner</div>',
        unsafe_allow_html=True
    )

    st.markdown("""
    <div class="hero" style="min-height:280px;padding:2.6rem;">
        <div class="hero-content">
            <div class="eyebrow">TENTANG PLATFORM</div>
            <h1 style="font-size:2.5rem;">Temukan. Pahami. Jelajahi.</h1>
            <p>
                Digital Knowledge Corner dikembangkan sebagai prototype
                media pendukung diseminasi informasi kebanksentralan
                di lingkungan perpustakaan.
            </p>
        </div>
    </div>
    """, unsafe_allow_html=True)

    c1, c2 = st.columns(2)

    with c1:

        st.markdown("""
        <div class="panel">
            <h3>🎯 Tujuan</h3>
            <p>
                Membantu pengunjung menemukan informasi kebanksentralan
                secara lebih mudah, ringkas, dan terarah melalui satu
                pintu digital.
            </p>
        </div>
        """, unsafe_allow_html=True)

    with c2:

        st.markdown("""
        <div class="panel">
            <h3>🔄 Konsep</h3>
            <p>
                Koleksi → Kurasi → Akses Digital → Pemahaman → Eksplorasi.
            </p>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("### ⚠️ Status Prototype")

    st.info(
        "Website ini merupakan prototype tugas akhir magang dan "
        "bukan aplikasi resmi Bank Indonesia. Konten dan tautan "
        "perlu diverifikasi oleh unit terkait sebelum digunakan "
        "sebagai layanan resmi."
    )

    c1, c2 = st.columns(2)

    with c1:
        st.link_button(
            "🏦 Bank Indonesia",
            BI_URL,
            use_container_width=True
        )

    with c2:
        st.link_button(
            "📚 iBI Library",
            LIBRARY_URL,
            use_container_width=True
        )

# ============================================================
# FOOTER
# ============================================================

st.markdown("""
<div class="footer">
    <b>BI Digital Knowledge Corner</b><br>
    Prototype Tugas Akhir Magang — Media Pendukung Diseminasi Informasi Kebanksentralan<br>
    Prototype — bukan aplikasi resmi Bank Indonesia
</div>
""", unsafe_allow_html=True)
