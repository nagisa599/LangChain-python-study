import langchain
from langchain.chains import LLMChain
from langchain_openai import ChatOpenAI  # 非推奨のインポートを修正
from langchain.prompts import PromptTemplate
from dotenv import load_dotenv
import os
def CHain():
  load_dotenv()  
  langchain.verbose = True

  chat = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0)

  template = """
  次のコマンドの概要を説明してください

  コマンド: {command}
  """
  prompt = PromptTemplate(input_variables=["command"], template=template)
  chain = LLMChain(llm=chat, prompt=prompt)

  # Replace LLMChain with the new RunnableSequence approach
  chain = prompt | chat
    
  # Replace `run` with `invoke`
  result = chain.invoke({"command": "ls -l"})

  print(result)