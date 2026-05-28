# 🎯 CipherGuess: CSV-Powered CLI Number Guessing Game

<p align="center">
  <b>A terminal-based number guessing game engineered in Python.</b><br>
  Focused on persistence handling, CSV data management, and structured CLI application flow.
</p>

---

## 📘 Project Overview

**CipherGuess** is a command-line number guessing game developed in Python as part of the [Number Guessing Game](https://roadmap.sh/projects/number-guessing-game) project on roadmap.sh.

The original version of this project was built using JSON storage and focused mainly on gameplay logic. This rewritten version was specifically created to improve understanding of CSV persistence, file handling, and data management inside Python applications.

The goal of this rewrite was not simply to recreate the game, but to better understand:

- CSV file reading and writing
- File persistence workflows
- Data mutation in memory
- Serialisation and deserialisation
- Record management
- CLI application structure
- Differences between JSON and CSV storage systems

One of the biggest learning objectives was understanding how CSV persistence differs from JSON persistence.

JSON storage feels very natural in Python because dictionaries and lists map directly to JSON objects:

```python
[
  {
    "username": "Sheikh",
    "time": 12.4
  }
]
```

CSV storage, however, requires manual schema management and full file rewrites whenever records are modified.

This project became a practical exercise in learning how lower-level persistence systems work before eventually progressing towards SQLite and proper databases.

---

## 🔄 Evolution: Old Version vs New Version

This repository represents a major rewrite of the original number guessing game.

The earlier version focused primarily on gameplay and JSON handling, whereas the rewritten version focuses much more heavily on architecture, persistence management, CSV workflows, and cleaner application structure.

| Feature           | Old Version (JSON Edition)                         | New Version (CipherGuess)                                       |
| ----------------- | -------------------------------------------------- | --------------------------------------------------------------- |
| Persistence Layer | JSON storage using `json.load()` and `json.dump()` | CSV persistence using `csv.DictReader()` and `csv.DictWriter()` |
| Data Updates      | Direct object mutation                             | Manual row-based persistence rewriting                          |
| Difficulty Modes  | Single gameplay structure                          | Multiple difficulty levels                                      |
| Terminal Styling  | Basic print statements                             | Enhanced CLI formatting using `rich`                            |
| Score Handling    | Always appended scores                             | Username matching and record updating                           |
| Learning Focus    | Gameplay logic                                     | Persistence architecture and CSV workflows                      |
| AI Usage          | Large portions AI-assisted                         | Much more independently structured and reasoned                 |

---

## 🧠 Learning Journey

One of the main challenges during development was understanding why JSON persistence feels significantly easier to work with compared to CSV persistence.

With JSON, the workflow is extremely straightforward:

```python
load data → modify object → save object
```

CSV persistence behaves differently because rows cannot simply be modified directly inside the file.

Through building this project, the persistence workflow gradually evolved into:

```python
Read CSV → Convert rows into dictionaries → Modify records in memory → Rewrite CSV
```

A large part of the development process involved learning:

- Why append mode cannot update rows
- Why CSV updates require full rewrites
- How file modes (`r`, `w`, `a`) behave
- How in-memory Python objects differ from persistence layers
- Why databases exist to solve these problems

The original version of this project relied heavily on AI assistance while learning Python fundamentals.

This rewritten version intentionally focused much more heavily on independently restructuring logic, debugging persistence issues manually, understanding why the code works, and improving overall application architecture.

---

## 🧩 Folder Structure

```text
CipherGuess/
│
├── main.py             # Main game logic
├── scores.csv          # Auto-generated persistence file
├── README.md           # Project documentation
```

---

## 🚀 How to Run

1. Ensure Python 3.8 or above is installed.

2. Clone the repository:

```bash
git clone https://github.com/Sheikh-H/CipherGuess.git
```

3. Navigate into the project directory:

```bash
cd CipherGuess
```

4. Install dependencies:

```bash
pip install rich
```

5. Run the application:

```bash
python main.py
```

---

## 🎮 Gameplay Features

- Random number generation
- Difficulty selection
- Attempt tracking
- Timer tracking
- CSV score persistence
- Username-based score updating
- Rich CLI formatting
- Win/loss tracking
- Cross-platform terminal clearing

---

## ⚙️ Code Architecture

### Persistence Layer

#### `save_data(data)`

This function acts as the entire persistence engine for the application.

Responsibilities include:

- Creating the CSV file if it does not exist
- Writing headers automatically
- Loading current records into memory
- Searching for username matches
- Updating existing scores
- Appending new entries
- Rewriting the entire CSV file

This structure was intentionally designed to make CSV handling behave similarly to JSON persistence.

---

### Gameplay Engine

#### `main_game(mode)`

Handles:

- User interaction
- Attempt management
- Countdown timers
- Random number generation
- Time tracking
- Win/loss detection
- Score recording

---

### Difficulty Modes

| Mode   | Attempts |
| ------ | -------- |
| Easy   | 10       |
| Medium | 5        |
| Hard   | 3        |

---

## 📂 CSV Storage Architecture

The persistence layer stores data using a structured CSV schema:

```csv
username,attempts,time,won?
SHEIKH,3,12.4,True
ALEX,5,20.1,False
```

Unlike JSON, CSV does not naturally support nested structures or direct object mutation.

Because of this, the application manually:

1. Loads all rows into memory
2. Converts rows into dictionaries
3. Modifies the required records
4. Rewrites the entire file

This project was specifically built to better understand these persistence mechanics.

---

## 🧰 Requirements & Dependencies

### Python Runtime

- Python 3.8 or above

### External Dependencies

- `rich` — enhanced terminal formatting and coloured CLI output

### Standard Libraries Used

- `csv`
- `os`
- `time`
- `datetime`
- `random`
- `sys`

---

## 📄 Licence

<p>
  This project is licensed under the <b>MIT Licence</b> — see the <a href="./LICENCE">LICENCE</a> file for details.
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
  <a class="header-badge" target="_blank" href="https://github.com/Sheikh-H"><img src="https://img.shields.io/badge/GitHub-376e00?style=flat&logo=github&logoColor=white" alt="GitHub"></a>
  <a class="header-badge" target="_blank" href="https://www.linkedin.com/in/sheikh-hussain/"><img src="https://img.shields.io/badge/LinkedIn-376e00?style=flat&logo=LinkedIn&logoColor=white" alt="LinkedIn"></a>
  <a class="header-badge" target="_blank" href="mailto:sheikh.hussain1155@gmail.com"><img src="https://img.shields.io/badge/Gmail-376e00?style=flat&logo=gmail&logoColor=white" alt="Gmail"></a>
  <a class="header-badge" target="_blank" href="https://sheikh-h.github.io/"><img src="https://img.shields.io/badge/Portfolio-376e00?style=flat&logo=github&logoColor=white" alt="Portfolio"></a>
</div>

<div align="center">
  <a href="https://www.linkedin.com/in/sheikh-hussain/" target="_blank">By Sheikh Hussain 💚</a>
</div>

---

<h2 align="center">⭐ If you like this project, please give it a star on GitHub!</h2>
