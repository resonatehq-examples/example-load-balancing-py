from __future__ import annotations

import asyncio
import os
import time
from typing import TYPE_CHECKING

from resonate.resonate import Resonate

if TYPE_CHECKING:
    from resonate.context import Context


async def compute_something(ctx: Context, id: str, compute_cost: int) -> None:
    """A function that simulates a computation that takes some time."""
    print(f"starting computation {id}")
    # Using time.sleep(), instead of ctx.sleep(), blocks the thread, simulating a time-consuming task
    time.sleep(compute_cost)
    print(f"computed something that cost {compute_cost} seconds")


async def main() -> None:
    r = Resonate(
        url=os.environ.get("RESONATE_URL", "http://localhost:8001"),
        group="worker-group",
    )
    r.register(compute_something)
    print("worker running...", flush=True)
    await asyncio.Event().wait()


if __name__ == "__main__":
    asyncio.run(main())
