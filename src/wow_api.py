import requests
from config import CLIENT_ID, CLIENT_SECRET, TOKEN_URL, BLIZZARD_API_BASE_URL, NAMESPACE, LOCALE

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

def fetch_mount_index(token):
    url = f"{BLIZZARD_API_BASE_URL}/data/wow/mount/index"
    headers = {"Authorization": f"Bearer {token}"}
    params = {"namespace": NAMESPACE, "locale": LOCALE}
    response = requests.get(url, headers=headers, params=params)
    response.raise_for_status()
    return response.json()

def fetch_mount_details(mount_id, token):
    url = f"{BLIZZARD_API_BASE_URL}/data/wow/mount/{mount_id}"
    headers = {"Authorization": f"Bearer {token}"}
    params = {"namespace": NAMESPACE, "locale": LOCALE}
    response = requests.get(url, headers=headers, params=params)
    response.raise_for_status()
    return response.json()

def fetch_pet_index(token):
    url = f"{BLIZZARD_API_BASE_URL}/data/wow/pet/index"
    headers = {"Authorization": f"Bearer {token}"}
    params = {"namespace": NAMESPACE, "locale": LOCALE}
    response = requests.get(url, headers=headers, params=params)
    response.raise_for_status()
    return response.json()

def fetch_pet_details(pet_id, token):
    url = f"{BLIZZARD_API_BASE_URL}/data/wow/pet/{pet_id}"
    headers = {"Authorization": f"Bearer {token}"}
    params = {"namespace": NAMESPACE, "locale": LOCALE}
    response = requests.get(url, headers=headers, params=params)
    response.raise_for_status()
    return response.json()
