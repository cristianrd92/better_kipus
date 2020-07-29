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
import math
import googlemaps

gmaps = googlemaps.Client(key='AIzaSyBUEx8t5HyVP5YMjnUPu0rIyuhVmR6Hzy0')

s_path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
data_path = s_path + '/Data/'
df_first = pd.read_excel(data_path + 'datos.xlsx', sheet_name="Datos", skiprows=[0,2], usecols="A:X")

#Cambiamos nombre a columnas
df_first.columns = ["region_id",'comuna','institution', "building_name", "building_address","building_ID" ,"building_area",
                    "building_space_type_1st", "building_space_type_2nd", "service",'medidor','clasificacion',
                    'm1','m2','m3','m4','m5','m6','m7','m8','m9','m10','m11','m12']
#Eliminamos toda fila con area no definida
df_first = df_first[np.isfinite(df_first['building_area'])]
#Creamos columnas nuevas latitud y longitud
estacionalidad_general = list()
estacionalidad_meses = list()
#Eliminamos las filas duplicadas
df_first = df_first.drop_duplicates('building_ID')
df_first = df_first.reset_index(drop=True)
#Algoritmo para verificar valores nulos, vacios o en 0 en el dataframe para excluir meses en calculo factor estacionalidad
df_temp = df_first.isnull().sum(axis=1)

#Convertimos el contador de valores nulos en un array para trabajar con el
a = np.array(df_temp)

#Eliminamos filas con mas de 6 valores nulos o vacios
for x in range (len(a)):
    if a[x]>6:
        df_first = df_first.drop(x)
df_first = df_first.reset_index(drop=True)

#Eliminamos filas con mas de 6 valores en 0
for x in range (len(df_first)):
    b = np.array(df_first.iloc[x,12:24])
    b = b.tolist()
    if b.count(0)>6:
        print("Fila numero "+str(x)+" contiene mas de 6 numeros 0")
        df_temp = df_first.drop(x)
df_first = df_temp.reset_index(drop=True)

#Eliminamos filas en dataframe temporal, solo para el calculo de factores de estacionalidad
for x in range(len(df_first)):
    #Eliminamos filas con valores nullos
    df_temp=df_temp.dropna()
    #Eliminamos filas con valores 0
    df_temp = df_temp[~(df_temp == 0).any(axis=1)]

#Calculamos la estacionalidad de cada mes de por edificio y la agregamos a una matriz
for x in range (len(df_temp)):
    promedio_meses_ed=df_temp.iloc[x,12:24].mean()
    for i in range (12,24):
        estacionalidad_meses.append(df_temp.iloc[x,i]/promedio_meses_ed)
    estacionalidad_general.append(estacionalidad_meses)
    estacionalidad_meses = list()

#Calculamos los factores de estacionalidad de cada uno de los 12 meses
estacionalidad_meses = list()
for x in range(12):
    suma = sum([fila[x] for fila  in estacionalidad_general])
    estacionalidad_meses.append(suma/len(estacionalidad_general))

for x in range (len(df_first)):
    b = np.array(df_first.iloc[x,12:24])
    print(b)
    c = np.array(b, dtype = np.float)
    c[np.isnan(c)] = 0
    promedio = np.mean(c)
    #Completamos valor faltante en enero
    if b[0]==0 or math.isnan(b[0]):
        b[0]= promedio*estacionalidad_meses[0]
    #Completamos valor faltante en febrero
    if (b[1]==0 or math.isnan(b[1])==True) and (b[2]!=0 or math.isnan(b[2])!=True) :
        b[1] = (b[0]+b[2])/2
    elif(b[1]==0 or math.isnan(b[1])==True) and (b[2]==0 or math.isnan(b[2])==True):
        b[1] = np.mean(c[2:11])*estacionalidad_meses[1]
    #Completamos valor faltante en marzo
    if (b[2]==0 or math.isnan(b[2])==True) and (b[3]!=0 or math.isnan(b[3])!=True):
        b[2] = (b[1]+b[3])/2
    elif(b[2]==0 or math.isnan(b[2])==True) and (b[3]==0 or math.isnan(b[3])==True):
        b[2] = np.mean(c[3:11])*estacionalidad_meses[2]
    #Completamos valor faltante en abril
    if (b[3]==0 or math.isnan(b[3])==True) and (b[4]!=0 or math.isnan(b[4])!=True):
        b[3] = (b[2]+b[4])/2
    elif(b[3]==0 or math.isnan(b[3])==True) and (b[4]==0 or math.isnan(b[4])==True):
        b[3] = np.mean(c[4:11])*estacionalidad_meses[3]
    #Completamos valor faltante en mayo
    if (b[4]==0 or math.isnan(b[4])==True) and (b[5]!=0 or math.isnan(b[5])!=True ):
        b[4] = (b[3]+b[5])/2
    elif(b[4]==0 or math.isnan(b[4])==True) and (b[5]==0 or math.isnan(b[5])==True):
        b[4] = np.mean(c[5:11])*estacionalidad_meses[4]
    #Completamos valor faltante en junio
    if (b[5]==0 or math.isnan(b[5])==True) and (b[6]!=0 or math.isnan(b[6])!=True ):
        b[5] = (b[4]+b[6])/2
    elif(b[5]==0 or math.isnan(b[5])==True) and (b[6]==0 or math.isnan(b[6])==True):
        b[5] = np.mean(c[6:11])*estacionalidad_meses[5]
    #Completamos valor faltante en julio
    if (b[6]==0 or math.isnan(b[6])==True) and (b[7]!=0 or math.isnan(b[7])!=True ):
        b[6] = (b[5]+b[7])/2
    elif(b[6]==0 or math.isnan(b[6])==True) and (b[7]==0 or math.isnan(b[7])==True):
        b[6] = np.mean(c[7:11])*estacionalidad_meses[6]
    #Completamos valor faltante en agosto
    if (b[7]==0 or math.isnan(b[7])==True) and (b[8]!=0 or math.isnan(b[8])!=True ):
        b[7] = (b[6]+b[8])/2
    elif(b[7]==0 or math.isnan(b[7])==True) and (b[8]==0 or math.isnan(b[8])==True):
        b[7] = np.mean(c[8:11])*estacionalidad_meses[7]
    #Completamos valor faltante en septiembre
    if (b[8]==0 or math.isnan(b[8])==True) and (b[9]!=0 or math.isnan(b[9])!=True ):
        b[8] = (b[7]+b[9])/2
    elif(b[8]==0 or math.isnan(b[8])==True) and (b[9]==0 or math.isnan(b[9])==True):
        b[8] = np.mean(b[0:7])*estacionalidad_meses[8]
    #Completamos valor faltante en octubre
    if (b[9]==0 or math.isnan(b[9])==True) and (b[10]!=0 or math.isnan(b[10])!=True ):
        b[9] = (b[8]+b[10])/2
    elif(b[9]==0 or math.isnan(b[9])==True) and (b[10]==0 or math.isnan(b[10])==True):
        b[9] = np.mean(b[0:8])*estacionalidad_meses[9]
    #Completamos valor faltante en noviembre
    if (b[10]==0 or math.isnan(b[10])==True) and (b[11]!=0 or math.isnan(b[11])!=True ):
        b[10] = (b[9]+b[11])/2
    elif(b[10]==0 or math.isnan(b[10])==True) and (b[11]==0 or math.isnan(b[11])==True):
        b[10] = np.mean(b[0:9])*estacionalidad_meses[10]
    #Completamos valor faltante en diciembre
    if (b[11]==0 or math.isnan(b[11])):
        b[11] = promedio*estacionalidad_meses[11]
    print(b)
    df_first.iloc[x,12:24]=b



list_ubid=list()
list_lat=list()
list_lng=list()
list_address=list()


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
#Generamos Excel con el que trabajara better
df_first.to_excel(data_path+'portfolio.xlsx', sheet_name='datos_procesados',index=False)

print('Ingrese año')
anio = input()
for x in range(len(df_first)):
    print('')
    print("---------------------------------------------------------------")
    run_single(bldg_id=df_first.iloc[x]['building_ID'], saving_target=2, cached_weather=False,anio=anio)
    # Uncomment the line below [delete the '#' before run_batch(...)] to run the analysis for buildings between start_id and end_id
#run_batch(start_id = 1, end_id = 2, saving_target=2, cached_weather=False, batch_report=True, use_default_benchmark_data=True)
