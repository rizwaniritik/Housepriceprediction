from django.shortcuts import render,HttpResponse,redirect
import pickle
import numpy as np
import json
# Create your views here.
def home(request):
    if request.method=="POST": 
        print("chlrha h")
        print((request.POST.get('Squareft')))
        sqft=int(request.POST.get('Squareft'))
        Bhk=request.POST.get('uiBHK')
        print(Bhk)
        bath=request.POST.get('uiBathrooms')
        area=request.POST.get('uiLocations')
       
        
        
        r=estimated_price(area,sqft,Bhk,bath)
        print(r)
        return render(request,"home.html",context={'price':r ,'Location':area,'Bhk':Bhk,'sqft':sqft,'bath':bath})
  

    return render(request,"home.html")


global __model
global __datacolumns
global __location

def estimated_price(location,sqft,bhk,bath):
    with open("./static/columns.json",'r')as f:
        __datacolumns=json.load(f)['data_columns']
        __location=__datacolumns[3:]
    with open('./static/banglore_home_prices_model.pickle','rb') as f:

        __model=pickle.load(f)
    try: 
        loc_index=__datacolumns.index(location.lower())
    except:
        loc_index=-1

    x=np.zeros(len(__datacolumns))
    x[0]=sqft
    x[1]=bath
    x[2]=bhk
    if loc_index>=0:
        x[loc_index]=1
    return round( __model.predict([x])[0],2)


    
