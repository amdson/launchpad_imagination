from ShipsEnv import ShipsEnv
import DumbAI as dum
from SmartAI import DQNAgent
import numpy as np

env = ShipsEnv(False)
vec = env.game_vec
reward = 0
games_count = 0
wins = 0

agent = DQNAgent(70, 4)

num_games = 100
i = 0
while i < num_games:
	print("iteration #", i)
	while reward == 0:
		player_ai = agent.act(vec)
		opponent_ai = dum.act(vec)
		reward, vec = env.step(player_ai, opponent_ai)
	games_count += 1
	if reward == 1:
		wins += 1
	i += 1
	env.reset()
	reward = 0
	vec = env.game_vec
	print("wins: ", wins)
win_rate = float(wins)/games_count
print(win_rate)