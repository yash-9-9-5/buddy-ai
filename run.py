from app import app

if __name__ == "__main__":
    print("Starting BUDDY AI web server on port 5005...")
    print("Open your browser and navigate to: http://localhost:5005")
    app.run(host='0.0.0.0', port=5005, debug=True) 