import streamlit as st

def footer(text_color="white"):
    logo_url = "https://raw.githubusercontent.com/palamit9411/snapclass/main/src/components/footer_icon.png"

    st.markdown(f"""
        <div style="
            margin-top:2rem;
            display:flex;
            gap:8px;
            justify-content:center;
            align-items:center;
        ">
            <p style="
                font-weight:600;
                color:{text_color};
                margin:0;
            ">
                Created with ❤️ by
            </p>
            <img src="{logo_url}" style="height:26px;" />
        </div>
    """, unsafe_allow_html=True)



def footer_home():
    footer("white")

def footer_dashboard():
    footer("black")
