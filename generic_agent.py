import gym
import numpy as np


class GenericAgent:
    
    def __init__(self, env: gym.wrappers.time_limit.TimeLimit):
        action_space = env.action_space

        # Action Space
        if type(action_space) == gym.spaces.discrete.Discrete:
            self.action_size = action_space.n
            self.action_type = "DISCRETE"
            self.action_space = np.arange(action_space.n)
        else:
            self.action_type = "CONTINUOUS"
            self.action_low = action_space.low
            self.action_high = action_space.high
            self.action_size = action_space.shape
        
        
        # Observation Type
        obs_space = env.observation_space
        if type(obs_space) == gym.spaces.discrete.Discrete:
            self.observation_type = "DISCRETE"
            self.observation_size = obs_space.n
        else:
            self.observation_type = "CONTINUOUS"
            self.observation_low = obs_space.low
            self.observation_high = obs_space.high
            self.observation_size = obs_space.shape
        
    
    def get_random_action(self, state = None):
        
        if self.action_type == "DISCRETE":
            return np.random.choice(self.action_space)
        else:
            return np.random.uniform(low=self.action_low, high=self.action_high, size=self.action_shape)
