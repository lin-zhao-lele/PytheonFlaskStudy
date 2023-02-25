import requests

# 构造 API 请求信息
url = "https://api.openai.com/v1/completions"
headers = {
    "Content-Type": "application/json",
    "Authorization": "Bearer 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"
}
data = {
    "model": "text-davinci-003",
    "prompt": "什么是chatGPT？",
    "temperature": 0,
    "max_tokens": 1000
}

# 发送 API 请求并处理响应
response = requests.post(url, headers=headers, json=data)
if response.status_code == 200:
    result = response.json()["choices"][0]["text"]
    print(result)
else:
    print("API 请求失败！")