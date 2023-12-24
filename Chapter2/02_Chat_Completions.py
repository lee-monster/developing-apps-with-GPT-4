# 2.5장 GPT-4와 ChatGPT 사용하기


from openai import OpenAI
client = OpenAI(api_key='OpenAI_API_KEY')

# GPT-3.5 터보 모델 지정 및 채팅 완성 기능 호출
response = client.chat.completions.create(

  # 모델 설정
  model="gpt-3.5-turbo", #모델별로 비용이 다르며, 많은 예제가 합리적인 gpt-3.5-turbo로 작성되었습니다. 아래 코드에 gpt-4-1106-preview 모델을 적용하여도 동일하게 작동됩니다

  # 대화 메시지 목록 설정

  messages=[

    {
      "role": "system",
      "content": "You are a helpful teacher."
    },
    {
      "role": "user",
      "content": "Are there other measures than time complexity for an \
      algorithm?",
    },
    {
      "role": "assistant",
      "content": "Yes, there are other measures besides time complexity \
      for an algorithm, such as space complexity.",
    },
    {
      "role": "user",
      "content": "What is it?",
    },
  ]
)
