from tkinter import *
import tkinter as tk
from tkinter import ttk
import numpy as np
import matplotlib.pyplot as plt

#parametres de la fenetre
root= Tk()
root.title("Comparateur")
root.geometry("1920x1080")
root.resizable(True, True)


def data_allemagne():
    #population
    x = np.array([1960, 1980, 2000, 2020])
    y = np.array([73, 78, 82, 83])
    plt.plot(x, y)
    plt.title ("Population")
    plt.xlabel("Années")
    plt.ylabel("Habitants (en millions")
    plt.show() # affiche la figure a l'ecran
    #PIB
    x = np.array([1960, 1980, 2000, 2008, 2020])
    y = np.array([543, 2857,10250, 14710,20940])
    plt.plot(x, y)
    plt.title ("PIB")
    plt.xlabel("Années")
    plt.ylabel("PIB (en milliars de dollars)")
    plt.show() # affiche la figure a l'ecran
    

def data_france():
    #population
    x = np.array([1960, 1980, 2000, 2020])
    y = np.array([46,55 ,61,67])
    plt.plot(x, y)
    plt.title ("Population")
    plt.xlabel("Années")
    plt.ylabel("Habitants (en millions")
    plt.show() # affiche la figure a l'ecran
    #PIB
    x = np.array([1970, 1980, 2000, 2008, 2020])
    y = np.array([215, 250,1943, 3730,3806])
    plt.plot(x, y)
    plt.title ("PIB")
    plt.xlabel("Années")
    plt.ylabel("PIB (en milliars de dollars)")
    plt.show() # affiche la figure a l'ecran
    
def data_usa  ():
    #population
    x = np.array([1960, 1980, 2000, 2020])
    y = np.array([667,981 ,1253,1402])
    plt.plot(x, y)
    plt.title ("Population")
    plt.xlabel("Années")
    plt.ylabel("Habitants (en millions")
    plt.show() # affiche la figure a l'ecran
    #PIB
    x = np.array([1960, 1980, 2000, 2008, 2020])
    y = np.array([60, 191,1211, 4594, 14720])
    plt.plot(x, y)
    plt.title ("PIB")
    plt.xlabel("Années")
    plt.ylabel("PIB (en milliars de dollars)")
    plt.show() # affiche la figure a l'ecran


def data_russie():
    #population
    x = np.array([1960, 1980, 2000, 2008, 2020])
    y = np.array([62, 701,1362, 2918,2603])
    plt.plot(x, y)
    plt.title ("PIB")
    plt.xlabel("Années")
    plt.ylabel("PIB (en milliars de dollars)")
    plt.show() # affiche la figure a l'ecran
    #PIB
    x = np.array([1990, 2000, 2008, 2020])
    y = np.array([554, 259, 1661,1483])
    plt.plot(x, y)
    plt.title ("PIB")
    plt.xlabel("Années")
    plt.ylabel("PIB (en milliars de dollars)")
    plt.show() # affiche la figure a l'ecran
    

def data_chine ():
    #population
    x = np.array([1960, 1980, 2000, 2020])
    y = np.array([120,139 ,146,144])
    plt.plot(x, y)
    plt.title ("Population")
    plt.xlabel("Années")
    plt.ylabel("Habitants (en millions")
    plt.show() # affiche la figure a l'ecran
    #PIB
    x = np.array([1990, 2000, 2008, 2020])
    y = np.array([554, 259, 1661,1483])
    plt.plot(x, y)
    plt.title ("PIB")
    plt.xlabel("Années")
    plt.ylabel("PIB (en milliars de dollars)")
    plt.show() # affiche la figure a l'ecran
    



    
    

def exitApp():  #Pour quitter l'application
    root.destroy()


def fenetrep ():
    #Liste pour les choix de Pays
    OptionList = [
        "Choisir un pays",
        "France",
        "Allemagne",
        "Etats-Unis",
        "Russie",
        "Chine",
        ]

   # Texte qui s'affiche quand un des choix est selectionne
    def menu1(self):
        if variable.get() == "France":
            left_label.config(data_france())
            
        elif variable.get() =="Allemagne":
            left_label.config(data_allemagne())
        elif variable.get() =="Etats-Unis":
            left_label.config(data_usa())
        elif variable.get() =="Russie":
            left_label.config(data_russie())
        elif variable.get() =="Chine":
            left_label.config(data_chine())
       
    def menu2(self):
        if variable2.get() == "France":
            right_label.config(data_france())
        elif variable2.get() =="Allemagne":
            right_label.config(data_allemagne())
        elif variable2.get() =="Etats-Unis":
            right_label.config(data_usa())
        elif variable2.get() =="Russie":
            right_label.config(data_russie())
        elif variable2.get() =="Chine":
            right_label.config(data_chine())
       
        
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
    
    opt = tk.OptionMenu(second_frame, variable, *OptionList, command=menu1)
    opt.config(width=90, font=('Helvetica', 12))
    opt.grid(column=0, row=0, padx=50)
    
    variable2 = tk.StringVar(app)
    variable2.set(OptionList[0])
    
    opt2 = tk.OptionMenu(second_frame, variable2, *OptionList, command=menu2)
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
                               "Toutes les données utilisés viennent de l'OCDE, du site de la banque nationale\n"
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