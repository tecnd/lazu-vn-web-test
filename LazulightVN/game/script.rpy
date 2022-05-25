# Game starts here. This file contains common content before branching paths.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

init:
    # Disable renpy default rollback/forward on mouse scroll, those are
    # set to show/hide dialogue history instead
    $ config.keymap['rollback'].remove('mousedown_4')
    $ config.keymap['rollforward'].remove('mousedown_5')

    # Disable rollback side by default
    default preferences.desktop_rollback_side = "disable"
    default preferences.mobile_rollback_side = "disable"

    # set to allow scrolling down to advance text
    $ config.keymap['dismiss'].append('mousedown_5')

    # swaps the save menu and hide interface keybind
    $ config.keymap['hide_windows'].remove('mouseup_2')
    $ config.keymap['game_menu'].remove('mouseup_3')
    $ config.keymap['hide_windows'].append('mouseup_3')
    $ config.keymap['game_menu'].append('mouseup_2')

    # Set of reached endings. After an ending is reached, it should insert its name into this set.
    # Number of reached endings is then simply the len() of this set.
    default persistent.endings = set()

    # Persist MC name.
    default persistent.mcName = ""

    python:
        # Reset Settings button calls this function
        def reset_custom_settings():
            config.skip_delay = 75
            persistent.skip_speed = config.skip_delay
            persistent.TextBoxAlpha = 0.9

            renpy.restart_interaction()

        # True Reset button calls this function
        def true_reset():
            persistent._clear(progress=True)
            persistent.endings = set()
            persistent.mcName = ""
            persistent.skip_speed = config.skip_delay
            persistent.TextBoxAlpha = 0.9
            renpy.full_restart() # Returns to main menu

    # Definition for flash transition
    $ flash = Fade(.25, 0, .75, color="#fff")

image bg black = "#000000"

label splashscreen:

    scene black
    pause 1

    show text ("{color=#ffffff}This is a work of fiction. Any similarity to real "
    "businesses, locations, and events is purely coincidental. The characters "
    "portrayed in this story are not intended to represent the views and opinions of "
    "the actual talents, Nijisanji, or ANYCOLOR Inc.\n\n This is a fan-made game "
    "intended for the enjoyment of other fans and the talents\n in celebration of "
    "Lazulight's one year anniversary. The creators are in no way related\n to the talents "
    "present, Nijisanji or ANYCOLOR Inc. in this Visual Novel.\n\n Please enjoy the "
    "game!{/color}")
    with dissolve
    pause

    hide text
    with dissolve

    return

# The game starts here.

label start:
    # If MC name is not set, prompt for name after splashscreen
    if (persistent.mcName == ""):
        call screen name_prompt
        
    jump demo_route
