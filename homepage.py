import streamlit as st
import base64
import requests  # 이 부분을 추가

image_file = {
    'main': "image/page/main/1.jpg",
    'page_1': "image/page/page_1/1.jpg",
    'page_2': "image/page/page_2/1.jpg",
    'sidebar': "image/sidebar/1.jpg",  # 이미지 경로가 오타 수정됨
}

def get_image_as_base64(path):
    with open(path, "rb") as image_file:
        encoded = base64.b64encode(image_file.read()).decode('utf-8')
    return "data:image/jpeg;base64," + encoded

def background_image(url):
    kkkaa = get_image_as_base64(url)
    st.markdown(
        f"""
        <style>
            .stApp {{
                background-image: url({kkkaa});
                background-size: cover;
            }}
        </style>
        """,
        unsafe_allow_html=True
    )

def main_page():
    background_image(image_file['main'])

def page_1():
    background_image(image_file['page_1'])

def page_2():
    background_image(image_file['page_2'])

# 초기화
if "page" not in st.session_state:
    st.session_state.page = 'main'

# 페이지 이동 버튼
if st.sidebar.button("메인 페이지"):
    st.session_state.page = 'main'
if st.sidebar.button("페이지 1"):
    st.session_state.page = 'page_1'
if st.sidebar.button("페이지 2"):
    st.session_state.page = 'page_2'

# 페이지 전환
if st.session_state.page == 'main':
    main_page()
elif st.session_state.page == 'page_1':
    page_1()
elif st.session_state.page == 'page_2':
    page_2()
