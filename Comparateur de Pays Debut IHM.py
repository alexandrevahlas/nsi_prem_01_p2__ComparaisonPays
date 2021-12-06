from tkinter import *

#parametres de la fenetre
root= Tk()
root.title("Comparateur")
root.geometry("1024x786")
root.resizable(True, True)

def comp():
    #fenetre de comparaison
    top = Toplevel()
    #pour mettre cette fenetre devant l'autre
    top.attributes('-topmost', True)
    window_width = 1024
    window_height = 786
    #dimension de la fenetre
    screen_width = top.winfo_screenwidth()
    screen_height = top.winfo_screenheight()
    #trouver le point central
    center_x = int(screen_width/2 - window_width / 2)
    center_y = int(screen_height/2 - window_height / 2)

def info():
    #fenetre d'acceuil
    top = Toplevel()
    #pour mettre cette fenetre devant l'autre
    top.attributes('-topmost', True)
    window_width = 1024
    window_height = 786
    #dimension de la fenetre
    screen_width = top.winfo_screenwidth()
    screen_height = top.winfo_screenheight()
    #trouver le point central
    center_x = int(screen_width/2 - window_width / 2)
    center_y = int(screen_height/2 - window_height / 2)
    #les instrutions ecrite
    imp = Label(top, text="Bienvenue dans le Comparateur de Pays \n"
                               "Si vous avez un probleme, regardez l'erreur affichée dans la console. \n"
                               "\n"
                               "Ce projet a été fait pas Alexandre Vahlas et Hugo Youf.\n"
                               "\n"
                               "Toutes les données utilisés viennent de l'OCDE.\n"
                               "Les données actuels sont :\n"
                               "PIB, Population\n"
                               "\n"
                               "Si vous souhaitez retourner a l'ecran principal appuyez sur 'Continuer'\n" )
    imp.grid(row=0, column=0, padx=200, pady=200)
    #button pour quitter
    extBtn = Button(top, text="Continuer", command=exitBtn).grid(row=1, column=0)

# Creation d'un menu
menubar = Menu(root) 
menu1 = Menu(menubar, tearoff=0)
menu1.add_command(label="Nouvelle Comparaison", command=comp)
menu1.add_command(label="Information", command=info)
menu1.add_separator()
menu1.add_command(label="Quitter", command=root.quit)
menubar.add_cascade(label="Menu", menu=menu1)
root.config(menu=menubar)


