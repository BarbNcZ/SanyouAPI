from fastapi import APIRouter
from app.services.database import getCursorAndConnection

router = APIRouter()


@router.get('/funcionarios')
def getFuncionarios():
    cursorAndConnection = getCursorAndConnection()
    cursor = cursorAndConnection[0]
    connection = cursorAndConnection[1]
    try:
        print("Getting Funcionarios")

        cursor.execute(
            "SELECT f.cd_funcionario, d.nm_depto, c.ds_cargo, f.nm_funcionario "
            "FROM funcionario f "
            "LEFT OUTER JOIN DEPTO d ON f.cd_depto = d.cd_depto "
            "LEFT OUTER JOIN CARGO c ON f.cd_cargo = c.cd_cargo "
        )
        funcionario = [
            {
            'cd_funcionario': row[0],
            'nm_depto': row[1],
            'ds_cargo': row[2],
            'nm_funcionario': row[3],
            'nr_pontos': None
            }
        for row in cursor.fetchall()
        ]

        cursor.close()
        connection.close()

        return {'funcionario': funcionario}
    except Exception as e:
        print(e)

        cursor.close()
        connection.close()

        return {'funcionario': []}


@router.put('/createfuncionario/{cd_depto}/{cd_cargo}/{ds_email}/{nm_funcionario}')
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


@router.delete('/deletefuncionario/{cd_funcionario}')
def deleteFuncionario(cd_funcionario):
    cursorAndConnection = getCursorAndConnection()
    cursor = cursorAndConnection[0]
    connection = cursorAndConnection[1]

    result = False

    try:
        print('Deleting Funcionario')

        cursor.execute("DELETE FROM FUNCIONARIO WHERE CD_FUNCIONARIO = :cd_funcionario", {'cd_funcionario': cd_funcionario})

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