import streamlit as st

# 상단 바에 제목을 설정합니다.
st.title("나의 Streamlit 앱")

# 상단 바에 메뉴를 추가할 수 있습니다.
menu = ["홈", "페이지1", "페이지2", "페이지3"]
choice = st.beta_container().radio("메뉴", menu)

# 선택한 메뉴에 따라 다른 내용을 표시할 수 있습니다.
if choice == "홈":
    st.write("이곳은 홈 페이지입니다.")
elif choice == "페이지1":
    st.write("이곳은 페이지 1입니다.")
elif choice == "페이지2":
    st.write("이곳은 페이지 2입니다.")
elif choice == "페이지3":
    st.write("이곳은 페이지 3입니다.")
