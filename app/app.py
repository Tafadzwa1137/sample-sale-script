import argparse
from pathlib import Path

import pandas as pd

from analysis import analyze_preferences, upload_analysis_results


PROJECT_ROOT = Path(__file__).resolve().parents[2]
DEFAULT_INPUT = PROJECT_ROOT / 'sample-sale-back' / 'data' / 'input' / 'preferences.csv'
DEFAULT_OUTPUT = PROJECT_ROOT / 'sample-sale-back' / 'data' / 'output'


def initialise(input_path=DEFAULT_INPUT, output_directory=DEFAULT_OUTPUT):
	try:
		data = pd.read_csv(input_path)
	except pd.errors.EmptyDataError as error:
		raise ValueError(
			f'Input file is empty: {input_path}. Add a header and preference rows before running the app.'
		) from error

	required_columns = {'preference_category', 'rating'}
	missing_columns = required_columns.difference(data.columns)
	if missing_columns:
		missing = ', '.join(sorted(missing_columns))
		raise ValueError(f'Input file is missing required column(s): {missing}')

	preference_counts, average_ratings = analyze_preferences(data)
	upload_analysis_results(preference_counts, average_ratings, output_directory)
	return output_directory


def main():
	parser = argparse.ArgumentParser(description='Run the sample sale preference analysis.')
	parser.add_argument('--input', type=Path, default=DEFAULT_INPUT, help='Path to the preference CSV file.')
	parser.add_argument('--output', type=Path, default=DEFAULT_OUTPUT, help='Directory for analysis results.')
	arguments = parser.parse_args()

	try:
		output_directory = initialise(arguments.input, arguments.output)
	except (FileNotFoundError, ValueError) as error:
		parser.error(str(error))

	print(f'Analysis complete. Results written to {output_directory}')


if __name__ == '__main__':
	main()


