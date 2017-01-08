from textblob import TextBlob
from file_management import prepare_directories_for_processing, get_all_files_for_processing, PATH_TO_PHILOSOPHERS
from graphs import convert_data_for_plotting, format_x_val_names

"""
––––––––––––––––––––– THE HAPPIEST PHILOSOPHER, Instant Linguistic Sentiment Analyses and Graph Generator –––––––––––––
                                            See README.md for more!
                                ------------––––––––––––––––––––––––––––––––––––
"""


# Uses TextBlob library to convert text to a TextBlob object, allowing for sentiment analyses
def convert_to_text_blobs(files_to_analyze):
    text_blobs = []
    for file in files_to_analyze:
        with open(file, 'r') as text_in:
            blob = TextBlob(text_in.read().replace('\n', ' '))
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


# Main Method
if __name__ == '__main__':
    directories_list = prepare_directories_for_processing(PATH_TO_PHILOSOPHERS)
    files_to_analyze, work_names, author_names = get_all_files_for_processing(directories_list)
    blobs = convert_to_text_blobs(files_to_analyze)
    polarity_values, subjectivity_values = sentiment_analysis(author_names, work_names, blobs)
    work_names = format_x_val_names(work_names, author_names)
    convert_data_for_plotting(work_names, polarity_values, subjectivity_values)

