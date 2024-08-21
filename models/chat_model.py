from dotenv import load_dotenv
import os
# chatModelを利用するときは, ChatOpenAIをインポート
from langchain_openai import ChatOpenAI  # 非推奨のインポートを修正

def load_chat_model():
    load_dotenv()  
    chat = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0)
    return chat


def chat_get_prediction(prompt):
    chat = load_chat_model()
    messages = [{"role": "user", "content": prompt}]
    # invokeメソッドでチャット補完を実行
    result = chat.invoke(messages)
    return result