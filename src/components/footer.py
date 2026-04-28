
import streamlit.components.v1 as components

def footer(text_color="white"):
    logo_url = "https://raw.githubusercontent.com/palamit9411/snapclass/main/src/components/footer_icon.png"

    html = f"""
    <div style="
        display:flex;
        justify-content:center;
        align-items:center;
        gap:6px;
        font-family:sans-serif;
    ">
        <span style="
            color:{text_color};
            font-weight:700;
            font-size:0.95rem;
        ">
            Created with ❤️ by
        </span>

        <img src="{logo_url}" 
             style="
                height:1.6rem;
                width:auto;
                object-fit:contain;
             " />
    </div>
    """

    components.html(html, height=60)
    
def footer_home():
    footer("white")

def footer_dashboard():
    footer("black")
