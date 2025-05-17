import pandas as pd
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv('cinema_hall_ticket_sales.csv')

# Bar chart: Average ticket price by movie genre
avg_price_by_genre = df.groupby('Movie_Genre')['Ticket_Price'].mean()
plt.bar(avg_price_by_genre.index, avg_price_by_genre.values, color='red')
plt.title('Average Ticket Price by Movie Genre')
plt.xlabel('Movie Genre')
plt.ylabel('Average Ticket Price')
plt.tight_layout()
plt.savefig('bar_chart.png')
plt.close()

# Scatter plot: Age vs Ticket Price
plt.scatter(df['Age'], df['Ticket_Price'], alpha=0.5)
plt.title('Age vs Ticket Price')
plt.xlabel('Age')
plt.ylabel('Ticket Price')
plt.tight_layout()
plt.savefig('scatter_plot.png')
plt.close()
