from fastapi import APIRouter
from app.services.database import getCursorAndConnection

router = APIRouter()

@router.get('/cargo')
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