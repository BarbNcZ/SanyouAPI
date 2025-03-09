from fastapi import APIRouter
from app.services.database import getCursorAndConnection

router = APIRouter()

@router.delete('/deletetarefa/{cd_tarefas}')
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


@router.put('/createtarefa/{cd_tipo_tarefa}/{ds_tarefas}/{cd_funcionario}')
def createTarefa(cd_tipo_tarefa, ds_tarefas, cd_funcionario):
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

        cursor.execute("INSERT INTO TAREFAS_func (cd_funcionario, cd_TAREFAS) VALUES (:cd_funcionario, :cd_tarefas)",
                       {'cd_funcionario': cd_funcionario, 'cd_tarefas': id_tarefa})
        cursor.execute('SELECT SEQ_tarefa_func.CURRVAL FROM DUAL')
        id_func_tarefa = cursor.fetchone()[0]
        connection.commit()

        cursor.close()
        connection.close()

        if id_func_tarefa > 0 and id_tarefa > 0:
            return {'id_tarefa': id_tarefa}
        else:
            raise Exception()

    except Exception as e:
        print(e)
        # raise HTTPException(status_code=500, detail=str(e))

        cursor.close()
        connection.close()

        return {'id_tarefa': -1}


@router.get('/tarefas')
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

        return {'tarefas': []}@router.get('/tarefas')


@router.get('/tarefas/{cd_tarefas}')
def getTarefa(cd_tarefas):
    cursorAndConnection = getCursorAndConnection()
    cursor = cursorAndConnection[0]
    connection = cursorAndConnection[1]
    try:
        print('Getting Tarefa')
        cursor.execute("SELECT tp.DS_TIPO_TAREFA, t.DS_TAREFAS FROM TAREFAS t "
                       "LEFT OUTER JOIN TIPO_TAREFA tp ON t.cd_tipo_tarefa = tp.cd_tipo_tarefa "
                       f"WHERE t.CD_TAREFAS = \'{cd_tarefas}\' "
                       )
        tarefas = [
            {
                'ds_tipo_tarefa': row[0],
                'ds_tarefas': row[1]
            }
            for row in cursor.fetchall()
        ]

        cursor.close()
        connection.close()

        if len(tarefas) > 0:
            return tarefas[0]
        else:
            return None

    except Exception as e:
        print(e)
        # raise HTTPException(status_code=500, detail=str(e))

        cursor.close()
        connection.close()

        return None


@router.get('/tarefasbyfuncionario/{cd_funcionario}')
def getTarefasByFuncionario(cd_funcionario):
    cursorAndConnection = getCursorAndConnection()
    cursor = cursorAndConnection[0]
    connection = cursorAndConnection[1]
    try:
        print('Getting Tarefa by Funcionario')
        cursor.execute("SELECT tp.DS_TIPO_TAREFA, t.DS_TAREFAS FROM TAREFAS_FUNC tf "
                        "LEFT OUTER JOIN FUNCIONARIO f ON f.cd_funcionario = tf.cd_funcionario "
                        "LEFT OUTER JOIN TAREFAS t ON t.cd_tarefas = tf.cd_tarefas "
                        "LEFT OUTER JOIN TIPO_TAREFA tp ON t.cd_tipo_tarefa = tp.cd_tipo_tarefa "
                        f"WHERE f.CD_FUNCIONARIO = \'{cd_funcionario}\' "
                       )
        tarefas = [
            {
                'ds_tipo_tarefa': row[0],
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

        return{'tarefas': []}