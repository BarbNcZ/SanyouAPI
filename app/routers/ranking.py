from fastapi import APIRouter
from app.services.database import getCursorAndConnection


router = APIRouter()

@router.get('/ranking')
def getRanking():
    cursorAndConnection = getCursorAndConnection()
    cursor = cursorAndConnection[0]
    connection = cursorAndConnection[1]
    try:
        print("Getting Ranking")

        cursor.execute(
            "SELECT f.nm_funcionario, f.nr_pontos "
            "FROM funcionario f "
            "ORDER BY f.nr_pontos DESC "
            "FETCH FIRST 10 ROWS ONLY "
        )
        funcionario = [
            {
                'nm_funcionario': row[0],
                'nr_pontos': row[1]
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