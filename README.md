## WordTree [![Tests](https://github.com/OhDxni/WordTree/actions/workflows/tests.yml/badge.svg)](https://github.com/OhDxni/WordTree/actions/workflows/tests.yml)
---
## Table of Contents
1. [Description](#description)  
2. [How It Works](#how-it-works)  
3. [Visuals](#visuals)  
4. [Installation and Requirements](#installation-and-requirements)  
5. [Usage](#usage)  
6. [Support](#support)  
7. [Roadmap](#roadmap)  
8. [Authors](#authors) 

---

## Description
**WordTree** is a word-based puzzle game inspired by the online game [Weaver](https://wordwormdormdork.com/). It challenges players to engage in creative and strategic thinking by transforming a starting word into a goal word, one letter at a time.
The game is designed with a user-friendly interface that allows for an easy navigation from the start, through login, to the game console and the game itself. Player can also select the difficulty of the game by choosing the length of the words (4, 5, or 6 letter words).  
The user can read the rules of the game before starting to play. Moreover, in case of any uncertainties the user can also go through a demo play. When the user gets to the end of the game, a leaderboard is displayed that shows statistics about the game and the shortest path they could have taken to win.

### Key features include:
- A user-friendly interface.
- Difficulty selection based on word length (4, 5, or 6 letters).
- Instructions and demo play for beginners.
- A leaderboard showcasing player statistics.

---

## How It Works
- Players start with a given starting word and a goal word, both of equal length.
- At each step, players can change only one letter in the current word, ensuring the new word is a valid dictionary entry.
- The game provides all possible word options at every stage, allowing players to plan the most efficient path to reach the goal word.

---

## Visuals
Below are two screenshots displaying some different parts of the user interface from our game.
1. **Main Page of the Game:**
   The first screenshot displays the **main page** of the game. From here players can choose different **game modes**, view     the **instructions**, and get familiar with the game  through a **demo** play.
2. **In-Game Moment (4-Letter Words):**
   The second screenshot shows the **game screen**, which is the interface players interact with while playing the game. This screen remains consistent regardless of the selected game mode.
   
<img src="https://i.imgur.com/wtv3ByL.jpeg" alt="tree" width="450"/>
<img src="https://i.imgur.com/5elELTL.jpeg" alt="tree" width="450"/>

---

## Installation and Requirements
To run the project, you can use any Python editor of your choice, such as **VSCode** or **PyCharm**. Below are two options to run the game.

### Option 1: Open the Project as a ZIP File
1. **Download the ZIP File**
   - Visit the GitHub repository:   
     `https://github.com/OhDxni/WordTree`
   - Click the **Code** button and select **Download ZIP**.

2. **Extract the ZIP File**
   - Extract the contents to a folder on your system.

3. **Open in Your IDE**
   - Open **PyCharm** or **VSCode**.
   - Use the **File > Open Folder** option and navigate to the extracted folder.

4. **Install Dependencies**
   - Open the terminal in your IDE and run the following commands:
     ```bash
     pip install customtkinter
     pip install pygame
     pip install -r dev-requirements.txt
     ```

5. **Run the Game**
   - Navigate to the `Project_Code` directory.
   - Open `main.py` and run the file using your IDE.



### Option 2: Clone the Project Using VCS
1. **Clone the Repository Using Your IDE's VCS Tool**
   - **PyCharm**:
     1. Go to **File > New Project > Get from Version Control**.
     2. Paste the repository URL:  
     `https://github.com/OhDxni/WordTree`
     3. Click **Clone**.
   - **VSCode**:
     1. Go to **View > Command Palette** (`Ctrl+Shift+P`).
     2. Search for **Git: Clone**.
     3. Paste the repository URL:  
     `https://github.com/OhDxni/WordTree`

     4. Select a folder to save the project.

2. **Install Dependencies**
   - Open the terminal in your IDE and run the following commands:
     ```bash
     pip install customtkinter
     pip install pygame
     pip install -r dev-requirements.txt
     ```

3. **Run the Game**
   - Navigate to the `Project_Code` directory.
   - Open `main.py` and run the file using your IDE.


### NB!
If you encounter any issues, please ensure that all necessary dependencies are installed as mentioned in the installation steps above. Double-check the installation steps and confirm that your eniorment is set up correctly.

---

## Usage
Below is a link to a simplified example of our gameplay
<br/>https://game-demo-for-readme.tiiny.site

---

## Support
In case of any problems or questions feel free to contact any of our group members via university email.

---

## Roadmap
In the future, the project could be released online and become available to the public. That would allow for the leaderboard to be accurate because it would be updated after every user plates the game. Additionally, more improvements could be made to make the game more enjoyable and easier to play. These could include adding hints to the game, showing history of the chosen words during the game as well as displaying definitions of words when their button is hovered over.

---

## Authors
Ewelina Kowalczyk: e.a.kowalczyk@umail.leidenuniv.nl
<br/>Talya Seryano: t.seryano@umail.leidenuniv.nl
<br/>Dani Jonas: d.jonas.2@umail.leidenuniv.nl
<br/>Hazel Buckley Mc Mahon: h.m.buckley.mc.mahon@umail.leidenuniv.nl
<br/>Djamey Hermelijn: d.n.t.hermelijn@umail.leidenuniv.nl
<br/>Mariela Pluutus: m.pluutus@umail.leidenuniv.nl
---
