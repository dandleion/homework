import streamlit as st

# ✅ set_page_config는 가장 먼저 위치해야 함
st.set_page_config(page_title="기능으로 찾는 플레이봇 명령어", page_icon="🔍")

# 명령어 설명 데이터
commands = {
    "move": "로봇을 앞으로 한 칸 이동시켜요. (예: 앞으로 가기, 전진)",
    "turn_left": "로봇이 왼쪽으로 90도 돌아요. (예: 왼쪽으로 회전)",
    "turn_right": "로봇이 오른쪽으로 90도 돌아요. (예: 오른쪽으로 회전)",
    "turn_off": "로봇의 전원을 꺼요. (예: 종료, 끄기)",
    "say": "로봇이 입력한 말을 해요. (예: 말하기, 음성 출력)",
    "popup": "팝업 메시지를 화면에 띄워요. (예: 알림창)",
    "repeat": "동일한 명령을 반복 실행해요. (예: 반복하기)",
    "get_random": "랜덤한 숫자를 생성해요. (예: 무작위 숫자)",
    "print": "메시지를 콘솔에 출력해요. (예: 출력)",
    "if": "조건이 맞으면 실행돼요. (예: 조건문)",
    "while": "조건이 참인 동안 반복해요. (예: 반복, 조건반복)"
}

# 스타일 설정
st.markdown("""
    <style>
    .title {
        font-size: 48px;
        text-align: center;
        color: #ff6f91;
        font-weight: bold;
    }
    .chat-box {
        background-color: #fff8f0;
        padding: 20px;
        border-radius: 20px;
        border: 2px dashed #ffb6b9;
    }
    </style>
""", unsafe_allow_html=True)

# 제목
st.markdown('<div class="title">🔍 기능으로 찾는 명령어 챗봇</div>', unsafe_allow_html=True)
st.markdown("### 🐥 원하는 기능을 입력하면 어떤 명령어를 써야 할지 알려줄게요!")

# 사용자 입력
user_input = st.text_input("무엇을 하고 싶나요? (예: 왼쪽으로 회전, 앞으로 가기, 출력 등)").strip()

# 검색 로직
if user_input:
    found = []
    for cmd, desc in commands.items():
        if user_input in desc:
            found.append((cmd, desc))

    st.markdown('<div class="chat-box">', unsafe_allow_html=True)

    if found:
        st.markdown("✅ **이런 명령어가 있어요!**")
        for cmd, desc in found:
            st.markdown(f"- **`{cmd}()`**: {desc}")
    else:
        st.markdown("😢 해당 기능에 맞는 명령어를 찾을 수 없어요.")
    
    st.markdown('</div>', unsafe_allow_html=True)

# 힌트
with st.expander("💡 예시 기능 키워드 보기"):
    st.markdown("예: `왼쪽으로 회전`, `앞으로 가기`, `말하기`, `반복하기`, `조건문`, `출력`")
