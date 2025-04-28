import json
import pandas as pd

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
        self.new_row['floor_ratio'] = self.new_row['floor'] / self.new_row['number_of_floors']
        self.new_row['age'] = 2025 - self.new_row['construction_year']
        self.new_row['area_per_room'] = self.new_row['total_area'] / (self.new_row['number_of_rooms'] + 1)
        self.new_row['height_age_ratio'] = self.new_row['ceiling_height'] / (self.new_row['age'] + 1)
        self.new_row['density'] = self.new_row['living_area'] / self.new_row['total_area']
        
        
    def standart_scale(self):        
        for col in self.data["scaling"]:
            mean = self.data["scaling"][col]["mean"]
            std = self.data["scaling"][col]["std"]
            self.new_row[col] = (self.new_row[col] - mean) / std
            
    def encoding(self):
        for col in self.data["encoding"]:
            self.new_row[f"{col}_encoded"] = self.data["encoding"][col][str(self.new_row[col])]
        
    
    def prep(self):
        self.import_data()
        self.generate_features()
        self.encoding()
        self.standart_scale()

        
        needed = ["min_to_metro", "total_area", "living_area", "number_of_floors", "construction_year", "ceiling_height", "floor_ratio", "age", "area_per_room", "height_age_ratio", "density", "region_of_moscow_encoded", "is_new_encoded", "is_apartments_encoded", "number_of_rooms_encoded", "floor_encoded"]
        needed_dict = {}
        for col in needed:
            needed_dict[col] = [self.new_row[col]]
            
            
        df = pd.DataFrame(needed_dict)
        return df
    