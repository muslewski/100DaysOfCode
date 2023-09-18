import random

dialogues = {
    1: "Boss: Good morning! I could really use a cup of that amazing coffee you make. It's like a lifesaver on hectic days like this. Whenever you have a moment, could you please whip up a cup for me? Thanks a million!",
    2: "Boss: Hey there! I've got back-to-back meetings lined up, and I'm already feeling drained. Your coffee is my secret weapon for staying alert and focused. Would you mind preparing a cup for me? I'd greatly appreciate it.",
    3: "Boss: Hi! You know, your coffee is the highlight of my day. It's a perfect blend of comfort and energy. If you have the time, could you make one for me? I've got a challenging afternoon ahead.",
    4: "Boss: Morning! That aroma of freshly brewed coffee is just heavenly. I'm in need of a little boost to kickstart my day, and I can always rely on your brew. Could you do me a favor and make one? You're a lifesaver!",
    5: "Boss: Hey, hope you're doing well. I've been running around since dawn, and I could really use a cup of your special coffee. It's like my personal recharge. If you could work your magic and make one, I'd be really grateful.",
    6: "Boss: Hi there! Your coffee has this uncanny ability to turn my mood around. The perfect balance of flavors does wonders. Could you prepare a cup for me? It would make this busy day a whole lot better.",
    7: "Boss: Good morning! Your coffee is like a hidden gem in this office. I hate to bother you, but could you brew one for me? I've got a mountain of tasks ahead, and your coffee is my secret weapon for conquering it all.",
    8: "Boss: Hey! Your coffee-making skills are legendary around here. I need a bit of that magic today. Would you mind making a cup for me? It's the little things that keep me going.",
    9: "Boss: Morning! Your coffee is better than what I've had at fancy cafes. Seriously, it's a game-changer. I could really use a cup right now to power through this pile of paperwork. Any chance you could prepare one for me?",
    10: "Boss: Hi there! Your coffee is like my personal oasis in the chaos of work. I hate to interrupt, but could you brew me a cup? It would be a moment of bliss in this hectic day."
}

boss_say = random.choice(dialogues)

responses = {
    1: "Sure thing, Boss! I'll brew your favorite cup right away.",
    2: "Of course, consider it done! Your coffee will be ready shortly.",
    3: "No problem, Boss. I'll make that special coffee just for you.",
    4: "Absolutely, Boss! Your cup of energy will be ready in a jiffy.",
    5: "Certainly, I'll get to work on your coffee immediately.",
    6: "You got it! I'll prepare your revitalizing cup of coffee.",
    7: "I'm on it, Boss. Your hidden gem of a coffee coming right up.",
    8: "Consider it my pleasure! Your magical cup will be ready soon.",
    9: "Of course, Boss! I'll create a cup that rivals the best cafes.",
    10: "No need to hesitate. Your oasis of bliss is in progress!"
}

response = random.choice(responses)
