import os
import openai
openai.api_key = os.getenv("OPENAI_API_KEY")

response = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[
        {"role": "system", "content": "You are a formal turkish translator"},
        {"role": "user", "content": "Hi its Ali and welcome to my chat."},
        {"role": "assistant", "content": "Selam ben Ali benim sohbetime hosgeldiniz."},
        {"role": "user", "content": "so today we are going to talk about turkey's economy in the last couple years."}
    ]
)

print(response.get('choices')[0].message.content)
print(response.get('usage').get('total_tokens'))
