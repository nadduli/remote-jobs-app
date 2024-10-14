#!/usr/bin/python3

import asyncio
from seeds.seed_users import run as seed_users


async def seed_all():
    # Call the individual seed functions
    await seed_users()

if __name__ == "__main__":
    asyncio.run(seed_all())
