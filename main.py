from fastapi import FastAPI
from app.routers import funcionarios, ranking
from app.routers import tarefas
from app.routers import tiposTarefa
from app.routers import departamentos
from app.routers import cargos
from app.routers import login

# Core
app = FastAPI()

# Routes
app.include_router(funcionarios.router)
app.include_router(ranking.router)
app.include_router(tarefas.router)
app.include_router(tiposTarefa.router)
app.include_router(departamentos.router)
app.include_router(cargos.router)

app.include_router(login.router)

# Main
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)

# CRUD (Create / Read / Update / Delete)

# @app.get select
# @app.put insert
# @app.patch update
# @app.delete delete
# @app.post coringa

# boas praticas do SOLID