from fastapi import FastAPI

app = FastAPI(title="Orders Service")


@app.get(path="/health")
async def health() -> dict[str, str]:
    return {"status": "ok"}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app="main:app", host="localhost", port=8000)
