import os

SAVE_PATH = None

def setPath(path:str|None, is_s1:bool):
    """
    Identifie le chemin de sauvegarde pour les fichiers téléchargés. Si aucun chemin n'est fourni, le dossier par défaut "downloaded_files" sera utilisé dans le répertoire courant. Le paramètre is_s1 détermine si le suffixe du dossier sera "Sentinel-1" ou "Sentinel-2".
    """
    # On indique à Python qu'on veut modifier la variable globale tout en haut
    global SAVE_PATH 

    base_dir = f"{os.getcwd()}\\downloaded_files" if path is None else path  # Si aucun chemin n'est fourni, utiliser le dossier "downloaded_files" dans le répertoire courant, sinon utiliser le chemin fourni

    suffix = "Sentinel-1" if is_s1 else "Sentinel-2" # Si is_s1 est True, le suffixe sera "Sentinel-1", sinon ce sera "Sentinel-2"

    SAVE_PATH = os.path.join(base_dir, suffix)  # combiner le chemin de base avec le suffixe pour créer le chemin complet

    # 2. Créer le dossier automatiquement s'il n'existe pas
    if not os.path.exists(SAVE_PATH):
        os.makedirs(SAVE_PATH, exist_ok=True)

def get_save_path():
    """
    Retourne le chemin de sauvegarde pour les fichiers téléchargés. Si aucun chemin n'a été défini, retourne None.
    """
    return SAVE_PATH