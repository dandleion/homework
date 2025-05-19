import streamlit as st

st.set_page_config(page_title="코딩플랫폼 내장함수 검색 챗봇", page_icon="🤖")

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

# 🎨 스타일 추가
st.markdown("""
    <style>
    body {
        background-color: #1e1e1e;
    }
    .title {
        font-size: 42px;
        text-align: center;
        color: #ffd95a;
        font-family: 'Courier New', monospace;
        font-weight: bold;
        margin-bottom: 0;
    }
    .subtitle {
        font-size: 20px;
        text-align: center;
        color: #b3b3b3;
        margin-bottom: 20px;
        font-family: 'Courier New', monospace;
    }
    .chat-box {
        background-color: #2d2d2d;
        padding: 20px;
        border-radius: 15px;
        border: 1px solid #444;
        font-family: 'Courier New', monospace;
        color: #e6e6e6;
        box-shadow: 0 0 10px #ffd95a66;
    }
    .command {
        background-color: #1a1a1a;
        color: #9cdcfe;
        padding: 8px;
        border-radius: 8px;
        font-family: 'Courier New', monospace;
        font-size: 16px;
        margin-bottom: 10px;
    }
    .robot {
        text-align: center;
        font-size: 70px;
        margin-top: -10px;
        margin-bottom: -10px;
        position: relative;
        animation: moveLeftRight 4s ease-in-out infinite;
        display: inline-block;
        user-select: none;
    }
    @keyframes moveLeftRight {
        0% { left: 0; transform: scaleX(1); }
        50% { left: calc(100vw - 70px); transform: scaleX(1); }
        51% { transform: scaleX(-1); }
        100% { left: 0; transform: scaleX(-1); }
    }

    /* ✅ 입력창 스타일 - 핑크색 배경 */
    .stTextInput input {
        background-color: #ffcce0 !important;
        color: black !important;
        border-radius: 10px !important;
        border: 1px solid #ff99cc !important;
        padding: 0.5rem !important;
        font-family: 'Courier New', monospace;
        font-size: 16px;
    }
    /* 입력창 감싸는 블록 제거 */
    .stTextInput {
        background: transparent !important;
        padding: 0px !important;
        box-shadow: none !important;
    }

    /* ✅ 검색 결과 위쪽 불필요한 검정 박스 제거 */
    .block-container > div:has(.stTextInput) + div {
        display: none !important;
    }

    /* 예: chat-box, 명령어 결과 카드 등은 그대로 유지 */
    .chat-box {
        background-color: #2d2d2d;
        padding: 20px;
        border-radius: 15px;
        border: 1px solid #444;
        font-family: 'Courier New', monospace;
        color: #e6e6e6;
        box-shadow: 0 0 10px #ffd95a66;
    }
    </style>
""", unsafe_allow_html=True)

# 🧠 제목
st.markdown('<div class="title">🤖 내장함수 검색 챗봇</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">기능을 입력하면 어떤 명령어를 써야 할지 알려줄게요!</div>', unsafe_allow_html=True)
st.markdown('<div class="robot">👾</div>', unsafe_allow_html=True)

# 🔍 입력창 (밝은 핑크 배경 적용됨)
user_input = st.text_input("💬 하고 싶은 기능을 입력하세요 (예: 왼쪽으로 회전, 앞으로 가기 등)", "").strip()

# 📌 검색 처리
if user_input:
    found = []
    for cmd, desc in commands.items():
        if user_input in desc:
            found.append((cmd, desc))

    st.markdown('<div class="chat-box">', unsafe_allow_html=True)

    if found:
        st.markdown("🧠 <b>검색 결과:</b>", unsafe_allow_html=True)
        for cmd, desc in found:
            st.markdown(f"<div class='command'>🧩 <b>{cmd}()</b><br>📘 {desc}</div>", unsafe_allow_html=True)
    else:
        st.markdown("😢 <i>해당 기능에 맞는 명령어를 찾을 수 없어요.</i>", unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)

# 힌트
with st.expander("💡 <b>예시 기능 키워드 보기</b>", expanded=False):
    st.markdown("예: `왼쪽으로 회전`, `앞으로 가기`, `말하기`, `조건문`, `출력`, `무작위 숫자`", unsafe_allow_html=True)
