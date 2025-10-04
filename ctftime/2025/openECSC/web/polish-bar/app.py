from fastapi import FastAPI, Request, Form
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates
import os, uvicorn, uuid
from config import BeverageConfig

app = FastAPI()
templates = Jinja2Templates(directory="templates")

sessions = {}

def admin_session_setup():
    session_id = str(uuid.uuid4())

    sessions[session_id] = {
        'username': 'admin',
        'password': str(os.urandom(10).hex()),
        'config': BeverageConfig(os.getenv('FLAG', 'openECSC{TEST_FLAG}'))
    }

admin_session_setup()
print(sessions)

@app.get("/")
async def get_index(request: Request):

    return templates.TemplateResponse("index.html", {"request": request})


@app.get("/register")
async def get_register(request: Request):

    return templates.TemplateResponse("register.html", {"request": request})


@app.post("/register")
async def post_register(request: Request, username: str = Form(...), password: str = Form(...)):

    new_session_id = str(uuid.uuid4())

    sessions[new_session_id] = { 'username': username, 'password': password, 'config': BeverageConfig(None) }

    response = RedirectResponse(url="/profile", status_code=303)
    response.set_cookie(key="session", value=new_session_id, httponly=True)
    return response


@app.get("/profile")
async def get_profile(request: Request):

    session_id = request.cookies.get('session')

    if session_id in sessions:
        return templates.TemplateResponse("profile.html", {
            "request": request, 
            "username": sessions[session_id]['username'],
            "config": sessions[session_id]['config'].get_config()
        })

    return RedirectResponse(url="/register", status_code=303)


@app.post("/config")
async def update_config(request: Request, config: str = Form(...), value: str = Form(...)):

    session_id = request.cookies.get('session')

    if session_id in sessions:
        err = sessions[session_id]['config'].update_property(config, value)

        return templates.TemplateResponse("profile.html", {
            "request": request, 
            "username": sessions[session_id]['username'],
            "config": sessions[session_id]['config'].get_config(),
            "error": 'Beverage is not in your shelf!' if err else ''
        })

    return RedirectResponse(url="/register", status_code=303)


@app.post("/beverage")
async def update_config(request: Request, beverage: str = Form(...)):

    session_id = request.cookies.get('session')

    if session_id in sessions:
        sessions[session_id]['config'].add_beverage(beverage)

        return templates.TemplateResponse("profile.html", {
            "request": request, 
            "username": sessions[session_id]['username'],
            "config": sessions[session_id]['config'].get_config()
        })

    return RedirectResponse(url="/register", status_code=303)


@app.post("/empty")
async def update_config(request: Request):

    session_id = request.cookies.get('session')

    if session_id in sessions:
        sessions[session_id]['config'].empty_alcohol_shelf()

        return templates.TemplateResponse("profile.html", {
            "request": request, 
            "username": sessions[session_id]['username'],
            "config": sessions[session_id]['config'].get_config()
        })

    return RedirectResponse(url="/register", status_code=303)


if __name__ == '__main__':
    uvicorn.run(app=app, host='0.0.0.0', port=80)
