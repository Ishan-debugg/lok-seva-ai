import streamlit as st

def inject_global_styles():
    st.markdown("""
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.0/css/all.min.css"/>
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=Rajdhani:wght@500;600;700&display=swap');

    /* ── HIDE SIDEBAR COMPLETELY ────────────────────────── */
    [data-testid="stSidebar"],
    [data-testid="collapsedControl"],
    [data-testid="stSidebarNav"],
    section[data-testid="stSidebar"] { display: none !important; }
    <style>
    /* ── ROOT TOKENS ─────────────────────────────────────── */
    :root {
        /* Backgrounds */
        --bg:         #f0f4f8;
        --bg-card:    #ffffff;
        --bg-input:   #f8fafc;

        /* Navy palette */
        --navy:       #0f2547;
        --navy-lt:    #1e3a5f;
        --navy-md:    #163263;

        /* Accent */
        --gold:       #f59e0b;
        --gold-dk:    #d97706;
        --green:      #15803d;
        --green-lt:   #166534;
        --teal:       #0891b2;

        /* Text */
        --text-h:     #0f2547;
        --text-b:     #1e293b;
        --text-s:     #475569;
        --text-m:     #94a3b8;

        /* Borders */
        --border:     #e2e8f0;
        --border-md:  #cbd5e1;
    }

    /* ── BASE ────────────────────────────────────────────── */
    html, body,
    [data-testid="stAppViewContainer"],
    [data-testid="stMain"], .main {
        background-color: var(--bg) !important;
        color: var(--text-b) !important;
        font-family: 'Inter', sans-serif !important;
    }
    [data-testid="stHeader"] { background: transparent !important; }
    .block-container { padding: 1.5rem 2.5rem !important; max-width: 1400px; }

    /* ── TYPOGRAPHY ──────────────────────────────────────── */
    h1, h2, h3, h4, h5, h6 {
        font-family: 'Rajdhani', sans-serif !important;
        color: var(--text-h) !important;
        letter-spacing: .02em;
    }
    p, li { color: var(--text-b); }
    .stMarkdown p:not(.hero-sub) {
    color: var(--text-b) !important;
    }
    [data-testid="stCaption"] { color: var(--text-m) !important; }
    label[data-testid="stWidgetLabel"] > div > p { color: var(--text-s) !important; }

    /* ── BUTTONS ─────────────────────────────────────────── */
    .stButton > button {
        background: #0E7A00 !important;
        color: #ffffff !important;
        border: none !important;
        border-radius: 8px !important;
        font-family: 'Inter', sans-serif !important;
        font-size: .95rem !important;
        font-weight: 600 !important;
        padding: .55rem 1.4rem !important;
        transition: none !important;
    }
    .stButton > button,
    .stButton > button span,
    .stButton > button div,
    .stButton > button p,
    .stButton > button i {
        color: #ffffff !important;
    }
    .secondary-btn-container .stButton > button {
        background: #0E7A00 !important;
        color: #ffffff !important;
        border: 1.5px solid #0E7A00 !important;
    }
    .citizen-btn-container .stButton > button {
        background: var(--green) !important;
        color: #ffffff !important;
        font-size: 1.05rem !important;
        padding: .7rem 1.6rem !important;
        border-radius: 10px !important;
    }
    .citizen-btn-container .stButton > button:hover {
        background: var(--green-lt) !important;
        transform: translateY(-2px) !important;
    }
    .submit-btn-container .stButton > button {
        background: var(--green) !important;
        color: #ffffff !important;
        font-size: 1.05rem !important;
        padding: .75rem 2rem !important;
        border-radius: 10px !important;
        width: 100% !important;
    }
    .submit-btn-container .stButton > button:hover {
        background: var(--green-lt) !important;
        transform: translateY(-2px) !important;
    }
    .track-btn-container .stButton > button {
        background: var(--navy) !important;
        color: #ffffff !important;
        border: 1.5px solid var(--navy) !important;
    }
    .track-btn-container .stButton > button:hover {
        background: var(--navy) !important;
        color: #ffffff !important;
    }

    /* ── INPUTS ──────────────────────────────────────────── */
    .stTextInput > div > div > input,
    .stTextArea  > div > div > textarea,
    .stSelectbox > div > div,
    .stNumberInput > div > div > input {
        background: var(--bg-input) !important;
        color: var(--text-b) !important;
        border: 1.5px solid var(--border-md) !important;
        border-radius: 8px !important;
    }
    .stTextInput > div > div > input::placeholder,
    .stTextArea  > div > div > textarea::placeholder { color: var(--text-m) !important; }
    .stTextInput > div > div > input:focus,
    .stTextArea  > div > div > textarea:focus {
        border-color: var(--navy) !important;
        box-shadow: 0 0 0 3px rgba(15,37,71,.1) !important;
    }
    .stSelectbox > div > div > div { color: var(--text-b) !important; }

    /* ── METRICS ─────────────────────────────────────────── */
    [data-testid="stMetric"] {
        background: var(--bg-card) !important;
        border: 1.5px solid var(--border) !important;
        border-radius: 12px !important;
        padding: 1.2rem 1.4rem !important;
    }
    [data-testid="stMetricValue"] {
        color: var(--navy) !important;
        font-family: 'Rajdhani', sans-serif !important;
        font-size: 2rem !important;
    }
    [data-testid="stMetricLabel"] {
        color: var(--text-s) !important;
        font-size: .75rem !important;
        text-transform: uppercase; letter-spacing: .07em;
    }

    /* ── DATAFRAME ───────────────────────────────────────── */
    [data-testid="stDataFrame"] {
        background: var(--bg-card) !important;
        border: 1.5px solid var(--border) !important;
        border-radius: 10px !important;
    }
    [data-testid="stDataFrame"] thead th {
        background: var(--bg) !important;
        color: var(--text-h) !important;
    }
    [data-testid="stDataFrame"] tbody td { color: var(--text-b) !important; }

    /* ── EXPANDERS ───────────────────────────────────────── */
    [data-testid="stExpander"] {
        background: var(--bg-card) !important;
        border: 1.5px solid var(--border) !important;
        border-radius: 10px !important;
        margin-bottom: .5rem !important;
    }
    [data-testid="stExpander"] summary { color: var(--text-h) !important; font-weight: 600 !important; }
    [data-testid="stExpander"] [data-testid="stMarkdownContainer"] p { color: var(--text-b) !important; }

    /* ── ALERTS ──────────────────────────────────────────── */
    [data-testid="stAlert"] { border-radius: 10px !important; }

    /* ── DIVIDER ─────────────────────────────────────────── */
    hr { border-color: var(--border) !important; opacity: 1 !important; }

    /* ══════════════════════════════════════════════════════
       CUSTOM COMPONENT CLASSES
    ══════════════════════════════════════════════════════ */

    /* Hero banner — dark navy-to-green gradient card */
    .hero-wrap {
        background: linear-gradient(135deg, #0d1b3e 0%, #0f2547 45%, #1a3a2e 100%);
        border: 2px solid var(--gold);
        border-radius: 16px;
        padding: 3rem 2.8rem;
        margin-bottom: 2rem;
        position: relative;
        overflow: hidden;
    }
    .hero-wrap::after {
        content: '';
        position: absolute; top: -80px; right: -80px;
        width: 320px; height: 320px;
        background: radial-gradient(circle, rgba(21,128,61,.3) 0%, transparent 70%);
        pointer-events: none;
    }
    .hero-tag {
        font-size: .7rem; letter-spacing: .2em; text-transform: uppercase;
        color: var(--gold); margin-bottom: .6rem; font-weight: 700;
    }
    .hero-title {
        font-family: 'Rajdhani', sans-serif;
        font-size: 3rem; font-weight: 700;
        line-height: 1.1; color: #ffffff; margin-bottom: .8rem;
    }
    .hero-title span { color: var(--gold); }
    .hero-sub,
    .hero-sub p,
    .hero-sub span,
    .hero-sub div {
        color: #ffffff !important;
    }
    .hero-sub { font-size: .95rem; max-width: 560px; line-height: 1.65; }

    /* Stat tiles */
    .stat-tile {
        background: var(--bg-card);
        border: 1.5px solid var(--border);
        border-radius: 12px;
        padding: 1.5rem 1.6rem;
        text-align: center;
        transition: border-color .2s, box-shadow .2s;
    }
    .stat-tile:hover { border-color: var(--navy); box-shadow: 0 4px 16px rgba(15,37,71,.08); }
    .stat-tile .num {
        font-family: 'Rajdhani', sans-serif;
        font-size: 2.4rem; font-weight: 700;
        color: var(--navy); line-height: 1;
    }
    .stat-tile .num.gold { color: var(--gold); }
    .stat-tile .lbl {
        font-size: .72rem; color: var(--text-s);
        letter-spacing: .08em; text-transform: uppercase; margin-top: .4rem;
    }
    .stat-tile-gold { border-color: var(--gold) !important; }

    /* Portal cards */
    .portal-card {
        background: var(--bg-card);
        border: 1.5px solid var(--border);
        border-top: 4px solid var(--gold);
        border-radius: 14px;
        padding: 2.2rem 2rem;
        min-height: 220px;
        height: 100%;
        display: flex;
        align-items: center;
        justify-content: center;
        transition: box-shadow .2s, border-color .2s;
        text-align: center;
    }
    .portal-card:hover { box-shadow: 0 8px 24px rgba(15,37,71,.1); border-color: var(--navy); }
    .portal-icon { font-size: 2.4rem; color: var(--navy); margin-bottom: .8rem; }
    .portal-title {
        font-family: 'Rajdhani', sans-serif;
        font-size: 1.5rem; font-weight: 700;
        color: var(--navy); margin-bottom: .5rem;
    }
    .portal-desc { color: var(--text-s); font-size: .92rem; line-height: 1.6; }

    /* Generic card */
    .lk-card {
        background: var(--bg-card);
        border: 1.5px solid var(--border);
        border-radius: 12px;
        padding: 1.4rem 1.6rem;
        margin-bottom: 1rem;
        transition: box-shadow .2s;
    }
    .lk-card:hover { box-shadow: 0 4px 16px rgba(15,37,71,.07); }
    .lk-card h4 { color: var(--text-h) !important; }
    .lk-card p, .lk-card li { color: var(--text-b) !important; }

    /* Complaint ID display */
    .complaint-id {
        font-family: 'Rajdhani', sans-serif;
        font-size: 2.2rem; font-weight: 700;
        color: var(--gold); letter-spacing: .1em;
    }

    /* Demo box on login */
    .demo-box {
        border: 1.5px dashed var(--gold);
        border-radius: 10px;
        padding: 1rem 1.4rem;
        background: #fffbeb;
        text-align: center;
        margin-top: 1.5rem;
        color: var(--text-b);
        font-size: .92rem;
    }
    .demo-box strong { color: var(--text-h); }
    .demo-title { color: var(--gold-dk); font-weight: 700; margin-bottom: .4rem; }

    /* Feedback stars */
    .star-row { font-size: 1.8rem; letter-spacing: .1em; }

    /* Download PDF button */
    [data-testid="stDownloadButton"] > button {
        background: var(--navy) !important;
        color: #ffffff !important;
        border-radius: 8px !important;
        font-weight: 600 !important;
        padding: .5rem 1.2rem !important;
        border: none !important;
    }
    [data-testid="stDownloadButton"] > button:hover {
        background: var(--navy-md) !important;
    }
    /* Force all button text to be readable */
    .stButton > button,
    .stButton > button *,
    .stButton > button p,
    .stButton > button span {
        color: inherit !important;
    }
    [data-testid="stDownloadButton"] > button,
    [data-testid="stDownloadButton"] > button * {
        color: #ffffff !important;
    }
    </style>
    """, unsafe_allow_html=True)
    