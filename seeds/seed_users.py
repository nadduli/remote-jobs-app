# seeds/seed_users.py
import asyncio
from faker import Faker
from sqlalchemy.ext.asyncio import AsyncSession
from app.models.user import User
from app.db.session import get_db

fake = Faker()

async def seed_users(db: AsyncSession, num_users: int = 100):
    """
    Function to create 100 users.
    """
    for _ in range(num_users):
        user = User(
            username=fake.user_name(),
            email=fake.email(),
            password=fake.password(),
            role=fake.random_element(elements=('admin', 'employers', 'job_seekers'))
        )
        db.add(user)
    await db.commit()

async def run():
    async for db in get_db(): 
        await seed_users(db)

if __name__ == "__main__":
    asyncio.run(run())
