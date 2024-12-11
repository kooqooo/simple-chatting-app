from pprint import pprint
import streamlit as st

from utils import write_message, write_messages, get_response_stream

st.set_page_config(page_title="18장 과제", page_icon="", layout="centered")
st.markdown(
    "<h3 style='text-align: center;'>💬 [2024년 2학기] 딥러닝/클라우드 18장 과제</h3>",
    unsafe_allow_html=True,
)

# 세션 상태 초기화
if "chat_started" not in st.session_state: # 채팅이 시작되었는지 여부
    st.session_state.chat_started = False
if "messages" not in st.session_state: # 메시지 리스트
    st.session_state.messages = []


write_messages(st.session_state.messages)

if not st.session_state.chat_started:
    st.session_state.chat_started = True
    message = {"role": "assistant", "content": "안녕하세요! 무엇을 도와드릴까요?"}
    st.session_state.messages.append(message)
    write_message(message)

if user_input := st.chat_input("텍스트를 입력하세요."):
    user_message = {"role": "user", "content": user_input}
    st.session_state.messages.append(user_message)
    pprint(st.session_state.messages)
    print("\n"*3)
    write_message(user_message)

    with st.chat_message("assistant"):
        st.write_stream(get_response_stream(st.session_state.messages))
