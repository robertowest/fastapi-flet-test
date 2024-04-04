from fastapi import FastAPI

from apps.personas.routes import router as personasRouter

app = FastAPI()

# incluímos las URL definidas en cada router
# localhost:8000/docs
app.include_router(personasRouter)




if __name__ == "__main__":
    import uvicorn
    # uvicorn.run("main:app", host="192.168.4.74", port=8000, workers=2, log_level="info")
    uvicorn.run('main:app', host='localhost', port=8000, workers=2, log_level='info')
