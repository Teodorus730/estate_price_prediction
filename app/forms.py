from flask_wtf import FlaskForm
from wtforms import IntegerField, FloatField, RadioField, DecimalField, SelectField
from wtforms.validators import NumberRange, AnyOf, InputRequired
from app.messages import *



class DataForm(FlaskForm): 
    min_to_metro = IntegerField(name=names["min_to_metro"], validators=[InputRequired(message=field_is_required_message),
                                                        NumberRange(min=normal_values["min_to_metro"][0], max=normal_values["min_to_metro"][1], message=normal_values_messages["min_to_metro"])])
    
    region_of_moscow = SelectField(name=names["region_of_moscow"], choices=regoins_choices.items(),
                                   validators=[InputRequired(message=field_is_required_message)])
    
    total_area = DecimalField(name=names["total_area"], validators=[InputRequired(message=field_is_required_message),
                                                        NumberRange(min=normal_values["total_area"][0], max=normal_values["total_area"][1], message=normal_values_messages["total_area"])])
    
    living_area = DecimalField(name=names["living_area"], validators=[InputRequired(message=field_is_required_message),
                                                        NumberRange(min=normal_values["living_area"][0], max=normal_values["living_area"][1], message=normal_values_messages["living_area"])])
   
    floor = IntegerField(name=names["floor"], validators=[InputRequired(message=field_is_required_message),
                                                        NumberRange(min=normal_values["floor"][0], max=normal_values["floor"][1], message=normal_values_messages["floor"])])
    
    number_of_floors = IntegerField(name=names["number_of_floors"], validators=[InputRequired(message=field_is_required_message),
                                                        NumberRange(min=normal_values["number_of_floors"][0], max=normal_values["number_of_floors"][1], message=normal_values_messages["number_of_floors"])])
    
    construction_year = IntegerField(name=names["construction_year"], validators=[InputRequired(message=field_is_required_message),
                                                        NumberRange(min=normal_values["construction_year"][0], max=normal_values["construction_year"][1], message=normal_values_messages["construction_year"])])
    
    is_new = RadioField(name=names["is_new"], choices=is_new_choices.items(), validators=[InputRequired(message=field_is_required_message)])
    
    is_apartments = RadioField(name=names["is_apartments"], choices=yes_no_choices.items(), validators=[InputRequired(message=field_is_required_message)])
    
    ceiling_height = DecimalField(name=names["ceiling_height"], validators=[InputRequired(message=field_is_required_message),
                                                        NumberRange(min=normal_values["ceiling_height"][0], max=normal_values["ceiling_height"][1], message=normal_values_messages["ceiling_height"])])
    
    number_of_rooms = RadioField(name=names["number_of_rooms"], choices=rooms_choices.items(), validators=[InputRequired(message=field_is_required_message)])
