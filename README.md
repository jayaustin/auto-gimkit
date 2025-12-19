# Auto-Gimkit Automation Bot

![Python](https://img.shields.io/badge/python-3.10%2B-blue)
![Platform](https://img.shields.io/badge/platform-Windows%20%7C%20macOS%20%7C%20Linux-lightgrey)
![Status](https://img.shields.io/badge/status-educational--use--only-orange)

A Python automation script designed to keep a Gimkit session active by simulating basic keyboard movement,  randomized input and basic question answering. This is designed to auto-farm Gimkit XP and collect the maximum number of weekly coins. The script includes a safety timer to ensure it shuts down automatically.

Gimkit awards XP based on "active play," which requires player movement and question answering.

> **⚠️ Important**
>
> This script functions as a **blind input automation tool**. It does **not** read the screen, parse questions, or determine correct answers.
>
> It is **strictly intended for use in Gimkit modes with trivial or non-impactful questions** (e.g., “1 + 1”) where incorrect answers are impossible or irrelevant to the game state.

---

## 📋 Features

- **AFK Movement**
  - Alternates holding the `A` and `D` keys in 5-second intervals to prevent idle kicks.

- **Randomized Activity**
  - Randomly presses the spacebar to add randomization to the minimal gameplay.

- **Automated Progression**
  - Executes a mouse click sequence answer simple questions and replinish game energy.

- **Built-In Safety Timer**
  - Automatically exits after **a configurable timer** to prevent runaway execution.

- **Fail-Safe Kill Switch**
  - Moving the mouse to the **top-left corner of the primary monitor** immediately terminates the script (PyAutoGUI fail-safe).

---

## 🚀 Installation & Setup (Using `uv`)

This project uses [`uv`](https://github.com/astral-sh/uv) for fast, reliable Python package and virtual environment management.

### 1. Install `uv`

If you don’t already have `uv` installed:

**macOS / Linux**
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

**Windows (PowerShell)**
```powershell
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"
```

---

### 2. Initialize the Project & Install Dependencies

Navigate to the directory containing `main.py`, then run:

```bash
# Initialize a new project (if not already initialized)
uv init

# Install required dependency
uv add pyautogui
```

---

### 3. Run the Script

Execute the script using `uv run` to ensure it runs inside the managed virtual environment:

```bash
uv run main.py
```

---

## ⚙️ Configuration

Open `main.py` in a text editor to customize the script for your setup.

### 🖥️ Multi-Monitor Configuration

If you run the script on a secondary monitor, screen offsets must be adjusted.

- **Primary / Main Monitor**
  ```python
  screenOffsetX = 0
  ```

- **Left-Side Monitor Example**
  ```python
  screenOffsetX = -1920 //This should be equal to your screen's horizontal resolution
  ```

Complete example:

```python
screenOffsetX = -1920  # Adjust based on monitor width
screenOffsetY = 0      # Adjust if monitors have different heights
```

---

### ⏱️ Timer Settings

Control how long the script runs before shutting down automatically:

```python
TOTAL_RUN_TIME_MINUTES = 57 //A safe limit for a max Gimkit session of 59 minutes
```

---

## ⚠️ Usage Tips & Best Practices

- **5-Second Focus Window**
  - After starting the script, you have 5 seconds to switch focus to the Gimkit browser window.

- **Emergency Stop**
  - If behavior becomes unexpected, move your mouse to the **top-left corner** of the primary screen to immediately stop execution.

- **Screen Resolution Matters**
  - Mouse click coordinates are hard-coded.
  - Changing screen resolution or resizing the browser window may cause misclicks.
  - For best results, use a maximized browser window at a consistent resolution.

---

## 📝 Disclaimer

This project is provided **for educational and experimentation purposes only**.

Automation tools may violate the Terms of Service of online platforms or games.  
You are responsible for understanding and complying with all applicable rules and policies.

Use responsibly (or don't, I'm a readme doc not the police).
