from fastapi import FastAPI
import requests
from fastapi.middleware.cors import CORSMiddleware
import ssl
import json

app = FastAPI()

origins = [
    "http://10.0.0.66:5173",
    "https://castleofgaara.com",
    "https://www.castleofgaara.com",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
ssl_context.load_cert_chain('/home/pcave/workspace/hue_v1/cert.pem', keyfile='/home/pcave/workspace/hue_v1/key.pem')

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.put("/on/")
async def on():
    json = {
        "on": True
    }

    r = requests.put('http://10.0.0.213/api/FoRt9CrSnk0g7YdF9x5vmGqpJmcjJUTQg1PbGykm/lights/1/state', json=json) 
  
    print(r) 
    print(r.content) 

    return {"message": "on"}

@app.put("/off/")
async def off():
    json = {
        "on": False
    }

    r = requests.put('http://10.0.0.213/api/FoRt9CrSnk0g7YdF9x5vmGqpJmcjJUTQg1PbGykm/lights/1/state', json=json) 
  
    print(r) 
    print(r.content) 

    return {"message": "off"}

@app.get("/status/")
async def status():

    r = requests.get('http://10.0.0.213/api/FoRt9CrSnk0g7YdF9x5vmGqpJmcjJUTQg1PbGykm/lights/1')
    
    jsonString = r.content.decode('utf-8')
    jsonObject = json.loads(jsonString)
    print(r)
    print(jsonObject["state"]["on"])

    return {"message": jsonObject["state"]["on"]}

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, ssl=ssl_context)

