from tkinter import *
import tkinter as tk

#parametres de la fenetre
root= Tk()
root.title("Comparateur")
root.geometry("1920x1080")
root.resizable(True, True)

def exitApp():  #Pour quitter l'application
    root.destroy()


def fenetrep (): #Création de deux menus déroulant
    OptionList = [
        "Choisir un pays",
        "France",
        "Allemagne",
        "Royaume-Uni"
        ]
    app = tk.Tk()
    app.geometry("1920x1080")
    variable = tk.StringVar(app)
    variable.set(OptionList[0])
    opt = tk.OptionMenu(app, variable, *OptionList)
    opt.config(width=90, font=('Helvetica', 12))
    opt.pack(side=TOP, anchor=NW, fill="both", expand=True)
    variable2 = tk.StringVar(app)
    variable2.set(OptionList[0])
    opt2 = tk.OptionMenu(app, variable2, *OptionList)
    opt2.config(width=90, font=('Helvetica', 12))
    opt2.pack(side=TOP, anchor=NE, fill="both", expand=True)
    


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




root.mainloop()
