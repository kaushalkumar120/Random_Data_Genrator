import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

class RandomDataGenerator:

    def __init__(self, seed=None):
        if seed:
            np.random.seed(seed)
        self.data1 = None
        self.data2 = None

    def generate_data(self, mean1, std1, mean2, std2, size):
        self.data1 = np.random.normal(mean1, std1, size)
        self.data2 = np.random.normal(mean2, std2, size)

    def visualize(self):
        # Histogram
        plt.figure()
        sns.histplot(self.data1, kde=True, label="Data1")
        sns.histplot(self.data2, kde=True, label="Data2")
        plt.legend()
        plt.title("Histogram Comparison")
        plt.show()

        # Box Plot
        plt.figure()
        sns.boxplot(data=[self.data1, self.data2])
        plt.xticks([0, 1], ["Data1", "Data2"])
        plt.title("Box Plot Comparison")
        plt.show()

        # Pie Chart
        means = [np.mean(self.data1), np.mean(self.data2)]
        plt.figure()
        plt.pie(means, labels=["Data1", "Data2"], autopct='%1.1f%%')
        plt.title("Mean Comparison")
        plt.show()

    def export_csv(self):
        df = pd.DataFrame({"Data1": self.data1, "Data2": self.data2})
        df.to_csv("data.csv", index=False)
        print("✅ Data exported")

# -------- MENU --------
gen = RandomDataGenerator()

print("🎲 Random Data Generator")

mean1 = float(input("Enter Mean1: "))
std1 = float(input("Enter Std1: "))
mean2 = float(input("Enter Mean2: "))
std2 = float(input("Enter Std2: "))
size = int(input("Enter Size: "))

gen.generate_data(mean1, std1, mean2, std2, size)

while True:
    print("\n1. Visualize\n2. Export CSV\n3. Exit")
    choice = input("Enter choice: ")

    if choice == "1":
        gen.visualize()
    elif choice == "2":
        gen.export_csv()
    elif choice == "3":
        break
    else:
        print("Invalid choice!")