from fastapi import FastAPI, HTTPException, Depends, Query
import requests
from typing import Dict
from pydantic import BaseModel
from fastapi.security import OAuth2PasswordBearer

# Initialize the FastAPI app
app = FastAPI()

# FatSecret API Credentials
CLIENT_ID = "4dd005b1bb5f42efa6984556469b93b4"
CLIENT_SECRET = "af55f5d5799c4395a9cd2d7487bfa78d"
TOKEN_URL = "https://oauth.fatsecret.com/connect/token"
SEARCH_URL= "https://platform.fatsecret.com/docs/v3/foods.search"

# OAuth2 for authentication
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

class TokenResponse(BaseModel):
    access_token: str
    token_type: str
    expires_in: int

# Function used to get the OAuth 2.0 Token
def get_access_token() -> str:
    headers = {"Content-Type": "application/x-www-form-urlencoded"}
    data = {
        "grant_type": "client_credentials",
        "client_id": CLIENT_ID,
        "client_secret": CLIENT_SECRET,
        "scope": "basic"
    }

    response = requests.post(TOKEN_URL, headers=headers, data=data)

    print(f"Token Request Status Code: {response.status_code}")
    print(f"Token Response Content: {response.text}")
    
    if response.status_code != 200:
        raise HTTPException(status_code=response.status_code, detail="Failed to get access token")
    
    try:
        token_data = response.json()
        return token_data["access_token"]
    except requests.exceptions.JSONDecodeError:
        raise HTTPException(status_code=500, detail="Invalid response from FatSecret API. Check credentials or API status.")

get_access_token()

# print(f"access token{get_access_token()}")
query = "ABC"

# Food Search Endpoint
@app.get("/search_food", summary="Search for food items")
async def search_food(query: str = Query(..., description="Enter the food name to search"), 
                      token: str = Depends(get_access_token)):    
    params = {
        "method": "foods.search",
        "search_expression": query,
        "format": "json"
    }
    headers = {"Authorization": f"Bearer {token}"}

    response = requests.get(SEARCH_URL, headers=headers, params=params)

    # Debugging - Print the response before parsing JSON
    print("Food Search Status Code:", response.status_code)
    print("Food Search Response Content:", response.text)

    if response.status_code != 200:
        raise HTTPException(status_code=response.status_code, detail="Failed to fetch food data")

    try:
        return response.json()
    except requests.exceptions.JSONDecodeError:
        raise HTTPException(status_code=500, detail="Invalid response from FatSecret API. Check API request format.")


search_food(query= "Apple")
# print(f"search_food  {search_food(query="Apple")}")

# Root endpoint
@app.get("/", summary="Root API check")
async def root():
    return {"message": "FatSecret API Integration with FastAPI is running!"}