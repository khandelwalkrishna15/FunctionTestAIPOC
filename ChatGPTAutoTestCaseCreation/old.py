import time

import openai
import requests
import os
from wheel.metadata import generate_requirements
import configparser


#Read API key From config file
config =configparser.RawConfigParser()
print(config.sections())
configFilePath = r'C:\Users\tdhivya\IdeaProjects\untitled\venv\TestData\config.properties'
config.read(configFilePath)
print(config.get('details','Openapi_key'))
api_key=config.get('details','Openapi_key')
prompt=config.get('details','prompt')
featurefile_folder_path = config.get('details','featurefile_folder_path')
stepdef_folder_path = config.get('details','stepdef_folder_path')
Requirement_File_path = config.get('details','Requirement_File_path')
# Set your API key
openai.api_key = api_key
prompt1_res_feature = " "
# Define the endpoint URL
endpoint_url = "https://api.openai.com/v1/chat/completions"  # Use the appropriate endpoint for your model

# Define the headers (including the API key)
headers = {
    "Authorization": f"Bearer {openai.api_key}",
    "Content-Type": "application/json"
}

def get_prompt_from_requirementFile():


    file_path = os.path.abspath(Requirement_File_path)

    try:
        with open(file_path, 'r') as file:
            file_content = file.read()
            print(file_content)
            file.close()
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")
    return  file_content
def extract_APIResponse_ForFeatureFile():
    prompt = get_prompt_from_requirementFile()
    newPrompt="Generate the Features files for below requitements "+prompt + " Without any additional introductory text."
    # Define the data (conversation and prompt)
    data = {
        "model":"gpt-3.5-turbo",

        "messages": [
            {"role": "system", "content": newPrompt}
        ],
        "temperature": 0.7
    }

    # Make a POST request to the API
    response = requests.post(endpoint_url, headers=headers, json=data)

    # Get the response content (the assistant's reply)
    # Extract the assistant's reply
    global prompt1_res_feature
    prompt1_res_feature = response.json()['choices'][0]['message']['content']
    # Use the assistant's reply
    print(prompt1_res_feature)
    return prompt1_res_feature

def extract_APIResponse_ForthePromptPOM(prompt1):
    # prompt = "Generate step implementation for the above feature file in java language Without any additional introductory text."
    # Define the data (conversation and prompt)
    promptNew = get_prompt_from_requirementFile(prompt1)
    data = {
        "model":"gpt-3.5-turbo",
        "messages": [
            {"role": "system", "content": promptNew}
        ]
    }

    # Make a POST request to the API
    response = requests.post(endpoint_url, headers=headers, json=data)

    # Get the response content (the assistant's reply)
    # Extract the assistant's reply
    assistant_reply= response.json()['choices'][0]['message']['content']
    # Use the assistant's reply
    print(assistant_reply)
    return assistant_reply
def extract_APIResponse_ForthePrompt():
    # prompt = "Generate step implementation for the above feature file in java language Without any additional introductory text."
    # Define the data (conversation and prompt)
    PromptSecond= prompt + prompt1_res_feature;
    data = {
        "model":"gpt-3.5-turbo",
        "messages": [
            {"role": "system", "content": PromptSecond}
        ]
    }

    # Make a POST request to the API
    response = requests.post(endpoint_url, headers=headers, json=data)

    # Get the response content (the assistant's reply)
    # Extract the assistant's reply
    assistant_reply = response.json()['choices'][0]['message']['content']
    # Use the assistant's reply
    print(assistant_reply)
    return assistant_reply

def generate_stepImplementationFile_For_FeatureFile(api_response, class_name):
    # Get the current directory of the script
    script_directory = os.path.dirname(os.path.abspath(__file__))
    # Path to the folder where you want to save the Java file
    #folder_name = "generatedJavaFiles"
    # folder_path = os.path.join(script_directory)
    folder_path = os.path.abspath(stepdef_folder_path)

    # Create the folder if it doesn't exist
    os.makedirs(folder_path, exist_ok=True)

    # Create a new Java file with the provided class name
    java_filename = f"{class_name}.java"
    java_file_path = os.path.join(folder_path, java_filename)

    with open(java_file_path, "w") as java_file:
        java_file.write(api_response)


def generate_featurefile_from_api_response(api_response, class_name):
    # Get the current directory of the script
    script_directory = os.path.dirname(os.path.abspath(__file__))

    # Path to the folder where you want to save the Java file
    #folder_name = "generatedJavaFiles"
    # folder_path = os.path.join(script_directory)
    folder_path = os.path.abspath(featurefile_folder_path)

    # Create the folder if it doesn't exist
    os.makedirs(folder_path, exist_ok=True)

    # Create a new Java file with the provided class name
    java_filename = f"{class_name}.feature"
    java_file_path = os.path.join(folder_path, java_filename)

    with open(java_file_path, "w") as java_file:
        java_file.write(api_response)
    time.sleep(10)
    generate_stepImplementationFile_For_FeatureFile(extract_APIResponse_ForthePrompt(),"Test")
    # generate_stepImplementationFile_For_FeatureFile(extract_APIResponse_ForthePromptFromFile("NewPageDOM.txt"),"PageObjectAI","PageObjects")

generate_featurefile_from_api_response(extract_APIResponse_ForFeatureFile(),"Test")
# get_prompt_from_requirementFile()
# generate_stepImplementationFile_For_FeatureFile(generate_featurefile_from_api_response(extract_APIResponse_ForFeatureFile(),"Test"))
