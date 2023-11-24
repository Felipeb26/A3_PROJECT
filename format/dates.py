from datetime import datetime

from pandas import Series


def month_to_number(month_abbreviation: str, str: bool=True):
    month_dict = {
        "jan": "1",
        "fev": "2",
        "mar": "3",
        "abr": "4",
        "mai": "5",
        "jun": "6",
        "jul": "7",
        "ago": "8",
        "set": "9",
        "out": "10",
        "nov": "11",
        "dez": "12",
    }

    months = month_abbreviation.lower().split("-")
    # Convert the input to lowercase to handle case-insensitivity
    month_abbreviation = months[2]

    # Check if the provided abbreviation is in the dictionary
    if month_abbreviation in month_dict:
        return (
            month_dict[month_abbreviation]
            if str
            else int(month_dict[month_abbreviation])
        )
    else:
        return None


def str_to_date(dates: Series, format: str):
    arrays = dates.unique()

    new_dates = []
    for date in arrays:
        formated_date = datetime.strptime(date, format).date()
        new_dates.append(str(formated_date))

    return new_dates
