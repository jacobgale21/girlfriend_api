# 🤖 ChatGPT API Task Processor

A comprehensive toolkit for using free ChatGPT APIs to process various tasks. This project demonstrates multiple ways to integrate AI capabilities into your applications using different free API options.

## 🚀 Features

- **Multiple API Support**: OpenAI, Anthropic Claude, Hugging Face, and Ollama
- **Free Tier Options**: All APIs offer free tiers or completely free usage
- **Web Interface**: Interactive web application for testing APIs
- **Task Processing**: Pre-built functions for common AI tasks
- **Easy Integration**: Simple Python classes for quick implementation

## 📋 Prerequisites

- Python 3.8+
- API keys for the services you want to use (see setup instructions)

## 🛠️ Installation

1. **Clone or download the project files**

2. **Install dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables**:
   - Copy `env_example.txt` to `.env`
   - Add your API keys to the `.env` file

## 🔑 API Setup

### 1. OpenAI API (Recommended - $5/month free credit)

- Visit [OpenAI Platform](https://platform.openai.com/)
- Create an account and get your API key
- Add to `.env`: `OPENAI_API_KEY=your_key_here`

### 2. Anthropic Claude API (Free tier available)

- Visit [Anthropic Console](https://console.anthropic.com/)
- Create an account and get your API key
- Add to `.env`: `ANTHROPIC_API_KEY=your_key_here`

### 3. Hugging Face API (Free tier available)

- Visit [Hugging Face](https://huggingface.co/settings/tokens)
- Create an account and get your API key
- Add to `.env`: `HUGGINGFACE_API_KEY=your_key_here`

### 4. Google Gemini API (Free tier available)

- Visit [Google AI Studio](https://makersuite.google.com/app/apikey)
- Create an account and get your API key
- Add to `.env`: `GOOGLE_GEMINI_API_KEY=your_key_here`

### 5. Ollama (Completely Free - Local)

- Install Ollama from [ollama.ai](https://ollama.ai/)
- Run: `ollama pull llama2`
- No API key needed!

## 🎯 Usage Examples

### Basic Usage

```python
from chatgpt_apis import ChatGPTAPIs

# Initialize
ai = ChatGPTAPIs()

# Simple chat
response = ai.openai_chat("Write a short story about a robot")
print(response)

# Use different APIs
response = ai.anthropic_claude("Explain quantum computing")
response = ai.google_gemini("Write a Python function to sort a list")
response = ai.ollama_local("Write a Python function to sort a list")
```

### Task Processing

```python
from task_examples import TaskProcessor

processor = TaskProcessor()

# Code review
result = processor.code_review_and_improve("""
def calculate_average(numbers):
    total = 0
    for num in numbers:
        total += num
    return total / len(numbers)
""")

# Content generation
result = processor.generate_content("artificial intelligence", "blog_post")

# Data analysis
result = processor.analyze_data([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], "trend")
```

### Web Application

1. **Start the web server**:

   ```bash
   python app.py
   ```

2. **Open your browser** to `http://localhost:8000`

3. **Use the interactive interface** to test different APIs and tasks

## 📊 API Comparison

| API                  | Cost            | Best For              | Setup Difficulty |
| -------------------- | --------------- | --------------------- | ---------------- |
| **OpenAI**           | $5/month free   | General tasks, coding | Easy             |
| **Anthropic Claude** | Free tier       | Analysis, reasoning   | Easy             |
| **Hugging Face**     | Free tier       | Specific models       | Medium           |
| **Google Gemini**    | Free tier       | Multimodal, creative  | Easy             |
| **Ollama**           | Completely free | Privacy, offline use  | Medium           |

## 🎨 Task Examples

### 1. Code Review & Improvement

```python
code = """
def calculate_average(numbers):
    total = 0
    for num in numbers:
        total += num
    return total / len(numbers)
"""

result = processor.code_review_and_improve(code)
```

### 2. Content Generation

```python
# Blog post
result = processor.generate_content("machine learning", "blog_post")

# Social media posts
result = processor.generate_content("AI trends", "social_media")

# Product descriptions
result = processor.generate_content("smartphone", "product_description")
```

### 3. Data Analysis

```python
data = [10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60]

# Basic analysis
result = processor.analyze_data(data, "basic")

# Trend analysis
result = processor.analyze_data(data, "trend")

# Anomaly detection
result = processor.analyze_data(data, "anomaly")
```

### 4. Translation & Localization

```python
result = processor.translate_and_localize(
    "Welcome to our website!",
    "Spanish",
    "business"
)
```

### 5. Idea Generation

```python
# Business ideas
result = processor.generate_ideas("sustainable technology", "business")

# Marketing campaigns
result = processor.generate_ideas("fitness app", "marketing")

# Product ideas
result = processor.generate_ideas("home automation", "product")
```

### 6. Text Summarization

```python
long_text = "Your long text here..."

# Key points
result = processor.summarize_text(long_text, "key_points")

# Executive summary
result = processor.summarize_text(long_text, "executive_summary")

# One sentence
result = processor.summarize_text(long_text, "one_sentence")
```

### 7. Troubleshooting

```python
result = processor.troubleshoot_issue(
    "My Python script is running very slowly",
    "programming"
)
```

## 🌐 Web API Endpoints

The web application provides these endpoints:

- `GET /` - Interactive web interface
- `POST /process-task` - Process tasks with AI
- `POST /chat` - Simple chat endpoint
- `GET /health` - Health check

### Example API Usage

```bash
# Process a task
curl -X POST "http://localhost:8000/process-task" \
  -H "Content-Type: application/json" \
  -d '{
    "task_type": "text",
    "prompt": "Write a story about a robot",
    "api_type": "openai"
  }'

# Simple chat
curl -X POST "http://localhost:8000/chat" \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "prompt=Explain quantum computing&api_type=anthropic"
```

## 🔧 Customization

### Adding New APIs

```python
def custom_api_chat(self, prompt: str) -> str:
    """Add your custom API implementation"""
    # Your implementation here
    pass
```

### Creating New Task Types

```python
def custom_task(self, input_data: str) -> Dict:
    """Add your custom task processing"""
    prompt = f"Your custom prompt: {input_data}"
    response = self.ai_apis.openai_chat(prompt)
    return {"result": response}
```

## 🚨 Error Handling

The APIs include error handling for:

- Missing API keys
- Network errors
- Rate limiting
- Invalid responses

## 📈 Performance Tips

1. **Use appropriate APIs for tasks**:

   - OpenAI for general tasks
   - Anthropic for analysis
   - Ollama for privacy-sensitive tasks

2. **Cache responses** when possible

3. **Use streaming** for long responses

4. **Implement retry logic** for failed requests

## 🤝 Contributing

Feel free to:

- Add new API integrations
- Create new task processors
- Improve error handling
- Add more examples

## 📄 License

This project is open source and available under the MIT License.

## 🆘 Support

If you encounter issues:

1. Check your API keys are correct
2. Ensure you have internet connection
3. Verify the API service is available
4. Check the error messages for specific guidance

## 🎯 Next Steps

1. **Get your API keys** from the services you want to use
2. **Set up the environment** with your keys
3. **Try the web interface** to test different APIs
4. **Integrate into your projects** using the provided classes
5. **Customize for your specific needs**

Happy coding with AI! 🤖✨
