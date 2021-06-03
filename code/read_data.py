import pandas as pd

def get_series(file):
    '''retrieves different series from the dataset'''

    all_data = pd.read_csv(file, na_values = "..")

    series_list = []
    tracking = []
    counter = 1
    for index, row in all_data.iterrows():
        if row['Series code'] not in tracking:
            series_list.append((counter, row['Series code'], row['Series name']))
            tracking.append(row['Series code'])
            counter += 1

    return series_list

def get_data(file, data_type):
    '''Retrieves specified type of data from inputfile.'''

    all_data = pd.read_csv(file, na_values = "..")

    filtered_data = all_data[all_data['Series code'] == data_type]

    return filtered_data