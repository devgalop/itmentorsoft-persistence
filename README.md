# ITMentorSoft Persistence

Servicio encargado de centralizar la creación y mantenimiento de la capa de persistencia de la plataforma ITMentorSoft. Gestiona el versionamiento de la base de datos mediante migraciones de Alembic y provee una capa de acceso a datos basada en repositorios construida sobre SQLAlchemy 2.0 async ORM.

---

## Arquitectura

La capa de persistencia sigue un diseño inspirado en arquitectura por capas/hexagonal que mantiene los objetos del dominio desacoplados de la base de datos:

```
┌─────────────────────────────────────────┐
│  Capa DTO (objetos de dominio, comandos) │
│  src/dto/ — clases y enums puros de Python│
├─────────────────────────────────────────┤
│  Interfaces de Repositorio (ABC)         │
│  src/repositories/ — contratos abstractos │
├─────────────────────────────────────────┤
│  Capa de Mappers (conversión DTO ↔ Entidad)│
│  src/mappers/ — específicos de PostgreSQL  │
├─────────────────────────────────────────┤
│  Capa de Modelos (entidades SQLAlchemy ORM)│
│  src/models/ — mapeados a tablas de la BD │
├─────────────────────────────────────────┤
│  Infraestructura (sesión, motor de BD)    │
│  src/postgresql_database_session.py       │
└─────────────────────────────────────────┘
```

**Flujo de datos**: Los mappers convierten DTOs a entidades de base de datos y viceversa. Los repositorios definen contratos abstractos (ABC) que consumen y retornan DTOs — los llamadores nunca tocan directamente los modelos de SQLAlchemy.

---

## Stack Tecnológico

| Componente     | Tecnología                | Versión  | Propósito                          |
| -------------- | ------------------------- | -------- | ---------------------------------- |
| Runtime        | Python                    | 3.13     | Lenguaje base                      |
| ORM            | SQLAlchemy                | 2.0.52   | ORM asíncrono con tipos `Mapped[]` |
| Migraciones    | Alembic                   | 1.19.1   | Versionamiento del esquema de BD   |
| Driver BD      | asyncpg                   | 0.31.0   | Driver asíncrono para PostgreSQL   |
| Validación     | Pydantic                  | 2.13.5   | Validación y serialización de datos|
| Entorno        | python-dotenv             | 1.2.3    | Carga de archivos `.env`           |
| Archivos I/O   | aiofiles                  | 25.1.0   | Operaciones asíncronas de archivos |
| Base de datos  | PostgreSQL                | —        | Almacén de datos principal         |

---

## Estructura del Proyecto

```
itmentorsoft-persistence/
├── alembic/
│   ├── env.py                  # Configuración del entorno asíncrono de Alembic
│   ├── script.py.mako          # Plantilla para scripts de migración
│   ├── versions/               # Scripts de migración generados
│   └── README                  # Documentación generada por Alembic
├── src/
│   ├── dto/                    # Objetos de Transferencia de Dominio (14 archivos)
│   │   ├── user.py
│   │   ├── role.py
│   │   ├── content.py
│   │   ├── question.py
│   │   ├── question_details.py
│   │   ├── assessment.py
│   │   ├── qualifier_result.py
│   │   ├── rate_content.py
│   │   ├── learning_path.py
│   │   ├── classification_result.py
│   │   ├── user_recovery_token.py
│   │   ├── assign_role.py
│   │   ├── student_report.py
│   │   └── category_report.py
│   ├── mappers/                # Mappers Entidad-DTO (específicos de PostgreSQL)
│   │   ├── postgresql_user_mapper.py
│   │   ├── postgresql_role_mapper.py
│   │   ├── postgresql_resource_content_mapper.py
│   │   ├── postgresql_question_mapper.py
│   │   ├── postgresql_assessment_mapper.py
│   │   ├── postgresql_learning_path_mapper.py
│   │   ├── postgresql_content_rating_mapper.py
│   │   ├── postgresql_user_recovery_token_mapper.py
│   │   └── postgresql_report_mapper.py
│   ├── models/                 # Entidades ORM de SQLAlchemy
│   │   ├── postgresql_user_model.py
│   │   ├── postgresql_role_model.py
│   │   ├── postgresql_question_model.py
│   │   ├── postgresql_assessment_model.py
│   │   ├── postgresql_resource_content.py
│   │   ├── postgresql_learning_path_model.py
│   │   ├── postgresql_content_rating.py
│   │   ├── postgresql_user_recovery_token_model.py
│   │   ├── postgresql_user_refresh_token_model.py
│   │   └── postgresql_user_refresh_token_mapper.py
│   ├── repositories/           # Interfaces de repositorio (ABC)
│   │   ├── user_repository.py
│   │   ├── role_repository.py
│   │   ├── questions_repository.py
│   │   ├── assessment_repository.py
│   │   ├── question_assessment_repository.py
│   │   ├── content_repository.py
│   │   ├── learning_path_repository.py
│   │   ├── user_recovery_token_repository.py
│   │   ├── refresh_token_repository.py
│   │   └── report_repository.py
│   ├── main.py                 # Punto de entrada para desarrollo (ejecuta create_all)
│   └── postgresql_database_session.py  # Motor, fábrica de sesiones, clase Base
├── alembic.ini                 # Configuración de Alembic
├── pyproject.toml              # Configuración del proyecto (pytest, ruff)
└── requirements.txt            # Dependencias de Python
```

---

## Entidades del Dominio

La capa de persistencia gestiona los siguientes modelos de dominio:

| Entidad                      | Descripción                                      |
| ---------------------------- | ------------------------------------------------ |
| Users                        | Cuentas de usuario de la plataforma              |
| Roles                        | Definición y asignación de roles de usuario      |
| Contents                     | Recursos y materiales de aprendizaje             |
| Questions                    | Preguntas de evaluación                          |
| Assessments                  | Registros y respuestas de evaluaciones de usuario|
| Content Ratings              | Calificaciones de usuarios sobre contenido       |
| Learning Paths               | Rutas estructuradas de progresión de aprendizaje |
| Classification Results       | Clasificación de preguntas y puntajes de rúbrica |
| User Recovery Tokens         | Tokens para recuperación de contraseña           |
| User Refresh Tokens          | Tokens de refresco JWT para autenticación        |
| Reports                      | Analíticas a nivel de estudiante y categoría     |

---

## Configuración

### Requisitos Previos

- Python 3.13+
- Servidor PostgreSQL en ejecución y accesible
- `pip` o `uv` para gestión de dependencias

### Instalación

1. Clonar el repositorio y navegar al directorio del proyecto:

   ```bash
   cd itmentorsoft-persistence
   ```

2. Crear y activar un entorno virtual:

   ```bash
   python -m venv .venv
   source .venv/bin/activate        # Linux/macOS
   .venv\Scripts\activate           # Windows
   ```

3. Instalar las dependencias:

   ```bash
   pip install -r requirements.txt
   ```

4. Crear un archivo `.env` (ver [Variables de Entorno](#variables-de-entorno) más abajo):

   ```bash
   cp .env.example .env   # si está disponible, o crear manualmente
   ```

5. Aplicar las migraciones de la base de datos:

   ```bash
   alembic upgrade head
   ```

   O, para desarrollo rápido, ejecutar el punto de entrada para crear todas las tablas:

   ```bash
   python -m src.main
   ```

---

## Variables de Entorno

Todas las variables se cargan mediante `python-dotenv` desde un archivo `.env` en la raíz del proyecto.

| Variable           | Requerida | Predeterminado | Descripción                                     |
| ------------------ | --------- | -------------- | ----------------------------------------------- |
| `DATABASE_URL`     | Sí        | —              | URL asíncrona de PostgreSQL, ej: `postgresql+asyncpg://usuario:clave@localhost/basedatos` |
| `DB_POOL_SIZE`     | Sí        | —              | Número de conexiones en el pool                 |
| `DB_MAX_OVERFLOW`  | Sí        | —              | Conexiones adicionales máximas más allá del pool |
| `DB_POOL_TIMEOUT`  | Sí        | —              | Segundos de espera antes de agotar el timeout del pool |
| `DB_POOL_RECYCLE`  | Sí        | —              | Segundos antes de reciclar una conexión         |

Si falta alguna variable obligatoria, se genera un `EnvironmentError` al momento de importar el módulo.

---

## Referencia de Comandos de Alembic

| Comando                                          | Descripción                                      |
| ------------------------------------------------ | ------------------------------------------------ |
| `alembic upgrade head`                           | Aplicar todas las migraciones pendientes         |
| `alembic downgrade -1`                           | Revertir la última migración                     |
| `alembic revision --autogenerate -m "mensaje"`   | Generar migración a partir de cambios en modelos |
| `alembic current`                                | Mostrar la versión actual de migración           |
| `alembic history`                                | Mostrar el historial completo de migraciones     |
| `alembic heads`                                  | Mostrar las revisiones head actuales             |
| `alembic stamp head`                             | Marcar la BD en el head actual sin ejecutar migraciones |

### Configuración

- `script_location = alembic` (relativo a `alembic.ini`)
- Usa `sqlalchemy.ext.asyncio` para soporte de migraciones asíncronas
- Lee `DATABASE_URL` del entorno (sobreescribir `sqlalchemy.url` en `alembic.ini` si es necesario)
- Soporta tanto migraciones asíncronas en modo online como modo offline (`--sql`)

---

## Decisiones Arquitectónicas Clave

### 1. Patrón Repositorio con ABC

Los repositorios se definen como clases base abstractas (`abc.ABC`) que especifican contratos. Esto permite intercambiar implementaciones concretas sin modificar el código que los consume — esencial para pruebas con bases de datos en memoria o mocks.

### 2. Mappers como Capa de Desacople

Los mappers se ubican entre los DTOs y las entidades de SQLAlchemy. Esto evita que los objetos de dominio se contaminen con preocupaciones del ORM y permite cambiar la tecnología de base de datos sin tocar los DTOs ni las interfaces de repositorio.

### 3. Diseño Asíncrono desde el Inicio

Todas las operaciones de base de datos usan `asyncpg` y `AsyncSession` de SQLAlchemy. El motor, la fábrica de sesiones y todas las rutas de I/O son asíncronas nativas — sin llamadas síncronas que bloqueen la base de datos.

### 4. Anotaciones de Tipo `Mapped[]`

Las entidades usan las anotaciones de tipo `Mapped[]` de SQLAlchemy 2.0 en lugar de la sintaxis legacy `Column()`. Esto brinda mejor soporte del IDE, verificación de tipos con mypy e intención más clara.

### 5. `create_all` para Desarrollo, Alembic para Producción

`src/main.py` llama a `Base.metadata.create_all` para desarrollo local rápido. Los despliegues en producción deben usar `alembic upgrade head` para cambios de esquema controlados y versionados con capacidad de rollback.

### 6. Creación Automática de la Base de Datos

El módulo de sesión (`postgresql_database_session.py`) incluye `ensure_database_exists()`, que se conecta a la base de datos administrativa `postgres` y crea la base de datos objetivo si no existe. Esto elimina un paso manual de configuración.

---

## Licencia

Propietaria — ITMentorSoft
