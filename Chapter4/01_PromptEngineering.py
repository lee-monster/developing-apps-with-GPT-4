def chat_completion(prompt, model="gpt-4-1106-preview", temperature=0):
  res = client.chat.completions.create(
    model=model,
    messages=[{"role": "user", "content": prompt}],
    temperature=temperature,
)

message = res.choices[0].message.content
print(message)


chat_completion("As Descartes said, I think therefore")


##Context, task and role

chat_completion("Give me a suggestion for the main course for today's lunch.")

prompt = """
Context: I do 2 hours of sport a day. I am vegetarian, and I don't like green
vegetables. I am conscientious about eating healthily.
Task: Give me a suggestion for a main course for today's lunch.
"""
chat_completion(prompt)


prompt = """
Context: I do 2 hours of sport a day. I am vegetarian and I don't like green
vegetables. I am very careful to eat healthily.
Task: Give me a suggestion for a main course for today's lunch?
Do not perform the requested task! Instead, can you ask me questions about the context
so that when I answer, you can perform the requested task more efficiently?
"""
chat_completion(prompt)
