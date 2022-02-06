from tkinter import *
import tkinter as tk
from tkinter import ttk

#parametres de la fenetre
root= Tk()
root.title("Comparateur")
root.geometry("1920x1080")
root.resizable(True, True)



def exitApp():  #Pour quitter l'application
    root.destroy()


def fenetrep ():
    #Liste pour les choix de Pays
    OptionList = [
        "Choisir un pays",
        "France",
        "Allemagne",
        "Royaume-Uni",
        "Etats-Unis",
        "Russie",
        "Chine",
        "Australie",
        "Mexique",
        "Bresil",
        ]

   # Texte qui s'affiche quand un des choix est selectionne
    def show(self):
        if variable.get() == "France":
            left_label.config(text="france")
        elif variable.get() =="Allemagne":
            left_label.config(text="allamagne")
        elif variable.get() =="Royaume-Uni":
            left_label.config(text="Royaume Ouni ")
        elif variable.get() =="Etats-Unis":
            left_label.config(text="Etat-Uni ")
        elif variable.get() =="Russie":
            left_label.config(text="Russieeaaa")
        elif variable.get() =="Chine":
            left_label.config(text="The wok")
        elif variable.get() =="Australie":
            left_label.config(text="Astralia")
        elif variable.get() =="Mexique":
            left_label.config(text="Mexico")
        elif variable.get() =="Bresil":
            left_label.config(text="Brasil")
    def show2(self):
        if variable2.get() == "France":
            right_label.config(text="france")
        elif variable2.get() =="Allemagne":
            right_label.config(text="allamagneh")
        elif variable2.get() =="Royaume-Uni":
            right_label.config(text="Royaume-Uno")
        elif variable2.get() =="Etats-Unis":
            right_label.config(text="Etat-Uni ")
        elif variable2.get() =="Russie":
            right_label.config(text="Russieeaaa")
        elif variable2.get() =="Chine":
            right_label.config(text="The wok")
        elif variable2.get() =="Australie":
            right_label.config(text="Astralia")
        elif variable2.get() =="Mexique":
            right_label.config(text="Mexico")
        elif variable2.get() =="Bresil":
            right_label.config(text="Brasil")
        
    #pour creer la fenetre de comparaison
    app=tk.Tk()
    #Creation d'un frame pour organiser les widgets
    main_frame = Frame(app)
    main_frame.pack(fill=BOTH, expand=1)
    #Mise en place du canvas
    my_canvas = Canvas(main_frame)
    my_canvas.pack(side=LEFT, fill=BOTH, expand=1)
    #Pour scroll
    my_scrollbar = ttk.Scrollbar(main_frame, orient=VERTICAL, command=my_canvas.yview)
    my_scrollbar.pack(side=RIGHT, fill=Y)
    #Configuration du canvas
    my_canvas.configure(yscrollcommand=my_scrollbar.set)
    my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion = my_canvas.bbox("all")))
    second_frame = Frame(my_canvas)
    #Ajout d'une nouveau frame
    my_canvas.create_window((0,0), window=second_frame, anchor="nw")


    app.geometry("1920x1080")
    
    #Création de deux menus déroulant
    variable = tk.StringVar(app)
    variable.set(OptionList[0])
    
    opt = tk.OptionMenu(second_frame, variable, *OptionList, command=show)
    opt.config(width=90, font=('Helvetica', 12))
    opt.grid(column=0, row=0, padx=50)
    
    variable2 = tk.StringVar(app)
    variable2.set(OptionList[0])
    
    opt2 = tk.OptionMenu(second_frame, variable2, *OptionList, command=show2)
    opt2.config(width=90, font=('Helvetica', 12))
    opt2.grid(column=1, row=0)

    left_label = Label(second_frame, text="")
    left_label.grid(column=0, row=1)
    right_label = Label(second_frame, text="")
    right_label.grid(column=1, row=1)
   

    

def info():
    #fenetre d'informations
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

def exitBtn ():  #Pour le boutton continuer
    info.destroy()

# Creation d'un menu
menubar = Menu(root) 
menu1 = Menu(menubar, tearoff=0)
menu1.add_command(label="Nouvelle Comparaison", command=fenetrep)
menu1.add_command(label="Information", command=info)
menu1.add_separator()
menu1.add_command(label="Quitter", command=exitApp)
menubar.add_cascade(label="Menu", menu=menu1)
root.config(menu=menubar)



#Boucle pour verifier les interactions
root.mainloop()
