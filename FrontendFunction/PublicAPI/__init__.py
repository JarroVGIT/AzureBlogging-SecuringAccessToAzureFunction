import logging
import azure.functions as func
import requests

def main(req: func.HttpRequest) -> func.HttpResponse:
    
    response = requests.get('https://azureblogging-backend.azurewebsites.net/api/SecretAPI').text

    return func.HttpResponse(
            "This message is generated from our PublicAPI in the Frontend Function. \n"+ response,
            status_code=200
    )


