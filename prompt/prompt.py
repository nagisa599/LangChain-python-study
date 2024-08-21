from langchain.prompts import PromptTemplate

def create_prompt(command: str) -> str:
    template = """
    次のコマンドの概要を説明してください

    コマンド: {command}
    """
    prompt = PromptTemplate(input_variables=["command"], template=template)
    return prompt.format(command=command)