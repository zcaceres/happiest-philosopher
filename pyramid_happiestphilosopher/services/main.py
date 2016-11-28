from textblob import TextBlob
from file_management import prepare_directories_for_processing, get_all_files_for_processing, PATH_TO_PHILOSOPHERS
from graphs import convert_data_for_plotting, format_x_val_names

"""
––––––––––––––––––––– THE HAPPIEST PHILOSOPHER, Instant Linguistic Sentiment Analyses and Graph Generator –––––––––––––
            Does sentiment analyses on the text of any .txt file held in the 'philosophers' directory.

            Shows you the POLARITY and the SUBJECTIVITY of any text.

            To use:
            1) Create a folder in 'philosophers' with the name of the AUTHOR.

            2) Add any .txt file that belongs to that author. The name of the .txt file is used in
            your results graph, so name accordingly!

            3) run main.py. You need a plotly account which will automatically generate a graph and
            open your browser to show it to you at the end of the analyses.
––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
"""

# Uses TextBlob library to convert text to a TextBlob object, allowing for sentiment analyses
def convert_to_text_blobs(files_to_analyze):
    text_blobs = []
    for file in files_to_analyze:
        with open(file, 'r') as text_in:
            blob = TextBlob (text_in.read().replace('\n', ' '))
            text_blobs.append(blob)
    return text_blobs

# Calculates polarity and subjectivity scores
def sentiment_analysis(author_names, work_names, text_blobs):
    polarity_sentiments = []
    subjectivity_sentiments = []
    counter = 0
    for blob in text_blobs:
        polarity_sentiments.append(blob.sentiment[0])
        subjectivity_sentiments.append(blob.sentiment[1])
        counter += 1
    return polarity_sentiments, subjectivity_sentiments


if __name__ == '__main__':
    directories_list = prepare_directories_for_processing(PATH_TO_PHILOSOPHERS)
    files_to_analyze, work_names, author_names = get_all_files_for_processing(directories_list)
    blobs = convert_to_text_blobs(files_to_analyze)
    polarity_values, subjectivity_values = sentiment_analysis(author_names, work_names, blobs)
    work_names = format_x_val_names(work_names, author_names)
    convert_data_for_plotting(work_names, polarity_values, subjectivity_values)

