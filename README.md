# Polsearch

A minimal command line tool that queries the Korean Law Portal for relevant judgments and summarizes applicable laws via an LLM.

## Setup

1. Install Python 3.9+ and create a virtual environment (optional).
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Set environment variables with your API keys:
   ```bash
   export LAW_API_KEY="<your-law-portal-key>"
   export OPENAI_API_KEY="<your-openai-key>"
   ```

## Usage
Run the script and enter the report text when prompted:

```bash
python src/main.py
```

The program will search relevant judgments and ask the LLM for applicable legal provisions.

