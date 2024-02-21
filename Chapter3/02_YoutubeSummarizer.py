# 파일에서 스크립트 읽기(파일 경로는 사용자의 환경설정에 따라 다를 수 있으니, 정확한 경로를 먼저 확인하시기 바랍니다.)
with open("transcript.txt", "r") as f:
  transcript = f.read()


# 오픈AI의 채팅 완성 엔드포인트 호출, GPT-4 모델 사용
response = client.chat.completions.create(
  model="gpt-4-1106-preview",
  messages=[
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "Summarize the following text"},
    {"role": "assistant", "content": "Yes."},
    {"role": "user", "content": transcript}
  ],
)

# 결과 출력
print(response.choices[0].message.content)
