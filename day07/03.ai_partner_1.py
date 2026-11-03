import streamlit as st
import os
import httpx2
from openai import OpenAI

print("------> 重新执行文件，渲染展示页面")

http_client = httpx2.Client(
    headers={"Accept-Encoding": "gzip, deflate"}
)

#页面的配置项
st.set_page_config(
    page_title="AI智能伴侣",
    page_icon="🤖",
    #布局
    layout="wide",
    #控制的是测量边栏的状态
    initial_sidebar_state="expanded",
    menu_items={}
)
#大标题
st.title("AI智能伴侣")

#创建与AI大模型交互的客户端对象（DEEPSEEK_API_KEY 环境变量的名字，值就是DeepSeek的API_KEYd）
client = OpenAI(
    api_key=st.secrets["DEEPSEEK_API_KEY"],
    base_url="https://api.deepseek.com",
    http_client=http_client #传入自定义客户端
)

#系统提示词
system_prompt = "你是一个非常可爱的AI助理，你的名字叫果冻，请你使用可爱俏皮的语气回答用户的问题"

#初始化聊天信息
if 'messages' not in st.session_state:
    st.session_state.messages = []

#展示聊天信息
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])



#消息输入
prompt = st.chat_input("请输入消息")
if prompt:#字符串会自动转化为布尔值，若字符串非空，则为True，否则为False
    st.chat_message("user").write(prompt)
    print("------>调用AI大模型，提示词：",prompt)
    #保存用户输入的提示词
    st.session_state.messages.append({"role": "user", "content": prompt})
    # 与AI大模型进行交互
    response = client.chat.completions.create(
        model="deepseek-flash",
        messages=[
            {"role": "system",
             "content": system_prompt},
            {"role": "user", "content": prompt},
        ],
        stream=False
    )


    # 输出大模型返回的结果
    print("----------->大模型返回的结果：",response.choices[0].message.content)
    st.chat_message("assistant").write(response.choices[0].message.content)
    # 保存AI大模型的返回结果

    # st.session_state.messages：存在 Streamlit 会话状态中的消息历史列表（通常是一个 list of dict），用于在页面重跑之间保留聊天记录。
    # .append({...})：向列表末尾添加一条新消息。
    # "role": "assistant"：标识这条消息来自 AI 助手（对应 OpenAI Chat Completions API 的角色格式）。
    # response.choices[0].message.content：从 API 返回对象中取出第一个候选回复的文本内容。
    # st.session_state.messages.append({"role": "assistant", "content": response.choices[0].message.content})


