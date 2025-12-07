import time
import sys
from plyer import notification
def countdown(t):
    while t:
        mins, secs = divmod(t, 60)
        timer = f"{mins:02d}:{secs:02d}"

        sys.stdout.write("\r" + timer + "   ")
        sys.stdout.flush()

        time.sleep(1)
        t -= 1

    print("\nZamanlayıcı sona erdi")

    notification.notify(
        title="Time manager",
        message="TİME İS OUT !!!",
        timeout=1
    )
t = int(input("zamanı giriniz: "))
countdown(t)2