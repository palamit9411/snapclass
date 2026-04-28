import streamlit as st

def footer(text_color="white"):
    col1, col2, col3 = st.columns([3, 2, 3])

    with col2:
        st.markdown(
            f"""
            <div style="text-align:center;">
                <p style="font-weight:600; color:{text_color}; margin-bottom:5px;">
                    Created with 💖 by
                </p>
            </div>
            """,
            unsafe_allow_html=True
        )
        st.image("src/components/footer_icon.png", width=70)

def footer_home():
    footer("white")

def footer_dashboard():
    footer("black")



# def footer_home():
#     st.image("src/components/footer_icon.png", width=80)

#     # logo_url = "src/components/footer_icon.png"
#     # st.markdown(f"""
#     #     <div style="margin-top:2rem; display:flex; gap:6px; justify-content:center; align-items:center">
#     #         <p style="font-weight:bold; color:white;">Created with 💖 by </p>
#     #         <img src='{logo_url}' style='max-height:25px' />
#     #     </div>

#     #             """, unsafe_allow_html=True)
    


# def footer_dashboard():
#     st.image("src/components/footer_icon.png", width=80)

#     # logo_url = "src/components/footer_icon.png"
#     # st.markdown(f"""
#     #     <div style="margin-top:2rem; display:flex; gap:6px; justify-content:center; align-items:center">
#     #         <p style="font-weight:bold; color:black;">Created with 💖 by </p>
#     #         <img src='{logo_url}' style='max-height:25px' />
#     #     </div>

#     #             """, unsafe_allow_html=True)
