import pandas as pd

# Load datasets
prompts = pd.read_csv("data/prompts.csv")
responses = pd.read_csv("data/model_responses.csv")
scores = pd.read_csv("data/evaluation_scores.csv")

# Merge datasets
df = scores.merge(responses, on=["prompt_id", "response_id"], how="left")
df = df.merge(prompts, on="prompt_id", how="left")

# Basic analysis

print("\n=== Overall Score Summary ===")
print(df["overall_score"].describe())

print("\n=== Average Score by Domain ===")
print(df.groupby("domain")["overall_score"].mean())

print("\n=== Average by Dimension ===")
dimensions = ["factual_accuracy", "completeness", "terminology", "clarity"]
print(df[dimensions].mean())

print("\n=== Risk Level Distribution ===")
print(df["risk_level"].value_counts())

# Generate Markdown summary report
with open("results/summary.md", "w", encoding="utf-8") as report:
    report.write("# Biomedical LLM Evaluation Summary\n\n")
    report.write(f"**Total responses evaluated:** {len(df)}\n\n")
    report.write(f"**Average overall score:** {df['overall_score'].mean():.2f}\n\n")

    report.write("## Average Score by Domain\n\n")
    domain_scores = df.groupby("domain")["overall_score"].mean()

    for domain, score in domain_scores.items():
        report.write(f"- {domain}: {score:.2f}\n")

    report.write("\n## Average by Evaluation Dimension\n\n")

    for dimension in dimensions:
        report.write(f"- {dimension}: {df[dimension].mean():.2f}\n")