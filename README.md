# Generate Transcript Project

## Overview

This project allows users to download audio from a YouTube video and generate its transcript using an API. It is structured into multiple Python files for better organization and maintainability.

## Project Structure

```
generate-transcript/
│── main.py                # Entry point of the project
│── config.py              # Loads environment variables (dotenv)
│── downloader.py          # Handles YouTube audio downloads
│── transcript.py          # Handles transcript generation
│── requirements.txt       # Dependencies
│── .env                   # Environment variables (ignored in .gitignore)
└── utils.py               # Helper functions
```

## Installation

### Prerequisites

- Python 3.8+
- `pip` (Python package manager)

### Steps

1. **Clone the repository** 📥:

   ```sh
   git clone https://github.com/your-username/generate-transcript.git
   cd generate-transcript
   ```

2. **Create and activate a virtual environment** 🛠️:

   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   ```

3. **Install dependencies** 📦:

   ```sh
   pip install -r requirements.txt
   ```

   📌 _You can also check the `requirements.txt` file directly:_ [requirements.txt](./requirements.txt)

4. **Set up the environment variables** 🔐:
   - Create a `.env` file in the root directory.
   - Add your API key in the `.env` file:
     ```sh
     GROQ_API_KEY=your_api_key_here
     ```

## Usage 🚀

1. **Run the script**:
   ```sh
   python main.py
   ```
2. **Enter the YouTube URL** when prompted.
3. **The audio will be downloaded, and the transcript will be generated and displayed.**

## Quick Links 🔗

- 📂 **Repository:** [GitHub Repository](https://github.com/your-username/generate-transcript)
- 📜 **Requirements:** [requirements.txt](./requirements.txt)
- 🔑 **Environment Setup:** [.env file setup](./.env)

## Dependencies 🛠️

- `yt-dlp`
- `dotenv`
- `requests`

## License 📜

This project is licensed under the MIT License.
