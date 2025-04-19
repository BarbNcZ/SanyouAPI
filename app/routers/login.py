from fastapi import APIRouter
from pydantic import BaseModel

from app.services.database import getCursorAndConnection

router = APIRouter()

class User(BaseModel):
    email: str
    password: str

@router.post('/login/')
def login(user: User):
    cursorAndConnection = getCursorAndConnection()
    cursor = cursorAndConnection[0]
    connection = cursorAndConnection[1]
    try:
        print('Logging in ...')

        query = "SELECT f.cd_funcionario, f.nm_funcionario, d.nm_depto, c.ds_cargo "\
            "FROM funcionario f "\
            "LEFT OUTER JOIN DEPTO d ON f.cd_depto = d.cd_depto "\
            "LEFT OUTER JOIN CARGO c ON f.cd_cargo = c.cd_cargo "\
            f"WHERE f.ds_email = \'{user.email}\' AND f.ps_password = \'{user.password}\' "

        print(query)

        cursor.execute(
            query
        )
        funcionario = [
            {
                'cd_funcionario': row[0],
                'nm_funcionario': row[1],
                'nm_depto': row[2],
                'ds_cargo': row[3]
            }
            for row in cursor.fetchall()
        ]

        cursor.close()
        connection.close()

        if len(funcionario) > 0:
            return funcionario[0]
        else:
            return None

    except Exception as e:
        print(e)

        cursor.close()
        connection.close()

        return None