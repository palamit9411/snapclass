import streamlit as st
import base64
import os

def get_base64_image(path):
    base_dir = os.path.dirname(__file__)
    full_path = os.path.join(base_dir, "footer_icon.png")
    with open(full_path, "rb") as f:
        return base64.b64encode(f.read()).decode()

def footer(text_color="black"):
    img_base64 = get_base64_image("footer_icon.png")

    st.markdown(
        f"""
        <div style="
            margin-top:2.5rem;
            display:flex;
            justify-content:center;
            align-items:center;
            gap:10px;
            font-weight:600;
            color:{text_color};
            letter-spacing:0.5px;
        ">
            <span style="opacity:0.8;">Created with ❤️ by</span>
            <img src="data:image/png;base64,{img_base64}" 
                 style="
                    height:100px;
                    vertical-align:middle;
                    filter: contrast(1.2) brightness(1.1);
                 " />
        </div>
        """,
        unsafe_allow_html=True
    )

def footer_home():
    footer("white")

def footer_dashboard():
    footer("black")
