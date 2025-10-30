from fastapi import FastAPI, Request,Form
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles

app=FastAPI()
templates=Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")
orders=[]

@app.get("/order")
def display_form(request:Request):
    return templates.TemplateResponse("form3.html", {"request":request})

@app.post("/order/confirm", response_class=HTMLResponse)
def proceed_confirm(request:Request, product_price:str=Form(...), name:str=Form(..., min_length=3), quantity:int=Form(..., ge=1, le=10), address:str=Form(..., min_length=10), priority:str=Form(None)):
    result="<!DOCTYPE html><html><head><title>Order Confirmation</title></head><body><h2>Order Confirmation</h2>"
    result+="<p>Customer Name - "+name+"</p>"
    pandp=product_price.split('-')
    product=pandp[0]
    price=quantity*int(pandp[1])
    result+="<p>Product Name - "+product+"</p>"
    result+=f"<p>quantity - {quantity}</p>"
    result+="<p>Shipping address - "+address+"</p>"
    result+=f"<p>Priority shipping status :"
    if priority and priority.lower()=="priority":
        result+="Yes </p>"
        price+=50
    else:
        result+="No </p>"
    
    history={
        "name" : name,
        "product":product,
        "quantity":quantity,
        "total_price":price
    }
    global orders
    
    if(len(orders)>=5):
        
        orders=orders[1:5]

    
    orders.append(history)
    
    result+=f"<p>Total price : ${price:.2f}"
    result+="</body></html>"
    
    return HTMLResponse(content=result)

@app.get("/order/history")
def display_orders(request:Request, response_class=HTMLResponse):
    result="<!DOCTYPE html><html><head><title>History</title></head><body>"
    if len(orders) ==0:
        result+="<p>No orders yet</p>"
    else:
        result+="<table><tr><th>Name</th><th>Product</th><th>Quantity</th><th>Total Price</th></tr>"
        for o in orders:
            result+=f"<tr><td>{o["name"]}</td><td>{o["product"]}</td><td>{o["quantity"]}</td><td>{o["total_price"]}</td></tr>"
        result+="</table>"
    result+="</body></html>"
    
    return HTMLResponse(content=result)
        
    
        
    