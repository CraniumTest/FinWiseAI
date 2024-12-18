import pandas as pd
from sqlalchemy import create_engine

def fetch_user_data(user_id: int, db_uri: str) -> pd.DataFrame:
    engine = create_engine(db_uri)
    query = f"SELECT * FROM users_data WHERE user_id = {user_id}"
    data = pd.read_sql(query, engine)
    engine.dispose()
    return data
