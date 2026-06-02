import streamlit as st
import pandas as pd
import plotly.express as px

from gmail_cleaner import scan_emails
from actions import (
    clean_spam,
    archive_newsletters
)

st.set_page_config(
    page_title="Gmail AI Cleaner",
    page_icon="📧",
    layout="wide"
)

st.title("📧 Gmail AI Cleaner")

st.markdown("""
### Gmail Automation Dashboard

- 🚫 Spam Detection
- 📰 Newsletter Detection
- ✅ Important Emails
""")

action_col1, action_col2, action_col3 = st.columns(3)

with action_col1:

    if st.button(
        "🚫 Clean Spam",
        use_container_width=True
    ):

        deleted = clean_spam()

        st.success(
            f"Deleted {deleted} spam emails"
        )

with action_col2:

    if st.button(
        "📰 Archive Newsletter",
        use_container_width=True
    ):

        archived = archive_newsletters()

        st.success(
            f"Archived {archived} newsletters"
        )

with action_col3:

    refresh = st.button(
        "🔄 Refresh Dashboard",
        use_container_width=True
    )

st.divider()

if (
    "scan_result"
    not in st.session_state
    or refresh
):

    with st.spinner(
        "Scanning Gmail..."
    ):

        st.session_state.scan_result = (
            scan_emails()
        )

result = st.session_state.scan_result

spam = result["spam_count"]
newsletter = result["newsletter_count"]
important = result["important_count"]

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "🚫 Spam",
        spam
    )

with col2:
    st.metric(
        "📰 Newsletter",
        newsletter
    )

with col3:
    st.metric(
        "✅ Important",
        important
    )

st.divider()

chart_col, stats_col = st.columns(
    [2, 1]
)

with chart_col:

    fig = px.pie(
        values=[
            spam,
            newsletter,
            important
        ],
        names=[
            "Spam",
            "Newsletter",
            "Important"
        ],
        title="Email Category Distribution"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

with stats_col:

    total = (
        spam
        + newsletter
        + important
    )

    st.subheader(
        "📊 Summary"
    )

    st.write(
        f"Total Emails: {total}"
    )

    st.write(
        f"Spam: {spam}"
    )

    st.write(
        f"Newsletter: {newsletter}"
    )

    st.write(
        f"Important: {important}"
    )

st.divider()

emails_df = pd.DataFrame(
    result["emails"]
)

keyword = st.text_input(
    "🔍 Search Subject"
)

category = st.selectbox(
    "Category Filter",
    [
        "All",
        "spam",
        "newsletter",
        "important"
    ]
)

filtered_df = emails_df

if category != "All":

    filtered_df = filtered_df[
        filtered_df["Category"]
        == category
    ]

if keyword:

    filtered_df = filtered_df[
        filtered_df["Subject"]
        .str.contains(
            keyword,
            case=False,
            na=False
        )
    ]

st.subheader(
    "📨 Email Classification Results"
)

st.dataframe(
    filtered_df,
    use_container_width=True
)
