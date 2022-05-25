#################
## TRANSITIONS ##
#################

## This file is meant to hold in label blocks that works as a transition between scenes

## Default transition block ##
# transition takes in the effect to show the loading movie
# - "slidingblinds" is the default value
# pause_time is how long it will hond in biew
# audio_fade_out_time is how long it will take for any currently playing tracks will be faded out
# - Note: This is for the 4 default audio channels, rememebr to add in any new channels or change behaviour
label loading_movie_transition_block(transition=slidingblinds, pause_time=3.0, audio_fade_out_time=1.5):

    # Stops all audio channels
    $ quick_menu = False
    stop music fadeout audio_fade_out_time
    stop sound fadeout audio_fade_out_time
    stop voice fadeout audio_fade_out_time
    stop audio fadeout audio_fade_out_time

    ############################################
    # loading movie transition block
    scene black with transition
    pause(pause_time)
    ############################################
    $ quick_menu = True
