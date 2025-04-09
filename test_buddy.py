from buddy_ai import BuddyAI

def test_text_mode():
    """Test the BUDDY AI agent in text mode"""
    print("\n=== Testing BUDDY AI in Text Mode ===\n")
    
    buddy = BuddyAI()
    
    # Simulate a conversation
    test_inputs = [
        "Hi BUDDY",
        "I need help with Instagram",
        "I want content tips",
        "What about marketing strategies?",
        "Thanks for the help",
        "bye"
    ]
    
    # Start conversation
    print("BUDDY: Hello! I'm BUDDY, your social media management assistant. How can I help you today?")
    
    # Process each test input
    for user_input in test_inputs:
        print(f"\nUser: {user_input}")
        response = buddy.generate_response(user_input)
        print(f"BUDDY: {response}")
    
    print("\n=== Text Mode Test Complete ===\n")

def test_voice_mode():
    """Test the BUDDY AI agent in voice mode"""
    print("\n=== Testing BUDDY AI in Voice Mode ===\n")
    print("This test will use your microphone. Please speak when prompted.")
    print("Press Ctrl+C to exit the test at any time.")
    
    try:
        buddy = BuddyAI()
        buddy.run(input_mode='voice')
    except KeyboardInterrupt:
        print("\nVoice test interrupted by user.")
    except Exception as e:
        print(f"\nError during voice test: {e}")
    
    print("\n=== Voice Mode Test Complete ===\n")

if __name__ == "__main__":
    print("BUDDY AI Test Script")
    print("===================")
    
    # Ask user which test to run
    print("\nWhich test would you like to run?")
    print("1. Text Mode Test (simulated conversation)")
    print("2. Voice Mode Test (requires microphone)")
    print("3. Exit")
    
    choice = input("\nEnter your choice (1-3): ")
    
    if choice == "1":
        test_text_mode()
    elif choice == "2":
        test_voice_mode()
    else:
        print("Exiting test script.") 