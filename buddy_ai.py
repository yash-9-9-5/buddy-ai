import speech_recognition as sr
import pyttsx3
import json
import random
import time
import os
import requests
from datetime import datetime
import re

class BuddyAI:
    def __init__(self):
        # Initialize speech recognition
        self.recognizer = sr.Recognizer()
        
        # Initialize text-to-speech engine
        self.engine = pyttsx3.init()
        self.engine.setProperty('rate', 150)  # Speed of speech
        
        # User session data
        self.user_session = {
            'platform': None,
            'focus_area': None,
            'last_interaction': None
        }
        
        # Greeting messages
        self.greetings = [
            "Hello! I'm BUDDY, your social media management assistant. How can I help you today?",
            "Hi there! I'm BUDDY, ready to help with your social media strategy. What would you like to know?",
            "Welcome! I'm BUDDY, your AI social media manager. What would you like to learn about?"
        ]
        
        # Farewell messages
        self.farewells = [
            "Goodbye! Feel free to ask for more help anytime.",
            "See you later! I'm here whenever you need social media advice.",
            "Take care! Don't hesitate to reach out if you need more guidance."
        ]
        
        # Google Search API configuration
        self.google_api_key = os.environ.get('GOOGLE_API_KEY', 'YOUR_GOOGLE_API_KEY')
        self.google_cse_id = os.environ.get('GOOGLE_CSE_ID', 'YOUR_GOOGLE_CSE_ID')
    
    def speak(self, text):
        """Convert text to speech"""
        print(f"BUDDY: {text}")
        self.engine.say(text)
        self.engine.runAndWait()
    
    def listen(self):
        """Listen for user input through microphone"""
        with sr.Microphone() as source:
            print("Listening...")
            self.recognizer.adjust_for_ambient_noise(source, duration=0.5)
            audio = self.recognizer.listen(source)
            
            try:
                text = self.recognizer.recognize_google(audio)
                print(f"User: {text}")
                return text.lower()
            except sr.UnknownValueError:
                return "I couldn't understand that. Could you please repeat?"
            except sr.RequestError:
                return "Sorry, there was an error with the speech recognition service."
    
    def get_text_input(self):
        """Get user input through text"""
        return input("You: ").lower()
    
    def identify_platform(self, user_input):
        """Identify which social media platform the user is asking about"""
        platforms = {
            'instagram': ['instagram', 'ig', 'insta'],
            'youtube': ['youtube', 'yt', 'video'],
            'facebook': ['facebook', 'fb', 'meta']
        }
        
        for platform, keywords in platforms.items():
            if any(keyword in user_input for keyword in keywords):
                return platform
        
        return None
    
    def identify_focus_area(self, user_input):
        """Identify what aspect of social media the user is asking about"""
        focus_areas = {
            'content': ['content', 'post', 'create', 'make', 'design', 'photo', 'video'],
            'marketing': ['marketing', 'promote', 'ad', 'advertise', 'reach', 'audience', 'followers'],
            'engagement': ['engagement', 'interact', 'comment', 'respond', 'community', 'fans']
        }
        
        for area, keywords in focus_areas.items():
            if any(keyword in user_input for keyword in keywords):
                return area
        
        return None
    
    def search_google(self, query):
        """Search Google for information using the Google Custom Search API"""
        try:
            # Format the query for better search results
            search_query = f"{query} social media tips best practices"
            
            # Use Google Custom Search API
            url = "https://www.googleapis.com/customsearch/v1"
            params = {
                'key': self.google_api_key,
                'cx': self.google_cse_id,
                'q': search_query,
                'num': 5  # Number of results to return
            }
            
            print(f"Searching with API key: {self.google_api_key[:10]}... and CSE ID: {self.google_cse_id}")
            response = requests.get(url, params=params)
            
            if response.status_code == 200:
                data = response.json()
                
                # Check if we have search results
                if 'items' in data and len(data['items']) > 0:
                    # Combine the results into a comprehensive answer
                    answer = f"Here's what I found about {query}:\n\n"
                    
                    # Add up to 5 search results
                    for i, item in enumerate(data['items'][:5]):
                        title = item.get('title', 'No title')
                        snippet = item.get('snippet', 'No description available')
                        link = item.get('link', '#')
                        
                        answer += f"{i+1}. {title}\n"
                        answer += f"   {snippet}\n"
                        answer += f"   Source: {link}\n\n"
                    
                    answer += "Would you like more specific information about any aspect of this topic?"
                    
                    return answer
                else:
                    print("No search results found in the response")
                    return self.get_fallback_response(query)
            else:
                print(f"Error with Google API: {response.status_code}")
                print(f"Response content: {response.text}")
                return self.get_fallback_response(query)
                
        except Exception as e:
            print(f"Error searching Google: {str(e)}")
            return self.get_fallback_response(query)
    
    def get_fallback_response(self, query):
        """Provide a fallback response when search fails"""
        platform = self.identify_platform(query)
        focus_area = self.identify_focus_area(query)
        
        if platform and focus_area:
            return f"I'm having trouble searching for specific information about {focus_area} on {platform}. Could you please rephrase your question or try a different topic?"
        elif platform:
            return f"I'm having trouble searching for specific information about {platform}. Could you please rephrase your question or try a different platform?"
        else:
            return "I'm having trouble finding specific information for your query. Could you please rephrase your question or try a different topic?"
    
    def generate_response(self, user_input):
        """Generate a response based on user input"""
        # Update last interaction time
        self.user_session['last_interaction'] = datetime.now()
        
        # Check for greetings
        greetings = ['hi', 'hello', 'hey', 'good morning', 'good afternoon', 'good evening']
        if any(greeting in user_input for greeting in greetings):
            return random.choice(self.greetings)
        
        # Check for farewells
        farewells = ['bye', 'goodbye', 'see you', 'thanks', 'thank you']
        if any(farewell in user_input for farewell in farewells):
            return random.choice(self.farewells)
        
        # Identify platform
        platform = self.identify_platform(user_input)
        if platform:
            self.user_session['platform'] = platform
        
        # Identify focus area
        focus_area = self.identify_focus_area(user_input)
        if focus_area:
            self.user_session['focus_area'] = focus_area
        
        # Search for information based on the user's query
        return self.search_google(user_input)
    
    def run(self, input_mode='text'):
        """Run the AI agent"""
        self.speak(random.choice(self.greetings))
        
        while True:
            # Get user input based on mode
            if input_mode == 'voice':
                user_input = self.listen()
            else:
                user_input = self.get_text_input()
            
            # Check for exit command
            if user_input in ['exit', 'quit', 'bye', 'goodbye']:
                self.speak(random.choice(self.farewells))
                break
            
            # Generate and speak response
            response = self.generate_response(user_input)
            self.speak(response)
            
            # Ask if user wants to continue
            self.speak("Do you have any other questions? Or would you like to exit?")
            
            if input_mode == 'voice':
                continue_input = self.listen()
            else:
                continue_input = self.get_text_input()
            
            if continue_input in ['exit', 'quit', 'bye', 'goodbye', 'no']:
                self.speak(random.choice(self.farewells))
                break

if __name__ == "__main__":
    # Create and run the AI agent
    buddy = BuddyAI()
    
    # Ask user for input mode
    print("Welcome to BUDDY - Your AI Social Media Manager")
    print("Choose input mode:")
    print("1. Text")
    print("2. Voice")
    
    choice = input("Enter your choice (1 or 2): ")
    
    if choice == "2":
        buddy.run(input_mode='voice')
    else:
        buddy.run(input_mode='text')