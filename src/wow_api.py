import requests
from config import CLIENT_ID, CLIENT_SECRET, TOKEN_URL

def get_access_token():
    response = requests.post(
        TOKEN_URL,
        auth=(CLIENT_ID, CLIENT_SECRET),
        data={"grant_type": "client_credentials"}
    )

    if response.status_code == 200:
        return response.json()["access_token"]
    else:
        raise Exception(f"Erro ao obter token: {response.status_code} - {response.text}")

from config import BLIZZARD_API_BASE_URL, NAMESPACE, LOCALE
from wow_api import get_access_token

def listar_reinos(token, regiao="us", locale="en_US"):
    url = f"https://{regiao}.api.blizzard.com/data/wow/connected-realm/index"

    params = {
        "namespace": f"dynamic-{regiao}",
        "locale": locale
    }
    headers = {
        "Authorization": f"Bearer {token}"
    }

    resposta = requests.get(url, params=params, headers=headers)
    resposta.raise_for_status()
    return resposta.json()["connected_realms"]
