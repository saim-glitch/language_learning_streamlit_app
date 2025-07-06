# 🌍 AI Language Learning Companion

A comprehensive, interactive language learning platform built with Streamlit that provides personalized language learning experiences through AI-powered conversations, vocabulary lessons, pronunciation practice, and cultural insights.

## ✨ Features

### 🏠 Dashboard
- **Personal Progress Tracking**: Monitor your learning journey with detailed metrics and analytics
- **Skill Assessment Radar**: Visual representation of your language proficiency across different areas
- **Weekly Activity Charts**: Track your daily learning progress with interactive charts
- **Achievement System**: Unlock badges and milestones as you advance through your learning journey

### 💬 AI Conversation Partner
- **Adaptive Scenarios**: Practice conversations tailored to your current skill level
- **Interactive Chat Interface**: Engage in real-time conversations with AI in your target language
- **Contextual Learning**: Practice language in realistic scenarios and situations
- **Difficulty Adjustment**: Conversations adapt based on your proficiency level

### 📚 Vocabulary Lessons
- **Themed Categories**: Organized vocabulary lessons covering essential topics
  - Greetings and Basic Phrases
  - Family and Relationships
  - Food and Dining
  - Numbers and Time
  - Colors and Descriptions
- **Interactive Flashcards**: Learn new words with spaced repetition techniques
- **Progress Tracking**: Monitor your vocabulary mastery with detailed statistics
- **Quiz Mode**: Test your knowledge with adaptive vocabulary quizzes

### 🎤 Pronunciation Practice
- **Word-by-Word Practice**: Focus on individual vocabulary pronunciation
- **Phrase Practice**: Master common expressions and everyday phrases
- **Pronunciation Scoring**: Get feedback on your pronunciation accuracy (simulated)
- **Difficulty Levels**: Practice materials adapted to your current level

### 🌍 Cultural Insights
- **Cultural Context**: Learn about customs, traditions, and social norms
- **Interactive Cultural Quizzes**: Test your understanding of cultural concepts
- **Appropriate Usage**: Understand when and how to use language in different contexts
- **Real-world Application**: Bridge the gap between language and culture

### 📈 Progress Analytics
- **Comprehensive Metrics**: Detailed breakdown of your learning progress across all areas
- **Learning Streaks**: Visual calendar showing your daily activity and consistency
- **Skill Distribution**: Analyze how your learning points are distributed across different skills
- **Performance Insights**: Identify strengths and areas for improvement

## 🚀 Getting Started

### Prerequisites
- Python 3.8 or higher
- pip package manager
- Modern web browser

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/saim-glitch/language_learning_streamlit_app.git
   cd language_learning_streamlit_app
   ```

2. **Create a virtual environment (recommended)**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application**
   ```bash
   streamlit run app.py
   ```

5. **Open your browser**
   Navigate to `http://localhost:8501` to start your language learning journey!

## 📦 Dependencies

```txt
streamlit>=1.28.0
plotly>=5.15.0
pandas>=2.0.0
numpy>=1.21.0
```

## 🎯 Supported Languages

Currently supports learning:
- 🇪🇸 **Spanish** - Comprehensive lessons and cultural insights
- 🇫🇷 **French** - Full vocabulary and conversation practice
- 🇩🇪 **German** - Complete learning modules with cultural context

### Coming Soon:
- 🇮🇹 Italian
- 🇵🇹 Portuguese
- 🇨🇳 Chinese (Mandarin)
- 🇯🇵 Japanese
- 🇷🇺 Russian
- 🇦🇷 Arabic

## 🏗️ Project Structure

```
language_learning_streamlit_app/
├── app.py                 # Main Streamlit application
├── requirements.txt       # Project dependencies
├── README.md             # Project documentation
├── components/           # Reusable UI components
├── data/                # Language data and resources
├── utils/               # Utility functions
└── assets/              # Static assets (images, icons)
```

## 🔧 Core Components

### User Profile Management
- Persistent user preferences and settings
- Learning progress tracking
- Personalized difficulty adjustments
- Achievement and badge system

### Conversation Engine
- AI-powered dialogue system
- Context-aware responses
- Adaptive conversation difficulty
- Cultural context integration

### Vocabulary System
- Structured word learning modules
- Spaced repetition algorithm
- Progress tracking and analytics
- Categorized vocabulary sets

### Progress Analytics
- Comprehensive learning metrics
- Visual progress representation
- Streak tracking and motivation
- Performance insights and recommendations

## 🎮 User Experience

### Beginner Level (< 100 points)
- Simple vocabulary introduction
- Basic greetings and common phrases
- Cultural basics and etiquette
- Gentle conversation practice

### Intermediate Level (100-300 points)
- Expanded vocabulary sets
- Complex sentence structures
- Cultural nuances and context
- Longer conversation scenarios

### Advanced Level (> 300 points)
- Advanced vocabulary and idioms
- Complex cultural discussions
- Free-form conversation practice
- Professional and academic contexts

## 🤝 Contributing

We welcome contributions from the community! Here's how you can help:

### Ways to Contribute
- 🌐 **Language Support**: Add new languages or improve existing ones
- 🎨 **UI/UX Enhancement**: Improve the user interface and experience
- 🧠 **Feature Development**: Add new learning features and capabilities
- 🐛 **Bug Fixes**: Help identify and fix issues
- 📖 **Documentation**: Improve documentation and tutorials

### Development Setup
1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Make your changes
4. Test thoroughly
5. Commit your changes (`git commit -m 'Add amazing feature'`)
6. Push to the branch (`git push origin feature/amazing-feature`)
7. Open a Pull Request

## 🛣️ Roadmap

### Phase 1: Foundation ✅
- [x] Core UI and navigation system
- [x] User profile and progress tracking
- [x] Basic vocabulary lessons
- [x] Conversation practice framework
- [x] Cultural insights module

### Phase 2: Enhancement 🚧
- [ ] Real speech recognition integration
- [ ] Advanced AI conversation models
- [ ] Audio pronunciation features
- [ ] Persistent data storage
- [ ] Mobile optimization

### Phase 3: Advanced Features 🔮
- [ ] Multi-user learning sessions
- [ ] Live conversation practice
- [ ] Advanced gamification
- [ ] Personalized learning paths
- [ ] Integration with external resources

## 📊 Technical Specifications

- **Framework**: Streamlit 1.28+
- **Visualization**: Plotly 5.15+
- **Data Processing**: Pandas 2.0+
- **Browser Support**: Chrome, Firefox, Safari, Edge
- **Performance**: < 3 seconds load time, ~50MB memory usage

## 🔒 Privacy & Data

- All user data is stored locally during sessions
- No personal information transmitted externally
- Session-based progress tracking
- No permanent data storage currently implemented
- Future versions will include secure data persistence options

## 🐛 Known Limitations

- **Pronunciation Scoring**: Currently simulated (ready for speech recognition integration)
- **AI Responses**: Uses predefined responses (ready for LLM integration)
- **Session Persistence**: Progress resets when browser is refreshed
- **Audio Features**: No audio playback currently implemented

## 🆘 Support

- **Issues**: [GitHub Issues](https://github.com/saim-glitch/language_learning_streamlit_app/issues)
- **Discussions**: [GitHub Discussions](https://github.com/saim-glitch/language_learning_streamlit_app/discussions)
- **Feature Requests**: Submit through GitHub Issues with the `enhancement` label

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- **Streamlit Team**: For the powerful and intuitive framework
- **Plotly**: For beautiful and interactive visualizations
- **Open Source Community**: For inspiration and best practices
- **Language Learning Community**: For feedback and feature suggestions

## 🌟 Show Your Support

If you find this project helpful, please consider:
- ⭐ **Star** the repository
- 🍴 **Fork** and contribute to the project
- 📢 **Share** with fellow language learners
- 🐛 **Report** issues and bugs
- 💡 **Suggest** new features and improvements

---

<div align="center">
  <p><strong>Happy Learning! 🎉</strong></p>
  <p>Made with ❤️ for language learners worldwide</p>
  
  [![Made with Streamlit](https://img.shields.io/badge/Made%20with-Streamlit-red.svg)](https://streamlit.io)
  [![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://python.org)
  [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
  [![GitHub stars](https://img.shields.io/github/stars/saim-glitch/language_learning_streamlit_app.svg?style=social)](https://github.com/saim-glitch/language_learning_streamlit_app/stargazers)
</div>
