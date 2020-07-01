from dateutil.rrule import rrule, MONTHLY
from datetime import datetime


class Scheduler:

    job_list = [0]
    calendar = []

    def __init__(self, name,_id):
        self.id  =_id
        self.name = name

    @classmethod
    def build_calendar(cls, inv_start_date, send_period, send_frequency):
        # Function to send email on a specific date
        mycal=list(rrule(freq = send_period, count = send_frequency, dtstart = inv_start_date))
        for dt in mycal:
            calendar.append(dt)
        return "Done"

    @classmethod
    def view_calendar(cls):
        return calendar

    
    def find_dates(self, run_date, cal):
        
        for i, dates in enumerate(cal):
            strp_date = datetime.strftime(dates,'%y-%m-%d')
            strp_run_date = str(datetime.strftime(run_date, '%y-%m-%d'))
            print(i, strp_date)
            if strp_date ==  strp_run_date:
                try:
                    if i in job_list:
                        print(i, "(skipped)")
                        continue
                    job_list.append(i)
                except:
                    print('An error occured')
                finally:
                    print(i, strp_date,  strp_run_date," ", "Computed")
            
        #print(datetime.today())




start_date = datetime(2020, 5, 11)
reference_date = datetime.today()


my_schedules = Scheduler("ATTS_SCHEDULER", 1)
calendar = my_schedules.build_calendar(start_date, MONTHLY, 4)

my_schedules.view_calendar()
# my_schedules.find_dates(start_date, calendar)


