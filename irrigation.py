def irrigation_advice(temp, humidity, rainfall):

    if rainfall >= 150:
        return "No irrigation is required because sufficient rainfall has been received."

    elif rainfall >= 75:
        return "Light irrigation is recommended as the soil may already contain enough moisture."

    elif temp >= 32 and humidity <= 60:
        return "High irrigation is recommended due to hot and dry weather."

    elif temp >= 28:
        return "Moderate irrigation is recommended."

    else:
        return "Normal irrigation is sufficient under the current weather conditions."