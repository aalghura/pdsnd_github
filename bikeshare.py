import time
import pandas as pd
import numpy as np

#Udacity Project
CITY_DATA = { 'Chicago': 'chicago.csv','New York': 'new_york_city.csv','Washington': 'washington.csv' }
CITIES = ['Chicago','New York', 'Washington']
MONTHS = ['All', 'January', 'February', 'March', 'April', 'May', 'June']
DAYS = ['All', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # Getting user input for city (chicago, new york city, washington). While loops to handle invalid inputs
    while True:
        city = input('Please, select one city from the following list to explore: Chicago, New York, or Washington\n ').title()
        if city in CITIES:
            print('-'*40)
            break
        else:
            print('-----Please enter a valid city-----')

    # Getting user input for month (all, january, february, ... , june)
    while True:
        month = input('Please, select one month from the following list to explore:\n  All, January, February, March, April, May, June\n ').title()
        if month in MONTHS:
            print('-'*40)
            break
        else:
            print('-----Please enter a valid month-----')

    # Getting user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input('Please, select one day from the following list to explore:\n  All, Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, or Saturday\n ').title()
        if day in DAYS:
            print('-'*40)
            break
        else:
            print('-----Please enter a valid day-----')

    return city, month, day

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
    # city is used to load the data file into Pandas DataFrame
    cityfile = CITY_DATA[city]
    df = pd.read_csv(cityfile)

    # Convert to datetime column
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # Create new columns from extracted month, weekday, and hour from Start Time CVS column
    df['Month'] = df['Start Time'].dt.month
    df['Week_Day'] = df['Start Time'].dt.weekday_name
    df['Hour'] = df['Start Time'].dt.hour

    # Filter according to month if requested
    if month != 'All':
        month = MONTHS.index(month)
        df = df[df['Month'] == month]

    # Filter according to day if requested
    if day != 'All':
        df = df[df['Week_Day'] == day]
    #print(df)
    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""
    print('\n'+'*'*80)
    print('Calculating The Most Frequent Times of Travel...')
    start_time = time.time()
    print('*'*80)

    # Display the most common month
    Most_Common_Month = df['Month'].mode()[0]
    print('The most common month in the filtered data set was found to be:\n', MONTHS[Most_Common_Month])
    print('\n'+'-'*80)
    # Display the most common day of week
    Most_Common_Day = df['Week_Day'].mode()[0]
    print('The most common day in the filtered data set was found to be:\n', Most_Common_Day)
    print('\n'+'-'*80)
    # Display the most common start hour
    Most_Common_Hour = df['Hour'].mode()[0]
    print('The most common hour in the filtered data set was found to be:\n', Most_Common_Hour)
    print('\n'+'-'*80)
    print("*********This took %s seconds*********" % (time.time() - start_time))
    print('-'*80)

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""
    print('\n'+'*'*80)
    print('Calculating The Most Popular Stations and Trip...')
    start_time = time.time()
    print('*'*80)

    # Display most commonly used start station
    Commonly_Used_Start_Station = df['Start Station'].mode()[0]
    print('The most commonly used start station from the filtered data is:\n' + Commonly_Used_Start_Station)
    print('\n'+'-'*80)

    # Display most commonly used end station
    Commonly_Used_End_Station = df['End Station'].mode()[0]
    print('The most commonly used end station from the filtered data is:\n' + Commonly_Used_End_Station)
    print('\n'+'-'*80)

    # Display most frequent combination of start station and end station trip
    Commonly_Used_Start_End = (df['Start Station'] + '-' + df['End Station']).mode()[0]
    print("The most commonly used combination of start & end stations from the filtered data is:\n" + str(Commonly_Used_Start_End.split('-')))

    print('\n'+'-'*80)
    print("*********This took %s seconds*********" % (time.time() - start_time))
    print('-'*80)

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""
    print('\n'+'*'*80)
    print('Calculating Trip Duration...')
    start_time = time.time()
    print('*'*80)

    # Display total travel time
    Total_Travel_Time = df['Trip Duration'].sum()
    print("The total travel time in seconds from the given data is found to be:\n", Total_Travel_Time)
    print('\n'+'-'*80)

    # Display mean travel time
    Travel_Time_Mean = df['Trip Duration'].mean()
    print("The travel time mean in seconds from the given data is found to be:\n", Travel_Time_Mean)
    print('\n'+'-'*80)

    print('\n'+'-'*80)
    print("*********This took %s seconds*********" % (time.time() - start_time))
    print('-'*80)

def user_stats(df):
    """Displays statistics on bikeshare users."""
    print('\n'+'*'*80)
    print('Calculating User Stats...')
    start_time = time.time()
    print('*'*80)

    # Display counts of user types
    User_Types = df['User Type'].value_counts()
    print('The counts of user types:')
    print('-'*80)
    for index, count in enumerate(User_Types):
        print("     Type:{} with Count:{}\n".format(User_Types.index[index],count))
    # Display counts of gender
    print('-'*80)
    print('The counts of gender:')
    print('-'*80)
    if 'Gender' in df.columns:
        Gender_Counts = df['Gender'].value_counts()
        for index, count in enumerate(Gender_Counts):
            print("     Gender:{} with Count:{}\n".format(Gender_Counts.index[index],count))

    # Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns:
        Birth_Year = df['Birth Year']
        Earliest_Year = Birth_Year.min()
        Most_Recent_Year = Birth_Year.max()
        Most_Common_Year = Birth_Year.value_counts().idxmax()
        print('-'*80)
        print('Birth Stats')
        print('-'*80)
        print('The earliest birth year is: {}\nThe most recent birth year is: {}\nThe most common year of birth is: {}\n'.format(int(Earliest_Year),int(Most_Recent_Year),int(Most_Common_Year)))
        print('\n')

    print('\n'+'-'*80)
    print("*********This took %s seconds*********" % (time.time() - start_time))
    print('-'*80)

def raw_data(df):
    # This function preview raw data starting from first 5 rows and then loops until user opt out
    counter = 0
    while True:
        raw_data_answer = input('Would you like to view 5 rows of raw data? yes or no?\n')
        if raw_data_answer == 'yes' or raw_data_answer == 'Yes':
            counter += 1
            results =  df.iloc[counter*5-5:counter*5]
            print(results)
        elif raw_data_answer == 'no' or raw_data_answer == 'No':
            break
        else:
            print('Please enter either yes or no')

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        raw_data(df)


        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
