from openai import OpenAI
from constants import *

client = OpenAI(
	organization='org-jMOPflbQO9AjlzM6dyINmTkw',
	api_key=OPENAI_API_KEY
)

def get_chat_completion(prompt, model="gpt-3.5-turbo"):  
	response = client.chat.completions.create(
		model=model, # "gpt-4-0125-preview", # 
		messages=[
			{"role": "system", "content": "You are a helpful assistant."},
			{"role": "user", "content": prompt},
			# {"role": "assistant", "content": "The Los Angeles Dodgers won the World Series in 2020."},
			# {"role": "user", "content": "Where was it played?"}
		]
	)

	# Returning the extracted response
	text_response = response.choices[0].message.content
	prompt_tokens, completion_tokens, total_tokens = response.usage.prompt_tokens, response.usage.completion_tokens, response.usage.total_tokens
	return text_response, prompt_tokens, completion_tokens, total_tokens