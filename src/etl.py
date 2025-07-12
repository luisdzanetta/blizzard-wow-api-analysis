import time
import pandas as pd
from wow_api import (
    get_access_token,
    fetch_mount_index,
    fetch_mount_details,
    fetch_pet_index,
    fetch_pet_details
)

def extract_mounts(token, max_items=None):
    """Extrai dados de montarias da API Blizzard."""
    index_data = fetch_mount_index(token)
    mounts = index_data.get("mounts", [])

    details = []
    for i, mount in enumerate(mounts):
        if max_items and i >= max_items:
            break
        try:
            data = fetch_mount_details(mount["id"], token)
            details.append({
                "id": data["id"],
                "name": data["name"],
                "source_type": data["source"]["type"] if data.get("source") else None,
                "source_name": data["source"]["name"] if data.get("source") else None,
                "faction": data.get("faction", {}).get("name")
            })
            time.sleep(0.1)  # respeita a API
        except Exception as e:
            print(f"Erro ao buscar montaria {mount['id']}: {e}")
    return pd.DataFrame(details)

def extract_pets(token, max_items=None):
    """Extrai dados de mascotes da API Blizzard."""
    index_data = fetch_pet_index(token)
    pets = index_data.get("pets", [])

    details = []
    for i, pet in enumerate(pets):
        if max_items and i >= max_items:
            break
        try:
            data = fetch_pet_details(pet["id"], token)
            details.append({
                "id": data["id"],
                "name": data["name"],
                "source_type": data["source"]["type"] if data.get("source") else None,
                "source_name": data["source"]["name"] if data.get("source") else None
            })
            time.sleep(0.1)
        except Exception as e:
            print(f"Erro ao buscar pet {pet['id']}: {e}")
    return pd.DataFrame(details)

def run_etl():
    print("Obtendo token de acesso...")
    token = get_access_token()

    print("Coletando dados de montarias...")
    df_mounts = extract_mounts(token)
    df_mounts.to_csv("data/processed/mounts.csv", index=False)
    print(f"{len(df_mounts)} montarias salvas em data/processed/mounts.csv")

    print("Coletando dados de mascotes...")
    df_pets = extract_pets(token)
    df_pets.to_csv("data/processed/pets.csv", index=False)
    print(f"{len(df_pets)} mascotes salvos em data/processed/pets.csv")

if __name__ == "__main__":
    run_etl()