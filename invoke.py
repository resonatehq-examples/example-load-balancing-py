from __future__ import annotations

import asyncio
import os
from random import randint
from uuid import uuid4

from resonate.resonate import Resonate


async def main() -> None:
    r = Resonate(
        url=os.environ.get("RESONATE_URL", "http://localhost:8001"),
        group="invoke-group",
    )
    try:
        # Generate a random compute cost between 1 and 10 seconds
        compute_cost = randint(1, 10)
        # Generate a random promise ID
        promise_id = str(uuid4())
        # Invoke compute_something() on the worker group (fire-and-forget)
        r.options(target="worker-group").rpc(promise_id, "compute_something", promise_id, compute_cost)
    finally:
        await r.stop()


if __name__ == "__main__":
    asyncio.run(main())
