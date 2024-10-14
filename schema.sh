mkdir -p app/api/v1/endpoints
mkdir -p app/core
mkdir -p app/db
mkdir -p app/models
mkdir -p app/schemas
mkdir -p app/services
mkdir alembic alembic/versions

touch app/api/v1/endpoints/jobs.py
touch app/api/v1/endpoints/auth.py
touch app/core/config.py
touch app/core/security.py
touch app/db/base.py
touch app/db/base_class.py
touch app/db/session.py
touch app/models/job.py
touch app/models/user.py
touch app/schemas/job.py
touch app/schemas/user.py
touch app/services/auth.py
touch app/services/jobs.py
touch app/main.py
touch .env .gitignore requirements.txt alembic.ini README.md
