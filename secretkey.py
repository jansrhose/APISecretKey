from fastapi import FastAPI, Request, HTTPException
app = FastAPI()
@app.get("/") 
async def read_main(token: str = None):
   if token != "ChavezSecretKey":
      raise HTTPException(status_code=401, detail="Unauthorized")
   return {"message": "Hello, World!"}
