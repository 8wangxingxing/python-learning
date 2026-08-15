import json
import os
import httpx
import requests
from openai import OpenAI

# 模型名（DeepSeek 官方文档里的最新模型）
MODEL = 'deepseek-v4-flash'

# 密钥从环境变量读取
api_key = os.environ.get('DEEPSEEK_API_KEY')
if not api_key:
    print('请先设置密钥：')
    print('$env:DEEPSEEK_API_KEY="sk-你的密钥"')
    exit()

# 直连 DeepSeek，不走代理
http_client = httpx.Client(trust_env=False)
client = OpenAI(
    api_key=api_key,
    base_url='https://api.deepseek.com',
    http_client=http_client,
)


# ===== 工具 1：查天气（你写的 wttr.in 代码）=====
def get_weather(city):
    try:
        # 直连天气网站，不走代理（防止系统里残留的失效代理干扰）
        r = requests.get(
            f'https://wttr.in/{city}?format=j1&lang=zh',
            timeout=15,
            proxies={'http': None, 'https': None},
        )
        if r.status_code != 200:
            return f'{city} 查询失败，请稍后再试'
        data = r.json()
        now = data['current_condition'][0]
        desc = now['weatherDesc'][0]['value']
        temp = now['temp_C']
        humidity = now['humidity']
        return f'{city}当前天气：{desc}，温度{temp}°C，湿度{humidity}%'
    except Exception as error:
        return f'查询出错：{error}'


# ===== 工具清单：告诉 AI 你有哪些工具 =====
tools = [
    {
        'type': 'function',
        'function': {
            'name': 'get_weather',
            'description': '查询一个城市的当前天气',
            'parameters': {
                'type': 'object',
                'properties': {
                    'city': {'type': 'string', 'description': '城市名，如：北京'}
                },
                'required': ['city'],
            },
        },
    }
]


print('=== 带工具的 AI 助手（输入 exit 退出）===')
print('试试问它：今天北京天气怎么样？')

messages = [
    {'role': 'system', 'content': '你是一个友好的助手。当用户问天气时，你必须调用 get_weather 工具来查询。'},
]

while True:
    user_input = input('你：').strip()
    if user_input.lower() == 'exit':
        print('再见！')
        break
    if not user_input:
        continue

    # 把用户的话加入历史
    messages.append({'role': 'user', 'content': user_input})

    # 第一轮：把消息和工具清单发给 AI
    response = client.chat.completions.create(
        model=MODEL,
        messages=messages,
        tools=tools,
    )
    msg = response.choices[0].message
   #print(msg)
    # 如果 AI 想调用工具
    if msg.tool_calls:
        # 把 AI 的完整返回（含 tool_calls 和思考过程 reasoning_content）记进历史
        # DeepSeek 要求：思考过程必须带回，原样带回最稳妥
        messages.append(msg)
        for call in msg.tool_calls:
            print(f'[AI 想调用工具] {call.function.name}，参数：{call.function.arguments}')
            if call.function.name == 'get_weather':
                args = json.loads(call.function.arguments)
                result = get_weather(args['city'])
                print(f'[工具返回] {result}')
                # 把工具结果记进历史
                messages.append({'role': 'tool', 'tool_call_id': call.id, 'content': result})

        # 第二轮：把工具结果发给 AI，让它组织最终回答
        response = client.chat.completions.create(
            model=MODEL,
            messages=messages,
            tools=tools,
        )
        msg = response.choices[0].message

    print('AI：', msg.content)
    messages.append({'role': 'assistant', 'content': msg.content})
