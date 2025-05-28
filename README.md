# Gemini Multi-turn Chat

A simple interactive chatbot using the Google Gemini API that supports multi-turn conversations with context preservation.

## Features

- Interactive console-based chat interface
- Multi-turn conversation support with context preservation
- Configurable model parameters (temperature)
- Simple and easy to use

## Setup

1. Clone the Repository

```bash
git clone https://github.com/Kini99/MisogiAI-gemini-multi-turn-chat.git
cd first-openai-api-call
```

2. Create a virtual environment and activate it:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Get your Gemini API key:
   - Go to [Google AI Studio](https://makersuite.google.com/app/apikey)
   - Create a new API key
   - Copy the API key

5. Create a `.env` file:
   - Copy the `.env.example` file to `.env`
   - Replace `your-api-key-here` with your actual Gemini API key
   ```bash
   cp .env.example .env
   ```
   Then edit the `.env` file and add your API key:
   ```
   GEMINI_API_KEY=your-actual-api-key-here
   ```

## Usage

Run the script:
```bash
python gemini_chat.py
```

The script will:
1. Prompt you for your first message
2. Show Gemini's response
3. Prompt you for a follow-up message
4. Show Gemini's final response

## Example

```
Enter your first message: What is the capital of France?
Gemini's response: The capital of France is Paris.

Enter your second: What is its population?
Gemini's second response: As of 2023, the population of Paris is approximately 2.2 million people within the city limits, and about 11 million in the metropolitan area.

Enter your third: What is its language?
Gemini's third response: The native language of France is French.