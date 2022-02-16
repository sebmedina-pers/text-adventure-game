# declaring moving commands in a list
directions = ['go north','go south','go east','go west']

# declaring room dictionary with properties
rooms = {
    "entrance hall": {
        "name": "entrance hall",
        "go north": "atic",
        "go south": "basement",
        "go east": "dining room",
        "go west": "kitchen",
        "text": "This is the main hall.. dark & empty.. you can only move here..\nYou can go north up the wood stairs to room that appears to be an atic, or go south down the stairs to a place that looks dark..\nYou can also go west through a door that smells like rotten food or go east to a semi-open purple door that appears to be a dining room",
        "directions": ["north","south","east","west"]
    },
    "atic": {
        "name": "atic",
        "go south": "entrance hall",
        "item": ["clock","statue"],
        "text": "This room smells like old wood.. You can only go south to the entrance hall where you came from..",
        "directions": ["south"]
    },
    "basement": {
        "name": "basement",
        "go north": "entrance hall",
        "go east": "wine cellar",
        "item": ["chair","doll"],
        "text": "This room is pretty dark & you can hear water dropping from broken pipes..\nYou can go east to a room that smells like a cantine or go north up the stairs to the entrance hall",
        "directions": ["north","east"]
    },
    "dining room": {
        "name": "dining room",
        "go south": "wine cellar",
        "go west": "entrance hall",
        "item": ["painting","lamp"],
        "text": "This room is long.. everything looks broken.. the tables, shelves, chairs..\nYou can go west through a purple door to the entrance hall or south down some stairs where there seems to be spilled wine",
        "directions": ["south","west"]
    },
    "kitchen": {
        "name": "kitchen",
        "go east": "entrance hall",
        "item": ["spoon","fork"],
        "text": "This room has some old cooking & eating items.. looks like food & drinks were spilled a long time ago..\nYou can only go east through a purple door to the entrance hall",
        "directions": ["east"]
    },
    "wine cellar": {
        "name": "wine cellar",
        "go north": "dining room",
        "go west": "basement",
        "item": ["wine","whisky"],
        "text": "This room smells like a cantine.. there are broken pieces of glass everywhere..\nYou go can west to the basement or go north to to the kitchen",
        "directions": ["north","west"]
    }
}

# declaring items with choices + scores
items = {
    "clock": {
        "description": "It looks like this clock has an amazing craftmanship..looking at the bezel it seems like it was manufactured in the 16th century\n",
        "item_in_room": "There's a clock hanged on the wall to your right.",
        "a": {"option": "start the time with clock", "score": 0},
        "b": {"option": "throw the clock", "score": 1}
    },
    "statue": {
        "description": "It looks like this statue is an ancient greek as it's made out of limestone & marble\n",
        "item_in_room": "There's a statue on the floor at the end of the room.",
        "a": {"option": "rub the head of the statue", "score": 1},
        "b": {"option": "hug the statue", "score": 0}
    },
    "chair": {
        "description": "This looks like a vintage barber chair.. black & elegant.\n",
        "item_in_room": "There's a chair on your left.",
        "a": {"option": "sit on the chair", "score": 1},
        "b": {"option": "spin the chair", "score": 0}
    },
    "doll": {
        "description": "This looks like a scary doll from the 1500s. it has creepy eyes and its arms and legs are about to get teared off\n",
        "item_in_room": "There's a doll laying on a sofa on your right.",
        "a": {"option": "pull the head out", "score": 0},
        "b": {"option": "pull the legs out", "score": 1}
    },
    "painting": {
        "description": "This painting has a landscape & looks like art from the 1200s\n",
        "item_in_room": "There's a painting hanged on the wall at the wall on the left.",
        "a": {"option": "blow the dust off the painting", "score": 1},
        "b": {"option": "remove the frame from the painting", "score": 0}
    },
    "lamp": {
        "description": "This lamp looks like it's from the gothic era.. there's candle inside\n",
        "item_in_room": "There's a lamp hanged on the right.",
        "a": {"option": "turn the lamp on", "score": 1},
        "b": {"option": "press the lightbulb", "score": 0}
    },
    "spoon": {
        "description": "This looks like a silver spoon that has a bull figure\n",
        "item_in_room": "There's a spoon laying at the beggining of the table.",
        "a": {"option": "bend the spoon", "score": 1},
        "b": {"option": "toss the spoon", "score": 0}
    },
    "fork": {
        "description": "This looks like a tarnished fork.. characterized by a trident form\n",
        "item_in_room": "There's a fork laying at the end of the table.",
        "a": {"option": "bend the fork", "score": 0},
        "b": {"option": "scratch yourself with the fork", "score": 1}
    },
    "wine": {
        "description": "This bottle of wine looks very old given the shape.. we usually don't see these anymore\n",
        "item_in_room": "There's a wine bottle at the end of the room.",
        "a": {"option": "break the bottle", "score": 1},
        "b": {"option": "drink the bottle", "score": 0}
    },
    "whisky": {
        "description": "This glass of whisky looks like it's very aged.. seems like the owner forgot to drink it\n",
        "item_in_room": "There's a glass of whisky in a small table.",
        "a": {"option": "drink the glass of whisky", "score": 1},
        "b": {"option": "blow the glass", "score": 0}
    }
}
