
from strings import *
from llm import *
import random

def build_prayer_prompt(trait_1, trait_2, caller_evilness=1):

    human_description = ""
    human_description += human_description_intro
    #human_description += human_description_evilness_1
    #human_description += str(caller_evilness)
    #human_description += human_description_evilness_2
    human_description += human_description_trait_1
    human_description += str(trait_1)
    if virtues.get(trait_1):
        human_description += " (" + virtues.get(trait_1) + ")"
    elif sins.get(trait_1):
        human_description += " (" + sins.get(trait_1) + ")"
    human_description += human_description_trait_2
    human_description += str(trait_2)
    if virtues.get(trait_2):
        human_description += " (" + virtues.get(trait_2) + ")"
    elif sins.get(trait_2):
        human_description += " (" + sins.get(trait_2) + ")"
    human_description += human_description_instructions

    return human_description


# moral selection
def select_next_trait_pair(proposed_counts):
    """Check which traits have been proposed least so far and generate a new pair."""

    lowest_count_keys = [k for k, v in proposed_counts.items() if v == min(proposed_counts.values())]
    trait_1 = random.choice(lowest_count_keys)
    trait_2 = trait_1
    while trait_2 == trait_1:
        trait_2 = random.choice(lowest_count_keys)

    return trait_1, trait_2


# moral compass
def detect_trait_in_user_utterance(last_two_messages):

    last_prayer_turn = last_two_messages[0].get("content")
    user_input = last_two_messages[1].get("content")

    # collect system prompt + chat history
    chat_history = [{"role": "system", "content": trait_classifier_prompt},
                   {"role": "assistant", "content": last_prayer_turn[-100:]},
                   {"role": "user", "content": user_input}]

    # assess user input morally
    moral = generate_groq_response(chat_history, max_tokens = 5, temperature = 0.1)

    print("moral:", moral)

    return moral
