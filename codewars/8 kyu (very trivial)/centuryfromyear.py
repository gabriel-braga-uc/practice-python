def century(year):
    return (year // 100 + 1) if (year % 100 >= 1) else (year // 100)