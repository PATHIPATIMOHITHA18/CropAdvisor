soil_data = {
    "black soil": {
        "N": 82,
        "P": 41,
        "K": 48,
        "ph": 6.8
    },
    "red soil": {
        "N": 55,
        "P": 30,
        "K": 35,
        "ph": 6.2
    },
    "alluvial soil": {
        "N": 70,
        "P": 45,
        "K": 55,
        "ph": 7.0
    },
    "laterite soil": {
        "N": 45,
        "P": 25,
        "K": 30,
        "ph": 5.8
    },
    "clay soil": {
        "N": 75,
        "P": 40,
        "K": 50,
        "ph": 7.2
    },
    "sandy soil": {
        "N": 40,
        "P": 20,
        "K": 25,
        "ph": 6.0
    }
}

def get_soil(soil_type):
    return soil_data.get(soil_type.lower())