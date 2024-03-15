from openai import OpenAI
from constants import *

client = OpenAI(
  organization='org-jMOPflbQO9AjlzM6dyINmTkw',
  api_key=OPENAI_API_KEY
)

def get_chat_completion(prompt, model="gpt-3.5-turbo"):
  
   # Creating a message as required by the API
   messages = [{"role": "user", "content": prompt}]
  
   # Calling the ChatCompletion API
   response = client.ChatCompletion.create(
       model=model,
       messages=messages,
       temperature=0,
   )

   # Returning the extracted response
   return response.choices[0].message["content"]

# response = get_chat_completion("Translate into Spanish: As a beginner data scientist, I'm excited to learn about OpenAI API!")

# print(response)


response = client.chat.completions.create(
  model="gpt-4-0125-preview", # "gpt-3.5-turbo"
  messages=[
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": """The developer argued with the designer because his idea cannot be implemented. [question]Who does "his" refer to in the sentence?

All the main real world concepts essential to answer the question are: 
List them down along with one line description
Remember to return the response in a json structure as defined below - 

{
  "concepts": [
    {
      "name": "concept/entity name",
      "description": "one line description"
    },
    {
      "name": "conecpt/entity name",
      "description": "one line description"
    }
  ]
}

[your concepts list]

In manner of ontology, describe the relationship for each concept to the other concepts in the context of the sentence in a structured manner along with one line description for each are:
Remember to return the response in a json structure as defined below -

"relationships": [
	{
		"concept": "concept1",
		"relationship": "relation",
		"related_concept": "concept2",
		"description": "one line description"
	},
	{
		"concept": "concept2",
		"relationship": "relation",
		"related_concept": "concept3",
		"description": "one line description"
	},
	....
]
 
[your relationship list]

Provide the answer to the original [question] and the reasoning for it based on the concepts/entities and their relationships you have identified - 
Remember to follow the following json structure - 
{
  "answer": "your answer",
  "reasoning": "your reasoning"
}
[your answer]"""},
    # {"role": "assistant", "content": "The Los Angeles Dodgers won the World Series in 2020."},
    # {"role": "user", "content": "Where was it played?"}
  ]
)

print(response.choices[0].message.content)

print(response)