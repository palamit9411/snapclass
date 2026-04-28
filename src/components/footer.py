import streamlit as st
import base64
import os

def get_base64_image():
    base_dir = os.path.dirname(__file__)
    full_path = os.path.join(base_dir, "footer_icon.png")
    with open(full_path, "rb") as f:
        return base64.b64encode(f.read()).decode()

def footer(text_color="white"):
    img_base64 = get_base64_image()

    st.markdown(
        f"""
        <div style="margin:20px auto; display:flex; justify-content:center; align-items:center; gap:8px; color:{text_color}; font-weight:700; letter-spacing:0.5px; width:fit-content; padding:10px 18px; border-radius:14px; background-color:#0D0D0D;">
            
            <span style="font-size:16px;">Created with ❤️ by</span>
            
            <img src="data:image/png;base64,{img_base64}" 
                 style="height:80px; transform:scale(1.5); transform-origin:center; filter:brightness(2.2) contrast(1.7);" />
        
        </div>
        """,
        unsafe_allow_html=True
    )

def footer_home():
    footer("white")

def footer_dashboard():
    footer("white")
