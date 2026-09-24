import pandas as pd


#Pull preference data

source_data = pd.read_csv('data/input/preferences.csv')


# Analysis of the preference data
def analyze_preferences(data):
    # Example analysis: Count the number of preferences for each category
    preference_counts = data['preference_category'].value_counts()
    
    # Example analysis: Calculate the average rating for each category
    average_ratings = data.groupby('preference_category')['rating'].mean()
    
    return preference_counts, average_ratings


#upload data to output folder
def upload_analysis_results(preference_counts, average_ratings):
    # Save the analysis results to CSV files
    preference_counts.to_csv('data/output/preference_counts.csv', index=True)
    average_ratings.to_csv('data/output/average_ratings.csv', index=True)