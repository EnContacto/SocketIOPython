# SocketIOPython
 Application built with Python using the SocketIO architecture. 
This is a simple application with **SOAP** architecture developed in **Python** using the **Flask**. 
## Features

- Flask Framework**: Handles HTTP routes and renders an HTML template.
- Flask-SocketIO**: Enables real-time communication with WebSocket.
- WebSocket Connection**: When connecting, the server sends a “Hello World!” message to the client.

## Prerequisites

Before you begin, make sure you have the following installed:

- **Python 3.8 or higher**.  
  Download it from [python.org](https://www.python.org/).
- **pip** (Python package manager)
  
## Steps to Download and Run the Project

1. **Clone the Repository**.  
   Clone this repository on your local machine using the command:
   ```bash
   git clone https://github.com/EnContacto/SocketIOPython.git
   cd SocketIOPython
2. **Install Dependencies**.
   This project uses Flask and Flask-SocketIO. Install them with:
   `pip install flask flask-socketio`
   
3. **Run aplication**
   Execute the main file:
   
   `python app.py`
   

## Project Structure.
   The project has the following basic structure:
   ```bash
📁 project-websocket
 ┣ 📄 app.py # main code of the application
 ┣ 📄 templates
 ┃ ┗ 📄 index.html # HTML template rendered by Flask
 ┗ 📄 README.md # Project Documentation
