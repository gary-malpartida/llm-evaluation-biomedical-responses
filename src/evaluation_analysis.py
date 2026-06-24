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
