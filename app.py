import dotenv
import os
from read import read_table

dotenv.load_dotenv()

endpoint = os.environ.get('SOURCE_DB_HOST')
db_name = os.environ.get('SOURCE_DB_NAME')
user_name = os.environ.get('SOURCE_DB_USER')
password = os.environ.get('SOURCE_DB_PASS')
table_name = 'orders'
limit = 10

res = read_table(endpoint, db_name, user_name, password, table_name, limit)

print(res[0])
print(res[1])
