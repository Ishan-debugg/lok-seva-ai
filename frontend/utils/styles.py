import streamlit as st

def inject_global_styles():

    # Inject font and icon CDN separately — never mix link tags with style tags
    st.markdown(
        '<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.0/css/all.min.css"/>',
        unsafe_allow_html=True
    )
    st.markdown(
        '<link rel="preconnect" href="https://fonts.googleapis.com">'
        '<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>'
        '<link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=Rajdhani:wght@500;600;700&display=swap" rel="stylesheet">',
        unsafe_allow_html=True
    )

    # Main stylesheet — single clean style block, no link tags mixed in
    st.markdown("""<style>
    [data-testid="stSidebar"],
    [data-testid="collapsedControl"],
    [data-testid="stSidebarNav"],
    section[data-testid="stSidebar"] { display: none !important; }

    :root {
        --bg:        #f0f4f8;
        --bg-card:   #ffffff;
        --bg-input:  #f8fafc;
        --navy:      #0f2547;
        --navy-lt:   #1e3a5f;
        --navy-md:   #163263;
        --gold:      #f59e0b;
        --gold-dk:   #d97706;
        --green:     #15803d;
        --green-lt:  #166534;
        --text-h:    #0f2547;
        --text-b:    #1e293b;
        --text-s:    #475569;
        --text-m:    #94a3b8;
        --border:    #e2e8f0;
        --border-md: #cbd5e1;
    }

    html, body,
    [data-testid="stAppViewContainer"],
    [data-testid="stMain"], .main {
        background-color: var(--bg) !important;
        color: var(--text-b) !important;
        font-family: 'Inter', sans-serif !important;
    }
    [data-testid="stHeader"] { background: transparent !important; }
    .block-container { padding: 1.5rem 2.5rem !important; max-width: 1400px; }

    [data-testid="stHorizontalBlock"] { align-items: stretch !important; }
    [data-testid="column"] { display: flex !important; flex-direction: column !important; }
    [data-testid="column"] > div[data-testid="stVerticalBlock"] {
        flex: 1 !important; display: flex !important; flex-direction: column !important;
    }

    h1, h2, h3, h4, h5, h6 {
        font-family: 'Rajdhani', sans-serif !important;
        color: var(--text-h) !important;
    }
    p, li { color: var(--text-b); }
    .stMarkdown p:not(.hero-sub) {
    color: var(--text-b) !important;
    }
    [data-testid="stCaption"] { color: var(--text-m) !important; }
    label[data-testid="stWidgetLabel"] > div > p { color: var(--text-s) !important; }

    .stButton > button {
        background: #0E7A00 !important;
        color: #ffffff !important;
        border: none !important;
        border-radius: 8px !important;
        font-family: 'Inter', sans-serif !important;
        font-size: .95rem !important;
        font-weight: 600 !important;
        padding: .55rem 1.4rem !important;
    }
    .stButton > button span,
    .stButton > button p,
    .stButton > button div { color: #ffffff !important; }
    .stButton > button:hover { background: #095c00 !important; }

    .secondary-btn-container .stButton > button {
        background: #ffffff !important;
        color: var(--navy) !important;
        border: 1.5px solid var(--border-md) !important;
    }
    .secondary-btn-container .stButton > button span,
    .secondary-btn-container .stButton > button p {
        color: var(--navy) !important;
        background: transparent !important;
    }

    .citizen-btn-container .stButton > button {
        background: var(--green) !important;
        color: #ffffff !important;
        font-size: 1.05rem !important;
        padding: .7rem 1.6rem !important;
        border-radius: 10px !important;
    }
    .official-btn-container .stButton > button {
        background: var(--navy) !important;
        color: #ffffff !important;
        font-size: 1.05rem !important;
        padding: .7rem 1.6rem !important;
        border-radius: 10px !important;
    }
    .submit-btn-container .stButton > button {
        background: var(--green) !important;
        color: #ffffff !important;
        font-size: 1.05rem !important;
        padding: .75rem 2rem !important;
        border-radius: 10px !important;
    }
    .track-btn-container .stButton > button {
        background: var(--navy) !important;
        color: #ffffff !important;
        border: 1.5px solid var(--navy) !important;
    }

    [data-testid="stDownloadButton"] > button {
        background: var(--navy) !important;
        color: #ffffff !important;
        border-radius: 8px !important;
        font-weight: 600 !important;
        border: none !important;
    }
    [data-testid="stDownloadButton"] > button span,
    [data-testid="stDownloadButton"] > button p { color: #ffffff !important; }

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
        text-transform: uppercase;
        letter-spacing: .07em;
    }

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

    [data-testid="stExpander"] {
        background: var(--bg-card) !important;
        border: 1.5px solid var(--border) !important;
        border-radius: 10px !important;
        margin-bottom: .5rem !important;
    }
    [data-testid="stExpander"] summary { color: var(--text-h) !important; font-weight: 600 !important; }
    [data-testid="stExpander"] [data-testid="stMarkdownContainer"] p { color: var(--text-b) !important; }

    [data-testid="stAlert"] { border-radius: 10px !important; }
    hr { border-color: var(--border) !important; opacity: 1 !important; }

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
    .hero-sub { color: #cbd5e1; font-size: .95rem; max-width: 560px; line-height: 1.65; }
    .hero-sub p { color: #cbd5e1 !important; }

    .stat-tile {
        background: var(--bg-card);
        border: 1.5px solid var(--border);
        border-radius: 12px;
        padding: 1.5rem 1.6rem;
        text-align: center;
        height: 100%;
    }
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

    .portal-card {
        background: var(--bg-card);
        border: 1.5px solid var(--border);
        border-top: 4px solid var(--gold);
        border-radius: 14px;
        padding: 2.2rem 2rem 1.8rem 2rem;
        min-height: 230px;
        text-align: center;
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        box-sizing: border-box;
    }
    .portal-icon { font-size: 2.4rem; color: var(--navy); margin-bottom: .8rem; }
    .portal-title {
        font-family: 'Rajdhani', sans-serif;
        font-size: 1.5rem; font-weight: 700;
        color: var(--navy); margin-bottom: .5rem;
    }
    .portal-desc { color: var(--text-s); font-size: .92rem; line-height: 1.6; }

    .lk-card {
        background: var(--bg-card);
        border: 1.5px solid var(--border);
        border-radius: 12px;
        padding: 1.4rem 1.6rem;
        margin-bottom: 1rem;
    }
    .lk-card h4 { color: var(--text-h) !important; }
    .lk-card p, .lk-card li { color: var(--text-b) !important; }

    .complaint-id {
        font-family: 'Rajdhani', sans-serif;
        font-size: 2.2rem; font-weight: 700;
        color: var(--gold); letter-spacing: .1em;
    }

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
    </style>""", unsafe_allow_html=True)
    