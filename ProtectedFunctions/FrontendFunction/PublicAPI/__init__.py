import logging
import azure.functions as func
import requests
import os

def get_bearer_token(resource_uri):
    identity_endpoint = os.environ["IDENTITY_ENDPOINT"]
    identity_header = os.environ["IDENTITY_HEADER"]
    token_auth_uri = f"{identity_endpoint}?resource={resource_uri}&api-version=2019-08-01"
    head_msi = {'X-IDENTITY-HEADER':identity_header}

    resp = requests.get(token_auth_uri, headers=head_msi)
    access_token = resp.json()['access_token']

    return access_token


def main(req: func.HttpRequest) -> func.HttpResponse:
        
        #Replace the URL with the URL from your Backend Function App
        access_token = get_bearer_token('https://azureblogging-backend.azurewebsites.net')
        headers = {'Authorization': 'Bearer '+access_token}
        
        #Replace the URL with the URL from your Backend Function SecretAPI.
        r = requests.get('https://azureblogging-backend.azurewebsites.net/api/SecretAPI', headers=headers)
        response_text = ""

        if r.status_code==200:
                response_text = r.text
        else:
                response_text = "There was a failure, response code: " + r.status_code.__str__() +  "\n\n" + r.text
        
        return func.HttpResponse(
            "This message is generated from our PublicAPI in the Frontend Function. \n"+ response_text,
            status_code=200    
        )


