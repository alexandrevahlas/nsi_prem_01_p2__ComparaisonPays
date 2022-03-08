from tkinter import *
from pandas import DataFrame
import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

#parametres de la fenetre
root= Tk()
root.title("Comparateur")
root.geometry("1920x1080")
root.resizable(True, True)



def exitApp():  #Pour quitter l'application
    root.destroy()

#Fonction qui comprend les fonctionnalités de la fenetre de comparaison
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

   # Fonction qui s'effectue quand un des choix est selectionnee, et va alors afficher un graphique
    def menu1(self):
        if variable.get() == "France":
            left_label.config(command = data_france())
        elif variable.get() =="Allemagne":
            left_label.config(command = data_allemagne())
        elif variable.get() =="Etats-Unis":
            left_label.config(command=data_usa ())
        elif variable.get() =="Russie":
            left_label.config(command=data_russie())
        elif variable.get() =="Chine":
            left_label.config(command=data_china())

    def menu2(self):
        if variable2.get() == "France":
            right_label.config(command = data_france())
        elif variable2.get() =="Allemagne":
            right_label.config(command = data_allemagne())
        elif variable2.get() =="Etats-Unis":
            right_label.config(command=data_usa ())
        elif variable2.get() =="Russie":
            right_label.config(command=data_russie())
        elif variable2.get() =="Chine":
            right_label.config(command=data_china())

        
    #pour creer la fenetre de comparaison
    app=tk.Tk()
    #Creation d'un frame pour organiser les widgets
    main_frame = Frame(app)
    main_frame.pack(fill=BOTH, expand=1)
    #Mise en place du canvas
    my_canvas = Canvas(main_frame)
    my_canvas.pack(side=LEFT, fill=BOTH, expand=1)
    #Mise en place du barre de scroll dans le canvas
    my_scrollbar = ttk.Scrollbar(main_frame, orient=VERTICAL, command=my_canvas.yview)
    my_scrollbar.pack(side=RIGHT, fill=Y)
    #Configuration du canvas
    my_canvas.configure(yscrollcommand=my_scrollbar.set)
    my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion = my_canvas.bbox("all")))
    second_frame = Frame(my_canvas)
    #Ajout d'une nouveau frame
    my_canvas.create_window((0,0), window=second_frame, anchor="nw")

    #Dimension de la fenetre
    app.geometry("1920x650")
    
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
  
    
# les "data2,3,4,5,6" sont des noms de variables pour que chaque fonction foncionne correctement
#Les differentes fonctions comporte les données entrées manuellement ainfi de pouvoir creer le graphique, elle sont utilisés par les menus déroulants
    def data_france ():
        #population
        data2 = {'Années': [1960,1980,2000,2020],
             'Habitants (en millions)': [46,55,61,67]
            }
        df2 = DataFrame(data2,columns=['Années','Habitants (en millions)'])

        figure2 = plt.Figure(figsize=(5,4), dpi=100)
        ax2 = figure2.add_subplot(111)
        line2 = FigureCanvasTkAgg(figure2, app)
        line2.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH)
        df2 = df2[['Années','Habitants (en millions)']].groupby('Années').sum()
        df2.plot(kind='line', legend=True, ax=ax2, color='r',marker='o', fontsize=10)
        ax2.set_title('Population')
        #PIB
        data2_1 = {'Années': [1960,1980,2000,2008,2020],
             'PIB (en milliards de dollars)': [62,701,1362 ,29180, 26030]
             }
        df2_1 = DataFrame(data2_1,columns=['Années','PIB (en milliards de dollars)'])

        figure2_1 = plt.Figure(figsize=(5,4), dpi=100)
        ax2_1 = figure2_1.add_subplot(111)
        line2_1 = FigureCanvasTkAgg(figure2_1, app)
        line2_1.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH)
        df2_1 = df2_1[['Années','PIB (en milliards de dollars)']].groupby('Années').sum()
        df2_1.plot(kind='line', legend=True, ax=ax2_1, color='y',marker='o', fontsize=10)
        ax2_1.set_title('PIB')
        
    def data_allemagne ():
        #population
        data3 = {'Années': [1960,1980,2000,2020],
             'Habitants (en millions)': [73,78,82,83]
            }
        df3 = DataFrame(data3,columns=['Années','Habitants (en millions)'])

        figure3 = plt.Figure(figsize=(5,4), dpi=100)
        ax3 = figure3.add_subplot(111)
        line3 = FigureCanvasTkAgg(figure3, app)
        line3.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH)
        df3 = df3[['Années','Habitants (en millions)']].groupby('Années').sum()
        df3.plot(kind='line', legend=True, ax=ax3, color='r',marker='o', fontsize=10)
        ax3.set_title('Population')
        
        #PIB
        data6_1 = {'Années': [1960,1980,2000,2008,2020],
             'PIB (en milliards de dollars)': [543,2857,10250 ,14710, 21000]
            }
        df6_1 = DataFrame(data6_1,columns=['Années','PIB (en milliards de dollars)'])

        figure6_1 = plt.Figure(figsize=(5,4), dpi=100)
        ax6_1 = figure6_1.add_subplot(111)
        line6_1 = FigureCanvasTkAgg(figure6_1, app)
        line6_1.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH)
        df6_1 = df6_1[['Années','PIB (en milliards de dollars)']].groupby('Années').sum()
        df6_1.plot(kind='line', legend=True, ax=ax6_1, color='y',marker='o', fontsize=10)
        ax6_1.set_title('PIB')
        
    def data_china():
        #population
        data4 = {'Années': [1960,1980,2000,2020],
             'Habitants (en millions)': [667,981,1263,1402]
            }
        df4 = DataFrame(data4,columns=['Années','Habitants (en millions)'])

        figure4 = plt.Figure(figsize=(5,4), dpi=100)
        ax4 = figure4.add_subplot(111)
        line4 = FigureCanvasTkAgg(figure4, app)
        line4.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH)
        df4 = df4[['Années','Habitants (en millions)']].groupby('Années').sum()
        df4.plot(kind='line', legend=True, ax=ax4, color='r',marker='o', fontsize=10)
        ax4.set_title('Population')
        
        #PIB
        data6_1 = {'Années': [1960,1980,2000,2008,2020],
             'PIB (en milliards de dollars)': [543,2857,10250 ,14710, 21000]
            }
        df6_1 = DataFrame(data6_1,columns=['Années','PIB (en milliards de dollars)'])

        figure6_1 = plt.Figure(figsize=(5,4), dpi=100)
        ax6_1 = figure6_1.add_subplot(111)
        line6_1 = FigureCanvasTkAgg(figure6_1, app)
        line6_1.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH)
        df6_1 = df6_1[['Années','PIB (en milliards de dollars)']].groupby('Années').sum()
        df6_1.plot(kind='line', legend=True, ax=ax6_1, color='y',marker='o', fontsize=10)
        ax6_1.set_title('PIB')
        
    def data_usa ():
        #population
        data5 = {'Années': [1960,1980,2000,2020],
             'Habitants (en millions)': [180,227,282,330]
            }
        df5 = DataFrame(data5,columns=['Années','Habitants (en millions)'])

        figure5 = plt.Figure(figsize=(5,4), dpi=100)
        ax5 = figure5.add_subplot(111)
        line5 = FigureCanvasTkAgg(figure5, app)
        line5.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH)
        df5 = df5[['Années','Habitants (en millions)']].groupby('Années').sum()
        df5.plot(kind='line', legend=True, ax=ax5, color='r',marker='o', fontsize=10)
        ax5.set_title('Population')
        #PIB
        
        data6_1 = {'Années': [1960,1980,2000,2008,2020],
             'PIB (en milliards de dollars)': [543,2857,10250 ,14710, 21000]
            }
        df6_1 = DataFrame(data6_1,columns=['Années','PIB (en milliards de dollars)'])

        figure6_1 = plt.Figure(figsize=(5,4), dpi=100)
        ax6_1 = figure6_1.add_subplot(111)
        line6_1 = FigureCanvasTkAgg(figure6_1, app)
        line6_1.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH)
        df6_1 = df6_1[['Années','PIB (en milliards de dollars)']].groupby('Années').sum()
        df6_1.plot(kind='line', legend=True, ax=ax6_1, color='y',marker='o', fontsize=10)
        ax6_1.set_title('PIB')
                
        
    
    def data_russie():
        #population
        data6 = {'Années': [1960,1980,2000,2020],
             'Habitants (en millions)': [119,139,146,144]
            }
        df6 = DataFrame(data6,columns=['Années','Habitants (en millions)'])

        figure6 = plt.Figure(figsize=(5,4), dpi=100)
        ax6 = figure6.add_subplot(111)
        line6 = FigureCanvasTkAgg(figure6, app)
        line6.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH)
        df6 = df6[['Années','Habitants (en millions)']].groupby('Années').sum()
        df6.plot(kind='line', legend=True, ax=ax6, color='r',marker='o', fontsize=10)
        ax6.set_title('Population')
        #PIB
        data6_1 = {'Années': [1960,2000,2008, 2010,2020],
             'PIB (en milliards de dollars)': [516,259,1661,1525, 1483]
            }
        df6_1 = DataFrame(data6_1,columns=['Années','PIB (en milliards de dollars)'])

        figure6_1 = plt.Figure(figsize=(5,4), dpi=100)
        ax6_1 = figure6_1.add_subplot(111)
        line6_1 = FigureCanvasTkAgg(figure6_1, app)
        line6_1.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH)
        df6_1 = df6_1[['Années','PIB (en milliards de dollars)']].groupby('Années').sum()
        df6_1.plot(kind='line', legend=True, ax=ax6_1, color='y',marker='o', fontsize=10)
        ax6_1.set_title('PIB')
       
   

    

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
