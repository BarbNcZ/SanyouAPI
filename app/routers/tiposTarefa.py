from fastapi import APIRouter
from app.services.database import getCursorAndConnection

router = APIRouter()

@router.get('/tipotarefa')
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