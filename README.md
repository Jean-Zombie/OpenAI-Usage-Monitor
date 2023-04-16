# OpenAI Usage Monitor

A simple menu bar app for macOS to monitor your OpenAI API usage. The app shows the total usage cost for the current month and refreshes the information every minute.

**Note**: This app is designed to work on macOS only.

## Getting Started

These instructions will help you set up the project and run it on your local machine.

### Prerequisites

You'll need Python 3.6 or higher installed on your machine and macOS as your operating system.

### Installing

1. Clone this repository:

   ```
   git clone https://github.com/Jean-Zombie/OpenAI-Usage-Monitor.git
   cd OpenAI-Usage-Monitor
   ```

2. Create a virtual environment and activate it:

   ```
   python3 -m venv venv
   source venv/bin/activate
   ```

3. Install the required packages:

   ```
   pip install -r requirements.txt
   ```

4. Create a `.env` file in the project root directory and add your OpenAI API key:

   ```
   API_KEY=your_openai_api_key
   ```
   Replace `your_openai_api_key` with your actual API key.

### Running the App

To run the app in the background, open a terminal, navigate to the project directory, and execute the following command:

```
nohup python main.py &
```

Your terminal will be available for use after running the command or you could close it altogether.

To stop the app use `Quit` in it’s menu, or find its process ID and terminate it:

```
ps aux | grep main.py
kill <process_id>
```

Replace `<process_id>` with the actual process ID of your script.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
