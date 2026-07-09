# Transaction Description Categoriser

A Python-based Command-Line Interface (CLI) application that takes raw, messy bank transaction descriptions and automatically predicts their spending category. This project solves a real-world data problem by standardizing and classifying text into clean budget categories.

## 📌 Project Goals & Functionality
* **Data Cleaning:** Handles human error, varied casing, and messy spacing by preprocessing inputs.
* **Accurate Classification:** Maps transactions to explicit categories: `Food`, `Transport`, `Entertainment`, `Shopping`, `Bills`, `Income`, or `Other`.
* **Crash-Free UI:** Built with a robust, two-option CLI menu that validates user inputs to ensure stable execution.

---

## 🛠️ Requirements & Tech Stack
* **Language:** Python 3.x
* **Libraries Used:** Built using standard Python built-in features (no external dependencies required for the base version).
* *Planned Extensions:* `csv` for file handling, `pandas` and `scikit-learn` for future machine learning integration.

---

## 🚀 How to Run the Application

1. Make sure you have Python installed on your system.
2. Open your terminal or command prompt and navigate to the project directory.
3. Run the following command:
   ```bash
   python main.py
