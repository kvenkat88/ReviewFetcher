import datetime

def validate_datetime(start_time):
        date_string = retrieve_current_date(start_time)
        try:
            datetime.datetime.strptime(date_string, '%Y-%m-%d')
            return True
        except ValueError as e:
            error = str(e)
            print error
            return False

def retrieve_current_date(start_time):
    return start_time.split("T")[0]

def retrieve_today_date():
    today = datetime.date.today()
    return str(today)

def date_comparision(start_time):
    try:
        retrieve_review_entry_date_time_today = retrieve_current_date(start_time)
        date_time_today = retrieve_today_date()
        if retrieve_review_entry_date_time_today == str(date_time_today):
            print "Review comments are available for today based upon the date time matching "
            return True
        else:
            print "Review comments are not available for today based upon the date time matching "
            return False
    except ValueError as e:
            error = str(e)
            print error
            return False

def getCurrentUTCPointTime():
        """
        Method to get the current UTC Time in Zulu Format.
        :param data: NA
        :return: current UTC Time in Zulu Format .'2016-02-03T06:02:29.472Z'
        """
        try:
            currentTime = datetime.datetime.utcnow().isoformat()[:-3] + "Z"
            return currentTime
        except Exception as e:
            error = str(e)
            print error


