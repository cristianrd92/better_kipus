'''
Energy Efficiency Targeting Tool Copyright (c) 2018, The Regents of the University of California, through Lawrence Berkeley National Laboratory (subject to receipt of any required approvals from the U.S. Dept. of Energy). All rights reserved.
If you have questions about your rights to use or distribute this software, please contact Berkeley Lab's Intellectual Property Office at  IPO@lbl.gov.
NOTICE.  This Software was developed under funding from the U.S. Department of Energy and the U.S. Government consequently retains certain rights. As such, the U.S. Government has been granted for itself and others acting on its behalf a paid-up, nonexclusive, irrevocable, worldwide license in the Software to reproduce, distribute copies to the public, prepare derivative works, and perform publicly and display publicly, and to permit other to do so.
'''

from demo import *
import pandas as pd
from pandas import ExcelWriter
import openlocationcode
import numpy as np
import googlemaps

gmaps = googlemaps.Client(key='AIzaSyBUEx8t5HyVP5YMjnUPu0rIyuhVmR6Hzy0')

s_path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
data_path = s_path + '/Data/'
df_first = pd.read_excel(data_path + 'datos.xlsx', sheet_name="Datos", skiprows=[0], usecols="A:X")

#Cambiamos nombre a columnas
df_first.columns = ["region_id",'comuna','institution', "building_name", "building_address","building_ID" ,"building_area",
                    "building_space_type_1st", "building_space_type_2nd", "service",'medidor','clasificacion',
                    'm1','m2','m3','m4','m5','m6','m7','m8','m9','m10','m11','m12']
#Eliminamos toda fila con area no definida
df_first = df_first[np.isfinite(df_first['building_area'])]
#Creamos columnas nuevas latitud y longitud

list_ubid=list()
list_lat=list()
list_lng=list()
list_address=list()

df_first = df_first.drop_duplicates('building_ID')
for i,d in df_first.iterrows():
    #Comienza proceso de confeccion de direccion
    x = d['building_address']
    x = x.split(',')
    f = x[1]
    f = f.split('Nro. ')
    n = f[-1]
    x = x[0]+' '+n+','+x[-1]+', Chile'
    #Finaliza confeccion direccion
    geocode_result = gmaps.geocode(x)
    lat = geocode_result[0]['geometry']['location']['lat']
    lng = geocode_result[0]['geometry']['location']['lng']
    ubid = openlocationcode.encode(lat,lng)
    list_address.append(x)
    list_lat.append(lat)
    list_lng.append(lng)
    list_ubid.append(ubid)

df_first['latitude'] = list_lat
df_first['longitude']  = list_lng
df_first['building_ID'] = list_ubid
df_first['building_address'] = list_address
#Eliminamos las filas duplicadas
#Generamos Excel con el que trabajara better
df_first.to_excel(data_path+'portfolio.xlsx', sheet_name='example',index=False)

# Notes:
    # Saving target: 1 ~ conservative, 2 ~ nominal, 3 ~ aggressive
    # Change the building id and saving target for the building you want to analyze
print('Ingrese año')
anio = input()
for x in range(len(df_first)):
    run_single(bldg_id=df_first.iloc[x]['building_ID'], saving_target=2, cached_weather=False,anio=anio)
    # Uncomment the line below [delete the '#' before run_batch(...)] to run the analysis for buildings between start_id and end_id
#run_batch(start_id = 1, end_id = 2, saving_target=2, cached_weather=False, batch_report=True, use_default_benchmark_data=True)
