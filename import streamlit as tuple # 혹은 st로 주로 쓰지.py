import streamlit as tuple  # 혹은 st로 주로 쓰지만, 직관적으로 st를 사용하겠습니다.
import streamlit as st

# 1. 앱 제목 및 상단 꾸미기
st.title("🎓 영어 천재 되기 퀴즈!")
st.subheader("제시된 영어 단어의 올바른 뜻을 맞춰보세요.")
st.markdown("---")

# 2. 데이터 정의
words = ("apple", "banana", "love")
meanings = ("사과", "바나나", "사랑")
score = 0

# 사용자의 입력을 저장할 리스트 생성
user_answers = []

# 3. 입력 위젯 (반복문을 통해 st.text_input 생성)
st.write("### 📝 문제를 풀어보세요")
for i in range(len(words)):
    # 각 입력창을 구분할 수 있도록 텍스트 입력 위젯 배치
    answer = st.text_input(f"'{words[i]}'의 한글 뜻을 입력하세요!", key=f"word_{i}")
    user_answers.append(answer.strip())  # 공백 제거 후 리스트에 저장

st.markdown("---")

# 4. 결과 출력 로직 (버튼을 누르면 실행)
if st.button("점수 및 결과 확인하기", type="primary"):
    st.write("### 📊 채점 결과")
    
    # 각 문항 채점
    for i in range(len(words)):
        if user_answers[i] == meanings[i]:
            st.success(f"⭕ '{words[i]}': 축하합니다 성공!")
            score += 1
        else:
            st.error(f"❌ '{words[i]}': 실패ㅠㅠ (입력한 값: {user_answers[i]})")
            st.info(f"💡 정답은 **'{meanings[i]}'** 입니다.")
            
    st.markdown("---")
    
    # 최종 점수 및 메시지 출력
    st.metric(label="당신의 최종 점수", value=f"{score} / {len(words)} 점")
    
    if score == 3:
        st.balloons()  # 축하 효과 효과음/효과
        st.success("🎉 영어천재가 된 것을 축하드립니다!")
    else:
        st.warning("🔄 다시 도전 해보세요!")