import requests
import json

def get_embedding(text, api_key):
    ## API Definitions
    url = "https://datathon.bindgapi.com/channel"
    headers =  {
        "X-API-Key": api_key,
        "Content-Type":"application/json"
    }
    body = { "inputs": text }
    ## API Call
    try:
        response = requests.post(url, data=json.dumps(body), headers=headers)
    except Exception:
        print(Exception)
        
    try:
        # return response 
        result = response.json()
        return json.loads(result['results'])
    except:
        print(response.status_code)
        
