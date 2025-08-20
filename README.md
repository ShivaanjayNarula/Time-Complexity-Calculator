# Multi-Language Time Complexity Calculator 

A powerful web application that analyzes time and space complexity of code written in multiple programming languages using Google's Gemini AI.

## 🌟 Features

- **Multi-Language Support**: Analyzes code in 20+ programming languages
- **AI-Powered Analysis**: Uses Google Gemini for intelligent complexity estimation
- **Auto-Language Detection**: Automatically detects the programming language
- **Manual Language Selection**: Option to manually specify the language
- **Comprehensive Analysis**: Provides both time and space complexity
- **Beautiful UI**: Clean, modern interface built with Streamlit
- **Detailed Explanations**: Includes reasoning and key factors contributing to complexity

## 🚀 Supported Languages

- **Python** - def, import, print, etc.
- **JavaScript** - function, const, let, console.log, etc.
- **Java** - public class, main method, System.out.println, etc.
- **C++** - #include, int main, std::cout, etc.
- **C** - #include, int main, printf, etc.
- **Go** - package main, func main, fmt.Println, etc.
- **Rust** - fn main, println!, use, etc.
- **PHP** - <?php, echo, function, $variables, etc.
- **Ruby** - def, puts, class, require, etc.
- **Swift** - import, func, print, class, etc.
- **Kotlin** - fun main, println, import, class, etc.
- **TypeScript** - interface, type, const: type, etc.
- **C#** - using System, namespace, class, Console.WriteLine, etc.
- **Scala** - object, def main, println, import, etc.
- **Haskell** - module, main :: IO (), putStrLn, etc.
- **Clojure** - (ns, (defn, (println, etc.
- **F#** - open, let main, printfn, type, etc.
- **Dart** - import 'dart:', void main, print, class, etc.
- **Elixir** - defmodule, def, IO.puts, import, etc.
- **Julia** - function, println, using, module, etc.

## 📋 Prerequisites

- Python 3.7 or higher
- Google Gemini API key
- Internet connection for AI analysis

## 🛠️ Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd TimeComplexityCalculator
   ```

2. **Create a virtual environment**
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up your API key**
   
   **Option 1: Environment Variable**
   ```bash
   export GEMINI_API_KEY="your_actual_api_key_here"
   ```
   
   **Option 2: .env file**
   Create a `.env` file in the project root:
   ```
   GEMINI_API_KEY=your_actual_api_key_here
   ```
   
   **Option 3: Streamlit Secrets**
   Create `.streamlit/secrets.toml`:
   ```toml
   GEMINI_API_KEY = "your_actual_api_key_here"
   ```

## 🚀 Usage

1. **Start the application**
   ```bash
   streamlit run main1.py
   ```

2. **Open your browser**
   Navigate to `http://localhost:8501`

3. **Use the application**
   - Select programming language or use "Auto-detect"
   - Paste your code in the text area
   - Click "🚀 Estimate Complexity"
   - View the detailed analysis

## 📊 Example Output

```
📊 Complexity Analysis:

⏱️ Time Complexity: O(n²)
💾 Space Complexity: O(1)
📝 Explanation: The algorithm uses nested loops where the outer loop runs n times and the inner loop also runs n times, resulting in O(n²) time complexity.
🔍 Key factors: Nested loops, array traversal
```

## 🏗️ Project Structure

```
TimeComplexityCalculator-main/
├── main1.py              # Main Streamlit application
├── requirements.txt      # Python dependencies
├── README.md            # This file
├── .env                 # Environment variables (create this)
└── .streamlit/          # Streamlit configuration (optional)
    └── secrets.toml     # API keys (optional)
```

## 🔧 Configuration

### Environment Variables
- `GEMINI_API_KEY`: Your Google Gemini API key (required)

### Streamlit Configuration
The app automatically handles:
- Language detection using regex patterns
- API key management with fallback options
- Error handling and user feedback

## 🤖 How It Works

1. **Language Detection**: Uses regex patterns to identify the programming language
2. **Code Analysis**: Sends code to Google Gemini with language-specific context
3. **AI Processing**: Gemini analyzes loops, recursion, data structures, and algorithms
4. **Result Formatting**: Formats the response with emojis and clear sections
5. **Display**: Shows time complexity, space complexity, explanation, and key factors

## 🛡️ Error Handling

- **Missing API Key**: Shows helpful warning with setup instructions
- **Invalid Code**: Provides clear error messages
- **Network Issues**: Handles API connection problems gracefully
- **Language Detection**: Falls back to "Unknown" if language can't be determined

## 🔍 Technical Details

### Dependencies
- `streamlit==1.33.0`: Web framework
- `google-generativeai==0.8.3`: Google Gemini API client
- `python-dotenv==1.0.1`: Environment variable management
- `pygments==2.19.2`: Code highlighting

### Key Functions
- `detect_language()`: Identifies programming language using regex patterns
- `estimate_complexity()`: Sends code to Gemini for analysis
- `format_complexity_result()`: Formats the AI response for display

## 🚀 Deployment

### Local Development
```bash
streamlit run main1.py
```

### Production Deployment
The app can be deployed to:
- Streamlit Cloud
- Heroku
- AWS/GCP/Azure
- Docker containers

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

---

**Made with ❤️ by Shivaanjay Narula**
