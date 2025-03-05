import oracledb
from config.settings import db_host
from config.settings import db_user
from config.settings import db_password

def getCursorAndConnection():
    try:
        print(f"Connecting to DB... Host: {db_host} | User: {db_user}")
        connection = oracledb.connect(user=db_user, password=db_password, host=db_host, sid='orcl')
        cursor = connection.cursor()
        print('Connection established')
        return [cursor, connection]

    except Exception as e:
        print('Error connecting to DB', e)
        return None