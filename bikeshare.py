import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washingtno). HINT: Use a while loop to handle invalid inputs
    city = input('Choose city (chicago, new york city, washingtno): ' ).lower()
    while city not in CITY_DATA:
        continue

    # TO DO: get user input for month (all, january, february, ... , june)
    month = input('Choose month (all, january, february, ....): ').title()

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day = input('Choose a day (all, monday, tuesday....): ').title()

    # What to do with nan values:
    handle_na = input('Choose how to handle nans choose >> delete , fill or no \n no is to leave nan values! ')
    if handle_na == 'fill':
        fillvalue = input('Enter the fill value ')
    else:
        fillvalue = 0

    print('-'*40)
    return city, month, day, handle_na, fillvalue


def load_data(city, month, day, handle_na, fillvalue):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    # City data
    df = pd.read_csv(CITY_DATA[city])
    # creating the month column
    df['month'] = pd.to_datetime(df['Start Time']).dt.strftime('%B')

    #creating the day column
    df['day_of_week'] = pd.to_datetime(df['Start Time']).dt.strftime('%A')

    # filtering by month
    if month != 'All':
        filter_month = df['month'] == month
        df = df[filter_month]


    #filterinh by day
    if day != 'All':
        filter_day = df['day_of_week'] == day
        df = df[filter_day]
    
    if handle_na == 'delete':
        df.dropna()
    elif handle_na == 'fill':
        df.fillna(int(fillvalue))
    else:
        df.fillna(0)




    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month    
    mode_month = df['month'].mode()[0]
    print(f'the most common month is { mode_month}' )

    # TO DO: display the most common day of week
    mode_day_week = df['day_of_week'].mode()[0]
    print(f'the most common day of week is {mode_day_week}')

    # TO DO: display the most common start hour
    df['Start Hour'] = pd.to_datetime(df['Start Time']).dt.hour
    mode_hour = df['Start Hour'].mode()[0]
    print(f'the most common start hour is {mode_hour}')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    common_start_station = df['Start Station'].mode()[0]
    print(f'most commonly used start station is { common_start_station}')

    # TO DO: display most commonly used end station
    common_end_station = df['End Station'].mode()[0]
    print(f'most commonly used end station is { common_end_station}')

    # TO DO: display most frequent combination of start station and end station trip
    df['Trip Start End'] = df['Start Station'] + ' to ' + df['End Station']
    most_used_line = df['Trip Start End'].mode()[0]
    print(f'most frequent combination of start station and end station trip is { most_used_line}')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    if 'Trip Duration' in df.columns:
        total_time = df['Trip Duration'].sum()
        print(f'total travel time is { total_time} seconds')
        
        # TO DO: display mean travel time
        mean_travel_time = df['Trip Duration'].mean() 
        print(f'mean travel time is { mean_travel_time} seconds')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    if 'User Type' in df.columns:
        user_type = df['User Type'].value_counts()
        print(f'counts of user types \n { user_type }')

    # TO DO: Display counts of gender
    if 'Gender' in df.columns:
        genders = df['Gender'].value_counts()
        print(f'counts of user types { genders}')

    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns:
        most_recent_bd = df['Birth Year'].max()
        earliest_bd = df['Birth Year'].min()
        most_common_bd = df['Birth Year'].mode()[0]
        print(f'earliest birth year is {earliest_bd}')
        print(f'most recent birth year is {most_recent_bd}')
        print(f'most common birth year is {most_common_bd}')
    

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
# the show function is to show 5 rows of data at a time.
def show():
  #Asking to show the results >>>
    to_show = input('\nWould you like to see 5 rows of data? Enter yes or no.\n')
    if to_show.lower != 'no':
        start_row = 0
        end_row = 4
        print(df.iloc[start_row:end_row])
        ## Asking if want to show more >>>>
        
        confirmation = input('\nWould you like to see an other 5 rows of data? Enter yes or no.\n')
        if confirmation.lower() != 'no':
          ## Increaing by 5
            start_row += 5
            end_row += 5
            print(df.iloc[start_row:end_row])
    
def main():
    while True:
        city, month, day, handle_na, fillvalue = get_filters()
        df = load_data(city, month, day, handle_na, fillvalue)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        # print(df['Birth Year'])
        show()

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    main()
