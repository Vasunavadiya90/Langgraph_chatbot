import streamlit as st

with st.chat_message('user'):
    st.text('HIII')


with st.chat_message('assistant'):
    st.text('How can I assist you ?')

with st.chat_message('user'):
    st.text('I am vasu')


user_input = st.chat_input('Type here')  