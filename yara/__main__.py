from core import baddyrequest
from core.data import Data
from jdate import conv
from google_calendar.create_event import create, list_events_summary
from ast import literal_eval
import datetime


def main():
    print(
        "Note: this one doesn't collect any password or username\n" +
        "This is only for personal use."
    )

    username = input("input username: ")
    password = input("input password: ")


    data = Data()  # data contains urls and params
    now = datetime.datetime.now()  # Now datetime
    events_list = list_events_summary()  # List of events in calendar

    # Get name and token
    token = baddyrequest.send_token(data, username, password)
    profile = baddyrequest.send_profile(data, token)
    # str to dict
    profile = literal_eval(profile)

    # Show name
    print(profile['FirstName'] + ' ' + profile['LastName'])

    # Get lessons and count the number of them
    lessons = baddyrequest.send_lessons(data, token)
    lessons = literal_eval(lessons)
    lessons = lessons[0]['Lessons']

    number_lessons = len(lessons)

    for les in lessons:
        number = les['GroupID']
        practice_url = \
            f'https://yaraapi.mazust.ac.ir/api/practices/actives/{number}'
        practices = baddyrequest.send(data, practice_url, token)

        for prac in practices:
            # Convert date by jalali
            finish_date = prac['FinishDate']
            finish_date = conv.jalali_converter(finish_date)
            # Finish time contains hour and minute
            finish_time = prac['FinishTime']
            # Seprate hour and minute
            finish_hour = int(finish_time[:2])
            finish_minute = int(finish_time[:2])
            # Add time to datetime.datetime
            finish_datetime = finish_date.replace(
                minute=finish_minute,
                hour=finish_hour
            )

            # Start DateTime
            start_date = prac['StartDate']
            start_time = prac['StartTime']
            # Convert date by jalali
            start_date = conv.jalali_converter(start_date)
            # Seprate hour and minute
            start_hour = int(start_time[:2])
            start_minute = int(start_time[:2])
            # Add time to datetime.datetime
            start_datetime = start_date.replace(
                minute=start_minute,
                hour=start_hour
            )

            title = prac['Title']
            description = prac['Description']
            body = {
                "summary": f"{les['LessonTitle']} - {title}",
                "description": description,
                "start": {"dateTime": start_datetime.isoformat(),
                        "timeZone": 'Asia/Tehran'},
                "end": {"dateTime": finish_datetime.isoformat(),
                        "timeZone": 'Asia/Tehran'},
            }

            if (finish_datetime >= now) and (body['summary'] not in events_list):
                create(body)


if __name__ == "__main__":
    main()