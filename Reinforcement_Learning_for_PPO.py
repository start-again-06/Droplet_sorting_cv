from stable_baselines3 import PPO

env = AcousticSortingEnv()
model = PPO("MlpPolicy", env, verbose=1)
model.learn(total_timesteps=10000)
model.save("acoustic_sorting_model")
