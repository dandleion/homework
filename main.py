import streamlit as st

st.set_page_config(page_title="PlayBot 기능 검색 챗봇", page_icon="🐣")

# 이미지 URL
title_icon_url = "https://i.imgur.com/vOe1b6T.png"   # 병아리 아이콘
cat_image_url = "https://i.imgur.com/JT6aONc.gif"    # 걷는 고양이 (움직임)

# 명령어 사전
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

# 💅 CSS
st.markdown(f"""
    <style>
    /* 타이틀바 */
    .title-bar {{
        display: flex;
        align-items: center;
        gap: 15px;
        justify-content: center;
        margin-bottom: 10px;
    }}
    .title-bar img {{
        width: 60px;
        height: 60px;
    }}
    .title-text {{
        font-size: 42px;
        font-family: 'Courier New', monospace;
        color: #ffd95a;
        font-weight: bold;
    }}

    .subtitle {{
        font-size: 20px;
        text-align: center;
        color: #b3b3b3;
        margin-bottom: 30px;
        font-family: 'Courier New', monospace;
    }}

    .cat-walk-wrapper {{
        position: relative;
        height: 100px;
        overflow: hidden;
        margin-bottom: 30px;
    }}

    .cat {{
        position: absolute;
        height: 100px;
        animation: moveLeftRight 6s linear infinite;
    }}

    @keyframes moveLeftRight {{
        0% {{ left: 0; }}
        50% {{ left: calc(100% - 100px); transform: scaleX(1); }}
        51% {{ transform: scaleX(-1); }}
        100% {{ left: 0; transform: scaleX(-1); }}
    }}

    .chat-box {{
        background-color: #2d2d2d;
        padding: 20px;
        border-radius: 15px;
        border: 1px solid #444;
        font-family: 'Courier New', monospace;
        color: #e6e6e6;
        box-shadow: 0 0 10px #ffd95a66;
    }}

    .command {{
        background-color: #1a1a1a;
        color: #9cdcfe;
        padding: 8px;
        border-radius: 8px;
        font-family: 'Courier New', monospace;
        font-size: 16px;
        margin-bottom: 10px;
    }}
    </style>
""", unsafe_allow_html=True)

# 🐥 제목
st.markdown(f"""
    <div class="title-bar">
        <img src="{title_icon_url}">
        <div class="title-text">PlayBot 코드 챗봇</div>
    </div>
""", unsafe_allow_html=True)

# 🌈 부제목
st.markdown('<div class="subtitle">원하는 기능을 입력하면 어떤 명령어를 써야 할지 알려줄게요!</div>', unsafe_allow_html=True)

# 🐱 걷는 고양이 애니메이션
st.markdown(f"""
    <div class="cat-walk-wrapper">
        <img src="{cat_image_url}" class="cat">
    </div>
""", unsafe_allow_html=True)

# 🎯 사용자 입력
user_input = st.text_input("💬 하고 싶은 기능을 입력하세요 (예: 왼쪽으로 회전, 앞으로 가기 등)", "").strip()

# 🔎 결과
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

# 💡 도움말
with st.expander("💡 예시 기능 키워드 보기", expanded=False):
    st.markdown("예: `왼쪽으로 회전`, `앞으로 가기`, `말하기`, `조건문`, `출력`, `무작위 숫자`")
