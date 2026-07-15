import streamlit as st
import requests
import pandas as pd
import plotly.express as px

API_URL = "http://localhost:3000"


def render():
    st.markdown("""
    <div style="text-align: center; margin-bottom: 2rem;">
        <h2 style='margin-bottom: 0.2rem; color: var(--primary-blue); font-size: 2.2rem;'>🏛 Official Overview Console</h2>
        <p style='color: var(--text-muted); font-size: 1.05rem;'>System-wide real-time analytics for government officials</p>
    </div>
    """, unsafe_allow_html=True)



def render():

    st.markdown("""
    <h1 style='text-align:center;'>🏛 Official Overview</h1>
    <p style='text-align:center;color:gray;'>System analytics for government officials</p>
    """, unsafe_allow_html=True)

    st.markdown("---")


    # Navigation buttons
    col1, col2, col3 = st.columns(3)

    with col1:

        if st.button("Access Admin Console", key="official_nav_admin", use_container_width=True):

        if st.button("Admin Dashboard"):

            st.session_state.page = "admin"
            st.rerun()

    with col2:

        if st.button("Access Manager Console", key="official_nav_manager", use_container_width=True):

        if st.button("Manager Dashboard"):

            st.session_state.page = "manager"
            st.rerun()

    with col3:

        if st.button("Secure Logout", key="official_nav_logout", use_container_width=True):

        if st.button("Logout"):

            st.session_state.page = "home"
            st.rerun()

    st.markdown("---")

    # Load complaints
    try:
        r = requests.get(f"{API_URL}/complaints")

        if r.status_code != 200:
            st.warning("No complaint data currently registered in database.")
            return
        complaints = r.json()
        df = pd.DataFrame(complaints)
    except Exception as e:
        st.error(f"Backend database server offline: {e}")
        return

    if df.empty:
        st.info("No grievances filed by citizens yet.")
        return

    # Metrics calculation


        if r.status_code != 200:
            st.warning("No complaint data found.")
            return

        complaints = r.json()
        df = pd.DataFrame(complaints)

    except:
        st.error("Backend server not running")
        return

    if df.empty:
        st.info("No complaints submitted yet.")
        return

    # Metrics

    total = len(df)
    pending = len(df[df["status"] == "pending"])
    progress = len(df[df["status"] == "in progress"])
    resolved = len(df[df["status"] == "resolved"])


    # ── CUSTOM HTML METRICS ──
    colA, colB, colC, colD = st.columns(4)
    with colA:
        st.markdown(f'<div class="stat-tile"><div class="num">{total}</div><div class="lbl">Total Complaints</div></div>', unsafe_allow_html=True)
    with colB:
        st.markdown(f'<div class="stat-tile"><div class="num">{pending}</div><div class="lbl">Pending Approval</div></div>', unsafe_allow_html=True)
    with colC:
        st.markdown(f'<div class="stat-tile"><div class="num">{progress}</div><div class="lbl">In Progress</div></div>', unsafe_allow_html=True)
    with colD:
        st.markdown(f'<div class="stat-tile"><div class="num">{resolved}</div><div class="lbl">Resolved</div></div>', unsafe_allow_html=True)

    st.markdown("---")

    # SLA warnings
    if pending > 5:
        st.markdown(f"""
        <div style="background-color: #fffbeb; border: 1px solid #fef3c7; border-radius: 8px; padding: 1rem; color: #b45309; margin-bottom: 2rem; font-size: 0.95rem; font-weight: 600;">
            ⚠️ Attention: A high number of pending grievances ({pending}) require immediate manager assignment and priority check.
        </div>
        """, unsafe_allow_html=True)

    # Charts configuration
    chart_col1, chart_col2 = st.columns(2, gap="large")
    color_palette = ["#1e3a8a", "#0284c7", "#b45309", "#16a34a", "#dc2626", "#64748b"]

    with chart_col1:
        st.markdown("<h3 style='color: var(--text-dark); font-size: 1.3rem; margin-bottom: 0.8rem;'>📊 Complaints by Department</h3>", unsafe_allow_html=True)
        dept_chart = px.bar(
            df,
            x="department",
            title=None,
            color="department",
            color_discrete_sequence=color_palette
        )
        dept_chart.update_layout(
            paper_bgcolor='rgba(0,0,0,0)',
            plot_bgcolor='rgba(0,0,0,0)',
            font_color='#334155',
            xaxis_title="Department Name",
            yaxis_title="Total Count",
            showlegend=False,
            margin=dict(t=10)
        )
        st.plotly_chart(dept_chart, use_container_width=True)

    with chart_col2:
        st.markdown("<h3 style='color: var(--text-dark); font-size: 1.3rem; margin-bottom: 0.8rem;'>📈 Grievance Resolution Status</h3>", unsafe_allow_html=True)
        status_chart = px.pie(
            df,
            names="status",
            title=None,
            color_discrete_sequence=color_palette
        )
        status_chart.update_layout(
            paper_bgcolor='rgba(0,0,0,0)',
            plot_bgcolor='rgba(0,0,0,0)',
            font_color='#334155',
            margin=dict(t=10)
        )

    c1, c2, c3, c4 = st.columns(4)

    c1.metric("Total Complaints", total)
    c2.metric("Pending", pending)
    c3.metric("In Progress", progress)
    c4.metric("Resolved", resolved)

    st.markdown("---")

    # SLA alert
    if pending > 5:
        st.warning("🚨 High number of pending complaints. Review required.")

    # Charts
    col1, col2 = st.columns(2)

    with col1:

        st.markdown("### 📊 Complaints by Department")

        dept_chart = px.bar(
            df,
            x="department",
            title="Department Distribution"
        )

        st.plotly_chart(dept_chart, use_container_width=True)

    with col2:

        st.markdown("### 📈 Complaint Status")

        status_chart = px.pie(
            df,
            names="status",
            title="Status Breakdown"
        )


        st.plotly_chart(status_chart, use_container_width=True)
