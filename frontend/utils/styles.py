import streamlit as st

def inject_global_styles():
    st.markdown("""
    <style>
    /* ── ROOT COLOUR TOKENS ─────────────────────────────── */
    :root {
        --bg-deep:     #020917;   /* deepest background */
        --bg-main:     #050f22;   /* page background    */
        --bg-card:     #0a1a35;   /* card surface       */
        --bg-hover:    #0d2246;   /* card hover         */
        --border:      #1a3260;   /* borders            */
        --border-soft: #122850;   /* subtle dividers    */

        --primary:     #2563eb;   /* primary blue       */
        --primary-lt:  #3b82f6;   /* lighter blue       */
        --primary-dk:  #1d4ed8;   /* darker blue        */

        --gold:        #f59e0b;   /* accent gold        */
        --teal:        #06b6d4;   /* accent teal        */
        --green:       #10b981;   /* success            */
        --red:         #ef4444;   /* danger             */
        --orange:      #f97316;   /* warning            */

        /* Backward-compatible aliases used by existing home/dashboard markup */
        --primary-blue: var(--primary);
        --accent-teal: var(--teal);
        --secondary-gold: var(--gold);
        --green-success: var(--green);

        /* TEXT — all white/near-white for maximum readability */
        --text-primary:   #ffffff;
        --text-secondary: #e2e8f0;
        --text-body:      #cbd5e1;
        --text-muted:     #94a3b8;
        --text-faint:     #64748b;
    }

    /* ── BASE ───────────────────────────────────────────── */
    html, body,
    [data-testid="stAppViewContainer"],
    [data-testid="stMain"],
    .main {
        background-color: var(--bg-main) !important;
        color: var(--text-primary) !important;
        font-family: 'Noto Sans', sans-serif !important;
    }
    [data-testid="stHeader"] { background: transparent !important; }
    .block-container { padding: 1.5rem 2.5rem !important; max-width: 1400px; }

    /* ── HEADINGS ───────────────────────────────────────── */
    h1, h2, h3, h4, h5, h6 {
        font-family: 'Rajdhani', sans-serif !important;
        color: var(--text-primary) !important;
        letter-spacing: .03em;
    }
    p, li, span, label, div {
        color: var(--text-body);
    }

    /* ── STREAMLIT LABELS AND CAPTIONS ─────────────────── */
    .stMarkdown p          { color: var(--text-body) !important; }
    [data-testid="stCaption"] { color: var(--text-muted) !important; }
    label[data-testid="stWidgetLabel"] > div > p { color: var(--text-secondary) !important; }

    /* ── BUTTONS ────────────────────────────────────────── */
    .stButton > button {
        background: var(--primary) !important;
        color: #ffffff !important;
        border: none !important;
        border-radius: 8px !important;
        font-family: 'Rajdhani', sans-serif !important;
        font-size: 1rem !important;
        font-weight: 600 !important;
        letter-spacing: .06em !important;
        padding: .55rem 1.4rem !important;
        transition: background .2s, transform .15s !important;
    }
    .stButton > button:hover {
        background: var(--primary-dk) !important;
        transform: translateY(-1px) !important;
        color: #ffffff !important;
    }

    /* Secondary / back buttons */
    .secondary-btn-container .stButton > button {
        background: var(--bg-card) !important;
        color: var(--text-secondary) !important;
        border: 1px solid var(--border) !important;
    }
    .secondary-btn-container .stButton > button:hover {
        background: var(--bg-hover) !important;
        border-color: var(--primary) !important;
        color: #ffffff !important;
    }

    /* Citizen portal button - gold accent */
    .citizen-btn-container .stButton > button {
        background: linear-gradient(135deg, var(--primary) 0%, #1e40af 100%) !important;
        color: #ffffff !important;
        border: 1px solid var(--primary-lt) !important;
        font-size: 1.05rem !important;
        padding: .7rem 1.6rem !important;
    }

    /* ── INPUTS ─────────────────────────────────────────── */
    .stTextInput > div > div > input,
    .stTextArea  > div > div > textarea,
    .stSelectbox > div > div,
    .stNumberInput > div > div > input {
        background-color: var(--bg-card) !important;
        color: var(--text-primary) !important;
        border: 1px solid var(--border) !important;
        border-radius: 8px !important;
        caret-color: var(--primary-lt) !important;
    }
    .stTextInput > div > div > input::placeholder,
    .stTextArea  > div > div > textarea::placeholder {
        color: var(--text-faint) !important;
    }
    .stTextInput > div > div > input:focus,
    .stTextArea  > div > div > textarea:focus {
        border-color: var(--primary-lt) !important;
        box-shadow: 0 0 0 2px rgba(59,130,246,.25) !important;
        color: var(--text-primary) !important;
    }
    /* Selectbox option text */
    .stSelectbox > div > div > div {
        color: var(--text-primary) !important;
    }

    /* ── DATAFRAME / TABLE ──────────────────────────────── */
    [data-testid="stDataFrame"] {
        background: var(--bg-card) !important;
        border: 1px solid var(--border) !important;
        border-radius: 10px !important;
    }
    [data-testid="stDataFrame"] thead th {
        background: var(--bg-deep) !important;
        color: var(--text-secondary) !important;
    }
    [data-testid="stDataFrame"] tbody td {
        color: var(--text-primary) !important;
        background: var(--bg-card) !important;
    }

    /* ── METRICS ────────────────────────────────────────── */
    [data-testid="stMetricValue"] {
        color: var(--primary-lt) !important;
        font-family: 'Rajdhani', sans-serif !important;
        font-size: 2rem !important;
    }
    [data-testid="stMetricLabel"] {
        color: var(--text-muted) !important;
        font-size: .8rem !important;
        text-transform: uppercase;
        letter-spacing: .06em;
    }
    [data-testid="stMetric"] {
        background: var(--bg-card) !important;
        border: 1px solid var(--border) !important;
        border-radius: 10px !important;
        padding: 1rem 1.2rem !important;
    }

    /* ── EXPANDERS (FAQ) ────────────────────────────────── */
    [data-testid="stExpander"] {
        background: var(--bg-card) !important;
        border: 1px solid var(--border) !important;
        border-radius: 10px !important;
        margin-bottom: .5rem !important;
    }
    [data-testid="stExpander"] summary {
        color: var(--text-secondary) !important;
        font-weight: 600 !important;
    }
    [data-testid="stExpander"] summary:hover {
        color: var(--text-primary) !important;
    }
    [data-testid="stExpander"] [data-testid="stMarkdownContainer"] p {
        color: var(--text-body) !important;
    }

    /* ── ALERTS ─────────────────────────────────────────── */
    [data-testid="stAlert"] {
        border-radius: 10px !important;
    }
    .stSuccess { background: rgba(16,185,129,.12) !important; border: 1px solid rgba(16,185,129,.3) !important; color: #6ee7b7 !important; }
    .stError   { background: rgba(239,68,68,.12)  !important; border: 1px solid rgba(239,68,68,.3)  !important; color: #fca5a5 !important; }
    .stWarning { background: rgba(245,158,11,.12) !important; border: 1px solid rgba(245,158,11,.3) !important; color: #fcd34d !important; }
    .stInfo    { background: rgba(37,99,235,.12)  !important; border: 1px solid rgba(37,99,235,.3)  !important; color: #93c5fd !important; }

    /* ── DIVIDER ────────────────────────────────────────── */
    hr { border-color: var(--border) !important; opacity: 1 !important; }

    /* ── PLOTLY CHARTS — force dark background ──────────── */
    .js-plotly-plot .plotly { background: transparent !important; }

    /* ── CUSTOM COMPONENT CLASSES ───────────────────────── */

    /* Hero section */
    .hero-wrap {
        background: linear-gradient(135deg, #020c1f 0%, #071235 50%, #030d22 100%);
        border: 1px solid var(--border);
        border-radius: 16px;
        padding: 3rem 2.5rem;
        margin-bottom: 2rem;
        position: relative;
        overflow: hidden;
    }
    .hero-wrap::before {
        content: '';
        position: absolute; top: -60px; right: -60px;
        width: 280px; height: 280px;
        background: radial-gradient(circle, rgba(37,99,235,.2) 0%, transparent 70%);
        pointer-events: none;
    }
    .hero-tag {
        font-size: .72rem; letter-spacing: .18em; text-transform: uppercase;
        color: var(--teal); margin-bottom: .6rem; font-weight: 600;
    }
    .hero-title {
        font-family: 'Rajdhani', sans-serif;
        font-size: 2.8rem; font-weight: 700;
        line-height: 1.15; color: #ffffff; margin-bottom: .8rem;
    }
    .hero-title span { color: var(--gold); }
    .hero-sub {
        color: var(--text-muted); font-size: 1rem;
        max-width: 560px; line-height: 1.65;
    }

    /* Stat tiles */
    .stat-tile {
        background: var(--bg-card);
        border: 1px solid var(--border);
        border-radius: 12px;
        padding: 1.3rem 1.4rem;
        text-align: center;
        transition: border-color .2s;
    }
    .stat-tile:hover { border-color: var(--primary-lt); }
    .stat-tile .num {
        font-family: 'Rajdhani', sans-serif;
        font-size: 2.2rem; font-weight: 700;
        color: var(--primary-lt); line-height: 1;
    }
    .stat-tile .lbl {
        font-size: .76rem; color: var(--text-muted);
        letter-spacing: .06em; text-transform: uppercase; margin-top: .35rem;
    }

    /* Portal cards */
    .portal-card {
        background: var(--bg-card);
        border: 1px solid var(--border);
        border-radius: 14px;
        padding: 2rem 1.8rem;
        min-height: 220px;
        transition: border-color .2s, background .2s;
    }
    .portal-card:hover { border-color: var(--primary-lt); background: var(--bg-hover); }
    .portal-icon {
        font-size: 2rem; color: var(--primary-lt);
        margin-bottom: .8rem;
    }
    .portal-title {
        font-family: 'Rajdhani', sans-serif;
        font-size: 1.4rem; font-weight: 700;
        color: var(--text-primary); margin-bottom: .5rem;
    }
    .portal-desc { color: var(--text-muted); font-size: .95rem; line-height: 1.6; }

    /* Generic card */
    .lk-card {
        background: var(--bg-card);
        border: 1px solid var(--border);
        border-radius: 12px;
        padding: 1.4rem 1.6rem;
        margin-bottom: 1rem;
        transition: border-color .2s;
    }
    .lk-card:hover { border-color: var(--primary-lt); }
    .lk-card h4 { color: var(--text-primary) !important; }
    .lk-card p  { color: var(--text-body)    !important; }
    .lk-card li { color: var(--text-body)    !important; }

    /* Status badges */
    .badge { display: inline-block; padding: .2rem .65rem; border-radius: 99px; font-size: .72rem; font-weight: 600; letter-spacing: .05em; }
    .badge-pending  { background: rgba(245,158,11,.15); color: #fcd34d; border: 1px solid rgba(245,158,11,.3); }
    .badge-progress { background: rgba(6,182,212,.15);  color: #67e8f9; border: 1px solid rgba(6,182,212,.3); }
    .badge-resolved { background: rgba(16,185,129,.15); color: #6ee7b7; border: 1px solid rgba(16,185,129,.3); }
    .badge-escalate { background: rgba(239,68,68,.15);  color: #fca5a5; border: 1px solid rgba(239,68,68,.3); }

    /* Complaint ID display */
    .complaint-id {
        font-family: 'Rajdhani', sans-serif;
        font-size: 2rem; font-weight: 700;
        color: var(--gold); letter-spacing: .12em;
    }

    /* Submit button container */
    .submit-btn-container .stButton > button {
        background: linear-gradient(135deg, var(--primary) 0%, #1e40af 100%) !important;
        color: #ffffff !important;
        font-size: 1.1rem !important;
        padding: .8rem 2rem !important;
        border-radius: 10px !important;
        border: 1px solid var(--primary-lt) !important;
    }
    .submit-btn-container .stButton > button:hover {
        background: linear-gradient(135deg, var(--primary-dk) 0%, #1e3a8a 100%) !important;
        transform: translateY(-2px) !important;
    }

    /* Track button */
    .track-btn-container .stButton > button {
        background: transparent !important;
        color: var(--primary-lt) !important;
        border: 1px solid var(--primary) !important;
        font-size: .95rem !important;
    }
    .track-btn-container .stButton > button:hover {
        background: var(--primary) !important;
        color: #ffffff !important;
    }
    </style>
    """, unsafe_allow_html=True)
    