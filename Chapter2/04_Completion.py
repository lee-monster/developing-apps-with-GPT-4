# 오픈AI 함수 호출, 코드 실행에는 API 키를 내장한 client의 사전 정의가 필요
response = client.completions.create(
  model="text-davinci-003", prompt="Hello World!"
)

# 결과 출력
print(response.choices[0].text)
