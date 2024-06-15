# Dwarf in the Flask

Secure Programming Challenge Against SSTI

## Scenario
In this challenge, participants are tasked with addressing a Server-Side Template Injection (SSTI) vulnerability within a Python web application built using Flask. The current code allows users to submit a string via a URL parameter, which is then rendered within an HTML template and returned as the response. However, the lack of input validation and unsafe handling of the input exposes the application to potential exploitation, enabling users to inject and execute arbitrary code on the server.
  
Participants are required to identify the location of the vulnerability and fix the issue(s) to fortify the application's defenses against SSTI attacks. Successful resolution of the vulnerability demands that the application maintains its functionality while effectively neutralizing the identified security risk.
  
Submissions for this challenge must comprise solely of the amended code, confined within the **main.py** file.

## Requirements

- Python 3
- Git
- Quanchecker package

## Setup

### 1. Clone the Repository
   - Clone this repository to your local machine using the following command:
     ```
     git clone https://github.com/xhfmvls/Dwarf-in-the-Flask.git
     ```

### 2. Install Dependencies
   - Navigate to the project directory.
   - (Optional) Set up a virtual environment for the project:
     ```
     python -m venv venv
     source venv/bin/activate  # On Unix/Linux
     .\venv\Scripts\activate    # On Windows
     ```
   - Install the required dependencies using the following command:
     ```
     pip install -r requirements.txt
     ```

### 3. Run the Application
   - Run the Flask application using the following command:
     ```
     python main.py
     ```
   - The application will start running locally on `http://localhost:8080`.

## Testing and Submission

### 1. Testing Procedure
  - To run the test, execute the following command in your terminal:
    ```
    python checker.py
    ```
  - Before running the tests, ensure that you have installed the latest Quanchecker package. You can do so by executing:

    ```
    pip install quanchecker
    ```
    or
    ```
    pip install quanchecker --upgrade
    ```
  - Please note that the test cases executed (in the `checker.py` file) are only examples provided for your reference. There are additional test cases that are kept confidential and will only be run when you submit your code.


#### Input Format:
- **Description**: The input consists of a string representing a search term (of various length).

#### Output Format:
- **Description**: The expected output is an HTML page with the search term correctly rendered. If the input is invalid (e.g., contains characters or patterns that could enable a hacker to inject and execute arbitrary code), it is displayed as-is in the HTML page without being executed.

### 2. Submission Guidelines
   - Once you have fixed the vulnerability, upload your solution to the web application.
   - The web application will validate whether the code is secure against the complete prepared payload.

## Resources
- 
- [OWASP Web Security Testing Guide: Testing for SSTI](https://owasp.org/www-project-web-security-testing-guide/v41/4-Web_Application_Security_Testing/07-Input_Validation_Testing/18-Testing_for_Server_Side_Template_Injection)
- [OWASP Injection Cheet Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Injection_Prevention_Cheat_Sheet.html)
- [SSTI Payloads](https://github.com/swisskyrepo/PayloadsAllTheThings/tree/master/Server%20Side%20Template%20Injection)

## Credits
- **[xhfmvls](https://github.com/xhfmvls)** - Quan C Lead Developer
