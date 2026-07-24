from crop_agent import crop_agent
from disease import get_disease
from irrigation import irrigation_advice

def crop_tool(location,soil):
    return crop_agent(location,soil)

def disease_tool(query):
    return get_disease(query)

def irrigation_tool(temp, humidity, rainfall):
    return irrigation_advice(
        temp,
        humidity,
        rainfall
    )