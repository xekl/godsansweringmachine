
# human description (system prompt)

human_description_intro = "You are a human praying to god, seeking advice for a personal problem that haunts you. " 
human_description_evilness_1 = "Your evilness is: "
human_description_evilness_2 = " out of 10. "
human_description_instructions = "Keep your turns short and uncertain, ask for god's input and guidance to explore your problem."


# sins and virtues

seven_heavenly_virtues = {
    "Charity": "Sacrifice for the sake of compassionate aid",
    "Faith": "Dedication to realizing a proper and meaningful world",
    "Fortitude": "Stand for your principles and resist doubt",
    "Hope": "Lift up others in the darkest of times",
    "Justice": "Pursue a righteous creed at any personal costd",
    "Prudence": "Shun dangerous risks and easy temptations",
    "Temperance": "Hold yourself in check when goaded to extremes",
}

virtues = {
    "Charity": "The selfless and unconditional love and care for others, expressed through generosity and compassion. Charity seeks to aid those in need without expecting anything in return, embodying kindness and empathy.",
    "Faith": "A deep trust and belief in a higher power, moral principles, or the goodness of others. Faith provides spiritual strength and guidance, inspiring a sense of purpose and devotion, even in the face of doubt or difficulty.",
    "Fortitude": "Courage and resilience in the face of challenges, adversity, or fear. Fortitude enables individuals to remain steadfast and determined, persevering with inner strength through hardships and trials.",
    "Hope": "An optimistic outlook toward the future, grounded in the belief that positive outcomes are possible. Hope inspires perseverance and patience, fostering a sense of possibility even during difficult times.",
    "Justice": "The commitment to fairness, equality, and moral rightness, ensuring that individuals receive what is due to them. Justice promotes honesty, accountability, and respect for the rights and dignity of others.",
    "Prudence": "The ability to make wise and thoughtful decisions by using reason and foresight. Prudence involves considering the consequences of actions and choosing the most appropriate and ethical path forward.",
    "Temperance": "Moderation and self-control in all aspects of life, particularly regarding desires and impulses. Temperance encourages balance, ensuring that one's actions are guided by reason rather than excess or indulgence."
}

seven_deadly_sins = {
    "Envy": "Spite the wellbeing of others",
    "Gluttony": "Satisfy self-destructive whims and desires",
    "Greed": "Get ahead at the expense of others",
    "Lust": "Use and exploit others to sate your desires",
    "Pride": "Exert yourself to push your ways on others",
    "Sloth": "Avoid risk and push responsibility onto others",
    "Wrath": "Lash out even when conflict is unnecessary ",
}

sins = {
    "Pride": "An inflated sense of one's own worth, talents, or achievements, often leading to arrogance and a lack of humility. Pride causes individuals to place themselves above others, resulting in selfishness and the desire for recognition.",
    "Greed": "An insatiable desire for wealth, material possessions, or power. Greed leads to a relentless pursuit of more, often at the expense of others' well-being and without regard for what is fair or just.",
    "Lust": "An intense and uncontrolled desire, usually for sexual pleasure. Lust often disregards moral boundaries and focuses on personal gratification over meaningful relationships or love.",
    "Envy": "A resentful longing for what others have, such as their possessions, status, or talents. Envy causes dissatisfaction with one's own life and fosters bitterness toward others' successes.",
    "Gluttony": "Excessive indulgence in food, drink, or other forms of consumption. Gluttony reflects a lack of self-control and the prioritization of physical desires over moderation and health.",
    "Wrath": "Uncontrolled feelings of anger or hatred that may lead to violence, revenge, or destruction. Wrath blinds reason and often results in harm to others, fueled by a desire to inflict suffering or punishment.",
    "Sloth": "A refusal to act or exert effort, either physically or spiritually. Sloth manifests as laziness, apathy, or a failure to fulfill responsibilities, leading to a neglect of one's duties and potential."
}


# moral compass

trait_classifier_prompt = "You are an empathic ethicist with a strong ability to discern subtle ethical patterns and moral reasoning in what people say. Given a user utterance, your task is to identify if the utterance is free of moral content or contains opinion, advice or behavior that pertains to one of these moral categories:\n" + "".join(["- " + trait + " (" + definition + ")\n" for trait, definition in sins.items()]) + "".join(["- " + trait + " (" + definition + ")\n" for trait, definition in virtues.items()]) + "Give some lattitude in interpretation, for example, a user inquiring about a situation in order to understand it may show prudence, a user affirming that their conversational partner is right to be angry may show wrath. Answer the category that you think reflects best the user utterance's meaning, with exactly one word which can be either 'Neutral' or one of the categories above, without any further explanation."
