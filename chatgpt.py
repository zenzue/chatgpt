import openai
openai.api_key = "YOUR_API_KEY"

def ask_gpt(question):
    model_engine = "davinci" # You can try other engines as well
    response = openai.Completion.create(
      engine=model_engine,
      prompt=question,
      max_tokens=1024,
      n=1,
      stop=None,
      temperature=0.5,
    )

    answer = response.choices[0].text.strip()
    return answer

while True:
    question = input("Ask me a question: ")
    answer = ask_gpt(question)
    print(answer)

