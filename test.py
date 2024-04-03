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
    company = encode_image_to_base64("image/background/company.jpg") 
    custom_styles = f"""
        <style>

          
        /* 전체 페이지 배경 이미지 설정 */
        [data-testid="stAppViewContainer"] {{
            background-image: url("data:image/jpeg;base64,{company}");
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
            opacity: 0
            background-color: rgba(0, 0, 0, 1); 
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


# 이미지 파일 불러오기 및 사이드바에 이미지 표시
image = Image.open('image/logo/1.jpg')
st.sidebar.image(image, caption='사이드바 이미지 설명')

st.markdown("""
    
    <div>
    <h1 style="color: black;">다온아트라이트(DAON ART LIGHT)</h1>
    <h2 style="color: black;">우리는 다온아트라이트(DAON ART LIGHT)입니다</h2>
    <p style="color: black;">열정, 혁신, 그리고 빛을 통한 예술 창조를 지향합니다. 다온아트라이트는 무대 특수조명 렌탈, 디자인 및 프로그래밍 서비스를 제공하는 전문 기업입니다. 대전의 중심에서 시작된 우리의 여정은 예술과 기술이 만나는 지점에서 새로운 가능성을 탐구합니다.</p>
    <h2 style="color: black;">우리의 서비스</h2>
    <p style="color: black;">- <strong>혁신적인 조명 솔루션:</strong> 공연, 이벤트, 전시회를 위한 혁신적인 무대 조명 디자인과 프로그래밍을 제공합니다.</p>
    <p style="color: black;">- <strong>맞춤형 디자인 및 렌탈 서비스:</strong> 고객의 니즈에 맞춘 조명 설계와 함께, 최신 기술의 조명 장비 렌탈을 제공합니다.</p>
    <p style="color: black;">- <strong>전문성과 창의력:</strong> 업계 경험을 바탕으로 한 우리 팀의 전문성과 젊은 세대의 창의력이 결합된 서비스를 제공합니다.</p>
    <h2 style="color: black;">우리의 비전</h2>
    <p style="color: black;">다온아트라이트는 기술과 예술의 결합을 통해 무대 조명의 새로운 기준을 제시합니다. 우리는 지속적인 혁신과 창의적인 디자인을 통해, 무대 조명이 단순한 밝기의 조절을 넘어 예술 작품 자체가 될 수 있음을 증명하고자 합니다.</p>
    <h2 style="color: black;">연락처 정보</h2>
    <p style="color: black;">함께 빛나는 미래를 위해 다온아트라이트와 함께하시길 원하신다면, 지금 바로 우리에게 연락하세요.</p>
    </div>

""", unsafe_allow_html=True)

