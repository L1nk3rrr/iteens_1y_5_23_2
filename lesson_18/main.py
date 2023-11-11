import random

import pandas as pd
from faker import Faker



my_fake = Faker()
data = {
    'Name': ['John', 'Alice', 'Bob'],
    'Age': [24, 30 ,22],
    'City': ['New York', 'Lviv', 'Chicago'],
    'Passport': [my_fake.passport_number(), my_fake.passport_number(), my_fake.passport_number()]
}

#   Name Age City
# 0 John 24  New York
# 1  ...............
# 2  ............
def work_with_dict():
    df = pd.DataFrame(data)
    print(df)


def add_delete_edit_new_column_test():
    columns = ['Name', 'Age', 'City', "Passport"]
    df = pd.DataFrame(data, columns=columns)
    # new_row = {"Name": "Valentyn", "Age": 21, "City": "Odesa"}
    
    for _ in range(10):
        new_row = [my_fake.first_name(), random.randint(20, 80), my_fake.city(), my_fake.passport_number()]
        # Додавання нової сторічки
        df.loc[len(df)] = new_row
    print(df)

    print()
    print("After deletion")
    # delete of column
    new_df = df.drop(columns=["City", ])
    # delete of rows
    new_df = new_df.drop([2, 4])
    print(new_df)
    
    print()
    print("After edit")
    new_df.at[0, "Age"] = 100
    print(new_df)

def test_filtration():
    data1 = {'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Emily'],
        'Age': [25, 30, 22, 28, 35],
        'City': ['New York', 'Los Angeles', 'Chicago', 'Miami', 'Seattle']}
    
    df = pd.DataFrame(data1)

    print("Start DF")
    print(df)
    print()
    
    filter_by_age = df[(df['Age'] > 25) & (df.Name.str.contains('a'))]
    # & -> and
    # | -> or
    print("Filter by age DF")
    print(filter_by_age)
    print()

    index_change_df = df.set_index("Name") 
    print("Index by Name")
    print(index_change_df)
    print()

    row_alice = index_change_df.loc['Alice']
    print("My Alice row")
    print(row_alice)


def test_smth():
    df = pd.DataFrame(data)
    # avg_age = df['Age'].mean()
    avg_age = df.Age.mean()
    print(avg_age)

    test_ser = pd.Series([random.random() for _ in range(1000)])
    print(f"{test_ser.max()=}")
    print(f"{test_ser.min()=}")
    print(f"{test_ser.mean()=}")
    print(test_ser)
    print(f"{test_ser.loc[3]=}")
    print(f"{test_ser[test_ser > 0.97]=}")


# work_with_dict()
# add_delete_edit_new_column_test()
# test_filtration()
test_smth()