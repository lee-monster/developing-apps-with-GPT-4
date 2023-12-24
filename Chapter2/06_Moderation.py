from openai import OpenAI
client = OpenAI(api_key='OpenAI_API_KEY')

# 오픈AI의 모더레이션 엔드포인트를 호출하고
# 자동 업데이트되는 text-moderation-latest 모델을 사용

response = client.moderations.create(
  model="text-moderation-latest",
  input="I want to kill my neighbor.",
)

output = response.results[0]
print(output)
