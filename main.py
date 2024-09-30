def is_leap_year(year):
    result1 = False
    result2 = False
    result3 = False
    result_final = False

    if year % 4 != 0:
        result1 = False
        if year % 100 == 0:
            result2 = True
            if year % 400 != 0:
                result3 = False
            else:
                result3 = True
        else:
            result2 = False
    else:
        result1 = True

    if not (result1 and result3):
        result_final == True
    else:
        result_final == False
        
    return result_final

print(is_leap_year(2000))
