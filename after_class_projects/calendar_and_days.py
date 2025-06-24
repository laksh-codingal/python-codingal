
import calendar

for month in range(1, 13):
    print(calendar.month_name[month].lower(), '2025')
    print('mon tue wed thu fri sat sun')
    cal = calendar.monthcalendar(2025, month)
    for week in cal:
        for day in week:
            if day == 0:
                print('   ', end=' ')
            else:
                print(f'{day:2d} ', end=' ')
        
