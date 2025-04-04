import matplotlib.pyplot as plt
import pandas as pd
import matplotlib.patches as mpatches

# Define tasks and their time spans
tasks = [
    ("Literature Review", 1, 2),
    ("Dataset Development", 1, 2),
    ("Conceptual Design of BaMFA Framework", 1, 3),
    ("Data Collection and Preprocessing", 2, 3),
    ("Model Implementation", 3, 4),
    ("Preliminary Model Validation", 4, 4),
    ("Real-world Case Study Application", 4, 5),
    ("Scenario Analysis & Simulation", 5, 5),
    ("Model Refinement and Integration", 5, 5),
    ("Final Application and Results Compilation", 5, 5),
    ("Writing, Publication & Policy Recommendations", 5, 5)
]

# Create DataFrame
df = pd.DataFrame(tasks, columns=["Task", "Start", "End"])
df["Duration"] = df["End"] - df["Start"] + 1

# Color coding by research phase
colors = {
    "Foundation": "#6baed6",       # Blue
    "Implementation": "#74c476",   # Green
    "Application": "#fd8d3c",      # Orange
    "Synthesis": "#9e9ac8"         # Purple
}

# Assign colors to each task
phase_mapping = {
    "Literature Review": "Foundation",
    "Dataset Development": "Foundation",
    "Conceptual Design of BaMFA Framework": "Foundation",
    "Data Collection and Preprocessing": "Implementation",
    "Model Implementation": "Implementation",
    "Preliminary Model Validation": "Implementation",
    "Real-world Case Study Application": "Application",
    "Scenario Analysis & Simulation": "Application",
    "Model Refinement and Integration": "Synthesis",
    "Final Application and Results Compilation": "Synthesis",
    "Writing, Publication & Policy Recommendations": "Synthesis"
}
df["Color"] = df["Task"].map(lambda x: colors[phase_mapping[x]])

# Plotting
fig, ax = plt.subplots(figsize=(10, 6))

# Plot each task as a horizontal bar
for i, row in df.iterrows():
    ax.barh(
        y=i,
        width=row["Duration"],
        left=row["Start"],
        height=0.6,
        color=row["Color"],
        edgecolor='black'
    )

# Axis formatting
ax.set_yticks(range(len(df)))
ax.set_yticklabels(df["Task"])
ax.invert_yaxis()  # Most recent on top
ax.set_xlabel("Month")
ax.set_xlim(1, 15)
ax.set_title("Project Timeline Gantt Chart")

# Custom legend
legend_patches = [mpatches.Patch(color=color, label=phase) for phase, color in colors.items()]
ax.legend(handles=legend_patches, loc='upper right')

# Aesthetics
plt.grid(axis='x', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()
