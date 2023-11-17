import seaborn
import matplotlib.pyplot as plt

titanic_data = seaborn.load_dataset('titanic')
tips_data = seaborn.load_dataset('tips')
planets_data = seaborn.load_dataset('planets')


# print(planets_data.head())
# print(type(titanic_data))


def histplot_titanic():
    seaborn.histplot(data=titanic_data, x="fare", )

    plt.title("Ticket Fare")
    plt.xlabel("Fare")
    plt.ylabel("Frequency")
    plt.show()

# histplot_titanic()

def countplot_titanic():
    seaborn.countplot(data=titanic_data, x='sex', hue="survived")
    plt.title("Survival Count by Gender")
    plt.xlabel("Gender")
    plt.ylabel("Count")
    plt.legend(title='Survived', labels=['Yes', 'No'])
    plt.show()

# countplot_titanic()

def boxplot_tips():
    seaborn.boxplot(data=tips_data, x='day', y='total_bill')
    plt.title("Total bill by day of the week")
    plt.xlabel("Day")
    plt.ylabel("Total bill")
    plt.show()

# boxplot_tips()


def barplot_tip():
    seaborn.barplot(data=tips_data, x='day', y='tip', hue='sex')
    plt.title('Tip amount by day and gender')
    plt.xlabel("Day")
    plt.ylabel("Tip")
    plt.legend(title="Gender")
    plt.show()

# barplot_tip()

def boxplot_planets():

    seaborn.scatterplot(data=planets_data, x='method', y='mass')
    seaborn.set_palette("Paired")
    seaborn.set_style("whitegrid")
    plt.xticks(rotation=45)
    plt.title("Boxplot of Planet mass by detection method")
    plt.xlabel("Detection method")
    plt.ylabel("Mass")
    plt.show()
boxplot_planets()