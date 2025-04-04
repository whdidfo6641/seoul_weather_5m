# 5분마다 한 번씩 서울의 기온 정보를 csv 형태로 저장
import requests
import csv
from datetime import datetime
import os

MY_API_KEY = os.getenv('OPENWEATHER_API_KEY')
CITY = 'Seoul'
URL = f"https://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={MY_API_KEY}&units=metric"

response = requests.get(URL)

data = response.json()
# 서울 기온
temp = data['main']['temp']
time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

csv_filename = 'seoul_weather.csv'
header = ['time','temp']

# csv 새로 생성, 있으면 갱신
file_exist = os.path.isfile(csv_filename) # 해당 경로에 파일 존재 여부 확인

# a mode: 없으면 write, 있으면 쓰기 모드로 불러오기
# w mode: 무조건 덮어쓰기
with open(csv_filename, 'a', newline='') as file:
    writer = csv.writer(file)

    #만약 csv 없다면 -> 헤더도 없다
    if not file_exist:
        writer.writerow(header)

    writer.writerow([time,temp])

    print('서울 기온 저장 완료')
