from services.activity_tracker import ActivityTracker

tracker = ActivityTracker()

tracker.add(
    "Connecting",
    "Connecting to GitHub MCP..."
)

tracker.add(
    "Reading",
    "Reading README.md..."
)

tracker.add(
    "Thinking",
    "Generating final response..."
)

for event in tracker.get_events():
    print(
        event.timestamp.strftime("%H:%M:%S"),
        event.title,
        event.description,
    )