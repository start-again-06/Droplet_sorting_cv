# Acoustic Droplet Sorting using Reinforcement Learning & OpenCV

---

## Overview
This project implements **droplet sorting under acoustic force** using:  
- **Reinforcement Learning (RL)** with Stable-Baselines3 (PPO)  
- **Computer Vision (OpenCV)** for droplet detection  
- **Acoustic Force** to control droplet movement  

The system detects droplet size, applies acoustic force, and learns to optimize sorting using RL.

---

## Features
- Droplet detection using OpenCV  
- Acoustic sorting with tunable frequency & amplitude  
- Reinforcement Learning for optimized sorting  
- Custom Gym environment for RL training  
- Compatible with real-time droplet sorting systems  

---

## How It Works

### Droplet Detection 📷
- Loads images and detects droplets using OpenCV  
- Extracts droplet size from contours  

### Reinforcement Learning 
- **State:** Droplet size & position  
- **Actions:** Adjust acoustic frequency & amplitude  
- **Reward:** +1 for correct sorting, -1 for incorrect sorting  

### Acoustic Sorting 
- RL agent learns optimal frequency & amplitude to sort droplets  
- Acoustic force is applied via piezoelectric transducers

## Results
- The trained RL model successfully sorts droplets into **Small, Medium, and Large** categories by dynamically adjusting acoustic parameters.

---

## Contributing
- Fork the repository  
- Create a new branch  
- Commit your changes  
- Open a pull request  

---

## License
MIT License. Free to use, modify, and distribute for academic and research purposes.

