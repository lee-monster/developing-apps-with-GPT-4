# 함수 예시
def find_product(sql_query):
  # 쿼리 실행
  results = [
    {"name": "pen", "color": "blue", "price": 1.99},
    {"name": "pen", "color": "red", "price": 1.78},
  ]
  return results


# 함수 정의
functions = [
  {
    "name": "find_product",
    "description": "Get a list of products from a sql query",
    "parameters": {
      "type": "object",
      "properties": {
        "sql_query": {
          "type": "string",
          "description": "A SQL query",
        }
      },
      "required": ["sql_query"],
    },
  }
]


# 예시 질문
user_question = "I need the top 2 products where the price is less than 2.00"
messages = [{"role": "user", "content": user_question}]

# client.chat.completions 엔드포인트를 함수 정의를 사용해 호출
response = client.chat.completions.create(
  model="gpt-3.5-turbo-0613", messages=messages, functions=functions
)

response_message = response["choices"][0]["message"]
messages.append(response_message)


# 함수를 호출
{
  "role": "assistant",
  "content": null,
  "function_call": {
    "name": "find_product",
    "arguments": "{\n \"sql_query\": \"SELECT * FROM products WHERE price < 2.00
    LIMIT 2\"\n}"
    }



import json

# 함수 호출
function_args = json.loads(
  response_message.function_call.arguments
)

products = find_product(function_args.get("sql_query"))
# 함수의 응답을 메시지에 추가
messages.append(
{
  "role": "function",
  "name": "function_name",
  "content": json.dumps(products)
  }
)

# 함수의 응답 호출
response = client.chat.completions.create(
  model="gpt-3.5-turbo-1106",
  messages=messages
)

# 결과 출력
print(response.choices[0].message.content)

  
