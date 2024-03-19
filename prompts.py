concept_guided_reasoning_prompt = """Question: - {question}
Options: - {options}

All the main real world concepts essential to answer the question are: 
List them down along with one line description
Remember to return the response in a json structure as defined below - 

"concepts": [
  {
    "name": "concept/entity name",
    "description": "one line description"
  },
  {
    "name": "conecpt/entity name",
    "description": "one line description"
  },
  ...
]

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

Provide the answer to the original [Question] from the [Options] and the reasoning for it based on the concepts/entities and their relationships you have identified - 
Remember to follow the following json structure - 
{
  "answer": "your answer",
  "reasoning": "your reasoning"
}
[your answer]
"""


concept_guided_reasoning_prompt_without_options = concept_guided_reasoning_prompt = """Question: - {question}

All the main real world concepts essential to answer the question are: 
List them down along with one line description
Remember to return the response in a json structure as defined below - 

"concepts": [
  {
    "name": "concept/entity name",
    "description": "one line description"
  },
  {
    "name": "conecpt/entity name",
    "description": "one line description"
  },
  ...
]

[your concepts list]

In manner of ontology, describe the relationship for each concept or entity to the other concepts/entities in the context of the question in a structured manner along with one line description for each:
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

Provide the answer to the original question given below and the reasoning for it based on the concepts/entities and their relationships you have identified - 
Question: {question}

Remember to follow the following json structure - 
{
  "answer": "your answer",
  "reasoning": "your reasoning"
}
[your answer]
"""