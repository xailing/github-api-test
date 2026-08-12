import requests

# 发送 GET 请求
response = requests.get("https://api.github.com/users/octocat")

# 打印状态码
print("状态码:", response.status_code)

# 打印返回的 JSON 数据（格式化显示）
print("返回的 JSON 数据:")
print(response.json())