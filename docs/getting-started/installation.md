# Installation

This guide will help you set up the Aspectify development environment.

## Prerequisites

- Python 3.10
- pip (Python package installer)
- Git

## Step 1: Clone the Repository

```bash
git clone https://github.com/hanifekaptan/Aspectify.git
cd Aspectify
```

## Step 2: Create a Virtual Environment

```bash
python -m venv .venv
```

#### Windows:
```bash
.venv\Scripts\activate
```

#### macOS/Linux:
```bash
source .venv/bin/activate
```

## Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

## Step 4: Configure the Environment

Create a `.env` file in the project's root directory:

```env
GOOGLE_API_KEY=your_google_api_key_here
LOG_LEVEL=INFO
PROJECT_NAME="Aspectify"
PROJECT_VERSION="1.0.0"
```

## Step 5: Verify the Installation

Verify that everything is working by running the test script:

```bash
python main.py
```

You should see an output similar to this:

```
--------------------------------------------------
Reading test data and performing sentiment analysis...
--------------------------------------------------

Analyzed Text: The camera of the new phone I bought takes great photos, but the battery barely lasts a day.
Expected Sentiment: neutral
Agent Result (Polarity): neutral
Agent Result (Score): 0.5
Agent Result (Aspects): [AspectAnalysisResponse(aspect='camera', sentiment='positive', score=0.98), AspectAnalysisResponse(aspect='battery', sentiment='negative', score=0.99)]
```

## Troubleshooting

### Common Issues

1. **ModuleNotFoundError**: Make sure you have activated the virtual environment.
2. **API Key Error**: Check that your Google API key is set correctly in the `.env` file.

### Getting a Google API Key

1. Visit [Google AI Studio](https://aistudio.google.com/)
2. Create a new project or select an existing one
3. Create an API key
4. Copy the key into your `.env` file

## Next Steps

- [Configuration](configuration.md) - Learn about the application configuration
- [Quick Start](quick-start.md) - Run your first analysis