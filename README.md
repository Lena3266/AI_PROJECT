# HMS-AI — Full Stack (Local Docker)

## Prerequisites
- Docker & Docker Compose installed
- (Optional) Node 18+ and Python 3.11+ for local runs without Docker

## Quick start (Docker Compose)

1. Copy the repository to your machine.
2. Rename `backend/.env.example` to `backend/.env` and set values if needed.
3. From project root:
   ```bash
   docker compose up --build
4.	Services:
o	Frontend: http://localhost:3000
o	Backend API: http://localhost:4000
o	AI service: http://localhost:5000
Running without Docker (development)
•	Backend: cd backend && npm install && npm run dev
•	AI service: cd ai-service && pip install -r requirements.txt && python app.py
•	Frontend: cd frontend && npm install && npm run dev

