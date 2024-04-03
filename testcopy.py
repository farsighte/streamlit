import streamlit as st

# HTML과 CSS를 사용하여 슬라이드 구현
slider_html = """
<div class="container">
  <div class="item">슬라이드 1</div>
  <div class="item">슬라이드 2</div>
  <div class="item">슬라이드 3</div>
</div>

<style>
.container {
  display: flex;
  overflow-x: auto;
}

.item {
  flex: none;
  width: 80%; /* 슬라이드의 너비를 설정 */
  margin: 10px;
  background-color: #f0f0f0;
  text-align: center;
}

/* 스크롤바 숨기기 */
.container::-webkit-scrollbar {
  display: none;
}
</style>
"""

st.markdown(slider_html, unsafe_allow_html=True)