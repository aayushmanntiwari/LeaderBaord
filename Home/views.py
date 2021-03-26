from django.shortcuts import render,redirect
from django.http import *
from django.core import serializers
from Teams.models import Teams,TeamScoring
from Teams.forms import Update_Team_Form
import json

# Create your views here.
def home(request):
    #this code save object data into json format
    try:
        with open("static/data.json", "w") as out:
            teamdata = serializers.serialize("json",Teams.objects.all(),indent=2)
            out.write(teamdata)
    except:
        pass
    return render(request,'index.html')


def Teams_asJson(request):
    object_list = Teams.objects.all().order_by('-score') #or any kind of queryset
    json = serializers.serialize('json', object_list)
    #print(True)
    return HttpResponse(json, content_type='application/json')      


def updatedata(request):
    try:
        value = request.GET.getlist('pk') #this will return all the values of same paramter as list
        if value!=[]:
            idx1 = value[0]
            idx2 =  value[1]
            team1 = Teams.objects.get(id = idx1)
            team2 = Teams.objects.get(id = idx2)
            if request.method == 'POST':
                option1 = request.POST.get('option1')
                option2 = request.POST.get('option2',False)
                if not option2:
                    option2 = "Loss"
                #print(option2)
                #print(team1,team2)
                if option1 == "wins":
                    team1.wins+=1
                    team1.save()
                if option1 == "ties":
                    team1.tie+=1
                    team1.save()
                if option1 == "Loss":
                    team1.losses+=1
                    team1.save()
                if option2 == "wins":
                    team2.wins+=1
                    team2.save()
                if option2 == "ties":
                    team2.tie+=1
                    team2.save()
                if option2 == "Loss":
                    team2.losses+=1
                    team2.save()
                team1.played_Count+=1
                team1.save()
                team2.played_Count+=1
                team2.save()
                return redirect('/')
            else:
                return render(request,'index.html',{'showmodel':True,'team1':team1.name,'team2':team2.name})
        else:
            return redirect('/')
    except:
        return render(request,'index.html')



def updatingdatabase(request):
    values = TeamScoring.objects.all()
    for value in values:
        #print(value.Teams.id,value.options)
        curr_team = Teams.objects.get(id = value.Teams.id)
        #print(curr_team)
        if value.options == "wins" and not value.options == "ties":
            #print(1)
            curr_team.wins+=3
            curr_team.save()
        if value.options == "ties" and not value.options == "wins":
            #print(2)
            curr_team.tie+=1
            curr_team.save()
    return redirect('/')
