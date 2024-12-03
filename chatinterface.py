
import streamlit as st
import time

import numpy as np
import random

from llm import *
from strings import *
from game import *


# ---- init session state ----

if "session_id" not in st.session_state.keys():
    st.session_state.session_id = random.randint(0, 1000000)
    print("------- ---- ------- ---- ------- ---- ------- ---- new session", st.session_state.session_id)

if "messages" not in st.session_state.keys():
    st.session_state.messages = [{"role": "assistant", "content": "... H- Hello? God? I need to tell you something."}]

if "caller_evilness" not in st.session_state.keys():
    st.session_state.caller_evilness = random.randint(1, 10)

if "trait_counts" not in st.session_state.keys(): # collects how often each trait has been offered in a scenario
    st.session_state.trait_counts = {
        "charity": 0,
        "faith": 0,
        "fortitude": 0,
        "hope": 0,
        "justice": 0,
        "prudence": 0,
        "temperance": 0,
        "envy": 0,
        "gluttony": 0,
        "greed": 0,
        "lust": 0,
        "pride": 0,
        "sloth": 0,
        "wrath": 0,
        "neutral": 0,
    }

if "caller_system_prompt" not in st.session_state.keys():
    trait_1, trait_2 = select_next_trait_pair(st.session_state.trait_counts)
    #st.session_state.trait_counts[trait_1] = st.session_state.trait_counts.get(trait_1, 0) + 1
    #st.session_state.trait_counts[trait_2] = st.session_state.trait_counts.get(trait_2, 0) + 1
    st.session_state.caller_system_prompt = build_prayer_prompt(trait_1, trait_2, st.session_state.caller_evilness)
    print(st.session_state.trait_counts)
    print(st.session_state.caller_system_prompt)

if "caller_number" not in st.session_state.keys():
    st.session_state.caller_number = 1 # start with first caller


# ---- helpers ----

# restart a session 
def restart_session():

    # remove all existing messages and start with a new caller
    st.session_state.caller_number += 1
    st.session_state.pop("session_id")
    st.session_state.pop("caller_system_prompt")
    st.session_state.messages = st.session_state.messages = [{"role": "assistant", "content": "... H- Hello? God? I need to tell you something."}]
    st.session_state.caller_evilness = random.randint(1, 10)

    st.rerun()

# log conversation via printouts
def log_with_print(role, message):
    if role == "user":
       print("- (" , st.session_state.session_id, ") user    :", message)
    else:
       print("- (" , st.session_state.session_id, ") caller  :", message)

# chat response generator with fake streaming
def prayer_generator(speed=0.05):

    # collect system prompt + chat history
    chat_history = [{"role": "system", "content": st.session_state.caller_system_prompt},]
    for message in st.session_state.messages:
        chat_history.append(message)

    # generate response
    prayer = generate_groq_response(chat_history)

    # log via printout
    log_with_print("caller", prayer)

    # stream-print response 
    for word in prayer.split():
        yield word + " "
        time.sleep(speed)

# user interaction 
def handle_user_input():
    
    # display user message immediately
    with st.chat_message("user"): 
        st.markdown(user_input)

    # log via printout
    log_with_print("user", user_input)

    # add message to history
    st.session_state.messages.append({"role": "user", "content": user_input})

    # check for sin/virtue
    user_moral = detect_trait_in_user_utterance(st.session_state.messages[-2:]).strip().lower()
    #print("user moral detected:", user_moral)
    if user_moral in st.session_state.trait_counts:
    #    print("selected count", user_moral)
        st.session_state.trait_counts[user_moral] += 1
    #else: 
    #    print(user_moral, "is STILL not in trait_counts")

    # generate and display response 
    with st.chat_message("assistant"):
        response = st.write_stream(prayer_generator())
    # add response to history
    st.session_state.messages.append({"role": "assistant", "content": response})

    # TODO detect end of conversation 
    # (has the praying person arrived at a conclusion)

    # rebuild page
    st.rerun()

# end one prayer conversation 
def hang_up_on_caller():

    # when hanging up, send message to caller that god is hanging up 
    # let them react according to current conversation state

    # display user message immediately
    with st.chat_message("user"): 
        st.markdown("(Hanging up)")

    # add hang-up message to history
    st.session_state.messages.append({"role": "user", "content": "(God is hanging up the phone. If you feel the conversation is done, you don't need to respond, otherwise this is your last chance to say something.)"})
    
    # TODO check for moral here, too?

    # generate and display response 
    with st.chat_message("assistant"):
        st.write_stream(prayer_generator())
    # wait a little 
    time.sleep(0.5)

    # end session by starting a new one
    restart_session()


# ---- streamlit page ---- 

st.set_page_config(page_title="GOD'S ANSWERING MACHINE", layout="centered", initial_sidebar_state="expanded")

st.title("GOD'S ANSWERING MACHINE")

st.markdown("""
Oh no! God is out, the prayerphone rings, the storage for incoming messages is full. Nobody here but you. Now it is on you to answer incoming prayers. Good or evil? Virtue or sin? Your advice decides.
""")

# write full chat log
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# user input
user_input = st.chat_input("What to say?")

# handle user input 
if user_input:
    handle_user_input()

if st.button("Hang up"):
    # TODO place next to chat line?
    hang_up_on_caller()

# sidebar with info
with st.sidebar:
    #progress_bar = st.progress(0, text="Progress...")
    st.markdown("## Caller")
    st.markdown("- caller no.: " + str(st.session_state.caller_number))
    st.markdown("... caller info ...")
    
    st.markdown("## Debugging")
    caller_evilness = st.slider("Caller Evilness", 1, 10, value=st.session_state.caller_evilness, disabled=True)
    if caller_evilness:
        st.session_state.caller_evilness = caller_evilness
    st.markdown(st.session_state.trait_counts)

    if st.button("Next caller"):
        # shortcut to end conversation
        restart_session() # end session by starting a new one
    
    # store conversation
    conversation_as_text = ""
    for turn in st.session_state.messages:
        if turn.get("role") == "assistant":
            conversation_as_text += "\nhuman :  "
        elif turn.get("role") == "user":
            conversation_as_text += "\nyou   :  "
        conversation_as_text += turn.get("content") + "\n"
    st.download_button("Save conversation", conversation_as_text, file_name="prayer_"+str(st.session_state.session_id)+".txt")

# debug
#print(st.session_state.messages)
