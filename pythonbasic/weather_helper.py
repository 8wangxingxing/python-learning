# 导入 requests 包
import requests

# 发送请求
x = requests.get('https://www.baidu.com/')

# 返回 http 的状态码
print(x)
