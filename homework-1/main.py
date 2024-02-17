"""Скрипт для заполнения данными таблиц в БД Postgres."""
import csv

import psycopg2

# connect to db
conn = psycopg2.connect(
    host='localhost',
    database='north',
    user='postgres',
    password='10123000v'
)
try:
    with conn:
        with conn.cursor() as cur:

            with open('north_data/customers_data.csv', 'r') as f:
                reader = csv.reader(f)
                next(reader)  # пропуск заголовка
                for row in reader:
                    cur.execute("INSERT INTO customers_data VALUES (%s, %s, %s)", row)

            with open('north_data/employees_data.csv', 'r') as f:
                reader = csv.reader(f)
                next(reader)  # пропуск заголовка
                for row in reader:
                    cur.execute("INSERT INTO employees_data VALUES (%s, %s, %s, %s, %s, %s)", row)

            with open('north_data/orders_data.csv', 'r') as f:
                reader = csv.reader(f)
                next(reader)  # пропуск заголовка
                for row in reader:
                    cur.execute("INSERT INTO orders_data VALUES (%s, %s, %s, %s, %s)", row)
finally:
    conn.close()
