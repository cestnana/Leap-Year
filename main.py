def is_leap_year(year):
    result = None
    if year % 4 == 0:
        # continue logic part
        if year % 100 != 0:
            # continue logic part
            result = True
            return result
        else:
            if year % 400 == 0:
                # continue logic part
                result = True
                return result
            else:
                result = False
                return result
    else:
        result = False
        return result

# print(f"Is 2000 Leap Year? {is_leap_year(2000)}.")
year_to_test = int(input(f"Which year do you want to test? "))
print(f"Is {year_to_test} Leap Year? {is_leap_year(year_to_test)}.")
