diseases = {

    "Tomato - Early Blight": {
        "Symptoms": "Brown spots on older leaves with concentric rings.",
        "Cause": "Alternaria fungus",
        "Treatment": "Remove infected leaves and spray Mancozeb.",
        "Fertilizer": "NPK 10-10-20"
    },

    "Tomato - Late Blight": {
        "Symptoms": "Dark water-soaked patches on leaves and fruits.",
        "Cause": "Phytophthora infestans",
        "Treatment": "Use Copper fungicide and avoid overhead watering.",
        "Fertilizer": "NPK 12-12-17"
    },

    "Potato - Early Blight": {
        "Symptoms": "Small dark spots with yellow halos.",
        "Cause": "Alternaria solani",
        "Treatment": "Spray Chlorothalonil.",
        "Fertilizer": "NPK 15-15-15"
    },

    "Potato - Late Blight": {
        "Symptoms": "Large brown-black lesions on leaves and stems.",
        "Cause": "Phytophthora infestans",
        "Treatment": "Spray Metalaxyl or Mancozeb.",
        "Fertilizer": "NPK 12-12-17"
    },

    "Rice - Bacterial Leaf Blight": {
        "Symptoms": "Yellowing and drying from leaf tips.",
        "Cause": "Xanthomonas oryzae",
        "Treatment": "Use Copper-based bactericide and resistant varieties.",
        "Fertilizer": "Nitrogen + Potash"
    },

    "Rice - Brown Spot": {
        "Symptoms": "Brown circular spots on leaves.",
        "Cause": "Bipolaris oryzae fungus",
        "Treatment": "Spray Mancozeb.",
        "Fertilizer": "Balanced NPK"
    },

    "Rice - Leaf Smut": {
        "Symptoms": "Small black raised lesions on leaves.",
        "Cause": "Entyloma oryzae",
        "Treatment": "Apply Carbendazim.",
        "Fertilizer": "Balanced NPK"
    }
}


def get_disease(query):

    text = query.lower()

    if "tomato" in text and ("brown" in text or "spot" in text):
        return "Tomato - Early Blight", diseases["Tomato - Early Blight"]

    elif "tomato" in text and ("water" in text or "dark" in text):
        return "Tomato - Late Blight", diseases["Tomato - Late Blight"]

    elif "potato" in text and "late" in text:
        return "Potato - Late Blight", diseases["Potato - Late Blight"]

    elif "potato" in text:
        return "Potato - Early Blight", diseases["Potato - Early Blight"]

    elif "rice" in text and "bacterial" in text:
        return "Rice - Bacterial Leaf Blight", diseases["Rice - Bacterial Leaf Blight"]

    elif "rice" in text and "brown" in text:
        return "Rice - Brown Spot", diseases["Rice - Brown Spot"]

    elif "rice" in text and "smut" in text:
        return "Rice - Leaf Smut", diseases["Rice - Leaf Smut"]

    return None, None