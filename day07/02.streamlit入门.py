#Streamlit是一个用于快速基于Python代码构建web网页的python库（数据科学及机器学习领域）
import streamlit as st
#设置页面的配置项
st.set_page_config(
    page_title="streamlit入门",
    page_icon="🧊",
    #布局
    layout="wide",
    #控制的是测量边栏的状态
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': 'https://www.extremelycoolapp.com/help',
        'Report a bug': "https://www.extremelycoolapp.com/bug",
        'About': "# This is a header. This is an *extremely* cool app!"
    }
)
#大标题
st.title("Streamlit,入门演示")
st.header("Streamlit,一级标题")
st.subheader("Streamlit,二级标题")
#段落文字
st.write("金毛寻回犬，大家亲切地叫它“金毛”，是犬界公认的“大暖男”。它体格匀称，披着一身浓密防水的金黄色被毛，阳光下闪闪发亮，配上永远上扬的嘴角和摇个不停的尾巴，看起来憨厚又温柔。")
st.write("性格上，金毛聪明、耐心、亲和力满分，对人几乎没脾气，对小孩尤其包容，是出了名的家庭伴侣犬。它也很爱玩水、爱捡球，精力旺盛但不神经质，每天需要足够的运动量和陪伴。智商在犬种里排前列，训练起来省心，不过幼犬期也会“拆家”捣乱，得有点耐心。")
st.write("养护方面，金毛掉毛量感人，尤其换毛季家里像下雪，需要勤梳毛；耳朵下垂容易藏污纳垢，要定期清理。它们容易发胖，喂食得控制量，还要留意髋关节和皮肤问题。总的来说，金毛是那种“你对它好，它就掏心掏肺对你”的狗，适合愿意花时间陪伴、不介意掉毛的家庭。")

#图片
st.image("./resources/dog.jpg")

#音频
st.audio("resources/music.mp3")

#视频
st.video("resources/news.mp4")

#表格
student_data = {
    "姓名":["王林","李慕婉","贝罗","张三","李四"],
    "学号":["0001","0002","0003","0004","0005"],
    "语文":[98,90,59,29,80],
    "数学":[88,78,65,70,39],
    "英语":[99,89,87,59,62],
    "总分":[285,257,211,158,181]
}
st.table(student_data)

#输入框
name = st.text_input("请输入姓名")
st.write(f"您的姓名是：{name}")

password = st.text_input("请输入密码",type = "password")
st.write(f"您的密码是：{password}")

#单选按钮
gender = st.radio("请输入您的性别",["男","女","未知"],index = 2)
st.write(gender)