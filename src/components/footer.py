import streamlit as st

def footer(text_color="white"):
    logo_url = "https://raw.githubusercontent.com/palamit9411/snapclass/main/src/components/footer_icon.png"

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
            <img src="{logo_url}" style="height:100px;" />
        </div>
        """,
        unsafe_allow_html=True
    )

def footer_home():
    footer("white")

def footer_dashboard():
    footer("black")
