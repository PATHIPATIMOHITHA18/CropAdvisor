import pickle
import pandas as pd
import re

with open("models/crop_model.pkl", "rb") as file:
    model = pickle.load(file)


def extract_values(text):

    patterns = {
        "N": r"N\s*=\s*([0-9.]+)",
        "P": r"P\s*=\s*([0-9.]+)",
        "K": r"K\s*=\s*([0-9.]+)",
        "temperature": r"Temperature\s*=\s*([0-9.]+)",
        "humidity": r"Humidity\s*=\s*([0-9.]+)",
        "ph": r"pH\s*=\s*([0-9.]+)",
        "rainfall": r"Rainfall\s*=\s*([0-9.]+)"
    }

    values = {}

    for key, pattern in patterns.items():
        match = re.search(pattern, text, re.IGNORECASE)

        if match:
            values[key] = float(match.group(1))
        else:
            return None

    return values


def predict_crop(query):

    values = extract_values(query)

    if values is None:
        return None

    data = pd.DataFrame(
        [[
            values["N"],
            values["P"],
            values["K"],
            values["temperature"],
            values["humidity"],
            values["ph"],
            values["rainfall"]
        ]],
        columns=[
            "N",
            "P",
            "K",
            "temperature",
            "humidity",
            "ph",
            "rainfall"
        ]
    )

    prediction = model.predict(data)

    return prediction[0]