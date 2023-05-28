
# Base image
FROM python:3.11-slim AS base

ARG BACKEND_PORT=8000
ENV BACKEND_PORT=$BACKEND_PORT

WORKDIR /app

# Install python packages
COPY Pipfile .
COPY Pipfile.lock .
RUN pip install pipenv --no-cache-dir --disable-pip-version-check
RUN pipenv install --system --deploy --ignore-pipfile

# Copy sources
COPY core/ core/
COPY config/ config/
COPY docs/ docs/
COPY auth/ auth/
COPY users/ users/
COPY candidates/ candidates/
COPY staff/ staff/
COPY interns/ interns/
COPY manage.py .
COPY demo_users.py .

# Copy entrypoint script
COPY docker-entrypoint.sh .


# Run image
FROM base AS run

WORKDIR /app

EXPOSE $BACKEND_PORT

# Add entrypoint script
ENTRYPOINT [ "bash", "-c", "./docker-entrypoint.sh", "docker-entrypoint.sh" ]
