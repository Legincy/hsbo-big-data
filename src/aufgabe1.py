from pathlib import Path
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

def aufgabe1(a, b: int) -> bool:
    """
    Check if two numbers are amicable.

    Two numbers are amicable if the sum of their proper divisors (excluding 
    the number itself) equals the other number.

    Example:
        220 -> divisors: 1, 2, 4, 5, 10, 11, 20, 22, 44, 55, 110
        sum = 284
        284 -> divisors: 1, 2, 4, 71, 142
        sum = 220
        => 220 and 284 are amicable numbers.

    Args:
        a (int): first number
        b (int): second number

    Returns:
        bool: True if the numbers are amicable, False otherwise
    """
    if a <= 0 or b <= 0:
        return False
    
    sum_a = sum(get_divider(a)) - a
    sum_b = sum(get_divider(b)) - b

    return sum_a == b and sum_b == a


def get_divider(x: int) -> list[int]:
    """
    Get all divisors of a number including the number itself.

    Args:
        x (int): number to find divisors for

    Returns:
        list[int]: list of divisors of x
    """
    return [i for i in range(1, x+1) if x % i == 0]

def aufgabe2() -> None:
    """
    Load house data from a CSV file and perform basic statistical analysis.

    Args:
        None

    Returns:
        None
    """
    file_path = Path(__file__).parent / "data" / "house_data.csv"
    if not file_path.exists():
        print(f"File not found: {file_path}")
        return
    data = pd.read_csv(file_path)

    data_size = data.shape
    print("Data size (rows, columns):\n", data_size)

    data_attributes = data.columns.tolist()
    print("Data attributes:\n", data_attributes)

    data_mean = data.mean(numeric_only=True)
    print("Mean values:\n", data_mean)

    data_median = data.median(numeric_only=True)
    print("Median values:\n", data_median)

    data_variance = data.var(numeric_only=True)
    print("Variance values:\n", data_variance)

    data_std_dev = data.std(numeric_only=True)
    print("Standard Deviation values:\n", data_std_dev)


def aufgabe3() -> None:
    """
    Create and display a heatmap of the correlation matrix for the house data.

    Args:
        None

    Returns:
        None
    """ 
    file_path = Path(__file__).parent / "data" / "house_data.csv"
    if not file_path.exists():
        print(f"File not found: {file_path}")
        return
    plt_path = Path(__file__).parent / "plt" / "house_data_heatmap.png"
    if not plt_path.parent.exists():
        plt_path.parent.mkdir(parents=True, exist_ok=True)
    data = pd.read_csv(file_path)

    corr_matrix = data.corr(numeric_only=True)
    mask = np.triu(np.ones_like(corr_matrix, dtype=bool))
    print("Correlation Matrix:\n", corr_matrix)

    plt.figure(figsize=(10, 8))
    sns.heatmap(corr_matrix, annot=True, mask=mask, fmt=".2f", cmap='coolwarm', cbar=True)
    plt.title("House_Data: Correlation Matrix Heatmap")

    plt.savefig(plt_path)
    plt.show()

def aufgabe4() -> pd.DataFrame:
    """
    Convert square footage columns to square meters and display the first few rows.

    Args:
        None

    Returns:
        None
    """
    file_path = Path(__file__).parent / "data" / "house_data.csv"
    if not file_path.exists():
        print(f"File not found: {file_path}")
        return
    data = pd.read_csv(file_path)

    data['m2_living'] = data['sqft_living'] * 0.092903
    print(data[['sqft_living', 'm2_living']].head())

    data['m2_lot'] = data['sqft_lot'] * 0.092903
    print(data[['sqft_lot', 'm2_lot']].head())

def aufgabe5() -> None:
    """
    Perform various analyses on the house data and print the results.
    
    Args:
        None
    
    Returns:
        None
    """

    file_path = Path(__file__).parent / "data" / "house_data.csv"
    if not file_path.exists():
        print(f"File not found: {file_path}")
        return
    data = pd.read_csv(file_path)

    data["m2_living"] = data["sqft_living"] * 0.092903

    house_with_largest_living_room = data[data['sqft_living'] == max(data['sqft_living'])]
    print("House with the largest living room:\n", house_with_largest_living_room)

    houses_built_between_1990_2010 = data[(data['yr_built'] >= 1990) & (data['yr_built'] <= 2010)]
    print(f"Houses built between 1990 and 2010 ({ houses_built_between_1990_2010.shape[0]}):\n", houses_built_between_1990_2010)

    renovated_house_with_smallest_lot = data[(data['yr_renovated'] > 0)].nsmallest(1, 'sqft_lot')
    print("Renovated house with the smallest lot:\n", renovated_house_with_smallest_lot)

    houses_with_lots_larger_than_70m2 = data[data['m2_living'] > 70]
    print(f"Houses with lots larger than 70m2:\n", houses_with_lots_larger_than_70m2)

    cheapest_house_with_2_floors = data[data["floors"] == 2].nsmallest(1, "price")
    print("Cheapest house with 2 floors:\n", cheapest_house_with_2_floors)

    data_mean = data.mean(numeric_only=True)
    houses = data[(data["floors"] == 3) & (data["price"] > data_mean["price"]) & (data["bedrooms"] < data_mean["bedrooms"]) & (data["bathrooms"] < data_mean["bedrooms"]) ]
    print("Houses with 3 floors, price above average, bedrooms and bathrooms below average:\n", houses)



#print(aufgabe1(17296, 18416))
#print(aufgabe1(9332, 9842))
#print(aufgabe1(15, 75))
#aufgabe2()
#aufgabe3()
#aufgabe4()
#aufgabe5()