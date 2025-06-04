"""Text based adventure game."""

print("running eXit version 1.2.2")


def display(text: str) -> None:
    """Print scene text with blank line before."""
    print(f"\n{text}")


def prompt(options):
    """Prompt user until a valid option is entered."""
    while True:
        choice = input("> ").lower()
        if choice in options:
            return options[choice]
        print("Invalid option.")


scenes = {
    "start": {
        "text": "You're trapped in a dungeon with your friend.\nYou see a barrel. What do you do?",
        "choices": {
            "interact": "move_barrel",
            "move the barrel": "move_barrel",
            "stay": "friend_note",
            "sit down next to my friend": "friend_note",
            "examine": "look_barrel",
        },
    },
    "look_barrel": {
        "text": "There is a light beam visible behind of the barrel.\nWhat do you do?",
        "choices": {
            "interact": "move_barrel",
            "move the barrel": "move_barrel",
            "stay": "friend_note",
            "sit down next to my friend": "friend_note",
        },
    },
    "move_barrel": {
        "text": "The barrel rolls aside and you find a secret tunnel.\nWhat do you do?",
        "choices": {
            "interact": "tunnel_escape",
            "enter tunnel": "tunnel_escape",
            "leave": "tunnel_escape",
        },
    },
    "tunnel_escape": {
        "text": "You start to escape but your friend is too weak to go with you.\nThey hand you a note.\nWhat do you do?",
        "choices": {
            "interact": "dark_note",
            "read": "dark_note",
            "read note": "dark_note",
            "take": "dark_note",
            "examine": "take_note",
            "stay": "friend_note",
        },
    },
    "dark_note": {
        "text": "It is too dark to read the note.\nWhat do you do?",
        "choices": {
            "leave": "beach",
            "light a match": "beach",
            "examine": "found_match",
            "stay": "found_match",
        },
    },
    "found_match": {
        "text": "You found a match on the ground.\nDo you light the match?",
        "choices": {
            "interact": "match_lit",
            "light": "match_lit",
            "yes": "match_lit",
            "leave": "beach",
            "no": "beach",
        },
    },
    "take_note": {
        "text": "Do you take the note?",
        "choices": {
            "interact": "match_lit",
            "stay": "match_lit",
            "yes": "match_lit",
            "leave": "beach",
            "no": "beach",
        },
    },
    "match_lit": {
        "text": "\"Don't leave me here.\"\nDo you leave your friend or stay?",
        "choices": {
            "stay": "friend_stay",
            "no": "friend_stay",
            "leave": "friend_leave",
            "yes": "friend_leave",
        },
    },
    "friend_note": {
        "text": "Your friend hands you a note.\nWhat do you do?",
        "choices": {
            "interact": "dark_note",
            "take": "dark_note",
            "stay": "dark_note",
        },
    },
    "beach": {
        "text": "You crawl through the tunnel and the tunnel leads you to a beach.\nWhat do you do?",
        "choices": {
            "leave": "look_boat",
            "examine": "look_boat",
            "look": "look_boat",
            "stay": "came_back",
        },
    },
    "look_boat": {
        "text": "In the water you see a boat.\nWhat do you do?",
        "choices": {
            "leave": "boat",
            "interact": "boat",
            "get on the boat": "boat",
            "stay": "fail_return",
        },
    },
    "boat": {
        "text": "Congratulations, you're heading to a new world!",
        "end": True,
    },
    "fail_return": {
        "text": "Tunnel is collapsed, you cannot come back!\nYou left your friend.",
        "end": True,
    },
    "came_back": {
        "text": "You came back! Your friend hands you a note.\nWhat do you do?",
        "choices": {
            "interact": "note_again",
            "take": "note_again",
            "read": "note_again",
            "stay": "note_again",
        },
    },
    "note_again": {
        "text": "\"Don't leave me here again.\"\nDo you leave your friend or stay?",
        "choices": {
            "stay": "friend_stay",
            "no": "friend_stay",
            "leave": "friend_leave",
            "yes": "friend_leave",
        },
    },
    "friend_stay": {
        "text": "Dungeon is collapsed.\nYou didn't left your friend.",
        "end": True,
    },
    "friend_leave": {
        "text": "You left your friend.",
        "end": True,
    },
}


def main():
    input("\nPRESS THE ENTER KEY TO START")
    current = "start"
    while True:
        scene = scenes[current]
        display(scene["text"])
        if scene.get("end"):
            input("\nPress enter to exit the game.")
            break
        current = prompt(scene["choices"])


if __name__ == "__main__":
    main()

