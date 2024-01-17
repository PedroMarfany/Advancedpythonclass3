"""
Script to make all the tests regarding the filtering
"""

def test_filter_by_top_movie_gross_that_year():
    """
    This test is for the top movie in gross terms each year
    """
    filtering_class = FilteringClass(load_dataset("sample_dataset.csv"))
    filtered_df = filtering_class.filter_top_movie_gross_that_year(5000000)
    assert all(filtered_df['top_movie_gross_that_year'] >= 5000000)

def test_filter_by_gross_profit():
    """
    Test to Filter by gross profit
    """
    filtering_class = FilteringClass(load_dataset("sample_dataset.csv"))
    filtered_df = filtering_class.filter_gross_profit(1000000)
    assert all(filtered_df['gross_profit'] >= 1000000)

def test_filter_by_price():
    """
    Test to Filter by Price
    """
    filtering_class = FilteringClass(load_dataset("sample_dataset.csv"))
    filtered_df = filtering_class.filter_price(100)
    assert all(filtered_df['Price Starting With ($)'] < 100)

def test_filter_by_movies_released():
    """
    Test to filter by movies released
    """
    filtering_class = FilteringClass(load_dataset("sample_dataset.csv"))
    filtered_df = filtering_class.filter_movies_released(50)
    assert all(filtered_df['movies_released'] >= 50)

#uso el sample_dataset para que sea generalizable a cualquier base de datos y no solo a al del ejercicio en cuestión!!!!


