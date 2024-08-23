import langchain
from langchain.chains import SimpleSequentialChain
from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate
from dotenv import load_dotenv
import os

def SimpleChain():
    load_dotenv()  
    langchain.verbose = True

    chat = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0)

    con_template = """
    以下の質問に答えてください

    ### 質問 ###
    {question}
    ### 回答 ###

    ステップバイステップで考えてください
    """
    prompt = PromptTemplate(input_variables=["question"], template=con_template)
    con_chain = prompt | chat  # Use the new RunnableSequence approach

    summary_template = """
    入力を結論だけ一言で要約してください

    ### 入力 ###
    {input}
    ### 入力終了 ###
    """
    summary_prompt = PromptTemplate(input_variables=["input"], template=summary_template)
    complate_chain = con_chain | summary_prompt | chat  # Combine chains using the RunnableSequence approach

    result = complate_chain.invoke({"question": "私は市場に行って10個リンゴを買いました。隣人は2つ、修理工に2つを渡しました。そりから5つリングを買って1つ食べました。残りは何個ですか?"})

    print(result)



