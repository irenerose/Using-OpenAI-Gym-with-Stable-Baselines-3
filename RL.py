#!/usr/bin/env python
# coding: utf-8


# Import the OpenAI Gym and PPO algorithm implementation from Stable Baselines3 libraries. 
import gym
from stable_baselines3 import PPO

# create the Cartpole environment from the OpenAI Gym
env = gym.make('CartPole-v1')

# create the agent and train it for 1000 steps
model = PPO('MlpPolicy', env, verbose=1)
model.learn(total_timesteps=1000)

# run the environment for one episode and get the steps and reward for this episode
vec_env = model.get_env()
obs = vec_env.reset()
done = False
steps = 0
reward = 0
while not done:
    action, _state = model.predict(obs, deterministic=True)
    obs, r, done, info = vec_env.step(action)
    steps += 1
    reward += r

# Print the number of steps taken and the accumulated reward obtained during the episode.
print('Reward and steps without evaluate_policy')
print(f'Steps: {steps}')
print(f'Reward: {reward}')


#This code demonstrates how to use the evaluate_policy function from the Stable Baselines3 library to evaluate the 
#performance of a trained agent on a given environment.
from stable_baselines3.common.evaluation import evaluate_policy

# create the environment
env = gym.make('CartPole-v1')

# create the agent and train it for 1000 steps
model = PPO('MlpPolicy', env, verbose=1)
model.learn(total_timesteps=1000)

# Evaluate the trained agent
#The function returns two variables: reward and step. The reward variable contains the total reward obtained by the agent 
# and the step variable contains the total number of steps taken by the agent.
reward, step = evaluate_policy(model, env, n_eval_episodes=1, return_episode_rewards=True)

print('Reward and steps with evaluate_policy')
print(f"reward:{reward} steps: {step}")






