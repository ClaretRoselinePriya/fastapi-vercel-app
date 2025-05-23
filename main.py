from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
import json
import os

app = FastAPI()

# Enable CORS for all origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["GET"],
    allow_headers=["*"],
)

# Load the marks data from JSON file
file_path = os.path.join(os.path.dirname(__file__), "q-vercel-python.json")
with open(file_path, "r") as f:
    student_data = json.load(f)
    marks_dict = {entry["name"]: entry["marks"] for entry in student_data}

@app.get("/api")
async def get_marks(request: Request):
    names = request.query_params.getlist("name")
    results = [marks_dict.get(name, None) for name in names]
    return JSONResponse(content={"marks": results})
