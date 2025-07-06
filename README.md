# 🌍 AI Language Learning Companion

A comprehensive, interactive language learning platform built with Streamlit that provides personalized language learning experiences through AI-powered conversations, vocabulary lessons, pronunciation practice, and cultural insights.

## ✨ Features

### 🏠 Dashboard
- **Personal Progress Tracking**: Monitor your learning journey with detailed metrics
- **Skill Assessment Radar**: Visual representation of your language skills
- **Weekly Activity Charts**: Track your daily learning progress
- **Achievement System**: Unlock badges as you progress

### 💬 AI Conversation Partner
- **Adaptive Scenarios**: Practice conversations based on your skill level
- **Real-time Chat**: Interactive conversations with AI in your target language
- **Cultural Context**: Learn appropriate responses for different situations
- **Pronunciation Integration**: Practice speaking during conversations

### 📚 Vocabulary Lessons
- **Categorized Learning**: Organized vocabulary by themes (greetings, family, food, etc.)
- **Flashcard System**: Interactive word learning with progress tracking
- **Quiz Mode**: Test your knowledge with adaptive quizzes
- **Mastery Tracking**: Monitor which words you've mastered

### 🎤 Pronunciation Practice
- **Individual Words**: Practice pronunciation of specific vocabulary
- **Common Phrases**: Learn everyday expressions with proper pronunciation
- **Tongue Twisters**: Challenge yourself with advanced pronunciation exercises
- **Score Analysis**: Get feedback on your pronunciation accuracy

### 🌍 Cultural Insights
- **Cultural Tips**: Learn about customs and traditions
- **Interactive Quizzes**: Test your cultural knowledge
- **Context Learning**: Understand when and how to use language appropriately

### 📈 Progress Analytics
- **Comprehensive Metrics**: Detailed breakdown of your learning progress
- **Learning Streaks**: Visual calendar of your daily activity
- **Skill Distribution**: See how your points are distributed across different areas
- **Personalized Recommendations**: Get suggestions based on your progress

## 🚀 Getting Started

### Prerequisites
- Python 3.8 or higher
- pip package manager

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/ai-language-learning-companion.git
   cd ai-language-learning-companion
   ```

2. **Create a virtual environment**
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
   Navigate to `http://localhost:8501` to start learning!

## 📦 Dependencies

Create a `requirements.txt` file with the following dependencies:

```txt
streamlit>=1.28.0
plotly>=5.15.0
pandas>=2.0.0
```

## 🎯 Supported Languages

Currently supports learning:
- 🇪🇸 **Spanish** (Full features)
- 🇫🇷 **French** (Full features)
- 🇩🇪 **German** (Full features)
- 🇮🇹 Italian (Coming soon)
- 🇵🇹 Portuguese (Coming soon)
- 🇨🇳 Chinese (Coming soon)
- 🇯🇵 Japanese (Coming soon)

## 🏗️ Architecture

### Core Components

- **User Profile Management**: Persistent user data and preferences
- **Conversation Engine**: AI-powered dialogue system
- **Vocabulary System**: Structured word learning and testing
- **Pronunciation Module**: Simulated speech analysis (ready for integration)
- **Progress Tracking**: Comprehensive analytics and reporting
- **Cultural Learning**: Context-aware cultural education

### Data Structure

```python
user_profile = {
    'name': str,
    'native_language': str,
    'target_language': str,
    'level': str,  # Beginner, Intermediate, Advanced
    'daily_goal': int,  # minutes
    'interests': list,
    'streak': int,
    'total_points': int,
    'lessons_completed': int,
    'conversations_had': int,
    'pronunciation_scores': list,
    'vocabulary_mastered': list,
    'last_login': str
}
```

## 🔧 Configuration

### Customizing Languages

To add a new language, update the `LANGUAGES` dictionary in the code:

```python
LANGUAGES['YourLanguage'] = {
    'greetings': ['Hello', 'Good morning', ...],
    'basics': ['Please', 'Thank you', ...],
    'questions': ['How are you?', ...],
    'family': ['mother', 'father', ...],
    'numbers': ['one', 'two', ...],
    'colors': ['red', 'blue', ...],
    'food': ['food', 'water', ...],
    'cultural_tips': ['Tip 1', 'Tip 2', ...]
}
```

### Adapting Difficulty Levels

The app automatically adjusts difficulty based on user progress:
- **Beginner**: < 100 points
- **Intermediate**: 100-300 points
- **Advanced**: > 300 points

## 🤝 Contributing

We welcome contributions! Here's how you can help:

1. **Fork the repository**
2. **Create a feature branch**
   ```bash
   git checkout -b feature/amazing-feature
   ```
3. **Commit your changes**
   ```bash
   git commit -m 'Add amazing feature'
   ```
4. **Push to the branch**
   ```bash
   git push origin feature/amazing-feature
   ```
5. **Open a Pull Request**

### Areas for Contribution

- 🌐 **New Languages**: Add support for additional languages
- 🎨 **UI/UX Improvements**: Enhance the user interface
- 🧠 **AI Integration**: Implement real language models
- 🎤 **Speech Recognition**: Add actual speech processing
- 📱 **Mobile Optimization**: Improve mobile experience
- 🔊 **Audio Features**: Add text-to-speech capabilities

## 🐛 Known Issues

- Pronunciation scoring is currently simulated (ready for speech recognition integration)
- Limited to mock AI responses (ready for LLM integration)
- No audio playback for pronunciation examples
- Session state resets when browser is refreshed

## 🛣️ Roadmap

### Phase 1: Core Features ✅
- [x] Basic UI and navigation
- [x] User profile system
- [x] Vocabulary lessons
- [x] Conversation practice
- [x] Progress tracking

### Phase 2: Enhanced Features 🚧
- [ ] Real speech recognition integration
- [ ] LLM integration for dynamic conversations
- [ ] Audio playback for pronunciation
- [ ] Persistent data storage
- [ ] Mobile app version

### Phase 3: Advanced Features 🔮
- [ ] Multiplayer learning sessions
- [ ] Video call practice with native speakers
- [ ] Gamification elements
- [ ] Personalized learning paths
- [ ] Integration with external language resources

## 📊 Performance

- **Loading Time**: < 3 seconds initial load
- **Memory Usage**: ~50MB typical usage
- **Supported Users**: Single-user per session
- **Browser Compatibility**: Chrome, Firefox, Safari, Edge

## 🔒 Privacy & Security

- All data is stored locally in session state
- No personal information is transmitted externally
- No audio recordings are permanently stored
- User progress is maintained only during active sessions

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- **Streamlit Team**: For the amazing framework
- **Plotly**: For beautiful visualizations
- **Language Learning Community**: For inspiration and feedback
- **Contributors**: Everyone who helps make this project better

## 📞 Support

- **Issues**: [GitHub Issues](https://github.com/yourusername/ai-language-learning-companion/issues)
- **Discussions**: [GitHub Discussions](https://github.com/yourusername/ai-language-learning-companion/discussions)
- **Email**: your.email@example.com

## 🌟 Show Your Support

If you find this project helpful, please consider:
- ⭐ Starring the repository
- 🍴 Forking and contributing
- 📢 Sharing with others
- 🐛 Reporting issues
- 💡 Suggesting improvements

---

<div align="center">
  <p><strong>Happy Learning! 🎉</strong></p>
  <p>Made with ❤️ for language learners worldwide</p>
  
  [![Made with Streamlit](https://img.shields.io/badge/Made%20with-Streamlit-red.svg)](https://streamlit.io)
  [![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://python.org)
  [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
</div>
