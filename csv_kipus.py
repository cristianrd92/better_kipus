
import pandas as pd
from pandas import ExcelWriter
import numpy as np
import os
from datetime import datetime


s_path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
citybes = s_path + '/outputs_citybes/'



def crear_csv(df_first,list_ubid,list_address,suma_anuales,list_pisos,list_area):
    df_csv = pd.DataFrame(columns=('UBID','search_index','building_id','shared_footprint','institution','use_type','city','address','year_built','cluster_probability','disaggregate_proportion_by_institution_floors',
    'disaggregate_proportion_by_institution_area','gross_floor_area_filled','old_gross_floor_area','real_year_built','num_floors','num_institution','institution_total_floor_area','building_total_floor_area',
    'floor_height','building_height','department_name','latitude','longitude','wall_material','wall_insulation','roof_insulation','window_frame','window_type','wwr_norte','wwr_oriente','wwr_poniente','wwr_sur',
    'shading_type_norte','shading_type_oriente','shading_type_poniente','shading_type_sur','shading_percent_norte','shading_percent_oriente','shading_percent_poniente','shading_percentage_sur','heating_type',
    'air_conditioning','lighting_system','Elec_Y17M01','Elec_Y17M02','Elec_Y17M03','Elec_Y17M04','Elec_Y17M05','Elec_Y17M06','Elec_Y17M07','Elec_Y17M08','Elec_Y17M09','Elec_Y17M10','Elec_Y17M11','Elec_Y17M12',
    'Elec_Y18M01','Elec_Y18M02','Elec_Y18M03','Elec_Y18M04','Elec_Y18M05','Elec_Y18M06','Elec_Y18M07','Elec_Y18M08','Elec_Y18M09','Elec_Y18M10','Elec_Y18M11','Elec_Y18M12','Elec_intensity_Y17','Elec_intensity_Y18',
    'Elec_annual_cost','Gas_Y17M01','Gas_Y17M02','Gas_Y17M03','Gas_Y17M04','Gas_Y17M05','Gas_Y17M06','Gas_Y17M07','Gas_Y17M08','Gas_Y17M09','Gas_Y17M10','Gas_Y17M11','Gas_Y17M12','Gas_Y18M01','Gas_Y18M02','Gas_Y18M03',
    'Gas_Y18M04','Gas_Y18M05','Gas_Y18M06','Gas_Y18M07','Gas_Y18M08','Gas_Y18M09','Gas_Y18M10','Gas_Y18M11','Gas_Y18M12','Gas_intensity_Y17','Gas_intensity_Y18','Gas_annual_cost','area','perimeter','cluster','cluster_probability_1','UBID_2','disaggregate_proportion'))

    search = list()
    id_ed = list()
    registros = len(list_ubid)
    #Generamos search_index de 1000 a x
    for x in range(1000,(registros+1000)):
        search.append(x)
    #Generamos building_id de 1 a x
    for x in range(1,(registros+1)):
        id_ed.append(x)
    #Generamos archivo 
    predefinidos = ['Office',1,10,1,1,2010,28,200,'Concret','No isolation','aluminium','Single']

    df_csv['UBID'] = list_ubid
    df_csv['search_index'] = search
    df_csv['building_id'] = id_ed
    df_csv['institution'] = df_first['institution']
    df_csv['use_type'] = predefinidos[0]
    df_csv['city'] = df_first['comuna']
    df_csv['address'] = list_address
    df_csv['year_built'] = predefinidos[1] #Cambiar por numero de cluster a asignar a futuro
    df_csv['cluster_probability'] = predefinidos[2]
    df_csv['disaggregate_proportion_by_institution_floors'] = predefinidos[3]
    df_csv['disaggregate_proportion_by_institution_area'] = predefinidos[4]
    df_csv['gross_floor_area_filled'] = df_first['building_area']
    df_csv['old_gross_floor_area'] = df_first['building_area']
    df_csv['real_year_built'] = predefinidos[5]
    df_csv['num_floors'] = df_first['pisos'] #Referencia al edificio completo
    df_csv['num_institution'] = list_pisos #Referencia a los pisos ocupados por la insitución
    df_csv['institution_total_floor_area'] = list_area #Area ocupada por la insitucion en referencia a los pisos
    df_csv['building_total_floor_area'] = df_first['building_area'] #Area total del edificio
    df_csv['floor_height'] = predefinidos[6]
    df_csv['building_height'] = predefinidos[7] #Altura edificio
    df_csv['department_name'] = df_first['building_name']
    df_csv['latitude'] = df_first['latitude']
    df_csv['longitude'] = df_first['longitude']
    df_csv['wall_material'] = predefinidos[8]
    df_csv['wall_insulation'] = predefinidos[9]
    df_csv['roof_insulation'] = predefinidos[9]
    df_csv['window_frame'] = predefinidos[10]
    df_csv['window_type'] = predefinidos[11]
    df_csv['wwr_norte'] = predefinidos[11]
    df_csv['Elec_Y17M01'] = round(df_first['m1'])
    df_csv['Elec_Y17M02'] = round(df_first['m2'])
    df_csv['Elec_Y17M03'] = round(df_first['m3'])
    df_csv['Elec_Y17M04'] = round(df_first['m4'])
    df_csv['Elec_Y17M05'] = round(df_first['m5'])
    df_csv['Elec_Y17M06'] = round(df_first['m6'])
    df_csv['Elec_Y17M07'] = round(df_first['m7'])
    df_csv['Elec_Y17M08'] = round(df_first['m8'])
    df_csv['Elec_Y17M09'] = round(df_first['m9'])
    df_csv['Elec_Y17M10'] = round(df_first['m10'])
    df_csv['Elec_Y17M11'] = round(df_first['m11'])
    df_csv['Elec_Y17M12'] = round(df_first['m12'])
    df_csv['Elec_Y18M01'] = 0
    df_csv['Elec_Y18M02'] = 0
    df_csv['Elec_Y18M03'] = 0
    df_csv['Elec_Y18M04'] = 0
    df_csv['Elec_Y18M05'] = 0
    df_csv['Elec_Y18M06'] = 0
    df_csv['Elec_Y18M07'] = 0
    df_csv['Elec_Y18M08'] = 0
    df_csv['Elec_Y18M09'] = 0
    df_csv['Elec_Y18M10'] = 0
    df_csv['Elec_Y18M11'] = 0
    df_csv['Elec_Y18M12'] = 0
    df_csv['Elec_intensity_Y17'] = 3 #????Que es????
    df_csv['Elec_intensity_Y18'] = 3 #????Que es????
    df_csv['Elec_annual_cost'] = round(suma_anuales)
    df_csv['Gas_Y17M01'] = 0
    df_csv['Gas_Y17M02'] = 0
    df_csv['Gas_Y17M03'] = 0
    df_csv['Gas_Y17M04'] = 0
    df_csv['Gas_Y17M05'] = 0
    df_csv['Gas_Y17M06'] = 0
    df_csv['Gas_Y17M07'] = 0
    df_csv['Gas_Y17M08'] = 0
    df_csv['Gas_Y17M09'] = 0
    df_csv['Gas_Y17M10'] = 0
    df_csv['Gas_Y17M11'] = 0
    df_csv['Gas_Y17M12'] = 0
    df_csv['Gas_Y18M01'] = 0
    df_csv['Gas_Y18M02'] = 0
    df_csv['Gas_Y18M03'] = 0
    df_csv['Gas_Y18M04'] = 0
    df_csv['Gas_Y18M05'] = 0
    df_csv['Gas_Y18M06'] = 0
    df_csv['Gas_Y18M07'] = 0
    df_csv['Gas_Y18M08'] = 0
    df_csv['Gas_Y18M09'] = 0
    df_csv['Gas_Y18M10'] = 0
    df_csv['Gas_Y18M11'] = 0
    df_csv['Gas_Y18M12'] = 0
    # Create an outputs directoty if there isn't one.
    if not os.path.exists(citybes): os.makedirs(citybes)

    now = datetime.now()
    if now.day<10:
        day='0'+str(now.day)
    else:
        day=now.day
    if now.month<10:
        month= '0'+str(now.month)
    else:
        month= now.month
    fecha = str(day)+str(month)+str(now.year)
    df_csv.to_csv(citybes+'chile_dataset_'+fecha+'.csv',index=False)
    #,encoding='utf-8-sig'