# hello_world.py

import tkinter as tk
from constantes import HELLO_WORLD_TITLE, HELLO_WORLD_TEXT

def fonction_principale():
    # Création de la fenêtre
    fenetre = tk.Tk()
    fenetre.title(HELLO_WORLD_TITLE)
<<<<<<< HEAD
    fenetre.geometry("400x400")

=======
    fenetre.geometry("200x200")
    fenetre.configure(bg="green")  # Fond d’écran vert
>>>>>>> 96cd0cf (C6 : couleur de fond en vert (fix_C5))
    
    # Création du label de texte
    label = tk.Label(fenetre, text=HELLO_WORLD_TITLE, fg="yellow", bg="black")
    label.pack(expand=True)  # Centrage vertical et horizontal
    
    # Finalisation
    fenetre.mainloop()

# Appel de la fonction principale
if __name__ == "__main__":
    fonction_principale()
