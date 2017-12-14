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
    # sql_query = """
    # SELECT * FROM film
    # """

    sql_query = """
    SELECT film_id,title
    FROM film
    WHERE film_id IN

    (SELECT inventory.film_id
    FROM rental
    INNER JOIN inventory
    ON inventory.inventory_id = rental.inventory_id
    WHERE return_date BETWEEN '2005-05-29' AND '2005-05-30')

    ORDER BY title
    """

    with get_conn(dbname='dvdrentals', dbuser='chris') as conn:
        df = pd.read_sql(sql_query, conn)

        print(df)
