import streamlit as st
import pandas as pd
from PIL import Image

st.set_page_config(
    page_title="줌인줌아웃",
    page_icon="📸",
    layout="wide"
)

# sidebar
with st.sidebar:
    st.markdown("## 📸줌인줌아웃📸")
    st.markdown("#### 실시간 웹캠 자리비움 탐지 보고서")

   
img = Image.open('data/logo.png')
st.image(img)

def main() :
    
    tab1, tab2, tab3 = st.tabs(["Topic", "Model", "Demonstration"])
    with tab1:
        st.header("A cat")
#         st.image("https://static.streamlit.io/examples/cat.jpg", width=200)

    with tab2:
        st.header("A dog")
#         st.image("https://static.streamlit.io/examples/dog.jpg", width=200)

    with tab3:
        st.header("An owl")
#         st.image("https://static.streamlit.io/examples/owl.jpg", width=200)
    
    
if __name__ == "__main__" :
    main()
