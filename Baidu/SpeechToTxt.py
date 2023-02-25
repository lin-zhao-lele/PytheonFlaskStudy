from aip import AipSpeech

APP_ID = 'your_app_id'
API_KEY = 'your_api_key'
SECRET_KEY = 'your_secret_key'

client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)

# 语音文件路径
speech_file = 'file.wav'

# 读取语音文件的二进制内容
with open(speech_file, 'rb') as f:
    speech_data = f.read()

# 识别结果
result = client.asr(speech_data, 'wav', 16000, {
    'dev_pid': 1536,
})

print(result)