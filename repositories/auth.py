import requests
import os

def get_token(username:str,password:str):
    token_url = os.getenv("TOKEN_URL")
    
    token_data = {
        "grant_type":"password",
        "username":username,
        "password":password,
        "client_id":"cdse-public"
    }

    token = requests.post(token_url, data=token_data).json()["access_token"]

    return token