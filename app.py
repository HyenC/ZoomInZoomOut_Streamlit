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

   
img1 = Image.open('data/logo.png')
st.image(img1)

def main() :
    
    tab1, tab2, tab3 = st.tabs(["Topic", "Model", "Output"])
    with tab1:
        st.subheader("코로나19와 비대면 원격 수업")
        st.write("신종 코로나바이러스 감염증(코로나19)으로 비대면 원격 서비스 활용이 늘어나면서, <멋쟁이사자처럼 AIS> 7기 수업 역시 줌(Zoom)을 통한 온라인 수업으로 진행되고 있습니다.")
        st.write("이런 온라인 강의는 대부분 관리 효율성을 위해 어느 정도 모니터링이 필요하며, 7기 수강생들 역시 모니터링 매니저님 덕분에 수업 집중도를 높일 수 있었습니다.")
        st.write("하지만 모니터링 매니저님 혼자서 다수의 줌 화면을 확인하는 데는 피로도가 높을 것으로 판단하였고, 저희 팀은 모니터링 매니저님의 업무 효율성을 높일 수 있는, <온라인 화상 수업 서포팅 프로그램> 을 프로젝트 주제로 선정했습니다.")
        st.image("data/topic.png")

    with tab2:
        selected_item = st.radio("", ("Mediapipe", "OpenCV", "Face Recognition", "Yolo"), horizontal=True)

        if selected_item == "Mediapipe":
            st.header("Mediapipe")
            st.write(
                f"""
                    - 구글에서 주로 인체를 대상으로 하는 비전인식기능들을 AI모델 개발과 기계 학습까지 마친 상태로 제공하는 서비스
                    - 다양한 프로그램 언어에서 사용하기 편하게 라이브러리 형태로 모듈화되어 제공되며 사용 방법 또한 풍부하게 제공되기 때문에 몇 가지 간단한 단계로 Mediapipe에서 제공하는 AI기능을 활용한 응용 프로그램 개발이 가능
                """
            )
            st.header("MediaPipe의 Face Detection")
            st.write(
                f"""
                    - 6개의 랜드마크(오른쪽 눈, 왼쪽 눈, 코 끝, 입 중심, 오른쪽 귀 윗 가장자리 위의 점 및 왼쪽 귀 윗 가장자리 위의 점) 및 다중 얼굴 지원과 함께 제공되는 초고속 얼굴 감지 솔루션
                """
            )
        elif selected_item == "OpenCV":
            st.write("B!!")
        elif selected_item == "Face Recognition":
            st.write("C!!!")
        else:
            col1, col2 = st.columns(2)

            with col1:
                st.subheader("yolo3")
                st.image("data/yolov3.png")

            with col2:
                st.subheader("yolo3")
                st.image("data/yolov5.png")

            st.subheader("yolo3")
            st.image("data/yolov7.png")

    with tab3:
        st.write("무엇을 넣을까요")
    
    
if __name__ == "__main__" :
    main()
