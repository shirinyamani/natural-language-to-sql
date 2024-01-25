import os

from openai import OpenAI


api_key = os.environ.get('openai_api_key')


def create_table_definiton_for_gpt(df, table_name):
    prompt = f"""### sqlite table definition
    #
    # {table_name}({','.join(str(col) for col in df.columns)})
    # 
    """
    return prompt


def user_input():
    user_input = input("Enter your query: ")
    return user_input


def combine_prompts(fixed_prompt, user_query):
    final_user_input = f'### A query to answer: {user_query}\nSELECT'
    return fixed_prompt + final_user_input

def send_to_openai(prompt):
    response = OpenAI(api_key=api_key).complete(
        model="davinci",
        prompt=prompt,
        max_tokens=100,
        temperature=0,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.0,
        stop=["###", ";"]
    )
    return response