import os, streamlit as st
from dotenv import load_dotenv
import google.generativeai as genai
import re

load_dotenv()
# Prefer Streamlit secrets; fall back to environment variable for local runs
GEMINI_API_KEY = None
try:
    GEMINI_API_KEY = st.secrets["GEMINI_API_KEY"]
except (FileNotFoundError, KeyError, Exception):
    # Silently fall back to environment variable
    GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

if GEMINI_API_KEY:
    genai.configure(api_key=GEMINI_API_KEY)
    _gemini_model = genai.GenerativeModel("gemini-1.5-flash")
else:
    _gemini_model = None

def detect_language(code):
    """Detect programming language based on code patterns"""
    code_lower = code.lower().strip()
    
    # Language detection patterns
    patterns = {
        'Python': [r'def\s+\w+\s*\(', r'import\s+\w+', r'from\s+\w+\s+import', r'print\s*\(', r'if\s+__name__\s*==\s*[\'"]__main__[\'"]'],
        'JavaScript': [r'function\s+\w+\s*\(', r'const\s+\w+', r'let\s+\w+', r'var\s+\w+', r'console\.log', r'=>\s*{'],
        'Java': [r'public\s+class', r'public\s+static\s+void\s+main', r'System\.out\.println', r'int\s+\w+', r'String\s+\w+'],
        'C++': [r'#include\s*<', r'int\s+main\s*\(', r'std::cout', r'using\s+namespace\s+std', r'class\s+\w+'],
        'C': [r'#include\s*<', r'int\s+main\s*\(', r'printf\s*\(', r'#define', r'struct\s+\w+'],
        'Go': [r'package\s+main', r'func\s+main\s*\(', r'fmt\.Println', r'import\s+[\'"](.*?)[\'"]'],
        'Rust': [r'fn\s+main\s*\(', r'println!\s*!', r'use\s+\w+', r'let\s+mut\s+\w+'],
        'PHP': [r'<\?php', r'echo\s+', r'function\s+\w+\s*\(', r'\$\w+'],
        'Ruby': [r'def\s+\w+', r'puts\s+', r'class\s+\w+', r'require\s+[\'"](.*?)[\'"]'],
        'Swift': [r'import\s+\w+', r'func\s+\w+\s*\(', r'print\s*\(', r'class\s+\w+'],
        'Kotlin': [r'fun\s+main\s*\(', r'println\s*\(', r'import\s+\w+', r'class\s+\w+'],
        'TypeScript': [r'interface\s+\w+', r'type\s+\w+', r'const\s+\w+:\s*\w+', r'function\s+\w+\s*<'],
        'C#': [r'using\s+System', r'namespace\s+\w+', r'class\s+\w+', r'Console\.WriteLine', r'public\s+class'],
        'Scala': [r'object\s+\w+', r'def\s+main\s*\(', r'println\s*\(', r'import\s+\w+'],
        'Haskell': [r'module\s+\w+', r'main\s*::\s*IO\s*\(\)', r'putStrLn', r'import\s+\w+'],
        'Clojure': [r'\(ns\s+\w+', r'\(defn\s+\w+', r'\(println', r'\(require\s+\['],
        'F#': [r'open\s+\w+', r'let\s+main\s*\(\)', r'printfn', r'type\s+\w+'],
        'Dart': [r'import\s+\'dart:', r'void\s+main\s*\(\)', r'print\s*\(', r'class\s+\w+'],
        'Elixir': [r'defmodule\s+\w+', r'def\s+\w+', r'IO\.puts', r'import\s+\w+'],
        'Julia': [r'function\s+\w+', r'println\s*\(', r'using\s+\w+', r'module\s+\w+']
    }
    
    scores = {}
    for lang, lang_patterns in patterns.items():
        score = 0
        for pattern in lang_patterns:
            if re.search(pattern, code_lower):
                score += 1
        scores[lang] = score
    
    # Return the language with highest score, or 'Unknown' if no clear match
    if scores:
        best_lang = max(scores, key=scores.get)
        return best_lang if scores[best_lang] > 0 else 'Unknown'
    return 'Unknown'

def estimate_complexity(code, language=None):
    if _gemini_model is None:
        raise RuntimeError("GEMINI_API_KEY is not set. Provide it via Streamlit secrets (.streamlit/secrets.toml) or as an environment variable.")
    
    if not language:
        language = detect_language(code)
    
    prompt = f'''
You are a time complexity expert. Analyze the following {language} code and determine its time complexity.

Code:
{code}

Please provide a detailed analysis including:
1. Time Complexity: O(...) notation
2. Space Complexity: O(...) notation (if applicable)
3. Explanation: Brief explanation of your reasoning
4. Key factors: What contributes most to the complexity

Focus on:
- Loops and nested loops
- Recursive calls
- Data structure operations
- Algorithm patterns

Format your response as:
Time Complexity: O(...)
Space Complexity: O(...)
Explanation: [your explanation]
Key factors: [main complexity contributors]
'''
    
    resp = _gemini_model.generate_content(
        prompt,
        generation_config={
            "temperature": 0.1,
            "max_output_tokens": 300
        }
    )
    return getattr(resp, "text", "")

def format_complexity_result(result):
    """Format the complexity analysis result for better display"""
    if not result:
        return "No analysis available."
    
    # Split the result into lines and format each section
    lines = result.strip().split('\n')
    formatted_lines = []
    
    for line in lines:
        line = line.strip()
        if not line:
            continue
            
        # Format different sections with better styling
        if line.startswith('Time Complexity:'):
            formatted_lines.append(f"**⏱️ {line}**")
        elif line.startswith('Space Complexity:'):
            formatted_lines.append(f"**💾 {line}**")
        elif line.startswith('Explanation:'):
            formatted_lines.append(f"**📝 {line}**")
        elif line.startswith('Key factors:'):
            formatted_lines.append(f"**🔍 {line}**")
        else:
            formatted_lines.append(line)
    
    return '\n\n'.join(formatted_lines)

# Custom CSS for better styling
st.markdown("""
<style>
</style>
""", unsafe_allow_html=True)

st.title("Multi-Language Time Complexity Calculator")
st.markdown("**Supports:** Python, JavaScript, Java, C++, C, Go, Rust, Swift, Kotlin, TypeScript and many more!")

# Language selection
language_options = ['Auto-detect', 'Python', 'JavaScript', 'Java', 'C++', 'C', 'Go', 'Rust', 'Swift', 'Kotlin', 'TypeScript']
selected_language = st.selectbox("Select programming language (or Auto-detect):", language_options)

code = st.text_area("Paste your code here", height=300, placeholder="// Paste your code here...\n// Supports multiple programming languages")

if not GEMINI_API_KEY:
    st.warning("⚠️ GEMINI_API_KEY not set. Add it to your `.env` file as `GEMINI_API_KEY=your_key_here` or set it as an environment variable to enable analysis.")

if st.button("🚀 Estimate Complexity", type="primary"):
    if not code.strip():
        st.error("Please enter some code!")
    else:
        with st.spinner("🔍 Analyzing complexity..."):
            try:
                # Use selected language or auto-detect
                language_to_use = None if selected_language == 'Auto-detect' else selected_language
                result = estimate_complexity(code, language_to_use)
                
                # Format and display the result
                formatted_result = format_complexity_result(result)
                st.markdown("**📊 Complexity Analysis:**")
                st.markdown(formatted_result)
                
            except Exception as e:
                st.error(f"❌ Error: {e}")
                st.info("💡 Make sure your GEMINI_API_KEY is set correctly in the .env file or as an environment variable.")
