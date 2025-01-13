# ollama-telegram-bot

A telegram bot that leverages the Ollama AI model for text processing.

## Getting started

Follow these steps to set up and run the application:

### 1. Install Ollama

Make sure you have the Ollama app installed on your machine. Download it from the [official Ollama website](https://ollama.com/) and follow the installation instructions for your platform.

### 2. Download the model

After installing Ollama, download the model you want to use (e.g., `llama3.2`). Run the following command in your terminal:

```
ollama pull llama3.2
```

### 3. Start the Ollama Server

Launch the Ollama app by running:

```
ollama serve
```

This will start the Ollama Server and make it accessible via `localhost:11434` by default.

### 4. Set up the environment file

Create a .env file in the root directory of the project, based on the provided .env.example file. Populate it with your API token and model name.

Example .env file:

```
API_TOKEN=your_telegram_api_token_here
LLAMA_MODEL=llama3.2
```

Replace your_telegram_api_token_here with your Telegram Bot API token and llama3.2 with the name of the model you downloaded.

### 5. Set up a virtual environment (optional but recommended)

1. Create a virtual environment:

   ```
   python -m venv venv
   ```

2. Activate the virtual environment:

   #### Windows

   ```
   venv\Scripts\activate
   ```

   #### macOS / GNU/Linux

   ```
   source venv/bin/activate
   ```

### 6. Install dependencies

Install the required Python libraries by running:

```
pip install -r requirements.txt
```

### 7. Run the application

Start the application by running:

```
python main.py
```

## The bot will now be up and running, connected to both your Telegram Bot and the Ollama model! 🚀