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
  - **Rule**: Out of the 5 bots, only **1 bot** can be designed to selectively code against specific enemy bots (i.e., a bot that alters its strategy based on the opponent).
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
   - Out of these, upto **1 bot** is allowed to have a strategy that selectively codes against **ONE** specific opponent bot.
   - Make your own file with your initials. Import and add it to **fight.py**, **ranking.py** and **main.py**.
2. **Bot Complexity**:
   - Bots can range from simple (e.g., always playing Rock) to very complex (e.g., machine learning-based strategies).
   - The complexity of your bots is up to you, but the average score wins. This means that creating a balanced bot with consistent performance may be more effective than a highly specialized bot.

3. **Selective Coding**:
   - If you choose to create a selective bot, make sure it only targets the one specific opponent bot. All other player bots must have generalized strategies. (Eg. Function One : if mimic_strategy => algo1 , else algo2)

4. **Scoring**:
   - Each bot will be matched against every other bot, and the win rates will be recorded.
   - The **average win rate** across all matches will determine the ranking.
5. **Naming**:
   - Names should be awesome. Show your creativity !


  # Simulation Results: Rock-Paper-Scissors Strategies

### CONTEST ENDS !

This simulation was run for over 2 hours, iterating through 3250 rounds of various Rock-Paper-Scissors strategies. The goal was to determine which strategy performed the best over a large number of iterations. The ranking shows the accumulated points for each strategy, with the highest score indicating the best-performing strategy.

### Results

### Results

| Rank | Strategy Name        | Points  |
|------|----------------------|---------|
| 1    | Maverick             | 214.0   |
| 2    | HyperBeam            | 193.0   |
| 3    | EldenRing            | 188.0   |
| 4    | SuperBaby            | 186.0   |
| 5    | casey_strategy       | 181.5   |
| 6    | taylor_strategy      | 180.0   |
| 7    | DragonDance          | 173.5   |
| 8    | as25_2               | 153.5   |
| 9    | nostradamus          | 149.0   |
| 10   | jordan_strategy      | 146.0   |
| 11   | as25_4               | 125.0   |
| 12   | as25_1               | 118.0   |
| 13   | as25_5               | 116.0   |
| 14   | random_strategy      | 115.5   |
| 15   | vladamir             | 115.0   |
| 16   | as25_3               | 104.5   |
| 17   | scissors_player      | 92.0    |
| 18   | magic_mike           | 89.0    |
| 19   | alex_strategy        | 83.0    |
| 20   | Avengers             | 82.5    |
| 21   | hikaru               | 81.5    |
| 22   | kyle_demanetrius     | 81.0    |
| 23   | paper_player         | 80.0    |
| 24   | mimic_strategy       | 75.5    |
| 25   | Ayanokoji            | 64.0    |
| 26   | rock_player          | 63.0    |


### Conclusion

The **Maverick** strategy emerged as the winner, accumulating a total of **214 points**. It outperformed the **HyperBeam** and **EldenRing** strategies, which took second and third place, respectively. Staregy by @harrionparrix is the winner !

From the results, we can conclude that not all strategies are equally effective in a simulated environment where a large number of iterations are involved. Some strategies consistently outperformed others, while some, like **rock_player**, ended up with significantly fewer points.

The simulation reveals that more complex or adaptive strategies tend to perform better in the long run, while simpler or static strategies, like **rock_player**, may fall behind. This could serve as a basis for further refinement and development of more sophisticated strategies in future simulations.

GLHF !

