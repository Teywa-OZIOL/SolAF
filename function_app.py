import azure.functions as func
import logging
import requests

app = func.FunctionApp(http_auth_level=func.AuthLevel.FUNCTION)

@app.route(route="solanamemeaf")
def solanamemeaf(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')
    
    mint_token = 0
    timestamp = 0
    description = 0
    description_name_token = 0
    try:
        request = req.get_json()
        logging.info(request)
        mint_token = request[0]["tokenTransfers"][0]["mint"]
        timestamp = request[0]["timestamp"]
        description = request[0]['description']
        description_name_token = description.split(' ')[-1][:-1]
        if description_name_token != 'tokens':
            url_4 = "https://api.solscan.io/v2/token/holders?token=" + mint_token + "&offset=0&size=10"

            headers = {
            'accept': 'application/json, text/plain, */*',
            'accept-language': 'fr-FR,fr;q=0.9,en-US;q=0.8,en;q=0.7',
            'cookie': '_ga=GA1.1.336648904.1712483576; cf_clearance=28qvlkAPHrkvQ9p3M5OFKxBYeWaEL53wdYRO2vXLGhE-1714310488-1.0.1.1-koZaE7YbaO9dV_5f2EkmLDXE47bORyU6O1n40vSk5aer8kxX8IpeKFA11ZEfMt05cylhA0RaG3BO3MqRJfFnOw; cf_clearance=MdCzAAW6XummBJWwiItOQhSTzUNpXYEQtmqqw4cXwLc-1715357433-1.0.1.1-oZsBxOY6j4kl0rs2gixaChHZyGLUbfN6MBzMLM0q76pgn6dvGWFMDxkKXZff7zK_vW1Cs.m2vcS1EjQLJkwSfw; _ga_PS3V7B7KV0=GS1.1.1715373996.7.1.1715374008.0.0.0',
            'if-none-match': 'W/"3688-pOU7pevHpi+en9tlxrsBzCOZt/o"',
            'origin': 'https://solscan.io',
            'priority': 'u=1, i',
            'referer': 'https://solscan.io/',
            'sec-ch-ua': '"Chromium";v="124", "Google Chrome";v="124", "Not-A.Brand";v="99"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-site',
            'sol-aut': 'jux1B9dls0fKo8qH89sjM0o8zbIkyy1MEiJX7Vlq',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36'
            }

            response_4 = requests.request("GET", url_4, headers=headers).json()
            logging.info("fezfezfezfezezfzfezfezfezef")
            logging.info(response_4)

    except ValueError:
        pass
    
    logging.info("mint : ", mint_token)
    logging.info("timestamp : ", timestamp)

    return func.HttpResponse("Done")


    