# subreddit-time-period
Simple script to generate the URL for subreddits' posts from a given time period.

### IMPORTANT UPDATE: Reddit [removed the Cloudsearch syntax functionality from their search API](https://www.reddit.com/r/ModSupport/comments/6w4juw/reddits_cloudsearch_syntax_no_longer_works_to/) and [apparently has no plans on adding it back or creating a replacement](https://www.reddit.com/r/ModSupport/comments/8btqyd/hows_it_going_with_the_reddit_syntax_cloudsearch/), so the code in here no longer works :cry:. Leaving the repository up anyway, if anyone has news about this let me know! 

------
### Description
Python script that generates URLs (and opens them with the `webbrowser` package) containing the top posts in a [Reddit](https://reddit.com) subreddit during the time period specified.

The URLs are generated according to Reddit's [Cloudsearch syntax](https://www.reddit.com/wiki/search#wiki_cloudsearch_syntax) for time period searches. 

------
### Usage

To run the script you need [Python 3](https://www.python.org/downloads/).

To run the script use `python3 time_period.py <subreddit> <start_date> <end_date> [start_time] [end_time]`

`subreddit` is the name of the subreddit you wish to view.

`start_date` and `end_date` are the dates of the start and the end, respectively, of the time period you wish to view, in the format `dd/mm/yyyy` (so, for example, January 5, 2017 is `05/01/2017`).

The last two arguments, `start_time` and `end_time`, are optional and represent the starting time and ending time (to go along with the dates) of the time period specified, in the format `HH:MM` (24-hour). If they aren't supplied, the starting time is assumed to be `00:00` and the ending time `23:59`.

Obs.: Reddit interprets the date and time as being in UTC.
