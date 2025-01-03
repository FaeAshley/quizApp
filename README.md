# quizApp

# Quiz App

This **Quiz App** is a Python-based console application that lets users test their knowledge with a **State Trivia Quiz** and offers a placeholder for a future **Personality Quiz**. The app calculates a score for the trivia quiz and provides users with options to replay or exit.

---

## Features

### 1. **State Trivia Quiz**
- A 3-question quiz about U.S. states:
  1. Which state has the largest population?
  2. Which state has the smallest population?
  3. Which state is the furthest south?
- Tracks correct answers and calculates a percentage score.
- Includes user-friendly feedback for correct and incorrect answers.

### 2. **Personality Quiz (In Progress)**
- Displays a placeholder message indicating future implementation.

### 3. **Main Menu**
- Allows users to:
  - Start the State Trivia Quiz.
  - Check out the placeholder for the Personality Quiz.
  - Exit the app gracefully.

---

## How It Works
1. **Start the App**:
   - Launch the program, and the main menu is displayed.

2. **Navigate Through Menus**:
   - Select an option from the main menu to start a quiz or exit the app.

3. **State Trivia Quiz**:
   - Answer 3 multiple-choice questions.
   - Get feedback for each question and see your final score as a percentage.
   - Return to the main menu or exit the app after the quiz.

4. **Personality Quiz**:
   - Currently under development.
   - Displays a "work in progress" message.

5. **Exit**:
   - Choose "Exit" to terminate the app.

---

## Requirements
- **Python 3.x**

---

## How to Run
1. Save the script to a file (e.g., `quiz_app.py`).
2. Run the script in your terminal or IDE:
   ```bash
   python quiz_app.py
   ```

---

## Code Overview

### `trivia_quiz()`
- **Handles the State Trivia Quiz**.
- Asks 3 questions and checks the user’s answers.
- Tracks the number of correct answers and calculates a percentage score.
- Includes an option to return to the main menu or exit the app.

### `personality_quiz()`
- Placeholder for a future quiz.
- Redirects users back to the main menu.

### `main_menu()`
- Displays the main menu and allows users to select a quiz or exit the app.
- Calls the appropriate quiz function based on user input.

### `main()`
- Entry point of the program that starts the main menu loop.

---

## Example Interaction
### Main Menu:
```plaintext
Quiz App
1. State Trivia Quiz
2. Personality Quiz
3. Exit
Select a quiz! 1
```

### State Trivia Quiz:
```plaintext
Which state has the largest population? california
Correct!

Which state has the smallest population? wyoming
Correct!

Which state is the furthest south? alaska
Incorrect

Score: 66.67%

1. Yes
2. Exit
Return to main menu? 2
Goodbye!
```

---

## Potential Enhancements
- Complete the **Personality Quiz** with meaningful questions and results.
- Add more questions and categories to the trivia quiz.
- Include a leaderboard to track high scores.
- Save quiz results to a file for later review.

---

## License
This project is open-source and available for personal or educational use.

---

Enjoy quizzing! 🐾

