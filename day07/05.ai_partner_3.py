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
system_prompt = """
你叫%s，现在使用户的真是伴侣，请完全代入伴侣角色。：
        规则：
              1.每次只回一条消息
              2.禁止任何场景或状态描述性文字
              3.匹配用户的语言
              4.回复简短，像微信聊天一样
              5.有需要的话可以用各种emoji表情和颜文字
              6.用符合伴侣性格的方式对话
              7.回复的内容，要充分体现伴侣的性格特征
        伴侣性格：
              %s
        你必须严格遵守上述规则来恢复用户。
"""

#初始化聊天信息
if 'messages' not in st.session_state:
    st.session_state.messages = []
if "nick_name" not in st.session_state:
    st.session_state.nick_name = "小琴"
if "nature" not in st.session_state:
    st.session_state.nature = "活泼俏皮开朗的四川姑娘"
#展示聊天信息
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

#左侧的侧边栏 - with：streamlit中上下文管理器
with st.sidebar:
    st.subheader("伴侣信息")
    #昵称输入框
    nick_name = st.text_input("昵称",placeholder="请输入昵称",value=st.session_state.nick_name)
    if nick_name:
        st.session_state.nick_name = nick_name
    #性格输入框
    nature = st.text_area("性格",placeholder="请输入性格",value=st.session_state.nature)
    if nature:
        st.session_state.nature = nature
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
             "content": system_prompt % (st.session_state.nick_name, st.session_state.nature)},
            *st.session_state.messages
        ],
        stream=True
    )


    # 输出大模型返回的结果(非流式输出的解析方式)
    # print("----------->大模型返回的结果：",response.choices[0].message.content)
    # st.chat_message("assistant").write(response.choices[0].message.content)
    # 保存AI大模型的返回结果

    #输出大模型返回的结果（流式输出的解析方式）
    response_message = st.empty()
    full_response = ""
    for chunk in response:
        if chunk.choices[0].delta.content is not None:
            content = chunk.choices[0].delta.content
            full_response += content
            response_message.chat_message("assistant").write(full_response)



    # st.session_state.messages：存在 Streamlit 会话状态中的消息历史列表（通常是一个 list of dict），用于在页面重跑之间保留聊天记录。
    # .append({...})：向列表末尾添加一条新消息。
    # "role": "assistant"：标识这条消息来自 AI 助手（对应 OpenAI Chat Completions API 的角色格式）。
    # response.choices[0].message.content：从 API 返回对象中取出第一个候选回复的文本内容。
    st.session_state.messages.append({"role": "assistant", "content": full_response})


