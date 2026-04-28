import streamlit as st
import base64
import os

def get_base64_image():
    base_dir = os.path.dirname(__file__)
    full_path = os.path.join(base_dir, "footer_icon.png")
    with open(full_path, "rb") as f:
        return base64.b64encode(f.read()).decode()

def footer(text_color="black"):
    img_base64 = get_base64_image()

    st.markdown(
        f"""
        <div style="
            margin-top:2.5rem;
            display:flex;
            justify-content:center;
            align-items:center;
            gap:8px;
            font-weight:800;
            color:{text_color};
            letter-spacing:0.5px;
        ">
            <span>Created with ❤️ by</span>
            <img src="data:image/png;base64,{img_base64}" 
                 style="
                    height:70px;
                    vertical-align:middle;
                    filter: brightness(1.9) contrast(1.5);
                 " />
        </div>
        """,
        unsafe_allow_html=True
    )

def footer_home():
    footer("white")

def footer_dashboard():
    footer("black")
