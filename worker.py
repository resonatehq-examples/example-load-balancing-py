from resonate import Resonate
from threading import Event
import time

# Initialize an instance of Resonate as a worker in "worker-group"
resonate = Resonate.remote(
    group="worker-group",
)

# Register the function with Resonate
@resonate.register
def compute_something(_, id, compute_cost):
    """A function that simulates a computation that takes some time."""
    print(f"starting computation {id}")
    # Using time.sleep(), instead of ctx.sleep(), blocks the thread, simulating a time-consuming task
    time.sleep(compute_cost)
    print(f"computed something that cost {compute_cost} seconds")
    return


def main():
    # Explicitly start Resonate instance threads
    resonate.start()
    print("worker running...")
    # Keep the main thread alive to allow async tasks to complete
    Event().wait() 


if __name__ == "__main__":
    main()
