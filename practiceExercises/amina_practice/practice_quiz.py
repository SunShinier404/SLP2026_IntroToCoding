questions = [
    (
        "Which development helped spread Renaissance ideas and the Reformation?",
        "A. The telegraph\nB. The printing press\nC. Steam-powered ships\nD. The magnetic compass",
        "B",
    ),
    (
        "What did Martin Luther chiefly criticize?",
        "A. The sale of indulgences\nB. The rule of King Henry VIII\nC. The Ottoman Empire\nD. The Treaty of Tordesillas",
        "A",
    ),
    (
        "What does the Columbian Exchange refer to?",
        "A. The transfer of plants, animals, diseases, and people between hemispheres\n"
        "B. The exchange of ambassadors among European monarchies\n"
        "C. A system of taxation in Ming China\n"
        "D. The spread of Buddhism through Central Asia",
        "A",
    ),
    (
        "Which empire controlled Constantinople during the early modern period?",
        "A. Mughal Empire\nB. Ottoman Empire\nC. Holy Roman Empire\nD. Aztec Empire",
        "B",
    ),
    (
        "What was a primary goal of Spanish and Portuguese exploration?",
        "A. Discover coal in Africa\nB. Establish trade routes and expand overseas influence\n"
        "C. Prevent Renaissance art from reaching Europe\nD. Unite Europe under one ruler",
        "B",
    ),
    (
        "Which product became important to transatlantic trade and plantation economies?",
        "A. Silk\nB. Sugar\nC. Tea\nD. Olive oil",
        "B",
    ),
    (
        "What did the Scientific Revolution emphasize?",
        "A. Divine right\nB. Observation, experimentation, and mathematical reasoning\n"
        "C. Religious authority alone\nD. Isolation from foreign ideas",
        "B",
    ),
    (
        "Which statement best describes absolute monarchy?",
        "A. Power shared equally with elected representatives\n"
        "B. Power limited by feudal estates\n"
        "C. A ruler claims centralized control with little formal limitation\n"
        "D. Rule only with the Catholic Church's approval",
        "C",
    ),
    (
        "What was a major consequence of the Atlantic slave trade?",
        "A. Plantation agriculture ended\nB. Europeans migrated widely to East Asia\n"
        "C. Millions of Africans were enslaved and forcibly displaced\n"
        "D. Democracy was established in West Africa",
        "C",
    ),
    (
        "Why is the Treaty of Westphalia (1648) significant?",
        "A. It ended the Protestant Reformation\n"
        "B. It established greater sovereignty for European states\n"
        "C. It created the Mughal Empire\nD. It began the Industrial Revolution",
        "B",
    ),
]

for question, choices, correct_answer in questions:
    answer = input(f"{question}\n{choices}\nYour answer (A-D): ")
    if answer.strip().upper() == correct_answer:
        print("That's correct")
    else:
        print("Incorrect. try again")
