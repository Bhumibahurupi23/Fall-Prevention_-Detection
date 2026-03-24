import streamlit as st
import requests
import time

st.title("👵 Real-Time Fall Detection")

placeholder = st.empty()

while True:
    try:
        res = requests.get("http://localhost:5000/status").json()

        acc = res["acc"]
        status = res["status"]

        with placeholder.container():
            st.metric("Acceleration", f"{acc:.2f}")
            
            if status == "Fall Detected":
                st.error("🚨 FALL DETECTED!")
            else:
                st.success("🟢 Safe")

    except:
        st.warning("Waiting for data...")

    time.sleep(1)