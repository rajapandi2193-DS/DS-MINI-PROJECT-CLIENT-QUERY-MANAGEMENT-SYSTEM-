# Client Query Management System

**What this is:** A simple Streamlit + SQL project for clients to submit support queries and for support staff to manage/close them.

**Tech:** Python, Streamlit, MySQL (primary) with optional SQLite fallback, pandas, mysql-connector-python.

## Quick start (using SQLite, easiest)
1. Make sure Python 3.8+ is installed.
2. Create and activate a virtualenv (recommended):
   ```
   python -m venv .venv
   source .venv/bin/activate   # mac/linux
   .venv\Scripts\activate    # windows
   ```
3. Install requirements:
   ```
   pip install -r requirements.txt
   ```
4. Run:
   ```
   streamlit run app.py
   ```
5. Default DB: `db.sqlite` will be created in the project folder if you use SQLite mode.

## Using MySQL
- Edit `db_config.py` to set `USE_SQLITE = False` and update `MYSQL_CONFIG`.
- Create a database in MySQL and ensure the user has privileges.
- Run the app; it will create tables if missing.

## Files
- `app.py` — Streamlit app (login/register + client + support)
- `db_config.py` — Database connection helper (SQLite fallback)
- `client_page.py` — Client submission code
- `support_page.py` — Support dashboard code
- `requirements.txt` — Dependencies
- `dataset.csv` — sample CSV to import
- `schema.sql` — SQL create table statements
- `helpers.py` — small helper functions

## Notes
- Passwords are hashed using SHA-256 (see `helpers.py`). For production, use bcrypt.
- Images uploaded are stored as BLOB in the database and displayed inline.
- This is a teaching/demo project. Do not use as-is in production without hardening.

