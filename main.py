import orjson
from fastapi import FastAPI
from fastapi.responses import ORJSONResponse

app = FastAPI(
    default_response_class=ORJSONResponse,
    debug=False
)

# read json file with ORJSON
with open('result.json', 'r') as f:
    result = orjson.loads(f.read())

@app.get("/")
async def read_root():
    return result
