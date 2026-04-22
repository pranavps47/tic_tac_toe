# GEMINI.md

## Project Overview
**Tic-Tac-Toe Pro** is a modern, responsive web application for playing Tic-Tac-Toe. It features a Flask backend and a sleek, glassmorphic frontend. The game supports three modes:
- **2 Players (PvP):** Local multiplayer on the same device.
- **Easy AI:** The computer makes random moves.
- **Hard AI:** The computer uses the **Minimax algorithm** to ensure it never loses.

### Core Technologies
- **Backend:** Python, Flask
- **Frontend:** HTML5, Vanilla JavaScript, CSS3 (Modern features like `backdrop-filter` and CSS Grid)
- **Deployment:** Gunicorn (Optimized for platforms like Render.com)

## Project Structure
- `app.py`: The main entry point. Contains the Flask application, game logic (win checking), and the Minimax AI implementation.
- `requirements.txt`: Lists Python dependencies (`flask`, `gunicorn`).
- `templates/index.html`: The frontend layout and client-side game logic.
- `static/style.css`: Modern, dark-themed styling for the application.
- `README.md`: Contains deployment links and basic information.

## Building and Running

### Local Development
1. **Create and activate a virtual environment:**
   ```bash
   python -m venv .venv
   # On Windows:
   .venv\Scripts\activate
   # On macOS/Linux:
   source .venv/bin/activate
   ```
2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
3. **Run the application:**
   ```bash
   python app.py
   ```
   The app will be available at `http://localhost:5000`.

### Production
The project is configured for production using Gunicorn:
```bash
gunicorn app:app
```

## Development Conventions

### Code Style
- **Python:** Follows standard PEP 8 conventions. Game logic is encapsulated in pure functions (`check_winner`, `minimax`) within `app.py`.
- **JavaScript:** Uses modern `async/await` for API calls and clear separation of UI updates (`updateUI`) and game state management.
- **CSS:** Utilizes a mobile-first approach with responsive units and modern aesthetic patterns (glassmorphism, gradients).

### Testing
- Currently, there are no automated tests. Logic verification is done manually through the web UI. 
- *TODO:* Consider adding unit tests for the `minimax` and `check_winner` functions in `app.py`.

### Architecture
- The frontend maintains the board state for PvP mode.
- For AI modes, the frontend sends the current board state to the `/move` endpoint, and the backend returns the optimal move.
- The UI uses CSS animations (`pop` class) and transitions for a polished user experience.
