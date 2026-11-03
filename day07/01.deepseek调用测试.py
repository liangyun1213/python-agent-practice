import os
import httpx2
from openai import OpenAI
http_client = httpx2.Client(
    headers={"Accept-Encoding": "gzip, deflate"}
)
#创建与AI大模型交互的客户端对象（DEEPSEEK_API_KEY 环境变量的名字，值就是DeepSeek的API_KEYd
client = OpenAI(
    api_key=os.environ.get('DEEPSEEK_API_KEY'),
    base_url="https://api.deepseek.com",
    http_client=http_client,#传入自定义客户端
)
#与AI大模型进行交互
response = client.chat.completions.create(
    model="deepseek-flash",
    messages=[
        {"role": "system", "content": "你是一个非常可爱的AI助理，你的名字叫果冻，请你使用可爱俏皮的语气回答用户的问题"},
        {"role": "user", "content": "你是谁，你能帮我做什么？"},
    ],
    stream=False,
    reasoning_effort="high",
    extra_body={"thinking": {"type": "enabled"}},
)
import sys
print(sys.executable)
#输出大模型返回的结果
print(response.choices[0].message.content)