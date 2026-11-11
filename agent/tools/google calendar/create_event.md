# create\_event

**Service:** Google Calendar connector. **Status:** used.

## What it does

Creates an event on a Google Calendar (the main calendar if no calendarId is given).

## How to call it

- summary (title), startTime, endTime, in local time with no offset. The server works out Mark's time zone.  
- **All-day:** allDay true, start at midnight on the day, end at midnight the next day.  
- **Doesn't block the day:** availability AVAILABILITY\_FREE.  
- **Repeats yearly:** recurrenceData \["RRULE:FREQ=YEARLY"\].  
- description, location, attendees and reminders are optional.

## Observations

- 2026-11-11: Created all-day, free, yearly events. They worked as expected and use the default reminders.  
- The result includes htmlLink, a link that opens the event. It can be put into a doc as a link.  
- With attendees, invitations are emailed by default (notificationLevel ALL). Set it to NONE to avoid emailing people.
