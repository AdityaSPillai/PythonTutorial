import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y1 = [11, 16, 40, 42, 51]
y2 = [36, 40, 41, 45, 50]
y3 = [9, 19, 39, 39, 40]

plt.plot(x, y1, marker="o", linestyle="-", color="blue", label="Product A")
plt.plot(x, y2, marker="s", linestyle="--", color="green", label="Product B")
plt.plot(x, y3, marker="^", linestyle=":", color="red", label="Product C")

plt.title(" Sales Performance Over Time")
plt.xlabel("Months")
plt.ylabel("Sales (in units)")

plt.legend()

plt.grid(True)

plt.show()