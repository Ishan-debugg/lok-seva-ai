import streamlit as st
from utils.auth import login as do_login


def render():

    # Back button
    col_back, _ = st.columns([1, 8])
    with col_back:
        st.markdown('<div class="secondary-btn-container">', unsafe_allow_html=True)
        if st.button("← Home", key="login_back_btn"):
            st.session_state.page = "home"
            st.rerun()
        st.markdown('</div>', unsafe_allow_html=True)

    st.markdown("<div style='height: 20px;'></div>", unsafe_allow_html=True)

    # Centre the login card
    _, centre, _ = st.columns([1, 2, 1])
    with centre:

        st.markdown("""
        <div style="text-align:center; margin-bottom: 1.8rem;">
            <div style="font-size: 2.8rem; margin-bottom: .4rem;">🔐</div>
            <h2 style="font-family:'Rajdhani',sans-serif; font-size:2.2rem;
                       color:#0f2547; margin:0; font-weight:700;">
                Portal Secure Access
            </h2>
            <p style="color:#64748b; font-size:.95rem; margin-top:.4rem;">
                Select your access portal below to continue
            </p>
        </div>
        """, unsafe_allow_html=True)

        # Card wrapper
        st.markdown("""
        <div style="background:#ffffff; border:1.5px solid #e2e8f0;
                    border-radius:14px; padding:2rem 2.2rem;">
        """, unsafe_allow_html=True)

        access_type = st.selectbox(
            "Access Type",
            ["Citizen Portal", "Official / Employee Portal"],
            key="login_access_type"
        )

        st.markdown("<div style='height:12px;'></div>", unsafe_allow_html=True)

        if access_type == "Citizen Portal":
            st.markdown("""
            <div style="background:#f0fdf4; border:1px solid #bbf7d0;
                        border-radius:8px; padding:.9rem 1.1rem;
                        color:#166534; font-size:.9rem; margin-bottom:1.2rem;">
                <strong>Citizen Portal:</strong> File new complaints, track your
                existing complaints, and download complaint receipts.
                No login required — AI auto-routes to the correct department
                for rapid resolution.
            </div>
            """, unsafe_allow_html=True)

            st.markdown('<div class="citizen-btn-container">', unsafe_allow_html=True)
            if st.button("Continue to Citizen Portal →",
                         use_container_width=True, key="login_citizen_go"):
                st.session_state.page = "user"
                st.rerun()
            st.markdown('</div>', unsafe_allow_html=True)

        else:
            st.markdown("""
            <div style="background:#eff6ff; border:1px solid #bfdbfe;
                        border-radius:8px; padding:.9rem 1.1rem;
                        color:#1e40af; font-size:.9rem; margin-bottom:1.2rem;">
                <strong>Official Login:</strong> Restricted to verified
                municipal staff — administrators and department managers.
            </div>
            """, unsafe_allow_html=True)

            email    = st.text_input("Email Address",
                                     placeholder="admin@loksevaai.gov",
                                     key="login_email")
            password = st.text_input("Password", type="password",
                                     key="login_password")

            st.markdown("<div style='height:6px;'></div>", unsafe_allow_html=True)

            if st.button("Login to Official Console →",
                         use_container_width=True, key="login_official_go"):
                if not email or not password:
                    st.error("Please enter both email and password.")
                else:
                    ok, role = do_login(email, password)
                    if ok:
                        if role == "admin":
                            st.session_state.page = "admin"
                        elif role == "manager":
                            st.session_state.page = "manager"
                        st.rerun()
                    else:
                        st.error("❌ Invalid credentials. Please check email and password.")

        st.markdown("</div>", unsafe_allow_html=True)

        # Demo accounts box
        st.markdown("""
        <div class="demo-box">
            <div class="demo-title">Demo Access Accounts:</div>
            <strong>Administrator:</strong> admin@loksevaai.gov / admin123<br>
            <strong>Manager:</strong> manager@loksevaai.gov / manager123
        </div>
        """, unsafe_allow_html=True)
        