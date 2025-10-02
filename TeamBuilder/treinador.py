import random
from tkinter import messagebox
import utils

def load_team_for_training(app_state, widgets):
    if not app_state['team_is_generated']:
        messagebox.showinfo("Aviso", "Você precisa gerar uma equipe primeiro!")
        return

    app_state['selected_team'] = utils.load_saved_team(app_state['saved_team_file'])
    app_state['image_references_manage'].clear()
    
    for i, pokemon_name in enumerate(app_state['selected_team']):
        (img_lbl, name_lbl, attempts_lbl, train_btn) = widgets['management_widgets'][i]
        
        photo = utils.load_pokemon_image_from_web(pokemon_name)
        app_state['image_references_manage'].append(photo)
        name_lbl.config(text=pokemon_name.capitalize())
        if photo: img_lbl.config(image=photo)
        else: img_lbl.config(image='')
        
        attempts_lbl.config(text=f"Tentativas: {app_state['training_attempts'][i]}/3")
        
        poke_data = app_state['db'].get(pokemon_name)
        if poke_data and poke_data['evolves_to'] is not None and app_state['training_attempts'][i] > 0:
            train_btn.config(state="normal")
        else:
            train_btn.config(state="disabled")

def attempt_training(app_state, widgets, slot_index):
    training_attempts = app_state['training_attempts']
    
    if training_attempts[slot_index] <= 0: return

    training_attempts[slot_index] -= 1
    
    pokemon_to_train = app_state['selected_team'][slot_index]
    
    if random.random() < 0.20:
        evolution = app_state['db'][pokemon_to_train]['evolves_to']
        messagebox.showinfo("Sucesso!", f"{pokemon_to_train.capitalize()} evoluiu para {evolution.capitalize()}!")
        app_state['selected_team'][slot_index] = evolution
        
        training_attempts[slot_index] = 3
        
        utils.save_team_to_file(app_state['selected_team'], app_state['saved_team_file'])
    else:
        messagebox.showwarning("Fracasso", f"{pokemon_to_train.capitalize()} falhou no treinamento.")
    
    load_team_for_training(app_state, widgets)
    team_power = utils.calculate_team_power(app_state['selected_team'], app_state['db'])
    widgets['power_label'].config(text=f"Poder Total da Equipe: {team_power}")