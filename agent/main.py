import os
from openai import OpenAI
from agent.tools import weather

openai = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def respond_to_query(query: str):
    """
    This function returns the assistant's response in Hindi.
    """

    # Use the tools
    weather_data = weather.get_weather(city="Delhi")
    crop_recommendation = weather.recommend_crop(weather=weather_data)

    # Construct the response in Hindi
    response = f"दिल्ली में मौसम का डेटा: {weather_data}, आपके लिए फसल की सिफारिश: {crop_recommendation}"
    return response

if __name__ == '__main__':
    query = "मुझे मौसम और फसल की जानकारी चाहिए"
    response = respond_to_query(query)
    print(response)
