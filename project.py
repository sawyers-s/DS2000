#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Sophie Sawyers
DS2001 - Economics
Final Project
December 5, 2023
"""

import csv
import matplotlib.pyplot as plt
import numpy as np

# First, write a function to create a list of keys and values for a dictionary.

def create_keys_values_list(filename):
    """
    This function isolates column 0 of the csv file (album rank), with each 
    element in this column becoming a dictionary key. The key's values come 
    from the rest of the row. 

    Parameters
    ----------
    filename : String
        The name of the file we want to make our 2D list from

    Returns
    -------
    A 2D list of [key, value] "little lists"

    """
    # Open the file and read in the data. Skip over the file header. 
    
    with open(filename, "r", encoding='latin-1') as data_f:
        
        reader = csv.reader(data_f)
        file_header = next(reader)
        
        # Initialize an empty list for keys and values.
    
        keys_and_values_list = []
        
        # For each row of data, designate the first element as a key and the
        # remaining elements as the key's values. Add to keys_and_values list.
    
        for row in reader:
            
            key = row[0]
            value = row[1:]
            
            keys_and_values_list.append([key, value])
            
        return(keys_and_values_list)

# Next, write a function that creates a dictionary from a pre-existing list
# like the one created above.    

def make_dictionary(list_name):
    """
    This function creates a dictionary from a 2D list of values.

    Parameters
    ----------
    list_name : List
        The list read in from the csv file that we want to use to make a 
        dictionary

    Returns
    -------
    A dictionary with album rank as keys and year, album name,
    artist, genre, and subgenre as values

    """
    # Create an empty dictionary.
    
    album_dictionary = {}
    
    # For each "little list" within the given list, designate the element in 
    # the first position as the key and the next element (containing the list
    # of key values) as the value. Add the key and its value to the dictionary.
    
    for element in list_name:
        
            dict_key = element[0]
            dict_value = element[1]
            
            album_dictionary[dict_key] = dict_value
            
    return album_dictionary

# Write a function to determine when albums were released.

def year_counts(dictionary_name):
    """
    This function extracts album years from the dictionary created and counts
    the total number of albums released before/in 1990 and after 1990.

    Parameters
    ----------
    dictionary_name : Dictionary
        The dictionary created using album rank as keys and year, album name,
        artist, genre, and subgenre as values

    Returns
    -------
    The percentage of albums released before/in 1990 and the percentage of albums 
    released after 1990

    """
    # Designate the album dictionary created above as dictionary_name.
    
    album_dictionary = dictionary_name
    
    # Initialize counters for year frequencies.
    
    before_1990 = 0
    
    after_1990 = 0
    
    # For each album year in the album dictionary, if its value is less than or
    # equal to 1990, add 1 to the before_1990 counter. If its value is more 
    # than 1990, add 1 to the after_1990 counter.
    
    for album in album_dictionary:
        
        album_year = album_dictionary[album][0]
        
        # Convert album_year from string to float.
        
        album_year = float(album_year)
        
        if album_year <= 1990:
            before_1990 += 1
            
        else:
            after_1990 +=1
            
    # Calculate the percentage of albums released before or in 1990 and the
    # percentage of albums released after 1990.
    
    before_1990_pct = before_1990/500 * 100
    
    after_1990_pct = after_1990/500 * 100
    
    return before_1990_pct, after_1990_pct
    
# Write a function to count the number of albums in each genre.

def genre_counts(dictionary_name):
    """
    This function extracts album genres from the dictionary created and counts
    the total number of albums per genre.

    Parameters
    ----------
    dictionary_name : Dictionary
        The dictionary created using album rank as keys and year, album name,
        artist, genre, and subgenre as values

    Returns
    -------
    Dictionary containing album genre as keys and the number of albums in 
    each genre as values

    """
    # Designate the album dictionary created above as dictionary_name.
    
    album_dictionary = dictionary_name
    
    # Initialize an empty dictionary for genre frequencies.
    
    genre_frequency_dict = {}
    
    # For each album in album_dictionary, determine its genre. If its genre is 
    # found in genre_frequency_dict, add one to its frequency. If it is not in 
    # genre_frequency_dict, set initial frequency to 1.
    
    for album in album_dictionary:
        
        album_genre = album_dictionary[album][3]
        
        if album_genre in genre_frequency_dict:
            genre_frequency_dict[album_genre] += 1
        
        else:
            genre_frequency_dict[album_genre] = 1
            
    # Sort the dictionary in descending order. This syntax was found on
    # https://www.freecodecamp.org/news/sort-dictionary-by-value-in-python/.
    
    sorted_genre_frequency = sorted(genre_frequency_dict.items(), 
                                         key = lambda x:x[1], reverse = True)
    
    cleaned_genre_frequency_dict = dict(sorted_genre_frequency)
    
    return cleaned_genre_frequency_dict

# Write a function to add gender data to each album's values in the dictionary.

def count_genders(filename, dictionary_name):
    """
    This function opens the given csv file, reads in the gender data, and adds
    the gender of the artist to the corresponding values list to the album
    dictionary created above.

    Parameters
    ----------
    filename : String
        The name of the file we want to read in the gender data from
        
    dictionary_name: Dictionary
        The dictionary created using album rank as keys and year, album name,
        artist, genre, and subgenre as values

    Returns
    -------
    An updated album dictionary using album rank as keys and year, album name,
    artist, genre, subgenre, and gender as values

    """
    # Designate the album dictionary created above as dictionary_name.
    
    album_dictionary = dictionary_name
    
    # Open the file and read in the data. Skip over the file header. 
    
    with open(filename, "r") as data_f:
        
        reader = csv.reader(data_f)
        file_header = next(reader)
        
        # For each row of data, isolate album ranking and corresponding gender.
        # Add the gender data to the list of value of rankings of the
        # corresponding album in album_dictionary. 
        
        for row in reader:
            
            album_rank = row[0]
            artist_gender = row[2]
            
            album_dictionary[album_rank].append(artist_gender)
            
    return album_dictionary

# Write a function to determine the gender of the top n artists.

def top_genders(dictionary_name, n=5):
    """
    This function extracts artist genders from the dictionary created and counts
    the number of artists per gender for the top n artists.

    Parameters
    ----------
    dictionary_name : Dictionary
        The dictionary created using album rank as keys and year, album name,
        artist, genre, subgenre, and gender as values
        
    n : Float, optional
        The top number of artists we want to examine genders for. 
        The default is 5.

    Returns
    -------
    The number of top n artists that are male, the number of top n artists that
    are female, and the number of top n artists that are "mixed" (have male
    and female members)

    """
    # Designate the album dictionary created above as dictionary_name.
    
    album_dictionary = dictionary_name
    
    # Initialize counters for gender frequencies.
    
    male_artists = 0
    
    female_artists = 0
    
    mixed_artists = 0
    
    # Convert the given dictionary to a list. Slice the list to only include
    # top n artists' data.
    
    top_artists = list(album_dictionary.items())[:n]
    
    # For the artists in top_artists, if they are male, add 1 to the male
    # counter. If they are female, add 1 to the female counter. If they are 
    # mixed, add 1 to the mixed counter.
    
    for artist_data in top_artists:
        
        rank, [year, album, artist, genre, subgenre, gender] = artist_data
        
        if gender == "Male":
            male_artists += 1
            
        elif gender == "Female":
            female_artists +=1
            
        else:
            mixed_artists += 1
            
    return male_artists, female_artists, mixed_artists
    
# Write a function to create a barplot of album years and frequency.

def plot_year_frequencies(dictionary_name):
    """
    This function extracts album years from the dictionary created and counts
    the frequency of each year. The function then plots the year and its 
    frequency in a barplot. 

    Parameters
    ----------
    dictionary_name : Dictionary
       The dictionary created using album rank as keys and year, album name,
       artist, genre, subgenre, and gender as values 

    Returns
    -------
    None.

    """
    # Designate the album dictionary created above as dictionary_name.

    album_dictionary = dictionary_name
    
    # Initialize an empty dictionary for year frequencies.
    
    year_frequency_dict = {}
    
    # For each album in album_dictionary, determine its year. If its year is 
    # found in year_frequency_dict, add one to its frequency. If it is not in 
    # year_frequency_dict, set initial frequency to 1.
    
    for album in album_dictionary:
        
        album_year = album_dictionary[album][0]
        
        if album_year in year_frequency_dict:
            year_frequency_dict[album_year] += 1
        
        else:
            year_frequency_dict[album_year] = 1
    
    # Sort the dictionary in ascending order by year. This syntax was found on
    # https://www.freecodecamp.org/news/sort-dictionary-by-value-in-python/.
    
    sorted_year_frequency = sorted(year_frequency_dict.items(), 
                                         key = lambda x:x[0], reverse = False)
    
    cleaned_year_frequency_dict = dict(sorted_year_frequency)
            
    # Designate x- and y-values.
    
    x_values = cleaned_year_frequency_dict.keys()
    
    y_values = cleaned_year_frequency_dict.values()
    
    # Create a barplot.
    
    plt.bar(x_values, y_values, color = "blue")
    plt.xlabel("Year")
    plt.ylabel("Frequency")
    plt.xticks(ticks = ["1955", "1960", "1965", "1970", "1975", "1980", "1985", 
                        "1990", "1995", "2000", "2005", "2010"], fontsize = 8)
    plt.title("Frequency of Album Rankings by Year")
    plt.show()
    
# Write a function to create a barplot of album genres and frequency.

def plot_genre_frequencies(dictionary_name):
    """
    This function plots album genres and their frequencies in a barplot. 

    Parameters
    ----------
    dictionary_name : Dictionary
        The dictionary created using album rank as keys and year, album name,
        artist, genre, subgenre, and gender as values

    Returns
    -------
    None.

    """
    # Designate the album dictionary created above as dictionary_name.

    album_dictionary = dictionary_name
    
    # Extracts album genres from the dictionary and count the total number of 
    # albums per genre using the genre_counts function.
    
    genre_dictionary = genre_counts(album_dictionary)
    
    # Designate x- and y-values.
    
    x_values = genre_dictionary.keys()
    
    y_values = genre_dictionary.values()
    
    # Create a barplot. We must increase the size of the figure to display all
    # data. Colors are randomized for each genre using syntax found on
    # https://www.statology.org/matplotlib-random-color/.
    
    plt.figure(figsize=(20, 6))
    plt.bar(x_values, y_values, color = np.random.rand(len(x_values),3))
    plt.xlabel("Genre", fontsize = 14)
    plt.ylabel("Frequency", fontsize = 14)
    plt.xticks(rotation = "vertical", fontsize = 12)
    plt.title("Frequency of Album Genres", fontsize = 16)
    plt.show()
    
# Write a function to create a barplot of artist genders and frequency.

def plot_gender_frequencies(dictionary_name, n=5):
    """
    This function plots artist genders and their frequencies in a barplot. 

    Parameters
    ----------
    dictionary_name : Dictionary
        The dictionary created using album rank as keys and year, album name,
        artist, genre, subgenre, and gender as values 
        
    n : Float, optional
        The top number of artists we want to examine gender frequencies for. 
        The default is 5.

    Returns
    -------
    None.

    """
    # Designate the album dictionary created above as dictionary_name.

    album_dictionary = dictionary_name
    
    # Determine the gender of the top n artists using the top_genders function
    # and count their frequencies. Convert result to a list.
    
    gender_data = top_genders(album_dictionary, n)
    
    gender_data = list(gender_data)
    
    # Initialize empty dictionary for gender data.
    
    gender_dictionary = {}
    
    # Add frequencies to dictionary for each gender.
    
    gender_dictionary["Male"] = gender_data[0]
    
    gender_dictionary["Female"] = gender_data[1]
    
    gender_dictionary["Mixed"] = gender_data[2]
    
    # Designate x- and y-values.
    
    x_values = gender_dictionary.keys()
    
    y_values = gender_dictionary.values()
    
    # Create colors list.
    
    colors = ["blue", "red", "green"]
    
    # Create a barplot.
    
    plt.bar(x_values, y_values, color = colors)
    plt.xlabel("Gender")
    plt.ylabel("Frequency")
    plt.xticks(fontsize = 8)
    plt.title("Frequency of Album Rankings by Gender")
    plt.show()


# Finally, write the main function using the functions defined above.

if __name__ == "__main__":
    
    # First, create list of keys and values for a dictionary from album data.
    
    initial_album_list = create_keys_values_list("albumlist.csv")

    # Create a dictionary from this list.

    initial_album_dict = make_dictionary(initial_album_list)

    # Calculate the percentage of albums released before or in 1990 and
    # percentage of albums released after 1990.

    before_1990_pct, after_1990_pct = year_counts(initial_album_dict)
    
    print("The percentage of albums released before or in 1990 is", 
          round(before_1990_pct,4), "\n")
    
    print("The percentage of albums released after 1990 is", 
          round(after_1990_pct, 4),"\n")
    
    # Count the number of albums in each genre and determine which is most
    # popular.

    album_genre_freq = genre_counts(initial_album_dict)
    
    print("The number of albums per genre is (from most popular to least popular):",
          album_genre_freq, "\n")
        
    # Add gender data from "genders.csv" to each album's dictionary values.

    updated_album_dict = count_genders("genders.csv", initial_album_dict)
    
    # Determine the genders of the top five artists.

    male_artists, female_artists, mixed_artists = top_genders(updated_album_dict)
    
    print("Of the top desired artists,", male_artists, "are male,", 
          female_artists, "are female, and", mixed_artists, 
          "have male and female members.\n")
    
    # Plot album years and year frequency (number of times album year is in data).

    print("Figure 1:\n")
    plot_year_frequencies(updated_album_dict)
    print("\n")
    
    # Plot album genres and their frequencies.

    print("Figure 2:\n")
    plot_genre_frequencies(updated_album_dict)
    print("\n")
    
    # Plot artist genders and their frequencies for all 500 artists.

    print("Figure 3:\n")
    plot_gender_frequencies(updated_album_dict, n=500)
    