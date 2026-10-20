"""
Ce fichier permet de gérer les fichiers json, les créer, les lires, les lister, les modifier
"""
from pathlib import Path
import json

TOOLS_PATH = Path(__file__).resolve().parent
GAMES_PATH = TOOLS_PATH.parent / "Games"
FILE_ERROR = {"titre": "Impossible de charger le fichier, appuyez sur [echap] pour revenir en arrière"}

def list_jeux():
    """retourne tous les noms de fichier en .json associé à leur path dans le dossier Games"""
    fichiers_jeux={}
    for fichier in GAMES_PATH.rglob("*.json"):
        if fichier.is_file():
            fichiers_jeux[fichier.name]=fichier.resolve()
    return fichiers_jeux


def load_jeux(name):
    """retourne toute les données du fichier json ayant un nom spécifique"""
    game_files=list_jeux()
    try:
        file_path=game_files[name]
        GAMES_PATH.mkdir(parents=True, exist_ok=True)
        if not file_path.exists():
            return FILE_ERROR
        with file_path.open("r", encoding="utf-8") as game_file:
            data = json.load(game_file)
        return data
    except (OSError, json.JSONDecodeError):
        return FILE_ERROR


if __name__ == "__main__":
    # tester chaque fonction
    print(list_jeux())
    for names_jeux in list_jeux():
        print(load_jeux(names_jeux))