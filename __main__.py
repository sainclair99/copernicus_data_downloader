import os
import repositories.auth as auth
import data_filter as df
import repositories.products_repository as pr
from dotenv import load_dotenv
import utils

def main():
    # Load the environment variables from the .env file
    load_dotenv()

    # Copernicus user credentials in .env file
    username = os.getenv("AUTH_USERNAME")
    password = os.getenv("AUTH_PASSWORD")

    # 1. Obtenir un token
    token = auth.get_token(username=username,password=password)

    if token is None:
        print("🟥 Erreur lors de l'authentification !")
    else:
        utils.setPath(None, is_s1=False)  # Définir le chemin de sauvegarde pour les fichiers téléchargés (None signifie utiliser le dossier par défaut "downloaded_files")

        # 2. Interroger l'API OData
        products = pr.fetch_products(token, df.s2_full_filter)

        min_file_size = 400 * (1024**2)  # 400 MB (Taille minimale pour lancer le téléchargement d'un fichier)

        # 3. Télécharger chaque produit
        pr.download_products(products, min_file_size, token)

if __name__ == "__main__" :
    main()