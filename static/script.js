document.addEventListener('DOMContentLoaded', () => {
    // DOM Elements
    const chatMessages = document.getElementById('chatMessages');
    const userInput = document.getElementById('userInput');
    const sendButton = document.getElementById('sendButton');
    const voiceButton = document.getElementById('voiceButton');
    const platformButtons = document.querySelectorAll('.platform-btn');
    const currentPlatform = document.getElementById('currentPlatform');
    const currentFocusArea = document.getElementById('currentFocusArea');
    
    // Speech recognition setup
    let recognition;
    let isListening = false;
    
    if ('webkitSpeechRecognition' in window) {
        recognition = new webkitSpeechRecognition();
        recognition.continuous = false;
        recognition.interimResults = false;
        
        recognition.onresult = (event) => {
            const transcript = event.results[0][0].transcript;
            userInput.value = transcript;
            isListening = false;
            voiceButton.classList.remove('active');
        };
        
        recognition.onend = () => {
            isListening = false;
            voiceButton.classList.remove('active');
        };
        
        recognition.onerror = (event) => {
            console.error('Speech recognition error:', event.error);
            isListening = false;
            voiceButton.classList.remove('active');
        };
    } else {
        voiceButton.style.display = 'none';
        console.log('Speech recognition not supported in this browser');
    }
    
    // Add message to chat
    function addMessage(message, isUser = false) {
        const messageDiv = document.createElement('div');
        messageDiv.classList.add('message');
        messageDiv.classList.add(isUser ? 'user-message' : 'buddy-message');
        
        const messageContent = document.createElement('div');
        messageContent.classList.add('message-content');
        
        // Check if the message contains links or formatted content
        if (message.includes('http') || message.includes('www.')) {
            // Process links in the message
            const processedMessage = processLinks(message);
            messageContent.innerHTML = processedMessage;
        } else {
            // Format the message with line breaks
            const formattedMessage = formatMessage(message);
            messageContent.innerHTML = formattedMessage;
        }
        
        messageDiv.appendChild(messageContent);
        chatMessages.appendChild(messageDiv);
        
        // Scroll to bottom
        chatMessages.scrollTop = chatMessages.scrollHeight;
    }
    
    // Format message with line breaks and styling
    function formatMessage(message) {
        // Replace line breaks with <br> tags
        let formatted = message.replace(/\n/g, '<br>');
        
        // Format numbered lists
        formatted = formatted.replace(/(\d+)\.\s/g, '<strong>$1.</strong> ');
        
        // Format bullet points
        formatted = formatted.replace(/\-\s/g, '• ');
        
        // Highlight important terms
        const importantTerms = ['Instagram', 'YouTube', 'Facebook', 'content', 'marketing', 'engagement'];
        importantTerms.forEach(term => {
            const regex = new RegExp(`\\b${term}\\b`, 'gi');
            formatted = formatted.replace(regex, `<span class="highlight">${term}</span>`);
        });
        
        return formatted;
    }
    
    // Process links in the message
    function processLinks(message) {
        // Convert URLs to clickable links
        const urlRegex = /(https?:\/\/[^\s]+)|(www\.[^\s]+\.[^\s]+)/g;
        return message.replace(urlRegex, url => {
            const href = url.startsWith('www.') ? `https://${url}` : url;
            return `<a href="${href}" target="_blank" rel="noopener noreferrer">${url}</a>`;
        });
    }
    
    // Send message to BUDDY
    async function sendMessage() {
        const message = userInput.value.trim();
        
        if (message === '') return;
        
        // Add user message to chat
        addMessage(message, true);
        
        // Clear input
        userInput.value = '';
        
        try {
            // Show typing indicator
            const typingDiv = document.createElement('div');
            typingDiv.classList.add('message', 'buddy-message', 'typing');
            typingDiv.innerHTML = '<div class="message-content"><p>BUDDY is searching for information...</p></div>';
            chatMessages.appendChild(typingDiv);
            chatMessages.scrollTop = chatMessages.scrollHeight;
            
            // Send message to server
            const response = await fetch('/api/chat', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ message }),
            });
            
            // Remove typing indicator
            chatMessages.removeChild(typingDiv);
            
            const data = await response.json();
            
            // Add BUDDY's response to chat
            addMessage(data.response);
            
            // Update session info
            updateSessionInfo(data.platform, data.focus_area);
            
        } catch (error) {
            console.error('Error sending message:', error);
            addMessage('Sorry, there was an error processing your request. Please try again.');
        }
    }
    
    // Update session info display
    function updateSessionInfo(platform, focusArea) {
        if (platform) {
            currentPlatform.textContent = platform.charAt(0).toUpperCase() + platform.slice(1);
            
            // Update platform button active state
            platformButtons.forEach(btn => {
                if (btn.dataset.platform === platform) {
                    btn.classList.add('active');
                } else {
                    btn.classList.remove('active');
                }
            });
        }
        
        if (focusArea) {
            currentFocusArea.textContent = focusArea.charAt(0).toUpperCase() + focusArea.slice(1);
        }
    }
    
    // Event Listeners
    sendButton.addEventListener('click', sendMessage);
    
    userInput.addEventListener('keypress', (e) => {
        if (e.key === 'Enter') {
            sendMessage();
        }
    });
    
    voiceButton.addEventListener('click', () => {
        if (!recognition) return;
        
        if (isListening) {
            recognition.stop();
        } else {
            recognition.start();
            isListening = true;
            voiceButton.classList.add('active');
        }
    });
    
    platformButtons.forEach(button => {
        button.addEventListener('click', () => {
            const platform = button.dataset.platform;
            userInput.value = `Tell me everything about ${platform} social media strategy`;
            sendMessage();
        });
    });
    
    // Add some CSS for highlights
    const style = document.createElement('style');
    style.textContent = `
        .highlight {
            color: var(--accent-primary);
            font-weight: bold;
        }
        
        a {
            color: var(--accent-secondary);
            text-decoration: underline;
        }
        
        a:hover {
            color: var(--accent-hover);
        }
    `;
    document.head.appendChild(style);
}); 