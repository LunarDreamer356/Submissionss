import pandas as pd


def generate_car_matrix(df)->pd.DataFrame:
    """
    Creates a DataFrame  for id combinations.

    Args:
        df (pandas.DataFrame)

    Returns:
        pandas.DataFrame: Matrix generated with 'car' values, 
                          where 'id_1' and 'id_2' are used as indices and columns respectively.
    """
    # Write your logic here
    def generate_car_matrix(df):
    car_matrix = df.pivot(index='id_1', columns='id_2', values='car').fillna(0).astype(int)
    
    car_matrix.values[[range(car_matrix.shape[0])]*2]
    
    return car_matrix

result_matrix = generate_car_matrix(df)
print(result_matrix)


def get_type_count(df)->dict:
    """
    Categorizes 'car' values into types and returns a dictionary of counts.

    Args:
        df (pandas.DataFrame)

    Returns:
        dict: A dictionary with car types as keys and their counts as values.
    """
    # Write your logic here
     def get_type_count(df):
    return dict(sorted(pd.cut(df['car'], bins=[-float('inf'), 15, 25, float('inf')],
                               labels=['low', 'medium', 'high'], right=False)
                               .value_counts().items()))


result_type_count = get_type_count(df)
print(result_type_count)


def get_bus_indexes(df)->list:
    """
    Returns the indexes where the 'bus' values are greater than twice the mean.

    Args:
        df (pandas.DataFrame)

    Returns:
        list: List of indexes where 'bus' values exceed twice the mean.
    """
    # Write your logic here
def get_bus_indexes(df):
    
    mean_bus_value = df['bus'].mean()

    
    return sorted(df[df['bus'] > 2 * mean_bus_value].index)

result_bus_indexes = get_bus_indexes(df)
print(result_bus_indexes)

    return list()


def filter_routes(df)->list:
    """
    Filters and returns routes with average 'truck' values greater than 7.

    Args:
        df (pandas.DataFrame)

    Returns:
        list: List of route names with average 'truck' values greater than 7.
    """
    # Write your logic here
    def filter_routes(df):
   
    return sorted(df.loc[df.groupby('route')['truck'].transform('mean') > 7, 'route'].unique())

result_filtered_routes = filter_routes(df)
print(result_filtered_routes)


    return list()

def multiply_matrix(matrix)->pd.DataFrame:
    """
    Multiplies matrix values with custom conditions.

    Args:
        matrix (pandas.DataFrame)

    Returns:
        pandas.DataFrame: Modified matrix with values multiplied based on custom conditions.
    """
    # Write your logic here
    
    modified_result_matrix = generate_car_matrix(df).applymap(lambda x: round(x * 0.75, 1) if x > 20 else round(x * 1.25, 1))
print(modified_result_matrix)


    return matrix

def time_check(df)->pd.Series:
    """
    Use shared dataset-2 to verify the completeness of the data by checking whether the timestamps for each unique (`id`, `id_2`) pair cover a full 24-hour and 7 days period

    Args:
        df (pandas.DataFrame)

    Returns:
        pd.Series: return a boolean series
    """
    # Write your logic here
    def time_check(df_2):
    df_2['start_datetime'] = pd.to_datetime(df_2['startDay'] + ' ' + df_2['startTime'], errors='coerce')
    df_2['end_datetime'] = pd.to_datetime(df_2['endDay'] + ' ' + df_2['endTime'], errors='coerce')
    
    result = df_2.groupby(['id', 'id_2']).apply(lambda group: any([
        group['start_datetime'].min() != pd.to_datetime('00:00:00', errors='coerce'),
        group['end_datetime'].max() != pd.to_datetime('23:59:59', errors='coerce'),
        (group['end_datetime'] - group['start_datetime']).max() > pd.Timedelta(days=7)
    ]))
    
    return result

result_series = time_check(df_2)
print(result_series)

    return pd.Series()
