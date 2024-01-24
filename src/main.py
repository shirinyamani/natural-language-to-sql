from openai import OpenAI
import os


api_key = os.environ['openapi_key']
client = OpenAI(api_key=api_key)


#print(completion.choices[0].text)


if __name__ == '__main__':
    completion = client.completions.create(model='davinci-002',
                                       prompt="gimme one reason to learn how to work with openai api",
                                       max_tokens=40)