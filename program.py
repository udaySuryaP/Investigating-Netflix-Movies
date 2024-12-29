https://www.datacamp.com/datalab/w/7165ab75-3dac-4e50-8f8d-40b0d72aa35c/edit?emitCellOutputs=false&reducedMenuBar=true&showExploreMore=false&showLeftNavigation=false&showNavBar=false&showPublicationButton=false&showOnlyRelevantSampleIntegrationIds[]=89e17161-a224-4a8a-846b-0adc0fe7a4b1&showOnlyRelevantSampleIntegrationIds[]=e0c96696-ae0a-46fb-b6f9-1a43eb428ecb&showOnlyRelevantSampleIntegrationIds[]=b1fcb109-b4fe-4543-bc98-681df8c4dc6e&showOnlyRelevantSampleIntegrationIds[]=fcf37a0e-f8bd-4c85-95a5-201d3eebea48&showOnlyRelevantSampleIntegrationIds[]=db697c09-0402-4a02-b327-26018dc2ecce&showOnlyRelevantSampleIntegrationIds[]=7569175e-98be-4c89-9873-c20f699a9cc7&fetchUnlistedSampleIntegrationIds[]=7569175e-98be-4c89-9873-c20f699a9cc7#937acf3c-c077-4ca6-8d90-8f6dd4d13c54


# Importing pandas and matplotlib
import pandas as pd
import matplotlib.pyplot as plt

# Read in the Netflix CSV as a DataFrame
netflix_df = pd.read_csv("netflix_data.csv")

# Subset the DataFrame for type "Movie"
netflix_subset = netflix_df[netflix_df["type"] == "Movie"]

# Filter the to keep only movies released in the 1990s
# Start by filtering out movies that were released before 1990
subset = netflix_subset[(netflix_subset["release_year"] >= 1990)]

# And then do the same to filter out movies released on or after 2000
movies_1990s = subset[(subset["release_year"] < 2000)]

# Another way to do this step is to use the & operator which allows you to do this type of filtering in one step
# movies_1990s = netflix_subset[(netflix_subset["release_year"] >= 1990) & (netflix_subset["release_year"] < 2000)]

# Visualize the duration column of your filtered data to see the distribution of movie durations
# See which bar is the highest and save the duration value, this doesn't need to be exact!
plt.hist(movies_1990s["duration"])
plt.title('Distribution of Movie Durations in the 1990s')
plt.xlabel('Duration (minutes)')
plt.ylabel('Number of Movies')
plt.show()

duration = 100

# Filter the data again to keep only the Action movies
action_movies_1990s = movies_1990s[movies_1990s["genre"] == "Action"]

# Use a for loop and a counter to count how many short action movies there were in the 1990s

# Start the counter
short_movie_count = 0

# Iterate over the labels and rows of the DataFrame and check if the duration is less than 90, if it is, add 1 to the counter, if it isn't, the counter should remain the same
for label, row in action_movies_1990s.iterrows() :
    if row["duration"] < 90 :
        short_movie_count = short_movie_count + 1
    else:
        short_movie_count = short_movie_count

print(short_movie_count)

# A quicker way of counting values in a column is to use .sum() on the desired column
# (action_movies_1990s["duration"] < 90).sum()