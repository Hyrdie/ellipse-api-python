import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api.login import login_router

app = FastAPI(
    title="Ellipse Approval",
    version="1.0.0"
)

origins = ['*']

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

@app.get("/lmao")
def lmao():
    return {"Hello": "World"}

app.include_router(login_router, tags=["privileges"])

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=5000)