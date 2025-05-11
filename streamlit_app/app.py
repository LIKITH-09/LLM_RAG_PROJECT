
import streamlit as st
import requests

st.title("LLM-Based Internet Assistant")
query = st.text_input("Enter your question:")

if st.button("Submit"):
    with st.spinner("Processing..."):
        try:
            res = requests.post("http://localhost:5000/query", json={"query": query})
            if res.ok:
                st.markdown("**Answer:**")
                st.write(res.json().get("response"))
            else:
                st.error("Backend returned an error. Please check the Flask server logs.")
        except Exception as e:
            st.error(f"Error contacting backend: {e}")
