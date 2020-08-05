'''
Energy Efficiency Targeting Tool Copyright (c) 2018, The Regents of the University of California, through Lawrence Berkeley National Laboratory (subject to receipt of any required approvals from the U.S. Dept. of Energy). All rights reserved.
If you have questions about your rights to use or distribute this software, please contact Berkeley Lab's Intellectual Property Office at  IPO@lbl.gov.
NOTICE.  This Software was developed under funding from the U.S. Department of Energy and the U.S. Government consequently retains certain rights. As such, the U.S. Government has been granted for itself and others acting on its behalf a paid-up, nonexclusive, irrevocable, worldwide license in the Software to reproduce, distribute copies to the public, prepare derivative works, and perform publicly and display publicly, and to permit other to do so.
'''

from demo import *
import pandas as pd
from scipy.spatial import distance
from pandas import ExcelWriter
import openlocationcode
import numpy as np
import csv_kipus
import math
import googlemaps
import model

gmaps = googlemaps.Client(key='AIzaSyBUEx8t5HyVP5YMjnUPu0rIyuhVmR6Hzy0')

s_path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
data_path = s_path + '/Data/'
report_path = s_path + '/outputs/'
df_first = pd.read_excel(data_path + 'datos.xlsx', sheet_name="Datos", skiprows=[0,2], usecols="A:AA")

#Cambiamos nombre a columnas
df_first.columns = ["region_id",'comuna','institution', "building_name", "building_address","building_ID" ,"building_area",
                    "building_space_type_1st", "building_space_type_2nd", "service",'medidor','clasificacion',
                    'm1','m2','m3','m4','m5','m6','m7','m8','m9','m10','m11','m12','heating_type','air_conditioning','pisos']
#Eliminamos toda fila con area no definida
df_first = df_first[np.isfinite(df_first['building_area'])]

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
for x in range(12):
    suma = sum([fila[x] for fila  in estacionalidad_general])
    estacionalidad_meses.append(suma/len(estacionalidad_general))

valores_q = list()
#Algortimo para completar datos de meses faltantes
for x in range (len(df_first)):
    b = np.array(df_first.iloc[x,12:24])
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
    df_first.iloc[x,12:24]=b
    #Algoritmo para eliminar valores muy alejados de q1 y q3
    valores_q.append(sum(b)/df_first.iloc[x,6])

q1 = np.percentile(valores_q,25)
q3 = np.percentile(valores_q,75)
iqr = q3-q1
lower = q1-(1.5*iqr)
higher = q3+(1.5*iqr)

#Algoritmo para eliminar en base a Q1 y Q3
indice =0
for x in valores_q:
    if x<lower or x>higher:
        df_first = df_first.drop(indice)
    indice+=1

#print(q1,q3,iqr,lower,higher,valores_q)

list_ubid=list()
list_lat=list()
list_lng=list()
list_address=list()


w = 400
h = 400
zoom = 16
lat = -36.4857709
lng = -72.70260139999999

def getPointLatLng(x, y):
    parallelMultiplier = math.cos(lat * math.pi / 180)
    degreesPerPixelX = 360 / math.pow(2, zoom + 8)
    degreesPerPixelY = 360 / math.pow(2, zoom + 8) * parallelMultiplier
    pointLat = lat - degreesPerPixelY * ( y - h / 2)
    pointLng = lng + degreesPerPixelX * ( x  - w / 2)

    return (pointLat, pointLng)

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
    #print(geocode_result)
    #print('-------------------------')
    n_lat = geocode_result[0]['geometry']['viewport']['northeast']['lat']
    n_lng = geocode_result[0]['geometry']['viewport']['northeast']['lng']
    s_lat = geocode_result[0]['geometry']['viewport']['southwest']['lat']
    s_lng = geocode_result[0]['geometry']['viewport']['southwest']['lng']
    lat = geocode_result[0]['geometry']['location']['lat']
    lng = geocode_result[0]['geometry']['location']['lng']
    #print(lat,lng)
    #print(n_lat,n_lng)
    #print(s_lat,s_lng)
    #input()
    ubid = openlocationcode.encode(lat,lng)
    list_address.append(x)
    list_lat.append(lat)
    list_lng.append(lng)
    list_ubid.append(ubid)
#print(lat,lng)
#NE
#print(getPointLatLng(w, 0))
#SW
#print(getPointLatLng(0, h))
#NW
#print(getPointLatLng(0, 0))
#SE
#print(getPointLatLng(w, h))


df_first['latitude'] = list_lat
df_first['longitude']  = list_lng
df_first['building_ID'] = list_ubid
df_first['building_address'] = list_address
#Generamos Excel con el que trabajara better
df_first.to_excel(data_path+'portfolio.xlsx', sheet_name='datos_procesados',index=False)

list_baseload = list()
list_cluster_a = list()
list_cluster_b = list()
list_cluster_c = list()
vector_cluster_d = list()
#Variables ya que sirven para asignacion de cluster c, estas ya fuerona calculadas obtenidas de wiki CityBES 
vector_cluster_c = [7.323208,35.72581,47.953624,250.00000,15.427423,130.69231]
vector_cluster_d_sin_estandarizar = [3.545455,12.030303,14.46364,19.39258,31.800000,24.000000,14.47000,16.76000,5.435897,9.076923,12.71026,14.71795]
promedio_v_d = np.mean(vector_cluster_d_sin_estandarizar)
desviacion_v_d = np.std(vector_cluster_d_sin_estandarizar)

vector_cluster_d=(vector_cluster_d_sin_estandarizar-promedio_v_d)/desviacion_v_d

list_hvac = list()
list_cooling_change_point = list()
list_cooling_sensitivity = list()
list_heating_start_point = list()
list_heating_sensitivity = list()
list_cluster_d = list()

def split(arr, size):
    arrs = []
    while len(arr) > size:
        pice = arr[:size]
        arrs.append(pice)
        arr   = arr[size:]
    arrs.append(arr)
    return arrs








suma_anuales = list()
 
print('Ingrese año')
anio = input()
for x in range(len(df_first)):
    print('')
    print("---------------------------------------------------------------")
    run_single(bldg_id=df_first.iloc[x]['building_ID'], saving_target=2, cached_weather=False,anio=anio)
    #Desde función run single se generan variables globales que son las que necesitamos para asignacion de cluster
    #Se preproceso toda la informacion por lo cual ya podemos asignar cluster

    #Cluster A (Tamaño)
    if df_first.iloc[x]['pisos']<=3 and df_first.iloc[x]['building_area']<2322:
        cluster_a = 1 #"Small"
    elif df_first.iloc[x]['pisos']>6 or  df_first.iloc[x]['building_area']>9290:
        cluster_a = 3 #"Large"
    else:
        cluster_a = 2 #"Medium"
    list_cluster_a.append(cluster_a)

    #Cluster B (HVAC Type)
    if df_first.iloc[x]['heating_type']=='Gas':
        cluster_b = 2
    elif df_first.iloc[x]['air_conditioning']=='Single':
        cluster_b = 1
    else:  
        cluster_b = 3
    list_cluster_b.append(cluster_b)
    
    #Sumamos costos anuales y los agregamos a una lista
    suma_anuales.append(sum(df_first.iloc[x,12:24]))

    #Agregamos todos los valores que calculo better para trabajar con ellos
    list_baseload.append(model.baseload)
    list_cooling_change_point.append(model.cooling_change_point)
    list_cooling_sensitivity.append(model.cooling_sensitivity)
    list_heating_start_point.append(model.heating_start_point)
    list_heating_sensitivity.append(model.heating_sensitivity)
    #HVAC
    hvac = (sum(df_first.iloc[x,12:24])/df_first.iloc[x]['building_area'])-model.baseload
    list_hvac.append(hvac)

    #Cluser C (HVAC vs Equipo)
    #Generamos los vectores que hay que comparar
    vector_c_1 = [vector_cluster_c[0],vector_cluster_c[1]]
    vector_c_2 = [vector_cluster_c[2],vector_cluster_c[3]]
    vector_c_3 = [vector_cluster_c[4],vector_cluster_c[5]]
    #Primero va HVAC luego Baseload
    vector_c_comparable = [hvac,model.baseload]

    dis_vc1 = distance.euclidean(vector_c_1,vector_c_comparable)
    dis_vc2 = distance.euclidean(vector_c_2,vector_c_comparable)
    dis_vc3 = distance.euclidean(vector_c_3,vector_c_comparable)
    
    #Generamos un array con los 3 valores de distancia ucleidiana c
    list_ucle_c = [dis_vc1,dis_vc2,dis_vc3]
    cluster_c = list_ucle_c[0]
    #Recorrer y comparar
    for numero in list_ucle_c:
        if numero < cluster_c:
            cluster_c = numero
    if cluster_c == dis_vc1:
        cluster_c = 1
    elif cluster_c == dis_vc2:
        cluster_c = 2
    else:
        cluster_c = 3
    list_cluster_c.append(cluster_c)

    #Cluser D (Sensitivity y change point)
    #Dividimos vector y creamos una matriz de tamaño 3
    vector_d = split(vector_cluster_d,4)
    #Generamos vector del edificio
    vector = [model.cooling_sensitivity,model.heating_sensitivity,model.heating_start_point,model.cooling_change_point]
    #Estandarizamos vector del edificio vs valores estandarizados de referencia
    v1=(vector-promedio_v_d)/desviacion_v_d
    dis_vd1 = distance.euclidean(vector_d[0],v1)
    dis_vd2 = distance.euclidean(vector_d[1],v1)
    dis_vd3 = distance.euclidean(vector_d[2],v1)

    list_ucle_d = [dis_vd1,dis_vd2,dis_vd3]
    cluster_d = list_ucle_d[0]
    #Recorrer y comparar
    for numero in list_ucle_d:
        if numero < cluster_d:
            cluster_d = numero
    if cluster_d == dis_vd1:
        cluster_d = 1
    elif cluster_d == dis_vd2:
        cluster_d = 2
    else:
        cluster_d = 3
    list_cluster_d.append(cluster_d)

#Agregamos variables a un excel con todos los datos procesador por better
df_first['hvac'] = list_hvac
df_first['baseload'] = list_baseload
df_first['cooling_change_point'] = list_cooling_change_point
df_first['cooling_sensitivity'] = list_cooling_sensitivity
df_first['heating_start_point'] = list_heating_start_point
df_first['heating_sensitivity'] = list_heating_sensitivity
#Agregamos a excel las asiganciones de cluster
df_first['cluster_a'] = list_cluster_a
df_first['cluster_b'] = list_cluster_b
df_first['cluster_c'] = list_cluster_c
df_first['cluster_d'] = list_cluster_d

#Creamos archivo excel con todos los datos obtenidos de better
df_first.to_excel(report_path+'Datos Finales.xlsx', sheet_name='Datos',index=False)

#Creamos archivo csv el cual se utilizara para subir a CityBes
csv_kipus.crear_csv(df_first,list_ubid,list_address,suma_anuales)
#geojson.crear_json(df_first,list_ubid,list_address,suma_anuales)