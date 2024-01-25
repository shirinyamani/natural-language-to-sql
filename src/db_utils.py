from sqlalchemy import create_engine, text



def dataframe_to_database(df, table_name):
    engine = create_engine(f'sqlite:///:memory:', echo=False)
    df.to_sql(table_name, con=engine, if_exists='replace', index=False)
    return engine

def handle_api_query_response(response):
    query = response["choices"][0]["text"]
    if query.startswith(" "):
        query = "SELECT"+query
    return query
    

def execute_sql_query(query, engine):
    with engine.connect() as conn:
        result = conn.execute(text(query))
        return result.fetchall()
