import os
import openai
openai.api_key = os.getenv("OPENAI_API_KEY")

Prompt = ('You will give a tasty cooking recipe with steps '
          'and explain it short. Only using the simple household ingredients '
          'and given ingredient from [START] to [END].\n[START]\n ')

test_prompt = 'say this is test'

ingredients = input('ingredients you have (must seperate with comma ",") :').replace(',', '\n').encode().decode('unicode_escape')
print(ingredients)

Prompt += ingredients + '\n[END]'

print(Prompt)

response = openai.Completion.create(
  model="text-curie-001",
  prompt=Prompt,
  max_tokens=130,
  temperature=0.2
)

print(response.choices[0].text.encode().decode('unicode_escape'))

with open('response.txt', 'a') as file:
    for i in list(dict(response).values()):
        file.write(str(i))


