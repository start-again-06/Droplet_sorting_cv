import gym
from gym import spaces
import numpy as np
import random

class AcousticSortingEnv(gym.Env):
    def __init__(self):
        super(AcousticSortingEnv, self).__init__()

        
        self.action_space = spaces.MultiDiscrete([10, 10])  # 10 levels of frequency & amplitude


        self.observation_space = spaces.Box(low=np.array([0, 0]), high=np.array([500, 1]), dtype=np.float32)

        self.current_droplet_size = None
        self.current_position = None

    def reset(self):
     
        self.current_droplet_size = random.randint(20, 400)
        self.current_position = 0.5  # Start at center of sorting field
        return np.array([self.current_droplet_size, self.current_position], dtype=np.float32)

    def step(self, action):
       
        freq, amp = action
        force = self.calculate_force(freq, amp, self.current_droplet_size)
        self.current_position += force

        reward = -1
        if self.current_position < 0.3:  # Small droplets move left
            reward = 1 if self.current_droplet_size < 150 else -1
        elif 0.3 <= self.current_position <= 0.7:  # Medium droplets
            reward = 1 if 150 <= self.current_droplet_size <= 300 else -1
        else:  # Large droplets move right
            reward = 1 if self.current_droplet_size > 300 else -1

        done = True  # Reset for next droplet
        return np.array([self.current_droplet_size, self.current_position], dtype=np.float32), reward, done, {}

    def calculate_force(self, freq, amp, size):
        return calculate_force

