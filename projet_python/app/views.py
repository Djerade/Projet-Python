from django.template import loader
from django.shortcuts import render
from django.http import HttpResponse

# Modules
import random

from app.Model.list_matier import ListUe
from app.Model.classMatier import Matier

# varaibles globales
list_ues = ListUe()
  
emploi_temps_global= [] 

jours = ["Lundi", "Mardi", "Mercredi", "Jeudi","Vendredi", "Samedi" ]

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


    
def generate():
    list_ues_copy = list_ues
    for i in  range(0, estimation_duree()):
        emploi_temps_semain= [] 
        for k in  range(0,len(jours)):
            martierjournee = []
            for j in range(0, 3):
                ue_choose = random.choice(list_ues_copy.get_list())
                if(ue_choose.heure > 0):
                    martierjournee.append(ue_choose)
                    if (ue_choose.heure <= 3 ):  
                        for ue in list_ues_copy.get_list():
                            if(ue_choose.titre == ue.titre):
                                ue.update_time(ue_choose.heure)

                    else:
                        for ue in list_ues_copy.get_list():
                            if(ue_choose.titre == ue.titre):
                                ue.update_time(ue_choose.heure)
                                # print('heure restant ', ue_choose.heure)
                else:
                    print('temps ecoulé ')       
            emploi_temps_semain.append({
                "nom_jour": jours[k],
                "ue_jour": martierjournee
            })
          



        emploi_temps_global.append(emploi_temps_semain)
    
    
    
    for x in  emploi_temps_semain:
        print("---" + x['nom_jour']+ "---")
        for ue in x['ue_jour']:
            print("-", ue.titre ," ", ue.heure )
                
        


            
def app(request):
    if list_ues.size_list() != 0 :
        generate()
        template = loader.get_template('index.html')
        context = {
            "emploi_temps_global": emploi_temps_global
        }    
        return HttpResponse(template.render(context, request))
    else:
        template = loader.get_template('index.html')
        return HttpResponse(template.render())



def enregistement(request):
    if request.method=="POST":
        ue = Matier()
        ue.titre = request.POST['titre']
        ue.credit = request.POST['credit']
        ue.heure = int(request.POST['heure'])
        list_ues.add_matier(ue)
    return render(request, 'input.html' )