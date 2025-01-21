import joblib
import numpy as np

model = joblib.load('model/decision_tree_model.joblib')

def classify_waste(material_type, decomposition_time, source):
    predication = model.predict([[material_type, decomposition_time, source]])
    return predication[0]

def get_tips(classification):
    tips = {
         'Recyclable': 'Ensure recyclable items are clean and dry before disposal.',
        'Organic': 'Compost organic waste to create nutrient-rich soil.',
        'Hazardous': 'Dispose of hazardous waste at designated collection points.'
    }
    return tips.get(classification)
    