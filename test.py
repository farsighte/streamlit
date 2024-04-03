import streamlit as st
from PIL import Image
import base64

def encode_image_to_base64(image_path):
    """이미지 파일을 Base64로 인코딩하는 함수."""
    with open(image_path, "rb") as file:
        return base64.b64encode(file.read()).decode('utf-8')

def apply_custom_styles():
    """사용자 정의 스타일을 적용하는 함수."""
    bg_img = encode_image_to_base64("image/background/1.jpg")
    sidebar_img = encode_image_to_base64('image/sidebar/2.jpg')

    custom_styles = f"""
        <style>

          
        /* 전체 페이지 배경 이미지 설정 */
        [data-testid="stAppViewContainer"] {{
            background-color: #000000;
            background-size: cover;
            background-attachment: fixed;
        }}

        /* 헤더 배경 투명하게 설정 */
        [data-testid="stHeader"] {{
            background-color: rgba(0,0,0,0);
            visibility: hidden;
        }}

        /* 사이드바 배경 이미지 설정 */
        [data-testid="stSidebarContent"] {{
            background-image: url("data:image/jpeg;base64,{sidebar_img}");
            background-size: cover;
            background-position: center;
            border-right: 5px solid #FFFF00; /* 오른쪽 테두리 설정 */
            border-radius: 5px; /* 둥근 모서리 추가 */
        }}
        </style>
    """
    st.markdown(custom_styles, unsafe_allow_html=True)

# 사용자 정의 스타일 적용
apply_custom_styles()

st.title("아몸랑 니")

# 이미지 파일 불러오기 및 사이드바에 이미지 표시
image = Image.open('image/logo/1.jpg')
st.sidebar.image(image, caption='사이드바 이미지 설명')
