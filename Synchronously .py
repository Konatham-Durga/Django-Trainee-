import time
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User

# Signal receiver with delay to simulate synchronous behavior
@receiver(post_save, sender=User)
def signal_handler(sender, instance, **kwargs):
    print("Signal handler started")
    time.sleep(2)  # Delay to prove synchronous behavior
    print("Signal handler finished")

# Test function to dynamically demonstrate synchronous execution
def test_signal():
    print("Before user save")
    user = User(username="testuser")
    user.save()
    print("After user save")

# Expected Output:
# 1. "Before user save" will print.
# 2. "Signal handler started" prints immediately after save is called.
# 3. "Signal handler finished" prints after the 2-second delay.
# 4. Finally, "After user save" prints, proving the synchronous nature.
