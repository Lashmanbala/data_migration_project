import dotenv
import os
from read import read_table
from write import build_insert_query, load_table
import psycopg2

dotenv.load_dotenv()

endpoint = os.environ.get('SOURCE_DB_HOST')
db_name = os.environ.get('SOURCE_DB_NAME')
user_name = os.environ.get('SOURCE_DB_USER')
password = os.environ.get('SOURCE_DB_PASS')
table_name = 'categories'
# limit = 10

res = read_table(endpoint, db_name, user_name, password, table_name)

print(res[0])
print(res[1])

data = res[0]
columns = res[1]


endpoint = os.environ.get('TGT_DB_HOST')
user_name = os.environ.get('TGT_DB_USER')
password = os.environ.get('TGT_DB_PASS')
db_name = os.environ.get('TGT_DB_NAME')

load_table(endpoint, db_name, user_name, password, table_name, columns, data)
