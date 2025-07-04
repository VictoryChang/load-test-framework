import time

from fastapi import FastAPI, HTTPException
import uvicorn


app = FastAPI()


@app.get("/fast")
def fast():
    return "fast" 


@app.get("/slow")
def fast():
    time.sleep(2)
    return "slow" 


user_db = {
    1: "Bob",
    2: "Anne",
    3: "Cynthia"
}


@app.get("/users/{user_id}")
def get_user(user_id: int):
    if user_id in user_db:
        return user_db[user_id]
    raise HTTPException(status_code=404, detail="User not found")


if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host='0.0.0.0', port=8000) 
