import pandas as pd


def calculate_distance_matrix(df)->pd.DataFrame():
    """
    Calculate a distance matrix based on the dataframe, df.

    Args:
        df (pandas.DataFrame)

    Returns:
        pandas.DataFrame: Distance matrix
    """
    # Write your logic here
def calculate_distance_matrix(df_3): 
    unique_ids = pd.unique(df_3[['id_start', 'id_end']].values.ravel('K'))
    distance_matrix = pd.DataFrame(0, index=unique_ids, columns=unique_ids)

    for _, row in df_3.iterrows():
        start_id, end_id, distance = row['id_start'], row['id_end'], row['distance']
        distance_matrix.at[start_id, end_id] += distance

    
    distance_matrix = distance_matrix + distance_matrix.T


    np.fill_diagonal(distance_matrix.values, 0.0)

    return distance_matrix

result_matrix = calculate_distance_matrix(df_3)
print(result_matrix)

    return df


def unroll_distance_matrix(df)->pd.DataFrame():
    """
    Unroll a distance matrix to a DataFrame in the style of the initial dataset.

    Args:
        df (pandas.DataFrame)

    Returns:
        pandas.DataFrame: Unrolled DataFrame containing columns 'id_start', 'id_end', and 'distance'.
    """
    # Write your logic here
def unroll_distance_matrix(distance_matrix):
    unrolled_data = []

    for id_start, row in distance_matrix.iterrows():
        for id_end, distance in row.items():
            if id_start != id_end:
                unrolled_data.append({'id_start': id_start, 'id_end': id_end, 'distance': distance})

    unrolled_df_3 = pd.DataFrame(unrolled_data)
    return unrolled_df_3


distance_matrix = calculate_distance_matrix(df_3)
unrolled_df_3 = unroll_distance_matrix(distance_matrix)
print(unrolled_df_3)
    return df


def find_ids_within_ten_percentage_threshold(df, reference_id)->pd.DataFrame():
    """
    Find all IDs whose average distance lies within 10% of the average distance of the reference ID.

    Args:
        df (pandas.DataFrame)
        reference_id (int)

    Returns:
        pandas.DataFrame: DataFrame with IDs whose average distance is within the specified percentage threshold
                          of the reference ID's average distance.
    """
    # Write your logic here
def find_ids_within_ten_percentage_threshold(unrolled_df_3, reference_value):
    reference_avg_distance = unrolled_df_3[unrolled_df_3['id_start'] == reference_value]['distance'].mean()

    threshold_lower = reference_avg_distance * 0.9
    threshold_upper = reference_avg_distance * 1.1

    selected_ids = unrolled_df_3[(unrolled_df_3['distance'] >= threshold_lower) & (unrolled_df_3['distance'] <= threshold_upper)]['id_start'].unique()
    
    sorted_selected_ids = sorted(selected_ids)
    
    return sorted_selected_ids


selected_ids = find_ids_within_ten_percentage_threshold(unrolled_df_3, reference_value)
print(selected_ids)
    return df


def calculate_toll_rate(df)->pd.DataFrame():
    """
    Calculate toll rates for each vehicle type based on the unrolled DataFrame.

    Args:
        df (pandas.DataFrame)

    Returns:
        pandas.DataFrame
    """
    # Wrie your logic here
unrolled_df = df_3
def calculate_toll_rate(unrolled_df):

    unrolled_df['moto'] = 0.0
    unrolled_df['car'] = 0.0
    unrolled_df['rv'] = 0.0
    unrolled_df['bus'] = 0.0
    unrolled_df['truck'] = 0.0


    rate_coefficients = {'moto': 0.8, 'car': 1.2, 'rv': 1.5, 'bus': 2.2, 'truck': 3.6}

    
    for vehicle_type, rate_coefficient in rate_coefficients.items():
        unrolled_df[vehicle_type] = unrolled_df['distance'] * rate_coefficient

    return unrolled_df

unrolled_df_with_toll_rates = calculate_toll_rate(unrolled_df_3)
print(unrolled_df_with_toll_rates)
    return df


def calculate_time_based_toll_rates(df)->pd.DataFrame():
    """
    Calculate time-based toll rates for different time intervals within a day.

    Args:
        df (pandas.DataFrame)

    Returns:
        pandas.DataFrame
    """
    # Write your logic here
from datetime import time, timedelta, datetime

def calculate_time_based_toll_rates(df_3):
    
    weekday_time_ranges = [(time(0, 0, 0), time(10, 0, 0)),
                           (time(10, 0, 0), time(18, 0, 0)),
                           (time(18, 0, 0), time(23, 59, 59))]

    weekend_time_range = (time(0, 0, 0), time(23, 59, 59))

   
    time_based_rates = pd.DataFrame(columns=['start_day', 'start_time', 'end_day', 'end_time'] + df_3.columns.tolist())

   
    def add_rows(start_time, end_time):
        for day in range(1, 8):
            start_datetime = datetime.combine(datetime.today(), start_time) + timedelta(days=day - 1)
            end_datetime = datetime.combine(datetime.today(), end_time) + timedelta(days=day - 1)

            time_based_rates.loc[len(time_based_rates)] = [
                start_datetime.strftime('%A'),
                start_time,
                end_datetime.strftime('%A'),
                end_time,
                *([0] * len(df_3.columns)) 
            ]

   
    for start_time, end_time in weekday_time_ranges:
        add_rows(start_time, end_time)

    
    add_rows(*weekend_time_range)

    return time_based_rates


time_based_rates = calculate_time_based_toll_rates(df_3)
print(time_based_rates)
    return df
