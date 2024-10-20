
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
   env\Scripts\Activate.ps1
   ```

   On Windows (PowerShell):
   ```
   .\venv\Scripts\Activate.ps1
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
Once the virtual environment is activated, install the necessary Python packages:
```
pip install -r requirements.txt
```

### 4. Configure the OpenAI API Key
To use the LLM features, you must provide an OpenAI API key.

1. Create a `.env` file in the root directory of the project (where `main.py` is located).
2. Add the following line to the `.env` file:
   ```
   OPENAI_API_KEY=your_openai_api_key_here
   ```
3. Replace `your_openai_api_key_here` with your actual OpenAI API key.

**Note:** This API key is temporary and will be deactivated on [insert expiration date]. Make sure to test the project before that time.

### 5. Running the Project
Make sure you are in the project directory, then run the program:
```
python main.py
```

### 6. Deactivate the Virtual Environment
When you are done, deactivate the virtual environment:
```
deactivate
```

## Notes
- Ensure Python 3.11.0 or higher is installed on your system.
- The Northwind database must remain in the `data/` folder to function correctly.
- If you encounter any issues, verify that you are running the program from the correct directory.
