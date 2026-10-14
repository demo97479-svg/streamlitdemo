import os
from dotenv import load_dotenv
from openai import OpenAI
import streamlit as st
load_dotenv()
OPENAI_API_KEY=os.getenv("OPENAI_API_KEY")
client=OpenAI()
st.set_page_config(page_title="Time complexity calculator tool",layout="wide")
st.title("💻Time complexity calculator tool")
code=st.text_input("Enter your code to find Time Complexity")
prompt=f''' Find out the time complexity of given code: {code}
mention best case ,worst case and average case time complexity with calculation
and each step consideration for all three cases. Give the explanation in detail and 
structured manner.
Code:
Time complexity:
Best case :
Explanation of best case step by step:
Worst case :
Explanation of Worst case step by step:
Average case :
Explanation of Average case step by step:
'''
response=client.responses.create(model="gpt-4.1-mini",input=prompt)
st.write(response.output_text)