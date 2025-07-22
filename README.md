# English Written Evaluation System ✍️

![English Writing](https://static01.nyt.com/images/2017/08/06/education/06WRITING_GIF/06WRITING_GIF-superJumbo.gif)

An intelligent English writing evaluation system that uses advanced AI vision models to analyze images and evaluate your written English descriptions based on CEFR standards. Get detailed feedback on grammar, vocabulary, relevance, and writing structure through engaging image description tasks.

## 🚀 Live Demo

**Try it now:** [English Helper Written - Live Demo](https://huggingface.co/spaces/YoussefA7med/English_Helper_Written)

Experience the full functionality of the English Written Evaluation System directly in your browser! No installation required.

## 🌟 Features

### 🖼️ **AI-Powered Image Analysis**
- Advanced Vision-Language Models (VLM) for detailed image description
- Support for Meta LLaMA 3.2 and Google Gemini 2.0 Flash models
- Comprehensive scene understanding and context analysis

### ✍️ **Comprehensive Writing Assessment**
- **Relevance Score**: How well your paragraph matches the image content (0-100)
- **Grammar Score**: Evaluation of grammar accuracy, tense usage, and structure (0-100)
- **Vocabulary Score**: Assessment of word choice richness and accuracy (0-100)
- **CEFR Level Assessment**: Automatic proficiency level determination (A1-C2)

### 📝 **Detailed Feedback System**
- **Grammar Mistakes**: Specific errors identified with improvement suggestions
- **Corrected Version**: Your paragraph with proper grammar and enhanced vocabulary
- **Learning Tips**: Actionable advice tailored to your writing weaknesses
- **Strengths Highlighting**: Recognition of impressive sentences or clever word usage
- **Motivational Comments**: Encouraging feedback to boost writing confidence

### 🔄 **Multi-Model Support**
- **Meta LLaMA 3.2 11B Vision**: Advanced vision understanding with detailed analysis
- **Google Gemini 2.0 Flash**: Fast and accurate image analysis
- **OpenRouter Integration**: Reliable API access with multiple fallback keys

## 🚀 Getting Started

### Try Online First
Before setting up locally, test the system using our **[Live Demo](https://huggingface.co/spaces/YoussefA7med/English_Helper_Written)** to see if it meets your needs!

### Prerequisites

Before running the application locally, ensure you have the following:

- Python 3.8 or higher
- Required Python packages (see [Installation](#installation))
- API keys for the required services

### Required API Keys

You'll need to obtain the following API keys:

1. **DeepSeek API Key**: For AI-powered evaluation and feedback
   - Sign up at [DeepSeek Platform](https://platform.deepseek.com/)

2. **OpenRouter API Keys**: For vision-language model access
   - Sign up at [OpenRouter](https://openrouter.ai/)
   - The system supports multiple API keys for reliability

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/youssefa7med/english-written-evaluation.git
   cd english-written-evaluation
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables**
   
   Create a `.env` file in the root directory:
   ```env
   DEEPSEEK_API_KEY=your_deepseek_api_key_here
   OPENROUTER_API_KEY_1=your_first_openrouter_key
   OPENROUTER_API_KEY_2=your_second_openrouter_key
   OPENROUTER_API_KEY_3=your_third_openrouter_key
   OPENROUTER_API_KEY_4=your_fourth_openrouter_key
   ```

4. **Run the application**
   ```bash
   python written_evaluation.py
   ```

5. **Access the interface**
   
   Open your browser and navigate to the URL displayed in the terminal (typically `http://localhost:7860`)

## 📋 Requirements

Create a `requirements.txt` file with the following dependencies:

```txt
gradio>=4.0.0
requests>=2.31.0
python-dotenv>=1.0.0
```

## 🎮 How to Use

### Step 1: Provide Image URL
- Enter a URL of any image you want to describe
- The system supports various image formats (JPG, PNG, GIF, etc.)
- Choose images with clear, interesting content for better evaluation

### Step 2: Select Vision Model
- **Meta LLaMA 3.2**: Advanced vision understanding with detailed analysis
- **Google Gemini 2.0 Flash**: Fast processing with accurate image description

### Step 3: Write Your Description
- **Observe the image**: Take time to analyze all visual elements
- **Write naturally**: Describe what you see in your own words
- **Be descriptive**: Include objects, people, actions, colors, settings, and emotions
- **Use varied vocabulary**: Try to use different sentence structures and descriptive words

### Step 4: Get Comprehensive Evaluation
- **Relevance Assessment**: How well your description matches the image content
- **Grammar Analysis**: Detailed breakdown of grammatical accuracy
- **Vocabulary Evaluation**: Assessment of word choice and language richness
- **Error Correction**: See your paragraph with proper grammar and enhanced vocabulary
- **Personalized Tips**: Get specific advice for writing improvement
- **CEFR Level**: Understand your current writing proficiency level

## 🏗️ System Architecture

```
┌─────────────────┐    ┌──────────────────┐    ┌─────────────────┐
│   Image URL     │───▶│  Vision Model    │───▶│ Image Analysis  │
└─────────────────┘    │   (LLaMA/Gemini) │    │  Description    │
                       └──────────────────┘    └─────────────────┘
                                                        │
                                                        ▼
┌─────────────────┐    ┌──────────────────┐    ┌─────────────────┐
│   Evaluation    │◀───│ Written Paragraph│◀───│ User Input      │
│   (DeepSeek)    │    │   Analysis       │    │   (Gradio)      │
└─────────────────┘    └──────────────────┘    └─────────────────┘
```

## 🎯 Learning Benefits

### For Language Learners
- **Visual Context Writing**: Practice describing real-world scenarios in writing
- **Grammar Improvement**: Get specific feedback on grammatical structures
- **Vocabulary Expansion**: Learn descriptive words through image analysis
- **Writing Fluency**: Develop natural writing flow and coherence
- **Error Awareness**: Understand common mistakes and how to correct them

### For Educators
- **Writing Assessment Tool**: Objectively evaluate student writing skills
- **Visual Learning Support**: Use images to prompt creative writing exercises
- **Progress Tracking**: Monitor improvement in writing proficiency over time
- **CEFR Alignment**: Standards-based evaluation system for consistent assessment
- **Engaging Activities**: Make writing practice more interactive and motivating

## 📊 Evaluation Metrics

### Core Scores
- **Relevance Score (0-100)**: How accurately your description captures the image content
- **Grammar Score (0-100)**: Assessment of grammatical accuracy and proper structure
- **Vocabulary Score (0-100)**: Evaluation of word choice richness and appropriateness

### Detailed Analysis
- **Grammar Mistakes**: Specific errors in subject-verb agreement, tense, articles, etc.
- **Vocabulary Issues**: Inappropriate word choices or missed opportunities for better words
- **Corrected Version**: Your paragraph improved with proper grammar and enhanced vocabulary
- **Learning Level**: CEFR proficiency assessment (A1-C2) based on writing complexity
- **Strengths**: Recognition of well-constructed sentences or sophisticated vocabulary
- **Learning Tips**: Personalized advice targeting your specific areas for improvement

## 🔧 Customization

### Adding New Vision Models
Modify the model dropdown in the Gradio interface to include additional vision-language models available through OpenRouter.

### Custom Evaluation Criteria
Extend the evaluation system by modifying the `evaluate_written_english()` function to include additional writing assessment metrics like coherence, creativity, or style.

### Language Support
Update the evaluation system to support other languages by modifying the prompt and evaluation criteria in the DeepSeek API call.

## 📊 Technical Details

### AI Models Used
- **Vision Models**: Meta LLaMA 3.2 11B Vision, Google Gemini 2.0 Flash for image analysis
- **Evaluation Engine**: DeepSeek Chat API for comprehensive writing assessment
- **Language Processing**: Advanced natural language processing for grammar and vocabulary analysis

### Supported Languages
- Primary: English (optimized for various English dialects)
- Writing evaluation and feedback optimized for English grammar and vocabulary assessment

### Text Processing
- **Input formats**: Plain text paragraphs of any length
- **Output format**: Structured JSON with comprehensive feedback
- **Analysis**: Grammar, vocabulary, relevance, and CEFR level assessment

### Image Support
- **Formats**: JPG, PNG, GIF, WebP, and other common image formats
- **Source**: Any publicly accessible image URL
- **Processing**: Advanced computer vision analysis through state-of-the-art VLM models

## 🤝 Contributing

We welcome contributions to improve the English Written Evaluation System!

### How to Contribute
1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

### Areas for Contribution
- Additional vision model integrations
- Multi-language writing evaluation
- New evaluation metrics (coherence, creativity, style)
- UI/UX improvements
- Performance optimizations
- Batch processing capabilities
- Writing style analysis features

## 🐛 Troubleshooting

### Common Issues

**Issue: Vision model not responding**
- Solution: Check OpenRouter API keys and ensure they have sufficient credits
- Try switching between LLaMA and Gemini models

**Issue: Image not loading**
- Solution: Ensure the image URL is publicly accessible and properly formatted
- Verify the image format is supported

**Issue: Evaluation fails**
- Solution: Check DeepSeek API key and account credits
- Ensure the written paragraph is not empty
- Verify internet connection for API calls

**Issue: JSON parsing errors**
- Solution: The system includes automatic JSON cleaning and error handling
- Check the raw API response in case of persistent issues

### Getting Help
- Check the [Issues](https://github.com/youssefa7med/english-written-evaluation/issues) page
- Create a new issue with detailed error descriptions
- Include system information and error logs

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- **DeepSeek**: For providing advanced language AI capabilities
- **OpenRouter**: For seamless access to multiple vision-language models
- **Meta**: For the powerful LLaMA 3.2 Vision model
- **Google**: For Gemini 2.0 Flash model
- **Gradio**: For the intuitive web interface framework
- **CEFR Framework**: For standardized language proficiency guidelines

## 📞 Contact

- **Project Maintainer**: [Youssef Ahmed](mailto:youssef111ahmed111@gmail.com)
- **GitHub**: [@youssefa7med](https://github.com/youssefa7med)
  
---

### 🌟 Star this repository if it helped you improve your English writing skills!

**Made with ❤️ for English language learners worldwide**
