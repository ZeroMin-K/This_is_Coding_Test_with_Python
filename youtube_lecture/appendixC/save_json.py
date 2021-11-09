import json

# 사전 자료형(dict) 데이터 선언
user = {
    'id' : 'gildong', 
    'password' : '1!2@##4$',
    'age': 30,
    'hobby':['footboall', 'programming']
}

# JSON데이터로 변환하여 파일 저장
with open('user.json', 'w', encoding = 'utf-8') as file:
    json_data = json.dump(user, file, indent = 4) 
