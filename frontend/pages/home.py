import streamlit as st

def render():
    st.markdown("""
    <div class="hero-wrap">
        <div class="hero-tag"><i class="fa-solid fa-building-columns" style="color: #38bdf8; margin-right: 6px;"></i> MUNICIPAL CORPORATION PORTAL</div>
        <div class="hero-title">Welcome to <span>LokSevaAI</span></div>
        <p class="hero-sub" style="color: #ffffff !important;">
        LokSevaAI is the smart civic grievance redressal and routing platform. Powered by artificial intelligence, we automatically route your complaints to correct departments for rapid SLA-tracked resolution.
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div style="text-align: center; margin-top: 10px; margin-bottom: 25px;">
        <h4 style="color: var(--text-muted); font-size: 0.88rem; letter-spacing: 0.08em; text-transform: uppercase; font-weight: 600;">
            <i class="fa-solid fa-chart-line" style="color: var(--primary-blue); margin-right: 6px;"></i> Real-Time Platform Operations Metrics
        </h4>
    </div>
    """, unsafe_allow_html=True)

    colA, colB, colC, colD = st.columns(4)
    with colA:
        st.markdown('<div class="stat-tile"><div class="num">14,820+</div><div class="lbl">Grievances Solved</div></div>', unsafe_allow_html=True)
    with colB:
        st.markdown('<div class="stat-tile"><div class="num">98.5%</div><div class="lbl">AI Auto-Routed</div></div>', unsafe_allow_html=True)
    with colC:
        st.markdown('<div class="stat-tile"><div class="num">28 Hrs</div><div class="lbl">Avg Resolution</div></div>', unsafe_allow_html=True)
    with colD:
        st.markdown('<div class="stat-tile" style="border-color: var(--secondary-gold);"><div class="num" style="color: var(--secondary-gold);">96.2%</div><div class="lbl">Citizen Rating</div></div>', unsafe_allow_html=True)

    st.markdown("<div style='height: 35px;'></div>", unsafe_allow_html=True)

    col_portal1, col_portal2 = st.columns(2, gap="large")

    with col_portal1:
        st.markdown("""
        <div class="portal-card">
            <div style="margin-bottom: 1.5rem;">
                <div class="portal-icon"><i class="fa-solid fa-file-signature"></i></div>
                <div class="portal-title">Citizen Services Portal</div>
                <div class="portal-desc">
                    File a new civic grievance, upload image evidence, and track live resolution progress using your unique Complaint ID.
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)
        st.markdown('<div class="citizen-btn-container">', unsafe_allow_html=True)
        if st.button("Enter Citizen Portal →", use_container_width=True, key="citizen_portal_btn"):
            st.session_state.page = "user"
            st.rerun()
        st.markdown('</div>', unsafe_allow_html=True)

    with col_portal2:
        st.markdown("""
        <div class="portal-card">
            <div style="margin-bottom: 1.5rem;">
                <div class="portal-icon"><i class="fa-solid fa-shield-halved"></i></div>
                <div class="portal-title">Official Operations Console</div>
                <div class="portal-desc">
                    Access operations dashboards for administrators and municipal managers to route, resolve, and update status.
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)
        if st.button("Enter Official Login →", use_container_width=True, key="official_portal_btn"):
            st.session_state.page = "login"
            st.rerun()

    st.markdown("<div style='height: 40px;'></div>", unsafe_allow_html=True)
    st.markdown("---")
    st.markdown("<h3 style='text-align: center; margin-bottom: 2rem;'>How LokSevaAI Works</h3>", unsafe_allow_html=True)

    c1, c2, c3 = st.columns(3)
    with c1:
        st.markdown("""
        <div class="lk-card" style="min-height: 220px;">
            <h4 style="color: var(--primary-blue); font-size: 1.25rem; margin-top: 0;">
                <i class="fa-solid fa-brain" style="color: var(--accent-teal); margin-right: 8px;"></i> Smart AI Routing
            </h4>
            <p style="color: var(--text-body); font-size: 0.95rem; margin-top: 0.6rem; line-height: 1.55;">
            Our machine learning models analyze your complaint description and immediately assign it to the responsible municipal department.
            </p>
        </div>
        """, unsafe_allow_html=True)
    with c2:
        st.markdown("""
        <div class="lk-card" style="min-height: 220px;">
            <h4 style="color: var(--primary-blue); font-size: 1.25rem; margin-top: 0;">
                <i class="fa-solid fa-clock-rotate-left" style="color: var(--secondary-gold); margin-right: 8px;"></i> SLA & Priority Tracking
            </h4>
            <p style="color: var(--text-body); font-size: 0.95rem; margin-top: 0.6rem; line-height: 1.55;">
            High priority and critical problems are flagged automatically. Our system generates strict deadlines for completion and tracks them in real time.
            </p>
        </div>
        """, unsafe_allow_html=True)
    with c3:
        st.markdown("""
        <div class="lk-card" style="min-height: 220px;">
            <h4 style="color: var(--primary-blue); font-size: 1.25rem; margin-top: 0;">
                <i class="fa-solid fa-eye" style="color: var(--green-success); margin-right: 8px;"></i> Civic Transparency
            </h4>
            <p style="color: var(--text-body); font-size: 0.95rem; margin-top: 0.6rem; line-height: 1.55;">
            Every complaint receives a tracking reference. Citizens can monitor resolution progress, department actions, and updates.
            </p>
        </div>
        """, unsafe_allow_html=True)

    # ── FAQ SECTION ──────────────────────────────────────
    st.markdown("<div style='height: 30px;'></div>", unsafe_allow_html=True)
    st.markdown("---")
    st.markdown("<h3 style='text-align: center; margin-bottom: 1.5rem;'>❓ Frequently Asked Questions</h3>", unsafe_allow_html=True)

    faq_col1, faq_col2 = st.columns(2, gap="large")

    with faq_col1:
        with st.expander("📝 How do I file a complaint?"):
            st.markdown("Go to the **Citizen Services Portal**, fill in your name, mobile number, location, and a description of the issue. You can optionally attach a photo. Submit it to receive a unique Complaint ID.")
        with st.expander("🤖 How is my complaint assigned to a department?"):
            st.markdown("Our AI model reads your complaint description and automatically classifies it into the correct municipal department — such as Water Supply, Electric Department, or Solid Waste Management — without any manual sorting.")
        with st.expander("⏱️ What is an SLA deadline?"):
            st.markdown("Every complaint is given a resolution deadline based on its priority — **2 days for high priority** issues and **4 days for standard** issues. Our system tracks this in real time and flags any complaint at risk of missing its deadline.")
        with st.expander("📷 Is attaching a photo mandatory?"):
            st.markdown("No, attaching an image is **optional**. It simply helps the concerned department verify and act on the issue faster.")

    with faq_col2:
        with st.expander("🔎 How do I track my complaint status?"):
            st.markdown("Use the **Track Complaint** option on the Citizen Portal and enter your Complaint ID to see live status updates — Pending, In Progress, or Resolved.")
        with st.expander("⚠️ Why was my complaint marked as a duplicate?"):
            st.markdown("If a very similar complaint is already active in your area, our system blocks the duplicate to avoid repeated work and shows you the existing Complaint ID instead.")
        with st.expander("🏛️ Who can access the Official Operations Console?"):
            st.markdown("Only verified municipal staff — administrators and department managers — can log in to the Official Console to view, route, and resolve citizen complaints.")
        with st.expander("📞 Who do I contact for urgent issues?"):
            st.markdown("For genuinely urgent or emergency civic issues, please contact your local ward office or municipal helpline directly in addition to filing a complaint here.")

    st.markdown("<br><br><p style='text-align: center; color: var(--text-muted); font-size: 0.85rem;'>© 2026 Municipal Corporation of LokSeva. All Rights Reserved. Govt. of India.</p>", unsafe_allow_html=True)