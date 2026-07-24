from weather import get_weather
from soil import get_soil
from crop import predict_crop


def crop_agent(location, soil):

    # -------------------------
    # Live Weather
    # -------------------------

    weather = get_weather(location)

    if weather is None:
        return "Unable to fetch weather for the given city."

    # -------------------------
    # Soil Data
    # -------------------------

    soil_data = get_soil(soil)

    if soil_data is None:
        return "Invalid soil type."

    # -------------------------
    # Crop Prediction
    # -------------------------

    crop_query = (
        f"N={soil_data['N']} "
        f"P={soil_data['P']} "
        f"K={soil_data['K']} "
        f"Temperature={weather['temperature']} "
        f"Humidity={weather['humidity']} "
        f"pH={soil_data['ph']} "
        f"Rainfall={weather['rainfall']}"
    )

    crop = predict_crop(crop_query)

    return {

        "location": location.title(),

        "soil": soil.title(),

        "weather": weather,

        "soil_values": soil_data,

        "crop": crop

    }