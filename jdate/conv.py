import jalali


def jalali_converter(date):
    """This convert Hijri calendar date such as 14000205 to 
        Gregorian calendar (2021, 4, 25)"""
    year = int(date[:4])
    month = int(date[4:6])
    day = int(date[6:])
    valid_date = (year, month, day)
    res = jalali.Persian(valid_date).gregorian_datetime()
    return res
