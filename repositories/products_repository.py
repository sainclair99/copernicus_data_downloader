import os
import requests
from tqdm import tqdm
from utils import SAVE_PATH, get_save_path

def fetch_products(token:str,filter:tuple):
    search_url =  os.getenv("ODATA_API_URL")

    params = {
        "$filter": filter,
        "$orderby": "ContentDate/Start asc",
        "$top": 1000,
    }

    headers = {"Authorization": f"Bearer {token}"}
    
    response = requests.get(search_url, params=params, headers=headers).json()

    products = response["value"]

    return products


def get_product(product_id:str, token:str):
    headers = {"Authorization": f"Bearer {token}"}
    download_url = f"https://download.dataspace.copernicus.eu/odata/v1/Products({product_id})/$value"
    product = requests.get(download_url, headers=headers, stream=True)
    return product

def download_products(products:list, min_file_size:int, token:str):
    current_file = 1
    
    print(f"Le chemin de sauvegarde est : {get_save_path()}")

    for product in products:
        product_id = product["Id"]
        product_name = product["Name"]
        
        # 3. Combiner le dossier et le fichier
        file_save = os.path.join(get_save_path(), f"{product_name}.zip")
        display_name = f"{product_name}.zip"

        if os.path.exists(file_save):
            print(f"Le fichier '{display_name}' existe déjà. Téléchargement annulé.")
        else:
            r = get_product(product_id,token)

            # Récupérer la taille totale du fichier en octets
            total_size = int(r.headers.get("content-length", 0))

            # Vérifier si la taille du fichier est inférieure à la taille minimale
            if total_size < min_file_size:
                print(f"Le fichier '{display_name}' est trop petit ({total_size} octets ({total_size / (1024**2):.2f} MB)). Téléchargement annulé.")
            else:
                with open(file_save, "wb") as f, tqdm(
                    desc=f"📂[{current_file}/{len(products)}] {display_name}",
                    total=total_size,
                    unit="iB",
                    unit_scale=True,
                    unit_divisor=1024,
                ) as bar:
                    alls = r.iter_content(chunk_size=8192)
                    for chunk in alls:
                        # f.write(chunk)
                        if chunk:  # Filtrer les chunks de type "keep-alive"
                            f.write(chunk)
                            bar.update(len(chunk))  # Mettre à jour la barre avec la taille du chunk
        current_file = current_file + 1