import re
import datetime


def convert_date_to_iso(date):
    """
    Converts a date string, e.g. 'Apr 20 1970' to an ISODate object 
    based on a regex match

    Args:
        date (str): The date string 
    Returns:
        isodate (Object): The datetime ISO standard date object
    """
    mdy_nocomma_match = r'[a-zA-Z]{3}\s\d{2}\s\d{4}'
    mdy_comma_match = r'[a-zA-Z]{3}\s\d{2},\s\d{4}'
    dmy_nocomma_match = r'\d{2}\s[a-zA-Z]{3}\s\d{4}'
    dmy_comma_match = r'\d{2}\s[a-zA-Z]{3},\s\d{4}'

    match date:
        case re.match(mdy_nocomma_match, date):
            dateobj = datetime.datetime.strptime(date, '%b %d %Y')
            isodate = datetime.isoformat(dateobj)
            return isodate
        case re.match(mdy_comma_match, date):
            dateobj = datetime.datetime.strptime(date, '%b %d, %Y')
            isodate = datetime.isoformat(dateobj)
            return isodate
        case re.match(dmy_nocomma_match, date):
            dateobj = datetime.datetime.strptime(date, '%d %b %Y')
            isodate = datetime.isoformat(dateobj)
            return isodate
        case re.match(dmy_comma_match, date):
            dateobj = datetime.datetime.strptime(date, '%d %b, %Y')
            isodate = datetime.isoformat(dateobj)
            return isodate
