import tkinter as tk
from tkinter import font
import os

import utils
import gerador
import treinador

def show_frame(frame_to_show, callback=None):
    if callback: callback()
    frame_to_show.tkraise()

SCRIPT_DIR = os.path.dirname(__file__)
POKEMON_DB_FILE = os.path.join(SCRIPT_DIR, 'pokemon_database.json')
SAVED_TEAM_FILE = os.path.join(SCRIPT_DIR, 'saved_team.json')
WINDOW_TITLE = "Pokémon Team Builder"; WINDOW_GEOMETRY = "1000x680"; COLOR_BACKGROUND = "#F5F5F5"; COLOR_SIDEBAR = "#FFFFFF"; COLOR_TEXT = "#212121"; COLOR_ACCENT = "#E3350D"; COLOR_ACCENT_HOVER = "#C32D0B"; COLOR_BORDER_INACTIVE = "#D0D0D0"; COLOR_SIDEBAR_HOVER = "#EEEEEE"; FONT_TITLE = ("Segoe UI", 26, "bold"); FONT_SUBTITLE = ("Segoe UI", 16, "bold"); FONT_BODY = ("Segoe UI", 11); FONT_POKENAME = ("Segoe UI", 10, "bold"); FONT_BUTTON = ("Segoe UI", 12, "bold")
style_constants = {"COLOR_ACCENT": COLOR_ACCENT, "COLOR_BORDER_INACTIVE": COLOR_BORDER_INACTIVE}

ALL_POKEMON_DB = utils.load_pokemon_database(POKEMON_DB_FILE)
if ALL_POKEMON_DB is None: exit()
STARTER_POOL = [name for name, data in ALL_POKEMON_DB.items() if data['stage'] == 1]

app_state = {
    "db": ALL_POKEMON_DB, "starter_pool": STARTER_POOL, "saved_team_file": SAVED_TEAM_FILE,
    "selected_team": [], "training_attempts": [3, 3, 3, 3, 3, 3], "team_is_generated": False,
    "image_references_gen": [], "image_references_manage": [], "window": None
}

window = tk.Tk(); window.title(WINDOW_TITLE); window.geometry(WINDOW_GEOMETRY); window.config(bg=COLOR_BACKGROUND); window.resizable(False, False)
app_state['window'] = window

sidebar_frame = tk.Frame(window, bg=COLOR_SIDEBAR, width=200); sidebar_frame.pack(side="left", fill="y", padx=(10, 0), pady=10); sidebar_frame.pack_propagate(False)
tk.Label(sidebar_frame, text="Navegação", font=FONT_SUBTITLE, bg=COLOR_SIDEBAR, fg=COLOR_TEXT).pack(pady=20, padx=20, anchor="w")
container = tk.Frame(window, bg=COLOR_BACKGROUND); container.pack(side="left", fill="both", expand=True); container.grid_rowconfigure(0, weight=1); container.grid_columnconfigure(0, weight=1)

generate_page = tk.Frame(container, bg=COLOR_BACKGROUND); generate_page.grid(row=0, column=0, sticky="nsew"); generate_page.grid_columnconfigure(0, weight=1); generate_page.grid_rowconfigure(0, weight=0); generate_page.grid_rowconfigure(1, weight=1); generate_page.grid_rowconfigure(2, weight=0)
tk.Label(generate_page, text="Sua Equipe Pokémon", font=FONT_TITLE, bg=COLOR_BACKGROUND, fg=COLOR_TEXT).grid(row=0, column=0, pady=(20, 10))
gen_team_frame = tk.Frame(generate_page, bg=COLOR_BACKGROUND); gen_team_frame.grid(row=1, column=0)
gen_bottom_frame = tk.Frame(generate_page, bg=COLOR_BACKGROUND); gen_bottom_frame.grid(row=2, column=0, pady=(10, 20))
gen_power_label = tk.Label(gen_bottom_frame, text="Poder Total da Equipe: 0", font=FONT_SUBTITLE, bg=COLOR_BACKGROUND, fg=COLOR_TEXT); gen_power_label.pack()
gen_action_button = tk.Button(gen_bottom_frame, text="Gerar Nova Equipe", font=FONT_BUTTON, bg=COLOR_ACCENT, fg="white", relief="flat", padx=20, pady=10, activebackground=COLOR_ACCENT_HOVER, activeforeground="white", cursor="hand2"); gen_action_button.pack(pady=10)
generation_widgets = []
for i in range(6):
    slot_frame = tk.Frame(gen_team_frame, width=160, height=190, bg=COLOR_BACKGROUND); slot_frame.grid(row=i // 3, column=i % 3, padx=15, pady=5); slot_frame.grid_propagate(False); slot_frame.grid_rowconfigure(0, weight=1); slot_frame.grid_columnconfigure(0, weight=1)
    border = tk.Frame(slot_frame, bg=COLOR_BORDER_INACTIVE); border.grid(row=0, column=0); image_label = tk.Label(border, width=140, height=140, bg="white", compound="center"); image_label.pack(padx=3, pady=3)
    name_label = tk.Label(slot_frame, text=f"Slot {i+1}", font=FONT_POKENAME, bg=COLOR_BACKGROUND, fg=COLOR_TEXT); name_label.grid(row=1, column=0, pady=4); generation_widgets.append((image_label, name_label, border))
widgets_gen = {"action_button": gen_action_button, "power_label": gen_power_label, "generation_widgets": generation_widgets}
gen_action_button.config(command=lambda: gerador.generate_team_logic(app_state, widgets_gen, style_constants))

manage_page = tk.Frame(container, bg=COLOR_BACKGROUND); manage_page.grid(row=0, column=0, sticky="nsew"); manage_page.grid_columnconfigure(0, weight=1); manage_page.grid_rowconfigure(0, weight=0); manage_page.grid_rowconfigure(1, weight=1)
tk.Label(manage_page, text="Treinar Equipe", font=FONT_TITLE, bg=COLOR_BACKGROUND, fg=COLOR_TEXT).grid(row=0, column=0, pady=(20, 10))
manage_team_frame = tk.Frame(manage_page, bg=COLOR_BACKGROUND); manage_team_frame.grid(row=1, column=0)
management_widgets = []
for i in range(6):
    slot_frame = tk.Frame(manage_team_frame, width=180, height=240, bg=COLOR_SIDEBAR_HOVER); slot_frame.grid(row=i // 3, column=i % 3, padx=15, pady=15); slot_frame.pack_propagate(False)
    img_lbl = tk.Label(slot_frame, bg="white", text="?"); img_lbl.pack(pady=5)
    name_lbl = tk.Label(slot_frame, text=f"Slot {i+1}", font=FONT_POKENAME, bg=COLOR_SIDEBAR_HOVER); name_lbl.pack()
    attempts_lbl = tk.Label(slot_frame, text="Tentativas: -/3", font=FONT_BODY, bg=COLOR_SIDEBAR_HOVER); attempts_lbl.pack(pady=5)
    train_btn = tk.Button(slot_frame, text="Treinar", font=FONT_BODY, state="disabled", command=lambda index=i: treinador.attempt_training(app_state, widgets_manage, index)); train_btn.pack(pady=5)
    management_widgets.append((img_lbl, name_lbl, attempts_lbl, train_btn))
widgets_manage = {"management_widgets": management_widgets, "power_label": gen_power_label}

nav_button_style = {"font": FONT_BODY, "bg": COLOR_SIDEBAR, "fg": COLOR_TEXT, "relief": "flat", "anchor": "w", "padx": 20, "pady": 10, "activebackground": COLOR_SIDEBAR_HOVER, "activeforeground": COLOR_TEXT, "cursor": "hand2"}
tk.Button(sidebar_frame, text="▶ Gerar Equipe", **nav_button_style, command=lambda: show_frame(generate_page)).pack(fill="x")
tk.Button(sidebar_frame, text="▶ Treinar Equipe", **nav_button_style, command=lambda: show_frame(manage_page, lambda: treinador.load_team_for_training(app_state, widgets_manage))).pack(fill="x")

show_frame(generate_page)
window.mainloop()