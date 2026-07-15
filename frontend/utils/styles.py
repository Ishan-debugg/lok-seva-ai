import streamlit as st

def inject_global_styles():
    st.markdown("""
    <style>
<<<<<<< HEAD
    @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;500;600;700;800&family=Inter:wght@300;400;500;600;700&family=Rajdhani:wght@500;600;700&display=swap');
    @import url('https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css');

    /* ── ROOT DESIGN VARIABLES (LIGHT FORMAL THEME) ── */
    :root {
        --bg-main:       #f8fafc; /* light slate */
        --bg-card:       #ffffff; /* crisp white cards */
        --border-color:  #cbd5e1; /* slate 300 */
        --primary-blue:  #1e3a8a; /* corporate navy blue */
        --secondary-gold: #b45309; /* amber 700 / gold accent */
        --accent-teal:   #0284c7; /* sky 600 */
        --green-success: #16a34a; /* green 600 */
        --red-danger:    #dc2626; /* red 600 */
        --text-dark:     #0f172a; /* slate 900 */
        --text-body:     #334155; /* slate 700 */
        --text-muted:    #64748b; /* slate 500 */
        --input-bg:      #ffffff;
    }

    /* ── BASE APPLICATION OVERRIDES ── */
    html, body, [data-testid="stAppViewContainer"] {
        background: var(--bg-main) !important;
        color: var(--text-body) !important;
        font-family: 'Inter', sans-serif !important;
    }
    [data-testid="stHeader"] { background: transparent !important; }
    [data-testid="stSidebar"] { 
        background: #0f172a !important; /* contrast sidebar */
        border-right: 1px solid var(--border-color); 
    }
    .block-container { padding: 2.5rem 3.5rem !important; max-width: 1400px; }

    /* ── TYPOGRAPHY ── */
    h1, h2, h3, h4 { 
        font-family: 'Outfit', sans-serif !important; 
        color: var(--text-dark) !important; 
        letter-spacing: -0.02em; 
        font-weight: 700 !important;
    }

    /* ── BUTTONS ── */
    .stButton > button {
        background: var(--primary-blue) !important;
        color: white !important;
        border: 1px solid var(--primary-blue) !important;
        border-radius: 8px !important;
        font-family: 'Outfit', sans-serif !important;
        font-size: 1.05rem !important;
        font-weight: 600 !important;
        letter-spacing: 0.02em !important;
        padding: 0.6rem 1.6rem !important;
        box-shadow: 0 4px 6px -1px rgba(30, 58, 138, 0.15) !important;
        transition: background 0.2s, transform 0.15s, box-shadow 0.2s !important;
    }
    .stButton > button:hover { 
        background: #1d4ed8 !important; 
        transform: translateY(-1px) !important; 
        box-shadow: 0 10px 15px -3px rgba(30, 58, 138, 0.25) !important;
        border-color: #1d4ed8 !important;
    }
    
    /* Secondary button styling (Back to Home, etc) */
    .secondary-btn-container .stButton > button {
        background: transparent !important;
        color: var(--primary-blue) !important;
        border: 1.5px solid var(--primary-blue) !important;
        box-shadow: none !important;
    }
    .secondary-btn-container .stButton > button:hover {
        background: rgba(30, 58, 138, 0.05) !important;
        border-color: var(--primary-blue) !important;
        color: var(--primary-blue) !important;
    }

    /* ── INPUTS & FORM CONTROLS ── */
    input, textarea, select, 
    .stTextInput input, .stTextArea textarea, 
    .stSelectbox div, .stSelectbox span, .stSelectbox select,
    div[data-baseweb="select"] *, [data-testid="stSelectbox"] *,
    div[class*="-singleValue"], div[class*="-singleValue"] *,
    .stSelectbox div[class^="st-"], .stSelectbox span[class^="st-"] {
        color: #0f172a !important;
        -webkit-text-fill-color: #0f172a !important; /* Force color fill */
    }

    .stTextInput > div > div > input,
    .stTextArea > div > div > textarea {
        background: var(--input-bg) !important;
        border: 1.5px solid var(--border-color) !important;
        border-radius: 8px !important;
        padding: 0.5rem !important;
        font-size: 1rem !important;
        transition: border-color 0.2s, box-shadow 0.2s !important;
    }

    .stSelectbox > div > div {
        background: var(--input-bg) !important;
        border: 1.5px solid var(--border-color) !important;
        border-radius: 8px !important;
        font-size: 1rem !important;
        transition: border-color 0.2s, box-shadow 0.2s !important;
    }
    .stTextInput > div > div > input:focus,
    .stTextArea > div > div > textarea:focus { 
        border-color: var(--primary-blue) !important; 
        box-shadow: 0 0 0 3px rgba(30, 58, 138, 0.15) !important; 
    }
    
    /* Dropdown Options Listbox overrides */
    div[role="listbox"] {
        background-color: var(--bg-card) !important;
        border: 1px solid var(--border-color) !important;
    }
    div[role="option"] {
        background-color: var(--bg-card) !important;
    }
    div[role="option"] * {
        color: var(--text-dark) !important;
    }
    div[role="option"]:hover, div[role="option"][aria-selected="true"] {
        background-color: var(--bg-main) !important;
    }

    /* ── RESPONSIVE MEDIA QUERIES ── */
    @media (max-width: 768px) {
        .block-container { padding: 1rem 1.5rem !important; }
        .hero-wrap { padding: 2rem 1.5rem !important; margin-bottom: 1.5rem; }
        .hero-title { font-size: 2.2rem !important; }
        .hero-sub { font-size: 0.95rem !important; }
        .stat-tile { padding: 1rem 0.8rem !important; }
        .stat-tile .num { font-size: 1.8rem !important; }
    }
    
    /* Input Labels */
    label[data-testid="stWidgetLabel"] p {
        color: var(--text-dark) !important;
        font-weight: 600 !important;
        font-size: 0.95rem !important;
    }

    /* ── CUSTOM CARDS ── */
    .lk-card {
        background: var(--bg-card);
        border: 1px solid var(--border-color);
        border-radius: 12px;
        padding: 1.8rem 2.2rem;
        margin-bottom: 1.5rem;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05);
        transition: border-color 0.2s, box-shadow 0.2s;
    }
    .lk-card:hover { 
        border-color: var(--primary-blue); 
        box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.08);
    }

    /* ── HERO BANNER ── */
    .hero-wrap {
        background: linear-gradient(135deg, #1e3a8a 0%, #1e40af 50%, #0f172a 100%);
        border: none;
        border-radius: 16px;
        padding: 3.5rem 3rem;
        margin-bottom: 2.5rem;
        position: relative;
        overflow: hidden;
        box-shadow: 0 10px 25px -5px rgba(30, 58, 138, 0.3);
    }
    .hero-wrap::before {
        content: '';
        position: absolute;
        width: 350px;
        height: 350px;
        background: radial-gradient(circle, rgba(245, 158, 11, 0.15) 0%, rgba(245, 158, 11, 0) 70%);
        top: -100px;
        right: -80px;
        border-radius: 50%;
        pointer-events: none;
    }
    .hero-wrap::after {
        content: '';
        position: absolute;
        width: 400px;
        height: 400px;
        background: radial-gradient(circle, rgba(2, 132, 199, 0.2) 0%, rgba(2, 132, 199, 0) 70%);
        bottom: -200px;
        left: -100px;
        border-radius: 50%;
        pointer-events: none;
    }
    .hero-tag { font-size:.8rem; letter-spacing:.2em; text-transform:uppercase; color:#38bdf8; margin-bottom:.8rem; font-weight:700; position: relative; z-index: 2; }
    .hero-title { font-family:'Outfit',sans-serif; font-size:3.2rem; font-weight:800; line-height:1.15; color:#ffffff; margin-bottom:.8rem; position: relative; z-index: 2; }
    .hero-title span { color:#f59e0b; }
    .hero-sub { color:#e2e8f0; font-size:1.1rem; max-width:620px; line-height:1.65; position: relative; z-index: 2; }

    /* ── PORTAL ACCESS CARDS ── */
    .portal-card {
        background: var(--bg-card) !important;
        border: 1px solid var(--border-color) !important;
        border-radius: 16px !important;
        padding: 2.2rem !important;
        text-align: center !important;
        box-shadow: 0 10px 20px -5px rgba(0, 0, 0, 0.05) !important;
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1) !important;
        height: 100% !important;
        display: flex !important;
        flex-direction: column !important;
        justify-content: space-between !important;
    }
    .portal-card:hover {
        transform: translateY(-8px) !important;
        border-color: var(--primary-blue) !important;
        box-shadow: 0 20px 25px -5px rgba(30, 58, 138, 0.12), 0 10px 10px -5px rgba(30, 58, 138, 0.06) !important;
    }
    .portal-icon {
        font-size: 3.2rem !important;
        color: var(--primary-blue) !important;
        margin-bottom: 1.2rem !important;
        transition: transform 0.3s ease, color 0.3s ease !important;
    }
    .portal-card:hover .portal-icon {
        transform: scale(1.1) rotate(2deg) !important;
        color: var(--secondary-gold) !important;
    }
    .portal-title {
        font-family: 'Outfit', sans-serif !important;
        font-size: 1.5rem !important;
        font-weight: 700 !important;
        color: var(--text-dark) !important;
        margin-bottom: 0.8rem !important;
    }
    .portal-desc {
        font-size: 0.95rem !important;
        color: var(--text-body) !important;
        line-height: 1.6 !important;
        margin-bottom: 1.5rem !important;
        flex-grow: 1 !important;
    }

    /* ── CUSTOM STAT TILES ── */
    .stat-tile {
        background: var(--bg-card);
        border: 1px solid var(--border-color);
        border-radius: 12px;
        padding: 1.5rem 1rem;
        text-align: center;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05);
        transition: transform 0.2s, box-shadow 0.2s;
    }
    .stat-tile:hover {
        transform: translateY(-2px);
        box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.08);
        border-color: var(--primary-blue);
    }
    .stat-tile .num {
        font-family: 'Outfit', sans-serif;
        font-size: 2.4rem;
        font-weight: 800;
        color: var(--primary-blue);
        line-height: 1.1;
    }
    .stat-tile .lbl {
        font-size: 0.8rem;
        font-weight: 700;
        color: var(--text-muted);
        letter-spacing: 0.05em;
        text-transform: uppercase;
        margin-top: 0.4rem;
    }

    /* ── BADGES & STATUSES ── */
    .badge { display:inline-block; padding:.25rem .75rem; border-radius:99px; font-size:.78rem; font-weight:700; letter-spacing:.05em; text-transform:uppercase; }
    .badge-pending  { background:#fef3c7; color:#b45309; border: 1px solid #fde68a; }
    .badge-progress { background:#e0f2fe; color:#0369a1; border: 1px solid #bae6fd; }
    .badge-resolved { background:#dcfce7; color:#15803d; border: 1px solid #bbf7d0; }
    .badge-escalate { background:#f3e8ff; color:#6b21a8; border: 1px solid #e9d5ff; }

    /* ── COMPLAINT ID LABEL ── */
    .complaint-id { font-family:'Outfit',sans-serif; font-size:2.2rem; font-weight:800; color:var(--secondary-gold); letter-spacing:.02em; }

    /* ── STREAMLIT METRICS OVERRIDE (BACKUP) ── */
    [data-testid="stMetricValue"] { color: var(--primary-blue) !important; font-family:'Outfit',sans-serif !important; font-weight:800 !important; }
    [data-testid="stMetricLabel"] p { color: var(--text-muted) !important; font-weight:600 !important; }

    /* ── GOLD CITIZEN ACTION BUTTONS ── */
    .track-btn-container .stButton > button,
    .citizen-btn-container .stButton > button,
    .submit-btn-container .stButton > button {
        background: var(--secondary-gold) !important;
        border-color: var(--secondary-gold) !important;
        color: white !important;
        box-shadow: 0 4px 6px -1px rgba(180, 83, 9, 0.15) !important;
    }
    .track-btn-container .stButton > button:hover,
    .citizen-btn-container .stButton > button:hover,
    .submit-btn-container .stButton > button:hover {
        background: #d97706 !important;
        border-color: #d97706 !important;
        box-shadow: 0 10px 15px -3px rgba(180, 83, 9, 0.25) !important;
        color: white !important;
    }

    /* ── STEPPER TIMELINE styling ── */
    .stepper-wrapper {
        display: flex;
        justify-content: space-between;
        margin-top: 2rem;
        margin-bottom: 2.5rem;
        position: relative;
    }
    .stepper-wrapper::before {
        content: '';
        position: absolute;
        top: 25px;
        left: 0;
        width: 100%;
        height: 4px;
        background-color: var(--border-color);
        z-index: 1;
    }
    .stepper-progress {
        position: absolute;
        top: 25px;
        left: 0;
        height: 4px;
        background-color: var(--green-success);
        z-index: 1;
        transition: width 0.4s ease;
    }
    .stepper-item {
        display: flex;
        flex-direction: column;
        align-items: center;
        position: relative;
        z-index: 2;
        flex: 1;
    }
    .stepper-item .step-counter {
        width: 50px;
        height: 50px;
        border-radius: 50%;
        background-color: #ffffff;
        border: 3px solid var(--border-color);
        display: flex;
        justify-content: center;
        align-items: center;
        font-weight: 700;
        font-size: 1.2rem;
        color: var(--text-muted);
        transition: all 0.3s ease;
    }
    .stepper-item.completed .step-counter {
        background-color: var(--green-success);
        border-color: var(--green-success);
        color: #ffffff;
    }
    .stepper-item.active .step-counter {
        background-color: #ffffff;
        border-color: var(--primary-blue);
        color: var(--primary-blue);
        box-shadow: 0 0 0 5px rgba(30, 58, 138, 0.15);
    }
    .stepper-item .step-name {
        margin-top: 0.6rem;
        font-size: 0.85rem;
        font-weight: 700;
        text-transform: uppercase;
        letter-spacing: 0.05em;
        color: var(--text-muted);
    }
    .stepper-item.completed .step-name {
        color: var(--green-success);
    }
    .stepper-item.active .step-name {
        color: var(--primary-blue);
    }

    /* ── MISC STYLING ── */
    .divider { height:1px; background:var(--border-color); margin:1.5rem 0; }
    .muted { color:var(--text-muted); font-size:.85rem; }
    hr { border-color: var(--border-color) !important; }
=======
    @import url('https://fonts.googleapis.com/css2?family=Rajdhani:wght@400;500;600;700&family=Noto+Sans:ital,wght@0,300;0,400;0,600;1,300&display=swap');

    /* ── ROOT VARIABLES ── */
    :root {
        --navy:   #0a0f1e;
        --ink:    #0d1630;
        --card:   #111b35;
        --border: #1e2f55;
        --accent: #2563eb;
        --gold:   #f59e0b;
        --teal:   #06b6d4;
        --green:  #10b981;
        --red:    #ef4444;
        --muted:  #64748b;
        --text:   #e2e8f0;
        --soft:   #94a3b8;
    }

    /* ── BASE ── */
    html, body, [data-testid="stAppViewContainer"] {
        background: var(--navy) !important;
        color: var(--text) !important;
        font-family: 'Noto Sans', sans-serif !important;
    }
    [data-testid="stHeader"] { background: transparent !important; }
    [data-testid="stSidebar"] { background: var(--ink) !important; border-right: 1px solid var(--border); }
    .block-container { padding: 1.5rem 2rem !important; max-width: 1400px; }

    /* ── HEADINGS ── */
    h1, h2, h3, h4 { font-family: 'Rajdhani', sans-serif !important; color: var(--text) !important; letter-spacing: .03em; }

    /* ── BUTTONS ── */
    .stButton > button {
        background: var(--accent) !important;
        color: white !important;
        border: none !important;
        border-radius: 6px !important;
        font-family: 'Rajdhani', sans-serif !important;
        font-size: 1rem !important;
        font-weight: 600 !important;
        letter-spacing: .06em !important;
        padding: .55rem 1.4rem !important;
        transition: background .2s, transform .15s !important;
    }
    .stButton > button:hover { background: #1d4ed8 !important; transform: translateY(-1px) !important; }

    /* ── INPUTS ── */
    .stTextInput > div > div > input,
    .stTextArea > div > div > textarea,
    .stSelectbox > div > div {
        background: var(--card) !important;
        color: var(--text) !important;
        border: 1px solid var(--border) !important;
        border-radius: 6px !important;
    }
    .stTextInput > div > div > input:focus,
    .stTextArea > div > div > textarea:focus { border-color: var(--accent) !important; box-shadow: 0 0 0 2px rgba(37,99,235,.25) !important; }

    /* ── CARDS ── */
    .lk-card {
        background: var(--card);
        border: 1px solid var(--border);
        border-radius: 12px;
        padding: 1.4rem 1.6rem;
        margin-bottom: 1rem;
        transition: border-color .2s;
    }
    .lk-card:hover { border-color: var(--accent); }

    /* ── STAT TILES ── */
    .stat-tile {
        background: var(--card);
        border: 1px solid var(--border);
        border-radius: 10px;
        padding: 1.2rem 1.4rem;
        text-align: center;
    }
    .stat-tile .num { font-family:'Rajdhani',sans-serif; font-size:2.2rem; font-weight:700; color:var(--accent); line-height:1; }
    .stat-tile .lbl { font-size:.78rem; color:var(--soft); letter-spacing:.06em; text-transform:uppercase; margin-top:.3rem; }

    /* ── BADGE STATUS ── */
    .badge { display:inline-block; padding:.2rem .65rem; border-radius:99px; font-size:.72rem; font-weight:600; letter-spacing:.05em; }
    .badge-pending  { background:#422006; color:#fbbf24; }
    .badge-progress { background:#0c2a4a; color:#38bdf8; }
    .badge-resolved { background:#052e16; color:#4ade80; }
    .badge-escalate { background:#3b0764; color:#e879f9; }

    /* ── NAV TABS ── */
    .lk-nav { display:flex; gap:.6rem; margin-bottom:1.6rem; flex-wrap:wrap; }
    .lk-tab {
        background:var(--card); border:1px solid var(--border);
        color:var(--soft); border-radius:8px; padding:.5rem 1.1rem;
        cursor:pointer; font-family:'Rajdhani',sans-serif;
        font-size:.95rem; font-weight:600; letter-spacing:.05em;
        transition: all .2s; text-decoration:none; display:inline-block;
    }
    .lk-tab.active { background:var(--accent); border-color:var(--accent); color:#fff; }

    /* ── HERO ── */
    .hero-wrap {
        background: linear-gradient(135deg, #0a1628 0%, #0d2050 50%, #091428 100%);
        border: 1px solid var(--border);
        border-radius: 16px;
        padding: 3rem 2.5rem;
        margin-bottom: 2rem;
        position: relative;
        overflow: hidden;
    }
    .hero-wrap::before {
        content:'';
        position:absolute; top:-60px; right:-60px;
        width:260px; height:260px;
        background: radial-gradient(circle, rgba(37,99,235,.18) 0%, transparent 70%);
        pointer-events:none;
    }
    .hero-tag { font-size:.72rem; letter-spacing:.18em; text-transform:uppercase; color:var(--teal); margin-bottom:.6rem; font-weight:600; }
    .hero-title { font-family:'Rajdhani',sans-serif; font-size:2.8rem; font-weight:700; line-height:1.15; color:#fff; margin-bottom:.8rem; }
    .hero-title span { color:var(--gold); }
    .hero-sub { color:var(--soft); font-size:1rem; max-width:560px; line-height:1.65; }

    /* ── TABLE ── */
    .lk-table { width:100%; border-collapse:collapse; font-size:.88rem; }
    .lk-table th { background:var(--ink); color:var(--soft); text-transform:uppercase; font-size:.72rem; letter-spacing:.09em; padding:.7rem 1rem; border-bottom:1px solid var(--border); text-align:left; }
    .lk-table td { padding:.75rem 1rem; border-bottom:1px solid var(--border); color:var(--text); vertical-align:middle; }
    .lk-table tr:last-child td { border-bottom:none; }
    .lk-table tr:hover td { background:rgba(37,99,235,.06); }

    /* ── COMPLAINT ID ── */
    .complaint-id { font-family:'Rajdhani',sans-serif; font-size:2rem; font-weight:700; color:var(--gold); letter-spacing:.12em; }

    /* ── MISC ── */
    .divider { height:1px; background:var(--border); margin:1.5rem 0; }
    .muted { color:var(--muted); font-size:.85rem; }
    hr { border-color: var(--border) !important; }
    [data-testid="stMetricValue"] { color: var(--accent) !important; font-family:'Rajdhani',sans-serif !important; }
>>>>>>> f36f5b7d3817ef6c49a4ac12405051899e1f77ca
    </style>
    """, unsafe_allow_html=True)
