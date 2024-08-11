import random

def monty_hall(change, num_trials):
    win_count = 0

    for _ in range(num_trials):
        prize_door = random.randint(1, 3)
        player_choice = random.randint(1, 3)
        remaining_doors = [door for door in [1, 2, 3] if door != player_choice and door != prize_door]
        monty_opens = random.choice(remaining_doors)
        if change:
            player_choice = [door for door in [1, 2, 3] if door != player_choice and door != monty_opens][0]
        if player_choice == prize_door:
            win_count += 1

    return win_count / num_trials

if __name__ == "__main__":
  num_trials = 1000
  win_rate_stay = monty_hall(True, num_trials)
  win_rate_change = monty_hall(False, num_trials)

