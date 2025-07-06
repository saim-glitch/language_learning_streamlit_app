import streamlit as st
import random
import json
import time
from datetime import datetime, timedelta
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import pandas as pd
import re

# Page configuration
st.set_page_config(
    page_title="AI Language Learning Companion",
    page_icon="🌍",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for better styling
st.markdown("""
<style>
    .main-header {
        background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
        padding: 2rem;
        border-radius: 10px;
        color: white;
        text-align: center;
        margin-bottom: 2rem;
    }
    
    .chat-message {
        padding: 1rem;
        border-radius: 10px;
        margin-bottom: 1rem;
        animation: fadeIn 0.5s;
    }
    
    .user-message {
        background-color: #e3f2fd;
        border-left: 4px solid #2196f3;
    }
    
    .ai-message {
        background-color: #f3e5f5;
        border-left: 4px solid #9c27b0;
    }
    
    .progress-card {
        background: white;
        padding: 1.5rem;
        border-radius: 10px;
        box-shadow: 0 2px 10px rgba(0,0,0,0.1);
        margin-bottom: 1rem;
    }
    
    .lesson-card {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 1.5rem;
        border-radius: 10px;
        margin-bottom: 1rem;
        cursor: pointer;
        transition: transform 0.3s;
    }
    
    .lesson-card:hover {
        transform: translateY(-2px);
    }
    
    .cultural-tip {
        background: #fff3e0;
        border: 1px solid #ffb74d;
        padding: 1rem;
        border-radius: 8px;
        margin: 1rem 0;
    }
    
    .achievement-badge {
        display: inline-block;
        background: #4caf50;
        color: white;
        padding: 0.5rem 1rem;
        border-radius: 20px;
        margin: 0.25rem;
        font-size: 0.8rem;
    }
    
    @keyframes fadeIn {
        from { opacity: 0; transform: translateY(20px); }
        to { opacity: 1; transform: translateY(0); }
    }
</style>
""", unsafe_allow_html=True)

# Initialize session state
if 'user_profile' not in st.session_state:
    st.session_state.user_profile = {
        'name': '',
        'native_language': 'English',
        'target_language': 'Spanish',
        'level': 'Beginner',
        'daily_goal': 20,
        'interests': [],
        'streak': 0,
        'total_points': 0,
        'lessons_completed': 0,
        'conversations_had': 0,
        'pronunciation_scores': [],
        'vocabulary_mastered': [],
        'last_login': datetime.now().isoformat()
    }

if 'conversation_history' not in st.session_state:
    st.session_state.conversation_history = []

if 'current_lesson' not in st.session_state:
    st.session_state.current_lesson = None

if 'pronunciation_feedback' not in st.session_state:
    st.session_state.pronunciation_feedback = []

# Language data and lessons
LANGUAGES = {
    'Spanish': {
        'greetings': ['Hola', 'Buenos días', 'Buenas tardes', 'Buenas noches'],
        'basics': ['Por favor', 'Gracias', 'De nada', 'Perdón', 'Lo siento'],
        'questions': ['¿Cómo estás?', '¿Cómo te llamas?', '¿Dónde vives?', '¿Qué haces?'],
        'family': ['madre', 'padre', 'hermano', 'hermana', 'hijo', 'hija'],
        'numbers': ['uno', 'dos', 'tres', 'cuatro', 'cinco', 'seis', 'siete', 'ocho', 'nueve', 'diez'],
        'colors': ['rojo', 'azul', 'verde', 'amarillo', 'negro', 'blanco', 'rosa', 'naranja'],
        'food': ['comida', 'agua', 'pan', 'leche', 'carne', 'pollo', 'pescado', 'verduras'],
        'cultural_tips': [
            "In Spanish-speaking countries, it's common to greet with a kiss on the cheek or a hug, even in business settings.",
            "The siesta tradition is still observed in many Spanish-speaking countries, with businesses closing from 2-4 PM.",
            "Family gatherings are extremely important in Hispanic culture, often lasting several hours with multiple generations present.",
            "Punctuality varies by country - in some places, arriving 15-30 minutes late is considered normal for social events."
        ]
    },
    'French': {
        'greetings': ['Bonjour', 'Bonsoir', 'Salut', 'Bonne nuit'],
        'basics': ['S\'il vous plaît', 'Merci', 'De rien', 'Pardon', 'Excusez-moi'],
        'questions': ['Comment allez-vous?', 'Comment vous appelez-vous?', 'Où habitez-vous?'],
        'family': ['mère', 'père', 'frère', 'sœur', 'fils', 'fille'],
        'numbers': ['un', 'deux', 'trois', 'quatre', 'cinq', 'six', 'sept', 'huit', 'neuf', 'dix'],
        'colors': ['rouge', 'bleu', 'vert', 'jaune', 'noir', 'blanc', 'rose', 'orange'],
        'food': ['nourriture', 'eau', 'pain', 'lait', 'viande', 'poulet', 'poisson', 'légumes'],
        'cultural_tips': [
            "French people value proper greetings - always say 'Bonjour' when entering shops or meeting someone.",
            "Lunch is sacred in France, typically lasting 1-2 hours with multiple courses.",
            "The French appreciate when foreigners attempt to speak French, even if imperfect.",
            "Tipping is not mandatory in France as service is included, but rounding up is appreciated."
        ]
    },
    'German': {
        'greetings': ['Guten Tag', 'Guten Morgen', 'Guten Abend', 'Gute Nacht'],
        'basics': ['Bitte', 'Danke', 'Bitte schön', 'Entschuldigung', 'Es tut mir leid'],
        'questions': ['Wie geht es Ihnen?', 'Wie heißen Sie?', 'Wo wohnen Sie?'],
        'family': ['Mutter', 'Vater', 'Bruder', 'Schwester', 'Sohn', 'Tochter'],
        'numbers': ['eins', 'zwei', 'drei', 'vier', 'fünf', 'sechs', 'sieben', 'acht', 'neun', 'zehn'],
        'colors': ['rot', 'blau', 'grün', 'gelb', 'schwarz', 'weiß', 'rosa', 'orange'],
        'food': ['Essen', 'Wasser', 'Brot', 'Milch', 'Fleisch', 'Huhn', 'Fisch', 'Gemüse'],
        'cultural_tips': [
            "Germans value punctuality highly - being late is considered disrespectful.",
            "Direct communication is preferred in German culture - beating around the bush is uncommon.",
            "Sunday is a day of rest in Germany - most shops are closed and loud activities are avoided.",
            "Germans often separate work and personal life strictly - don't be offended by formal interactions."
        ]
    }
}

CONVERSATION_SCENARIOS = {
    'Beginner': [
        {'scenario': 'Meeting Someone New', 'context': 'You\'re at a coffee shop and want to introduce yourself to someone.'},
        {'scenario': 'Ordering Food', 'context': 'You\'re at a restaurant and need to order your meal.'},
        {'scenario': 'Asking for Directions', 'context': 'You\'re lost and need to ask someone for help getting to the train station.'},
        {'scenario': 'Shopping', 'context': 'You\'re at a store and want to buy clothes.'}
    ],
    'Intermediate': [
        {'scenario': 'Job Interview', 'context': 'You\'re interviewing for a position at a local company.'},
        {'scenario': 'Making Plans', 'context': 'You\'re trying to coordinate weekend plans with friends.'},
        {'scenario': 'Discussing Hobbies', 'context': 'You\'re at a social gathering talking about your interests.'},
        {'scenario': 'Traveling', 'context': 'You\'re at the airport dealing with a flight delay.'}
    ],
    'Advanced': [
        {'scenario': 'Business Meeting', 'context': 'You\'re presenting a proposal to international clients.'},
        {'scenario': 'Cultural Discussion', 'context': 'You\'re debating cultural differences with native speakers.'},
        {'scenario': 'Problem Solving', 'context': 'You\'re working with a team to solve a complex issue.'},
        {'scenario': 'Academic Discussion', 'context': 'You\'re participating in a university seminar.'}
    ]
}

def get_user_level_score():
    """Calculate user's current level based on their progress"""
    profile = st.session_state.user_profile
    score = (
        profile['lessons_completed'] * 10 +
        profile['conversations_had'] * 15 +
        len(profile['vocabulary_mastered']) * 5 +
        profile['total_points']
    )
    return score

def get_adaptive_difficulty():
    """Determine appropriate difficulty based on user's progress"""
    score = get_user_level_score()
    if score < 100:
        return 'Beginner'
    elif score < 300:
        return 'Intermediate'
    else:
        return 'Advanced'

def simulate_pronunciation_score():
    """Simulate pronunciation scoring (in real app, this would use speech recognition)"""
    base_score = random.randint(70, 100)
    user_level = get_adaptive_difficulty()
    
    if user_level == 'Beginner':
        return max(60, base_score - 10)
    elif user_level == 'Intermediate':
        return max(70, base_score - 5)
    else:
        return base_score

def get_ai_response(user_input, scenario_context, language):
    """Generate AI response based on user input and context"""
    responses = {
        'Spanish': {
            'greeting': "¡Hola! Me llamo María. ¿Cómo te llamas?",
            'food': "¡Excelente elección! ¿Te gustaría algo de beber también?",
            'directions': "¡Por supuesto! La estación de tren está a dos cuadras hacia el norte.",
            'general': "Interesante. ¿Puedes contarme más sobre eso?"
        },
        'French': {
            'greeting': "Bonjour! Je m'appelle Marie. Comment vous appelez-vous?",
            'food': "Excellent choix! Voulez-vous quelque chose à boire aussi?",
            'directions': "Bien sûr! La gare est à deux pâtés de maisons vers le nord.",
            'general': "C'est intéressant. Pouvez-vous m'en dire plus?"
        },
        'German': {
            'greeting': "Hallo! Ich heiße Maria. Wie heißen Sie?",
            'food': "Ausgezeichnete Wahl! Möchten Sie auch etwas trinken?",
            'directions': "Natürlich! Der Bahnhof ist zwei Blocks nach Norden.",
            'general': "Das ist interessant. Können Sie mir mehr darüber erzählen?"
        }
    }
    
    # Simple keyword matching for demo purposes
    if any(word in user_input.lower() for word in ['hello', 'hi', 'hola', 'bonjour', 'hallo']):
        return responses[language]['greeting']
    elif any(word in user_input.lower() for word in ['food', 'eat', 'comida', 'manger', 'essen']):
        return responses[language]['food']
    elif any(word in user_input.lower() for word in ['direction', 'where', 'dónde', 'où', 'wo']):
        return responses[language]['directions']
    else:
        return responses[language]['general']

def create_dashboard():
    """Create the main dashboard"""
    st.markdown('<div class="main-header"><h1>🌍 AI Language Learning Companion</h1><p>Your personalized journey to fluency</p></div>', unsafe_allow_html=True)
    
    # User profile section
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("🏆 Total Points", st.session_state.user_profile['total_points'])
    
    with col2:
        st.metric("🔥 Current Streak", f"{st.session_state.user_profile['streak']} days")
    
    with col3:
        st.metric("📚 Lessons Completed", st.session_state.user_profile['lessons_completed'])
    
    with col4:
        st.metric("💬 Conversations", st.session_state.user_profile['conversations_had'])
    
    # Progress visualization
    st.subheader("📊 Your Learning Progress")
    
    # Create progress charts
    col1, col2 = st.columns(2)
    
    with col1:
        # Skill level radar chart
        skills = ['Vocabulary', 'Grammar', 'Pronunciation', 'Conversation', 'Listening', 'Reading']
        scores = [
            min(len(st.session_state.user_profile['vocabulary_mastered']), 10),
            random.randint(5, 10),  # Mock grammar score
            8 if st.session_state.user_profile['pronunciation_scores'] else 5,
            min(st.session_state.user_profile['conversations_had'], 10),
            random.randint(5, 10),  # Mock listening score
            random.randint(5, 10)   # Mock reading score
        ]
        
        fig = go.Figure()
        fig.add_trace(go.Scatterpolar(
            r=scores,
            theta=skills,
            fill='toself',
            name='Your Skills',
            marker=dict(color='rgb(102, 126, 234)')
        ))
        fig.update_layout(
            polar=dict(
                radialaxis=dict(
                    visible=True,
                    range=[0, 10]
                )),
            showlegend=False,
            title="Skill Assessment"
        )
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        # Weekly progress
        dates = [datetime.now() - timedelta(days=i) for i in range(7, 0, -1)]
        daily_points = [random.randint(10, 50) for _ in range(7)]
        
        fig = px.line(
            x=dates,
            y=daily_points,
            title="Weekly Learning Activity",
            labels={'x': 'Date', 'y': 'Points Earned'}
        )
        fig.update_traces(line_color='rgb(102, 126, 234)')
        st.plotly_chart(fig, use_container_width=True)
    
    # Achievements
    st.subheader("🏅 Recent Achievements")
    achievements = [
        "First Conversation Complete",
        "10 Words Mastered",
        "Perfect Pronunciation",
        "3-Day Streak"
    ]
    
    achievement_html = ""
    for achievement in achievements:
        achievement_html += f'<span class="achievement-badge">{achievement}</span>'
    
    st.markdown(achievement_html, unsafe_allow_html=True)

def create_profile_setup():
    """Create user profile setup"""
    st.header("👤 User Profile Setup")
    
    col1, col2 = st.columns(2)
    
    with col1:
        name = st.text_input("Your Name", value=st.session_state.user_profile.get('name', ''))
        native_language = st.selectbox(
            "Native Language",
            ['English', 'Spanish', 'French', 'German', 'Chinese', 'Japanese', 'Arabic'],
            index=0 if st.session_state.user_profile.get('native_language') == 'English' else 0
        )
        target_language = st.selectbox(
            "Target Language",
            ['Spanish', 'French', 'German', 'Italian', 'Portuguese', 'Chinese', 'Japanese'],
            index=0 if st.session_state.user_profile.get('target_language') == 'Spanish' else 0
        )
    
    with col2:
        level = st.selectbox(
            "Current Level",
            ['Beginner', 'Intermediate', 'Advanced'],
            index=['Beginner', 'Intermediate', 'Advanced'].index(st.session_state.user_profile.get('level', 'Beginner'))
        )
        daily_goal = st.slider("Daily Learning Goal (minutes)", 10, 120, st.session_state.user_profile.get('daily_goal', 20))
        interests = st.multiselect(
            "Learning Interests",
            ['Travel', 'Business', 'Culture', 'Food', 'Sports', 'Technology', 'Arts', 'Music'],
            default=st.session_state.user_profile.get('interests', [])
        )
    
    if st.button("Save Profile", type="primary"):
        st.session_state.user_profile.update({
            'name': name,
            'native_language': native_language,
            'target_language': target_language,
            'level': level,
            'daily_goal': daily_goal,
            'interests': interests
        })
        st.success("Profile updated successfully!")
        st.rerun()

def create_conversation_practice():
    """Create conversation practice interface"""
    st.header("💬 AI Conversation Partner")
    
    # Scenario selection
    target_language = st.session_state.user_profile['target_language']
    user_level = get_adaptive_difficulty()
    
    st.subheader(f"Current Level: {user_level}")
    
    scenarios = CONVERSATION_SCENARIOS.get(user_level, CONVERSATION_SCENARIOS['Beginner'])
    
    col1, col2 = st.columns([1, 2])
    
    with col1:
        st.subheader("Choose a Scenario")
        selected_scenario = st.selectbox(
            "Conversation Scenario",
            [s['scenario'] for s in scenarios],
            key="scenario_select"
        )
        
        scenario_context = next(s['context'] for s in scenarios if s['scenario'] == selected_scenario)
        st.info(f"**Context:** {scenario_context}")
        
        # Cultural tip
        if target_language in LANGUAGES:
            cultural_tip = random.choice(LANGUAGES[target_language]['cultural_tips'])
            st.markdown(f'<div class="cultural-tip"><strong>💡 Cultural Tip:</strong><br>{cultural_tip}</div>', unsafe_allow_html=True)
    
    with col2:
        st.subheader("Conversation")
        
        # Display conversation history
        chat_container = st.container()
        
        with chat_container:
            for i, message in enumerate(st.session_state.conversation_history):
                if message['role'] == 'user':
                    st.markdown(f'<div class="chat-message user-message"><strong>You:</strong> {message["content"]}</div>', unsafe_allow_html=True)
                else:
                    st.markdown(f'<div class="chat-message ai-message"><strong>AI Partner:</strong> {message["content"]}</div>', unsafe_allow_html=True)
        
        # User input
        user_input = st.text_input("Type your message:", key="conversation_input")
        
        col_send, col_pronounce, col_clear = st.columns([1, 1, 1])
        
        with col_send:
            if st.button("Send Message", type="primary"):
                if user_input:
                    # Add user message
                    st.session_state.conversation_history.append({
                        'role': 'user',
                        'content': user_input
                    })
                    
                    # Generate AI response
                    ai_response = get_ai_response(user_input, scenario_context, target_language)
                    st.session_state.conversation_history.append({
                        'role': 'assistant',
                        'content': ai_response
                    })
                    
                    # Update user stats
                    st.session_state.user_profile['conversations_had'] += 1
                    st.session_state.user_profile['total_points'] += 10
                    
                    st.rerun()
        
        with col_pronounce:
            if st.button("🎤 Practice Pronunciation"):
                if user_input:
                    # Simulate pronunciation analysis
                    score = simulate_pronunciation_score()
                    st.session_state.user_profile['pronunciation_scores'].append(score)
                    
                    if score >= 85:
                        st.success(f"Excellent pronunciation! Score: {score}/100")
                        st.session_state.user_profile['total_points'] += 15
                    elif score >= 70:
                        st.info(f"Good pronunciation! Score: {score}/100")
                        st.session_state.user_profile['total_points'] += 10
                    else:
                        st.warning(f"Keep practicing! Score: {score}/100")
                        st.session_state.user_profile['total_points'] += 5
        
        with col_clear:
            if st.button("Clear Chat"):
                st.session_state.conversation_history = []
                st.rerun()

def create_vocabulary_lessons():
    """Create vocabulary learning interface"""
    st.header("📚 Vocabulary Lessons")
    
    target_language = st.session_state.user_profile['target_language']
    
    if target_language not in LANGUAGES:
        st.warning(f"Vocabulary lessons for {target_language} are coming soon!")
        return
    
    language_data = LANGUAGES[target_language]
    
    # Lesson categories
    categories = list(language_data.keys())
    if 'cultural_tips' in categories:
        categories.remove('cultural_tips')
    
    selected_category = st.selectbox("Choose a lesson category:", categories)
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.subheader(f"📖 {selected_category.title()} Vocabulary")
        
        words = language_data[selected_category]
        
        # Create flashcard-style learning
        if f"current_{selected_category}_index" not in st.session_state:
            st.session_state[f"current_{selected_category}_index"] = 0
        
        current_index = st.session_state[f"current_{selected_category}_index"]
        current_word = words[current_index]
        
        # Display current word
        st.markdown(f"""
        <div style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); 
                    color: white; padding: 2rem; border-radius: 10px; text-align: center; margin: 1rem 0;">
            <h2 style="margin: 0; font-size: 3rem;">{current_word}</h2>
            <p style="margin: 0.5rem 0 0 0; opacity: 0.8;">Word {current_index + 1} of {len(words)}</p>
        </div>
        """, unsafe_allow_html=True)
        
        # Navigation buttons
        col_prev, col_next, col_master = st.columns(3)
        
        with col_prev:
            if st.button("⬅️ Previous", disabled=current_index == 0):
                st.session_state[f"current_{selected_category}_index"] = max(0, current_index - 1)
                st.rerun()
        
        with col_next:
            if st.button("➡️ Next", disabled=current_index == len(words) - 1):
                st.session_state[f"current_{selected_category}_index"] = min(len(words) - 1, current_index + 1)
                st.rerun()
        
        with col_master:
            if st.button("✅ Mark as Mastered"):
                if current_word not in st.session_state.user_profile['vocabulary_mastered']:
                    st.session_state.user_profile['vocabulary_mastered'].append(current_word)
                    st.session_state.user_profile['total_points'] += 20
                    st.success(f"Great! You've mastered '{current_word}'")
                else:
                    st.info("Already mastered!")
    
    with col2:
        st.subheader("🎯 Practice Quiz")
        
        # Simple quiz functionality
        if st.button("Start Quiz", type="primary"):
            quiz_words = random.sample(words, min(5, len(words)))
            st.session_state.current_quiz = {
                'words': quiz_words,
                'current_question': 0,
                'score': 0,
                'answers': []
            }
        
        if 'current_quiz' in st.session_state and st.session_state.current_quiz:
            quiz = st.session_state.current_quiz
            
            if quiz['current_question'] < len(quiz['words']):
                current_word = quiz['words'][quiz['current_question']]
                st.write(f"**Question {quiz['current_question'] + 1}/{len(quiz['words'])}**")
                st.write(f"What does '{current_word}' mean in English?")
                
                # Generate multiple choice options (simplified)
                options = ["Option A", "Option B", "Option C", "Correct Answer"]
                random.shuffle(options)
                
                answer = st.radio("Choose your answer:", options, key=f"quiz_{quiz['current_question']}")
                
                if st.button("Submit Answer"):
                    is_correct = answer == "Correct Answer"
                    if is_correct:
                        quiz['score'] += 1
                        st.success("Correct!")
                    else:
                        st.error("Try again next time!")
                    
                    quiz['current_question'] += 1
                    st.session_state.user_profile['total_points'] += 5 if is_correct else 2
                    st.rerun()
            else:
                # Quiz completed
                st.success(f"Quiz completed! Your score: {quiz['score']}/{len(quiz['words'])}")
                st.session_state.user_profile['lessons_completed'] += 1
                if st.button("Start New Quiz"):
                    del st.session_state.current_quiz
                    st.rerun()
        
        # Vocabulary progress
        st.subheader("📊 Your Vocabulary Progress")
        mastered_count = len(st.session_state.user_profile['vocabulary_mastered'])
        total_words = sum(len(words) for words in language_data.values() if isinstance(words, list))
        
        progress = mastered_count / total_words if total_words > 0 else 0
        st.progress(progress)
        st.write(f"Words mastered: {mastered_count}/{total_words}")
        
        # Recent mastered words
        if st.session_state.user_profile['vocabulary_mastered']:
            st.subheader("🏆 Recently Mastered")
            recent_words = st.session_state.user_profile['vocabulary_mastered'][-5:]
            for word in recent_words:
                st.write(f"✅ {word}")

def create_pronunciation_practice():
    """Create pronunciation practice interface"""
    st.header("🎤 Pronunciation Practice")
    
    target_language = st.session_state.user_profile['target_language']
    
    if target_language not in LANGUAGES:
        st.warning(f"Pronunciation practice for {target_language} is coming soon!")
        return
    
    language_data = LANGUAGES[target_language]
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.subheader("🗣️ Practice Session")
        
        # Select practice type
        practice_type = st.selectbox(
            "Choose practice type:",
            ["Individual Words", "Common Phrases", "Tongue Twisters"]
        )
        
        if practice_type == "Individual Words":
            # Get random words from vocabulary
            all_words = []
            for category, words in language_data.items():
                if isinstance(words, list):
                    all_words.extend(words)
            
            if all_words:
                practice_word = st.selectbox("Select a word to practice:", all_words)
                
                st.markdown(f"""
                <div style="background: #f0f2f6; padding: 2rem; border-radius: 10px; text-align: center; margin: 1rem 0;">
                    <h3 style="margin: 0; color: #333;">Practice Word:</h3>
                    <h1 style="margin: 0.5rem 0; color: #667eea; font-size: 3rem;">{practice_word}</h1>
                </div>
                """, unsafe_allow_html=True)
                
                col_record, col_listen = st.columns(2)
                
                with col_record:
                    if st.button("🎤 Record Pronunciation", type="primary"):
                        # Simulate recording and analysis
                        with st.spinner("Analyzing pronunciation..."):
                            time.sleep(2)
                            score = simulate_pronunciation_score()
                            st.session_state.pronunciation_feedback.append({
                                'word': practice_word,
                                'score': score,
                                'timestamp': datetime.now().isoformat()
                            })
                            
                            if score >= 90:
                                st.success(f"🎉 Excellent! Score: {score}/100")
                                st.balloons()
                                st.session_state.user_profile['total_points'] += 25
                            elif score >= 80:
                                st.success(f"👍 Very Good! Score: {score}/100")
                                st.session_state.user_profile['total_points'] += 20
                            elif score >= 70:
                                st.info(f"😊 Good! Score: {score}/100")
                                st.session_state.user_profile['total_points'] += 15
                            elif score >= 60:
                                st.warning(f"🤔 Keep practicing! Score: {score}/100")
                                st.session_state.user_profile['total_points'] += 10
                            else:
                                st.error(f"😅 Try again! Score: {score}/100")
                                st.session_state.user_profile['total_points'] += 5
                
                with col_listen:
                    if st.button("🔊 Listen to Pronunciation"):
                        st.info("🎵 Playing pronunciation... (Audio would play here)")
                    elif practice_type == "Common Phrases":
                         phrases = [
                "Hello, how are you?",
                "Thank you very much",
                "Where is the bathroom?",
                "I don't understand",
                "Can you help me?",
                "What time is it?",
                "I'm sorry",
                "Excuse me"
            ]
            
            practice_phrase = st.selectbox("Select a phrase to practice:", phrases)
            
            st.markdown(f"""
            <div style="background: #f0f2f6; padding: 2rem; border-radius: 10px; text-align: center; margin: 1rem 0;">
                <h3 style="margin: 0; color: #333;">Practice Phrase:</h3>
                <h2 style="margin: 0.5rem 0; color: #667eea;">{practice_phrase}</h2>
            </div>
            """, unsafe_allow_html=True)
            
            if st.button("🎤 Record Phrase", type="primary"):
                with st.spinner("Analyzing pronunciation..."):
                    time.sleep(2)
                    score = simulate_pronunciation_score()
                    st.session_state.pronunciation_feedback.append({
                        'phrase': practice_phrase,
                        'score': score,
                        'timestamp': datetime.now().isoformat()
                    })
                    
                    if score >= 85:
                        st.success(f"🎉 Excellent phrase pronunciation! Score: {score}/100")
                        st.session_state.user_profile['total_points'] += 30
                    else:
                        st.info(f"Good effort! Score: {score}/100")
                        st.session_state.user_profile['total_points'] += 15
        
        elif practice_type == "Tongue Twisters":
            twisters = {
                'Spanish': [
                    "Tres tristes tigres tragaban trigo en un trigal",
                    "El perro de San Roque no tiene rabo",
                    "Pablito clavó un clavito"
                ],
                'French': [
                    "Les chaussettes de l'archiduchesse",
                    "Un chasseur sachant chasser",
                    "Ces six saucissons-ci sont si secs"
                ],
                'German': [
                    "Fischers Fritz fischt frische Fische",
                    "Brautkleid bleibt Brautkleid",
                    "Zehn zahme Ziegen"
                ]
            }
            
            language_twisters = twisters.get(target_language, twisters['Spanish'])
            practice_twister = st.selectbox("Select a tongue twister:", language_twisters)
            
            st.markdown(f"""
            <div style="background: #fff3e0; padding: 2rem; border-radius: 10px; text-align: center; margin: 1rem 0; border: 2px solid #ffb74d;">
                <h3 style="margin: 0; color: #333;">🌪️ Tongue Twister Challenge:</h3>
                <h2 style="margin: 0.5rem 0; color: #ff9800;">{practice_twister}</h2>
            </div>
            """, unsafe_allow_html=True)
            
            if st.button("🎤 Challenge Accepted!", type="primary"):
                with st.spinner("Analyzing your tongue twister..."):
                    time.sleep(3)
                    score = simulate_pronunciation_score()
                    st.session_state.pronunciation_feedback.append({
                        'twister': practice_twister,
                        'score': score,
                        'timestamp': datetime.now().isoformat()
                    })
                    
                    if score >= 90:
                        st.success(f"🏆 AMAZING! Tongue twister master! Score: {score}/100")
                        st.balloons()
                        st.session_state.user_profile['total_points'] += 50
                    elif score >= 80:
                        st.success(f"🎉 Great job! Score: {score}/100")
                        st.session_state.user_profile['total_points'] += 40
                    else:
                        st.info(f"Good attempt! Tongue twisters are tricky! Score: {score}/100")
                        st.session_state.user_profile['total_points'] += 25
    
    with col2:
        st.subheader("📊 Pronunciation Analytics")
        
        # Display recent pronunciation scores
        if st.session_state.pronunciation_feedback:
            recent_scores = [item['score'] for item in st.session_state.pronunciation_feedback[-10:]]
            
            # Create line chart of progress
            fig = px.line(
                x=list(range(1, len(recent_scores) + 1)),
                y=recent_scores,
                title="Recent Pronunciation Scores",
                labels={'x': 'Attempt', 'y': 'Score'}
            )
            fig.update_traces(line_color='rgb(102, 126, 234)')
            fig.update_layout(yaxis_range=[0, 100])
            st.plotly_chart(fig, use_container_width=True)
            
            # Average score
            avg_score = sum(recent_scores) / len(recent_scores)
            st.metric("Average Score", f"{avg_score:.1f}/100")
            
            # Pronunciation tips based on performance
            if avg_score >= 85:
                st.success("🎯 Excellent pronunciation! You're doing great!")
            elif avg_score >= 70:
                st.info("👍 Good progress! Keep practicing to improve further.")
            else:
                st.warning("💪 Focus on pronunciation practice to improve your scores.")
        else:
            st.info("Start practicing to see your pronunciation analytics!")
        
        # Pronunciation tips
        st.subheader("💡 Pronunciation Tips")
        tips = [
            "Listen to native speakers and try to mimic their pronunciation",
            "Practice individual sounds before attempting full words",
            "Use a mirror to watch your mouth movements",
            "Record yourself and compare with native pronunciation",
            "Focus on stress patterns and intonation",
            "Practice little and often for better retention"
        ]
        
        for tip in tips:
            st.write(f"• {tip}")

def create_cultural_insights():
    """Create cultural insights and tips section"""
    st.header("🌍 Cultural Insights")
    
    target_language = st.session_state.user_profile['target_language']
    
    if target_language not in LANGUAGES:
        st.warning(f"Cultural insights for {target_language} are coming soon!")
        return
    
    cultural_tips = LANGUAGES[target_language]['cultural_tips']
    
    st.subheader(f"🎭 {target_language} Cultural Tips")
    
    # Display cultural tips in cards
    for i, tip in enumerate(cultural_tips):
        st.markdown(f"""
        <div class="cultural-tip">
            <h4>💡 Cultural Tip #{i+1}</h4>
            <p>{tip}</p>
        </div>
        """, unsafe_allow_html=True)
    
    # Interactive cultural quiz
    st.subheader("🧩 Cultural Knowledge Quiz")
    
    quiz_questions = {
        'Spanish': [
            {
                'question': "What time do people typically eat dinner in Spain?",
                'options': ["6 PM", "8 PM", "10 PM", "12 AM"],
                'correct': 2,
                'explanation': "In Spain, dinner is typically eaten very late, often around 10 PM or later."
            },
            {
                'question': "What is the appropriate greeting in most Spanish-speaking countries?",
                'options': ["Handshake", "Bow", "Kiss on cheek", "Wave"],
                'correct': 2,
                'explanation': "A kiss on the cheek (or air kiss) is common, even in business settings."
            }
        ],
        'French': [
            {
                'question': "What should you always do when entering a French shop?",
                'options': ["Smile and wave", "Say 'Bonjour'", "Nod silently", "Ask for help immediately"],
                'correct': 1,
                'explanation': "Always greet with 'Bonjour' - it's considered rude not to greet in France."
            },
            {
                'question': "How long is a typical French lunch break?",
                'options': ["30 minutes", "1 hour", "1-2 hours", "3 hours"],
                'correct': 2,
                'explanation': "French lunch breaks are typically 1-2 hours, reflecting the importance of meals."
            }
        ],
        'German': [
            {
                'question': "How important is punctuality in German culture?",
                'options': ["Not important", "Somewhat important", "Very important", "Only for business"],
                'correct': 2,
                'explanation': "Punctuality is extremely important in German culture and being late is considered disrespectful."
            },
            {
                'question': "What happens to most German shops on Sundays?",
                'options': ["Open as usual", "Close early", "Most are closed", "Only food shops open"],
                'correct': 2,
                'explanation': "Most shops in Germany are closed on Sundays as it's considered a day of rest."
            }
        ]
    }
    
    if target_language in quiz_questions:
        questions = quiz_questions[target_language]
        
        if 'cultural_quiz_started' not in st.session_state:
            st.session_state.cultural_quiz_started = False
            st.session_state.cultural_quiz_score = 0
            st.session_state.cultural_quiz_question = 0
        
        if not st.session_state.cultural_quiz_started:
            if st.button("Start Cultural Quiz", type="primary"):
                st.session_state.cultural_quiz_started = True
                st.session_state.cultural_quiz_score = 0
                st.session_state.cultural_quiz_question = 0
                st.rerun()
        
        else:
            if st.session_state.cultural_quiz_question < len(questions):
                current_q = questions[st.session_state.cultural_quiz_question]
                st.write(f"**Question {st.session_state.cultural_quiz_question + 1}/{len(questions)}**")
                st.write(current_q['question'])
                
                answer = st.radio("Choose your answer:", current_q['options'], key=f"cultural_q_{st.session_state.cultural_quiz_question}")
                
                if st.button("Submit Answer"):
                    if current_q['options'].index(answer) == current_q['correct']:
                        st.success("Correct! " + current_q['explanation'])
                        st.session_state.cultural_quiz_score += 1
                        st.session_state.user_profile['total_points'] += 15
                    else:
                        st.error("Not quite right. " + current_q['explanation'])
                        st.session_state.user_profile['total_points'] += 5
                    
                    st.session_state.cultural_quiz_question += 1
                    time.sleep(2)
                    st.rerun()
            else:
                st.success(f"Quiz completed! Your score: {st.session_state.cultural_quiz_score}/{len(questions)}")
                if st.session_state.cultural_quiz_score == len(questions):
                    st.balloons()
                    st.write("🎉 Perfect score! You're a cultural expert!")
                
                if st.button("Restart Quiz"):
                    st.session_state.cultural_quiz_started = False
                    st.rerun()

def create_progress_analytics():
    """Create detailed progress analytics"""
    st.header("📈 Progress Analytics")
    
    profile = st.session_state.user_profile
    
    # Overall progress summary
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("🎯 Total Points", profile['total_points'])
    with col2:
        st.metric("📚 Lessons Completed", profile['lessons_completed'])
    with col3:
        st.metric("💬 Conversations", profile['conversations_had'])
    with col4:
        st.metric("🔤 Words Mastered", len(profile['vocabulary_mastered']))
    
    # Detailed analytics
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("📊 Learning Streak")
        
        # Simulate learning activity over time
        dates = [datetime.now() - timedelta(days=i) for i in range(30, 0, -1)]
        activity = [random.choice([0, 1, 1, 1, 2, 2, 3]) for _ in range(30)]
        
        # Create heatmap-style calendar
        fig = px.imshow(
            [activity],
            x=[d.strftime('%m-%d') for d in dates],
            color_continuous_scale='Blues',
            title="Daily Learning Activity (Last 30 Days)"
        )
        fig.update_layout(
            xaxis_title="Date",
            yaxis_title="",
            yaxis_showticklabels=False
        )
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        st.subheader("🎯 Skill Breakdown")
        
        # Create pie chart of points distribution
        skills = ['Vocabulary', 'Pronunciation', 'Conversation', 'Cultural Knowledge']
        points = [
            len(profile['vocabulary_mastered']) * 20,
            len(st.session_state.pronunciation_feedback) * 15,
            profile['conversations_had'] * 10,
            profile['lessons_completed'] * 25
        ]
        
        if sum(points) > 0:
            fig = px.pie(
                values=points,
                names=skills,
                title="Points Distribution by Skill"
            )
            st.plotly_chart(fig, use_container_width=True)
        else:
            st.info("Start learning to see your skill breakdown!")
    
    # Learning recommendations
    st.subheader("🎯 Personalized Recommendations")
    
    score = get_user_level_score()
    if score < 50:
        st.info("💡 Focus on vocabulary building and basic conversations to improve your foundation.")
    elif score < 150:
        st.info("💡 Great progress! Try more challenging conversations and pronunciation practice.")
    else:
        st.info("💡 Excellent work! Continue with advanced conversations and cultural learning.")
    
    # Achievement system
    st.subheader("🏆 Achievement System")
    
    achievements = [
        {"name": "First Steps", "description": "Complete your first lesson", "unlocked": profile['lessons_completed'] >= 1},
        {"name": "Chatterbox", "description": "Have 5 conversations", "unlocked": profile['conversations_had'] >= 5},
        {"name": "Word Master", "description": "Master 20 vocabulary words", "unlocked": len(profile['vocabulary_mastered']) >= 20},
        {"name": "Pronunciation Pro", "description": "Score 90+ on pronunciation", "unlocked": any(score >= 90 for score in profile['pronunciation_scores'])},
        {"name": "Streak Keeper", "description": "Maintain a 7-day streak", "unlocked": profile['streak'] >= 7},
        {"name": "Point Collector", "description": "Earn 500 total points", "unlocked": profile['total_points'] >= 500}
    ]
    
    for achievement in achievements:
        if achievement['unlocked']:
            st.success(f"🏆 {achievement['name']}: {achievement['description']}")
        else:
            st.info(f"🔒 {achievement['name']}: {achievement['description']}")

def main():
    """Main application function"""
    
    # Sidebar navigation
    with st.sidebar:
        st.title("🌍 Language Learning")
        
        # User greeting
        if st.session_state.user_profile['name']:
            st.write(f"Welcome back, {st.session_state.user_profile['name']}! 👋")
        
        # Navigation menu
        page = st.selectbox(
            "Choose a section:",
            [
                "🏠 Dashboard",
                "👤 Profile Setup", 
                "💬 Conversation Practice",
                "📚 Vocabulary Lessons",
                "🎤 Pronunciation Practice",
                "🌍 Cultural Insights",
                "📈 Progress Analytics"
            ]
        )
        
        # Quick stats in sidebar
        st.markdown("---")
        st.subheader("Quick Stats")
        st.metric("Points", st.session_state.user_profile['total_points'])
        st.metric("Streak", f"{st.session_state.user_profile['streak']} days")
        
        # Language info
        st.markdown("---")
        st.subheader("Current Settings")
        st.write(f"**Target:** {st.session_state.user_profile['target_language']}")
        st.write(f"**Level:** {st.session_state.user_profile['level']}")
        
        # Daily goal progress
        st.markdown("---")
        st.subheader("Daily Goal")
        # Simulate daily progress
        daily_minutes = random.randint(5, st.session_state.user_profile['daily_goal'])
        progress = min(daily_minutes / st.session_state.user_profile['daily_goal'], 1.0)
        st.progress(progress)
        st.write(f"{daily_minutes}/{st.session_state.user_profile['daily_goal']} minutes")
    
    # Main content area
    if page == "🏠 Dashboard":
        create_dashboard()
    elif page == "👤 Profile Setup":
        create_profile_setup()
    elif page == "💬 Conversation Practice":
        create_conversation_practice()
    elif page == "📚 Vocabulary Lessons":
        create_vocabulary_lessons()
    elif page == "🎤 Pronunciation Practice":
        create_pronunciation_practice()
    elif page == "🌍 Cultural Insights":
        create_cultural_insights()
    elif page == "📈 Progress Analytics":
        create_progress_analytics()
    
    # Footer
    st.markdown("---")
    st.markdown(
        """
        <div style="text-align: center; color: #666; padding: 2rem;">
            <p>🌟 Keep learning, keep growing! 🌟</p>
            <p>Made with ❤️ for language learners worldwide</p>
        </div>
        """,
        unsafe_allow_html=True
    )

if __name__ == "__main__":
    main()
