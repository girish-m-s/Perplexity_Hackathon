import streamlit as st
from threading import Thread
import schedule
import time

from Perplexity_Hack import (
    process_command_with_llm,
    start_scheduled_stock_watch,
    watch_my_stocks_and_notify,
    conversation_history
)

# Page Config
st.set_page_config(page_title="AI Trading Assistant", layout="wide")
st.title("💹 AI Trading Assistant")
st.write("Ask anything like:\n- `Buy 1 AAPL`\n- `Sell 0.002 BTC/USD`\n- `What's in my portfolio?`")

# Initialize session state
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# --- Chat Input Form ---
with st.form("chat_form", clear_on_submit=True):
    user_input = st.text_input(
        "Enter your command", placeholder="e.g., Buy 0.01 BTC or What's my balance?")
    submitted = st.form_submit_button("Send")

if submitted and user_input:
    st.session_state.chat_history.append(
        {"role": "user", "content": user_input})

    with st.spinner("Thinking..."):
        process_command_with_llm(user_input)

    if conversation_history:
        assistant_reply = conversation_history[-1]['content']
        st.session_state.chat_history.append(
            {"role": "assistant", "content": assistant_reply})

# --- Chat Display ---
for msg in st.session_state.chat_history:
    role_icon = "🧑‍💼" if msg["role"] == "user" else "🤖"
    with st.chat_message(msg["role"]):
        st.markdown(f"{role_icon} {msg['content']}")

# --- Manual Watch Button ---
if st.button("🔍 Watch My Stocks Now"):
    with st.spinner("Checking your stocks..."):
        watch_my_stocks_and_notify()
    st.success("Stock check completed!")

# --- Background Scheduler ---


def run_schedule():
    while True:
        schedule.run_pending()
        time.sleep(1)


def start_background_scheduler():
    schedule.every(4).hours.do(watch_my_stocks_and_notify)
    thread = Thread(target=run_schedule, daemon=True)
    thread.start()


if "scheduler_started" not in st.session_state:
    start_background_scheduler()
    st.session_state.scheduler_started = True
