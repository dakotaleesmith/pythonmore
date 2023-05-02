"""
pythonmore's module for date-related functionality.
"""
import datetime


class Date():
    def __init__(self, utc_date: datetime.date) -> None:
        self.__UNIX_MICROSECONDS_FACTOR = 1000
        self.__UNIX_EOD_MICROSECONDS = 999
        self.start_of_day_dt = datetime.datetime.combine(
            utc_date, datetime.time.min, tzinfo=datetime.timezone.utc
        )
        self.end_of_day_dt = datetime.datetime.combine(
            utc_date, datetime.time.max, tzinfo=datetime.timezone.utc
        )

    def start_of_day_unix_ts(self) -> int:
        return int(self.start_of_day_dt.timestamp()) * self.__UNIX_MICROSECONDS_FACTOR

    def end_of_day_unix_ts(self) -> int:
        return (
            int(self.end_of_day_dt.timestamp()) * self.__UNIX_MICROSECONDS_FACTOR
            + self.__UNIX_EOD_MICROSECONDS
        )


class Yesterday(Date):
    def __init__(self):
        self.utc_date = datetime.datetime.now(
            tz=datetime.timezone.utc
        ).date() - datetime.timedelta(1)
        super().__init__(self.utc_date)


if __name__ == "__main__":
    yesterday = Yesterday()
    print(yesterday.start_of_day_dt)
    a_date = Date(datetime.date(2023, 4, 28))
    print(a_date.start_of_day_dt)
