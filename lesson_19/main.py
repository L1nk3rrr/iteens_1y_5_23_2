import matplotlib.pyplot as plt
import numpy as np
# plt.bar - стовпчикова діаграма
# plt.plot - лінійний графік

def get_bar():
    months = ['Січень', 'Лютий', 'Березень', 'Квітень', 'Травень']
    sales = [150, 200, 180, 300, 250]
    plt.bar(months, sales)
    plt.xlabel('Місяці')
    plt.ylabel('Кількість продаж')
    plt.title('Продажі за місяцями')
    plt.show()

def get_plot():
    x = np.arange(-11, 11, 0.01)
    y = np.sinc(x)
    plt.plot(x, y)
    plt.xlabel('X-ось')
    plt.ylabel('Y-ось')
    plt.title('Лінійний графік')
    plt.show()

def get_plot_customized():
    x = np.arange(-11, 11, 0.01)
    y = np.sinc(x)
    plt.plot(x, y, marker='o', linestyle='dashdot', color='r', label='My Label')
    plt.xlabel('X-ось')
    plt.ylabel('Y-ось')
    plt.title('Лінійний графік')
    plt.legend()

    plt.grid(True, axis='x', linestyle='dashed', color='b', linewidth=0.5)
    plt.show()

def get_subplots_horizontal():
    x = list(range(5))

    y_1 = [0, 1, 4 ,9 ,16]
    y_2 = [0, 1, 8 ,27 ,64]

    plt.subplot(1, 2, 1)
    plt.plot(x, y_1)
    plt.title('Перший графік')

    plt.subplot(1, 2, 2)
    plt.plot(x, y_2)
    plt.title('Другий графік')

    plt.tight_layout()
    plt.show()

def get_subplots_vertical():
    #       1      2
    #   1 graph1  graph2 
    #   2 graph3
    #   
    x = list(range(5))

    y_1 = [0, 1, 4 ,9 ,16]
    y_2 = [0, 1, 8 ,27 ,64]
    y_3 = [0, 1, 16 ,54 ,128]

    plt.subplot(2, 2, 1)
    plt.plot(x, y_1)
    plt.title('Перший графік')

    plt.subplot(2, 2, 2)
    plt.plot(x, y_2)
    plt.title('Другий графік')

    plt.subplot(2, 2, 3)
    plt.plot(x, y_3)
    plt.title('Третій графік')

    plt.tight_layout()
    plt.show()

def get_scatter():
    x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
    y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])
    # colors = np.array(["red","green","blue","yellow","pink","black","orange","purple","beige","brown","gray","cyan","magenta"])
    # plt.scatter(x, y, c=colors)

    # colors = np.array([0, 10, 20, 30, 40, 45, 50, 55, 60, 70, 80, 90, 100])
    # plt.scatter(x, y, c=colors, cmap='viridis')

    # plt.scatter(x, y, color='#D0CE86')

    x = np.random.randint(1, 1000, size=(100))
    y = np.random.randint(1, 1000, size=(100))
    colors = np.random.randint(1, 1000, size=(100))
    sizes = np.random.randint(1, 600, size=(100))
    plt.scatter(x, y, c=colors, s=sizes, alpha=0.5, cmap='gist_rainbow', label="My custom color graph")
    plt.legend()
    plt.colorbar()
    plt.show()

# get_bar()
# get_plot()
# get_plot_customized()
# get_subplots_horizontal()
# get_subplots_vertical()
get_scatter()