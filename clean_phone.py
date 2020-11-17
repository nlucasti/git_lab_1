import pandas as pd

def validate_phone(phone_number):
    """
    Tests if phone numbers are valid

    Arguments:
    phone_number - A Pandas Series of phone_numbers as string object

    Return:
    A boolean Pandas Series
    """
    bool_phone = phone_number.str.contains("^\d{3}[-]?\d{3}[-]?\d{3}")
    return bool_phone

numbers = pd.Series(['531-231-1231','235-123-2352','23-12-41'])
print(validate_phone(numbers))