from fastapi import FastAPI, Request,Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

app=FastAPI()

template=Jinja2Templates(directory="templates")



@app.get("/student/reg")
def show_form(request:Request):
	return  template.TemplateResponse("form.html", {"request":request})


@app.post("/student/reg", response_class=HTMLResponse)
def submit_form(request: Request,  age:int=Form(...),  name:str=Form(...), email:str=Form(...)):
	style= f"<!DOCTYPE html><html><head><title>Student Registration</title></head><body><h1> "
	if age>=18 and age<=100:
		style+=f"Registration Successful for {name}, Email: {email}, Age : {age} </h1></body></html>"
		
	else:
		style+="Invalid age. Must be between 18 and 100</h1></body></html>"
	return HTMLResponse(content=style)
