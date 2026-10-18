# AI Brand Tweet Generator 🚀

An AI-powered web application built with Django that helps users generate **10 on-brand tweets** based on a brand's identity, tone, target audience, and content themes.

The application uses **Groq AI** to generate engaging tweets and **Tavily Search API** to research brand information from publicly available web sources.

## ✨ Features

- Generate 10 AI-powered tweets for any brand.
- Research brand information using the Tavily API.
- Analyze brand voice, tone, target audience, and content themes.
- Generate relevant and engaging tweet ideas.
- Simple and user-friendly interface.
- Copy generated tweets to the clipboard.

## 🛠️ Technologies Used

- Python
- Django
- HTML
- CSS
- JavaScript
- Groq API
- Tavily Search API

## 📋 Prerequisites

Before starting, make sure you have installed:

- Python 3.10 or later
- Git
- A code editor such as VS Code
- A Groq API key
- A Tavily API key

## 🚀 Installation and Setup

Follow these steps to run the project on your local machine.

### Step 1: Clone the Repository

Open your terminal or command prompt and run:

```bash
git clone https://github.com/KKSAGAR08/Tweet_Generator.git
```

Navigate to the cloned repository:

```bash
cd Tweet_Generator
```

### Step 2: Create a Virtual Environment

Create a Python virtual environment:

```bash
python -m venv venv
```

### Step 3: Activate the Virtual Environment

**For Windows (Command Prompt):**

```bash
venv\Scripts\activate
```

**For Windows (PowerShell):**

```powershell
.\venv\Scripts\Activate.ps1
```

**For Linux or macOS:**

```bash
source venv/bin/activate
```

After activation, you should see `(venv)` in your terminal.

### Step 4: Navigate to the Django Project

Move into the Django project directory:

```bash
cd ai_brand_tweet_generator
```

### Step 5: Install Dependencies

Install the required Python packages:

```bash
pip install -r requirements.txt
```

If `requirements.txt` is missing, make sure you have created and committed it in the `ai_brand_tweet_generator` directory before following this step.

### Step 6: Generate a Groq API Key

1. Visit [Groq Console](https://console.groq.com/).
2. Sign in or create an account.
3. Open the API Keys section.
4. Generate a new API key.
5. Copy the key and keep it private.

### Step 7: Generate a Tavily API Key

1. Visit [Tavily](https://tavily.com/).
2. Sign in or create an account.
3. Open your API key or dashboard section.
4. Generate or copy your API key.
5. Keep the key private.

### Step 8: Create the `.env` File

Inside the `ai_brand_tweet_generator` directory, create a file named `.env`.

Add your API keys in the following format:

```env
GROQ_API_KEY=your_groq_api_key_here
TAVILY_API_KEY=your_tavily_api_key_here
```

Replace the placeholder values with your actual API keys.

**Important:** Never upload your `.env` file to GitHub. Ensure that `.env` is included in your `.gitignore` file.

### Step 9: Run Database Migrations

Run the following command to prepare the Django database:

```bash
python manage.py migrate
```

### Step 10: Start the Django Development Server

Run:

```bash
python manage.py runserver
```

Open your browser and visit:

http://127.0.0.1:8000/

You can now use the AI Brand Tweet Generator to research a brand and generate 10 on-brand tweets.

## 📁 Project Structure

```text
Tweet_Generator/
├── ai_brand_tweet_generator/
│   ├── ai_brand_tweet_generator/
│   │   ├── settings.py
│   │   ├── urls.py
│   │   ├── asgi.py
│   │   └── wsgi.py
│   ├── tweet_generator/
│   │   ├── templates/
│   │   ├── static/
│   │   ├── views.py
│   │   ├── urls.py
│   │   ├── helper.py
│   │   └── models.py
│   ├── manage.py
│   ├── requirements.txt
│   └── .env
├── .gitignore
└── README.md
```

*Note: The `.env` file and virtual environment are local files and should not be committed to GitHub.*

## 🔐 Environment Variables

| Variable | Purpose |
|---|---|
| `GROQ_API_KEY` | Generates AI-powered tweets using Groq |
| `TAVILY_API_KEY` | Searches publicly available information for brand research |

## 🐛 Troubleshooting

**1. API key errors**

Check that your `.env` file is in the correct directory and that the variable names match those used in your Python code.

**2. Port already in use**

Start the server on another port:

```bash
python manage.py runserver 8001
```

Then visit http://127.0.0.1:8001/.

## 🔒 Security

- Do not commit API keys, passwords, or other secrets.
- Keep `.env` in `.gitignore`.
- If an API key is accidentally exposed, revoke or rotate it immediately.

GitHub: [@KKSAGAR08](https://github.com/KKSAGAR08)
