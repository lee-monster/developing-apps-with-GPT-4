# 레디스 클라이언트

class DataService():
  def __init__(self):
  # 레디스 연결
  self.redis_client = redis.Redis(
    host=REDIS_HOST,
    port=REDIS_PORT,
    password=REDIS_PASSWORD
    )


def pdf_to_embeddings(self, pdf_path: str, chunk_length: int = 1000):
# PDF 파일에서 데이터를 읽고 여러 부분으로 분할
reader = PdfReader(pdf_path)
chunks = []
for page in reader.pages:
text_page = page.extract_text()
chunks.extend([text_page[i:i+chunk_length]
for i in range(0, len(text_page), chunk_length)])
# 임베딩 생성
response = client.embeddings.create(model='text-embedding-ada-002',
input=chunks)
return [{'id': value['index'],
'vector':value['embedding'],
'text':chunks[value['index']]} for value in response['choices']]



def load_data_to_redis(self, embeddings):
  for embedding in embeddings:
      key = f"{PREFIX}:{str(embedding['id'])}"
      embedding["vector"] = np.array(
          embedding["vector"], dtype=np.float32).tobytes()
      self.redis_client.hset(key, mapping=embedding)


def search_redis(self,user_query: str):
# 사용자 쿼리에서 임베딩 벡터 생성
embedded_query = client.embeddings.create(
  input=user_query,
  model="text-embedding-ada-002")["data"][0]['embedding']

# 벡터 검색 수행
results = self.redis_client.ft(index_name).search(query, params_dict)
return [doc['text'] for doc in results.docs]



# 의도 분류
class IntentService():
  def __init__(self):
    pass
  def get_intent(self, user_question: str):
      # 오픈AI 채팅 완성 엔드포인트 호출
      response = client.chat.completions.create(
          model="gpt-3.5-turbo",
          messages=[
              {"role": "user",
               "content": f"""Extract the keywords from the following
                question: {user_question}."""}
          ]
      )
      # 응답 추출
      return (response.choices[0].message.content)


# 답변 생성
class ResponseService():
  def __init__(self):
    pass
  def generate_response(self, facts, user_question):
      # 오픈AI 채팅 완성 엔드포인트 호출
      response = client.chat.completions.create(
          model="gpt-3.5-turbo",
          messages=[
                {"role": "user",
                 "content": f"""Based on the FACTS, answer the QUESTION.
                  QUESTION: {user_question}. FACTS: {facts}"""}
          ]
      )
      # 응답 추출
      return (response.choices[0].message.content)


def run(question: str, file: str='ExplorersGuide.pdf'):
    data_service = DataService()
    data = data_service.pdf_to_embeddings(file)
    data_service.load_data_to_redis(data)

intent_service = IntentService()
intents = intent_service.get_intent(question)

facts = service.search_redis(intents)

return response_service.generate_response(facts, question)
