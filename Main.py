from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import oracledb
from dotenv import load_dotenv
import os

app = FastAPI()

load_dotenv()  # Load variables from .env

db_host = os.getenv("DB_HOST")
db_user = os.getenv("DB_USER")
db_password = os.getenv("DB_PASSWORD")

try:
    connection = oracledb.connect(user=db_user, password=db_password, host=db_host, sid='orcl')
    cursor = connection.cursor()
    print('Connection established')

except Exception as e:
    print('Error connecting to db', e)

#crud

@app.get('/tarefa/{cd_tipo_tarefa}/{ds_tarefas}')
def createTarefa(cd_tipo_tarefa, ds_tarefas):
    try:
        cursor.execute("INSERT INTO TAREFAS (CD_TIPO_TAREFA, DS_TAREFAS) VALUES (:cd_tipo_tarefa, :ds_tarefas)",{'cd_tipo_tarefa': cd_tipo_tarefa, 'ds_tarefas': ds_tarefas})
        cursor.execute('SELECT SEQ_TAREFAS.CURRVAL FROM DUAL')
        id_tarefa = cursor.fetchone()[0]
        connection.commit()
        return { 'id_tarefa': id_tarefa }
    except Exception as e:
        print(e)
        #raise HTTPException(status_code=500, detail=str(e))
        return {'id_tarefa': -1}



#@app.put insert
#@app.get select
#@app.patch update
#@app.delete delete
#@app.post coringa