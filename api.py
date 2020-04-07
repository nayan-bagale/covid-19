import requests
import json
import logging
import data_manage
import hidden
import os
from datetime import datetime, timedelta

def previous():
    url = "https://corona-virus-world-and-india-data.p.rapidapi.com/api_india_timeline"
    response = requests.request("GET", url, headers=hidden.head())
    data = response.json()
    try:
        for i in data:
            confirmed = i['totalconfirmed']
            recovered = i['totalrecovered']
            deaths = i['totaldeceased']
            bad_date = i['date']
            data_manage.previous_data(confirmed,recovered,deaths,bad_date)
            print(i)
    except Exception as e:
        x = data['message']
        logging.warning('Previous: '+ x)
        print('Previous: '+ x)

def worlwide():
    url = "https://corona-virus-world-and-india-data.p.rapidapi.com/api"
    response = requests.request("GET", url, headers=hidden.head())
    data = response.json()
    try:
        countrys = data['countries_stat']
        for i in countrys:
            country = i['country_name']
            confirmed_cases = i['cases']
            deaths = i['deaths']
            recovered = i['total_recovered']
            critical = i['serious_critical']
            active = i['active_cases']
            data_manage.worldwide_data(country,active,confirmed_cases,critical,recovered,deaths)
    except Exception as e:
        x = data['message']
        print('Worldwide: '+ x)
        logging.warning('Worldwide: '+ str(x) +' '+ str(e))

def total(total_values):
    active = total_values['active']
    confirmed = total_values['confirmed']
    deaths = total_values['deaths']
    recovered = total_values['recovered']
    data_manage.total_values(active,confirmed,recovered,deaths)

def state(state_name,state_data):
    try:
        active = state_data[state_name]['active']
        confirmed = state_data[state_name]['confirmed']
        deaths = state_data[state_name]['deaths']
        recovered = state_data[state_name]['recovered']
        try:
            d_confirmed = state_data[state_name]['deltaconfirmed']
            d_recovered = state_data[state_name]['deltarecovered']
            d_deaths = state_data[state_name]['deltadeaths']
            delta = {}
            delta['confirmed'] = d_confirmed
            delta['deaths'] = d_deaths
            delta['recoverd'] = d_recovered
            #print(delta)
        except:
            delta = 'null'
            logging.info('KeyError: delta, Not find data in ' +'"'+state_name+'"'+ ' State. delta is set to NULL')

        data_manage.state_data(state_name,active,confirmed,recovered,deaths,delta)

    except KeyError as e:
        logging.info('KeyError: ' +str(e)+','+ ' Not find data in ' +'"'+state_name+'"'+ ' State')

def district_d(district_name,district_data):
    confirmed = district_data[district_name]['confirmed']
    delta = district_data[district_name]['delta']
    data_manage.district_data(district_name,confirmed,delta)

date = datetime.strftime(datetime.now(), '%m-%d-%y')
log_file = 'report/'+date+'.log'
try:
    os.mkdir('report')
    os.mkdir('database')
except OSError:
    print("Creation of the directory %s failed" % 'report')
    pass
logging.basicConfig(filename= log_file,level=logging.DEBUG,format='%(asctime)s:%(levelname)s:%(message)s')

url = "https://corona-virus-world-and-india-data.p.rapidapi.com/api_india"
try:
    response = requests.request("GET", url, headers=hidden.head())
except Exception as e:
    print('Connection error')
    logging.info('Internet Connection Error: ',str(e))
    quit()


data = response.json()
if len(data) < 3:
    try:
        x = data['message']
        logging.warning('Main: '+ x)
        worlwide()#this is important
        previous() #this is important
        print('Main: '+ x)
        quit()
    except Exception as e:
        logging.warning('UnknownError: ' +str(data)+','+ '\n'+ e)
        worlwide()#this is important
        previous() #this is important
        print(e)
        quit()
try:
    total_value = data['total_values']
    total(total_value)
except Exception as e:
    logging.info('KeyError: ' +str(e)+','+ ' Not find total values ')

state_wise = data['state_wise']
for state_name in state_wise:
    state(state_name,state_wise) #this is important
    #print(state_wise[state_name])
    try:
        district = state_wise[state_name]['district']
    except KeyError as e:
        logging.info('KeyError: ' +str(e)+','+ ' Not find District in ' +'"'+state_name+'"')
        continue
    for district_name in district:
        district_d(district_name,district) #this is important
        #pass

worlwide()#this is important
previous() #this is important
