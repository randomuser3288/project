import torch
#import ollama

#stream = ollama.chat(
 #   model='llama3',
  #  messages=[{'role': 'user', 'content': input('What can I help you with today? ')}],
   # stream=True,
#)

#for chunk in stream:
 # print(chunk['message']['content'], end='', flush=True)
import ollama
with open('datacc.txt', 'r') as file:
    text = file.read()

response = ollama.chat(model='llama3', messages=[
  {
    'role': 'user',
    'content': input('What can I help you with today? '),
    prompt : text
  },
])
print(response['message']['content'])