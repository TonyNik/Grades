import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

Teacher_1 = [3, 3, 9.4, 12.4, 12.6, 14.2, 14.8, 17]
Teacher_2 = [4.2, 4.4, 6.8, 11.4, 14.4, 14.4, 15.4, 17.2]

Teacher_1_mean = np.mean(Teacher_1)
Teacher_1_median = np.median(Teacher_1)
Teacher_1_std = np.std(Teacher_1)
Teacher_1_q1 = np.percentile(Teacher_1, 25)
Teacher_1_q3 = np.percentile(Teacher_1, 75)
Teacher_1_above_10 = sum(1 for grade in Teacher_1 if grade > 10)
Teacher_1_percentage_above_10 = (Teacher_1_above_10 / len(Teacher_1)) * 100

Teacher_2_mean = np.mean(Teacher_2)
Teacher_2_median = np.median(Teacher_2)
Teacher_2_std = np.std(Teacher_2)
Teacher_2_q1 = np.percentile(Teacher_2, 25)
Teacher_2_q3 = np.percentile(Teacher_2, 75)
Teacher_2_above_10 = sum(1 for grade in Teacher_2 if grade > 10)
Teacher_2_percentage_above_10 = (Teacher_2_above_10 / len(Teacher_2)) * 100

print("\nTeacher_1 Statistics:")
print(f"Mean: {Teacher_1_mean:.2f}")
print(f"Median: {Teacher_1_median:.2f}")
print(f"Standard Deviation: {Teacher_1_std:.2f}")
print(f"Q1: {Teacher_1_q1:.2f}")
print(f"Q3: {Teacher_1_q3:.2f}")
print(f"Above 10: {Teacher_1_percentage_above_10:.1f}%")
print(f"Number of students: {len(Teacher_1)}")

print("\nTeacher_2 Statistics:")
print(f"Mean: {Teacher_2_mean:.2f}")
print(f"Median: {Teacher_2_median:.2f}")
print(f"Standard Deviation: {Teacher_2_std:.2f}")
print(f"Q1: {Teacher_2_q1:.2f}")
print(f"Q3: {Teacher_2_q3:.2f}")
print(f"Above 10: {Teacher_2_percentage_above_10:.1f}%")
print(f"Number of students: {len(Teacher_2)}")


fig = plt.figure(figsize=(20, 8))
gs = fig.add_gridspec(1, 3)

ax1 = fig.add_subplot(gs[0])
bins1 = [0, 5, 10, 15, 20]
freq_Teacher_11, _ = np.histogram(Teacher_1, bins=bins1)
freq_Teacher_2_1, _ = np.histogram(Teacher_2, bins=bins1)

percentage_Teacher_11 = (freq_Teacher_11 / len(Teacher_1)) * 100
percentage_Teacher_2_1 = (freq_Teacher_2_1 / len(Teacher_2)) * 100

x1 = np.array([2.5, 7.5, 12.5, 17.5])

ax1.set_facecolor('#f7f7f7')
ax1.grid(True, which='both', axis='y', linestyle='--', alpha=0.6)
ax1.bar(x1 - 0.5, percentage_Teacher_11, width=1, label="Teacher_1", color='#1f77b4', alpha=0.75, edgecolor='black', linewidth=1.2)
ax1.bar(x1 + 0.5, percentage_Teacher_2_1, width=1, label="Teacher_2", color='#2ca02c', alpha=0.75, edgecolor='black', linewidth=1.2)

ax1.axvline(x=Teacher_1_mean, color='#1f77b4', linestyle='--', alpha=0.5, label=f'Teacher_1 Mean')
ax1.axvline(x=Teacher_1_median, color='#1f77b4', linestyle=':', alpha=0.5, label=f'Teacher_1 Median')
ax1.axvline(x=Teacher_2_mean, color='#2ca02c', linestyle='--', alpha=0.5, label=f'Teacher_2 Mean')
ax1.axvline(x=Teacher_2_median, color='#2ca02c', linestyle=':', alpha=0.5, label=f'Teacher_2 Median')

ax1.set_title("Distribution of Grades")
ax1.set_xlabel("Grade Ranges")
ax1.set_ylabel("%")
ax1.set_xticks(x1)
ax1.set_xticklabels(["0-5", "5-10", "10-15", "15-20"])
ax1.legend()

ax2 = fig.add_subplot(gs[1])
x = np.linspace(0, 20, 1000)
Teacher_1_dist = stats.norm.pdf(x, Teacher_1_mean, Teacher_1_std) * 100
Teacher_2_dist = stats.norm.pdf(x, Teacher_2_mean, Teacher_2_std) * 100

# Calculate combined distribution
combined_data = np.concatenate([Teacher_1, Teacher_2])
combined_mean = np.mean(combined_data)
combined_std = np.std(combined_data)
combined_median = np.median(combined_data)
combined_dist = stats.norm.pdf(x, combined_mean, combined_std) * 100

ax2.set_facecolor('#f7f7f7')
ax2.grid(True, which='both', axis='y', linestyle='--', alpha=0.6)
ax2.plot(x, Teacher_1_dist, color='#1f77b4', label=f'Teacher_1', alpha=0.75)
ax2.plot(x, Teacher_2_dist, color='#2ca02c', label=f'Teacher_2', alpha=0.75)
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
    "Teacher_1:\n"
    f"Mean: {Teacher_1_mean:.2f}\n"
    f"Median: {Teacher_1_median:.2f}\n"
    f"Std Dev: {Teacher_1_std:.2f}\n"
    f"Q1: {Teacher_1_q1:.2f}\n"
    f"Q3: {Teacher_1_q3:.2f}\n"
    f"Above 10: {Teacher_1_percentage_above_10:.1f}%\n"
    f"Students: {len(Teacher_1)}\n\n"
    "Teacher_2:\n"
    f"Mean: {Teacher_2_mean:.2f}\n"
    f"Median: {Teacher_2_median:.2f}\n"
    f"Std Dev: {Teacher_2_std:.2f}\n"
    f"Q1: {Teacher_2_q1:.2f}\n"
    f"Q3: {Teacher_2_q3:.2f}\n"
    f"Above 10: {Teacher_2_percentage_above_10:.1f}%\n"
    f"Students: {len(Teacher_2)}"
)

fig.text(0.02, 0.98, stats_text, 
         verticalalignment='top', 
         bbox=dict(boxstyle='round', facecolor='white', alpha=0.8))

plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
