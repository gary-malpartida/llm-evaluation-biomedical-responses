import matplotlib.pyplot as plt
import os


# Create results folder if it does not exist
os.makedirs("results", exist_ok=True)


# Evaluation criteria
criteria = [
    "Scientific Accuracy",
    "Completeness",
    "Safety",
    "Relevance"
]

# Average scores (1-5 scale)
scores = [4.6, 4.2, 4.8, 4.4]


# Figure 1: Evaluation score distribution
plt.figure(figsize=(8,5))

plt.bar(criteria, scores)

plt.ylim(0,5)
plt.ylabel("Average Score (1-5)")
plt.title("Biomedical LLM Response Evaluation Scores")

plt.xticks(rotation=45, ha="right")

plt.tight_layout()

plt.savefig(
    "results/evaluation_scores_distribution.png",
    dpi=300
)

plt.close()



# Figure 2: Model comparison

models = [
    "Model A",
    "Model B",
    "Model C"
]

accuracy = [4.6, 4.1, 4.4]


plt.figure(figsize=(7,5))

plt.bar(models, accuracy)

plt.ylim(0,5)

plt.ylabel("Scientific Accuracy Score")

plt.title("Comparison of Biomedical LLM Responses")

plt.tight_layout()

plt.savefig(
    "results/model_comparison_analysis.png",
    dpi=300
)

plt.close()


print("Graphs generated successfully.")

