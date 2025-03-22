import json

def get_weather(location: str):
    """
    This tool returns a hardcoded weather string in Hindi.
    """
    return "Lucknow ke liye agle 3 din ka mausam: Halka barish aur 24-30°C temperature."

def recommend_crop(weather: str):
    """
    This tool recommends a crop based on the current weather conditions.
    """
    # Placeholder for crop recommendation logic
    if "Sunny" in weather:
        crop = "Rice"
    else:
        crop = "Wheat"
    return crop
