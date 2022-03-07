# Comparateur de Pays
#
# Alexandre Vahlas  Hugo Youf
#
# Ce programme permet de comparer des donnés nationales parmis plusieurs pays, plus de contenu sera ajouté au fil du temps.
#
# Ce projet original cherche a se differencier d'autre programme de traitement de "data" qui seront proposés. Les differentes parties du projets ont été séparés en deux, une partie IHM par Alexandre Vahlas et une partie pandas par Hugo Youf sur le traitement de données l'IHM a été effectué en premier pour laisser place ensuite aux donnés 
#
# La fonction principale qui ouvre le fenetre de comparaison "fenetrep" consiste de deux menu deroulants, fonctions "menu1" et "menu2" qui vont ensuite afficher les differentes "data" des pays
#
# Le programme fonctionne a condition d'avoir pandas, matplotlib et tkinter
#
# La realisation du programme fut compliqués pour trouver des données a cause d'un bug sur le site de l'OCDE n'affichant pas les pays recherchées
#
# Source : https://donnees.banquemondiale.org/
#
# Pays disponible : France, Etats-Unis, Chine, Allemagne, Russie
#
# Donnés utilisés : 
# - Population
# - Education : https://data.oecd.org/fr/france.htm#profile-education
# - PIB : 
# - RNT : https://data.oecd.org/fr/natincome/revenu-national-net.htm#indicator-chart
# - Impot sur le revenu : https://data.oecd.org/fr/inequality/inegalite-de-revenu.htm
# - Emmision de CO2 : https://data.oecd.org/fr/air/emissions-de-ges-et-de-polluants-de-l-air.htm
# - Emplois : https://data.oecd.org/fr/france.htm#profile-jobs
