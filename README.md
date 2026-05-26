# 🎯 GuessFlow: Terminal-Based Intelligent Number Guessing System

<p align="center">
  <b>A structured command-line number guessing game with persistent JSON-based leaderboard tracking, performance timing, and dynamic session management.</b><br>
  Designed as a lightweight interactive CLI application engineered for gameplay logic control, state persistence, and real-time user feedback.
</p>

---

<h2>📘 Project Overview</h2>

<p>
<b>GuessFlow</b> is an interactive terminal-based number guessing game developed in Python as part of the <b><a href="https://roadmap.sh/projects/number-guessing-game" target="_blank">Number Guessing Game</a></b> challenge on <b>roadmap.sh</b>.
</p>

<p>
The application simulates a structured guessing environment where the system randomly selects a number and the player must deduce it within a defined attempt limit. The game integrates difficulty scaling, attempt tracking, performance timing, and persistent leaderboard storage using a local JSON datastore.
</p>

<p>
Unlike basic CLI guessing games, GuessFlow introduces a structured persistence layer and modular gameplay loop designed to reinforce core Python concepts including file handling, control flow logic, error handling, and data serialisation.
</p>

---

<h2>🎮 Gameplay Experience & User Journey</h2>

<p>
GuessFlow is designed to feel like a structured, session-based terminal game rather than a simple script-based guessing exercise.
</p>

<p>
When the application starts, the user is guided through a controlled gameplay flow that ensures clarity, pacing, and engagement from start to finish.
</p>

<h3>🧭 How the Game Works</h3>

<ol>
  <li>
    The player is prompted to enter a username, which is used for leaderboard tracking.
  </li>

  <li>
    The system randomly generates a secret number within a fixed range (1–10 in the current implementation).
  </li>

  <li>
    The player selects a difficulty level which determines how many attempts they are allowed:
    <ul>
      <li>Easy → 10 attempts</li>
      <li>Medium → 5 attempts</li>
      <li>Hard → 3 attempts</li>
    </ul>
  </li>

  <li>
    The game loop begins and the player repeatedly enters guesses via the terminal.
  </li>

  <li>
    After each guess, the system provides real-time feedback:
    <ul>
      <li><b>“Go higher!”</b> if the guess is too low</li>
      <li><b>“Go lower!”</b> if the guess is too high</li>
    </ul>
  </li>

  <li>
    The session ends when either:
    <ul>
      <li>The correct number is guessed (win condition)</li>
      <li>All attempts are exhausted (loss condition)</li>
    </ul>
  </li>

  <li>
    On completion, the system records:
    <ul>
      <li>Username</li>
      <li>Attempts used</li>
      <li>Time taken (rounded to 1 decimal place)</li>
      <li>Win status</li>
    </ul>
  </li>

  <li>
    The result is then stored in a persistent JSON leaderboard for future comparison.
  </li>
</ol>

---

<h2>🆚 What Changed From the Previous Version</h2>

<p>
This version of GuessFlow significantly improves both the <b>technical architecture</b> and the <b>player experience flow</b> compared to the earlier CSV-based implementation.
</p>

<h3>🎯 Player Experience Improvements</h3>

<ul>
  <li>
    The game now includes a structured countdown sequence, improving pacing and anticipation before gameplay begins.
  </li>

  <li>
    Difficulty selection is more meaningful, directly affecting gameplay challenge through attempt limits.
  </li>

  <li>
    Input validation prevents crashes caused by invalid user input, making the experience more stable and user-friendly.
  </li>

  <li>
    Game feedback is immediate and consistent, improving clarity during each guessing round.
  </li>
</ul>

<h3>⚙️ Technical Improvements</h3>

<ul>
  <li>
    Migration from CSV to JSON eliminates data corruption issues and improves structured data handling.
  </li>

  <li>
    File handling is now safe and consistent, preventing overwrites of existing leaderboard data.
  </li>

  <li>
    Attempt tracking is more accurate and separated from win-state logic.
  </li>

  <li>
    Time tracking is now rounded and standardised for leaderboard consistency.
  </li>

  <li>
    Game state transitions are explicitly controlled using boolean flags, improving reliability of win/loss detection.
  </li>
</ul>

---

<h2>📊 Overall Experience Summary</h2>

<p>
Compared to the earlier version, GuessFlow is not just a functional upgrade — it is a structural redesign of how the game behaves from a user perspective.
</p>

<p>
Instead of being a simple loop-based script, it now behaves like a controlled game session with:
</p>

<ul>
  <li>Predictable flow</li>
  <li>Clear rules and difficulty scaling</li>
  <li>Persistent performance tracking</li>
  <li>Stable input handling</li>
</ul>

<h2>🧠 Architectural Philosophy & Design Intent</h2>

<p>
GuessFlow was designed around a <b>session-driven CLI architecture</b>, where each gameplay session is treated as an isolated runtime event with persistent outcome recording.
</p>

<p>
The system prioritises simplicity of execution while maintaining structured internal state tracking. Every decision within the architecture was made to reinforce foundational Python programming principles:
</p>

<ol>
  <li>
    <b>State Management via Local Persistence:</b><br>
    All scores are stored in a structured JSON file rather than ephemeral memory, ensuring long-term retention of gameplay history and leaderboard continuity.
  </li>

  <li>
    <b>Deterministic Game Loop Design:</b><br>
    The guessing loop is engineered to maintain strict termination conditions based on either success (correct guess) or failure (attempt exhaustion), ensuring predictable execution flow.
  </li>

  <li>
    <b>Difficulty-Based Dynamic Scaling:</b><br>
    The system modifies available attempts based on selected difficulty, introducing controlled complexity progression.
  </li>

  <li>
    <b>Time-Based Performance Tracking:</b><br>
    Each session records completion time using high-resolution timing functions, enabling performance comparison across sessions.
  </li>
</ol>

---

<h2>⚡ Core Features & Project Enhancements</h2>

<p>
This version of GuessFlow represents a significant evolution over earlier CSV-based implementations by introducing structured JSON persistence, improved input validation, and cleaner gameplay state handling.
</p>

| Capability          | Previous Version (CSV Prototype) | GuessFlow Implementation                                            |
| ------------------- | -------------------------------- | ------------------------------------------------------------------- |
| Data Storage        | CSV overwrite / append issues    | Structured JSON persistence with safe load/save lifecycle           |
| Game State Handling | Basic loop logic                 | Controlled win/loss state tracking with explicit boolean flags      |
| Input Validation    | Minimal handling                 | Try/except based validation preventing runtime crashes              |
| Timing System       | Raw float seconds                | Rounded time tracking with improved display formatting              |
| Difficulty System   | Fixed attempt logic only         | Structured scaling system (Easy / Medium / Hard)                    |
| Persistence Safety  | File overwrite risk              | Controlled file write operations with consistent schema enforcement |
| User Experience     | Linear CLI flow                  | Countdown sequence, screen clearing, and structured session flow    |

---

<h2>🧩 Folder Structure</h2>

<pre>
GuessFlow/
│
├── number-guessing-game.py   # Main game engine and CLI logic
├── score_board.json          # Persistent leaderboard datastore
└── README.md                 # Project documentation
</pre>

---

<h2>🚀 How to Run</h2>

<ol>
  <li>Ensure you have <b>Python 3.8 or above</b> installed locally.</li>

  <li>Clone or download this repository:
    <pre>git clone https://github.com/your-username/GuessFlow.git</pre>
  </li>

  <li>Navigate into the project directory:
    <pre>cd GuessFlow</pre>
  </li>

  <li>No external dependencies are required — the project uses only Python standard libraries.</li>

  <li>Run the game using:
    <pre>python number-guessing-game.py</pre>
  </li>
</ol>

---

<h2>🖥️ Gameplay Instructions</h2>

<ol>
  <li>Launch the program via terminal.</li>
  <li>Enter a username when prompted.</li>
  <li>Select a difficulty level:
    <ul>
      <li>Easy – 10 attempts</li>
      <li>Medium – 5 attempts</li>
      <li>Hard – 3 attempts</li>
    </ul>
  </li>
  <li>Guess the randomly generated number between 1 and 10.</li>
  <li>The system will provide feedback after each guess until the correct number is found or attempts are exhausted.</li>
</ol>

---

<h2>⚙️ Code Architecture & Function Breakdown</h2>

<p>
The application is structured into modular functional blocks responsible for UI handling, game logic execution, timing control, and persistent storage management.
</p>

---

<h3>System Utilities</h3>

<ul>
  <li>
    <code>clear_screen()</code>:  
    Handles OS-aware terminal clearing for improved UI readability.
  </li>

  <li>
    <code>time.sleep()</code>:  
    Used to create structured pacing between game states and improve user experience flow.
  </li>
</ul>

---

<h3>Persistence Layer</h3>

<ul>
  <li>
    <code>load_data()</code>:  
    Loads leaderboard data from JSON file or initialises a new structured datastore if none exists.
  </li>

  <li>
    <code>save_data()</code>:  
    Writes structured leaderboard data back to persistent JSON storage ensuring data consistency.
  </li>
</ul>

---

<h3>Game Engine</h3>

<ul>
  <li>
    <code>main_game()</code>:  
    Core gameplay loop responsible for number generation, input handling, attempt tracking, and win/loss resolution.
  </li>

  <li>
    <code>difficulty modes</code>:  
    Controls attempt allocation dynamically based on selected difficulty level.
  </li>
</ul>

---

<h3>Performance Tracking</h3>

<ul>
  <li>
    <code>start_timer()</code> & <code>stop_timer()</code>:  
    Measures session duration from game start to completion.
  </li>

  <li>
    Time values are stored in rounded seconds for leaderboard consistency.
  </li>
</ul>

---

<h2>📂 Data Architecture</h2>

<p>
All leaderboard entries are stored inside <code>score_board.json</code> using a structured format:
</p>

<pre>
{
  "scores": [
    {
      "username": "HUSSAIN",
      "attempts": 3,
      "time": 4.2,
      "won?": true
    }
  ]
}
</pre>

---

<h2>🧪 Improvements Over Previous Version</h2>

<p>
This implementation is a direct evolution of an earlier CSV-based guessing game prototype.
</p>

<p>
Key improvements include:
</p>

<ul>
  <li>Migration from CSV to structured JSON persistence for safer data handling</li>
  <li>Fixed file overwrite and corruption issues present in earlier save logic</li>
  <li>Improved attempt tracking with accurate decrement logic</li>
  <li>Enhanced exception handling for invalid user input</li>
  <li>More stable game loop termination conditions</li>
  <li>Cleaner modular structure with separation of concerns</li>
</ul>

---

<h2>📌 Roadmap.sh Submission Context</h2>

<p>
This project was developed as part of the <b>roadmap.sh Python backend learning track</b>, specifically the <b>Number Guessing Game</b> challenge.
</p>

<p>
The objective of this implementation was to move beyond a basic CLI script and demonstrate structured application design, persistent state handling, and improved user interaction flow within a terminal environment.
</p>

---

<h2>🧰 Requirements & Dependencies</h2>

<ul>
  <li><b>Python Runtime:</b> 3.8+</li>
  <li><b>Standard Libraries Only:</b> os, time, random, json, sys</li>
  <li>No external dependencies required</li>
</ul>

---

<h2>📄 Licence</h2>

<p>
This project is licensed under the <b>MIT Licence</b>.
</p>

<pre>
MIT Licence

Copyright (c) 2026 Sheikh Hussain

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
</pre>

---

## Footnote

<div align="center" style="border: 1px solid green; padding: 10px; border-radius: 5px;">
  <p>🗣️ Feel free to follow, connect, and chat!</p>
  <a class="header-badge" target="_blank" href="https://github.com/your-username"><img src="https://img.shields.io/badge/GitHub-376e00?style=flat&logo=github&logoColor=white" alt="GitHub"></a>
  <a class="header-badge" target="_blank" href="https://www.linkedin.com"><img src="https://img.shields.io/badge/LinkedIn-376e00?style=flat&logo=LinkedIn&logoColor=white" alt="LinkedIn"></a>
  <a class="header-badge" target="_blank" href="mailto:your@email.com"><img src="https://img.shields.io/badge/Gmail-376e00?style=flat&logo=gmail&logoColor=white" alt="Gmail"></a>
</div>

<div align="center">
  <a href="#" target="_blank">By Sheikh Muhammed Ajmer Hussain 💚</a>  
</div>

---

<h2 align="center">⭐ If you like this project, please give it a star on GitHub!</h2>
