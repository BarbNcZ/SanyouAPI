from fastapi import APIRouter
from app.services.database import getCursorAndConnection

router = APIRouter()

@router.get('/departamentos')
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