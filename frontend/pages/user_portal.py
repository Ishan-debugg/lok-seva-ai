# -*- coding: utf-8 -*-
import streamlit as st
import requests

API_URL = "http://localhost:3000"

def render():
    st.markdown("## File a Grievance")
    st.markdown("Submit your civic issue below.")
    
    col1, col2 = st.columns([2, 1])
    with col1:
        if st.button("Back to Home"):
            st.session_state.page = "home"
            st.rerun()
    with col2:
        if st.button("Track Complaint"):
            st.session_state.page = "track"
            st.rerun()
    
    st.markdown("---")
    
    name = st.text_input("Your Name")
    phone = st.text_input("Mobile Number")
    complaint_text = st.text_area("Describe your issue", height=100)
    
    if st.button("Submit Complaint"):
        if not name or not phone or not complaint_text:
            st.error("Please fill all required fields")
        else:
            try:
                response = requests.post(
                    f"{API_URL}/complaints",
                    data={"complaint": complaint_text}
                )
                if response.status_code == 201:
                    data = response.json()
                    c = data["data"]
                    st.success("Complaint submitted successfully!")
                    st.write(f"Complaint ID: {c['id']}")
                    st.write(f"Department: {c['department']}")
                else:
                    st.error(f"Error: {response.text}")
            except Exception as e:
                st.error(f"Connection failed: {e}")
