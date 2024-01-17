import time
import openai
import requests
import os
from wheel.metadata import generate_requirements
import configparser
import constant


#Read API key From config file
config =configparser.RawConfigParser()
print(config.sections())
#_____________Reading config property files________________________

# Creating the path to the properties file
# Get the current working directory
script_directory = os.path.dirname(os.path.abspath(__file__))
parent_directory = os.path.dirname(script_directory)
configFilePath = os.path.join(parent_directory, 'TestData', 'config.properties')


config.read(configFilePath)
featurefile_folder_path = config.get('details','featurefile_folder_path')
stepdef_folder_path = config.get('details','stepdef_folder_path_new')
Requirement_File_path = config.get('details','Requirement_File_path')
Generate_FeatureFile = config.get('details','Generate_FeatureFile')
Generate_StepDefFile = config.get('details', 'Generate_StepDefFile')
PathOfFeatureFile_generateStepdef = config.get('details','PathOfFeatureFile_generateStepdef')
nameOf_featureFile = config.get('details','nameOf_featureFile')
nameOf_StepDefFile = config.get('details','nameOf_StepDefFile')
Generate_PageObject = config.get('details','Generate_PageObject')
pathOfPageObject = config.get('details','pathOfPageObject')
nameOf_PageObjectFile = config.get('details','nameOf_PageObjectFile')
PathOftheUrl_DOM = config.get('details','PathOftheUrl_DOM')
prompt_applicationURL = config.get('details','Application_URL')
prompt_applicationUserName = config.get('details','Username')
prompt_applicationPassword = config.get('details','Password')

#_____________Reading Prompt property files________________________
PromptFilePath = os.path.join(parent_directory, 'TestData', 'Prompt.properties')
config.read(PromptFilePath)
#api_key=config.get('prompts','Openapi_key')
prompt_feature1 = config.get('prompts','prompt_feature1')
prompt_feature2 = config.get('prompts','prompt_feature2')
prompt_stepImplementation = config.get('prompts','prompt_stepImplementation')
promptForPOMGeneration = config.get('prompts','promptForPOMGeneration')

# Set your API key
#openai.api_key = api_key
openai.api_key = constant.APIKEY
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

def get_prompt_from_requirementFileForPOM():


    file_path = os.path.abspath(PathOftheUrl_DOM)

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
    newPrompt=prompt_feature1 + os.linesep+prompt_applicationURL+ os.linesep+'UserName: '+prompt_applicationUserName+os.linesep+'Password: '+prompt_applicationPassword+ os.linesep+prompt + os.linesep+prompt_feature2
    #print(newPrompt)
    # Define the data (conversation and prompt)
    data = {
        "model":"gpt-3.5-turbo",
        "temperature": 0.2,
        "messages": [
            {"role": "system",
             "content": newPrompt
             }
        ]
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

def extract_APIResponse_ForthePromptPOM():
    # prompt = "Generate step implementation for the above feature file in java language Without any additional introductory text."
    # Define the data (conversation and prompt)
    promptNew = promptForPOMGeneration +os.linesep+prompt_applicationURL+os.linesep+'UserName: '+prompt_applicationUserName+'Password: '+os.linesep+prompt_applicationPassword+os.linesep+get_prompt_from_requirementFileForPOM()
    print(promptNew)
    data = {
        "model":"gpt-3.5-turbo",
        "temperature": 0.2,
        "messages": [
            {"role": "system",
             "content": promptNew
             }
        ]
    }


    # Make a POST request to the API
    response = requests.post(endpoint_url, headers=headers, json=data)

    # Get the response content (the assistant's reply)
    # Extract the assistant's reply
    assistant_reply= response.json()['choices'][0]['message']['content']
    # Use the assistant's reply
    #print("Constructed prompt" +assistant_reply)
    return assistant_reply
def extract_APIResponse_ForthePrompt():
    # prompt = "Generate step implementation for the above feature file in java language Without any additional introductory text."
    # Define the data (conversation and prompt)
    PromptSecond= prompt_stepImplementation + prompt1_res_feature;
    data = {
        "model":"gpt-3.5-turbo",
        "temperature": 0.2,
        "messages": [
            {"role": "system", "content": PromptSecond}
        ]}
    # Make a POST request to the API
    response = requests.post(endpoint_url, headers=headers, json=data)

    # Get the response content (the assistant's reply)
    # Extract the assistant's reply
    assistant_reply = response.json()['choices'][0]['message']['content']
    # Use the assistant's reply
    #print(assistant_reply)
    return assistant_reply

def generate_OnlyStepDefFileForGiven_featurefile():
    # prompt = "Generate step implementation for the above feature file in java language Without any additional introductory text."
    # Define the data (conversation and prompt)
    with open(PathOfFeatureFile_generateStepdef, "r") as file:
       featurefileData=file.read()
       #featurefileData = extract_APIResponse_ForFeatureFile()
    PromptSecond= prompt_stepImplementation + featurefileData;
    data = {
        "model":"gpt-3.5-turbo",
        "temperature": 0.2,
        "messages": [
            {"role": "system", "content": PromptSecond}
        ]}
    # Make a POST request to the API
    response = requests.post(endpoint_url, headers=headers, json=data)

    # Get the response content (the assistant's reply)
    # Extract the assistant's reply
    assistant_reply = response.json()['choices'][0]['message']['content']
    # Use the assistant's reply
   # print(assistant_reply)
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
def generate_javafile_For_PageObject(api_response, class_name):
    # Get the current directory of the script
    script_directory = os.path.dirname(os.path.abspath(__file__))
    # Path to the folder where you want to save the Java file
    #folder_name = "generatedJavaFiles"
    # folder_path = os.path.join(script_directory)
    folder_path = os.path.abspath(pathOfPageObject)

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

if (Generate_FeatureFile.lower() == 'yes' and Generate_StepDefFile.lower() == 'no'):
    generate_featurefile_from_api_response(extract_APIResponse_ForFeatureFile(), nameOf_featureFile)
    # print("generated only feature file")
elif (Generate_FeatureFile.lower() == 'yes' and Generate_StepDefFile.lower() == 'yes'):
    generate_featurefile_from_api_response(extract_APIResponse_ForFeatureFile(), nameOf_featureFile)
    generate_stepImplementationFile_For_FeatureFile(generate_OnlyStepDefFileForGiven_featurefile(), nameOf_StepDefFile)
    # print("generated both feature and step def files")
elif (Generate_FeatureFile.lower() == 'no' and Generate_StepDefFile.lower() == 'no'):
    print("no file is selected to generate")
else:
    print("Invalid combination of generation preferences")



if (Generate_PageObject.lower()=='yes'):
    generate_javafile_For_PageObject(extract_APIResponse_ForthePromptPOM(),nameOf_PageObjectFile)
