from datasets import load_dataset
import json

from openai_service import get_chat_completion
from prompts import *

dataset = load_dataset("allenai/ai2_arc", "ARC-Challenge")
df = dataset['train'].to_pandas()

print(df.head())

def build_prompt_for_sample(id, df):
    question = df.iloc[id].question
    choices = df.iloc[id].choices
    options = choices['text']
    return concept_guided_reasoning_prompt.format(question=question, options=options)

print(build_prompt_for_sample(0, df))


