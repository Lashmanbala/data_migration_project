import dotenv
import os
from read import read_table
from write import load_table

def main():
    src_endpoint = os.environ.get('SOURCE_DB_HOST')
    src_db_name = os.environ.get('SOURCE_DB_NAME')
    src_user_name = os.environ.get('SOURCE_DB_USER')
    src_password = os.environ.get('SOURCE_DB_PASS')

    tgt_endpoint = os.environ.get('TGT_DB_HOST')
    tgt_user_name = os.environ.get('TGT_DB_USER')
    tgt_password = os.environ.get('TGT_DB_PASS')
    tgt_db_name = os.environ.get('TGT_DB_NAME')

    table_list = os.environ.get('TABLE_LIST_STR').split(', ')

    for table_name in table_list:

        data, columns = read_table(src_endpoint, src_db_name, src_user_name, src_password, table_name)
    
        load_table(tgt_endpoint, tgt_db_name, tgt_user_name, tgt_password, table_name, columns, data)


if __name__ == "__main__":

    dotenv.load_dotenv()
    main()