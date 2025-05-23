from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
import json

app = FastAPI()

# CORS settings
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["GET"],
    allow_headers=["*"],
)

# Load marks
with open("q-vercel-python.json", "r") as f:
    student_data = json.load(f)
    marks_dict = {entry["name"]: entry["marks"] for entry in student_data}

@app.get("/api")
async def get_marks(request: Request):
    names = request.query_params.getlist("name")
    result = [marks_dict.get(name, None) for name in names]
    return JSONResponse(content={"marks": result})
