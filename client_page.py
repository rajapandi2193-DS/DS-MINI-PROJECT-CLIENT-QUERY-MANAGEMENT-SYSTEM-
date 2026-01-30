import streamlit as st
import pandas as pd
import io
from helpers import now_str

def client_page(conn, cursor, use_sqlite):
    st.header("Client — Submit a Query")
    with st.form("submit_query", clear_on_submit=True):
        mail = st.text_input("Email ID")
        mobile = st.text_input("Mobile Number")
        heading = st.text_input("Query Heading")
        desc = st.text_area("Query Description")
        img = st.file_uploader("Optional: Upload screenshot (png/jpg)", type=['png','jpg','jpeg'])
        submitted = st.form_submit_button("Submit Query")

    if submitted:
        if not mail or not heading or not desc:
            st.error("Please fill Email, Heading and Description.")
            return

        img_bytes = None
        if img:
            img_bytes = img.getvalue()

        if use_sqlite:
            cursor.execute(
                """INSERT INTO queries
                   (mail_id, mobile_number, query_heading, query_description, status, query_created_time, query_closed_time, image)
                   VALUES (?, ?, ?, ?, ?, ?, ?, ?)
                """,
                (mail, mobile, heading, desc, "Open", now_str(), None, img_bytes)
            )
            conn.commit()
        else:
            cursor.execute(
                """INSERT INTO queries
                   (mail_id, mobile_number, query_heading, query_description, status, query_created_time, query_closed_time, image)
                   VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
                """,
                (mail, mobile, heading, desc, "Open", now_str(), None, img_bytes)
            )
            conn.commit()

        st.success("Query submitted successfully!")