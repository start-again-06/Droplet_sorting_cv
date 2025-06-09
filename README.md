🎵 Acoustic Droplet Sorting using Reinforcement Learning & OpenCV

📌 Overview:

This project implements droplet sorting under the influence of acoustic force using:

Reinforcement Learning (RL) with Stable-Baselines3 (PPO)

Computer Vision (OpenCV) for droplet detection

Acoustic Force Application to control droplet movement

🔬 The system detects droplet size, applies an acoustic force, and learns to optimize sorting using RL.

🚀 Features:


✅ Droplet detection using OpenCV

✅ Acoustic sorting with tunable frequency & amplitude

✅ Reinforcement Learning for optimized sorting

✅ Custom Gym environment for RL training

✅ Compatible with real-time droplet sorting systems

🛠 Installation:

Ensure you have the required libraries installed:

pip install opencv-python numpy gym stable-baselines3 matplotlib

📂 Project Structure:

📁 acoustic-droplet-sorting

│── 📜 README.md       # Project Documentation

│── 📜 main.py         # Main script for sorting

│── 📜 env.py          # Gym environment

│── 📜 detect.py       # OpenCV-based droplet detection

│── 📜 train.py        # RL training script

│── 📜 test.py         # Testing trained model

│── 📁 models          # Saved RL models

│── 📁 images          # Sample droplet images

🎯 How It Works:

Droplet Detection 📷

Loads image and detects droplets using OpenCV.

Extracts droplet size from contours.

Reinforcement Learning 🧠

State: Droplet size & position.

Actions: Adjust acoustic frequency & amplitude.

Reward: +1 for correct sorting, -1 for incorrect sorting.

Acoustic Sorting 🎵

RL agent learns the optimal frequency & amplitude to sort droplets.

Acoustic force is applied based on piezoelectric transducers.

📜 Usage:

1️⃣ Run Droplet Detection

python detect.py --image path/to/droplet_image.jpg

2️⃣ Train RL Model

python train.py

3️⃣ Test RL Model on New Droplets

python test.py --image path/to/new_image.jpg

📊 Results:

📌 The trained RL model successfully sorts droplets into Small, Medium, and Large categories by dynamically adjusting acoustic parameters.

🤝 Contributing:

🔹 Fork the repository 📌🔹 Create a new branch 🔄🔹 Commit your changes 🎯🔹 Open a pull request 🚀
