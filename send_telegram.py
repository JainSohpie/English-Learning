import json
import os
import requests
from datetime import datetime

# 환경 변수에서 토큰 가져오기
TOKEN = os.environ.get('TELEGRAM_TOKEN')
CHAT_ID = os.environ.get('TELEGRAM_CHAT_ID')

# words.json 읽기
with open('words.json', 'r', encoding='utf-8') as f:
    vocabulary = json.load(f)

# 상위 10개 단어 선택
words = vocabulary[:10]

# 메시지 생성
today = datetime.now().strftime('%Y년 %m월 %d일')
message = f'📚 <b>{today} 영어 학습</b>\n\n'

for i, word in enumerate(words, 1):
    korean = word.get('korean', '')
    english = word.get('english', '')
    example = word.get('example', '')
    
    message += f'<b>{i}. {korean}</b>\n'
    message += f'   ➤ {english}\n'
    message += f'   📝 <i>{example}</i>\n\n'

message += '━━━━━━━━━━━━━━━━\n💡 오늘도 화이팅! 🚀'

# 텔레그램 전송
url = f'https://api.telegram.org/bot{TOKEN}/sendMessage'
payload = {
    'chat_id': CHAT_ID,
    'text': message,
    'parse_mode': 'HTML'
}

response = requests.post(url, json=payload)

if response.status_code == 200:
    print('✅ 텔레그램 전송 성공!')
else:
    print(f'❌ 전송 실패: {response.text}')
    exit(1)
