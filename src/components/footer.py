import streamlit as st
import base64

def get_base64_image(path):
    with open(path, "rb") as f:
        return base64.b64encode(f.read()).decode()

def footer(text_color="white"):
    img_base64 = get_base64_image("src/components/footer_icon.png")

    st.markdown(
        f"""
        <div style="
            margin-top:2rem;
            display:flex;
            justify-content:center;
            align-items:center;
            gap:8px;
            font-weight:600;
            color:{text_color};
            opacity:0.9;
            letter-spacing:0.5px;
        ">
            <span>Created with 💖 by</span>
            <img src="data:image/png;base64,{img_base64}" 
                 style="height:36px; vertical-align:middle;" />
        </div>
        """,
        unsafe_allow_html=True
    )

def footer_home():
    footer("white")

def footer_dashboard():
    footer("black")
