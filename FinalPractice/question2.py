from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

app=FastAPI()
templates=Jinja2Templates(directory="templates")
@app.get("/")
def show_form(request:Request):
    return templates.TemplateResponse("form2.html", {"request":request});


@app.post("/convert")
def convert_temp(request:Request, temp:int=Form(..., ge=20),c_type:str=Form(...)):
    result="<!DOCTYPE html><html><head><title>Temperature conversion</title></head><body><h1>"
    if c_type=="C2F":
        converted=temp*9/5+32
        result+=f"Result: {temp}° Celsius= {converted}° Fahrenheit"
    else:
        converted=(temp-32)*5/9
        result+=f"Result: {temp}° Fahrenheit= {converted}° Celsius"
    result+="</h1></body></html>"
    return HTMLResponse(content=result)




    