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


prompt = """
Context: I do 2 hours of sport a day. I am vegetarian, and I don't like green
vegetables. I am conscientious about eating healthily.
Task: Give me a suggestion for a main course for today's lunch. With this suggestion, I
also want a table with two columns where each row contains an ingredient from the main
course. The first column in the table is the name of the ingredient. The second column
of the table is the number of grams of that ingredient needed for one person. Do not
give the recipe for preparing the main course.
"""
chat_completion(prompt)


## Thinking Step by Step

prompt = "How much is 369 * 1235?"
chat_completion(prompt)

prompt = "How much is 369 * 1235 ? Let's think step by step."
chat_completion(prompt)



## Few Shot Learning

prompt = """
I go home --> 😊 go 🏠
my dog is sad --> my 🐶 is 😞
I run fast --> 😊 run ⚡
I love my wife --> 😊 ❤️ my wife
the girl plays with the ball --> the 👧 🎮 with the 🏀
The boy writes a letter to a girl --> 
"""
chat_completion(prompt)
