def add_time(start, duration, starting_day=""):
  # Separate the time into hours and minutes
  p = start.split()
  t = p[0].split(":")
  a = p[1]

  # Separate the duration into hours and minutes
  d = duration.split(":")

  # Calculate the time in 24-hour format
  if a == "PM":
    t[0] = int(t[0]) + 12

  # Add days, hours and minutes
  eh = int(t[0]) + int(d[0])
  em = int(t[1]) + int(d[1])

  da = 0

  if em >= 60:
    ha = em // 60
    em -= ha * 60
    eh += ha

  if eh > 24:
    da = eh // 24
    eh -= da * 24

  # Find AM or PM
  # Return to 12-hour clock format

  if eh > 12:
    eh -= 12
    a = "PM"
  elif eh == 12:
    a = "PM"
  elif eh > 0 and eh < 12:
    a = "AM"
  else:
    a = "AM"
    eh += 12

  # Find days later
  dl = (" (next day)" if da == 1 else " (" + str(da) +
        " days later)") if da > 0 else ""

  # Find week day
  wd = ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday',
        'Sunday')

  if starting_day:
    b = int(da) + wd.index(starting_day.title())
    c = b // 7
    b = b - c * 7
    ed = str(", " + wd[b])
  else:
    ed = starting_day

  new_time = str(eh) + ":" + (str(em) if em > 9 else
                              ("0" + str(em))) + " " + a + "" + ed + dl

  return new_time
