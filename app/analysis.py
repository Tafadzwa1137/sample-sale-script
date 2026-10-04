import pandas as pd


def analyze_preferences(data):
    preference_counts = data['preference_category'].value_counts()
    average_ratings = data.groupby('preference_category')['rating'].mean()

    return preference_counts, average_ratings


def upload_analysis_results(preference_counts, average_ratings, output_directory):
    output_directory.mkdir(parents=True, exist_ok=True)
    preference_counts.to_csv(output_directory / 'preference_counts.csv', index=True)
    average_ratings.to_csv(output_directory / 'average_ratings.csv', index=True)