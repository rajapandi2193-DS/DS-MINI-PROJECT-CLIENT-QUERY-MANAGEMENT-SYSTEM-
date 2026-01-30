import streamlit as st
import pandas as pd
import os
from db_config import USE_SQLITE, MYSQL_CONFIG, DB_PATH
from helpers import hash_password, now_str
import sqlite3

# dynamic imports only when needed
if not USE_SQLITE:
    import mysql.connector

from client_page import client_page
from support_page import support_page

st.set_page_config(page_title='Client Query Management', layout='wide')

# --- DB init ---
def init_db_sqlite(path):
    conn = sqlite3.connect(path, check_same_thread=False)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users(
            username TEXT PRIMARY KEY,
            hashed_password TEXT,
            role TEXT
        )
    """)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS queries(
            query_id INTEGER PRIMARY KEY AUTOINCREMENT,
            mail_id TEXT,
            mobile_number TEXT,
            query_heading TEXT,
            query_description TEXT,
            status TEXT,
            query_created_time TEXT,
            query_closed_time TEXT,
            image BLOB
        )
    """)
    conn.commit()
    return conn, cursor

def init_db_mysql(cfg):
    conn = mysql.connector.connect(**cfg)
    cursor = conn.cursor(dictionary=True)
    cursor.execute("""CREATE TABLE IF NOT EXISTS users(
        username VARCHAR(100) PRIMARY KEY,
        hashed_password TEXT,
        role VARCHAR(20)
    )""")
    cursor.execute("""CREATE TABLE IF NOT EXISTS queries(
        query_id INT AUTO_INCREMENT PRIMARY KEY,
        mail_id VARCHAR(255),
        mobile_number VARCHAR(50),
        query_heading TEXT,
        query_description TEXT,
        status VARCHAR(20),
        query_created_time DATETIME,
        query_closed_time DATETIME,
        image LONGBLOB
    )""")
    conn.commit()
    return conn, cursor

if USE_SQLITE:
    conn, cursor = init_db_sqlite(DB_PATH)
else:
    try:
        conn, cursor = init_db_mysql(MYSQL_CONFIG)
    except Exception as e:
        st.error(f"Could not connect to MySQL: {e}")
        st.stop()

# --- Simple sidebar navigation/login ---
st.sidebar.title("Client Query System")
page = st.sidebar.radio("Go to", ["Home","Register","Login"])

def register_user():
    st.subheader("Register")
    username = st.text_input("Username (email)")
    password = st.text_input("Password", type="password")
    role = st.selectbox("Role", ["Client","Support"])
    if st.button("Register"):
        if not username or not password:
            st.error("Provide username and password")
            return
        hp = hash_password(password)
        try:
            if USE_SQLITE:
                cursor.execute("INSERT INTO users(username, hashed_password, role) VALUES (?, ?, ?)", (username, hp, role))
                conn.commit()
            else:
                cursor.execute("INSERT INTO users(username, hashed_password, role) VALUES (%s, %s, %s)", (username, hp, role))
                conn.commit()
            st.success("Registered. You can now login.")
        except Exception as e:
            st.error(f"Could not register: {e}")

def login_user():
    st.subheader("Login")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    if st.button("Login"):
        if not username or not password:
            st.error("Enter username and password")
            return
        hp = hash_password(password)
        if USE_SQLITE:
            cursor.execute("SELECT username, role FROM users WHERE username=? AND hashed_password=?", (username, hp))
            row = cursor.fetchone()
        else:
            cursor.execute("SELECT username, role FROM users WHERE username=%s AND hashed_password=%s", (username, hp))
            row = cursor.fetchone()
        if row:
            st.success("Logged in as %s" % row[0] if USE_SQLITE else row['username'])
            role = row[1] if USE_SQLITE else row['role']
            st.session_state['username'] = username
            st.session_state['role'] = role
            st.rerun()
        else:
            st.error("Invalid credentials")

if page == "Home":
    st.title("Client Query Management System")
    st.write("Use Register to create a user. Use Login to access pages.")
    st.write("Sample CSV is included (dataset.csv).")

elif page == "Register":
    register_user()

elif page == "Login":
    login_user()

# After login — show pages based on role
if 'username' in st.session_state and 'role' in st.session_state:
    role = st.session_state['role']
    st.sidebar.write(f"Logged in as: {st.session_state['username']} ({role})")
    if role == 'Client':
        client_page(conn, cursor, USE_SQLITE)
    else:
        support_page(conn, cursor, USE_SQLITE)

