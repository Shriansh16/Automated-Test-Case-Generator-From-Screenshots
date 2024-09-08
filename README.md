Deployed Link: https://automated-test-case-generator-from-screenshots.streamlit.app/                                             

Demo Video: https://drive.google.com/file/d/13N8szUxezKMHs59GPg3AqJfIsasYbePs/view?usp=sharing                                                                                            
                                                                                                       
Documentation: Automated Test Case Generator from Screenshots                                                                                                          
Overview:
This application is designed to automate the process of generating detailed test cases from screenshots and optional context. It leverages Google’s Gemini API (Generative AI) to interpret the uploaded images and context, providing a step-by-step testing guide that can be used for quality assurance of digital products.

Key Features:
1. Image Upload and Processing: Users can upload multiple screenshots (in formats such as JPG, JPEG, PNG), which represent various features of a digital product. These images are processed and prepared as inputs for the Generative AI model.

2. Optional Context Input: The user has the option to provide additional context about the digital product. This helps the AI generate more precise and relevant test cases.

3. Integration with Google Gemini API: The application uses Google Generative AI (Gemini) to analyze the images and the provided context. Based on this, it generates comprehensive test cases that include descriptions, pre-conditions, steps for testing, and expected results.

4. Automated Test Case Generation: The core functionality of the app is to produce test cases that are easy to follow and detailed. The generated test case consists of:
    Description: A brief overview of what the test case covers.
    Pre-conditions: Any necessary setup or requirements that need to be met before performing the test.
    Testing Steps: Clear, numbered instructions for testing the features shown in the screenshots.
    Expected Result: The outcome that should occur if the feature works as intended.
5. Streamlit-Based UI: The application provides a clean and simple interface using Streamlit, where users can upload images, enter optional text, and submit a request to generate test cases. After submission, the generated test cases are displayed on the same interface.

Use Case:
This tool is ideal for quality assurance teams, developers, or product testers who work on digital products and need a streamlined way to generate test cases based on visual information (screenshots). It removes the need for manually writing test cases, speeding up the process and reducing human error.

Workflow:
1. Input Collection: Users provide screenshots of the product feature and optional context.

2. Processing: The uploaded screenshots and the input text are sent to the Gemini API for interpretation.

3. Content Generation: Based on the input, the AI generates a step-by-step testing guide with detailed instructions.

4. Output: The test case is displayed on the UI, ready for the user to review and implement.

Benefits:
1. Efficiency: Automates the process of generating test cases, saving time and effort.
2. Accuracy: Produces clear and detailed instructions that reduce the chances of missing critical steps in testing.
3. Scalability: Can handle multiple images and large contexts, generating comprehensive test cases for multiple features at once.

How to run?

1. Create a virtual environment using the command "conda create -p venv python==3.10 -y"                                    
2. Activate the environment using the command "conda activate venv"                                                         
3. Create a "secrets.toml" file in the project root directory and write this line:
4. GOOGLE_API_KEY="your google api key"                                                            
5. Install all the dependencies using the command "pip install -r requirements.txt"
6. Execute "app.py" using the command "streamlit run app1.py”
                                                                                      
