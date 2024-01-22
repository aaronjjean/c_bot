import streamlit as st

def main():
    st.title("Simple Streamlit App")
    user_input = st.text_input("Enter your name:")
    st.write(f"Hello, {user_input}!")

if __name__ == "__main__":
    main()