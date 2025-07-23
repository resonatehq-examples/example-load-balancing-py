from resonate import Resonate
from uuid import uuid4
from random import randint


# Initialize an instance of Resonate as a client in "invoke-group"
resonate = Resonate.remote(
    group="invoke-group",
)

def main():
    # Generate a random compute cost between 1 and 10 seconds
    compute_cost = randint(1, 10)
    # Generate a random promise ID
    promise_id = str(uuid4())
    # Invoke compute_something() on the worker group
    _ = resonate.options(target="poll://any@worker-group").begin_rpc(promise_id, "compute_something",  promise_id, compute_cost)


if __name__ == "__main__":
    main()