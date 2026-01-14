import psycopg2
from config import DB_CONFIG

conn = psycopg2.connect(**DB_CONFIG)
conn.autocommit = True

def q(sql, params=(), fetch=False):
    with conn.cursor() as cur:
        cur.execute(sql, params)
        if fetch:
            return cur.fetchall()
