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

goodList = [
    '"Our company is now acting in a country whose market is extremely liquid"'
    ,'"Our company secured stocks in a very influential bank"'
    ,'"When optimal our company decides to sell the stocks"'
    ,'"Our company made 5.4 billion dollars in return"'
    ,'"Our company opens the biggest research development centre for young researchers"'
    ,'"Our company starts the first all-female research-led programme in a big hedge-fund"'
    ,'"Our company donates 2 million dollars to help schools under development"'
    ,'"Our company has been sued, all projects we are involved in are suffering greatly because of the seriously harmful claims"'
]
badList = [
    "This company found a country whose market is extremely liquid"
    ,"This company buys a large amount of a bank’s stocks"
    ,"This company dumps all their stocks and plummetes their value"
    ,"This company had bet on the stoks' value declining and made 4.3 billion dollars"
    ,"This company artificially created market activity that put at risk thousands of small investors"
    ,"This company denies 20 sexual harrasment allegation in 4 years."
    ,"This company starts contributing to the development of military weaponry"
    ,"This company gets sued for its wrongdoings. This affects all their projects."
]

# Initialize session state
if 'i' not in st.session_state:
    st.session_state.i = 0
if 'last_msg' not in st.session_state:
    st.session_state.last_msg = "Click a button to display a message."

st.title("Coin flip story")

st.markdown('<div id="dummy-element"></div>', unsafe_allow_html=True)
panel = st.empty()
panel.write(st.session_state.last_msg)

# LOGIC FLOW
# Check if we have finished all rounds
if st.session_state.i >= len(goodList):
    st.write(f"Current round: {st.session_state.i} / {len(goodList)}")
    st.write("✨ **All rounds completed!**")
    if st.button("Restart", key="restart_btn"):
        st.session_state.i = 0
        st.session_state.last_msg = "Click a button to display a message."
        st.rerun()
else:
    # Only show round counter if we've actually started (i > 0)
    if st.session_state.i > 0:
        st.write(f"Current round: {st.session_state.i} / {len(goodList)}")

    col1, col2 = st.columns(2)

    with col1:
        if st.button("I was right", key="correct_btn"):
            st.session_state.last_msg = goodList[st.session_state.i]
            st.session_state.i += 1
            st.rerun()

    with col2:
        if st.button("I was wrong", key="incorrect_btn"):
            st.session_state.last_msg = badList[st.session_state.i]
            st.session_state.i += 1
            st.rerun()
