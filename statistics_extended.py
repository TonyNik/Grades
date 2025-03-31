import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

# --- Data Input Section ---

# Ask user for the number of professors
num_professors = int(input("Enter the number of professors: "))

# Dictionary to store professor names and their grades
professors = {}
professor_names = []
for i in range(num_professors):
    name = input(f"Enter the name of professor {i+1}: ")
    grades = []
    print(f"Enter the grades for {name} (each between 0 and 20). Type 'done' when finished.")
    while True:
        grade_input = input("Enter a grade (or 'done'): ")
        if grade_input.lower() == 'done':
            break
        try:
            grade = float(grade_input)
            if grade < 0 or grade > 20:
                print("Grade must be between 0 and 20. Please try again.")
                continue
            grades.append(grade)
        except ValueError:
            print("Invalid input. Please enter a number or 'done'.")
    professors[name] = grades
    professor_names.append(name)

# Display the sorted ratings for each professor
for name, grades in professors.items():
    print(f"\n{name}'s ratings: {np.sort(grades)}")

# --- Statistics Computation Section ---

# Compute statistics for each professor
prof_stats = {}
for name, grades in professors.items():
    if len(grades) > 0:
        mean_val = np.mean(grades)
        median_val = np.median(grades)
        std_val = np.std(grades)
        q1_val = np.percentile(grades, 25)
        q3_val = np.percentile(grades, 75)
        skew_val = stats.skew(grades) if len(grades) > 1 else 0
        kurt_val = stats.kurtosis(grades) if len(grades) > 1 else 0
        above_10 = sum(1 for grade in grades if grade > 10)
        percentage_above_10 = (above_10 / len(grades)) * 100
        prof_stats[name] = {
            "mean": mean_val,
            "median": median_val,
            "std": std_val,
            "q1": q1_val,
            "q3": q3_val,
            "skew": skew_val,
            "kurtosis": kurt_val,
            "above_10": percentage_above_10,
            "n": len(grades)
        }
    else:
        prof_stats[name] = None

# Print the computed statistics for each professor
print("\nProfessor Statistics:")
for name, s in prof_stats.items():
    if s is not None:
        print(f"\n{name}:")
        print(f"  Mean: {s['mean']:.2f}")
        print(f"  Median: {s['median']:.2f}")
        print(f"  Std Dev: {s['std']:.2f}")
        print(f"  Q1: {s['q1']:.2f}")
        print(f"  Q3: {s['q3']:.2f}")
        print(f"  Skewness: {s['skew']:.2f}")
        print(f"  Kurtosis: {s['kurtosis']:.2f}")
        print(f"  Above 10: {s['above_10']:.1f}%")
        print(f"  Number of students: {s['n']}")
    else:
        print(f"\n{name} has no grades entered.")

# Combine data from all professors for overall statistics
all_grades = [grade for grades in professors.values() for grade in grades if grades]
if all_grades:
    combined_data = np.array(all_grades)
    combined_mean = np.mean(combined_data)
    combined_median = np.median(combined_data)
    combined_std = np.std(combined_data)
    combined_skew = stats.skew(combined_data)
    combined_kurtosis = stats.kurtosis(combined_data)
    combined_above_10 = sum(1 for grade in combined_data if grade > 10)
    combined_percentage_above_10 = (combined_above_10 / len(combined_data)) * 100
else:
    combined_data = np.array([])
    combined_mean = combined_median = combined_std = combined_skew = combined_kurtosis = combined_percentage_above_10 = 0

print("\nCombined Statistics:")
print(f"  Mean: {combined_mean:.2f}")
print(f"  Median: {combined_median:.2f}")
print(f"  Std Dev: {combined_std:.2f}")
print(f"  Skewness: {combined_skew:.2f}")
print(f"  Kurtosis: {combined_kurtosis:.2f}")
print(f"  Above 10: {combined_percentage_above_10:.1f}%")
print(f"  Number of students: {len(combined_data)}")

# --- Plotting Section ---

# Create a figure with a gridspec layout for multiple subplots
fig = plt.figure(figsize=(20, 12))
gs = fig.add_gridspec(2, 2)

# Define histogram bins and centers
bins = [0, 5, 10, 15, 20]
bin_centers = np.array([2.5, 7.5, 12.5, 17.5])
colors = plt.rcParams['axes.prop_cycle'].by_key()['color']

# Subplot 1: Grouped Histogram for each professor and combined results
ax1 = fig.add_subplot(gs[0, 0])
# Total number of groups: professors + combined
n_total = len(professors) + 1
bar_width = 0.8 / n_total

# Plot histogram for each professor
for idx, (name, grades) in enumerate(professors.items()):
    if len(grades) == 0:
        continue
    freq, _ = np.histogram(grades, bins=bins)
    percentage = (freq / len(grades)) * 100
    offsets = bin_centers - 0.4 + idx * bar_width
    ax1.bar(offsets, percentage, width=bar_width, label=name,
            color=colors[idx % len(colors)], alpha=0.75, edgecolor='black', linewidth=1.2)
    # Plot vertical lines for mean and median
    mean_val = prof_stats[name]['mean']
    median_val = prof_stats[name]['median']
    ax1.axvline(x=mean_val, color=colors[idx % len(colors)], linestyle='--', alpha=0.5, label=f'{name} Mean')
    ax1.axvline(x=median_val, color=colors[idx % len(colors)], linestyle=':', alpha=0.5, label=f'{name} Median')

# Plot combined histogram
if len(combined_data) > 0:
    offsets = bin_centers - 0.4 + len(professors) * bar_width
    freq_combined, _ = np.histogram(combined_data, bins=bins)
    percentage_combined = (freq_combined / len(combined_data)) * 100
    ax1.bar(offsets, percentage_combined, width=bar_width, label="Combined",
            color='gray', alpha=0.75, edgecolor='black', linewidth=1.2)
    # Plot vertical lines for combined mean and median
    ax1.axvline(x=combined_mean, color='gray', linestyle='--', alpha=0.5)
    ax1.axvline(x=combined_median, color='gray', linestyle=':', alpha=0.5)

ax1.set_title("Distribution of Grades by Professor and Combined")
ax1.set_xlabel("Grade Ranges")
ax1.set_ylabel("%")
ax1.set_xticks(bin_centers)
ax1.set_xticklabels(["0-5", "5-10", "10-15", "15-20"])
ax1.legend()
ax1.grid(True, which='both', axis='y', linestyle='--', alpha=0.6)

# Subplot 2: Normal Distribution Curves for each professor and the combined data
ax2 = fig.add_subplot(gs[0, 1])
x = np.linspace(0, 20, 1000)
for idx, (name, grades) in enumerate(professors.items()):
    if len(grades) < 2:
        continue  # Need at least 2 points for a meaningful distribution
    mean_val = prof_stats[name]['mean']
    std_val = prof_stats[name]['std']
    dist = stats.norm.pdf(x, mean_val, std_val) * 100
    ax2.plot(x, dist, color=colors[idx % len(colors)], label=name, alpha=0.75)
# Plot the combined normal distribution (if applicable)
if len(combined_data) >= 2:
    combined_dist = stats.norm.pdf(x, combined_mean, combined_std) * 100
    ax2.plot(x, combined_dist, color='black', linestyle='--', label="Combined", alpha=0.75)
ax2.set_title("Normal Distribution Curves")
ax2.set_xlabel("Grade")
ax2.set_ylabel("Probability Density (%)")
ax2.legend()
ax2.grid(True, which='both', axis='y', linestyle='--', alpha=0.6)

# Subplot 3: Box Plot of Grades for each professor and the combined data
ax3 = fig.add_subplot(gs[1, :])
boxplot_data = [grades for grades in professors.values() if grades]
labels = [name for name, grades in professors.items() if grades]
if len(combined_data) > 0:
    boxplot_data.append(combined_data)
    labels.append("Combined")
ax3.boxplot(boxplot_data, labels=labels, patch_artist=True)
ax3.set_title("Box Plot of Grades")
ax3.set_ylabel("Grade")
ax3.grid(True, which='both', axis='y', linestyle='--', alpha=0.6)

# Annotate overall statistics in a text box
stats_text = ""
for name, s in prof_stats.items():
    if s is not None:
        stats_text += (f"{name}:\n"
                       f"  Mean: {s['mean']:.2f}\n"
                       f"  Median: {s['median']:.2f}\n"
                       f"  Std Dev: {s['std']:.2f}\n"
                       f"  Q1: {s['q1']:.2f}\n"
                       f"  Q3: {s['q3']:.2f}\n"
                       f"  Skewness: {s['skew']:.2f}\n"
                       f"  Kurtosis: {s['kurtosis']:.2f}\n"
                       f"  Above 10: {s['above_10']:.1f}%\n"
                       f"  Students: {s['n']}\n\n")
stats_text += ("Combined:\n"
               f"  Mean: {combined_mean:.2f}\n"
               f"  Median: {combined_median:.2f}\n"
               f"  Std Dev: {combined_std:.2f}\n"
               f"  Skewness: {combined_skew:.2f}\n"
               f"  Kurtosis: {combined_kurtosis:.2f}\n"
               f"  Above 10: {combined_percentage_above_10:.1f}%\n"
               f"  Students: {len(combined_data)}\n")

fig.text(0.02, 0.98, stats_text,
         verticalalignment='top',
         bbox=dict(boxstyle='round', facecolor='white', alpha=0.8))

plt.tight_layout(rect=[0, 0, 1, 0.95])
plt.show()
