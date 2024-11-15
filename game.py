
from strings import *
import random

def build_prayer_prompt(caller_evilness=1):

    human_description = ""
    human_description += human_description_intro
    human_description += human_description_evilness_1
    human_description += str(caller_evilness)
    human_description += human_description_evilness_2
    human_description += human_description_instructions

    print(human_description)

    return human_description


def select_next_trait_pair(proposed_counts):
    """Check which traits have been proposed least so far and generate a new pair."""

    lowest_count_keys = [k for k, v in proposed_counts.items() if v == min(proposed_counts.values())]
    trait_1 = random.choice(lowest_count_keys)
    trait_2 = trait_1
    while trait_2 == trait_1:
        trait_2 = random.choice(lowest_count_keys)

    return trait_1, trait_2

