import os
import httpx
from openai import OpenAI

# 模型名（DeepSeek 官方文档里的最新模型，如果报模型错误就去官网确认）
MODEL = 'deepseek-v4-flash'

# 密钥从环境变量读取，不写死在代码里（防止传到 GitHub 泄露）
api_key = os.environ.get('DEEPSEEK_API_KEY')
if not api_key:
    print('请先设置密钥，再运行本程序：')
    print('$env:DEEPSEEK_API_KEY="sk-你的密钥"')
    exit()

# 连接 DeepSeek（OpenAI 兼容接口）
# trust_env=False：不让程序走系统代理，直连 DeepSeek
http_client = httpx.Client(trust_env=False)
client = OpenAI(
    api_key=api_key,
    base_url='https://api.deepseek.com',
    http_client=http_client,
)

# 对话历史，第一句是给 AI 定的身份
messages = [
    {'role': 'system', 'content': '你是一个友好的中文学习助手，回答要简洁清楚。'},
]

print('=== 聊天机器人（输入 exit 退出）===')
while True:
    user_input = input('你：').strip()
    if user_input.lower() == 'exit':
        print('再见！')
        break
    if not user_input:
        continue

    # 把用户的话加入历史
    messages.append({'role': 'user', 'content': user_input})

    # 把完整历史发给 AI
    response = client.chat.completions.create(
        model=MODEL,
        messages=messages,
    )
    # print(response)
    # print(response.choices[0])
    # print(response.choices[0].message)
    # print(response.choices[0].message.content)
    answer = response.choices[0].message.content

    print('AI：', answer)

    # 把 AI 的回答也加入历史（下次才能记住上下文）
    messages.append({'role': 'assistant', 'content': answer})
