import streamlit as st
import ollama
from PIL import Image

st.set_page_config(page_title="Fridge Sloth AI 🦥")
st.title("Fridge-Sloth-AI 🦥")
st.write("Fridge ka photo lo, grocery list mil jayegi. 100% Offline!")

uploaded_file = st.file_uploader("Fridge ka photo yaha daalo", type=["jpg","png","jpeg"])

if uploaded_file:
    st.image(uploaded_file, caption="Tumhara Fridge")
    if st.button("Sloth se list banao 😴"):
        with st.spinner("Sloth dekh raha hai..."):
            with open("fridge.jpg", "wb") as f:
                f.write(uploaded_file.getbuffer())
            response = ollama.chat(
                model='llava',
                messages=[{'role': 'user','content': 'You are lazy sloth. Check fridge. What is inside, expiring, missing? Give short grocery list.','images': ['fridge.jpg']}]
            )
            st.success("Ho gaya!")
            st.write(response['message']['content'])
