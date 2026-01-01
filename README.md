# AI Advertisement Script Generator

An intelligent system that generates high-quality, targeted advertisement scripts using a multi-agent AI pipeline. The application takes product information as input and produces compelling ad scripts by considering various aspects like target audience, tone, and effective marketing hooks.

## 🚀 Features

- **Multi-Agent Pipeline**: Utilizes specialized AI agents for different aspects of ad creation:
  - Product Analysis
  - Audience Targeting
  - Tone Setting
  - Hook Generation
  - Script Writing
  - Call-to-Action (CTA) Creation
  - Final Polish

- **Streamlit Web Interface**: User-friendly web interface for easy interaction
- **Customizable Output**: Generates ads tailored to specific products and target audiences
- **Modular Architecture**: Easy to extend with new agents or modify existing ones

## 🛠️ Installation

1. **Set up the project directory**
   ```bash
   mkdir Script-generator
   cd Script-generator
   ```

2. **Create and activate a virtual environment**
   ```bash
   python -m venv venv
   .\venv\Scripts\activate  # On Windows
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**
   Create a `.env` file in the root directory and add your API keys:
   ```
   GEMINI_API_KEY=your_gemini_api_key_here
   ```

## 🚀 Usage

1. **Run the Streamlit application**
   ```bash
   streamlit run app.py
   ```

2. **Using the application**
   - Enter your product details in the text area
   - Click "Generate Advertisement"
   - The system will generate a complete ad script


## 🤖 How It Works

The application uses a directed acyclic graph (DAG) to process the ad generation through multiple specialized agents:

1. **Product Agent**: Analyzes the product information
2. **Audience Agent**: Identifies and profiles the target audience
3. **Tone Agent**: Determines the appropriate tone for the advertisement
4. **Hook Agent**: Creates an engaging opening hook
5. **Script Agent**: Writes the main body of the advertisement
6. **CTA Agent**: Generates an effective call-to-action
7. **Polish Agent**: Refines and polishes the final output


## 🙏 Acknowledgments

- Built with [LangGraph](https://langchain-ai.github.io/langgraph/)
- Powered by [Google Gemini](https://ai.google.dev/)
- UI powered by [Streamlit](https://streamlit.io/)
