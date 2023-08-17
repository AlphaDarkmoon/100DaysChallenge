import notify2
import time

# Initialize the notify2 library
notify2.init("My Application")

# Create a notification object
notification = notify2.Notification(
    "Title",
    "Notifications Here...",
    "de2.png"
)

times = 0
while times<10:
    time.sleep(5)
    # Show the notification
    notification.show()
    times+=1
    print(times)




