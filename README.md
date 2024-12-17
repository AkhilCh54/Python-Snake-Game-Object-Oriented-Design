# Python Snake Game: Object-Oriented Design


## **Project Overview**
This project is a fully functional version of the Snake game, designed to showcase OOP concepts such as encapsulation, abstraction, and modular design. It features a clean separation of responsibilities across four main files:

1. **`main.py`**: Acts as the central controller, bringing together all components of the game and managing the game loop.
2. **`snake.py`**: Defines the Snake class, handling its creation, movement, and growth mechanics.
3. **`food.py`**: Manages the creation of food items at random locations on the game map. When the snake eats a piece of food, a new one is randomly generated.
4. **`scoreboard.py`**: Tracks and displays the player's score, updating it as the snake eats food.

---

## **Key Features**
- **Object-Oriented Design**: The project demonstrates strong OOP practices, making the code modular, reusable, and easy to maintain.
- **Dynamic Gameplay**: The snake grows as it eats food, and the player's score increases accordingly.
- **Randomized Food Placement**: Each time food is consumed, a new food item appears at a random location.
- **Score Tracking**: A scoreboard displays the current score, which updates in real time.

---

## **How to Run**
To run this game, you need to have Python installed on your system.

1. Clone this repository to your local machine:
   ```bash
   git clone https://github.com/AkhilCh54/Python-Snake-Game-Object-Oriented-Design.git
   ```

2. Navigate to the project directory:
   ```bash
   cd Python-Snake-Game-Object-Oriented-Design
   ```

3. Run the game:
   ```bash
   python main.py
   ```

---

## **Gameplay Instructions**
1. Use the arrow keys to control the movement of the snake.
2. Eat the food to grow longer and increase your score.
3. Avoid running into the walls or the snake's own body, or it's game over!

---

## **Technologies Used**
- **Programming Language**: Python
- **Concepts**: Object-Oriented Programming (OOP), Modular Design, Randomization, Event Handling

---

## **Possible Improvements**
- **Add Levels/Difficulty**: Increase the snake's speed as the score increases.
- **Enhance Graphics**: Use a graphical library like `pygame` for improved visuals and animations.
- **Save High Score**: Implement a feature to save the highest score across sessions.

