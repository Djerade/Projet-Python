from django.template import loader
from django.shortcuts import render
from django.http import HttpResponse

# Modules
import random

from app.Model.list_matier import ListUe
from app.Model.classMatier import Matier

# varaibles globales
list_ues = ListUe()
emploi_temps_semain= []   
emploi_temps_global= [] 

jours = ["Lundi", "Mardi", "Mercredi", "Jeudi","Vendredi", "Samedi" ]

def enregistrement(list_ue):
   i = 1
   while(i == 1):
      ue = Matier()
      print("-----nouvelle matière ------")
      ue.titre = input("titre: ")
      ue.credit = int(input("crédit: "))
      ue.heure =int(input("heure: "))
      list_ue.add_matier(ue)
      print("une autre matier ? 1 == oui /  0 == Non")
      i = int(input())

# Cette fonction retourne le nombre max de semaine
def estimation_duree():
    heure_par_semaine = 54
    heure_total=0
    for ue in list_ues.get_list():
        heure_total += ue.heure
    nbre_semaine = heure_total/heure_par_semaine
    if isinstance(nbre_semaine, float):
        return round(nbre_semaine) + 1
    else:
        return nbre_semaine

   

    #  print("semaine estimée")
    #  print(estimation_duree())
    
    
def main():
    for i in  range(0, estimation_duree()):
        for jour in  jours:
            martierjournee = []
            for i in range(0, 3):
                ue_choose = random.choice(list_ues.get_list())
                if(ue_choose.heure > 0):
                    martierjournee.append(ue_choose)
                    if (ue_choose.heure <= 3 ):  
                        for ue in list_ues.get_list():
                            if(ue_choose.titre == ue.titre):
                                ue.update_time(ue_choose.heure)

                    else:
                        for ue in list_ues.get_list():
                            if(ue_choose.titre == ue.titre):
                                ue.update_time(ue_choose.heure)
                                # print('heure restant ', ue_choose.heure)
                else:
                    print('temps ecoulé ')       
            emploi_temps_semain.append({
                "nom_jour": jour,
                "ue_jour": martierjournee
            })



        emploi_temps_global.append(emploi_temps_semain)
    
    
    for x in  emploi_temps_semain:
        print("---" + x['nom_jour']+ "---")
        for ue in x['ue_jour']:
            print("-", ue.titre ," ", ue.heure )
        
        


            
def app(request):
    # main()
    # enregistrement(list_ues)
    # main()
    # if list_ues.size_list() != 0 :
    #     template = loader.get_template('index.html')
    #     context = {
    #         "emploi_temps_global": emploi_temps_global
    #     }
    #     # for i in emploi_temps_global:
    #     #     context["semaines"] = i
            
    #     return HttpResponse(template.render(context, request))
        
    # else:
         template = loader.get_template('index.html')
         return HttpResponse(template.render())