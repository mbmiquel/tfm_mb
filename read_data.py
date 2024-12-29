import pandas as pd

def read_clean_dataset():
    format_df = {
        'ID': 'object',
        'Caracteristicas': 'object',
        'Habitaciones': 'int32',
        'Aseos': 'int32',
        'Terraza': 'int32',
        'Piscina': 'int32',
        'Garaje': 'int32',
        'Precio': 'int32',
        'Metros': 'int32',
        'CodigoPostal': 'object',
        'Latitud': 'float64',
        'Longitud': 'float64',
        'NPRO': 'object',
        'NCA': 'object',
        'NMUN': 'object',
        'PrecioM2': 'float64',
        'CUDIS': 'object'
    }
    df= pd.read_csv("output/clean_dataset.csv", dtype = format_df)[list(format_df.keys())]
    return df

def read_anomaly_detection_dataset():
    format_df = {
        'ID': 'object',
        'Caracteristicas': 'object',
        'Habitaciones': 'int32',
        'Aseos': 'int32',
        'Terraza': 'int32',
        'Piscina': 'int32',
        'Garaje': 'int32',
        'Precio': 'int32',
        'Metros': 'int32',
        'CodigoPostal': 'object',
        'Latitud': 'float64',
        'Longitud': 'float64',
        'NPRO': 'object',
        'NCA': 'object',
        'NMUN': 'object',
        'PrecioM2': 'float64',
        'CUDIS': 'object'
    }
    df= pd.read_csv("output/anomaly_detection.csv", dtype = format_df)[list(format_df.keys())]
    return df

def read_enhanced_dataset():
    format_df = {
        'ID': 'object',
        'Caracteristicas': 'object',
        'Habitaciones': 'int32',
        'Aseos': 'int32',
        'Terraza': 'int32',
        'Piscina': 'int32',
        'Garaje': 'int32',
        'Precio': 'int32',
        'Metros': 'int32',
        'CodigoPostal': 'object',
        'Latitud': 'float64',
        'Longitud': 'float64',
        'NPRO': 'object',
        'NCA': 'object',
        'NMUN': 'object',
        'PrecioM2': 'float64',
        'CUDIS': 'object',
        'RentaBrutaHogar': 'float64',
        'RentaBrutaPersona': 'float64',
        'poblacion_2023' : 'Int64',
        '%_servicios': 'float64',
        'densidad_inm_m2': 'float64',
        '%_agricultura': 'float64',
        '%_industria': 'float64',
        '%_construccion': 'float64',
    }
    df= pd.read_csv("output/enhanced.csv", dtype = format_df)[list(format_df.keys())]
    return df

def read_enhanced_microscore_dataset():
    format_df = {
        'ID': 'object',
        'Caracteristicas': 'object',
        'Habitaciones': 'int32',
        'Aseos': 'int32',
        'Terraza': 'int32',
        'Piscina': 'int32',
        'Garaje': 'int32',
        'Precio': 'int32',
        'Metros': 'int32',
        'CodigoPostal': 'object',
        'Latitud': 'float64',
        'Longitud': 'float64',
        'NPRO': 'object',
        'NCA': 'object',
        'NMUN': 'object',
        'PrecioM2': 'float64',
        'CUDIS': 'object',
        'RentaBrutaHogar': 'float64',
        'RentaBrutaPersona': 'float64',
        'poblacion_2023' : 'Int64',
        '%_servicios': 'float64',
        'densidad_inm_m2': 'float64',
        '%_agricultura': 'float64',
        '%_industria': 'float64',
        '%_construccion': 'float64',
        'University_Distance': 'float64',
        'School_Distance': 'float64',
        'Kindergarten_Distance': 'float64', 
        'City Center_Distance': 'float64',
        'Supermarket_Distance': 'float64', 
        'Bakery_Distance': 'float64', 
        'Hospital_Distance': 'float64',
        'Pharmacy_Distance': 'float64', 
        'Restaurant_Distance': 'float64', 
        'Café_Distance': 'float64',
        'Park_Distance': 'float64', 
        'Gym_Distance': 'float64', 
        'Movie Theater_Distance': 'float64',
        'Theater_Distance': 'float64', 
        'Shopping Mall_Distance': 'float64', 
        'Bus Stop_Distance': 'float64',
        'Metro Station_Distance': 'float64', 
        'Score': 'float64'
    }
    df= pd.read_csv("output/enhanced_microscore.csv", dtype = format_df)[list(format_df.keys())]
    return df
