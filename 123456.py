import math
import random

def create_dataset():
    rng = random.Random(10)
    data = []

    for i in range(120):
        x = -1.0 + (2.0 * i / 119.0)
        noise = rng.uniform(-0.05, 0.05)
        y = math.sin(2.5 * x) + noise
        data.append((x, y))

    rng.shuffle(data)

    split = int(0.8 * len(data))
    return data[:split], data[split:]
    print(data)

print(create_dataset)