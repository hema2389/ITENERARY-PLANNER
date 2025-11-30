# Intent-Driven Anti-Overtourism Planning Agent

This project is an AI-powered travel planning agent that helps users create itineraries that avoid crowds and promote sustainable tourism. It uses a conversational interface to understand user intent and preferences, and then generates personalized travel plans that prioritize off-peak timing, lesser-known destinations, and authentic local experiences.

## Architecture

The application is built with a modern web stack:

*   **Frontend:** React.js with Vite and Tailwind CSS
*   **Backend:** Flask (Python)
*   **AI/Agent Framework:** LangChain
*   **Database:** Firebase Firestore
*   **Authentication:** Firebase Auth

### Architecture Diagram

(Coming Soon)

## API Endpoints

(Coming Soon)

## Setup Instructions

### Prerequisites

*   Node.js and npm
*   Python 3.9+ and pip
*   Firebase project with Auth and Firestore enabled

### Frontend

1.  Navigate to the `frontend` directory: `cd frontend`
2.  Install dependencies: `npm install`
3.  Run the development server: `npm run dev`

### Backend

1.  Navigate to the `backend` directory: `cd backend`
2.  Create a virtual environment: `python -m venv venv`
3.  Activate the virtual environment: `source venv/bin/activate` (Linux/macOS) or `venv\Scripts\activate` (Windows)
4.  Install dependencies: `pip install -r requirements.txt`
5.  Create a `.env` file from the example: `cp .env.example .env`
6.  Populate `.env` with your API keys.
7.  Run the development server: `python app.py`
