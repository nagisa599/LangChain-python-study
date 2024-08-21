# llm_wrapper.py
from dotenv import load_dotenv
import os
## LLMsを使うときは, OpenAIをインポート
from langchain_openai import OpenAI  # 非推奨のインポートを修正

def load_model():
    load_dotenv()  
    llm = OpenAI(model_name="gpt-3.5-turbo-instruct", temperature=0)
    return llm


def get_prediction(prompt):
    llm = load_model()
    result = llm.invoke(prompt)  # 非推奨の`predict`を`invoke`に置き換え
    return result