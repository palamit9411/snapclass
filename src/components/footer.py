
import streamlit import st

def footer(text_color="white"):
    logo_url = "https://raw.githubusercontent.com/palamit9411/snapclass/main/src/components/footer_icon.png"

    st.markdown(f"""
        <div style="
            margin-top:2.5rem;
            display:flex;
            justify-content:center;
            align-items:center;
            gap:8px;
        ">
            <span style="
                color:{text_color};
                font-weight:600;
                font-size:1.05rem;
                letter-spacing:0.3px;
            ">
                Created with ❤️ by
            </span>

            <img src="{logo_url}" 
                 style="
                    height:1.8rem;
                    width:auto;
                    object-fit:contain;
                 " />
        </div>
    """, unsafe_allow_html=True)
    
def footer_home():
    footer("white")

def footer_dashboard():
    footer("black")
