import langchain
from langchain.chains import LLMChain
from langchain_openai import ChatOpenAI  # 非推奨のインポートを修正
from langchain.prompts import PromptTemplate
from pydantic import BaseModel, Field
from typing import List
from langchain.output_parsers import PydanticOutputParser
from dotenv import load_dotenv
def OutPutParserTest():
  load_dotenv()  
  langchain.verbose = True

  chat = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0)

  class Recipe(BaseModel):
    ingredients:List[str] = Field(description="ingredients of the dish")
    steps:List[str] =  Field(description="steps to prepare the dish")

  template = """料理の材料と手順を教えてください。

  {format_instructions}

  料理名: {dish}
  """

  parser = PydanticOutputParser(pydantic_object=Recipe)
  prompt = PromptTemplate(
    template=template,
    input_variables={"dish"}, 
    partial_variables={"format_instructions": parser.get_format_instructions()}
  )
  chain = LLMChain(llm=chat, prompt=prompt)
  result = chain.invoke({"dish": "チキンカレー"})
  print(result)

    