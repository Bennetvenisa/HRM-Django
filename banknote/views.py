from django.shortcuts import render, redirect
import django.contrib.messages as messages
import pickle
import pandas as pandas
import numpy as np
import sklearn.linear_model.logistic

# Create your views here.

def banknote(request):
    if request.method=="POST":
        variance=int(request.POST['variance'])
        skewness=int(request.POST['skewness'])
        curtosis=int(request.POST['curtosis'])
        entropy=int(request.POST['entropy'])

        #pickle_in=open("logistic.pkl", "rb")
        mdl_in=open("D:\Datascience\Bank_note_authentication\logistic.pkl",'rb')

        log_reg=pickle.load(mdl_in)


        prediction=log_reg.predict([[variance, skewness, curtosis, entropy]])
        
        messages.info(request, "Your Bank Note is Predicted as" + str(prediction)) 
        return redirect('banknote')


    else:
        return render (request, "note.html")
