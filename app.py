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

   
def main() :
    
    img = Image.open('data/logo.png')
    st.image(img)

    
    
if __name__ == "__main__" :
    main()
