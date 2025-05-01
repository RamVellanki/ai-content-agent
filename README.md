# AI Content Digest Agent

An intelligent content aggregation and summarization system that automatically generates daily digests from various sources. The system uses AI to discover, process, and summarize content while categorizing it into relevant topics.

## 🚀 Features

- **Automated Content Discovery**
  - Fixed feed sources monitoring
  - Dynamic web search across configured topics
  - Customizable keywords for targeted content discovery

- **Smart Content Processing**
  - Intelligent content extraction from web articles
  - AI-powered summarization
  - Automatic content categorization
  - Link preservation and source attribution

- **Daily Digest Generation**
  - Automated daily runs via GitHub Actions
  - Markdown-formatted output
  - GitHub Pages integration for easy access
  - Configurable topics and sources

## 🛠️ Technical Architecture

The system consists of several key components:

- **Digest Agent**: Core processing engine that:
  - Discovers content from fixed and dynamic sources
  - Processes and summarizes articles
  - Categorizes content using AI
  - Generates structured digest outputs

- **Tools**:
  - Web search integration
  - Content fetching and extraction
  - Feed processing

- **AI Chains**:
  - Smart router for choosing appropriate summarization strategies
  - Content classification system
  - Summary generation

## 🔧 Setup

1. Clone the repository
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Configure environment variables:
   ```
   SERPER_API_KEY=your_serper_key
   OPENAI_API_KEY=your_openai_key
   ```

## 🚀 Usage

### Manual Execution
```bash
python orchestrator/run_pipeline.py
```

### Automated Execution
The system runs automatically daily at 3 AM UTC through GitHub Actions. The workflow:
1. Discovers new content
2. Processes and summarizes articles
3. Generates a digest
4. Publishes to GitHub Pages

## 📊 Configuration

Topics and sources can be configured through the configuration files:
- Add/modify topics in the topics configuration
- Customize fixed feed sources
- Adjust search parameters and keywords

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📝 License

[Add your chosen license here]

## 🔗 Dependencies

- Python 3.11+
- OpenAI API
- Serper API for web search
- Various Python packages (see requirements.txt)

## 📫 Contact

[Add your contact information here]
