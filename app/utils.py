import json
import pandas as pd
import numpy as np

from app.messages import regoins_choices

def to_row(row: dict):
    row.pop("csrf_token")
    for col in row:
        row[col] = int(row[col])
        
    row["region_of_moscow"] = regoins_choices[row["region_of_moscow"]]
    return row


class DataRowModel():
    def __init__(self, row: dict):
        self.new_row = row
        
        
    def import_data(self):
        with open("app/static/data/data.json", "r") as file:
            self.data = json.load(file)      
            
    def generate_features(self):
        self.new_row['floor_ratio'] = self.new_row['floor'] / (self.new_row['number_of_floors'])
        self.new_row['age'] = np.maximum(2025 - self.new_row['construction_year'], 0)
        self.new_row['area_per_room'] = self.new_row['total_area'] / (self.new_row['number_of_rooms'])
        self.new_row['height_age_ratio'] = self.new_row['ceiling_height'] / (self.new_row['age'] + 1)
        self.new_row['density'] = self.new_row['living_area'] / self.new_row['total_area']
        self.new_row['metro_distance_inv'] = 1 / (self.new_row['min_to_metro'])
        self.new_row['is_new_area'] = self.new_row["living_area"] * self.new_row["is_new"]
        self.new_row['is_apartments_area'] = self.new_row["living_area"] * self.new_row["is_apartments"]
            
    def encoding(self):
        for col in self.data:
            self.new_row[f"{col}_encoded"] = self.data[col][str(self.new_row[col])]
        
    
    def prep(self):
        self.import_data()
        self.generate_features()
        self.encoding()

        
        needed = [
            'total_area',
            'number_of_floors',
            'ceiling_height',
            'floor_ratio',
            'age',
            'area_per_room',
            'density',
            'metro_distance_inv',
            'is_new_area',
            'is_apartments_area',
            'region_of_moscow_encoded'
        ]
        needed_dict = {}
        for col in needed:
            needed_dict[col] = [self.new_row[col]]
            
        df = pd.DataFrame(needed_dict)
        return df
    