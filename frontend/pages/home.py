import streamlit as st

def render():
    st.markdown("""
    <div class="hero-wrap">
        <div class="hero-tag">
            <i class="fa-solid fa-building-columns" style="margin-right:6px;"></i>
            MUNICIPAL CORPORATION PORTAL
        </div>
        <div class="hero-title">Welcome to <span>LokSevaAI</span></div>
        <p class="hero-sub">
        LokSevaAI is the smart civic grievance redressal and routing platform.
        Powered by artificial intelligence, we automatically route your complaints
        to correct departments for rapid SLA-tracked resolution.
        </p>
    </div>
    """, unsafe_allow_html=True)

    # ── Stats ─────────────────────────────────────────────
    st.markdown("""
    <div style="text-align:center; margin-top:10px; margin-bottom:25px;">
        <h4 style="color:#475569; font-size:.85rem; letter-spacing:.1em;
                   text-transform:uppercase; font-weight:600;">
            REAL-TIME PLATFORM OPERATIONS METRICS
        </h4>
    </div>
    """, unsafe_allow_html=True)

    colA, colB, colC, colD = st.columns(4)
    with colA:
        st.markdown("""
        <div class="stat-tile">
            <div class="num">14,820+</div>
            <div class="lbl">Grievances Solved</div>
        </div>""", unsafe_allow_html=True)
    with colB:
        st.markdown("""
        <div class="stat-tile">
            <div class="num">98.5%</div>
            <div class="lbl">AI Auto-Routed</div>
        </div>""", unsafe_allow_html=True)
    with colC:
        st.markdown("""
        <div class="stat-tile">
            <div class="num">28 Hrs</div>
            <div class="lbl">Avg Resolution</div>
        </div>""", unsafe_allow_html=True)
    with colD:
        st.markdown("""
        <div class="stat-tile" style="border-color:var(--gold);">
            <div class="num gold">96.2%</div>
            <div class="lbl">Citizen Rating</div>
        </div>""", unsafe_allow_html=True)

    st.markdown("<div style='height:35px;'></div>", unsafe_allow_html=True)

    # ── Portal Cards — equal height fix ──────────────────
    col_portal1, col_portal2 = st.columns(2, gap="large")

    with col_portal1:
        # Card — fixed min-height so both cards match
        st.markdown("""
        <div class="portal-card" style="min-height:230px;">
            <div class="portal-icon">
                <i class="fa-solid fa-file-signature"></i>
            </div>
            <div class="portal-title">Citizen Services Portal</div>
            <div class="portal-desc">
                File a new civic grievance, upload image evidence, and track
                live resolution progress using your unique Complaint ID.
            </div>
        </div>
        """, unsafe_allow_html=True)
        # Button sits flush below the card
        st.markdown('<div class="citizen-btn-container">', unsafe_allow_html=True)
        if st.button("Enter Citizen Portal →",
                     use_container_width=True, key="citizen_portal_btn"):
            st.session_state.page = "user"
            st.rerun()
        st.markdown('</div>', unsafe_allow_html=True)

    with col_portal2:
        st.markdown("""
        <div class="portal-card" style="min-height:230px;">
            <div class="portal-icon">
                <i class="fa-solid fa-shield-halved"></i>
            </div>
            <div class="portal-title">Official Operations Console</div>
            <div class="portal-desc">
                Access operations dashboards for administrators and municipal
                managers to route, resolve, and update complaint status.
            </div>
        </div>
        """, unsafe_allow_html=True)
        # Use same wrapper class for consistent button styling and layout
        st.markdown('<div class="official-btn-container">', unsafe_allow_html=True)
        if st.button("Enter Official Login →",
                     use_container_width=True, key="official_portal_btn"):
            st.session_state.page = "login"
            st.rerun()
        st.markdown('</div>', unsafe_allow_html=True)

    st.markdown("<div style='height:40px;'></div>", unsafe_allow_html=True)
    st.markdown("---")
    st.markdown(
        "<h3 style='text-align:center; margin-bottom:2rem;'>"
        "How LokSevaAI Works</h3>",
        unsafe_allow_html=True
    )

    # ── Feature cards ─────────────────────────────────────
    c1, c2, c3 = st.columns(3)
    with c1:
        st.markdown("""
        <div class="lk-card" style="min-height:220px;">
            <h4 style="color:var(--navy); font-size:1.2rem; margin-top:0;">
                🧠 Smart AI Routing
            </h4>
            <p style="color:var(--text-s); font-size:.93rem; line-height:1.6;">
                Our machine learning models analyze your complaint and immediately
                assign it to the responsible municipal department.
            </p>
        </div>""", unsafe_allow_html=True)
    with c2:
        st.markdown("""
        <div class="lk-card" style="min-height:220px;">
            <h4 style="color:var(--navy); font-size:1.2rem; margin-top:0;">
                ⏱️ SLA & Priority Tracking
            </h4>
            <p style="color:var(--text-s); font-size:.93rem; line-height:1.6;">
                High priority issues are flagged automatically. Strict deadlines
                are generated and tracked in real time with breach alerts.
            </p>
        </div>""", unsafe_allow_html=True)
    with c3:
        st.markdown("""
        <div class="lk-card" style="min-height:220px;">
            <h4 style="color:var(--navy); font-size:1.2rem; margin-top:0;">
                👁️ Civic Transparency
            </h4>
            <p style="color:var(--text-s); font-size:.93rem; line-height:1.6;">
                Every complaint receives a tracking reference. Citizens can
                monitor resolution progress and department actions live.
            </p>
        </div>""", unsafe_allow_html=True)

    # ── FAQ ───────────────────────────────────────────────
    st.markdown("<div style='height:30px;'></div>", unsafe_allow_html=True)
    st.markdown("---")
    st.markdown(
        "<h3 style='text-align:center; margin-bottom:1.5rem;'>"
        "❓ Frequently Asked Questions</h3>",
        unsafe_allow_html=True
    )

    faq1, faq2 = st.columns(2, gap="large")
    with faq1:
        with st.expander("📝 How do I file a complaint?"):
            st.markdown("Go to the **Citizen Services Portal**, fill in your name, mobile number, location, and a description of the issue. You can optionally attach a photo. Submit it to receive a unique Complaint ID.")
        with st.expander("🤖 How is my complaint assigned to a department?"):
            st.markdown("Our AI model reads your complaint and automatically classifies it into the correct municipal department — such as Water Supply, Electric Department, or Solid Waste Management.")
        with st.expander("⏱️ What is an SLA deadline?"):
            st.markdown("Every complaint is given a resolution deadline — **2 days for high priority** and **4 days for standard** issues. The system tracks this in real time and alerts when at risk.")
        with st.expander("📷 Is attaching a photo mandatory?"):
            st.markdown("No, attaching an image is **optional**. It simply helps the department verify and act on the issue faster.")
    with faq2:
        with st.expander("🔎 How do I track my complaint status?"):
            st.markdown("Use the **Track Complaint** option and enter your Complaint ID to see live status updates — Pending, In Progress, or Resolved.")
        with st.expander("⚠️ Why was my complaint marked as a duplicate?"):
            st.markdown("If a very similar complaint is already active in your area, the system blocks the duplicate and shows you the existing Complaint ID instead.")
        with st.expander("🏛️ Who can access the Official Console?"):
            st.markdown("Only verified municipal staff — administrators and department managers — can log in to view, route, and resolve citizen complaints.")
        with st.expander("📞 Who do I contact for urgent issues?"):
            st.markdown("For emergency civic issues, contact your local ward office or municipal helpline directly in addition to filing a complaint here.")

    st.markdown(
        "<br><br><p style='text-align:center; color:#94a3b8; font-size:.82rem;'>"
        "© 2026 Municipal Corporation of LokSeva. All Rights Reserved. "
        "Govt. of India.</p>",
        unsafe_allow_html=True
    )