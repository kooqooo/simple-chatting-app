import streamlit as st
from openai import OpenAI

openai = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

def write_message(message: dict[str, str]):
    with st.chat_message(message["role"]):
        st.write(message["content"])


def write_messages(messages: list[dict[str, str]]):
    for message in messages:
        write_message(message)


def write_input():
    return st.text_input("메시지 입력", key="input")


def write_stream_message(message: dict[str, str]):
    with st.chat_message("assistant"):
        st.write_stream(message["content"])


def get_response_stream(messages: list[dict[str, str]]):
    response = openai.chat.completions.create(
        model="gpt-4o-mini",
        messages=messages,
        stream=True,
    )
    
    full_response = "" # 전체 응답을 저장할 변수

    # 스트리밍 응답 처리하여 yield 반환
    for chunk in response:
        if chunk.choices[0].delta.content is not None:
            content = chunk.choices[0].delta.content
            full_response += content
            yield content

    st.session_state.messages.append({"role": "assistant", "content": full_response})