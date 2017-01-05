from datetime import datetime as dt, timezone

import sys
import webbrowser


def timestamp_from_text(text):
    format_string = '%d/%m/%Y -- %H:%M'

    try:
        dt_repr = dt.strptime(text, format_string)
    except ValueError:
        print('-' * 78 + '\nERROR: Invalid date/time format. Exiting.\n' +
              '-' * 78)
        sys.exit()

    dt_repr = dt.replace(dt_repr, tzinfo=timezone.utc)

    timestamp = int(dt.timestamp(dt_repr))

    return timestamp


def make_url(subreddit, start_timestamp, end_timestamp, sort='top'):
    base_url = 'http://reddit.com/r/'

    query = 'q=timestamp%3A' + str(start_timestamp) + '..' + str(end_timestamp)
    sort = '&sort=' + sort
    syntax = '&syntax=cloudsearch'
    restrict = '&restrict_sr=on'

    search = '/search?' + query + sort + syntax + restrict

    url = base_url + subreddit + search
    return url


def usage():
    print('Usage:')
    print('    $ python3 time_period.py <subreddit> <start_date> <end_date>' +
          '[start_time] [end_time]')
    print()


if __name__ == '__main__':
    if len(sys.argv) < 4 or len(sys.argv) > 6:
        usage()

    subreddit = sys.argv[1]

    if len(sys.argv) == 4:
        start = sys.argv[2] + ' -- 00:00'
        end = sys.argv[3] + ' -- 23:59'

    if len(sys.argv) == 5:
        start = sys.argv[2] + ' -- ' + sys.argv[4]
        end = sys.argv[3] + ' -- 23:59'

    if len(sys.argv) == 6:
        start = sys.argv[2] + ' -- ' + sys.argv[4]
        end = sys.argv[3] + ' -- ' + sys.argv[5]

    start_timestamp = timestamp_from_text(start)
    end_timestamp = timestamp_from_text(end)
    url = make_url(subreddit, start_timestamp, end_timestamp)

    webbrowser.open(url)
