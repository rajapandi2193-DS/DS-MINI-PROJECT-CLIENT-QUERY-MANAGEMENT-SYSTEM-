import streamlit as st
import pandas as pd
import io
from helpers import now_str, image_bytes_to_pil

def support_page(conn, cursor, use_sqlite):
    st.header("Support — Dashboard")
    status_filter = st.selectbox("Filter by status", ["All","Open","Closed"])
    refresh = st.button("Refresh")

    query = "SELECT * FROM queries"
    if use_sqlite:
        df = pd.read_sql_query(query, conn)
    else:
        df = pd.read_sql(query, conn)

    if status_filter != "All":
        df = df[df['status'] == status_filter]

    st.dataframe(df[['query_id','mail_id','mobile_number','query_heading','status','query_created_time','query_closed_time']])

    st.markdown('---')
    st.subheader("Take action on a query")
    qid = st.number_input("Enter query_id to view/close", min_value=1, step=1)
    if st.button("Load query"):
        row = df[df['query_id']==qid]
        if row.empty:
            st.warning("No such query in current filter/search (try Refresh).")
        else:
            r = row.iloc[0]
            st.write("Heading:", r['query_heading'])
            st.write("Description:", r['query_description'])
            st.write("Status:", r['status'])
            if r.get('image') is not None and not pd.isna(r.get('image')):
                try:
                    img_bytes = r['image']
                    st.image(img_bytes)
                except Exception:
                    st.info("Image exists but could not be displayed.")
            if r['status'] == 'Open':
                if st.button("Close query"):
                    if use_sqlite:
                        cursor.execute("UPDATE queries SET status=?, query_closed_time=? WHERE query_id=?", ("Closed", now_str(), qid))
                        conn.commit()
                    else:
                        cursor.execute("UPDATE queries SET status=%s, query_closed_time=%s WHERE query_id=%s", ("Closed", now_str(), qid))
                        conn.commit()
                    st.success("Query closed.")
                    st.experimental_rerun()
            else:
                st.info("Query already closed.")