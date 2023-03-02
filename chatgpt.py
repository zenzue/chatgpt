import openai
import json

openai.api_key = "YOUR_API_KEY"

def generate_response(prompt):
    response = openai.Completion.create(
        engine="davinci",
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.7,
    )

    response_text = response.choices[0].text.strip()

    return response_text

def handle_input():
    user_input = input("> ")

    response = generate_response(user_input)

    print(response)

    handle_input()

def main():
    print("Ask me a question:")
    handle_input()

if __name__ == "__main__":
    main()
