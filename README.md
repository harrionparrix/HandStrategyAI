# Hand Strategy AI Contest

This project allows you to create your own RPS bots, compete against other bots, and see how your bots rank against the competition. 

## Project Structure

- **`fight.py`**: This script runs matches between your bot and all the other bots in the competition.
- **`bots.py`**: Contains the implementation of all the bots that participate in the contest.
- **`contest.py`**: The main file where you can add the code for your bots. This is where you define the strategies your bots will use.
- **`ranking.py`**: Runs the contest between all bots and ranks them based on their performance.

## Getting Started

### 1. Creating Your Bots

- **Step 1**: Open `contest.py`.
- **Step 2**: Define up to **5 bots** with unique strategies.
  - You can create simple or complex bots using any approach you like.
  - **Rule**: Out of the 5 bots, only **2 bots** can be designed to selectively code against specific enemy bots (i.e., a bot that alters its strategy based on the opponent).
- **Step 3**: Save your changes, make sure you add a comment with your name beside your bot.

### Example Bot Implementation in `contest.py`:
```python
def my_first_bot(prev_opponent_play, my_history=[]):
    # Simple bot that always plays Rock
    return 'R'

def my_second_bot(prev_opponent_play, my_history=[]):
    # Complex bot that analyzes opponent's moves and adapts
    my_history.append(prev_opponent_play)
    if len(my_history) > 5:
        return 'P'
    return 'S'
```
### Contest Rules

1. **Bot Submission**:
   - You can submit up to **5 bots**.
   - Out of these, upto **2 bots** are allowed to have a strategy that selectively codes against specific opponent bots.

2. **Bot Complexity**:
   - Bots can range from simple (e.g., always playing Rock) to very complex (e.g., machine learning-based strategies).
   - The complexity of your bots is up to you, but the average score wins. This means that creating a balanced bot with consistent performance may be more effective than a highly specialized bot.

3. **Selective Coding**:
   - If you choose to create a selective bot, make sure it only targets specific opponent bots. All other player bots must have generalized strategies.

4. **Scoring**:
   - Each bot will be matched against every other bot, and the win rates will be recorded.
   - The **average win rate** across all matches will determine the ranking.
5. **Naming**:
   - Names should be awesome. Show your creativity !


