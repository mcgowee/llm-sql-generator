
# LLM SQL Generator Project

## Overview
This project generates SQL queries using a Large Language Model (LLM) based on natural language questions. It then executes the queries on the Northwind SQLite database and returns the results to the user. This tool demonstrates the practical use of natural language processing (NLP) for database interaction.

## Requirements
- Python 3.11.0 or higher
- Virtual environment setup (recommended but optional)

## Setup Instructions

### 1. Download and Extract the Project
1. Download the provided project ZIP file.
2. Extract the contents to a folder on your computer.
3. It is recommended to create a virtual environment in the next set of instructions.

### 2. Create and Activate a Virtual Environment

#### On Windows:
1. Open PowerShell and navigate to the project directory.
2. Create the virtual environment:
   ```
   python -m venv venv
   ```
3. Activate the virtual environment:

   On Command Prompt:
   ```
   venv\Scripts\Activate
   ```

   On Windows (PowerShell):
   ```
   .\venv\Scripts\Activate
   ```

#### On Linux or WSL:
1. Open a terminal and navigate to the project directory.
2. Create the virtual environment:
   ```
   python3 -m venv venv
   ```
3. Activate the virtual environment:
   ```
   source venv/bin/activate
   ```

### 3. Install Dependencies
Install the necessary Python packages:
```
pip install -r requirements.txt
```

### 4. Configure the OpenAI API Key
An OpenAI API key has been provided for this assighmnet, but will expire after a certain time.
This temporary API key is in the .env file.
Follow the instructions below to use your own OpenAI API Key.

#### Add your own API key to the .env File
1. Open the `.env` file and replace the placeholder with your API key:
   ```
   OPENAI_API_KEY=your_openai_api_key_here
   ```

**Note:** The current API key is temporary and will be deactivated.

### 5. Running the Project
Make sure you are in the project directory, then run the program:
```
python main.py
```

## Notes
- Ensure Python 3.11.0 or higher is installed on your system.
- The Northwind database must remain in the `data/` folder to function correctly.
- If you encounter any issues, verify that you are running the program from the correct directory.
