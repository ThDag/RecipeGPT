import os
import openai
openai.api_key = os.getenv("OPENAI_API_KEY")

response = openai.Image.create_edit(
  image=open("grainy_photo.jpg", "rb"),
  prompt="remove the grain from the photo ",
  n=1,
  size="1024x1024"
)

with open('response.txt', 'w') as file:
    file.write(response)

image_url = response['data'][0]['url']
print(image_url)