import uvicorn

from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from config import settings
from usuarios.routers import urlRouter as userRouter


app = FastAPI(
    title = settings.PROJECT_NAME,
    description = settings.PROJECT_DESCRIPTION,
    version = settings.PROJECT_VERSION,
    openapi_tags=[{
        'name': 'usuarios',
        'description': 'usuarios routes'
    }],
    swagger_ui_parameters = {'docExpansion': 'none'},
)

origins = ['*']

# habilitar CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)

templates = Jinja2Templates(directory='templates')

@app.get('/', response_class=HTMLResponse, include_in_schema=False)
def home(request: Request):
    return templates.TemplateResponse('landing.html', {'request': request})


# incluímos las URL definidas en cada router
# localhost:8000/docs
app.include_router(userRouter)


if __name__ == '__main__':
    uvicorn.run('main:app', host='192.168.4.74', port=8000, workers=2, log_level='info')
