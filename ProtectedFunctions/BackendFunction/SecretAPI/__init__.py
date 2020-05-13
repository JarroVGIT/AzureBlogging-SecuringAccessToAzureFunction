import logging
import azure.functions as func


def main(req: func.HttpRequest) -> func.HttpResponse:
    
    return func.HttpResponse(
            "\nThis message is from our Secret API in the Backend Function.",
            status_code=200
    )
