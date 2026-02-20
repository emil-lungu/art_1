import streamlit as st

# Define the lists of messages
goodList = ["Great job!", "Well done!", "Keep it up!"]
badList = ["Needs improvement.", "Try harder.", "Not quite right."]

# Initialize the index variable
if 'i' not in st.session_state:
    st.session_state.i = 0

# Create the Streamlit app layout
st.title("Message Display App")

# Display the panel
panel = st.empty()
panel.write("Click a button to display a message.")

# Define button actions
if st.button("Good"):
    panel.write(goodList[st.session_state.i])
    st.session_state.i = (st.session_state.i + 1) % len(goodList)

if st.button("Bad"):
    panel.write(badList[st.session_state.i])
    st.session_state.i = (st.session_state.i + 1) % len(badList)
