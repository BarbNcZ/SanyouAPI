from fastapi import APIRouter
from app.services.database import getCursorAndConnection


router = APIRouter()

@router.get('/charttaskperrole')
def getChartTaskPerRole():
    cursorAndConnection = getCursorAndConnection()
    cursor = cursorAndConnection[0]
    connection = cursorAndConnection[1]
    try:
        print("Getting Chart Task Per Role")


        cursor.execute(
            "SELECT c.ds_cargo, COUNT(t.cd_tarefas) AS qtd_tarefas "
            "FROM tarefas t "
            "LEFT OUTER JOIN TAREFAS_FUNC tf ON tf.cd_tarefas = t.cd_tarefas "
            "LEFT OUTER JOIN FUNCIONARIO f ON f.cd_funcionario = tf.cd_funcionario "
            "LEFT OUTER JOIN CARGO c ON c.cd_cargo = f.cd_cargo "
            "WHERE c.cd_cargo != 1 "
            "GROUP BY c.ds_cargo "
        )

        totalTasks = [
            {
                'ds_cargo': row[0],
                'qtd_tarefas': row[1]
            }
            for row in cursor.fetchall()
        ]

        cursor.execute(
            "SELECT c.ds_cargo, COUNT(t.cd_tarefas) AS qtd_tarefas "
            "FROM tarefas t "
            "LEFT OUTER JOIN TAREFAS_FUNC tf ON tf.cd_tarefas = t.cd_tarefas "
            "LEFT OUTER JOIN FUNCIONARIO f ON f.cd_funcionario = tf.cd_funcionario "
            "LEFT OUTER JOIN CARGO c ON c.cd_cargo = f.cd_cargo "
            "WHERE c.cd_cargo != 1 AND t.bt_finalizado = 1 "
            "GROUP BY c.ds_cargo "
        )
        data = [
            {
                'ds_cargo': row[0],
                'qtd_tarefas': row[1],
                'qtd_tarefasTotal': totalTasks[index]['qtd_tarefas']
            }
        for index, row in enumerate(cursor.fetchall())
        ]

        cursor.close()
        connection.close()

        return {'data': data}
    except Exception as e:
        print(e)

        cursor.close()
        connection.close()

        return {'data': []}


@router.get('/charttaskperdepartment')
def getChartTaskPerDepartment():
    cursorAndConnection = getCursorAndConnection()
    cursor = cursorAndConnection[0]
    connection = cursorAndConnection[1]
    try:
        print("Getting Chart Task Per Department")


        cursor.execute(
            "SELECT d.nm_depto, COUNT(t.cd_tarefas) AS qtd_tarefas "
            "FROM tarefas t "
            "LEFT OUTER JOIN TAREFAS_FUNC tf ON tf.cd_tarefas = t.cd_tarefas "
            "LEFT OUTER JOIN FUNCIONARIO f ON f.cd_funcionario = tf.cd_funcionario "
            "LEFT OUTER JOIN DEPTO d ON d.cd_depto = f.cd_depto "
            "WHERE f.cd_cargo != 1 "
            "GROUP BY d.nm_depto "
        )

        totalTasks = [
            {
                'nm_depto': row[0],
                'qtd_tarefas': row[1]
            }
            for row in cursor.fetchall()
        ]

        cursor.execute(
            "SELECT d.nm_depto, COUNT(t.cd_tarefas) AS qtd_tarefas "
            "FROM tarefas t "
            "LEFT OUTER JOIN TAREFAS_FUNC tf ON tf.cd_tarefas = t.cd_tarefas "
            "LEFT OUTER JOIN FUNCIONARIO f ON f.cd_funcionario = tf.cd_funcionario "
            "LEFT OUTER JOIN DEPTO d ON d.cd_depto = f.cd_depto "
            "WHERE f.cd_cargo != 1 AND t.bt_finalizado = 1 "
            "GROUP BY d.nm_depto "
        )
        data = [
            {
                'nm_depto': row[0],
                'qtd_tarefas': row[1],
                'qtd_tarefasTotal': totalTasks[index]['qtd_tarefas']
            }
        for index, row in enumerate(cursor.fetchall())
        ]

        cursor.close()
        connection.close()

        return {'data': data}
    except Exception as e:
        print(e)

        cursor.close()
        connection.close()

        return {'data': []}


@router.get('/charttaskperdifficulty')
def getChartTaskPerDifficulty():
    cursorAndConnection = getCursorAndConnection()
    cursor = cursorAndConnection[0]
    connection = cursorAndConnection[1]
    try:
        print("Getting Chart Task Per Difficulty")

        cursor.execute(
            "SELECT CASE  "
            "    WHEN ( "
            "        t.nr_dificuldade - ( "
            "            50*( "
            "                TO_NUMBER( "
            "                    TO_CHAR( "
            "                        TIMESTAMP '1970-01-01 00:00:00 UTC' +  "
            "                        NUMTODSINTERVAL(t.nr_tempo / 1000, 'SECOND'), "
            "                        'MI' "
            "                    ) "
            "                )/30 "
            "            ) "
            "        ) - ( "
            "            100*TO_NUMBER( "
            "                TO_CHAR( "
            "                    TIMESTAMP '1970-01-01 00:00:00 UTC' +  "
            "                    NUMTODSINTERVAL(t.nr_tempo / 1000, 'SECOND'), "
            "                    'HH' "
            "                ) "
            "            ) "
            "        ) "
            "    ) = 10 THEN 1 "
            "    WHEN ( "
            "        t.nr_dificuldade - ( "
            "            50*( "
            "                TO_NUMBER( "
            "                    TO_CHAR( "
            "                        TIMESTAMP '1970-01-01 00:00:00 UTC' +  "
            "                        NUMTODSINTERVAL(t.nr_tempo / 1000, 'SECOND'), "
            "                        'MI' "
            "                    ) "
            "                )/30 "
            "            ) "
            "        ) - ( "
            "            100*TO_NUMBER( "
            "                TO_CHAR( "
            "                    TIMESTAMP '1970-01-01 00:00:00 UTC' +  "
            "                    NUMTODSINTERVAL(t.nr_tempo / 1000, 'SECOND'), "
            "                    'HH' "
            "                ) "
            "            ) "
            "        ) "
            "    ) = 25 THEN 2 "
            "    WHEN ( "
            "        t.nr_dificuldade - ( "
            "            50*( "
            "                TO_NUMBER( "
            "                    TO_CHAR( "
            "                        TIMESTAMP '1970-01-01 00:00:00 UTC' +  "
            "                        NUMTODSINTERVAL(t.nr_tempo / 1000, 'SECOND'), "
            "                        'MI' "
            "                    ) "
            "                )/30 "
            "            ) "
            "        ) - ( "
            "            100*TO_NUMBER( "
            "                TO_CHAR( "
            "                    TIMESTAMP '1970-01-01 00:00:00 UTC' +  "
            "                    NUMTODSINTERVAL(t.nr_tempo / 1000, 'SECOND'), "
            "                    'HH' "
            "                ) "
            "            ) "
            "        ) "
            "    ) = 50 THEN 3 "
            "    WHEN ( "
            "        t.nr_dificuldade - ( "
            "            50*( "
            "                TO_NUMBER( "
            "                    TO_CHAR( "
            "                        TIMESTAMP '1970-01-01 00:00:00 UTC' +  "
            "                        NUMTODSINTERVAL(t.nr_tempo / 1000, 'SECOND'), "
            "                        'MI' "
            "                    ) "
            "                )/30 "
            "            ) "
            "        ) - ( "
            "            100*TO_NUMBER( "
            "                TO_CHAR( "
            "                    TIMESTAMP '1970-01-01 00:00:00 UTC' +  "
            "                    NUMTODSINTERVAL(t.nr_tempo / 1000, 'SECOND'), "
            "                    'HH' "
            "                ) "
            "            ) "
            "        ) "
            "    ) = 75 THEN 4 "
            "    WHEN ( "
            "        t.nr_dificuldade - ( "
            "            50*( "
            "                TO_NUMBER( "
            "                    TO_CHAR( "
            "                        TIMESTAMP '1970-01-01 00:00:00 UTC' +  "
            "                        NUMTODSINTERVAL(t.nr_tempo / 1000, 'SECOND'), "
            "                        'MI' "
            "                    ) "
            "                )/30 "
            "            ) "
            "        ) - ( "
            "            100*TO_NUMBER( "
            "                TO_CHAR( "
            "                    TIMESTAMP '1970-01-01 00:00:00 UTC' +  "
            "                    NUMTODSINTERVAL(t.nr_tempo / 1000, 'SECOND'), "
            "                    'HH' "
            "                ) "
            "            ) "
            "        ) "
            "    ) = 100 THEN 5 "
            "    ELSE 0 "
            "  END AS NR_DIFICULDADE, COUNT(*) AS qtd_tarefas  "
            "FROM tarefas t  "
            "WHERE t.bt_finalizado = 1  "
            "GROUP BY CASE  "
            "    WHEN ( "
            "        t.nr_dificuldade - ( "
            "            50*( "
            "                TO_NUMBER( "
            "                    TO_CHAR( "
            "                        TIMESTAMP '1970-01-01 00:00:00 UTC' +  "
            "                        NUMTODSINTERVAL(t.nr_tempo / 1000, 'SECOND'), "
            "                        'MI' "
            "                    ) "
            "                )/30 "
            "            ) "
            "        ) - ( "
            "            100*TO_NUMBER( "
            "                TO_CHAR( "
            "                    TIMESTAMP '1970-01-01 00:00:00 UTC' +  "
            "                    NUMTODSINTERVAL(t.nr_tempo / 1000, 'SECOND'), "
            "                    'HH' "
            "                ) "
            "            ) "
            "        ) "
            "    ) = 10 THEN 1 "
            "    WHEN ( "
            "        t.nr_dificuldade - ( "
            "            50*( "
            "                TO_NUMBER( "
            "                    TO_CHAR( "
            "                        TIMESTAMP '1970-01-01 00:00:00 UTC' +  "
            "                        NUMTODSINTERVAL(t.nr_tempo / 1000, 'SECOND'), "
            "                        'MI' "
            "                    ) "
            "                )/30 "
            "            ) "
            "        ) - ( "
            "            100*TO_NUMBER( "
            "                TO_CHAR( "
            "                    TIMESTAMP '1970-01-01 00:00:00 UTC' +  "
            "                    NUMTODSINTERVAL(t.nr_tempo / 1000, 'SECOND'), "
            "                    'HH' "
            "                ) "
            "            ) "
            "        ) "
            "    ) = 25 THEN 2 "
            "    WHEN ( "
            "        t.nr_dificuldade - ( "
            "            50*( "
            "                TO_NUMBER( "
            "                    TO_CHAR( "
            "                        TIMESTAMP '1970-01-01 00:00:00 UTC' +  "
            "                        NUMTODSINTERVAL(t.nr_tempo / 1000, 'SECOND'), "
            "                        'MI' "
            "                    ) "
            "                )/30 "
            "            ) "
            "        ) - ( "
            "            100*TO_NUMBER( "
            "                TO_CHAR( "
            "                    TIMESTAMP '1970-01-01 00:00:00 UTC' +  "
            "                    NUMTODSINTERVAL(t.nr_tempo / 1000, 'SECOND'), "
            "                    'HH' "
            "                ) "
            "            ) "
            "        ) "
            "    ) = 50 THEN 3 "
            "    WHEN ( "
            "        t.nr_dificuldade - ( "
            "            50*( "
            "                TO_NUMBER( "
            "                    TO_CHAR( "
            "                        TIMESTAMP '1970-01-01 00:00:00 UTC' +  "
            "                        NUMTODSINTERVAL(t.nr_tempo / 1000, 'SECOND'), "
            "                        'MI' "
            "                    ) "
            "                )/30 "
            "            ) "
            "        ) - ( "
            "            100*TO_NUMBER( "
            "                TO_CHAR( "
            "                    TIMESTAMP '1970-01-01 00:00:00 UTC' +  "
            "                    NUMTODSINTERVAL(t.nr_tempo / 1000, 'SECOND'), "
            "                    'HH' "
            "                ) "
            "            ) "
            "        ) "
            "    ) = 75 THEN 4 "
            "    WHEN ( "
            "        t.nr_dificuldade - ( "
            "            50*( "
            "                TO_NUMBER( "
            "                    TO_CHAR( "
            "                        TIMESTAMP '1970-01-01 00:00:00 UTC' +  "
            "                        NUMTODSINTERVAL(t.nr_tempo / 1000, 'SECOND'), "
            "                        'MI' "
            "                    ) "
            "                )/30 "
            "            ) "
            "        ) - ( "
            "            100*TO_NUMBER( "
            "                TO_CHAR( "
            "                    TIMESTAMP '1970-01-01 00:00:00 UTC' +  "
            "                    NUMTODSINTERVAL(t.nr_tempo / 1000, 'SECOND'), "
            "                    'HH' "
            "                ) "
            "            ) "
            "        ) "
            "    ) = 100 THEN 5 "
            "    ELSE 0 "
            "END "
        )
        data = [
            {
                'nr_dificuldade': row[0],
                'qtd_tarefas': row[1]
            }
        for row in cursor.fetchall()
        ]

        cursor.close()
        connection.close()

        return {'data': data}
    except Exception as e:
        print(e)

        cursor.close()
        connection.close()

        return {'data': []}