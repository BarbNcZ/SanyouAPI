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

        cursor.execute("DELETE FROM TAREFAS_FUNC WHERE CD_TAREFAS = :cd_tarefas", {'cd_tarefas': cd_tarefas})

        connection.commit()

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


@router.delete('/concluirtarefa/{cd_tarefas}/{cd_funcionario}')
def concluirTarefa(cd_tarefas, cd_funcionario):
    cursorAndConnection = getCursorAndConnection()
    cursor = cursorAndConnection[0]
    connection = cursorAndConnection[1]

    result = False

    try:
        print('Finalizando Tarefa')


        cursor.execute(
            "SELECT t.NR_DIFICULDADE, f.NR_PONTOS FROM TAREFAS_FUNC tf "
            "LEFT OUTER JOIN FUNCIONARIO f ON tf.CD_FUNCIONARIO = f.CD_FUNCIONARIO "
            "LEFT OUTER JOIN TAREFAS t ON tf.CD_TAREFAS = t.CD_TAREFAS "
            f"WHERE t.CD_TAREFAS = \'{cd_tarefas}\' "
            f"AND f.CD_FUNCIONARIO = \'{cd_funcionario}\' "
            )
        tarefas = [
            {
                'nr_dificuldade': row[0],
                'nr_pontos': row[1]
            }
            for row in cursor.fetchall()
        ]

        if len(tarefas) > 0:
            tarefa = tarefas[0]

            cursor.execute(
                "UPDATE FUNCIONARIO SET nr_pontos = :nr_pontos "
                "WHERE cd_funcionario = :cd_funcionario ",
                {
                    'nr_pontos': (tarefa['nr_pontos'] + tarefa['nr_dificuldade']),
                    'cd_funcionario':cd_funcionario
                }
            )

            connection.commit()

            cursor.execute("UPDATE TAREFAS SET bt_finalizado = 1 WHERE CD_TAREFAS = :cd_tarefas", {'cd_tarefas': cd_tarefas})

            if cursor.rowcount != 0:
                result = True

            connection.commit()

            cursor.close()
            connection.close()

            return {'result': result}


        else:
            return {'result': False}

    except Exception as e:
        print(e)

        cursor.close()
        connection.close()

        return {'result': False}


@router.put('/createtarefa/{cd_tipo_tarefa}/{ds_tarefas}/{cd_funcionario}/{nr_dificuldade}/{nr_tempo}')
def createTarefa(cd_tipo_tarefa, ds_tarefas, cd_funcionario, nr_dificuldade, nr_tempo):
    cursorAndConnection = getCursorAndConnection()
    cursor = cursorAndConnection[0]
    connection = cursorAndConnection[1]
    try:
        print('Creating Tarefa')
        cursor.execute("INSERT INTO TAREFAS (CD_TIPO_TAREFA, DS_TAREFAS, NR_DIFICULDADE, NR_TEMPO) VALUES (:cd_tipo_tarefa, :ds_tarefas, :nr_dificuldade, :nr_tempo)",
                       {'cd_tipo_tarefa': cd_tipo_tarefa, 'ds_tarefas': ds_tarefas, 'nr_dificuldade': nr_dificuldade, 'nr_tempo': nr_tempo})
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
        cursor.execute("SELECT CD_TAREFAS, DS_TAREFAS, NR_TEMPO, NR_DIFICULDADE, BT_FINALIZADO FROM TAREFAS")
        tarefas = [
            {
                'cd_tarefas': row[0],
                'ds_tarefas': row[1],
                'nr_tempo': row[2],
                'nr_dificuldade': row[3],
                'bt_finalizado': row[4]
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
        cursor.execute("SELECT tp.DS_TIPO_TAREFA, t.DS_TAREFAS, t.NR_TEMPO, t.NR_DIFICULDADE, t.BT_FINALIZADO FROM TAREFAS t "
                       "LEFT OUTER JOIN TIPO_TAREFA tp ON t.cd_tipo_tarefa = tp.cd_tipo_tarefa "
                       f"WHERE t.CD_TAREFAS = \'{cd_tarefas}\' "
                       )
        tarefas = [
            {
                'ds_tipo_tarefa': row[0],
                'ds_tarefas': row[1],
                'nr_tempo': row[2],
                'nr_dificuldade': row[3],
                'bt_finalizado': row[4]
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
        cursor.execute("SELECT t.cd_tarefas, tp.DS_TIPO_TAREFA, t.DS_TAREFAS, t.NR_TEMPO, t.NR_DIFICULDADE, t.BT_FINALIZADO FROM TAREFAS_FUNC tf "
                        "LEFT OUTER JOIN FUNCIONARIO f ON f.cd_funcionario = tf.cd_funcionario "
                        "LEFT OUTER JOIN TAREFAS t ON t.cd_tarefas = tf.cd_tarefas "
                        "LEFT OUTER JOIN TIPO_TAREFA tp ON t.cd_tipo_tarefa = tp.cd_tipo_tarefa "
                        f"WHERE f.CD_FUNCIONARIO = \'{cd_funcionario}\' "
                       )
        tarefas = [
            {
                'cd_tarefas': row[0],
                'ds_tipo_tarefa': row[1],
                'ds_tarefas': row[2],
                'nr_tempo': row[3],
                'nr_dificuldade': row[4],
                'bt_finalizado': row[5]
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