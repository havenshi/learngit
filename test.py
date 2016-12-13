import pytz, datetime
local = pytz.timezone ("America/Los_Angeles")
naive = datetime.datetime.strptime ("2001-2-3 10:11:12", "%Y-%m-%d %H:%M:%S")
local_dt = local.localize(naive, is_dst=None)
utc_dt = local_dt.astimezone (pytz.utc)

print utc_dt