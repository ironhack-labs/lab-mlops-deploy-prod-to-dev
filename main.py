import numpy as np

def calculate_mean(numbers):
    return np.mean(numbers)

if __name__ == "__main__":
    data = [10, 20, 30, 40, 50]
    result = calculate_mean(data)
    print(f"The mean is: {result}")