import time

from fastapi import FastAPI
import uvicorn


app = FastAPI()


@app.get("/fast")
def fast():
    return "fast" 


@app.get("/slow")
def fast():
    time.sleep(2)
    return "slow" 


if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host='0.0.0.0', port=8000) 
