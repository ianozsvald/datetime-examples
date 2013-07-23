# NOTE these are code snippets
import datetime
import time
from dateutil import parser as dt_parser  # python-dateutil package

# make a date 30 days ago, conver to truncated string in custom format, convert
# back to datetime
filter_from = datetime.datetime.now() - datetime.timedelta(days=30)
print filter_from, type(filter_from)
filter_from_str = time.strftime("%Y-%m-%dT%H:%M", filter_from.timetuple())
print filter_from_str, type(filter_from_str)
filter_from_new = dt_parser.parse(filter_from_str)
print filter_from_new, type(filter_from_new)

# now build a GMT datetime string from a web Expires header as GMT
d = dt_parser.parse('Tue, 23 Jul 2013 12:47:09 GMT')
print "d as GMT", d  # e.g. 2013-07-23 12:47:09+01:00
import pytz
print "d as UTC", d.astimezone(pytz.utc)  # e.g. 2013-07-23 11:47:09+00:00
