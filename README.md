# Soccer Guru automated Bot

## Overview
The Soccer Guru automated Bot is a script that automates the process of claiming player rewards on the Soccer Guru game website. The bot is designed to be scheduled to run every hour, ensuring that players receive their rewards regularly.

## Features
- **Automated Reward Claiming**: The bot automates the login process and claims player rewards on the Soccer Guru website.
- **Scheduled Execution**: Configured to run every hour, ensuring timely reward claims.

## Requirements
- Python 3.x
- Selenium
- Microsoft Edge WebDriver
- dotenv

## Setup
1. Install Python 3.x: [Python Downloads](https://www.python.org/downloads/)
2. Install required dependencies:
    ```bash
    pip install selenium webdriver_manager python-dotenv
    ```
3. Download and install Microsoft Edge WebDriver: [Microsoft Edge WebDriver](https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/)
4. Create a `.env` file in the project directory with the following content:
    ```env
    login=your_soccer_guru_login
    password=your_soccer_guru_password
    ```
    Replace `your_soccer_guru_login` and `your_soccer_guru_password` with your actual credentials.

## Usage
1. Run the script manually:
    ```bash
    python your_script_name.py
    ```
2. **Schedule to Run Every Hour**:

    - **Unix/Linux (Using cron)**:
    
        Open your terminal and type:
        ```bash
        crontab -e
        ```
        Add the following line to run the script every hour:
        ```bash
        0 * * * * /path/to/your/python /path/to/your/script.py
        ```
        Replace `/path/to/your/python` with the path to your Python interpreter, and `/path/to/your/script.py` with the full path to your Python script. Save and exit the editor.

    - **Windows (Using Task Scheduler)**:

        1. Open Task Scheduler.
        2. Click "Create Basic Task...".
        3. Follow the wizard, specifying a name and description.
        4. Choose "Daily" trigger, set it to recur every 1 day, and set the start time.
        5. Choose "Start a Program" as the action.
        6. Browse and select the path to your Python executable as the program/script and the path to your script as the argument.
        7. Complete the wizard and save the task.


## License
This project is licensed under the [MIT License](LICENSE).
