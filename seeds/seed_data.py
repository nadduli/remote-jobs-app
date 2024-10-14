# seeds/seed_data.py
import sys
import os
import asyncio

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from seeds.seed_users import run as seed_users

async def seed_all():
    await seed_users()

if __name__ == "__main__":
    asyncio.run(seed_all())
