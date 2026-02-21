#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd

def preprocess_input(size, rooms, bathrooms, hasFurniture, municipality, hasBalcony, hasMetro, hasLift, hasGarage, isLuxury,                     property_Type):
    
    # Calculating the 'size_per_room' and 'total_rooms' variable
    total_rooms = rooms + bathrooms
    
    size_per_room = size / total_rooms
    
    if total_rooms > 10:
        total_rooms = 11
    
     # Transforming the 'rooms' variable
    if rooms > 5:
        rooms = 6
    
    # Transforming the 'municipality' variable into 'isCityCenter'
    city_center_municipalities = ['Santo António', 'Santa Maria Maior', 'Misericórida', 'Estrela', 'Avenidas Novas', 'Arroios',                                  'Campolide', 'São Vicente', 'Campo de Ourique']
    isCityCenter = 1 if municipality in city_center_municipalities else 0
    
    # Transforming the 'property_Type' variable into 'propertyType_duplex'
    propertyType_duplex = 1 if property_Type == 'duplex' else 0
    
    # Transforming boolean variables in 0 and 1
    hasFurniture = 1 if hasFurniture else 0
    hasBalcony = 1 if hasBalcony else 0
    hasMetro = 1 if hasMetro else 0
    hasLift = 1 if hasLift else 0
    hasGarage = 1 if hasGarage else 0
    isLuxury = 1 if isLuxury else 0
    
    # Creating a DataFrame with the preprocessed data
    data = pd.DataFrame({
        'size': [size],
        'rooms': [rooms],
        'hasLift': [hasLift],
        'hasGarage': [hasGarage],
        'isLuxury': [isLuxury],
        'total_rooms': [total_rooms],
        'size_per_room': [size_per_room],
        'hasFurniture': [hasFurniture],
        'hasBalcony': [hasBalcony],
        'hasMetro': [hasMetro],
        'isCityCenter': [isCityCenter],
        'propertyType_duplex': [propertyType_duplex]
    })
    
    return data

