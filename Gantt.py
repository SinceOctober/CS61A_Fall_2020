import matplotlib.pyplot as plt
import pandas as pd
import matplotlib.patches as mpatches

# Updated timeline data
tasks = [
    ("Literature Review", 1, 3),
    ("Dataset Development", 2, 6),
    ("Conceptual Design of BaMFA Framework", 3, 6),
    ("Data Collection and Preprocessing", 4, 7),
    ("Model Implementation", 7, 9),
    ("Preliminary Model Validation", 9, 10),
    ("Real-world Case Study Application", 10, 12),
    ("Scenario Analysis & Simulation", 12, 13),
    ("Model Refinement and Integration", 13, 14),
    ("Final Application and Results Compilation", 14, 15),
    ("Writing, Publication & Policy Recommendations", 13, 15)
]

# Create DataFrame
df = pd.DataFrame(tasks, columns=["Task", "Start", "End"])
df["Duration"] = df["End"] - df["Start"] + 1

# Phase colors
colors = {
    "Foundation": "#6baed6",       # Blue
    "Implementation": "#74c476",   # Green
    "Application": "#fd8d3c",      # Orange
    "Synthesis": "#9e9ac8"         # Purple
}

# Task to phase mapping
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

# Plot
fig, ax = plt.subplots(figsize=(12, 7))
for i, row in df.iterrows():
    ax.barh(
        y=i,
        width=row["Duration"],
        left=row["Start"],
        height=0.6,
        color=row["Color"],
        edgecolor='black'
    )

# Axis setup
ax.set_yticks(range(len(df)))
ax.set_yticklabels(df["Task"])
ax.invert_yaxis()
ax.set_xlabel("Month")
ax.set_xlim(1, 15)
ax.set_title("Project Timeline Gantt Chart")

# Legend
legend_patches = [mpatches.Patch(color=color, label=label) for label, color in colors.items()]
ax.legend(handles=legend_patches, loc='upper right')

# Style
plt.grid(axis='x', linestyle='--', alpha=0.6)
plt.tight_layout()
plt.show()
