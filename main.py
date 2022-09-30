

from threading import Thread
from config import getConfig

from typing import Optional
import uvicorn
from fastapi import FastAPI,Header,Body
from win32 import win32api, win32event
# import win32con
from command import getCommandFunction, getCommandIdList
from fastapi.exceptions import HTTPException
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
# import pydantic
import subprocess

def startServer(onCommandExecute , onRawCommandExecute, port, authentication):
    print('server start')

    app = FastAPI()

    @app.get("/api/1.0/commands")
    def getCommands(Authorization : Optional[str] = Header(None)):
        if Authorization == None or Authorization != 'Basic ' + authentication:
            raise HTTPException(status_code=401 , detail="Unauthorized")
        return getCommandIdList()

    @app.post("/api/1.0/commands/{commandId}/execute")
    def executeCommand(commandId: str, Authorization : Optional[str] = Header(None)):
        if Authorization == None or Authorization != 'Basic ' + authentication:
            raise HTTPException(status_code=401 , detail="Unauthorized")
        return onCommandExecute({"commandId": commandId})

    class RawCmd(BaseModel):
        type: str
        value: str

    @app.post("/api/1.0/raw_commands")
    def executeCommand( item: RawCmd, Authorization : Optional[str] = Header(None)):
        if Authorization == None or Authorization != 'Basic ' + authentication:
            raise HTTPException(status_code=401 , detail="Unauthorized")
        # return onCommandExecute({"commandId": commandId})
        return onRawCommandExecute(item)
    

    app.mount("/", StaticFiles(directory="public"), name="static")

    uvicorn.run(app, host="0.0.0.0", port=port)

    print('server exit')



if __name__ == "__main__":
    config = getConfig()

    def onCommandExecute(event):
        commandFunction = getCommandFunction(event['commandId'])
        if commandFunction == None:
            raise HTTPException(status_code=404, detail="Command not found")
        
        commandFunction(config['main_hwmd'])

        return {"ok":1}

    def onRawCommandExecute(event):
        if(event.type == 'native'):
            p = subprocess.Popen(event.value, shell = config['run_command_with_shell']) # Needs to be shell since start isn't an executable, its a shell cmd
            p.wait() 
        
        

    startServer(onCommandExecute, onRawCommandExecute, config["server_port"], config["server_auth"])

