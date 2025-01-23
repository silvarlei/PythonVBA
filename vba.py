afrom fastapi import FastAPI

app = FastAPI()

@app.get("/")
def hello_root():
    return {"message": "Sua senha esta errada"}
