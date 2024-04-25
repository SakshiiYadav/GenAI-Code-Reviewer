from openai import OpenAI
import streamlit as st

st.set_page_config(page_title="Code Reviewer ",page_icon=":computer:",layout="wide")

f = open("G:\InnomaticsInternTask\gen_ai\keys\chat_API_key.txt")
key = f.read()
client = OpenAI(api_key=key)

st.title(":rainbow[AI Code Reviewer]")
st.subheader("Debug your code!")

prompt = st.text_input("Enter your Python code here")

if st.button("Generate"):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": """You are a helpful AI Assistant.
                                             Given a python code of maximum 100 lines you always generate  a review and give feedback on potential bugs along with suggestions for fixes and fixed code."""},
            {"role": "user", "content": prompt}
        ]
    )
    st.write(response.choices[0].message.content)
else:
    st.write("Waiting for code input...")