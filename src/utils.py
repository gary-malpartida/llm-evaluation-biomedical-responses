import pandas as pd

def load_data():
    prompts = pd.read_csv("data/prompts.csv")
    responses = pd.read_csv("data/model_responses.csv")
    scores = pd.read_csv("data/evaluation_scores.csv")
    return prompts, responses, scores


def merge_data():
    prompts, responses, scores = load_data()
    df = scores.merge(responses, on=["prompt_id", "response_id"])
    df = df.merge(prompts, on="prompt_id")
    return df
