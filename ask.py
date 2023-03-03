import openai
from API_KEY import KEY


# Instructions:

# Clone repository to a directory of your choosing
# "python -m venv venv"
# This will create a new venv for your project

# "source venv/bin/activate"
# This will activate your virtual environment

# "pip install openai"
# This will install the openai library to the virtual environment we setup

# Create a new .py file in the project directory and add a variable named KEY
# This var should be set to your openAI API key

# API keys can be created at https://platform.openai.com/account/api-keys
# You will need to create an account and sign up for the free trial to get an API KEY
# (The free trial does NOT require a credit card) This may have changed since Feb 1 2023

# Once you have added the api key, you can run the ask.py file
# "python ask.py"


class OpenAI:
    def __init__(self):
        # Set your API key
        openai.api_key = KEY
        self.model_engine = "text-davinci-003"

    def ask(self):
        completion = openai.Completion.create(
            engine=self.model_engine,
            prompt=input("Ask Text-Davinci-003:\n"),
            # Max tokens can be changed
            # 1000 Token equals 750 words
            max_tokens=800,
            # n is numer of responses
            n=1,
            stop=None,
            # Variability of answers
            # Higher values like 0.8 will make the output more random, 
            # while lower values like 0.2 will make it more focused and deterministic.
            # 0 - 2 Range
            temperature=0.7,
        )

        response = completion.choices[0].text
        print(response)
        return response


OpenAI().ask()
