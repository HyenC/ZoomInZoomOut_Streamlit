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
            st.write(f"""
                - 구글에서 주로 인체를 대상으로 하는 비전인식기능들을 AI모델 개발과 기계 학습까지 마친 상태로 제공하는 서비스
                - 다양한 프로그램 언어에서 사용하기 편하게 라이브러리 형태로 모듈화되어 제공되며 사용 방법 또한 풍부하게 제공되기 때문에 몇 가지 간단한 단계로 Mediapipe에서 제공하는 AI기능을 활용한 응용 프로그램 개발이 가능
            """)
            st.header("MediaPipe의 Face Detection")
            st.write(f"""
                - 6개의 랜드마크(오른쪽 눈, 왼쪽 눈, 코 끝, 입 중심, 오른쪽 귀 윗 가장자리 위의 점 및 왼쪽 귀 윗 가장자리 위의 점) 및 다중 얼굴 지원과 함께 제공되는 초고속 얼굴 감지 솔루션
            """)
        elif selected_item == "OpenCV":
            st.header("OpenCV")
            st.write(f"""
                - Open Source Computer Vision의 약자로, 영상 처리에 사용할 수 있는 오픈 소스 라이브러리
                - 컴퓨터가 사람의 눈처럼 인식할 수 있게 처리해주는 역할을 하기도 하며, 카메라 어플에서도 OpenCV가 사용됨
                - 추가로 사용되는 예시 : 공장에서 제품 검사, 의료 영상 처리 및 보정 그리고 판단, CCTV영상, 로보틱스
             """)
        elif selected_item == "Face Recognition":
            st.header("Face Recognition")
            st.write(f"""
                - 해당 라이브러리는 딥러닝 기반으로 제작된 [dlib](http://dlib.net/)의 얼굴 인식 기능을 사용하여 구축
                - 이 모델은 [Labeled Faces in the Wild](http://vis-www.cs.umass.edu/lfw/) 기반으로 99.38%의 정확도를 가짐([https://github.com/ageitgey/face_recognition](https://github.com/ageitgey/face_recognition))
             """)
        else:
            col1, col2 = st.columns(2)
            with col1:
                st.image("data/yolov3.png")
                st.caption("사진1️⃣ : YOLOv3, 4, 5를 비교(4와 5 버전의 우위가 정확하지 않음)")
            with col2:
                st.image("data/yolov5.png")
                st.caption("사진2️⃣ : 4, 5를 따로 비교한 자료")

            st.image("data/yolov7.png")
            
            st.subheader("📝 결론")
            st.write(f"""
                - YOLOv4는 v5에 비해 느리게 동작하지만 FPS성능의 최적화 가능
                - YOLOv5는 v4에 비해 더 쉽게 환경을 구성하고, 구현 가능
                - YOLOv7은 real-time object detection 분야에서 SOTA로 인정받고 있으며, 그 전 모델들보다 훨씬 더 좋은 성능과 속도를 가짐
            """)

    with tab3:
        st.image("data/o1.png")
        
        col1, col2, col3 = st.columns(3)
            with col1:
                st.image("data/o2.png")
            with col2:
                st.image("data/o3.png")
            with col3:
                st.image("data/o4.png")
        
        st.image("data/o5.png")
        
        col4, col5 = st.columns(2)
            with col4:
                st.image("data/o6.png")
            with col5:
                st.image("data/o7.png")
    
    
if __name__ == "__main__" :
    main()
