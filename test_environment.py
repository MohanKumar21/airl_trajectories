import gymnasium as gym 
import gymnasium_robotics 

gym.register_envs(gymnasium_robotics)
env = gym.make("Hopper-v4")
print(env.action_space)
