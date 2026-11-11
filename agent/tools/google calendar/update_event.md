# update\_event

**Service:** Google Calendar connector. **Status:** loaded, not used yet.

## What it does

Changes an existing event: title, time, all-day, availability, description, location, attendees, reminders, colour, visibility.

## Observations

- 2026-11-11: It has no setting for repeats. To make a one-off event repeat yearly, a new repeating event was created with create\_event and the old one deleted with delete\_event.
