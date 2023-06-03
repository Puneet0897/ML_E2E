from main import *
import pandas as pd
from flask import request
import datetime as dt


def SourceDestCheck():
    src = request.form["Source"]
    dest = request.form["Destination"]
    if src == dest:
        return True
    else :
        return False

def DepArrDateCheck():
    date_dep = request.form["Dep_Time"]
    Journey_day = int(pd.to_datetime(date_dep, format="%Y-%m-%dT%H:%M").day)
    Journey_month = int(pd.to_datetime(date_dep, format ="%Y-%m-%dT%H:%M").month)
    Journey_year = int(pd.to_datetime(date_dep, format ="%Y-%m-%dT%H:%M").year)

    date_arr = request.form["Arrival_Time"]
    Arrival_day = int(pd.to_datetime(date_arr, format ="%Y-%m-%dT%H:%M").day)
    Arrival_month = int(pd.to_datetime(date_arr, format ="%Y-%m-%dT%H:%M").month)
    Arrival_year = int(pd.to_datetime(date_arr, format ="%Y-%m-%dT%H:%M").year)

    dep_dt = dt.datetime(Journey_year,Journey_month,Journey_day)
    arr_dt = dt.datetime(Arrival_year,Arrival_month,Arrival_day)

    if dep_dt < arr_dt:
        return True
    else:
        return False

def OneHotEncode():
# Date_of_Journey
    date_dep = request.form["Dep_Time"]
    Journey_day = int(pd.to_datetime(date_dep, format="%Y-%m-%dT%H:%M").day)
    Journey_month = int(pd.to_datetime(date_dep, format ="%Y-%m-%dT%H:%M").month)

# Departure
    Dep_hour = int(pd.to_datetime(date_dep, format ="%Y-%m-%dT%H:%M").hour)
    Dep_min = int(pd.to_datetime(date_dep, format ="%Y-%m-%dT%H:%M").minute)

# Arrival
    date_arr = request.form["Arrival_Time"]
    Arrival_hour = int(pd.to_datetime(date_arr, format ="%Y-%m-%dT%H:%M").hour)
    Arrival_min = int(pd.to_datetime(date_arr, format ="%Y-%m-%dT%H:%M").minute)

# Duration
    dur_hour = abs(Arrival_hour - Dep_hour)
    dur_min = abs(Arrival_min - Dep_min)

# Total Stops
    Total_stops = int(request.form["stops"])

# Airline
    airline=request.form['airline']
    if(airline=='Jet Airways'):
        Jet_Airways = 1
        IndiGo = 0
        Air_India = 0
        Multiple_carriers = 0
        SpiceJet = 0
        Vistara = 0
        GoAir = 0
        Multiple_carriers_Premium_economy = 0
        Jet_Airways_Business = 0
        Vistara_Premium_economy = 0
        Trujet = 0 

    elif (airline=='IndiGo'):
        Jet_Airways = 0
        IndiGo = 1
        Air_India = 0
        Multiple_carriers = 0
        SpiceJet = 0
        Vistara = 0
        GoAir = 0
        Multiple_carriers_Premium_economy = 0
        Jet_Airways_Business = 0
        Vistara_Premium_economy = 0
        Trujet = 0 

    elif (airline=='Air India'):
        Jet_Airways = 0
        IndiGo = 0
        Air_India = 1
        Multiple_carriers = 0
        SpiceJet = 0
        Vistara = 0
        GoAir = 0
        Multiple_carriers_Premium_economy = 0
        Jet_Airways_Business = 0
        Vistara_Premium_economy = 0
        Trujet = 0 
            
    elif (airline=='Multiple carriers'):
        Jet_Airways = 0
        IndiGo = 0
        Air_India = 0
        Multiple_carriers = 1
        SpiceJet = 0
        Vistara = 0
        GoAir = 0
        Multiple_carriers_Premium_economy = 0
        Jet_Airways_Business = 0
        Vistara_Premium_economy = 0
        Trujet = 0 
            
    elif (airline=='SpiceJet'):
        Jet_Airways = 0
        IndiGo = 0
        Air_India = 0
        Multiple_carriers = 0
        SpiceJet = 1
        Vistara = 0
        GoAir = 0
        Multiple_carriers_Premium_economy = 0
        Jet_Airways_Business = 0
        Vistara_Premium_economy = 0
        Trujet = 0 
            
    elif (airline=='Vistara'):
        Jet_Airways = 0
        IndiGo = 0
        Air_India = 0
        Multiple_carriers = 0
        SpiceJet = 0
        Vistara = 1
        GoAir = 0
        Multiple_carriers_Premium_economy = 0
        Jet_Airways_Business = 0
        Vistara_Premium_economy = 0
        Trujet = 0

    elif (airline=='GoAir'):
        Jet_Airways = 0
        IndiGo = 0
        Air_India = 0
        Multiple_carriers = 0
        SpiceJet = 0
        Vistara = 0
        GoAir = 1
        Multiple_carriers_Premium_economy = 0
        Jet_Airways_Business = 0
        Vistara_Premium_economy = 0
        Trujet = 0

    elif (airline=='Multiple carriers Premium economy'):
        Jet_Airways = 0
        IndiGo = 0
        Air_India = 0
        Multiple_carriers = 0
        SpiceJet = 0
        Vistara = 0
        GoAir = 0
        Multiple_carriers_Premium_economy = 1
        Jet_Airways_Business = 0
        Vistara_Premium_economy = 0
        Trujet = 0

    elif (airline=='Jet Airways Business'):
        Jet_Airways = 0
        IndiGo = 0
        Air_India = 0
        Multiple_carriers = 0
        SpiceJet = 0
        Vistara = 0
        GoAir = 0
        Multiple_carriers_Premium_economy = 0
        Jet_Airways_Business = 1
        Vistara_Premium_economy = 0
        Trujet = 0

    elif (airline=='Vistara Premium economy'):
        Jet_Airways = 0
        IndiGo = 0
        Air_India = 0
        Multiple_carriers = 0
        SpiceJet = 0
        Vistara = 0
        GoAir = 0
        Multiple_carriers_Premium_economy = 0
        Jet_Airways_Business = 0
        Vistara_Premium_economy = 1
        Trujet = 0
            
    elif (airline=='Trujet'):
        Jet_Airways = 0
        IndiGo = 0
        Air_India = 0
        Multiple_carriers = 0
        SpiceJet = 0
        Vistara = 0
        GoAir = 0
        Multiple_carriers_Premium_economy = 0
        Jet_Airways_Business = 0
        Vistara_Premium_economy = 0
        Trujet = 1

    else:
        Jet_Airways = 0
        IndiGo = 0
        Air_India = 0
        Multiple_carriers = 0
        SpiceJet = 0
        Vistara = 0
        GoAir = 0
        Multiple_carriers_Premium_economy = 0
        Jet_Airways_Business = 0
        Vistara_Premium_economy = 0
        Trujet = 0

    # Source
    Source = request.form["Source"]
    if (Source == 'Delhi'):
        s_Delhi = 1
        s_Kolkata = 0
        s_Mumbai = 0
        s_Chennai = 0

    elif (Source == 'Kolkata'):
        s_Delhi = 0
        s_Kolkata = 1
        s_Mumbai = 0
        s_Chennai = 0

    elif (Source == 'Mumbai'):
        s_Delhi = 0
        s_Kolkata = 0
        s_Mumbai = 1
        s_Chennai = 0

    elif (Source == 'Chennai'):
        s_Delhi = 0
        s_Kolkata = 0
        s_Mumbai = 0
        s_Chennai = 1

    else:
        s_Delhi = 0
        s_Kolkata = 0
        s_Mumbai = 0
        s_Chennai = 0


    # Destination
    # Banglore = 0 (not in column)
    Dest = request.form["Destination"]
    if (Dest == 'Cochin'):
        d_Cochin = 1
        d_Delhi = 0
        d_New_Delhi = 0
        d_Hyderabad = 0
        d_Kolkata = 0
        
    elif (Dest == 'Delhi'):
        d_Cochin = 0
        d_Delhi = 1
        d_New_Delhi = 0
        d_Hyderabad = 0
        d_Kolkata = 0

    elif (Dest == 'New_Delhi'):
        d_Cochin = 0
        d_Delhi = 0
        d_New_Delhi = 1
        d_Hyderabad = 0
        d_Kolkata = 0

    elif (Dest == 'Hyderabad'):
        d_Cochin = 0
        d_Delhi = 0
        d_New_Delhi = 0
        d_Hyderabad = 1
        d_Kolkata = 0

    elif (Dest == 'Kolkata'):
        d_Cochin = 0
        d_Delhi = 0
        d_New_Delhi = 0
        d_Hyderabad = 0
        d_Kolkata = 1

    else:
        d_Cochin = 0
        d_Delhi = 0
        d_New_Delhi = 0
        d_Hyderabad = 0
        d_Kolkata = 0
    
    return [[
            Total_stops,
            Journey_day,
            Journey_month,
            Dep_hour,
            Dep_min,
            Arrival_hour,
            Arrival_min,
            dur_hour,
            dur_min,
            Air_India,
            GoAir,
            IndiGo,
            Jet_Airways,
            Jet_Airways_Business,
            Multiple_carriers,
            Multiple_carriers_Premium_economy,
            SpiceJet,
            Trujet,
            Vistara,
            Vistara_Premium_economy,
            s_Chennai,
            s_Delhi,
            s_Kolkata,
            s_Mumbai,
            d_Cochin,
            d_Delhi,
            d_Hyderabad,
            d_Kolkata,
            d_New_Delhi
        ]]