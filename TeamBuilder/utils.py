import os
import json
import requests
import io
from tkinter import messagebox
from PIL import Image, ImageTk

def load_pokemon_database(file_path):
    if not os.path.exists(file_path):
        messagebox.showerror("Erro Crítico", f"Arquivo de banco de dados '{file_path}' não encontrado!")
        return None
    with open(file_path, 'r', encoding='utf-8') as f:
        return json.load(f)

def save_team_to_file(team, file_path):
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(team, f, indent=4)

def load_saved_team(file_path):
    if not os.path.exists(file_path):
        return []
    with open(file_path, 'r', encoding='utf-8') as f:
        return json.load(f)

def load_pokemon_image_from_web(pokemon_name, size=(125, 125)):
    url = f"https://img.pokemondb.net/artwork/large/{pokemon_name.lower()}.jpg"
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status() 
        image_data = io.BytesIO(response.content)
        pil_image = Image.open(image_data).resize(size, Image.Resampling.LANCZOS)
        return ImageTk.PhotoImage(pil_image)
    except requests.exceptions.RequestException:
        return None

def calculate_team_power(team, db):
    return sum(db.get(pokemon, {}).get("power", 0) for pokemon in team)