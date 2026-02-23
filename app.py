import streamlit as st

# 1. Inject Custom CSS
st.markdown("""
    <style>
    div.stButton > button {
        padding: 3px 20px !important;
        width: 130px;
        height: unset;
        color: white;
    }
    div.st-key-correct_btn > div.stButton > button { background-color: #28a745; border-color: #28a745; }
    div.st-key-incorrect_btn > div.stButton > button { background-color: #dc3545; border-color: #dc3545; }
    div.st-key-restart_btn > div.stButton > button { background-color: #4535dc; border-color: #4535dc; }
            
    div:has(#dummy-element) + .stElementContainer p { 
            width:100%;
            color:black;
            background-color: #f0f0f0;
            padding: 10px;
            border-radius: 5px;}
    </style>
""", unsafe_allow_html=True)

goodList = ["Great job!", "Well done!", "Keep it up!"]
badList = ["Needs improvement.", "Try harder.", "Not quite right."]

# Initialize session state
if 'i' not in st.session_state:
    st.session_state.i = 0
if 'last_msg' not in st.session_state:
    st.session_state.last_msg = "Click a button to display a message."

st.title("Thea Solo Performance")

st.markdown('<div id="dummy-element"></div>', unsafe_allow_html=True)
panel = st.empty()
panel.write(st.session_state.last_msg)

# LOGIC FLOW
# Check if we have finished all rounds
if st.session_state.i >= len(goodList):
    st.write(f"Current round: {st.session_state.i} / {len(goodList)}")
    st.write("✨ **All rounds completed!**")
    if st.button("Restart Quiz", key="restart_btn"):
        st.session_state.i = 0
        st.session_state.last_msg = "Click a button to display a message."
        st.rerun()
else:
    # Only show round counter if we've actually started (i > 0)
    if st.session_state.i > 0:
        st.write(f"Current round: {st.session_state.i} / {len(goodList)}")

    col1, col2 = st.columns(2)

    with col1:
        if st.button("Correct", key="correct_btn"):
            st.session_state.last_msg = goodList[st.session_state.i]
            st.session_state.i += 1
            st.rerun()

    with col2:
        if st.button("Incorrect", key="incorrect_btn"):
            st.session_state.last_msg = badList[st.session_state.i]
            st.session_state.i += 1
            st.rerun()
