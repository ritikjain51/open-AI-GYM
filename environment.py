import gym 

class Environment(gym.wrappers.time_limit.TimeLimit):
    
    def __init__(self, env_name, *args, **kwargs):
        super(Environment, self).__init__(gym.make(env_name,  *args, **kwargs))
        self.print_env()
    
    def print_env(self):
        print("Environment Name: ", self.spec.name)
        print("Action Space Type: ", "DISCRETE" if type(self.action_space) == gym.spaces.discrete.Discrete else "CONTINUOUS" )
        print("Observation Space Type: ", "DISCRETE" if type(self.observation_space) == gym.spaces.discrete.Discrete else "CONTINUOUS" )
        print("Observation Space: ", self.observation_space)
        
    def __del__(self):
        self.close()
