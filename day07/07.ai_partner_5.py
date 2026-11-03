import streamlit as st
import os
import httpx2
from openai import OpenAI
import datetime
import json
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

#生成会话标识函数
def generate_session_name():
    return datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")


#保存会话信息函数
def save_session():
    if st.session_state.current_session:
        # 构建新的会话对象
        session_data = {
            "nick_name": st.session_state.nick_name,
            "nature": st.session_state.nature,
            "current_session": st.session_state.current_session,
            "messages": st.session_state.messages
        }
        # 如果session目录不存在，则创建
        if not os.path.exists("session"):
            os.mkdir("session")

            # 保存会话信息
        with open(f"session/{st.session_state.current_session}.json", "w", encoding="utf-8") as f:
            json.dump(session_data, f, ensure_ascii=False, indent=4)

#加载所有的会话列表信息
def load_sessions():
    session_list = []
    #加载sessions目录下的文件
    if os.path.exists("session"):
        file_list = os.listdir("session")
        for filename in file_list:
            if filename.endswith(".json"):
                session_list.append(filename[:-5])
    session_list.sort(reverse=True)
    return session_list

#加载指定会话信息函数
def load_session(session_name):
    try:
        if os.path.exists(f"session/{session_name}.json"):
            # 读取会话数据
            with open(f"session/{session_name}.json", "r", encoding="utf-8") as f:
                session_data = json.load(f)
                st.session_state.nick_name = session_data["nick_name"]
                st.session_state.nature = session_data["nature"]
                st.session_state.current_session = session_data["current_session"]
                st.session_state.messages = session_data["messages"]
    except Exception:
        st.error("加载会话失败")

#删除会话信息函数
def deltte_session(session_name):
    try:
        if os.path.exists(f"session/{session_name}.json"):
            os.remove(f"session/{session_name}.json")
            #r如果删除的是当前会话，则需要更新消息列表
            if session_name == st.session_state.current_session:
                st.session_state.messages = []
                st.session_state.current_session = generate_session_name()
    except Exception:
        st.error("删除会话失败")


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
#昵称
if "nick_name" not in st.session_state:
    st.session_state.nick_name = "小琴"
#性格
if "nature" not in st.session_state:
    st.session_state.nature = "活泼俏皮开朗的四川姑娘"
#会话标识
if "current_session" not in st.session_state:
    #获取当前时间
    st.session_state.current_session = generate_session_name()

#展示聊天信息
st.text(f"会话名称：{st.session_state.current_session}")
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

#左侧的侧边栏 - with：streamlit中上下文管理器
with st.sidebar:
    #会话信息
    st.subheader("AI控制面板")
    #新建会话
    if st.button("新建会话",width = "stretch",icon = "✒️"):
        #1.保存当前会话信息
        save_session()
        #2.创建新的会话
        if st.session_state.current_session:#如果聊天信息非空，True；否则，False
            st.session_state.messages = []
            st.session_state.current_session = generate_session_name()
            save_session()
            st.rerun()  # 重新运行页面
    #会话历史
    st.text("会话历史")
    session_list = load_sessions()
    for session in session_list:
        col1,col2 = st.columns([4,1])#columns：创建若干列
        with col1:
            #加载会话信息
            #三元运算符：如果条件为真，则返回第一个表达式的值；否则，返回第二个表达式的值------->语法：值1 if 条件 else 值2
            if st.button(session,width = "stretch",icon="📄",key=f"load_{session}",type="primary" if session == st.session_state.current_session else "secondary"):
                load_session(session)
                st.rerun()

        with col2:
            #删除会话信息
            if st.button("",width = "stretch",icon="❌️",key=f"delete_{session}"):
                deltte_session(session)
                st.rerun()


    #分割线
    st.divider()

    #伴侣信息
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
    #保存大模型返回的结果
    st.session_state.messages.append({"role": "assistant", "content": full_response})
    #保存会话信息
    save_session()


