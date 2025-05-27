import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Set plot style
sns.set(style="whitegrid")
plt.rcParams["figure.figsize"] = (12, 6)

# Load your sample dataset
df = pd.read_csv("sample_airbnb_listings.csv")

# Basic cleaning (price is already numeric)
df['reviews_per_month'].fillna(0, inplace=True)
df.dropna(subset=['price', 'room_type', 'neighbourhood'], inplace=True)

# 1. Room Type Distribution
room_type_counts = df['room_type'].value_counts()
sns.barplot(x=room_type_counts.index, y=room_type_counts.values, palette='Set2')
plt.title("Room Type Distribution", fontsize=16)
plt.xlabel("Room Type")
plt.ylabel("Number of Listings")
plt.tight_layout()
plt.show()

# 2. Average Price by Room Type
avg_price = df.groupby('room_type')['price'].mean().sort_values()
sns.barplot(x=avg_price.index, y=avg_price.values, palette='viridis')
plt.title("Average Price by Room Type", fontsize=16)
plt.xlabel("Room Type")
plt.ylabel("Average Price ($)")
plt.tight_layout()
plt.show()

# 3. Top 5 Neighbourhoods by Number of Listings
top_neighbourhoods = df['neighbourhood'].value_counts().head(5)
sns.barplot(y=top_neighbourhoods.index, x=top_neighbourhoods.values, palette='coolwarm')
plt.title("Top 5 Neighbourhoods by Listings", fontsize=16)
plt.xlabel("Number of Listings")
plt.ylabel("Neighbourhood")
plt.tight_layout()
plt.show()

# Save cleaned dataset (optional)
df.to_csv("cleaned_sample_airbnb.csv", index=False)
print("✅ Completed analysis and saved cleaned data as cleaned_sample_airbnb.csv")
