import pandas as pd
from sqlalchemy import create_engine, text

# Conexión usando tus nuevas credenciales personalizadas
engine = create_engine("postgresql+psycopg://tilcel:mineria2607@localhost:5432/dataset_mineria")

# Ejecutar SQL con la sintaxis de SQLAlchemy 2.0+
with engine.begin() as conn:
    # 1. Crear tabla
    conn.execute(text("""
        CREATE TABLE IF NOT EXISTS verificacion_laboratorio (
            id SERIAL PRIMARY KEY, 
            mensaje TEXT NOT NULL
        );
    """))

    # 2. Insertar fila
    conn.execute(text("INSERT INTO verificacion_laboratorio (mensaje) VALUES ('Base de datos dataset_mineria operativa');"))

# 3. Cargar en Pandas
df = pd.read_sql("SELECT * FROM verificacion_laboratorio", engine)

print("\n--- DATOS CARGADOS EN PANDAS ---")
print(df)