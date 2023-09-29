team_A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
team_B = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
card = input().split(" ")
terminated_game = False
for player in card:
    player_to_remove = player.split("-")
    if (int(player_to_remove[1]) not in team_A and player_to_remove[0] == "A") or \
            (int(player_to_remove[1]) not in team_B and player_to_remove[0] == "B"):
        continue
    if player_to_remove[0] == "A":
        team_A.remove(int(player_to_remove[1]))
    elif player_to_remove[0] == "B":
        team_B.remove(int(player_to_remove[1]))
    if len(team_A) < 7 or len(team_B) < 7:
        terminated_game = True
        break
print(f"Team A - {len(team_A)}; Team B - {len(team_B)}")
if terminated_game:
    print("Game was terminated")
# this solution is working but is a bit impractical there is another way to do this