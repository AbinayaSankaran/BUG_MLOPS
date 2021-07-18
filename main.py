import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel
from ml_utils import load_model, predict, retrain
from datetime import date, datetime
from typing import List
app = FastAPI(
    title="Bug Predictor",
    docs_url="/"
)

app.add_event_handler("startup", load_model)

class QueryIn(BaseModel):
    line_countof_code: float
    cyclomatic_complexity : float
    essential_complexity : float
    design_complexity: float
    total_operators_operands : float
    volume :float
    program_length : float
    difficulty :float
    intelligence :float
    effort :float
    b :float
    time_estimator :float
    line_count :float
    count_of_lines_of_comments :float
    count_of_blank_lines :float
    count_of_CodeAndComment :float
    unique_operators :float
    unique_operands :float
    total_operators : float
    total_operands :float
    branchCount_of_flow_graph : float
    

class QueryOut(BaseModel):
    defects: str
    timestamp: str
    timestamp1 : datetime

class FeedbackIn(BaseModel):
  
    line_countof_code: float
    cyclomatic_complexity : float
    essential_complexity : float
    design_complexity: float
    total_operators_operands : float
    volume :float
    program_length : float
    difficulty :float
    intelligence :float
    effort :float
    b :float
    time_estimator :float
    line_count :float
    count_of_lines_of_comments :float
    count_of_blank_lines :float
    count_of_CodeAndComment :float
    unique_operators :float
    unique_operands :float
    total_operators : float
    total_operands :float
    branchCount_of_flow_graph : float
    defects: str
    


@app.get("/ping")
def ping():
    return {"ping": "pong"}


@app.post("/predict", response_model=QueryOut, status_code=200)
def predict_bug(query_data: QueryIn):
    output = {'defects': predict(query_data),'timestamp': datetime.now()}
    return output

@app.post("/feedback",status_code=200)
def feedback(data: List[FeedbackIn]):
    retrain(data)
    return{"detail":"Feedback successful retrained the model"}

if __name__ == "__main__":
    uvicorn.run("main:app", host='127.0.0.1', port=8888, reload=True)
