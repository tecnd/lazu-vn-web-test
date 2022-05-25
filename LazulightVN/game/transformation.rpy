# Basic transformations to help with implimentation of hops, position movement and other such features

# The basic setup for all of these is that the attributes being tweened are set to a starting postion
# the tween happens, genaerly using an ease in or ease in followed by ease out (go up and down)
# the end position is then reseting to the location

# Example of how this should be done to properly
#
# // first set up the animation
# pomu at bounce_param
# pomu "bounce!"
# // This needs to be done in case user clicks too fast
# pomu at clear_offset
#
# // for a higher bounce
# pomu at bounce_param(y_offset_pixels=-LARGE_BOUNCE_Y_OFFSET)
# pomu "hi bounce!"
# pomu at clear_offset
#
# // For sliding do the following
# pomu at slide_from_to(LEFT_X_SLOT, STANDARD_Y_ALIGN, MIDDLE_X_SLOT, STANDARD_Y_ALIGN, MID_SPEED)
# pomu "I'm sliding!"
# // As tehre is soem aligns being changed we use the set aligns at the end position
# pomu at set_aligns(MIDDLE_X_SLOT, STANDARD_Y_ALIGN)
# // Note that the Y may not need to be set unless the slide is from one y to another
# // So could be done as the following for a post x movement
# pomu at set_aligns(MIDDLE_X_SLOT)

init python:

    # Baisc slot locations
    #TODO get proper slot anchor locations based on side

    # 3 slots
    # note that there is some irregularity with tyring to use 0 for an x anchor point when doing tweens
    LEFT_X_SLOT = -600
    MIDDLE_X_SLOT = 0
    RIGHT_X_SLOT = 600

    # 4 character slots
    LEFT_FOUR_X_SLOT = -660
    MID_LEFT_FOUR_X_SLOT = -220
    MID_RIGHT_FOUR_X_SLOT = 220
    RIGHT_FOUR_X_SLOT = 660

    # for offscreen
    OFFSCREEN_LEFT_OFFSET = -1000
    OFFSCREEN_RIGHT_OFFSET = 1000

    # for farther offscreen
    OFFSCREEN_FAR_LEFT_OFFSET = -1600
    OFFSCREEN_FAR_RIGHT_OFFSET = 1600

    # custom dialogue specific offsets
    LEFT_HAND_X_SLOT = -400
    RIGHT_HAND_X_SLOT = 400

    # some heights I expect these may have to become characterspecific
    STANDARD_Y_OFFSET = 500
    STANDARD_Y_ALIGN = 0.5
    ON_KNEES = 750
    SITTING = 650

    #Some standard speeds. When used in bounces note that these will be doubled as it is used for going up and coming down
    QUICK_SPEED = .1
    MID_SPEED = .5
    SLOW_SPEED = 1

    # for speaking bounce offset
    SMALL_BOUNCE_Y_OFFSET = -20
    MID_BOUNCE_Y_OFFSET = -35
    LARGE_BOUNCE_Y_OFFSET = -50
    MED_BOUNCE = 450
    LARGE_BOUNCE = 400

    #for certain X offset effects
    STANDARD_X_OFFSET = 960

########################################################################################################
# Custom shaker class obtained from the Renpy Cookbook
########################################################################################################
init:
    python:
        import math
        class Shaker(object):

            anchors = {
                'top' : 0.0,
                'center' : 0.5,
                'bottom' : 1.0,
                'left' : 0.0,
                'right' : 1.0,
                }

            def __init__(self, start, child, dist):
                if start is None:
                    start = child.get_placement()
                #
                self.start = [ self.anchors.get(i, i) for i in start ]  # central position
                self.dist = dist    # maximum distance, in pixels, from the starting point
                self.child = child

            def __call__(self, t, sizes):
                # Float to integer... turns floating point numbers to
                # integers.
                def fti(x, r):
                    if x is None:
                        x = 0
                    if isinstance(x, float):
                        return int(x * r)
                    else:
                        return x

                xpos, ypos, xanchor, yanchor = [ fti(a, b) for a, b in zip(self.start, sizes) ]

                xpos = xpos - xanchor
                ypos = ypos - yanchor

                nx = xpos + (1.0-t) * self.dist * (renpy.random.random()*2-1)
                ny = ypos + (1.0-t) * self.dist * (renpy.random.random()*2-1)

                return (int(nx), int(ny), 0, 0)

        def _Shake(start, time, child=None, dist=100.0, **properties):

            move = Shaker(start, child, dist=dist)

            return renpy.display.layout.Motion(move,
                time,
                child,
                add_sizes=True,
                **properties)

        Shake = renpy.curry(_Shake)
    #
########################## SCREEN SHAKE DEFINITIONS HERE #############################################
init:
    $ sshake_s = Shake((0, 0, 0, 0), 0.25, dist=15)
    $ sshake_m = Shake((0, 0, 0, 0), 0.35, dist=30)
    $ sshake_l = Shake((0, 0, 0, 0), 0.45, dist=45)
    $ sshake_xl = Shake((0, 0, 0, 0), 0.55, dist=60)
#######################################################################################################

transform bounce_between_align_param(start_offset_x=0, start_offset_y=STANDARD_Y_OFFSET, end_offset_x=0, end_offset_y=STANDARD_Y_OFFSET, y_offset_pixels=480, speed=.1):
    #default aligns
    xalign 0.5
    yalign STANDARD_Y_ALIGN

    # bounce the character from a starting point to an ending point
    xoffset start_offset_x
    yoffset start_offset_y


    parallel:
        easein speed yoffset y_offset_pixels
        easeout speed yoffset end_offset_y
    parallel:
        linear speed * 2 xoffset end_offset_x

    # set to end values
    xoffset end_offset_x
    yoffset end_offset_y



transform bounce_param(y_offset_pixels=480, speed=.1):
    #default aligns
    xalign 0.5
    yalign STANDARD_Y_ALIGN

    # speed is rise and fall of the character
    easein speed yoffset y_offset_pixels
    easeout speed yoffset STANDARD_Y_OFFSET

    # set to default offset
    yoffset STANDARD_Y_OFFSET

transform nodding(y_offset_pixels=520, speed=.1):
    #default aligns
    xalign 0.5
    yalign STANDARD_Y_ALIGN

    # speed is rise and fall of the character
    easein speed yoffset y_offset_pixels
    easeout speed yoffset STANDARD_Y_OFFSET

    # set to default offset
    yoffset STANDARD_Y_OFFSET

transform set_aligns(x=0, y=500):
    # simple set the charcter in position
    # to be used after x/y slot changes
    xoffset x
    yoffset y

    #default aligns
    xalign 0.5
    yalign STANDARD_Y_ALIGN


transform clear_offset():
    # clear offsets without alignment change
    # to be used after bounces with no slot changes
    xoffset 0
    yoffset STANDARD_Y_OFFSET


transform slide_from_to(start_offset_x=-600, offset_y=STANDARD_Y_OFFSET, end_offset_x=0, speed=.5):
    #default aligns
    xalign 0.5
    yalign STANDARD_Y_ALIGN

    # this is a simple tween

    xoffset start_offset_x
    yoffset offset_y

    # tween
    linear speed xoffset end_offset_x

    # set to end values
    xoffset end_offset_x
    yoffset offset_y

# simple slot transformers
# 3 slots
transform set_left_slot(offset_y=STANDARD_Y_OFFSET):
    set_aligns(LEFT_X_SLOT, offset_y)

transform set_mid_slot(offset_y=STANDARD_Y_OFFSET):
    set_aligns(MIDDLE_X_SLOT, offset_y)

transform set_right_slot(offset_y=STANDARD_Y_OFFSET):
    set_aligns(RIGHT_X_SLOT, offset_y)

# 4 slots
transform set_left_four_slot(offset_y=STANDARD_Y_OFFSET):
    set_aligns(LEFT_FOUR_X_SLOT, offset_y)

transform set_middle_left_four_slot(offset_y=STANDARD_Y_OFFSET):
    set_aligns(MID_LEFT_FOUR_X_SLOT, offset_y)

transform set_middle_right_four_slot(offset_y=STANDARD_Y_OFFSET):
    set_aligns(MID_RIGHT_FOUR_X_SLOT, offset_y)

transform set_right_four_slot(offset_y=STANDARD_Y_OFFSET):
    set_aligns(RIGHT_FOUR_X_SLOT, offset_y)

# image transforms
transform sky_zoom:
    xalign 0.5
    zoom 2.0
transform sky_fall:
    xalign 0.5
    zoom 2.0
    easein 0.3 zoom 2.5
    parallel:
        ease 0.5 zoom 1.5
    parallel:
        ease 0.5 yoffset -400
transform rooftop_zoom:
    zoom 2.0
transform rooftop_zoom2:
    zoom 2.3
    xoffset -300
transform river_zoom:
    zoom 2.0
    xoffset -1600
    yoffset -600

transform offscreen_far_right:
    xalign 0.5
    yalign STANDARD_Y_ALIGN
    xoffset 1600
transform offscreen_far_left:
    xalign 0.5
    yalign STANDARD_Y_ALIGN
    xoffset -1600

transform on_knees:
    xalign 0.5
    yalign STANDARD_Y_ALIGN
    yoffset 750

transform finana_staring:
    zoom 1.5
    xoffset -600

transform focus_stare:
    zoom 1.7
    yoffset 950
transform unfocus_stare:
    zoom 1.0
    yoffset STANDARD_Y_OFFSET

transform sit_left:
    xalign 0.5
    xoffset -600
    yalign STANDARD_Y_ALIGN
    yoffset 750

# sprite focus effects

transform focus_sprite:
    yoffset STANDARD_Y_OFFSET
    easein 0.20 zoom 1.050

transform unfocus_sprite:
    yoffset STANDARD_Y_OFFSET
    easeout 0.20 zoom 1.0

transform focus_scream:
    yoffset STANDARD_Y_OFFSET
    easein 0.20 zoom 1.1


# sprite special effects

transform shake_head(offset_x=STANDARD_X_OFFSET, repeat_times=1):
    linear 0.25 xoffset offset_x+15
    linear 0.25 xoffset offset_x-30
    linear 0.25 xoffset offset_x+15
    repeat repeat_times

transform pomusuke_shake:
    linear 0.05 xoffset +10
    linear 0.05 xoffset -10
    repeat

transform fish_shake:
    xalign 0.5
    linear 0.05 xoffset 230
    linear 0.05 xoffset 210
    repeat

transform shiver_soft(offset_x=STANDARD_X_OFFSET):
    linear 0.05 xoffset offset_x+10
    linear 0.05 xoffset offset_x-10
    repeat

transform shiver_softer(offset_x=STANDARD_X_OFFSET):
    linear 0.05 xoffset offset_x+5
    linear 0.05 xoffset offset_x-5
    repeat

transform fidget:
    xalign 0.5
    easein 1.0 xoffset +10
    easein 1.0 xoffset -10
    repeat

transform pomu_sing:
    xalign 0.5
    easein 1.0 xoffset +20
    easein 1.0 xoffset -20
    repeat

transform elira_sing:
    xalign 0.5
    easein 1.0 xoffset +40
    easein 1.0 xoffset -40
    repeat

transform finana_sing:
    alignaround (0.5,0.4)
    ease 1.5 clockwise circles 1
    ease 1.5 counterclockwise circles 1
    repeat

transform pomu_stone_skip:
    xalign 0.5
    easein 2.0 xoffset -180
    easeout 0.1 xoffset 0

transform pomu_stone_skip_repeat:
    xalign 0.5
    easein 2.0 xoffset -180
    easeout 0.1 xoffset 0
    linear 1.0
    repeat

transform panting:
    easein 1.0 yoffset 510
    easein 1.0 yoffset 495
    repeat

transform run_tired_elira:
    easein 1.0 xoffset RIGHT_X_SLOT
    easein 2.0 xoffset MID_RIGHT_FOUR_X_SLOT
    easein 1.5 xoffset MIDDLE_X_SLOT

transform happy_bounce(y_offset_pixels=480, speed=.1):
    block:
        xalign 0.5
        yalign STANDARD_Y_ALIGN
        easein speed yoffset y_offset_pixels
        easeout speed yoffset STANDARD_Y_OFFSET
        yoffset STANDARD_Y_OFFSET
        repeat 2
    linear 0.8
    repeat

transform elira_skipping_to_mid(y_offset_pixels=460, speed=.1):
    parallel:
        linear 2.0 xoffset MIDDLE_X_SLOT
    parallel:
        xalign 0.5
        yalign STANDARD_Y_ALIGN
        easein speed yoffset y_offset_pixels
        easeout speed yoffset STANDARD_Y_OFFSET
        yoffset STANDARD_Y_OFFSET
        linear 0.3
        repeat 5

transform pomu_zoom_face:
    parallel:
        easein 0.5 xoffset MID_LEFT_FOUR_X_SLOT
    parallel:
        easein 0.5 yoffset 950
    parallel:
        easein 0.5 zoom 1.7

transform pomu_unzoom(x_offset_pixels=-600):
    parallel:
        easein 0.6 xoffset x_offset_pixels
    parallel:
        easein 0.6 yoffset STANDARD_Y_OFFSET
    parallel:
        easein 0.6 zoom 1.0

transform elira_fishing:
    parallel:
        linear 0.05 xoffset +5
        linear 0.05 xoffset -5
        repeat
    parallel:
        xalign 0.5
        easein 2.0 xoffset -180
        easeout 0.1 xoffset 0
        linear 1.0
        repeat

transform finana_splashing(splashes=1):
    yalign 0.5
    easein 1.0 yoffset 480
    parallel:
        easein 0.2 zoom 1.2
    parallel:
        yalign 0.5
        yoffset 500
    easein 0.2 zoom 1.0
    linear 0.5
    repeat splashes

transform finana_splashing2(splashes=1):
    parallel:
        easein 0.2 zoom 1.2
        easein 0.2 zoom 1.0
        repeat splashes
    parallel:
        yalign 0.5
        easein 0.2 yoffset 460
        easein 0.2 yoffset 500
        repeat splashes

# special special effects
transform phantom_pain:
    truecenter
    easein 0.125 zoom 1.025
    easeout 0.125 zoom 1.00
    easein 0.125 zoom 1.025
    easeout 0.125 zoom 1.00
    linear 0.5
    repeat
