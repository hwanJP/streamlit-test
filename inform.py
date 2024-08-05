import streamlit as st
from datetime import date

# 제목 및 설명
st.title("이차전지 노칭 설비 이슈 입력 폼")
st.write("이 폼은 노칭 설비 장비의 이슈 발생 및 처리 내역을 기록하기 위한 것입니다.")

# 이슈 기본 정보 입력
st.header("기본 정보")
issue_id = st.text_input("이슈 ID")
occurrence_date = st.date_input("발생 날짜", date.today())
author = st.text_input("작성자 이름")
equipment_name = st.text_input("설비 이름")
equipment_id = st.text_input("장비 ID")

# 이슈 상세 정보 입력
st.header("이슈 상세 정보")
phenomenon = st.text_area("이슈 현상", "이슈에 대한 설명을 입력하세요.")
cause_analysis = st.text_area("원인 분석", "이슈 원인에 대한 상세 분석을 입력하세요.")
action_taken = st.text_area("조치 사항", "취해진 조치에 대한 상세 내용을 입력하세요.")
status = st.selectbox("현재 상태", ["진행 중", "해결됨", "보류"])

# 추가 정보 및 파일 첨부
st.header("추가 정보")
uploaded_file = st.file_uploader("관련 파일 첨부", type=["png", "jpg", "pdf", "docx"])
additional_notes = st.text_area("비고 및 추가 설명", "추가로 기록할 내용이 있으면 입력하세요.")

# 제출 버튼
if st.button("제출"):
    # 데이터 저장 로직을 구현
    st.success("이슈가 성공적으로 제출되었습니다.")
