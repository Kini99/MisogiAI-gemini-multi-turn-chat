import os
from typing import List, Dict
from dotenv import load_dotenv
from google import genai
from google.genai import types

load_dotenv()

def get_user_input(prompt: str) -> str:
    return input(prompt).strip()

def main():
    client = genai.Client(api_key=os.getenv('GEMINI_API_KEY'))

    # First turn
    first_input = get_user_input("Enter your first message: ")
    response = client.models.generate_content(
        model="gemini-1.5-pro",
        contents=[first_input],
        config=types.GenerateContentConfig(
            system_instruction="You are a helpful assistant that provides clear and concise responses.",
            max_output_tokens=500,
            temperature=0.7
        )
    )
    print("\nGemini's response:", response.text)

    # Second turn
    second_input = get_user_input("\nEnter your second message: ")
    response = client.models.generate_content(
        model="gemini-1.5-pro",
        contents=[first_input, second_input],
        config=types.GenerateContentConfig(
            system_instruction="You are a helpful assistant that provides clear and concise responses.",
            max_output_tokens=500,
            temperature=0.7
        )
    )
    print("\nGemini's second response:", response.text)
    
    # Third turn
    third_input = get_user_input("\nEnter your third message: ")
    response = client.models.generate_content(
        model="gemini-1.5-pro",
        contents=[first_input, second_input, third_input],
        config=types.GenerateContentConfig(
            system_instruction="You are a helpful assistant that provides clear and concise responses.",
            max_output_tokens=500,
            temperature=0.7
        )
    )
    print("\nGemini's third response:", response.text)

if __name__ == "__main__":
    main()

