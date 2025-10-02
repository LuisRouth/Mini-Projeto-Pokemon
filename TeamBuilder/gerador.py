import time
import random
import utils

def generate_team_logic(app_state, widgets, style_constants):
    action_button = widgets['action_button']
    power_label = widgets['power_label']
    generation_widgets = widgets['generation_widgets']

    action_button.config(state="disabled")

    animation_duration = 1.5
    start_time = time.time()
    while time.time() - start_time < animation_duration:
        for image_label, name_label, border in generation_widgets:
            random_name = random.choice(app_state['starter_pool']).capitalize()
            image_label.config(image='')
            name_label.config(text=random_name)
            border.config(bg=style_constants['COLOR_BORDER_INACTIVE'])
            app_state['window'].update()
        time.sleep(0.05)

    app_state['selected_team'] = random.sample(app_state['starter_pool'], 6)
    app_state['training_attempts'] = [3, 3, 3, 3, 3, 3]
    app_state['team_is_generated'] = True
    utils.save_team_to_file(app_state['selected_team'], app_state['saved_team_file'])
    
    team_power = utils.calculate_team_power(app_state['selected_team'], app_state['db'])
    power_label.config(text=f"Poder Total da Equipe: {team_power}")
    app_state['image_references_gen'].clear()
    
    for (image_label, name_label, border), pokemon_name in zip(generation_widgets, app_state['selected_team']):
        photo = utils.load_pokemon_image_from_web(pokemon_name)
        app_state['image_references_gen'].append(photo)
        name_label.config(text=pokemon_name.capitalize())
        if photo:
            image_label.config(image=photo)
            border.config(bg=style_constants['COLOR_ACCENT'])
        else:
            image_label.config(image='')
            name_label.config(text=f"{pokemon_name.capitalize()}\n(Falha)")
    
    action_button.config(text="Equipe Definida!")