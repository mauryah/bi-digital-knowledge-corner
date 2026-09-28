import streamlit as st
import pandas as pd
from pathlib import Path
from datetime import datetime
import re

# ============================================================
# BI DIGITAL KNOWLEDGE CORNER
# Final Prototype - Tugas Akhir Magang
# Perpustakaan Bank Indonesia
# ============================================================

st.set_page_config(
    page_title="BI Digital Knowledge Corner",
    page_icon="🏦",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ============================================================
# KONFIGURASI
# ============================================================

BI_URL = "https://www.bi.go.id/"
LIBRARY_URL = "https://web-ibilibrary.moco.co.id/"

DATA_DIR = Path("data")
DATA_DIR.mkdir(exist_ok=True)

FEEDBACK_FILE = DATA_DIR / "feedback.csv"
USAGE_FILE = DATA_DIR / "usage.csv"

# ============================================================
# STYLE
# ============================================================

st.markdown("""
<style>
.stApp {
    background: #f5f8fc;
}

.main .block-container {
    padding-top: 1.5rem;
    padding-bottom: 2rem;
    max-width: 1200px;
}

.hero {
    padding: 3rem 3.2rem;
    border-radius: 24px;
    background: linear-gradient(135deg, #063b63 0%, #0b6b93 58%, #1597b8 100%);
    color: white;
    margin-bottom: 1.4rem;
    box-shadow: 0 10px 30px rgba(6,59,99,.16);
}

.hero h1 {
    font-size: 2.65rem;
    line-height: 1.12;
    margin: 0 0 .65rem 0;
    font-weight: 800;
}

.hero .tagline {
    font-size: 1.15rem;
    font-weight: 700;
    margin-bottom: .45rem;
}

.hero p {
    font-size: 1rem;
    max-width: 780px;
    margin: 0;
    opacity: .94;
    line-height: 1.65;
}

.eyebrow {
    text-transform: uppercase;
    letter-spacing: .12em;
    font-size: .78rem;
    font-weight: 800;
    opacity: .78;
    margin-bottom: .6rem;
}

.section-title {
    color: #063b63;
    font-weight: 800;
    margin-top: .4rem;
    margin-bottom: .8rem;
}

.topic-card {
    background: white;
    border: 1px solid #e4ebf2;
    border-radius: 18px;
    padding: 1.35rem;
    min-height: 195px;
    margin-bottom: 1rem;
    box-shadow: 0 5px 18px rgba(15,53,80,.045);
}

.topic-card h3 {
    color: #063b63;
    margin: 0 0 .55rem 0;
    font-size: 1.12rem;
}

.topic-card p {
    color: #5b6875;
    line-height: 1.55;
    min-height: 66px;
}

.topic-label {
    display: inline-block;
    background: #eaf6fa;
    color: #0b6b93;
    padding: .28rem .62rem;
    border-radius: 999px;
    font-size: .75rem;
    font-weight: 700;
    margin-bottom: .65rem;
}

.info-box {
    background: #edf7fb;
    border-left: 5px solid #0b6b93;
    padding: 1rem 1.2rem;
    border-radius: 10px;
    margin: 1rem 0;
    color: #244354;
    line-height: 1.6;
}

.fact-box {
    background: linear-gradient(135deg, #fff8e8, #fffdf7);
    border: 1px solid #f2dfad;
    border-radius: 16px;
    padding: 1.1rem 1.25rem;
    margin: 1rem 0;
}

.fact-box .title {
    color: #8a6100;
    font-weight: 800;
    margin-bottom: .3rem;
}

.step-card {
    background: white;
    border: 1px solid #e4ebf2;
    border-radius: 16px;
    padding: 1.2rem;
    height: 100%;
    box-shadow: 0 4px 15px rgba(15,53,80,.04);
}

.step-number {
    color: #0b6b93;
    font-weight: 800;
    font-size: .8rem;
    letter-spacing: .08em;
}

.step-card h4 {
    color: #063b63;
    margin: .35rem 0 .45rem;
}

.library-box {
    background: linear-gradient(135deg, #063b63, #0b6b93);
    color: white;
    border-radius: 20px;
    padding: 1.6rem;
    margin: 1.2rem 0;
}

.library-box h3 {
    margin-top: 0;
}

.small-note {
    color: #687785;
    font-size: .88rem;
    line-height: 1.5;
}

.footer {
    text-align: center;
    color: #71808d;
    padding: 2.2rem 0 1rem;
    font-size: .82rem;
    line-height: 1.6;
}

[data-testid="stMetric"] {
    background: white;
    border: 1px solid #e4ebf2;
    border-radius: 14px;
    padding: .9rem;
}

div.stButton > button,
div[data-testid="stLinkButton"] > a {
    border-radius: 10px;
    font-weight: 700;
}

@media (max-width: 768px) {
    .hero {
        padding: 2rem 1.35rem;
        border-radius: 18px;
    }

    .hero h1 {
        font-size: 2rem;
    }

    .hero p {
        font-size: .94rem;
    }

    .topic-card {
        min-height: auto;
    }
}
</style>
""", unsafe_allow_html=True)

# ============================================================
# DATA TOPIK
# ============================================================

TOPICS = {
    "💰 Rupiah": {
        "short": "Mengenal Rupiah, Cinta Bangga Paham Rupiah, dan peran Rupiah sebagai simbol kedaulatan negara.",
        "keywords": ["rupiah", "cbp", "cinta", "bangga", "paham", "uang"],
        "intro": "Rupiah merupakan mata uang negara Indonesia. Topik ini menjadi pintu masuk untuk memahami penggunaan, karakteristik, dan pentingnya Rupiah.",
        "fact": "Rupiah tidak hanya digunakan sebagai alat pembayaran, tetapi juga memiliki makna sebagai simbol kedaulatan negara.",
        "content": [
            "Cinta Rupiah berkaitan dengan mengenali, merawat, dan menggunakan Rupiah dengan baik.",
            "Bangga Rupiah menempatkan Rupiah sebagai salah satu simbol identitas dan kedaulatan negara.",
            "Paham Rupiah mencakup pemahaman terhadap fungsi, karakteristik, dan penggunaan Rupiah."
        ],
        "source": BI_URL
    },

    "💳 Sistem Pembayaran": {
        "short": "Mengenal QRIS, BI-FAST, dan perkembangan sistem pembayaran yang mendukung transaksi masyarakat.",
        "keywords": ["qris", "bi-fast", "pembayaran", "digital", "transaksi"],
        "intro": "Sistem pembayaran merupakan bagian penting dari aktivitas ekonomi. Pengguna dapat mengenal berbagai infrastruktur dan layanan pembayaran melalui topik ini.",
        "fact": "QRIS dirancang untuk membantu menciptakan interoperabilitas pembayaran berbasis QR.",
        "content": [
            "QRIS merupakan standar QR Code pembayaran yang dikembangkan untuk mendukung interoperabilitas pembayaran.",
            "BI-FAST merupakan infrastruktur pembayaran ritel yang mendukung transaksi secara cepat dan efisien.",
            "Literasi sistem pembayaran juga mencakup pemahaman dan penggunaan layanan digital secara aman."
        ],
        "source": BI_URL
    },

    "📈 Stabilitas Ekonomi": {
        "short": "Pengantar mengenai inflasi, kebijakan moneter, dan stabilitas ekonomi.",
        "keywords": ["inflasi", "moneter", "stabilitas", "ekonomi", "harga"],
        "intro": "Stabilitas ekonomi dapat dipahami melalui berbagai indikator dan kebijakan. Topik ini memberikan pengantar sebelum pengguna membaca sumber yang lebih lengkap.",
        "fact": "Inflasi perlu dilihat berdasarkan periode, indikator, dan sumber data yang digunakan.",
        "content": [
            "Inflasi berkaitan dengan perubahan tingkat harga barang dan jasa secara umum.",
            "Kebijakan moneter merupakan salah satu bagian penting dalam kerangka menjaga stabilitas ekonomi.",
            "Data ekonomi perlu dibaca berdasarkan periode dan sumber resmi."
        ],
        "source": BI_URL
    },

    "🌾 Ketahanan Pangan": {
        "short": "Memahami hubungan pasokan pangan, harga pangan, dan stabilitas ekonomi.",
        "keywords": ["pangan", "gnpip", "harga pangan", "pasokan", "distribusi"],
        "intro": "Perkembangan harga pangan memiliki keterkaitan dengan kondisi pasokan, distribusi, dan stabilitas harga.",
        "fact": "Pengendalian inflasi pangan melibatkan sinergi berbagai pihak karena dipengaruhi oleh pasokan dan distribusi.",
        "content": [
            "Ketersediaan pasokan dan kelancaran distribusi berhubungan dengan stabilitas harga pangan.",
            "Pengendalian inflasi pangan membutuhkan sinergi lintas pihak.",
            "Informasi harga dan kondisi pangan sebaiknya dibaca berdasarkan data dan periode yang jelas."
        ],
        "source": BI_URL
    },

    "📊 Data & Publikasi": {
        "short": "Pintu masuk ke statistik, laporan, kajian, dan berbagai publikasi Bank Indonesia.",
        "keywords": ["data", "statistik", "publikasi", "laporan", "kajian"],
        "intro": "Data dan publikasi membantu pengguna memahami perkembangan ekonomi dan kebanksentralan berdasarkan sumber yang terdokumentasi.",
        "fact": "Saat membaca data ekonomi, perhatikan periode, definisi indikator, satuan, dan sumber data.",
        "content": [
            "Statistik ekonomi dan keuangan dapat digunakan untuk memahami perkembangan ekonomi.",
            "Publikasi BI menyediakan informasi, kajian, dan analisis ekonomi serta kebanksentralan.",
            "Gunakan periode dan definisi indikator yang tepat ketika membaca data."
        ],
        "source": BI_URL
    },

    "🏦 Kebanksentralan": {
        "short": "Mengenal fungsi, tugas, dan isu utama dalam kebanksentralan.",
        "keywords": ["kebanksentralan", "bank indonesia", "moneter", "makroprudensial", "sistem pembayaran"],
        "intro": "Topik kebanksentralan memberikan gambaran umum mengenai fungsi dan bidang yang berkaitan dengan Bank Indonesia.",
        "fact": "Informasi kebanksentralan dapat dipelajari lebih lanjut melalui berbagai sumber resmi dan publikasi Bank Indonesia.",
        "content": [
            "Topik kebanksentralan dapat dipelajari melalui sumber resmi Bank Indonesia.",
            "Informasi dapat dikelompokkan berdasarkan kebijakan moneter, makroprudensial, dan sistem pembayaran.",
            "Halaman ini merupakan pengantar sebelum pengguna membaca sumber yang lebih lengkap."
        ],
        "source": BI_URL
    }
}

# ============================================================
# FUNGSI DATA
# ============================================================

def save_row(file_path, row):
    new_data = pd.DataFrame([row])

    if file_path.exists():
        old_data = pd.read_csv(file_path)
        data = pd.concat([old_data, new_data], ignore_index=True)
    else:
        data = new_data

    data.to_csv(file_path, index=False)


def load_csv(file_path):
    if file_path.exists():
        return pd.read_csv(file_path)

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
# NAVIGASI
# ============================================================

if "menu" not in st.session_state:
    st.session_state["menu"] = "🏠 Beranda"

menu_options = [
    "🏠 Beranda",
    "🔎 Cari Informasi",
    "📚 Jelajah Topik",
    "📖 Perpustakaan BI",
    "📝 Feedback",
    "📊 Dashboard Evaluasi",
    "ℹ️ Tentang"
]

st.sidebar.markdown("## 🏦 BI Knowledge Corner")
st.sidebar.caption("Prototype Digital Knowledge Corner")

menu = st.sidebar.radio(
    "Navigasi",
    menu_options,
    index=menu_options.index(st.session_state["menu"])
)

st.session_state["menu"] = menu

st.sidebar.divider()
st.sidebar.caption(
    "Media pendukung diseminasi informasi kebanksentralan."
)

# ============================================================
# BERANDA
# ============================================================

if menu == "🏠 Beranda":

    st.markdown("""
    <div class="hero">
        <div class="eyebrow">DIGITAL KNOWLEDGE CORNER</div>
        <h1>BI Digital Knowledge Corner</h1>
        <div class="tagline">Temukan. Pahami. Jelajahi.</div>
        <p>
            Satu pintu akses untuk mengenal Rupiah, sistem pembayaran,
            stabilitas ekonomi, ketahanan pangan, data dan publikasi,
            serta berbagai informasi kebanksentralan.
        </p>
    </div>
    """, unsafe_allow_html=True)

    c1, c2 = st.columns(2)

    with c1:
        if st.button(
            "🔎 Mulai Jelajah Informasi",
            use_container_width=True
        ):
            st.session_state["menu"] = "🔎 Cari Informasi"
            st.rerun()

    with c2:
        st.link_button(
            "📚 Buka iBI Library",
            LIBRARY_URL,
            use_container_width=True
        )

    st.markdown("")

    st.markdown(
        '<div class="section-title">🔎 Apa yang ingin kamu pelajari?</div>',
        unsafe_allow_html=True
    )

    search_home = st.text_input(
        "Pencarian",
        placeholder="Contoh: QRIS, Rupiah, inflasi, BI-FAST, publikasi...",
        label_visibility="collapsed"
    ).strip().lower()

    if search_home:

        matches = []

        for topic, data in TOPICS.items():

            text = " ".join([
                topic,
                data["short"],
                data["intro"],
                data["fact"],
                " ".join(data["keywords"]),
                " ".join(data["content"])
            ]).lower()

            if search_home in text:
                matches.append(topic)

        log_usage("search", query=search_home)

        if matches:

            st.success(
                f"Ditemukan {len(matches)} topik yang relevan."
            )

            for topic in matches:
                st.write(
                    f"• **{topic}** — {TOPICS[topic]['short']}"
                )

        else:
            st.warning(
                "Informasi belum ditemukan. Coba kata kunci lain."
            )

    st.markdown(
        '<div class="section-title">📚 Jelajahi berdasarkan topik</div>',
        unsafe_allow_html=True
    )

    cols = st.columns(3)

    for i, (topic, data) in enumerate(TOPICS.items()):

        with cols[i % 3]:

            st.markdown(
                f"""
                <div class="topic-card">
                    <div class="topic-label">TOPIK INFORMASI</div>
                    <h3>{topic}</h3>
                    <p>{data['short']}</p>
                </div>
                """,
                unsafe_allow_html=True
            )

            if st.button(
                "Pelajari topik →",
                key=f"home_{safe_key(topic)}",
                use_container_width=True
            ):

                st.session_state["selected_topic"] = topic
                st.session_state["menu"] = "📚 Jelajah Topik"

                log_usage(
                    "open_topic",
                    topic=topic
                )

                st.rerun()

    st.divider()

    st.markdown(
        '<div class="section-title">✨ Mengapa Digital Knowledge Corner?</div>',
        unsafe_allow_html=True
    )

    st.markdown("""
    <div class="info-box">
        <b>Digital Knowledge Corner</b> dirancang sebagai
        <b>quick access point</b> untuk membantu pengunjung menemukan
        informasi kebanksentralan secara lebih terarah, ringkas,
        dan mudah diakses. Platform ini berfungsi sebagai media
        pendukung dan <b>tidak menggantikan iBI Library</b>.
    </div>
    """, unsafe_allow_html=True)

    s1, s2, s3, s4 = st.columns(4)

    with s1:
        st.metric("Topik", len(TOPICS))

    with s2:
        st.metric("Akses", "Digital")

    with s3:
        st.metric("Fokus", "Literasi")

    with s4:
        st.metric("Perpustakaan", "iBI Library")

    st.markdown(
        '<div class="section-title">🚀 Cara Menggunakan</div>',
        unsafe_allow_html=True
    )

    a, b, c, d = st.columns(4)

    steps = [
        (
            "01",
            "Scan QR",
            "Akses Digital Knowledge Corner dari perangkat kamu."
        ),
        (
            "02",
            "Pilih Topik",
            "Temukan informasi sesuai kebutuhan."
        ),
        (
            "03",
            "Baca & Jelajahi",
            "Baca ringkasan lalu lanjutkan ke sumber resmi."
        ),
        (
            "04",
            "Berikan Feedback",
            "Bantu pengembangan melalui penilaian pengguna."
        )
    ]

    for col, (num, title, desc) in zip(
        [a, b, c, d],
        steps
    ):

        with col:

            st.markdown(
                f"""
                <div class="step-card">
                    <div class="step-number">{num}</div>
                    <h4>{title}</h4>
                    <div class="small-note">{desc}</div>
                </div>
                """,
                unsafe_allow_html=True
            )

# ============================================================
# CARI INFORMASI
# ============================================================

elif menu == "🔎 Cari Informasi":

    st.title("🔎 Cari Informasi")

    st.write(
        "Cari informasi berdasarkan topik, kata kunci, "
        "atau istilah kebanksentralan."
    )

    q = st.text_input(
        "Kata kunci",
        placeholder="Contoh: QRIS, Rupiah, inflasi, BI-FAST, data..."
    ).strip().lower()

    if q:

        log_usage(
            "search",
            query=q
        )

        results = []

        for topic, data in TOPICS.items():

            text = " ".join([
                topic,
                data["short"],
                data["intro"],
                data["fact"],
                " ".join(data["keywords"]),
                " ".join(data["content"])
            ]).lower()

            if q in text:
                results.append((topic, data))

        if results:

            st.success(
                f"{len(results)} topik ditemukan."
            )

            for topic, data in results:

                with st.container(border=True):

                    st.subheader(topic)

                    st.write(data["short"])

                    st.markdown("**Materi pengantar:**")

                    for item in data["content"]:
                        st.markdown(f"- {item}")

                    c1, c2 = st.columns(2)

                    with c1:

                        if st.button(
                            "📖 Lihat topik",
                            key=f"search_{safe_key(topic)}",
                            use_container_width=True
                        ):

                            st.session_state["selected_topic"] = topic
                            st.session_state["menu"] = "📚 Jelajah Topik"

                            log_usage(
                                "open_topic",
                                topic=topic
                            )

                            st.rerun()

                    with c2:

                        st.link_button(
                            "🏦 Sumber resmi BI",
                            data["source"],
                            use_container_width=True
                        )

        else:

            st.warning(
                "Belum ditemukan. Coba kata kunci lain."
            )

# ============================================================
# JELAJAH TOPIK
# ============================================================

elif menu == "📚 Jelajah Topik":

    st.title("📚 Jelajah Topik")

    if "selected_topic" not in st.session_state:
        st.session_state["selected_topic"] = list(TOPICS.keys())[0]

    topic_list = list(TOPICS.keys())

    default_topic = st.session_state["selected_topic"]

    selected = st.selectbox(
        "Pilih topik",
        topic_list,
        index=topic_list.index(default_topic)
    )

    st.session_state["selected_topic"] = selected

    data = TOPICS[selected]

    log_usage(
        "view_topic",
        topic=selected
    )

    st.markdown(
        f"""
        <div class="hero" style="padding:2rem 2.2rem;">
            <div class="eyebrow">TOPIK PILIHAN</div>
            <h1 style="font-size:2.1rem;">{selected}</h1>
            <p>{data['short']}</p>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown("### 📌 Ringkasan")

    st.write(data["intro"])

    st.markdown(
        f"""
        <div class="fact-box">
            <div class="title">💡 TAHUKAH KAMU?</div>
            <div>{data['fact']}</div>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown("### 📖 Materi Pengantar")

    for item in data["content"]:
        st.markdown(f"- {item}")

    st.markdown("### 🔗 Lanjutkan Eksplorasi")

    c1, c2 = st.columns(2)

    with c1:

        st.link_button(
            "🏦 Buka Sumber Resmi Bank Indonesia",
            data["source"],
            use_container_width=True
        )

    with c2:

        st.link_button(
            "📚 Cari Koleksi di iBI Library",
            LIBRARY_URL,
            use_container_width=True
        )

    st.markdown("""
    <div class="info-box">
        <b>Tips:</b> Gunakan ringkasan di atas sebagai pengantar,
        kemudian lanjutkan membaca sumber resmi untuk memperoleh
        informasi yang lebih lengkap dan mendalam.
    </div>
    """, unsafe_allow_html=True)

# ============================================================
# PERPUSTAKAAN BI
# ============================================================

elif menu == "📖 Perpustakaan BI":

    st.title("📖 Perpustakaan Bank Indonesia")

    st.markdown("""
    <div class="library-box">
        <h3>📚 Butuh informasi yang lebih lengkap?</h3>
        <p>
            Digital Knowledge Corner membantu pengguna menemukan
            topik dan informasi awal. Untuk eksplorasi koleksi dan
            layanan perpustakaan digital, lanjutkan ke
            <b>iBI Library</b>.
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.link_button(
        "📚 Buka iBI Library",
        LIBRARY_URL,
        use_container_width=True
    )

    log_usage(
        "open_ibi_library"
    )

    st.markdown("")

    st.markdown("### 🔄 Alur Akses")

    a, b, c = st.columns(3)

    with a:

        st.markdown("""
        <div class="step-card">
            <div class="step-number">01</div>
            <h4>Digital Knowledge Corner</h4>
            <div class="small-note">
                Temukan informasi berdasarkan topik.
            </div>
        </div>
        """, unsafe_allow_html=True)

    with b:

        st.markdown("""
        <div class="step-card">
            <div class="step-number">02</div>
            <h4>Informasi Pengantar</h4>
            <div class="small-note">
                Pahami konsep dasar secara ringkas.
            </div>
        </div>
        """, unsafe_allow_html=True)

    with c:

        st.markdown("""
        <div class="step-card">
            <div class="step-number">03</div>
            <h4>iBI Library</h4>
            <div class="small-note">
                Lanjutkan eksplorasi koleksi yang lebih lengkap.
            </div>
        </div>
        """, unsafe_allow_html=True)

# ============================================================
# FEEDBACK
# ============================================================

elif menu == "📝 Feedback":

    st.title("📝 Evaluasi Pengguna")

    st.write(
        "Bantu kami mengevaluasi pengalaman penggunaan "
        "Digital Knowledge Corner."
    )

    with st.form("feedback_form"):

        role = st.selectbox(
            "Kategori pengguna",
            [
                "Mahasiswa",
                "Pelajar",
                "Pegawai",
                "Umum",
                "Lainnya"
            ]
        )

        topic = st.selectbox(
            "Topik yang paling menarik",
            list(TOPICS.keys())
        )

        ease = st.slider(
            "Website mudah digunakan",
            1, 5, 4
        )

        find_info = st.slider(
            "Informasi mudah ditemukan",
            1, 5, 4
        )

        understand = st.slider(
            "Informasi mudah dipahami",
            1, 5, 4
        )

        useful = st.slider(
            "Website bermanfaat",
            1, 5, 4
        )

        appearance = st.slider(
            "Tampilan mudah dipahami",
            1, 5, 4
        )

        recommendation = st.slider(
            "Saya bersedia merekomendasikan website ini",
            1, 5, 4
        )

        comment = st.text_area(
            "Saran atau komentar",
            placeholder=(
                "Tuliskan hal yang menurut Anda perlu "
                "dipertahankan atau diperbaiki..."
            )
        )

        submit = st.form_submit_button(
            "Kirim Feedback",
            use_container_width=True
        )

    if submit:

        row = {
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

        save_row(
            FEEDBACK_FILE,
            row
        )

        st.success(
            "Terima kasih. Feedback berhasil dicatat."
        )

        st.balloons()

# ============================================================
# DASHBOARD
# ============================================================

elif menu == "📊 Dashboard Evaluasi":

    st.title("📊 Dashboard Evaluasi")

    feedback = load_csv(FEEDBACK_FILE)
    usage = load_csv(USAGE_FILE)

    if feedback.empty:

        st.info(
            "Belum ada data feedback. "
            "Lakukan uji coba terlebih dahulu."
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

        with c1:
            st.metric(
                "Responden",
                len(feedback)
            )

        with c2:
            st.metric(
                "Kemudahan",
                f"{means['kemudahan']:.2f}/5"
            )

        with c3:
            st.metric(
                "Manfaat",
                f"{means['manfaat']:.2f}/5"
            )

        with c4:
            st.metric(
                "Rekomendasi",
                f"{means['rekomendasi']:.2f}/5"
            )

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

            with u1:
                st.metric(
                    "Aktivitas Tercatat",
                    len(usage)
                )

            with u2:
                st.metric(
                    "Pencarian",
                    int(
                        (
                            usage["action"] == "search"
                        ).sum()
                    )
                )

            with u3:
                st.metric(
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

            st.write(
                "Belum ada komentar."
            )

        else:

            for _, row in comments.iterrows():

                st.markdown(
                    f"**{row['kategori_pengguna']}** — "
                    f"{row['komentar']}"
                )

        st.divider()

        st.subheader("⬇️ Data Evaluasi")

        feedback_csv = feedback.to_csv(
            index=False
        ).encode("utf-8")

        st.download_button(
            "Download Data Feedback",
            data=feedback_csv,
            file_name=(
                "feedback_digital_knowledge_corner.csv"
            ),
            mime="text/csv",
            use_container_width=True
        )

        if not usage.empty:

            usage_csv = usage.to_csv(
                index=False
            ).encode("utf-8")

            st.download_button(
                "Download Data Aktivitas",
                data=usage_csv,
                file_name=(
                    "aktivitas_digital_knowledge_corner.csv"
                ),
                mime="text/csv",
                use_container_width=True
            )

# ============================================================
# TENTANG
# ============================================================

elif menu == "ℹ️ Tentang":

    st.title("ℹ️ Tentang Digital Knowledge Corner")

    st.markdown("""
    ### 🎯 Tujuan

    Digital Knowledge Corner dikembangkan sebagai **prototype media
    pendukung diseminasi informasi kebanksentralan** di lingkungan
    perpustakaan.

    ### 💡 Konsep

    **Koleksi → Kurasi → Akses Digital → Pemahaman → Eksplorasi**

    ### 🔄 Cara Kerja

    **QR Code → Digital Knowledge Corner → Pilih Topik → Baca Ringkasan
    → Sumber Resmi → iBI Library**

    ### 👥 Manfaat

    **Bagi pengunjung**  
    Membantu menemukan informasi kebanksentralan secara lebih cepat
    dan terarah.

    **Bagi perpustakaan**  
    Menjadi media pendukung untuk memperkenalkan dan mengarahkan
    pengguna kepada sumber informasi yang relevan.

    **Bagi evaluasi pengembangan**  
    Menyediakan feedback dan data penggunaan sebagai bahan evaluasi
    prototype.

    ### ⚠️ Status

    Website ini merupakan **prototype tugas akhir magang** dan bukan
    aplikasi resmi Bank Indonesia. Konten dan tautan perlu diverifikasi
    oleh unit terkait sebelum digunakan sebagai layanan resmi.
    """)

    st.markdown("### 🔗 Tautan")

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
    Prototype Tugas Akhir Magang — Media Pendukung Diseminasi
    Informasi Kebanksentralan<br>
    <span>© Prototype — bukan aplikasi resmi Bank Indonesia</span>
</div>
""", unsafe_allow_html=True)
