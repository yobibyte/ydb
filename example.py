import ydb
import matplotlib.pyplot as plt

print(f"Session name: {ydb.SESSION_NAME}")

text = "Hello World4242"

result = ydb.add_text(text)
print(result)

plt.figure()
plt.plot([1, 2, 3, 4], [1, 4, 9, 16])
plt.title("lolala")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")

# Save the plot to a BytesIO object
result = ydb.add_figure(plt.gcf())
print(result)
