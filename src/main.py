import os

import openai
import pandas as pd

from src import api_utils, db_utils


api_key = os.environ.get('openai_api_key')


if __name__ == '__main__':
    print("Welcome to the SQL Query Generator!")
    df = pd.read_csv("data/sales_data.csv")
    print(f'data fromat {df.shape}')

    print("Creating table definition for GPT...")
    database = db_utils.dataframe_to_database(df, "Sales")

    fixed_prompt = api_utils.create_table_definiton_for_gpt(df, "Sales")
    print(f'fixed_prompt {fixed_prompt}')

    print("waiting for user input...")
    user_input = api_utils.user_input()
    final_prompt = api_utils.combine_prompts(fixed_prompt, user_input)
    print(f'final_prompt {final_prompt}')

    print("Sending to OpenAI...")
    response = api_utils.send_to_openai(final_prompt)
    proposed_query = response["choices"][0]["text"]
    proposed_query_postprocessed = db_utils.handle_api_query_response(response)
    print(f'proposed_query {proposed_query_postprocessed}')
    result = db_utils.execute_sql_query(database, proposed_query_postprocessed)
    print(f'result: {result}')
