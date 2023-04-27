# Using-OpenAI-Gym-with-Stable-Baselines-3
## Description
This README provides a step-by-step guide on how to use the open AI gym environment “CartPole” for training it with stable-baselines-3 with PPO for 1000 steps. The trained agent is then run through the environment once until the cart pole falls down, and the steps and reward of this episode are reported.

## Installation
To run this code using Anaconda, you can create the environment from the environment.yml file above by using the following commands in an Anaconda Prompt:
```ruby
conda env create -f environment.yml
```
Verify that the new environment was installed correctly using:
```ruby
conda env list
```
The first line of the yml file sets the new environment's name(here: rl_env). Activate the new environment using:
```ruby
conda activate rl_env
```
Run the python file(here:RL.py) as normal in the Annaconda prompt using :
```ruby
python RL.py
```
It can also be run using the different applications available in Anaconda Navigator that aid in developing Python eg: Jupyter Notebook, Visual Studio, Spyder etc.
