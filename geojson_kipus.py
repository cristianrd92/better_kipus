import json
from datetime import datetime
import os

s_path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
citybes = s_path + '/outputs_citybes/'

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

OUTPUT_GEOJSON = citybes+"chile_dataset_"+fecha+".geojson"

null = None
geojson2 = dict({"name": "CityBES_santiago_dataset_061419b", "crs": {"type": "name", "properties": {"name": "urn:ogc:def:crs:EPSG::2229"}}, "type": "FeatureCollection", "features": [{"type": "Feature", "properties": {"search_ind": None, "id": 1001, "UBID": "47RFH87X+CV", "search_index": "1001", "building_id": "", "shared_footprint": "", "institution": "Ministerio del Interior y Seguridad Publica", "use_type": "Office", "city": "Santiago", "address": "21 de Mayo  592", "year_built": "6", "cluster_probability": "1.0", "disaggregate_proportion_by_institution_floors": "1", "disaggregate_proportion_by_institution_area": "1", "gross_floor_area": None, "gross_floor_area_filled": "200", "old_gross_floor_area": "11077", "real_year_built": "1980", "num_floors": "7", "num_institution": "6", "institution_total_floor_area": "1200", "building_total_floor_area": "1400", "floor_height": "2.8", "building_height": "19.6", "department_name": "Direccion de Prevision de Carabineros de Chile", "latitude": "-33.436394", "longitude": "-70.650322", "wall_material": "Concret", "wall_insulation": "No isolation", "roof_insulation": "No isolation", "window_frame": "aluminium", "window_type": "Single", "wwr_norte": "30", "wwr_oriente": "40%", "wwr_poniente": "0%", "wwr_sur": "0%", "shading_type_norte": "alero", "shading_type_oriente": "alero", "shading_type_poniente": "no", "shading_type_sur": "no", "shading_percent_norte": "50", "shading_percent_oriente": "50", "shading_percent_poniente": "100", "shading_percentage_sur": "100%", "heating_type": "Gas", "air_conditioning": "Single", "lighting_system": "fluorescente", "Elec_Y17M01": "43768", "Elec_Y17M02": "37096", "Elec_Y17M03": "36482", "Elec_Y17M04": "40461", "Elec_Y17M05": "36568", "Elec_Y17M06": "36608", "Elec_Y17M07": "39074", "Elec_Y17M08": "37358", "Elec_Y17M09": "34795", "Elec_Y17M10": "0", "Elec_Y17M11": "2433", "Elec_Y17M12": "37346", "Elec_Y18M01": "35341", "Elec_Y18M02": "37911", "Elec_Y18M03": "37046", "Elec_Y18M04": "35634", "Elec_Y18M05": "32225", "Elec_Y18M06": "34469", "Elec_Y18M07": "38474", "Elec_Y18M08": "0", "Elec_Y18M09": "0", "Elec_Y18M10": "0", "Elec_Y18M11": "0", "Elec_Y18M12": "0", "Elec_intensity_Y17": "3", "Elec_intensity_Y18": "3", "Elec_annual_cost": "52139904", "Gas_Y17M01": "131.9795222", "Gas_Y17M02": "97.81569966", "Gas_Y17M03": "149.8976109", "Gas_Y17M04": "132.6279863", "Gas_Y17M05": "161.9112628", "Gas_Y17M06": "172.3549488", "Gas_Y17M07": "171.3651877", "Gas_Y17M08": "172.0136519", "Gas_Y17M09": "163.9249147", "Gas_Y17M10": "146.0409556", "Gas_Y17M11": "139.4539249", "Gas_Y17M12": "118.7030717", "Gas_Y18M01": "120.5802048", "Gas_Y18M02": "100.4778157", "Gas_Y18M03": "123.5494881", "Gas_Y18M04": "130.8532423", "Gas_Y18M05": "153.447099", "Gas_Y18M06": "163.9931741", "Gas_Y18M07": "196.8600683", "Gas_Y18M08": "195.6996587", "Gas_Y18M09": "0", "Gas_Y18M10": "0", "Gas_Y18M11": "0", "Gas_Y18M12": "0", "Gas_intensity_Y17": "0", "Gas_intensity_Y18": "0", "Gas_annual_cost": "108144.0614", "area": "28699.125", "perimeter": "", "department": null, "latitud": null, "long": None, "layer": None, "path": None, "cluster": "6"}, "geometry": {"type": "MultiPolygon", "coordinates": [[[[34660739.13288364, -22882465.068160176], [34660702.399118096, -22882406.91083627], [34660729.23041844, -22882389.751680564], [34660764.89599292, -22882447.45474032], [34660739.13288364, -22882465.068160176]]]]}}
,{"type": "Feature", "properties": {"search_ind": None, "id": 1249, "UBID": "47RFH958+QM", "search_index": "1249", "building_id": "", "shared_footprint": "", "institution": "Ministerio de las Culturas, las Artes y el Patrimonio", "use_type": "Office", "city": "Providencia", "address": "Vina del mar  27", "year_built": "8", "cluster_probability": "0.99", "disaggregate_proportion_by_institution_floors": "1", "disaggregate_proportion_by_institution_area": "1", "gross_floor_area": None, "gross_floor_area_filled": "322", "old_gross_floor_area": "322", "real_year_built": "1970", "num_floors": "2", "num_institution": "2", "institution_total_floor_area": "644", "building_total_floor_area": "644", "floor_height": "2.8", "building_height": "5.6", "department_name": "Servicio Nacional del Patrimonio Cultural", "latitude": "-33.440548", "longitude": "-70.633281", "wall_material": "Brick", "wall_insulation": "No isolation", "roof_insulation": "< 50mm isolation", "window_frame": "wood", "window_type": "Single", "wwr_norte": "30", "wwr_oriente": "0%", "wwr_poniente": "0%", "wwr_sur": "0%", "shading_type_norte": "no", "shading_type_oriente": "high build", "shading_type_poniente": "high build", "shading_type_sur": "no", "shading_percent_norte": "0", "shading_percent_oriente": "100", "shading_percent_poniente": "100", "shading_percentage_sur": "100%", "heating_type": "Gas", "air_conditioning": "Single", "lighting_system": "fluorescente", "Elec_Y17M01": "685", "Elec_Y17M02": "549", "Elec_Y17M03": "594", "Elec_Y17M04": "487", "Elec_Y17M05": "848", "Elec_Y17M06": "944", "Elec_Y17M07": "880", "Elec_Y17M08": "826", "Elec_Y17M09": "689", "Elec_Y17M10": "629", "Elec_Y17M11": "534", "Elec_Y17M12": "484", "Elec_Y18M01": "574", "Elec_Y18M02": "495", "Elec_Y18M03": "505", "Elec_Y18M04": "509", "Elec_Y18M05": "665", "Elec_Y18M06": "858", "Elec_Y18M07": "862", "Elec_Y18M08": "0", "Elec_Y18M09": "0", "Elec_Y18M10": "0", "Elec_Y18M11": "0", "Elec_Y18M12": "0", "Elec_intensity_Y17": "2", "Elec_intensity_Y18": "2", "Elec_annual_cost": "984449", "Gas_Y17M01": "0", "Gas_Y17M02": "0.273037543", "Gas_Y17M03": "0.102389078", "Gas_Y17M04": "7.406143345", "Gas_Y17M05": "25.6996587", "Gas_Y17M06": "33.99317406", "Gas_Y17M07": "36.45051195", "Gas_Y17M08": "36.14334471", "Gas_Y17M09": "22.21843003", "Gas_Y17M10": "14.06143345", "Gas_Y17M11": "4.675767918", "Gas_Y17M12": "0.443686007", "Gas_Y18M01": "1.126279863", "Gas_Y18M02": "2.116040956", "Gas_Y18M03": "3.105802048", "Gas_Y18M04": "3.515358362", "Gas_Y18M05": "26.48464164", "Gas_Y18M06": "37.98634812", "Gas_Y18M07": "0", "Gas_Y18M08": "0", "Gas_Y18M09": "0", "Gas_Y18M10": "0", "Gas_Y18M11": "0", "Gas_Y18M12": "0", "Gas_intensity_Y17": "0.068259386", "Gas_intensity_Y18": "0.034129693", "Gas_annual_cost": "11056.27986", "area": "6558.625", "perimeter": "0", "department": null, "latitud": null, "long": null, "layer": null, "path": null, "cluster": "8"}, "geometry": {"type": "MultiPolygon", "coordinates": [[[[34671449.8895337, -22880383.606566027], [34671477.621008106, -22880358.23059647], [34671537.4788522, -22880431.760646254], [34671509.077883445, -22880454.666196648], [34671449.8895337, -22880383.606566027]]]]}}]}) 
geojson = dict()
def crear_geojson(df_first,list_ubid,list_address,suma_anuales,list_pisos,list_area):
    id_ed = list()
    search = list()
    registros = len(list_ubid)
    #Generamos search_index de 1000 a x
    for x in range(1000,(registros+1000)):
        search.append(x)
    #Generamos building_id de 1 a x
    for x in range(1,(registros+1)):
        id_ed.append(x)
    # geojson = {"name": "CityBES_santiago_dataset_061419b", "crs": 
    # {"type": "name", "properties": 
    # {"name": "urn:ogc:def:crs:EPSG::2229"}}, "type": "FeatureCollection", "features":[{}]}
   
    edificios = dict()
    edificios['name'] = 'CityBES_chile_dataset_'+fecha
    edificios['crs'] = {"type": "name", "properties": {"name": "urn:ogc:def:crs:EPSG::2229"}}   
    edificios['type'] = 'FeatureCollection'
    edificios['features'] = list()
    
    for x in range (len(list_ubid)):
        edificio = dict()
        cluster = df_first.iloc[x]['cluster_a'],df_first.iloc[x]['cluster_b'],df_first.iloc[x]['cluster_c'],df_first.iloc[x]['cluster_d']
        edificio['search_id'] = 'null'
        edificio['id'] = int(id_ed[x])
        edificio['UBID'] = list_ubid[x]
        edificio['search_index'] = int(search[x])
        edificio['building_id'] = ''
        edificio['shared_footprint'] = ''
        edificio['institution'] = df_first.iloc[x]['institution']
        edificio['use_type'] = 'Office'
        edificio['city'] = df_first.iloc[x]['comuna']
        edificio['address'] = list_address[x]
        edificio['year_built'] = cluster
        edificio['cluster_probability'] = '1.0'
        edificio['disaggregate_proportion_by_institution_floors'] = '1'
        edificio['disaggregate_proportion_by_institution_area'] = '1'
        edificio['gross_floor_area'] = 'null'
        edificio['gross_floor_area_filled'] = int(df_first.iloc[x]['building_area'])
        edificio['old_gross_floor_area'] = int(df_first.iloc[x]['building_area'])
        edificio['real_year_built'] = '2000' #No se tiene año real de la construccion por lo cual se debe definir un metodo de calculo de este
        edificio['num_floors'] = int(df_first.iloc[x]['pisos']) #Pisos del edificio
        edificio['num_institution'] = int(df_first.iloc[x]['num_institution']) #Pisos ocupados por la insititucion
        edificio['institution_total_floor_area'] = int(df_first.iloc[x]['building_area'])
        edificio['building_total_floor_area'] = int(df_first.iloc[x]['building_area'])
        edificio['floor_height'] = 2.8
        edificio['building_height'] = int(df_first.iloc[x]['altura'])
        edificio['department_name'] = df_first.iloc[x]['building_name']
        edificio['latitude'] = df_first.iloc[x]['latitude']
        edificio['longitude'] = df_first.iloc[x]['longitude']
        edificio['wall_material'] = 'Concret'
        edificio['wall_insulation'] = 'No isolation'
        edificio['roof_insulation'] = 'No isolation'
        edificio['window_frame'] = 'aluminium'
        edificio['window_type'] = 'Single'
        edificio['wwr_norte'] = '30'
        edificio['wwr_oriente'] = '40%'
        edificio['wwr_poniente'] = '0%'
        edificio['wwr_sur'] = '0%'
        edificio['shading_type_norte'] = 'alero'
        edificio['shading_type_poniente'] = 'no'
        edificio['shading_type_sur'] = 'no'
        edificio['shading_percent_norte'] = '50'
        edificio['shading_percent_oriente'] = '50'
        edificio['shading_percent_poniente'] = '100'
        edificio['shading_percentage_sur'] = '100%'
        edificio['heating_type'] = df_first.iloc[x]['heating_type']
        edificio['air_conditioning'] = df_first.iloc[x]['air_conditioning']
        edificio['lighting_system'] = 'fluorescente'
        edificio['Elec_Y17M01'] = int(df_first.iloc[x]['m1'])
        edificio['Elec_Y17M02'] = int(df_first.iloc[x]['m2'])
        edificio['Elec_Y17M03'] = int(df_first.iloc[x]['m3'])
        edificio['Elec_Y17M04'] = int(df_first.iloc[x]['m4'])
        edificio['Elec_Y17M05'] = int(df_first.iloc[x]['m5'])
        edificio['Elec_Y17M06'] = int(df_first.iloc[x]['m6'])
        edificio['Elec_Y17M07'] = int(df_first.iloc[x]['m7'])
        edificio['Elec_Y17M08'] = int(df_first.iloc[x]['m8'])
        edificio['Elec_Y17M09'] = int(df_first.iloc[x]['m9'])
        edificio['Elec_Y17M10'] = int(df_first.iloc[x]['m10'])
        edificio['Elec_Y17M11'] = int(df_first.iloc[x]['m11'])
        edificio['Elec_Y17M12'] = int(df_first.iloc[x]['m12'])
        edificio['Elec_Y18M01'] = ''
        edificio['Elec_Y18M02'] = ''
        edificio['Elec_Y18M03'] = ''
        edificio['Elec_Y18M04'] = ''
        edificio['Elec_Y18M05'] = ''
        edificio['Elec_Y18M06'] = ''
        edificio['Elec_Y18M07'] = ''
        edificio['Elec_Y18M08'] = ''
        edificio['Elec_Y18M09'] = ''
        edificio['Elec_Y18M10'] = ''
        edificio['Elec_Y18M11'] = ''
        edificio['Elec_Y18M12'] = ''
        edificio['Elec_intensity_Y17'] = '3'
        edificio['Elec_intensity_Y18'] = '3'
        edificio['Elec_annual_cost'] = int(suma_anuales[x])
        edificio['Gas_Y17M01'] = ''
        edificio['Gas_Y17M02'] = ''
        edificio['Gas_Y17M03'] = ''
        edificio['Gas_Y17M04'] = ''
        edificio['Gas_Y17M05'] = ''
        edificio['Gas_Y17M06'] = ''
        edificio['Gas_Y17M07'] = ''
        edificio['Gas_Y17M08'] = ''
        edificio['Gas_Y17M09'] = ''
        edificio['Gas_Y17M10'] = ''
        edificio['Gas_Y17M11'] = ''
        edificio['Gas_Y17M12'] = ''
        edificio['Gas_Y18M01'] = ''
        edificio['Gas_Y18M02'] = ''
        edificio['Gas_Y18M03'] = ''
        edificio['Gas_Y18M04'] = ''
        edificio['Gas_Y18M05'] = ''
        edificio['Gas_Y18M06'] = ''
        edificio['Gas_Y18M07'] = ''
        edificio['Gas_Y18M08'] = ''
        edificio['Gas_Y18M09'] = ''
        edificio['Gas_Y18M10'] = ''
        edificio['Gas_Y18M11'] = ''
        edificio['Gas_Y18M12'] = ''
        edificio['Gas_intensity_Y17'] = '0'
        edificio['Gas_intensity_Y18'] = '0'
        edificio['Gas_annual_cost'] = '0'
        edificio['area'] = ''
        edificio['perimeter'] = ''
        edificio['department'] = 'mull'
        edificio['latitud'] = 'null'
        edificio['long'] = 'null'
        edificio['layer'] = 'null'
        edificio['path'] = 'null'
        edificio['cluster'] = cluster
        edificios['features'].append({"type": "Feature", "properties":edificio, "geometry":{"type": "MultiPolygon", "coordinates":[[[[34660739.13288364, -22882465.068160176], [34660702.399118096, -22882406.91083627], [34660729.23041844, -22882389.751680564], [34660764.89599292, -22882447.45474032], [34660739.13288364, -22882465.068160176]]]]}})
    
    #Generamos el archivo GEOJSON
    print("Se genero GeoJson")
    with open(OUTPUT_GEOJSON,'w') as f:
        json.dump(edificios,f)