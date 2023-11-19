from langchain.chains.sequential import SequentialChain
from langchain.llms import OpenAI
from langchain.chains import LLMChain, SequentialChain
from langchain.prompts import PromptTemplate
from secret_key import openapi_key
import os
os.environ['OPENAI_API_KEY']=openapi_key
llm=OpenAI(temperature=0.7) 

def generate_store_items(Stored):
  prompt_template_name=PromptTemplate(
    input_variables=['Store'],
    template="I want to have {Store} store, give me a good name for this"
  )
  chain=LLMChain(llm=llm,prompt=prompt_template_name,output_key="Store_name")
  prompt_template_items=PromptTemplate(
    input_variables=['Store_name'],
    template="""List me all the models available in {Store_name}. Return them in point wise properly"""
  )
  items=LLMChain(llm=llm,prompt=prompt_template_items,output_key="Item_name")
  chain4=SequentialChain(
    chains=[chain,items],
    input_variables=['Store'],
    output_variables=['Store_name','Item_name']
  )
  response=chain4({'Store':Stored})
  return response
if __name__ == "__main__":
  print(generate_store_items("Apple Store"))
