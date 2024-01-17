**ReadMe File for FunctionalTestPOC**

## Prerequisites

Before using the FunctionalTestPOC code, ensure that you have the following prerequisites:

1. **ChatGPT API Access**: Obtain access to the OpenAI ChatGPT API. You need an API key to interact with the OpenAI models.

2. **Python Installation**: Make sure Python is installed on your machine. The code is compatible with Python 3.11 and above.

3. **Required Packages**: Install the necessary Python packages using the following command:

   ```bash
   pip install openai requests wheel configparser
   ```

## Configuration

1. **API Key Configuration**:
   - Open the `constant.py` file located at `FunctionalTestPOC/ChatGPTAutoTestCaseCreation/constant.py`.
   - Set the `APIKEY` property to your ChatGPT API key.

2. **Test Data Configuration**:
   - Update other properties in the `config.properties` file as per your project requirements.

3. **Prompt Configuration**:
   - Open the `Prompt.properties` file located at `FunctionalTestPOC/TestData/Prompt.properties`.
   - Set the prompt-related properties according to your test cases.

## Usage

### Running the Code

1. Execute the Python script:
   ```bash
   python ChatGPTAPIEndPoint.py
   ```

### Options

- **Feature File Generation**:
  - Set `Generate_FeatureFile` to `'yes'` in the `config.properties` file to generate feature files.

- **Step Definition File Generation**:
  - Set `Generate_StepDefFile` to `'yes'` in the `config.properties` file to generate step definition files.

- **Page Object Generation**:
  - Set `Generate_PageObject` to `'yes'` in the `config.properties` file to generate page object files.

### Generated Files

- **Feature Files**:
  - Located at the path specified in `featurefile_folder_path`.

- **Step Definition Files**:
  - Located at the path specified in `stepdef_folder_path_new`.

- **Page Object Files**:
  - Located at the path specified in `pathOfPageObject`.

## Troubleshooting

If you encounter any issues or errors, refer to the following troubleshooting steps:


1. **File Path Issues**:
   - Verify that the paths specified in the configuration files are correct and accessible.

2. **Python Version Compatibility**:
   - Confirm that the Python version is 3.7 or above.

3. **Package Installation**:
   - Double-check that all required Python packages are installed.

## Additional Information

For additional information or support, please contact [your contact information].

**Note:** This ReadMe assumes that you are familiar with ChatGPT and have access to the necessary resources. If not, refer to the OpenAI documentation for guidance.
