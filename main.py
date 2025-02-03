from fastapi import FastAPI, HTTPException, Query
import requests
from operations import get_property, is_perfect_number, is_prime_number, digit_sum
from fastapi.responses import JSONResponse
import uvicorn
import os


app = FastAPI()


def get_fun_fact(number):
    url = f"http://numbersapi.com/{number}/math"

    try:
        response = requests.get(url)
        return response.text
    
    except requests.RequestException as e:  
        return f"error: {e}"

@app.get('/')
def error_message():
    return {
            "number": "alphabet",
            "error": True
    }
    
@app.get('/api/classify-number')
def classify_number(number: int = Query(None)):
    if number is None:
        data={
            "number": "alphabet",
            "error": True
        }

        return data

    try:
        is_prime = is_prime_number(number)
        is_perfect = is_perfect_number(number)
        property = get_property(number)
        sum = digit_sum(number)
        fun_fact = get_fun_fact(number)
        
        data =  {
            "number": number,
            "is_prime": is_prime,
            "is_perfect": is_perfect,
            "properties": property,
            "digit_sum": sum,  
            "fun_fact": fun_fact
        }
        return JSONResponse(content=data)
    
    except:
        raise HTTPException(
            status_code=400,
            detail={
                "number": "alphabet",
                "error": True
            }
        )
    
if __name__ == "__main__":
    
    port = int(os.getenv("PORT", 5000))
        
        # Run the app with uvicorn
    uvicorn.run(
        app,
        host="0.0.0.0",  
        port=port
    )