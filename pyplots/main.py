import math
import time
import gym
env = gym.make('CartPole-v0')

env.reset()
obs = env.env.state = [0, 0, math.radians(1), 0]
print(obs)

done = False
totalReward = 0
while not done:
    env.render()

    # pos = obs[0]
    # vel = obs[1]
    angle = obs[2]
    # angleVelocity = obs[3]

    if angle < 0:
        action = 0
    else:
        action = 1

    obs, reward, done, info = env.step(action)
    print(obs)
    totalReward += reward
    time.sleep(0.1)

print("Total reward: %d" % totalReward)
env.close()