import psycopg2
from dotenv import load_dotenv
import os
from faker import Faker
import random

load_dotenv()

fake= Faker()

conn= psycopg2.connect(
    dbname= os.getenv('DBname'),
    user= os.getenv('User'),
    password= os.getenv('Password'),
    host=os.getenv('Host')
)
cursor= conn.cursor()

create_sales= """
CREATE TABLE IF NOT EXISTS sales(
id INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
product VARCHAR(100) NOT NULL,
amount NUMERIC,
date DATE,
customer_id INTEGER,
FOREIGN KEY (customer_id) REFERENCES customer(id) ON DELETE CASCADE
);
 """

create_customer= """
CREATE TABLE IF NOT EXISTS customer(
id INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
name VARCHAR(100),
city VARCHAR(100));

"""


cursor.execute(create_customer)
cursor.execute(create_sales)
conn.commit()



num_customers=100
for _ in range(num_customers):
    cursor.execute("INSERT INTO customer(name,city) VALUES(%s,%s)",
                   (
                       fake.name(),
                       fake.city()
    ))

conn.commit()


num_sales=200
for _ in range(num_sales):
    cursor.execute("INSERT INTO sales(product,amount,date,customer_id) VALUES(%s,%s,%s,%s)",
                   (
                       fake.word().title(),
                       fake.random_int(min=300, max=1000),
                       fake.date_between(start_date='-1y', end_date='today'),
                       random.randint(1,num_customers)
                       ))
conn.commit()

cursor.close()
conn.close()
    
