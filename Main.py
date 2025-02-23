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

def getCursorAndConnection():
    try:
        print(f"Connecting to DB... Host: {db_host}, User: {db_user}")
        connection = oracledb.connect(user=db_user, password=db_password, host=db_host, sid='orcl')
        cursor = connection.cursor()
        print('Connection established')
        return [cursor, connection]

    except Exception as e:
        print('Error connecting to db', e)
        return None

# crud

@app.delete('/deletetarefa/{cd_tarefas}')
def deleteTarefa(cd_tarefas):
    cursorAndConnection = getCursorAndConnection()
    cursor = cursorAndConnection[0]
    connection = cursorAndConnection[1]

    result = False

    try:
        print('Deleting Tarefa')

        cursor.execute("DELETE FROM TAREFAS WHERE CD_TAREFAS = :cd_tarefas", {'cd_tarefas': cd_tarefas})

        if cursor.rowcount != 0:
            result = True

        connection.commit()

        cursor.close()
        connection.close()

        return {'result': result}


    except Exception as e:
        print(e)

        cursor.close()
        connection.close()

        return {'result': False}


@app.put('/createtarefa/{cd_tipo_tarefa}/{ds_tarefas}')
def createTarefa(cd_tipo_tarefa, ds_tarefas):
    cursorAndConnection = getCursorAndConnection()
    cursor = cursorAndConnection[0]
    connection = cursorAndConnection[1]
    try:
        print('Creating Tarefa')
        cursor.execute("INSERT INTO TAREFAS (CD_TIPO_TAREFA, DS_TAREFAS) VALUES (:cd_tipo_tarefa, :ds_tarefas)",
                       {'cd_tipo_tarefa': cd_tipo_tarefa, 'ds_tarefas': ds_tarefas})
        cursor.execute('SELECT SEQ_TAREFAS.CURRVAL FROM DUAL')
        id_tarefa = cursor.fetchone()[0]
        connection.commit()

        cursor.close()
        connection.close()

        return {'id_tarefa': id_tarefa}
    except Exception as e:
        print(e)
        # raise HTTPException(status_code=500, detail=str(e))

        cursor.close()
        connection.close()

        return {'id_tarefa': -1}


@app.get('/tipotarefa')
def getTipoTarefa():
    cursorAndConnection = getCursorAndConnection()
    cursor = cursorAndConnection[0]
    connection = cursorAndConnection[1]
    try:
        print('Getting Tipo Tarefa')
        cursor.execute("SELECT CD_TIPO_TAREFA, DS_TIPO_TAREFA FROM TIPO_TAREFA")
        tipos_tarefa = [
            {
                'cd_tipo_tarefa': row[0],
                'ds_tipo_tarefa': row[1]
            }
            for row in cursor.fetchall()
        ]

        cursor.close()
        connection.close()

        return {'tipo_tarefa': tipos_tarefa}
    except Exception as e:
        print(e)
        # raise HTTPException(status_code=500, detail=str(e))

        cursor.close()
        connection.close()

        return {'tipo_tarefa': []}


@app.get('/tarefas')
def getTarefas():
    cursorAndConnection = getCursorAndConnection()
    cursor = cursorAndConnection[0]
    connection = cursorAndConnection[1]
    try:
        print('Getting Tarefas')
        cursor.execute("SELECT CD_TAREFAS, DS_TAREFAS FROM TAREFAS")
        tarefas = [
            {
                'cd_tarefas': row[0],
                'ds_tarefas': row[1]
            }
            for row in cursor.fetchall()
        ]

        cursor.close()
        connection.close()

        return {'tarefas': tarefas}
    except Exception as e:
        print(e)
        # raise HTTPException(status_code=500, detail=str(e))

        cursor.close()
        connection.close()

        return {'tarefas': []}


@app.get('/departamentos')
def getDepartamento():
    cursorAndConnection = getCursorAndConnection()
    cursor = cursorAndConnection[0]
    connection = cursorAndConnection[1]
    try:
        print('Getting Departamentos')
        cursor.execute("SELECT CD_DEPTO, NM_DEPTO FROM DEPTO")
        depto = [
            {
                'cd_depto': row[0],
                'nm_depto': row[1]
            }
            for row in cursor.fetchall()
        ]

        cursor.close()
        connection.close()

        return {'depto': depto}
    except Exception as e:
        print(e)

        cursor.close()
        connection.close()

        return {'depto': []}


@app.get('/cargo')
def getCargo():
    cursorAndConnection = getCursorAndConnection()
    cursor = cursorAndConnection[0]
    connection = cursorAndConnection[1]
    try:
        print('Getting Cargos')
        cursor.execute("SELECT CD_CARGO, DS_CARGO FROM CARGO")
        cargo = [
            {
                'cd_cargo': row[0],
                'ds_cargo': row[1]
            }
            for row in cursor.fetchall()
        ]

        cursor.close()
        connection.close()

        return {'cargo': cargo}
    except Exception as e:
        print(e)

        cursor.close()
        connection.close()

        return {'cargo': []}


@app.put('/createfuncionario/{cd_depto}/{cd_cargo}/{ds_email}/{nm_funcionario}')
def createFuncionario(cd_depto, cd_cargo, ds_email, nm_funcionario):
    cursorAndConnection = getCursorAndConnection()
    cursor = cursorAndConnection[0]
    connection = cursorAndConnection[1]
    try:
        print('Creating Funcionario')
        cursor.execute(
            "INSERT INTO FUNCIONARIO (" \
            "cd_depto, cd_cargo, ds_email, nm_funcionario" \
            ") VALUES (" \
            ":cd_depto, :cd_cargo, :ds_email, :nm_funcionario" \
            ")",
            {
                'cd_depto': cd_depto,
                'cd_cargo': cd_cargo,
                'ds_email': ds_email,
                'nm_funcionario': nm_funcionario
            }
        )
        cursor.execute('SELECT SEQ_funcionario.CURRVAL FROM DUAL')
        cd_funcionario = cursor.fetchone()[0]
        connection.commit()

        cursor.close()
        connection.close()

        return {'cd_funcionario': cd_funcionario}
    except Exception as e:
        print(e)

        cursor.close()
        connection.close()

        return {'cd_funcionario': -1}

# @app.get select
# @app.put insert
# @app.patch update
# @app.delete delete
# @app.post coringa
# boas praticas do SOLID