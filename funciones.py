import streamlit as st
import psycopg2
import pandas as pd
import sqlite3


def get_db_conection():
     user = "tyhsawfa"
     password = "YZkjeiJ1oUDtrSJLhVFlyXDiQItoMxs7"
     host = "isilo.db.elephantsql.com"
     port = "5432"
     dbname = "tyhsawfa"
     conn = psycopg2.connect(
          dbname = dbname,
          user = user,
          password = password,
          host = host,
          port = port
     )
     return conn

def insertUser(dni, nombre, cumpleaños, zona):
    conn = get_db_conection()
    try:
        with conn.cursor() as cur:
            query = "INSERT INTO movilidad.usuario(dni, nombre_apellido, cumpleaños, zona)VALUES (%s, %s, %s, %s)"
            cur.execute(query, (dni, nombre, cumpleaños, zona))
            conn.commit()
            st.success("Usuario registrado exitosamente.")
    except psycopg2.Error as e:
        st.error(f"Se produjo un error al guardar el usuario:{e}")
    finally:
        conn.close()

def insertEmpresa(id_empresa, nombre, zona):
    conn = get_db_conection()
    try:
        with conn.cursor() as cur:
            query = "INSERT INTO movilidad.empresa(id_empresa, nombre, zona)VALUES (%s, %s, %s)"
            cur.execute(query, (id_empresa, nombre, zona))
            conn.commit()
            st.success("Empresa registrada exitosamente.")
    except psycopg2.Error as e:
        st.error(f"Se produjo un error al guardar la empresa:{e}")
    finally:
        conn.close()

def insertPostulacion(id_empresa,especialidad, turno, presencialidad, experienciaLaboral, descripcion, contacto):
    conn = get_db_conection()
    try:
        with conn.cursor() as cur:
            query = "INSERT INTO movilidad.puestos(id_empresa, especialidad, turno, presencialidad, experienciaLaboral, descripcion, contacto)VALUES (%s, %s, %s, %s,%s, %s,%s)"
            cur.execute(query, (id_empresa, especialidad, turno, presencialidad, experienciaLaboral, descripcion, contacto))
            conn.commit()
            st.success("Puesto publicado exitosamente.")
    except psycopg2.Error as e:
        st.error(f"Se produjo un error al registrar el puesto:{e}")
    finally:
        conn.close()

def insertCurriculum(dni, especialidad, turno, presencialidad, estudios, experienciaLaboral):
    conn = get_db_conection()
    try:
        with conn.cursor() as cur:
            query = "INSERT INTO movilidad.profesionalusuarios(dni, especialidad, turno, presencialidad, estudios, experienciaLaboral) VALUES (%s, %s, %s, %s, %s, %s)"
            print(query)
            cur.execute(query, (dni, especialidad, turno, presencialidad, estudios, experienciaLaboral))
            conn.commit()
            st.success("Curriculum registrado exitosamente.")
    except psycopg2.Error as e:
        st.error(f"Se produjo un error al guardar el curriculum:{e}")
    finally:
        conn.close()

def dni_exists(dni):
    conn = get_db_conection()
    try:
        with conn.cursor() as cur:
            query = "SELECT * FROM movilidad.usuario WHERE dni = %s"
            cur.execute(query, (dni,))
            result = cur.fetchone()
            return result is not None
    finally:
        conn.close()

def id_empresa_exist(id_empresa):
    conn = get_db_conection()
    try:
        with conn.cursor() as cur:
            query = "SELECT * FROM movilidad.empresa WHERE id_empresa = %s"
            cur.execute(query, (id_empresa,))
            result = cur.fetchone()
            return result is not None
    finally:
        conn.close()

def match(dni):
    conn = get_db_conection()
    if conn is None:
        return pd.DataFrame()  # Devolver un DataFrame vacío si no hay conexión

    try:
        # Actualización de la consulta para incluir un INNER JOIN
        query = """
        select DISTINCT e.nombre, p.descripcion, p.contacto
        FROM movilidad.puestos p
        JOIN movilidad.profesionalusuarios pr ON pr.especialidad = p.especialidad
            AND pr.turno = p.turno
            AND pr.presencialidad = p.presencialidad
            AND pr.experienciaLaboral = p.experienciaLaboral
        JOIN movilidad.empresa e ON p.id_empresa = e.id_empresa
        WHERE pr.dni = %s
        """
        df = pd.read_sql(query, conn, params=(dni,))
        return df
    except Exception as e:
        print(f"Error al realizar la consulta: {e}")
        return pd.DataFrame()  # Devolver un DataFrame vacío en caso de error
    finally:
        conn.close()

