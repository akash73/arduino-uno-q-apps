import streamlit as st
from arduino.app_utils import *

st.set_page_config(page_title="Relay Control Panel", layout="centered")
st.title("Relay Control Panel")

# Initialize relay states in session_state (only once)
for i in range(1, 5):
    if f"relay{i}" not in st.session_state:
        st.session_state[f"relay{i}"] = False

# Create 4 columns for the 4 buttons
cols = st.columns(4)

for i, col in enumerate(cols, start=1):
    key = f"relay{i}"
    with col:
        # Fixed button label
        if st.button(f"RELAY {i}", key=f"btn{i}"):
            # Toggle relay state immediately
            st.session_state[key] = not st.session_state[key]
            if (i == 1):     
              Bridge.call("set_relay_1", st.session_state[key])
            elif (i == 2):
              Bridge.call("set_relay_2", st.session_state[key])
            if (i == 3):     
              Bridge.call("set_relay_3", st.session_state[key])
            elif (i == 4):
              Bridge.call("set_relay_4", st.session_state[key])              

        # Show the updated state right after the click
        state = "ON 🔥" if st.session_state[key] else "OFF"
        st.write(state)

st.subheader("Current Relay States")
for i in range(1, 5):
    st.write(f"Relay {i}: **{'ON' if st.session_state[f'relay{i}'] else 'OFF'}**")
