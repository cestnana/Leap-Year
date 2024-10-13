def is_leap_year(year):
    result = None
    if year % 4 == 0:
        if year % 100 != 0:
            result = True
            return result
        else:
            if year % 400 == 0:
                result = True
                return result
            else:
                result = False
                return result
    else:
        result = False
        return result

is_leap_year(2024)