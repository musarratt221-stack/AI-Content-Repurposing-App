# AI Content Repurposing Tool

A simple web app that takes a blog post, article, or transcript and instantly repurposes it into multiple ready-to-post formats — a Twitter/X thread, a LinkedIn post, an Instagram caption, and an email newsletter blurb — powered by Claude (Anthropic's AI model).

## What it does

Content creators and marketers often write one piece of long-form content and then spend extra time manually rewriting it for every platform. This tool automates that step: paste your content once, pick the formats and tone you want, and get platform-ready copy in seconds.

## Features

- Generate multiple content formats from a single source text
- Choose from four tones: Professional, Casual, Witty, Inspirational
- Character-limit awareness for Twitter/X and Instagram
- Clean, simple web interface — no coding needed to use it
- Powered by Claude's language model via the Anthropic API

## Tech Stack

- **Python**
- **Streamlit** — for the web interface
- **Anthropic API (Claude)** — for content generation
- **python-dotenv** — for secure API key management

## Setup Instructions

1. **Clone this repository**
   ```
   git clone https://github.com/yourusername/musarrat.git
   cd musarrat
   ```

2. **Install dependencies**
   ```
   pip install -r requirements.txt
   ```

3. **Add your API key**
   - Get a key from [console.anthropic.com](https://console.anthropic.com)
   - Rename `.env.example` to `.env`
   - Open `.env` and add your key:
     ```
     ANTHROPIC_API_KEY=your-key-here
     ```

4. **Run the app**
   ```
   streamlit run app.py
   ```
   Your browser will open automatically at `http://localhost:8501`.

## How to Use

1. Paste your blog post, article, or transcript into the text box.
2. Select which formats you want generated (Twitter thread, LinkedIn post, etc.).
3. Choose a tone.
4. Click **Generate**.
5. Copy any output using the copy icon in each result box.

## Project Structure

```
├── app.py              # Main Streamlit application
├── requirements.txt    # Python dependencies
├── .env.example         # Template for your API key (rename to .env)
└── README.md           # This file
```

## Future Improvements

- Support for additional platforms (Facebook, TikTok scripts, YouTube descriptions)
- Save/export generated content as a file
- Support for direct URL input instead of pasted text
- Option to regenerate a single format without redoing all of them

## License

This project is open for personal and commercial use. Feel free to fork and adapt it.
