def chat_completion(prompt, model="gpt-4-1106-preview", temperature=0):
  res = client.chat.completions.create(
    model=model,
    messages=[{"role": "user", "content": prompt}],
    temperature=temperature,
)

message = res.choices[0].message.content
print(message)


chat_completion("As Descartes said, I think therefore")
