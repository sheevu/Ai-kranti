import os
from openai import OpenAI
from agent.tools import weather

openai = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def respond_to_query(query: str) -> str:
    """
    AI-Kranti backend processor: returns assistant's response in Hindi
    """
    try:
        weather_data = weather.get_weather(city="Delhi")
        crop_recommendation = weather.recommend_crop(weather=weather_data)

        # Construct response in Hindi
        response = f"🌤️ दिल्ली का मौसम: {weather_data}\n🌾 सुझाई गई फसल: {crop_recommendation}"
        return response
    except Exception as e:
        return f"❌ त्रुटि हुई: {str(e)}"

if __name__ == "__main__":
    test_query = "मुझे मौसम और फसल की जानकारी चाहिए"
    print(respond_to_query(test_query))
