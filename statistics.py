import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

Antonis = [3, 3, 9.4, 12.4, 12.6, 14.2, 14.8, 17]
Athina = [4.2, 4.4, 6.8, 11.4, 14.4, 14.4, 15.4, 17.2]

print(f"Antonis' ratings: {np.sort(Antonis)}")
print(f"Athina's ratings: {np.sort(Athina)}")

Antonis_mean = np.mean(Antonis)
Antonis_median = np.median(Antonis)
Antonis_std = np.std(Antonis)
Antonis_q1 = np.percentile(Antonis, 25)
Antonis_q3 = np.percentile(Antonis, 75)
Antonis_above_10 = sum(1 for grade in Antonis if grade > 10)
Antonis_percentage_above_10 = (Antonis_above_10 / len(Antonis)) * 100

Athina_mean = np.mean(Athina)
Athina_median = np.median(Athina)
Athina_std = np.std(Athina)
Athina_q1 = np.percentile(Athina, 25)
Athina_q3 = np.percentile(Athina, 75)
Athina_above_10 = sum(1 for grade in Athina if grade > 10)
Athina_percentage_above_10 = (Athina_above_10 / len(Athina)) * 100

print("\nAntonis Statistics:")
print(f"Mean: {Antonis_mean:.2f}")
print(f"Median: {Antonis_median:.2f}")
print(f"Standard Deviation: {Antonis_std:.2f}")
print(f"Q1: {Antonis_q1:.2f}")
print(f"Q3: {Antonis_q3:.2f}")
print(f"Above 10: {Antonis_percentage_above_10:.1f}%")
print(f"Number of students: {len(Antonis)}")

print("\nAthina Statistics:")
print(f"Mean: {Athina_mean:.2f}")
print(f"Median: {Athina_median:.2f}")
print(f"Standard Deviation: {Athina_std:.2f}")
print(f"Q1: {Athina_q1:.2f}")
print(f"Q3: {Athina_q3:.2f}")
print(f"Above 10: {Athina_percentage_above_10:.1f}%")
print(f"Number of students: {len(Athina)}")


fig = plt.figure(figsize=(20, 8))
gs = fig.add_gridspec(1, 3)

ax1 = fig.add_subplot(gs[0])
bins1 = [0, 5, 10, 15, 20]
freq_Antonis1, _ = np.histogram(Antonis, bins=bins1)
freq_Athina_1, _ = np.histogram(Athina, bins=bins1)

percentage_Antonis1 = (freq_Antonis1 / len(Antonis)) * 100
percentage_Athina_1 = (freq_Athina_1 / len(Athina)) * 100

x1 = np.array([2.5, 7.5, 12.5, 17.5])

ax1.set_facecolor('#f7f7f7')
ax1.grid(True, which='both', axis='y', linestyle='--', alpha=0.6)
ax1.bar(x1 - 0.5, percentage_Antonis1, width=1, label="Antonis", color='#1f77b4', alpha=0.75, edgecolor='black', linewidth=1.2)
ax1.bar(x1 + 0.5, percentage_Athina_1, width=1, label="Athina", color='#2ca02c', alpha=0.75, edgecolor='black', linewidth=1.2)

ax1.axvline(x=Antonis_mean, color='#1f77b4', linestyle='--', alpha=0.5, label=f'Antonis Mean')
ax1.axvline(x=Antonis_median, color='#1f77b4', linestyle=':', alpha=0.5, label=f'Antonis Median')
ax1.axvline(x=Athina_mean, color='#2ca02c', linestyle='--', alpha=0.5, label=f'Athina Mean')
ax1.axvline(x=Athina_median, color='#2ca02c', linestyle=':', alpha=0.5, label=f'Athina Median')

ax1.set_title("Distribution of Grades")
ax1.set_xlabel("Grade Ranges")
ax1.set_ylabel("%")
ax1.set_xticks(x1)
ax1.set_xticklabels(["0-5", "5-10", "10-15", "15-20"])
ax1.legend()

ax2 = fig.add_subplot(gs[1])
x = np.linspace(0, 20, 1000)
Antonis_dist = stats.norm.pdf(x, Antonis_mean, Antonis_std) * 100
Athina_dist = stats.norm.pdf(x, Athina_mean, Athina_std) * 100

# Calculate combined distribution
combined_data = np.concatenate([Antonis, Athina])
combined_mean = np.mean(combined_data)
combined_std = np.std(combined_data)
combined_median = np.median(combined_data)
combined_dist = stats.norm.pdf(x, combined_mean, combined_std) * 100
combined_above_10 = sum(1 for grade in combined_data if grade > 10)
combined_percentage_above_10 = (combined_above_10 / len(combined_data)) * 100

ax2.set_facecolor('#f7f7f7')
ax2.grid(True, which='both', axis='y', linestyle='--', alpha=0.6)
ax2.plot(x, Antonis_dist, color='#1f77b4', label=f'Antonis', alpha=0.75)
ax2.plot(x, Athina_dist, color='#2ca02c', label=f'Athina', alpha=0.75)
ax2.plot(x, combined_dist, color='#ff7f0e', label=f'Combined', alpha=0.75)

ax2.set_title("Distribution Around Mean")
ax2.set_xlabel("Grade Ranges")
ax2.set_ylabel("Probability Density (%)")
ax2.legend()

# Third plot: Combined 5-point bins
ax3 = fig.add_subplot(gs[2])
freq_combined, _ = np.histogram(combined_data, bins=bins1)
percentage_combined = (freq_combined / len(combined_data)) * 100

ax3.set_facecolor('#f7f7f7')
ax3.grid(True, which='both', axis='y', linestyle='--', alpha=0.6)
ax3.bar(x1, percentage_combined, width=1, color='#ff7f0e', alpha=0.75, edgecolor='black', linewidth=1.2)

# Add mean and median lines with labels
ax3.axvline(x=combined_mean, color='#ff7f0e', linestyle='--', alpha=0.5, label=f'Mean')
ax3.axvline(x=combined_median, color='#ff7f0e', linestyle=':', alpha=0.5, label=f'Median')

ax3.set_title("Combined Distribution")
ax3.set_xlabel("Grade Ranges")
ax3.set_ylabel("%")
ax3.set_xticks(x1)
ax3.set_xticklabels(["0-5", "5-10", "10-15", "15-20"])
ax3.legend()

stats_text = (
    "Antonis:\n"
    f"Mean: {Antonis_mean:.2f}\n"
    f"Median: {Antonis_median:.2f}\n"
    f"Std Dev: {Antonis_std:.2f}\n"
    f"Q1: {Antonis_q1:.2f}\n"
    f"Q3: {Antonis_q3:.2f}\n"
    f"Above 10: {Antonis_percentage_above_10:.1f}%\n"
    f"Students: {len(Antonis)}\n\n"
    "Athina:\n"
    f"Mean: {Athina_mean:.2f}\n"
    f"Median: {Athina_median:.2f}\n"
    f"Std Dev: {Athina_std:.2f}\n"
    f"Q1: {Athina_q1:.2f}\n"
    f"Q3: {Athina_q3:.2f}\n"
    f"Above 10: {Athina_percentage_above_10:.1f}%\n"
    f"Students: {len(Athina)}\n\n"
    "Combined:\n"
    f"Mean: {combined_mean:.2f}\n"
    f"Median: {combined_median:.2f}\n"
    f"Std Dev: {combined_std:.2f}\n"
    f"Above 10: {combined_percentage_above_10:.1f}%\n"
    f"Students: {len(combined_data)}\n\n"
)


print(f"Total ratings: {np.sort(combined_data)}")

fig.text(0.02, 0.98, stats_text,
         verticalalignment='top',
         bbox=dict(boxstyle='round', facecolor='white', alpha=0.8))

plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
