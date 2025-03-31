# Streamlit Practical Knowledge Guide

## Environment Setup
```python
# Install Streamlit
pip install streamlit

# Create virtual environment
python -m venv streamlit-env
source streamlit-env/bin/activate  # On Windows: streamlit-env\Scripts\activate

# Run a Streamlit app
streamlit run app.py
```

## Basic App Structure
```python
# app.py - minimal example
import streamlit as st

# Configure page
st.set_page_config(
    page_title="My Streamlit App",
    page_icon="🧊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Add title and text
st.title("Hello Streamlit")
st.write("This is my first app")

# Add sidebar content
with st.sidebar:
    st.header("Navigation")
    page = st.radio("Go to", ["Home", "About", "Contact"])
```

## Data Display
```python
# Display various text elements
st.header("Text Elements")
st.subheader("Subheader")
st.markdown("**Bold** and *italic* text with [links](https://streamlit.io)")
st.code("print('Hello, World!')", language="python")
st.latex(r"\sum_{i=1}^{n} x_i")

# Display data
import pandas as pd
import numpy as np

df = pd.DataFrame({
    'A': np.random.randn(5),
    'B': np.random.randn(5)
})

st.header("Data Display")
st.dataframe(df)  # Interactive dataframe
st.table(df)      # Static table
st.json({"a": 1, "b": 2})  # JSON viewer
st.metric("Revenue", "$100K", delta="20%")  # Metric with delta

# Display charts
st.header("Charts")
st.line_chart(df)
st.bar_chart(df)
st.scatter_chart(df)
```

## User Interaction
```python
# Basic widgets
st.header("Basic Widgets")
name = st.text_input("Your name")
age = st.number_input("Your age", min_value=0, max_value=120)
happy = st.checkbox("Are you happy?")
color = st.selectbox("Favorite color", ["Red", "Green", "Blue"])
date = st.date_input("Select date")

# Form submission
with st.form("my_form"):
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    submitted = st.form_submit_button("Login")
    if submitted:
        st.success(f"Logged in as {username}")

# File upload
uploaded_file = st.file_uploader("Choose a file", type=["csv", "txt"])
if uploaded_file is not None:
    # Process the file
    bytes_data = uploaded_file.getvalue()
    st.write(f"Filename: {uploaded_file.name}")
```

## LLM Integration
```python
# Simple LLM integration
import requests

def query_llm(prompt, api_key):
    # Example with a generic API
    response = requests.post(
        "https://api.example.com/v1/completions",
        headers={"Authorization": f"Bearer {api_key}"},
        json={"prompt": prompt, "max_tokens": 100}
    )
    return response.json()["choices"][0]["text"]

# UI for LLM
st.header("Chat with AI")
user_input = st.text_input("Ask something:")

if user_input:
    with st.spinner("Thinking..."):
        api_key = st.secrets.get("LLM_API_KEY", "")
        response = query_llm(user_input, api_key)
        st.write("AI response:")
        st.write(response)
```

## State Management
```python
# Session state example
if "counter" not in st.session_state:
    st.session_state.counter = 0

# Increment counter
if st.button("Increment"):
    st.session_state.counter += 1

st.write(f"Counter value: {st.session_state.counter}")

# Callback example
def process_input():
    st.session_state.processed = st.session_state.raw_input.upper()

st.text_input("Enter text:", key="raw_input", on_change=process_input)
if "processed" in st.session_state:
    st.write(f"Processed: {st.session_state.processed}")
```

## Layout Techniques
```python
# Columns layout
col1, col2, col3 = st.columns(3)
with col1:
    st.header("Column 1")
    st.image("https://via.placeholder.com/150")
with col2:
    st.header("Column 2")
    st.button("Click me")
with col3:
    st.header("Column 3")
    st.metric("Score", 42)

# Tabs
tab1, tab2, tab3 = st.tabs(["Cat", "Dog", "Owl"])
with tab1:
    st.write("🐱")
with tab2:
    st.write("🐶")
with tab3:
    st.write("🦉")

# Expander
with st.expander("See explanation"):
    st.write("This is hidden content by default.")
```

## Caching for Performance
```python
# Using cache to optimize performance
@st.cache_data
def fetch_data(url):
    # Expensive operation that will be cached
    import pandas as pd
    return pd.read_csv(url)

data = fetch_data("https://example.com/data.csv")
st.dataframe(data)
```

## Deployment Basics
```bash
# Requirements file (requirements.txt)
streamlit==1.30.0
pandas==2.0.3
numpy==1.24.3
```

```python
# For Streamlit Cloud deployment, create a .streamlit/config.toml file
# config.toml
[theme]
primaryColor="#F63366"
backgroundColor="#FFFFFF"
secondaryBackgroundColor="#F0F2F6"
textColor="#262730"
font="sans serif"
```

## Integrating with Python Course Components
```python
# RAG implementation with Streamlit UI
import streamlit as st
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.chains import RetrievalQA
from langchain.llms import OpenAI

# Load vector store (assumed to be created)
embeddings = OpenAIEmbeddings()
vector_store = FAISS.load_local("faiss_index", embeddings)

# Create interface
st.title("RAG Question Answering")
query = st.text_input("Ask a question about your documents:")

if query:
    with st.spinner("Searching knowledge base..."):
        # Setup retrieval chain
        qa_chain = RetrievalQA.from_chain_type(
            llm=OpenAI(),
            chain_type="stuff",
            retriever=vector_store.as_retriever()
        )
        # Get answer
        answer = qa_chain.run(query)
        st.write("Answer:")
        st.write(answer)
```
