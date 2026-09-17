import pandas as pd
from sqlalchemy import create_engine, text

# Conexión usando las credenciales del laboratorio Docker
engine = create_engine("postgresql+psycopg://alumno:alumno123@localhost:5432/mineria_pg")

# Abrir una conexión explícita y ejecutar los comandos SQL
with engine.begin() as conn:
    # 1. Crear una tabla de prueba
    conn.execute(text("""
        CREATE TABLE IF NOT EXISTS verificacion_laboratorio (
            id SERIAL PRIMARY KEY, 
            mensaje TEXT NOT NULL
        );
    """))

    # 2. Insertar un registro de prueba
    conn.execute(text("INSERT INTO verificacion_laboratorio (mensaje) VALUES ('PostgreSQL + Python operativo');"))

# 3. Leer la tabla directamente desde Pandas
df = pd.read_sql("SELECT * FROM verificacion_laboratorio", engine)

print("\n--- DATOS CARGADOS EN PANDAS CON ÉXITO ---")
print(df)