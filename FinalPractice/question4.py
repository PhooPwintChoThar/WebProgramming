from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

app=FastAPI()
templates=Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")
questions=["I enjoy working with numbers and data","I prefer creative and artistic tasks","I like helping and teaching others","I enjoy building and fixing things","I'm interested in science and research"]
categories=["Analytical", "Creative", "Socail", "Technical"]
categories_scores=[0,0,0,0,0]
careers=["Data Analyst or Scientist","Designer or Artist","Teacher or Counselor", "Engineer or Technician"]
recommended_counts=[0,0,0,0]
survery_counts=0
@app.get("/survery")
def show_form(request:Request):
    return templates.TemplateResponse("form4.html", {"request":request})

@app.post("/survery/results", response_class=HTMLResponse)
def show_results(q1:int=Form(...), q2:int=Form(...),q3:int=Form(...),q4:int=Form(...),q5:int=Form(...)):
    global survery_counts
    survery_counts+=1
    result="<!DOCTYPE html><html><head><title>Result</title></head><body>"
    scores=[q1, q2, q3,q4,q5]
    categories_scores[0]=q1+q5
    categories_scores[1]=q2
    categories_scores[2]=q3
    categories_scores[3]=q4
    
    highest=max(categories_scores)
    result+="<h1>Survey Results for Career Aptitude</h1><h3>Individual question scores</h3>"
    for i in range(0,5):
        result+=f"<p>{questions[i]} - {scores[i]}</p>"
    result+="<h3>Category Breakdown</h3>"
    for j in range(0,4):
        result+=f"<p>{categories[j]} - {categories_scores[j]}"
    result+="<h3>Recommended Career paths</h3>"
    for i in range(0,4):
        if categories_scores[i]==highest:
            result+=f"<p>{careers[i]}<p>"
            recommended_counts[i]+=1
    result+="</body></html>"
    return HTMLResponse(content=result)

@app.get("/survery/stats", response_class=HTMLResponse)
def get_statistics():
    result="<!DOCTYPE html><html><head><title>Statistics</title></head><body>"
    result+=f"<h3>Total surveys completed - {survery_counts}</h3>"
    result+="<h3>Number of recommendations for each career path</h3>"
    popular=max(recommended_counts)
    p_career=""
    for i in range(0,4):
        result+=f"<h5>{careers[i]} - {recommended_counts[i]}"
        if recommended_counts[i]==popular:
            p_career=careers[i]
            
    result+=f"<h2>Popular career : {p_career}</h2>"
    
    result+="</body></html>"
    return HTMLResponse(content=result)
