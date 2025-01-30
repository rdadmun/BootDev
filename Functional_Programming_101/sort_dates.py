def sort_dates(dates):
    copy_dates = dates.copy()
    new_dates = []
    final_dates = []
    for d in copy_dates:
        month, day, year = d.split("-")
        new_dates.append("-".join([year, month, day]))
    sorted_dates = sorted(new_dates)
    for e in sorted_dates:
        year, month, day = e.split("-")
        final_dates.append("-".join([month, day, year]))
    return final_dates