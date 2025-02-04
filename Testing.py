model = PPO.load("acoustic_sorting_model")


image_path = "droplets.jpg"
droplet_sizes = detect_droplets(image_path)

for size in droplet_sizes:
    obs = np.array([size, 0.5], dtype=np.float32)  
    action, _ = model.predict(obs)

    freq, amp = action
    print(f"Droplet {size} µm -> Acoustic Freq: {freq * 10} kHz, Amp: {amp * 10}")
