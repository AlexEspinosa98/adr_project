# SQLAlchemy Models and Alembic Migrations Guide

This guide details the process of creating new SQLAlchemy models and managing database migrations using Alembic, following the project's established conventions.

## 1. Creating a New SQLAlchemy Model

All database models must inherit from a common base to ensure they are correctly managed by Alembic and include standard fields.

### Steps:

1.  **Location**: Create your new model file within a relevant domain, for example, `common/infrastructure/database/models/`.
2.  **Inheritance**: Your model class must inherit from `BaseModel`, which is imported from `common.infrastructure.database.models.base`. This automatically includes `id`, `is_active`, `created_at`, `updated_at`, and `deleted_at` fields.
3.  **SQLAlchemy Mapping**: Use `Mapped` and `mapped_column` for defining columns, as per SQLAlchemy 2.0 standards.

### Example: Creating a `Product` Model

Let's create a `product.py` file at `common/infrastructure/database/models/product.py`.

```python
# common/infrastructure/database/models/product.py

from sqlalchemy import String, Integer, Float
from sqlalchemy.orm import Mapped, mapped_column
from common.infrastructure.database.models.base import BaseModel

class Product(BaseModel):
    """
    Represents a product in the inventory.
    """
    __tablename__ = 'products'

    name: Mapped[str] = mapped_column(String(150), nullable=False, unique=True)
    description: Mapped[str] = mapped_column(String(500), nullable=True)
    price: Mapped[float] = mapped_column(Float, nullable=False, default=0.0)
    stock: Mapped[int] = mapped_column(Integer, nullable=False, default=0)

    def __repr__(self) -> str:
        return f"<Product(id={self.id}, name='{self.name}', price={self.price})>"

```

### Important: Model Discovery

The project uses an auto-discovery mechanism. For your new model to be recognized by Alembic, you must ensure it is imported. The file `common/infrastructure/database/models/__init__.py` automatically imports all other modules in its directory. By placing your model file there, it will be discovered automatically.

## 2. Managing Database Migrations

We use a custom script that simplifies Alembic commands.

### Location of Tools:

-   **Alembic Configuration**: `alembic.ini`
-   **Migration Environment**: `alembic/env.py` (This is where the database connection and models' metadata are configured).
-   **Migration CLI Script**: `migrations_service/cli.py`

### Generating a New Migration

After creating or modifying a model, you need to generate a migration script that reflects the changes in the database schema.

1.  **Command**: Run the `make` command from our custom CLI script, providing a descriptive message.

```bash
python migrations_service/cli.py make "Create product table"
```

2.  **Output**: This command executes `alembic revision --autogenerate` and creates a new migration file inside `alembic/versions/`. The file will contain the Python code needed to apply (`upgrade`) or revert (`downgrade`) the changes.

Example of a generated file name: `alembic/versions/3d9b1b8d9a9a_create_product_table.py`.

### Applying a Migration

To apply the changes to the database, use the `upgrade` command.

1.  **Command**: To apply all pending migrations up to the latest version (`head`).

```bash
python migrations_service/cli.py upgrade
```

2.  **Output**: The script will execute the `upgrade` function in the new migration file(s), and you will see log output from Alembic confirming the operations.

### Reverting a Migration

If you need to undo a migration, use the `downgrade` command.

1.  **Command**: To revert the last applied migration.

```bash
python migrations_service/cli.py downgrade
```

2.  **Specific Revision**: You can also revert to a specific revision by providing its identifier.

```bash
# This will revert all migrations after the specified revision
python migrations_service/cli.py downgrade <revision_id>
```

By following these steps, you can manage database models and schema migrations consistently and safely within the project.
