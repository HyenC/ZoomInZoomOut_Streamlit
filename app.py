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
		st.subheader("Mediapipe")
              	st.write("A!")
        elif selected_item == "OpenCV":
		st.subheader("OpenCV")
              	st.write("B!!")
        elif selected_item == "Face Recognition":
		st.subheader("Face Recognition")
              	st.write("C!!!")
        else:
		st.subheader("Yolo")
              	col1, col2, col3 = st.columns(3)

		with col1:
			st.header("Yolov3")
   			st.image("https://s3.us-west-2.amazonaws.com/secure.notion-static.com/3eb0dd96-562d-4937-a766-b1789baa301e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45EIPT3X45%2F20230104%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20230104T184234Z&X-Amz-Expires=86400&X-Amz-Signature=8c93dae77a6959f98243e67ede33b2d907708e190116f3a1d8e9a191b761d688&X-Amz-SignedHeaders=host&response-content-disposition=filename%3D%22Untitled.png%22&x-id=GetObject")

		with col2:
   			st.header("Yolov5")
   			st.image("https://s3.us-west-2.amazonaws.com/secure.notion-static.com/e5412de4-0d2d-4eb1-94da-d538c99dd641/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45EIPT3X45%2F20230104%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20230104T184317Z&X-Amz-Expires=86400&X-Amz-Signature=f11e4e6cde071c027320b2fa59f7d079065efc5200c8c313c8cf39fa95139c46&X-Amz-SignedHeaders=host&response-content-disposition=filename%3D%22Untitled.png%22&x-id=GetObject")

		with col3:
   			st.header("Yolov7")
   			st.image("https://s3.us-west-2.amazonaws.com/secure.notion-static.com/a6c530d4-d901-4d0f-9089-74cb2eed2294/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45EIPT3X45%2F20230104%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20230104T184341Z&X-Amz-Expires=86400&X-Amz-Signature=53ba0c07f9486669f4aff96ed0368da2d4ba08ee99b402474789469bb371770e&X-Amz-SignedHeaders=host&response-content-disposition=filename%3D%22Untitled.png%22&x-id=GetObject")

    with tab3:
	st.write("무엇을 넣을까요")
    
    
if __name__ == "__main__" :
    main()
