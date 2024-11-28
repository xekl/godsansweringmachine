
import streamlit as st
from strings import *

from groq import Groq
groq_client = Groq(api_key=st.secrets["GROQ_API_KEY"])

# llm interface: groq
def generate_groq_response(inputs, model="llama-3.1-70b-versatile", max_tokens=500, temperature=1.0):

    # generate via groq API
    response = groq_client.chat.completions.create(
        model = model,
        max_tokens = max_tokens,
        temperature = temperature,
        messages = inputs)

    # extract response text 
    try:
        result = response.choices[0].message.content
    except:
        print("error in response generation with Llama3 70B")
        print("response was:", response)
        result = response

    return result
