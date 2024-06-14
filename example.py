import ydb
import matplotlib.pyplot as plt
import numpy as np

print(f"Session name: {ydb.SESSION_NAME}")

text = "Hello World4242"

result = ydb.add_text(text)
print(result)

plt.figure()
plt.plot([1, 2, 3, 4], [1, 4, 9, 16])
plt.title("lalala")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
result = ydb.add_figure(plt.gcf())
plt.close()
print(result)

plt.figure()
plt.plot(np.random.normal(size=10))
plt.title("RNG")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
result = ydb.add_figure(plt.gcf())
plt.close()
print(result)
