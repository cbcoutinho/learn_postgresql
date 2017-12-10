import pandas as pd
import psycopg2

def get_conn(dbname=None, dbuser=None, dbpass=None):
    try:
        conn = psycopg2.connect(dbname=dbname,
                                user=dbuser,
                                password=dbpass)

    except psycopg2.Error as e:
        print(e.pgerror)

    except Exception as e:
        print(e)
        return None

    return conn

if __name__ == '__main__':
    with get_conn(dbname='dvdrentals', dbuser='chris') as conn:
        df = pd.read_sql('select * from film', conn)

        print(df)
