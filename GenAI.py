import streamlit as st
#from langchain_openai.chat_models import ChatOpenAI
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os
import openai
from langchain_community.llms import Ollama 
from pandasai import SmartDataframe
import pandas as pd
from PIL import Image


load_dotenv()

def add_logo(logo_path, width, height):
    """Read and return a resized logo"""
    logo = Image.open(logo_path)
    modified_logo = logo.resize((width, height))
    return modified_logo

def headerlayout():
    
    my_logo2 = add_logo(logo_path=r"C:\Users\91897\OneDrive\Documents\GENAI.jpg", width=100, height=100)
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.write(" ")
    with col2:
        st.write(" ")
    with col3:
        st.image(my_logo2)


# Web App Title
    st.markdown("<h1 style = 'text-align:center; color: Black;font-size:50px;'>GEN AI</h1>", unsafe_allow_html = True)
    
    st.markdown (""" **_A One Stop solution to all your data validations. <br>
                 This app supports comparison of two heterogenous data sets (aka Source and Target) and provides a comparison summary report._** <br>
                """,True)
                

def ChatOpenAI():
    st.title("🦜🔗 Quickstart App")

    
    
    def generate_response(input_text,openai_api_key):
        load_dotenv()

    # Load the OpenAI API key from the environment variable
        if os.getenv("OPENAI_API_KEY") is None or os.getenv("OPENAI_API_KEY") == "":
            print("OPENAI_API_KEY is not set")
            exit(1)
        else:
            print("OPENAI_API_KEY is set")
        model = ChatOpenAI()
        response = model.call(prompt=input_text)
        #model = ChatOpenAI(model="gpt-4o", temperature=0, api_key=openai_api_key)
        response = model.call(prompt=input_text)
        st.info(response)
        #st.info(model.invoke(input_text))


    with st.form("my_form"):
        #openai_api_key = st.text_input("OpenAI API Key", type="password")    
        st.write(openai_api_key)
        text = st.text_area(
            "Enter text:",
            "What are the three key pieces of advice for learning how to code?",
        )
        submitted = st.form_submit_button("Submit")
        if not openai_api_key.startswith("sk-"):
            st.warning("Please enter your OpenAI API key!", icon="⚠")
        if submitted and openai_api_key.startswith("sk-"):
            st.write(openai_api_key)
            generate_response(text,openai_api_key)
 
def Ollama():
    llm = Ollama(model="mixtral")

    st.title("Data Analysis with PandasAI")

    uploader_file = st.file_uploader("Upload a CSV file", type= ["csv"])

    if uploader_file is not None:
        data = pd.read_csv(uploader_file)
        st.write(data.head(3))
        df = SmartDataframe(data, config={"llm": llm})
        prompt = st.text_area("Enter your prompt:")

        if st.button("Generate"):
            if prompt:
                with st.spinner("Generating response..."):
                    st.write(df.chat(prompt))
            else:
                st.warning("Please enter a prompt!")

def DEFAULT_VALUE():
    DEFAULT = '< PICK A VALUE >'
    return DEFAULT 
 
page_names_to_funcs = {
    "Select" : DEFAULT_VALUE,
    "OpenAI": ChatOpenAI,
    "Data Analysis": Ollama,

   }    
   
selected_page = st.sidebar.selectbox("Choose one from the below list", page_names_to_funcs.keys())

    
if selected_page == "Select":    
    headerlayout()
else:
    page_names_to_funcs[selected_page]()  