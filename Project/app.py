import streamlit as st
import pandas as pd
import os

# CSV 파일 경로
DATA_PATH = "data/users.csv"

# 데이터 저장 함수
def save_user(data):
    if not os.path.exists(DATA_PATH):
        df = pd.DataFrame(columns=["아이디", "비번", "성별", "나이", "얼굴상 테스트 결과", "DISC 검사 결과"])
        df.to_csv(DATA_PATH, index=False)
    else:
        df = pd.read_csv(DATA_PATH)
    df = df.append(data, ignore_index=True)
    df.to_csv(DATA_PATH, index=False)

# 로그인 인증 함수
def authenticate(username, password):
    if not os.path.exists(DATA_PATH):
        return False
    df = pd.read_csv(DATA_PATH)
    user = df[(df["아이디"] == username) & (df["비번"] == password)]
    return not user.empty

# Streamlit UI
st.title("회원가입 및 로그인 시스템")

menu = st.sidebar.selectbox("메뉴 선택", ["회원가입", "로그인"])

if menu == "회원가입":
    st.header("회원가입 페이지")
    username = st.text_input("아이디")
    password = st.text_input("비번", type="password")
    gender = st.radio("성별", ["남성", "여성", "기타"])
    age = st.number_input("나이", min_value=1, step=1)
    animal_test_result = st.text_area("얼굴상(동물상) 테스트 결과")
    disc_result = st.text_area("DISC 검사 결과")

    if st.button("회원가입"):
        if username and password:
            save_user({
                "아이디": username,
                "비번": password,
                "성별": gender,
                "나이": age,
                "얼굴상 테스트 결과": animal_test_result,
                "DISC 검사 결과": disc_result,
            })
            st.success("회원가입 성공!")
        else:
            st.error("아이디와 비밀번호를 입력하세요.")

elif menu == "로그인":
    st.header("로그인 페이지")
    username = st.text_input("아이디")
    password = st.text_input("비번", type="password")

    if st.button("로그인"):
        if authenticate(username, password):
            st.success(f"환영합니다, {username}님!")
        else:
            st.error("아이디 또는 비밀번호가 잘못되었습니다.")
