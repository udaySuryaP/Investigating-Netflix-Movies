import matplotlib.pyplot as plt
import pandas as pd

# Read in the Netflix CSV as a DataFrame
netflixDataframe = pd.read_csv("netflix_data.csv")

# Subset the DataFrame for type "Movie"
netflixSubset = netflixDataframe[netflixDataframe["type"] == "Movie"]

# Filter the data to keep only movies released in the 1990s
movies1990s = netflixSubset[
    (netflixSubset["release_year"] >= 1990) & (netflixSubset["release_year"] < 2000)
]

# Visualize the duration column of your filtered data to see the distribution of movie durations
plt.hist(movies1990s["duration"])
plt.title("Distribution of Movie Durations in the 1990s")
plt.xlabel("Duration (in minutes)")
plt.ylabel("Number of movies")
plt.show()

# Filter the data again to keep only the Action movies
actionMovies = movies1990s[movies1990s["genre"] == "Action"]

duration = 100
shortMovies = 0

# Iterate over the labels and rows of the DataFrame and check if the duration is less than 90, if it is, add 1 to the counter, if it isn't, the counter should remain the same
for label, row in actionMovies.iterrows():
    if row["duration"] < 90:
        shortMovies += 1

print(shortMovies)
