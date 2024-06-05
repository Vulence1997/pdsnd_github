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
    print('Hello! Let\'s explore some US bikeshare data together!')

    # Define valid options for user input as a dictionary
    valid_options = {
        'city': ['new york city', 'chicago', 'washington'],
        'month': ['all', 'january', 'february', 'march', 'april', 'may', 'june'],
        'day': ['all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
    }

    # Prompt user for city, month, and day inputs
    user_inputs = {}
    for category, options in valid_options.items():
        user_input = input(f'Please enter the {category} name ({", ".join(options)}): ').strip().lower()
        while user_input not in options:
            print(f'Invalid input for {category} name. Please choose from the provided options.')
            user_input = input(f'Please enter the {category} name ({", ".join(options)}): ').strip().lower()
        user_inputs[category] = user_input

    return user_inputs['city'], user_inputs['month'], user_inputs['day']



def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    
    # Load data for the input city
    df = pd.read_csv(CITY_DATA[city])

    # Convert 'Start Time' column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # Extract month and day of teh week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()

    # Filter by month, if applicable
    if month != 'all':
        # Convert month name to month number
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # Filter by month to create the new dataframe
        df = df[df['month'] == month]

    # Filter by day of the week if applicable
    if day != 'all':
        # Filter by day of the week to create a new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""
    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # Display the most common month
    common_month = df['month'].mode()[0]
    print("The most common month is:", common_month)

    # Display the most common day of week
    common_day_of_week = df['day_of_week'].mode()[0]
    print("The most common day of week is:", common_day_of_week)

    # Display the most common start hour
    df['start_hour'] = df['Start Time'].dt.hour
    common_start_hour = df['start_hour'].mode()[0]
    print("The most common start hour is:", common_start_hour)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""
    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # Display most commonly used start station
    common_start_station = df['Start Station'].mode()[0]
    print("The most commonly used start station is:", common_start_station)

    # Display most commonly used end station
    common_end_station = df['End Station'].mode()[0]
    print("The most commonly used end station is: ", common_end_station)

    # Display most frequent combination of start station and end station trip
    df['Trip'] = df['Start Station'] + ' to ' + df['End Station']
    common_trip = df['Trip'].mode()[0]
    print("The most frequent combination of start station and end station trip is:", common_trip)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""
    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # Display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print("Total travel time:", total_travel_time)

    # Display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print("The mean travel time is:", mean_travel_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""
    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_types_counts = df['User Type'].value_counts()
    print("Counts of user types:")
    print(user_types_counts)

    # Display counts of gender
    if 'Gender' in df.columns:
        gender_counts = df['Gender'].value_counts()
        print("\nCounts of gender:")
        print(gender_counts)
    else:
        print("\nGender information is not available in this dataset.")

    # Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns:
        earliest_birth_year = df['Birth Year'].min()
        most_recent_birth_year = df['Birth Year'].max()
        most_common_birth_year = df['Birth Year'].mode()[0]

        print("\nEarliest birth year:", earliest_birth_year)
        print("Most recent birth year:", most_recent_birth_year)
        print("Most common birth year:", most_common_birth_year)
    else:
        print("\nBirth year information is not available in this dataset.")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        # Prompt user if they want to see raw data
        while True:
            raw_data_display = input('\nWould you like to view raw data? Enter yes or no.\n').lower()
            if raw_data_display in ['yes', 'no']:
                break
            else:
                print('Invalid input. Please enter "yes" or "no".')

        if raw_data_display == 'yes':
            # Prompt user for the number of lines of raw data
            while True:
                num_lines = input('How many lines of raw data would you like to view? Please enter a number: ')
                try:
                    num_lines = int(num_lines)
                    display_raw_data(df, num_lines)
                    break
                except ValueError:
                    print('Invalid input. Please enter a valid number.')

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break

def display_raw_data(df, num_lines):
    """Display specified number of lines of raw data from the DataFrame."""
    # Display specified number of lines of raw data
    print(df.head(num_lines))

    # Check if there is more data to display
    if num_lines < len(df):
        while True:
            more_data = input('\nWould you like to view more raw data? Enter yes or no.\n').lower()
            if more_data in ['yes', 'no']:
                break
            else:
                print('Invalid input. Please enter "yes" or "no".')

        if more_data == 'yes':
            display_raw_data(df[num_lines:], num_lines)

if __name__ == "__main__":
	main()
