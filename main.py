import numpy as np
from sklearn.linear_model import LinearRegression

f = "data/computer_price.csv"
data = np.loadtxt(f, delimiter=',', skiprows=1)

x = data[:, :-1]
y = data[:, -1]

model = LinearRegression()
model.fit(x, y)

try:
    cpu = float(input("CPU (MHz): "))
    ram = float(input("RAM (GB): "))
    storage = float(input("Storage (GB): "))
    gpu = int(input("GPU (1 - yes, 0 - no): "))
    screen = float(input("Screen Size (inches): "))
    battery = float(input("Battery Life (hours): "))
    
    pred = model.predict([[cpu, ram, storage, gpu, screen, battery]])
    print(f"Estimated Price: ${pred[0]:.2f}")
except ValueError:
    print("Incorrect input!")