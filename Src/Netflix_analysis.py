import pandas as pd

df = pd.read_csv(r"C:\Users\Renuk\Downloads\archive\netflix_titles.csv")

print("First 5 Rows:")
print(df.head())

print("\nShape:")
print(df.shape)

print("\nColumns:")
print(df.columns)

print("\nInfo:")
df.info()
print("\nMissing Values:")
print(df.isnull().sum())
print("\nDuplicate Rows:")
print(df.duplicated().sum())
# Remove duplicates
df = df.drop_duplicates()

# Convert date_added column into datetime format
df['date_added'] = pd.to_datetime(df['date_added'],format="mixed")

print("\nCleaned Successfully")
import matplotlib.pyplot as plt

print("\nMovies vs TV Shows:")
print(df['type'].value_counts())

df['type'].value_counts().plot(kind='bar')

plt.title("Movies vs TV Shows on Netflix")
plt.xlabel("Type")
plt.ylabel("Count")

plt.savefig("Charts/movies_vs_tvshows.png")
plt.show()
# Extract year from date_added
df['year_added'] = df['date_added'].dt.year

print("\nContent Added Per Year:")
print(df['year_added'].value_counts().sort_index())

# Plot graph
df['year_added'].value_counts().sort_index().plot(kind='line')

plt.title("Content Added to Netflix Per Year")
plt.xlabel("Year")
plt.ylabel("Number of Titles")

plt.savefig("Charts/content_growth.png")
plt.show()
print("\nFirst 10 Genre Entries:")
print(df['listed_in'].head(10))
genres = df['listed_in'].str.split(', ').explode()

print("\nTop 10 Genres:")
print(genres.value_counts().head(10))
genres.value_counts().head(10).plot(kind='bar')

plt.title("Top 10 Netflix Genres")
plt.xlabel("Genre")
plt.ylabel("Count")

plt.savefig("Charts/top_genres.png")
plt.show()
print("\nrating distribution :")
print(df['rating'].value_counts())
df['rating'].value_counts().head(10).plot(kind='bar')

plt.title("Top Netflix Ratings")
plt.xlabel("Rating")
plt.ylabel("Count")

plt.savefig("Charts/ratings_distribution.png")
plt.show()
print("\ntop 10 countries:")
print(df['country'].value_counts().head(10))
countries = df['country'].str.split(', ').explode()
countries.value_counts().head(10).plot(kind='bar')

plt.title("Top 10 Countries on Netflix")
plt.xlabel("Country")
plt.ylabel("Count")

plt.savefig("Charts/top_countries.png")
plt.show()