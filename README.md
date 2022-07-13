# FastAPI Blog
API de un CRUD de blogs y migraciones a base de datos

- Create user request
```json
{
  "username": "string",
  "email": "string",
  "password": "string",
  "role": "string"
}
```

## Comandos para migración
- alembic current
- alembic revision --autogenerate -m "first m"
- alembic upgrade head
## postgresql
- docker-compose-postgres.yml
```
version: '3.8'
services:
  db:
    image: postgres:14.1-alpine
    restart: always
    environment:
      - POSTGRES_USER=postgres
      - POSTGRES_PASSWORD=postgres
    ports:
      - '5432:5432'
    volumes:
      - /var/lib/postgresql/data
```
- docker-compose -f docker-compose-postgres.yml up -d

## repeat_every
- https://fastapi-utils.davidmontague.xyz/user-guide/repeated-tasks/
- https://apscheduler.readthedocs.io/en/3.x/userguide.html#adding-jobs
```python
from fastapi_utils.tasks import repeat_every

@router.on_event("startup")
@repeat_every(seconds=60)
def repeated_task() -> str:
    """
    Internal Task that start on the startup event.
    Must dont have arguments.
    Repeat every "n" seconds
    """
    ...

@router.get("start1")
@repeat_every(seconds=2)
def repeated_task_two() -> str:
    print("Imprimiendo 2")
```

## Buildear una imagen
Commando para construir la imagen de docker
````docker build . -t testing:v1.0.0````