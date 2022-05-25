################################################################################
## Initialization
################################################################################

init offset = -1


################################################################################
## Styles
################################################################################

style default:
    properties gui.text_properties()
    language gui.language

style input:
    properties gui.text_properties("input", accent=True)
    adjust_spacing False

style hyperlink_text:
    properties gui.text_properties("hyperlink", accent=True)
    hover_underline True

style gui_text:
    properties gui.text_properties("interface")


style button:
    properties gui.button_properties("button")


style button_text is gui_text:
    properties gui.text_properties("button")
    yalign 0.5


style label_text is gui_text:
    properties gui.text_properties("label", accent=True)

style prompt_text is gui_text:
    properties gui.text_properties("prompt")


style bar:
    ysize gui.bar_size
    left_bar Frame("gui/bar/left.png", gui.bar_borders, tile=gui.bar_tile)
    right_bar Frame("gui/bar/right.png", gui.bar_borders, tile=gui.bar_tile)

style vbar:
    xsize gui.bar_size
    top_bar Frame("gui/bar/top.png", gui.vbar_borders, tile=gui.bar_tile)
    bottom_bar Frame("gui/bar/bottom.png", gui.vbar_borders, tile=gui.bar_tile)

style scrollbar:
    ysize gui.scrollbar_size
    base_bar Frame("gui/scrollbar/horizontal_[prefix_]bar.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/scrollbar/horizontal_[prefix_]thumb.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)

style vscrollbar:
    xsize gui.scrollbar_size
    base_bar Frame("gui/scrollbar/vertical_[prefix_]bar.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/scrollbar/vertical_[prefix_]thumb.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)

style slider:
    ysize gui.slider_size
    base_bar Frame("gui/slider/horizontal_[prefix_]bar.png", gui.slider_borders, tile=gui.slider_tile)
    thumb "gui/slider/horizontal_[prefix_]thumb.png"

style vslider:
    xsize gui.slider_size
    base_bar Frame("gui/slider/vertical_[prefix_]bar.png", gui.vslider_borders, tile=gui.slider_tile)
    thumb "gui/slider/vertical_[prefix_]thumb.png"


style frame:
    padding gui.frame_borders.padding
    background Frame("gui/frame.png", gui.frame_borders, tile=gui.frame_tile)

################################################################################
## In-game screens
################################################################################


## Say screen ##################################################################
##
## The say screen is used to display dialogue to the player. It takes two
## parameters, who and what, which are the name of the speaking character and
## the text to be displayed, respectively. (The who parameter can be None if no
## name is given.)
##
## This screen must create a text displayable with id "what", as Ren'Py uses
## this to manage text display. It can also create displayables with id "who"
## and id "window" to apply style properties.
##
## https://www.renpy.org/doc/html/screen_special.html#say

screen say(who, what):
    # Show history on mouse scroll up
    key "mousedown_4" action ShowMenu("history")

    style_prefix "say"

    window:
        id "window"

        #handles dialogue box opacity
        background Transform(style.window.background, alpha=persistent.TextBoxAlpha)

        if who is not None:

            window:
                id "namebox"
                style "namebox"
                text who id "who"
                background Transform(style.namebox.background, alpha=persistent.TextBoxAlpha)

        text what id "what"


    ## If there's a side image, display it above the text. Do not display on the
    ## phone variant - there's no room.
    if not renpy.variant("small"):
        add SideImage() xalign 0.0 yalign 1.0


## Make the namebox available for styling through the Character object.
init python:
    config.character_id_prefixes.append('namebox')

style window is default
style say_label is default
style say_dialogue is default
style say_thought is say_dialogue

style namebox is default
style namebox_label is say_label


style window:
    xalign 0.5
    xfill True
    yalign gui.textbox_yalign
    ysize gui.textbox_height

    background Image("gui/textbox.png", xalign=0.5, yalign=1.0)

style namebox:
    xpos gui.name_xpos
    xanchor gui.name_xalign
    xsize gui.namebox_width
    ypos gui.name_ypos
    ysize gui.namebox_height

    background Frame("gui/namebox.png", gui.namebox_borders, tile=gui.namebox_tile, xalign=gui.name_xalign)
    padding gui.namebox_borders.padding

style say_label:
    color "#ffffff"
    outlines [ (absolute(2), "#000000", absolute(0), absolute(0)) ]
    properties gui.text_properties("name", accent=True)
    xalign gui.name_xalign
    yalign 0.5

style say_dialogue:
    color "#ffffff"
    outlines [ (absolute(2), "#000000", absolute(0), absolute(0)) ]
    properties gui.text_properties("dialogue")

    xpos gui.dialogue_xpos
    xsize gui.dialogue_width
    ypos gui.dialogue_ypos


## Input screen ################################################################
##
## This screen is used to display renpy.input. The prompt parameter is used to
## pass a text prompt in.
##
## This screen must create an input displayable with id "input" to accept the
## various input parameters.
##
## https://www.renpy.org/doc/html/screen_special.html#input

screen input(prompt):
    style_prefix "input"

    window:

        vbox:
            xalign gui.dialogue_text_xalign
            xpos gui.dialogue_xpos
            xsize gui.dialogue_width
            ypos gui.dialogue_ypos

            text prompt style "input_prompt"
            input id "input"

style input_prompt is default

style input_prompt:
    xalign gui.dialogue_text_xalign
    properties gui.text_properties("input_prompt")

style input:
    xalign gui.dialogue_text_xalign
    xmaximum gui.dialogue_width


## Choice screen ###############################################################
##
## This screen is used to display the in-game choices presented by the menu
## statement. The one parameter, items, is a list of objects, each with caption
## and action fields.
##
## https://www.renpy.org/doc/html/screen_special.html#choice

screen choice(items):
    style_prefix "choice"

    vbox:
        for i in items:
            textbutton i.caption action i.action


## When this is true, menu captions will be spoken by the narrator. When false,
## menu captions will be displayed as empty buttons.
define config.narrator_menu = True


style choice_vbox is vbox
style choice_button is button
style choice_button_text is button_text

style choice_vbox:
    xalign 0.5
    ypos 405
    yanchor 0.5

    spacing gui.choice_spacing

style choice_button is default:
    properties gui.button_properties("choice_button")
    # sound for main selections in game play choices
    hover_sound audio.choose
    activate_sound audio.confirm

style choice_button_text is default:
    properties gui.button_text_properties("choice_button")
    yalign 0.5


## Quick Menu screen ###########################################################
##
## The quick menu is displayed in-game to provide easy access to the out-of-game
## menus.

screen quick_menu():

    ## Ensure this appears on top of other screens.
    zorder 100

    if quick_menu:

        hbox:
            style_prefix "quick"

            xalign 0.5
            yalign 0.96

            # textbutton _("Back") action Rollback()
            textbutton _("History") action ShowMenu('history') hover_sound audio.choose activate_sound audio.confirm
            textbutton _("Skip") action Skip() alternate Skip(fast=True, confirm=True) hover_sound audio.choose activate_sound audio.confirm
            textbutton _("Auto") action Preference("auto-forward", "toggle") hover_sound audio.choose activate_sound audio.confirm
            textbutton _("Save") action ShowMenu('save') hover_sound audio.choose activate_sound audio.confirm
            textbutton _("Q.Save") action QuickSave() hover_sound audio.choose activate_sound audio.confirm
            textbutton _("Q.Load") action QuickLoad() hover_sound audio.choose activate_sound audio.confirm
            textbutton _("Prefs") action ShowMenu('preferences') hover_sound audio.choose activate_sound audio.confirm


## This code ensures that the quick_menu screen is displayed in-game, whenever
## the player has not explicitly hidden the interface.
init python:
    config.overlay_screens.append("quick_menu")

default quick_menu = True

style quick_button is default
style quick_button_text is button_text

style quick_button:
    properties gui.button_properties("quick_button")

style quick_button_text:
    properties gui.button_text_properties("quick_button")
    font "ABeeZee-Regular.ttf"


################################################################################
## Main and Game Menu Screens
################################################################################

## Navigation screen ###########################################################
##
## This screen is included in the main and game menus, and provides navigation
## to other menus, and to start the game.

screen navigation():

    vbox:
        style_prefix "navigation"

        xpos gui.navigation_xpos
        yalign 0.5

        spacing gui.navigation_spacing

        if main_menu:

            textbutton _("Start") action Start()

        else:

            textbutton _("History") action ShowMenu("history")

            textbutton _("Save") action ShowMenu("save")

        textbutton _("Load") action ShowMenu("load")

        textbutton _("Preferences") action ShowMenu("preferences")

        if _in_replay:

            textbutton _("End Replay") action EndReplay(confirm=True)

        elif not main_menu:

            textbutton _("Main Menu") action MainMenu()

        if len(persistent.endings) != 0:
            textbutton _("Credits") action ShowMenu("about")


        if renpy.variant("pc"):

            ## The quit button is banned on iOS and unnecessary on Android and
            ## Web.
            textbutton _("Quit") action Quit(confirm=not main_menu)



style navigation_button is gui_button
style navigation_button_text is gui_button_text

style navigation_button:
    size_group "navigation"
    properties gui.button_properties("navigation_button")
    # sounds for main menu buttons scrolling over
    hover_sound audio.choose
    activate_sound audio.confirm

style navigation_button_text:
    properties gui.button_text_properties("navigation_button")


## Main Menu screen ############################################################
##
## Used to display the main menu when Ren'Py starts.
##
## https://www.renpy.org/doc/html/screen_special.html#main-menu

screen main_menu():

    ## This ensures that any other menu screen is replaced.
    tag menu

    if len(persistent.endings) == 0:
        add gui.main_menu_background_0
    elif len(persistent.endings) == 1:
        add gui.main_menu_background_1
    elif len(persistent.endings) == 2:
        add gui.main_menu_background_2
    elif len(persistent.endings) == 3:
        add gui.main_menu_background_3
    elif len(persistent.endings) == 4:
        add gui.main_menu_background_4
    else:
        add gui.main_menu_background_notfound
    add gui.main_menu_logo
    if "finana" in persistent.endings:
        add gui.main_menu_finana
    if "pomu" in persistent.endings:
        add gui.main_menu_pomu
    if "elira" in persistent.endings:
        add gui.main_menu_elira

    ## This empty frame darkens the main menu.
    frame:
        style "main_menu_frame"

    ## The use statement includes another screen inside this one. The actual
    ## contents of the main menu are in the navigation screen.
    use navigation

    if gui.show_name:

        vbox:
            style "main_menu_vbox"

            text "[config.name!t]":
                style "main_menu_title"

            text "[config.version]":
                style "main_menu_version"



style main_menu_frame is empty
style main_menu_vbox is vbox
style main_menu_text is gui_text
style main_menu_title is main_menu_text
style main_menu_version is main_menu_text

style main_menu_frame:
    xsize 420
    yfill True

    background "gui/overlay/main_menu.png"

style main_menu_vbox:
    xalign 1.0
    xoffset -30
    xmaximum 1200
    yalign 1.0
    yoffset -30

style main_menu_text:
    properties gui.text_properties("main_menu", accent=True)

style main_menu_title:
    properties gui.text_properties("title")

style main_menu_version:
    properties gui.text_properties("version")


## Game Menu screen ############################################################
##
## This lays out the basic common structure of a game menu screen. It's called
## with the screen title, and displays the background, title, and navigation.
##
## The scroll parameter can be None, or one of "viewport" or "vpgrid". When
## this screen is intended to be used with one or more children, which are
## transcluded (placed) inside it.

screen game_menu(title, scroll=None, yinitial=0.0):

    # Close menu on right click
    key "mouseup_3" action Return()

    style_prefix "game_menu"

    if main_menu:
        if len(persistent.endings) == 0:
            add gui.main_menu_background_0
        elif len(persistent.endings) == 1:
            add gui.main_menu_background_1
        elif len(persistent.endings) == 2:
            add gui.main_menu_background_2
        elif len(persistent.endings) == 3:
            add gui.main_menu_background_3
        elif len(persistent.endings) == 4:
            add gui.main_menu_background_4
        else:
            add gui.main_menu_background_notfound
    else:
        add gui.game_menu_background

    frame:
        style "game_menu_outer_frame"

        hbox:

            ## Reserve space for the navigation section.
            frame:
                style "game_menu_navigation_frame"

            frame:
                style "game_menu_content_frame"

                if scroll == "viewport":

                    viewport:
                        yinitial yinitial
                        scrollbars "vertical"
                        mousewheel True
                        draggable True
                        pagekeys True

                        side_yfill True

                        vbox:
                            transclude

                elif scroll == "vpgrid":

                    vpgrid:
                        cols 1
                        yinitial yinitial

                        scrollbars "vertical"
                        mousewheel True
                        draggable True
                        pagekeys True

                        side_yfill True

                        transclude

                else:

                    transclude

    use navigation

    textbutton _("Return"):
        style "return_button"
        activate_sound audio.close

        action Return()

    label title

    if main_menu:
        key "game_menu" action ShowMenu("main_menu")
    else:
        key "game_menu" action [ShowMenu("save"), Play("sound", audio.confirm)]


style game_menu_outer_frame is empty
style game_menu_navigation_frame is empty
style game_menu_content_frame is empty
style game_menu_viewport is gui_viewport
style game_menu_side is gui_side
style game_menu_scrollbar is gui_vscrollbar

style game_menu_label is gui_label
style game_menu_label_text is gui_label_text

style return_button is navigation_button
style return_button_text is navigation_button_text

style game_menu_outer_frame:
    bottom_padding 45
    top_padding 180

    background "gui/overlay/game_menu.png"

style game_menu_navigation_frame:
    xsize 420
    yfill True

style game_menu_content_frame:
    left_margin 60
    right_margin 30
    top_margin 15

style game_menu_viewport:
    xsize 1380

style game_menu_vscrollbar:
    unscrollable gui.unscrollable

style game_menu_side:
    spacing 15

style game_menu_label:
    xpos 75
    ysize 180

style game_menu_label_text:
    size gui.title_text_size
    color gui.accent_color
    yalign 0.5

style return_button:
    xpos gui.navigation_xpos
    yalign 1.0
    yoffset -45


## About screen ################################################################
##
## This screen gives credit and copyright information about the game and Ren'Py.
##
## There's nothing special about this screen, and hence it also serves as an
## example of how to make a custom screen.

screen about():

    tag menu

    ## This use statement includes the game_menu screen inside this one. The
    ## vbox child is then included inside the viewport inside the game_menu
    ## screen.
    use game_menu(_("Credits"), scroll="viewport"):

        style_prefix "about"

        vbox:

            label "[config.name!t]"
            text _("Version [config.version!t]\n")

            # One long text block causes weird artifacting, so split it
            text "[gui.about.management!t]\n"
            text "[gui.about.writing!t]\n"
            text "[gui.about.art!t]\n"
            text "[gui.about.programming!t]\n"
            text "[gui.about.bgm!t]\n"
            text "[gui.about.video!t]\n"
            text "[gui.about.misc!t]\n"

            text _("Made with {a=https://www.renpy.org/}Ren'Py{/a} [renpy.version_only].\n\n[renpy.license!t]")


style about_label is gui_label
style about_label_text is gui_label_text
style about_text is gui_text

style about_label_text:
    size gui.label_text_size

style about_text:
    font "ABeeZee-Regular.ttf"
    color "#fff"
    size 45


## Load and Save screens #######################################################
##
## These screens are responsible for letting the player save the game and load
## it again. Since they share nearly everything in common, both are implemented
## in terms of a third screen, file_slots.
##
## https://www.renpy.org/doc/html/screen_special.html#save https://
## www.renpy.org/doc/html/screen_special.html#load

screen save():

    tag menu

    use file_slots(_("Save"))


screen load():

    tag menu

    use file_slots(_("Load"))


screen file_slots(title):
    # Close menu on escape
    key "game_menu" action [Return(), Play("sound", audio.close)]

    default page_name_value = FilePageNameInputValue(pattern=_("Page {}"), auto=_("Automatic saves"), quick=_("Quick saves"))
    if title == "Save":
        add "gui/bg_save.png"
    else:
        add "gui/bg_load.png"

    fixed:

        ## This ensures the input will get the enter event before any of the
        ## buttons do.
        order_reverse True

        ## The page name, which can be edited by clicking on a button.
        button:
            style "page_label"

            key_events True
            xalign 0.5
            yalign 0.18
            action page_name_value.Toggle()

            hover_sound audio.choose
            activate_sound audio.confirm

            input:
                if title == "Save":
                    style "save_label_text"
                else:
                    style "load_label_text"
                value page_name_value
                length 46

        ## The grid of file slots.
        grid gui.file_slot_cols gui.file_slot_rows:
            if title == "Save":
                style_prefix "save_slot"
            else:
                style_prefix "load_slot"

            xalign 0.5
            yalign 0.62

            spacing gui.slot_spacing
            yspacing 40

            for i in range(gui.file_slot_cols * gui.file_slot_rows):

                $ slot = i + 1

                button:
                    hover_sound audio.choose
                    activate_sound audio.confirm

                    action FileAction(slot)

                    has vbox
                    xalign 0.5
                    yoffset -2
                    if FileLoadable(slot):
                        add AlphaMask(Composite(
                            (405, 224),
                            (0, 0), FileScreenshot(slot),
                            (0, 0), "gui/saveload_overlay.png"),
                            "gui/saveload_mask.png")
                    else:
                        add AlphaMask(FileScreenshot(slot), "gui/saveload_mask.png")

                    null height 10

                    text FileTime(slot, format=_("{#file_time}%A, %B %d %Y, %H:%M"), empty=_("empty slot")):
                        if title == "Save":
                            style "save_slot_time_text"
                        else:
                            style "load_slot_time_text"

                    text FileSaveName(slot):
                        style "slot_name_text"

                    key "save_delete" action FileDelete(slot)

        ## Buttons to access other pages.
        hbox:
            style_prefix "page"

            xalign 0.2
            yalign 0.95

            spacing gui.page_spacing

            textbutton _("<") action FilePagePrevious() hover_sound audio.choose activate_sound audio.confirm

            if config.has_autosave:
                textbutton _("{#auto_page}A") action FilePage("auto") hover_sound audio.choose activate_sound audio.confirm

            if config.has_quicksave:
                textbutton _("{#quick_page}Q") action FilePage("quick") hover_sound audio.choose activate_sound audio.confirm

            ## range(1, 10) gives the numbers from 1 to 9.
            for page in range(1, 10):
                textbutton "[page]" action FilePage(page) hover_sound audio.choose activate_sound audio.confirm

            textbutton _(">") action FilePageNext() hover_sound audio.choose activate_sound audio.confirm
        # Footer buttons
        hbox:
            xalign 1.0
            yalign 0.95
            xoffset -50
            spacing 20
            if title == "Save":
                imagebutton auto "gui/button/save_load_%s.png" action ShowMenu("load") hover_sound audio.choose activate_sound audio.confirm
                imagebutton auto "gui/button/save_back_%s.png" action Return() hover_sound audio.choose activate_sound audio.confirm
            else:
                imagebutton auto "gui/button/load_save_%s.png" action ShowMenu("save") hover_sound audio.choose activate_sound audio.confirm
                imagebutton auto "gui/button/load_back_%s.png" action Return() hover_sound audio.choose activate_sound audio.confirm


style page_label is gui_label
style page_label_text is gui_label_text
style page_button is gui_button
style page_button_text is gui_button_text

style slot_button is gui_button
style slot_button_text is gui_button_text
style slot_time_text is slot_button_text
style slot_name_text is slot_button_text

style save_label_text is page_label_text
style load_label_text is page_label_text

style save_slot_button is slot_button
style save_slot_button_text is slot_button_text
style save_slot_time_text is slot_time_text
style save_slot_name_text is slot_name_text

style load_slot_button is slot_button
style load_slot_button_text is slot_button_text
style load_slot_time_text is slot_time_text
style load_slot_name_text is slot_name_text

style page_label:
    xpadding 75
    ypadding 5

style page_label_text:
    text_align 0.5
    layout "subtitle"
    size 63
    color u"#fff"
    font "DancingScript.ttf"

style save_label_text:
    outlines [(7, "#62d2c9", 0, 0)]

style load_label_text:
    outlines [(7, "#68d698", 0, 0)]

style page_button:
    properties gui.button_properties("page_button")

style page_button_text:
    properties gui.button_text_properties("page_button")
    idle_color u"#b0b1b3"
    selected_color u"#cf7dc4"
    hover_color u"#eab1e4"
    outlines []
    hover_outlines []
    font "AaronScript.otf"

style slot_button:
    properties gui.button_properties("slot_button")


style save_slot_button:
    background "gui/button/save_slot_[prefix_]background.png"

style load_slot_button:
    background "gui/button/load_slot_[prefix_]background.png"

style slot_button_text:
    properties gui.button_text_properties("slot_button")

style slot_time_text:
    font "ABeeZee-Regular.ttf"
    size 22
    color u"#fff"

style save_slot_time_text:
    outlines [(3, "#62d2c9", 0, 0)]
    hover_outlines [(3, "#89eae5", 0, 0)]

style load_slot_time_text:
    outlines [(3, "#68d698", 0, 0)]
    hover_outlines [(3, "#a9ecb3", 0, 0)]


## Preferences screen ##########################################################
##
## The preferences screen allows the player to configure the game to better suit
## themselves.
##
## https://www.renpy.org/doc/html/screen_special.html#preferences

screen preferences():
    # Close menu on right click
    key "mouseup_3" action [Return(), Play("sound", audio.close)]
    # Close menu on escape
    key "game_menu" action [Return(), Play("sound", audio.close)]

    tag menu
    style_prefix "pref"
    add "gui/bg_settings.png"
    hbox:
        ypos 200
        xalign 0.5
        # Left column
        vbox:
            spacing gui.pref_spacing
            xalign 0.5
            label _("Display Settings")
            if renpy.variant("pc") or renpy.variant("web"):
                hbox:
                    style_prefix "pref_buttons"
                    imagebutton auto "gui/button/settings_windowed_%s.png" action Preference("display", "window") hover_sound audio.choose activate_sound audio.confirm
                    imagebutton auto "gui/button/settings_fullscreen_%s.png" action Preference("display", "fullscreen") hover_sound audio.choose activate_sound audio.confirm
            hbox:
                style_prefix "pref_inline_slider"
                label _("Text Speed")
                bar value Preference("text speed")
            hbox:
                style_prefix "pref_inline_slider"
                label _("Auto Speed")
                bar value Preference("auto-forward time") bar_invert True
            label _("Skip Transitions")
            hbox:
                style_prefix "pref_buttons"
                box_wrap True
                imagebutton auto "gui/button/settings_unseen_text_%s.png" action Preference("skip", "toggle") hover_sound audio.choose activate_sound audio.confirm
                imagebutton auto "gui/button/settings_transitions_%s.png" action InvertSelected(Preference("transitions", "toggle")) hover_sound audio.choose activate_sound audio.confirm
                imagebutton auto "gui/button/settings_after_choices_%s.png" action Preference("after choices", "toggle") hover_sound audio.choose activate_sound audio.confirm
            hbox:
                style_prefix "pref_inline_slider"
                label _("Skip Speed")
                bar:
                    value FieldValue(persistent, "skip_speed", step=1.0, offset=5, range=300, style="slider", action=SetField(config, "skip_delay", persistent.skip_speed))
                    bar_invert True
                    alt _("Skip Speed")
            vbox:
                style_prefix "pref_slider"
                label _("Dialogue Box Opacity")
                bar value FieldValue(persistent, "TextBoxAlpha", range=1.0, style="slider")
        # Spacer
        null width 200
        # Right column
        vbox:
            xalign 0.5

            label _("Sound Settings")
            if config.has_music:
                vbox:
                    style_prefix "pref_slider"
                    label _("Music Volume")
                    bar value Preference("music volume")

            if config.has_sound:
                vbox:
                    style_prefix "pref_slider"
                    label _("Sound Volume")
                    bar value Preference("sound volume")

                    if config.sample_sound:
                        textbutton _("Test") action Play("sound", config.sample_sound)


            if config.has_voice:
                vbox:
                    style_prefix "pref_slider"
                    label _("Voice Volume")
                    bar value Preference("voice volume")

                    if config.sample_voice:
                        textbutton _("Test") action Play("voice", config.sample_voice)

            if config.has_music or config.has_sound or config.has_voice:
                vbox:
                    style_prefix "pref_buttons"
                    null height gui.pref_spacing
                    imagebutton auto "gui/button/settings_mute_all_%s.png" action Preference("all mute", "toggle") hover_sound audio.choose activate_sound audio.confirm
            null height 40
            hbox:
                spacing gui.pref_button_spacing
                label _("Player Name")
                imagebutton auto "gui/button/settings_change_name_%s.png" action Show("name_prompt") hover_sound audio.choose activate_sound audio.confirm

            imagebutton auto "gui/button/settings_reset_%s.png" action [
                Preference("skip", "seen"),
                Preference("transitions", "all"),
                Preference("after choices", "stop"),
                Preference("music volume", 0.4),
                Preference("sound volume", 0.4),
                Preference("text speed", 40),
                Preference("auto-forward time", 15),
                Function(reset_custom_settings)
                ] hover_sound audio.choose activate_sound audio.confirm

    # Left footer
    hbox:
        yalign 0.95
        xoffset 50
        imagebutton auto "gui/button/settings_nuke_%s.png" action Confirm("This will reset EVERYTHING. Are you sure?", Function(true_reset)) hover_sound audio.choose activate_sound audio.confirm
    # Right footer
    hbox:
        xalign 1.0
        yalign 0.95
        xoffset -50
        imagebutton auto "gui/button/settings_exit_%s.png" action Quit(confirm = not main_menu) hover_sound audio.choose activate_sound audio.confirm
        if not main_menu:
            imagebutton auto "gui/button/settings_title_%s.png" action MainMenu() hover_sound audio.choose activate_sound audio.confirm
        imagebutton auto "gui/button/settings_back_%s.png" action Return() hover_sound audio.choose activate_sound audio.close


style pref_label_text is gui_label_text

style pref_buttons_label_text is pref_label_text
style pref_buttons_hbox is pref_boxes
style pref_buttons_vbox is pref_boxes

style pref_slider_label_text is pref_label_text
style pref_slider_slider is gui_slider
style pref_slider_button is gui_button
style pref_slider_button_text is gui_button_text
style pref_slider_hbox is pref_boxes
style pref_slider_vbox is pref_boxes

style pref_inline_slider_label_text is pref_slider_label_text
style pref_inline_slider_slider is pref_slider_slider
style pref_inline_slider_hbox is pref_slider_hbox

style pref_boxes:
    xoffset 20
    spacing gui.pref_button_spacing

style pref_label_text:
    font "ABeeZee-Regular.ttf"
    color u"#fff"
    size 46
    outlines [ (12, u"#ffffff20", 0, 0),
        (11, u"#ffffff20", 0, 0),
        (10, u"#ffffff20", 0, 0),
        (9, u"#ffffff20", 0, 0),
        (5, u"#c984c0", 0, 0) ]

style pref_buttons_label_text:
    size 42

style pref_buttons_hbox:
    xmaximum 700

style pref_slider_label_text:
    size 42

style pref_slider_slider:
    xsize 478
    yalign 0.6

style pref_slider_button:
    properties gui.button_properties("slider_button")
    yalign 0.5
    left_margin 15


style pref_slider_button_text:
    properties gui.button_text_properties("slider_button")

style pref_inline_slider_label:
    xsize 270

## History screen ##############################################################
##
## This is a screen that displays the dialogue history to the player. While
## there isn't anything special about this screen, it does have to access the
## dialogue history stored in _history_list.
##
## https://www.renpy.org/doc/html/history.html

screen history():

    # Close history on mouse scroll down
    key "mousedown_5" action [Return(), Play("sound", audio.close)]
    # Close history on right click
    key "mouseup_3" action [Return(), Play("sound", audio.close)]

    tag menu

    add gui.history
    ## Avoid predicting this screen, as it can be very large.
    predict False

    viewport:
        style_prefix "history"
        yinitial 1.0

        xanchor 0.5
        xpos 1000
        yanchor 0.0
        ypos 150

        xmaximum 1770
        ymaximum 890

        draggable True
        mousewheel "change"
        scrollbars "vertical"

        vbox:
            for h in _history_list:

                window:

                    ## This lays things out properly if history_height is None.
                    has fixed:
                        yfit True

                    if h.who:

                        label h.who:
                            style "history_name"
                            substitute False

                            ## Take the color of the who text from the Character, if
                            ## set.
                            if "color" in h.who_args:
                                text_color h.who_args["color"]

                    if h.rollback_identifier:
                        imagebutton:
                            ypos 40
                            idle "gui/button/backlog_jump_idle.png"
                            hover "gui/button/backlog_jump_hover.png"
                            action Confirm("Return to this point?", RollbackToIdentifier(h.rollback_identifier))
                            hover_sound audio.choose
                            activate_sound audio.confirm

                    $ what = renpy.filter_text_tags(h.what, allow=gui.history_allow_tags)
                    text what:
                        substitute False

                    null height 175 #bottom padding

            if not _history_list:
                label _("The dialogue history is empty.")

    imagebutton:
        xpos 1500
        ypos 950
        idle "gui/button/settings_back_idle.png"
        hover "gui/button/settings_back_hover.png"
        hover_sound audio.choose
        activate_sound audio.close
        action Return()
## This determines what tags are allowed to be displayed on the history screen.

define gui.history_allow_tags = { "alt", "noalt" }


style history_window is empty

style history_name is gui_label
style history_name_text is gui_label_text
style history_text is gui_text

style history_text is gui_text

style history_label is gui_label
style history_label_text is gui_label_text

style history_window:
    xfill True
    ysize gui.history_height

style history_name:
    xpos gui.history_name_xpos
    xanchor gui.history_name_xalign
    ypos gui.history_name_ypos
    xsize gui.history_name_width

style history_name_text:
    font "ABeeZee-Regular.ttf"
    size 42
    #outlines [(2, u"#fff", 0, 0) ] #uncomment to change outline to white
    min_width gui.history_name_width
    text_align gui.history_name_xalign

style history_text:
    font "OpenSans.ttf"
    size 32
    color u"#fff"
    outlines [(2, u"#7c3673", 0, 0) ]
    xpos gui.history_text_xpos
    ypos gui.history_text_ypos
    xanchor gui.history_text_xalign
    xsize gui.history_text_width
    min_width gui.history_text_width
    text_align gui.history_text_xalign
    layout ("subtitle" if gui.history_text_xalign else "tex")

style history_label:
    xfill True

style history_label_text:
    xalign 0.5

style history_slider:
    thumb_offset 11


## Help screen #################################################################
##
## A screen that gives information about key and mouse bindings. It uses other
## screens (keyboard_help, mouse_help, and gamepad_help) to display the actual
## help.

screen help():

    tag menu

    default device = "keyboard"

    use game_menu(_("Help"), scroll="viewport"):

        style_prefix "help"

        vbox:
            spacing 23

            hbox:

                textbutton _("Keyboard") action SetScreenVariable("device", "keyboard")
                textbutton _("Mouse") action SetScreenVariable("device", "mouse")

                if GamepadExists():
                    textbutton _("Gamepad") action SetScreenVariable("device", "gamepad")

            if device == "keyboard":
                use keyboard_help
            elif device == "mouse":
                use mouse_help
            elif device == "gamepad":
                use gamepad_help


screen keyboard_help():

    hbox:
        label _("Enter")
        text _("Advances dialogue and activates the interface.")

    hbox:
        label _("Space")
        text _("Advances dialogue without selecting choices.")

    hbox:
        label _("Arrow Keys")
        text _("Navigate the interface.")

    hbox:
        label _("Escape")
        text _("Accesses the game menu.")

    hbox:
        label _("Ctrl")
        text _("Skips dialogue while held down.")

    hbox:
        label _("Tab")
        text _("Toggles dialogue skipping.")

    hbox:
        label _("Page Up")
        text _("Rolls back to earlier dialogue.")

    hbox:
        label _("Page Down")
        text _("Rolls forward to later dialogue.")

    hbox:
        label "H"
        text _("Hides the user interface.")

    hbox:
        label "S"
        text _("Takes a screenshot.")

    hbox:
        label "V"
        text _("Toggles assistive {a=https://www.renpy.org/l/voicing}self-voicing{/a}.")

    hbox:
        label "Shift+A"
        text _("Opens the accessibility menu.")


screen mouse_help():

    hbox:
        label _("Left Click")
        text _("Advances dialogue and activates the interface.")

    hbox:
        label _("Middle Click")
        text _("Hides the user interface.")

    hbox:
        label _("Right Click")
        text _("Accesses the game menu.")

    hbox:
        label _("Mouse Wheel Up")
        text _("Shows dialogue history.")

    hbox:
        label _("Mouse Wheel Down")
        text _("Hides dialogue history.")


screen gamepad_help():

    hbox:
        label _("Right Trigger\nA/Bottom Button")
        text _("Advances dialogue and activates the interface.")

    hbox:
        label _("Left Trigger\nLeft Shoulder")
        text _("Rolls back to earlier dialogue.")

    hbox:
        label _("Right Shoulder")
        text _("Rolls forward to later dialogue.")


    hbox:
        label _("D-Pad, Sticks")
        text _("Navigate the interface.")

    hbox:
        label _("Start, Guide")
        text _("Accesses the game menu.")

    hbox:
        label _("Y/Top Button")
        text _("Hides the user interface.")

    textbutton _("Calibrate") action GamepadCalibrate()


style help_button is gui_button
style help_button_text is gui_button_text
style help_label is gui_label
style help_label_text is gui_label_text
style help_text is gui_text

style help_button:
    properties gui.button_properties("help_button")
    xmargin 12

style help_button_text:
    properties gui.button_text_properties("help_button")

style help_label:
    xsize 375
    right_padding 30

style help_label_text:
    size gui.text_size
    xalign 1.0
    text_align 1.0



################################################################################
## Additional screens
################################################################################


## Confirm screen ##############################################################
##
## The confirm screen is called when Ren'Py wants to ask the player a yes or no
## question.
##
## https://www.renpy.org/doc/html/screen_special.html#confirm

screen confirm(message, yes_action, no_action):

    ## Ensure other screens do not get input while this screen is displayed.
    modal True

    zorder 200

    style_prefix "confirm"

    add "gui/overlay/confirm.png"

    frame:

        vbox:
            xalign .5
            yalign .5
            spacing 45

            label _(message):
                style "confirm_prompt"
                xalign 0.5

            hbox:
                xalign 0.5
                spacing 150
                imagebutton auto "gui/button/prompt_yes_%s.png" action yes_action hover_sound audio.choose activate_sound audio.confirm
                imagebutton auto "gui/button/prompt_no_%s.png" action no_action hover_sound audio.choose activate_sound audio.close

    ## Right-click and escape answer "no".
    key "game_menu" action [no_action, Play("sound", audio.close)]


style confirm_frame is gui_frame
style confirm_prompt is gui_prompt
style confirm_prompt_text is gui_prompt_text
style confirm_button is gui_medium_button
style confirm_button_text is gui_medium_button_text

style confirm_frame:
    background Frame([ "gui/prompt_box.png", "gui/prompt_box.png"], gui.confirm_frame_borders, tile=gui.frame_tile)
    padding gui.confirm_frame_borders.padding
    xalign .5
    yalign .5

style confirm_prompt_text:
    text_align 0.5
    layout "subtitle"

style confirm_button:
    properties gui.button_properties("confirm_button")

style confirm_button_text:
    properties gui.button_text_properties("confirm_button")

style confirm_prompt_text:
    font "ABeeZee-Regular.ttf"
    color u"#fff"
    size 46
    outlines [ (12, u"#ffffff20", 0, 0),
        (11, u"#ffffff20", 0, 0),
        (10, u"#ffffff20", 0, 0),
        (9, u"#ffffff20", 0, 0),
        (4, u"#c984c0", 0, 0) ]


init python:
    # if the persistant name is blank choose from a list/tupple
    from random import choice
    def fix_name():
        if not persistent.mcName:
            # Attempting to be a list of joke/meme names
            persistent.mcName = choice(
                (
                    "Tazumi",
                    "Pomudachi",
                    "Rosebud",
                    "Enzo",
                    "Pog-san",
                    "Daredemo-san",
                    "Yuu",
                    "Ryu Fameldachi",
                    "Famel Guardachi",
                    "Daisuke",
                    "D. Nutz",
                    # if we're doing joke names go full joke names
                    "Koitsu",
                    "Aitsu",
                    "Soitsu",
                    "Doitsu"
                )
            )

screen name_prompt():
    modal True
    zorder 200
    style_prefix "confirm" # Use same styles as confirm prompt
    frame:
        vbox:
            xalign .5
            yalign .5
            xsize 700
            text "Please enter your name" style "confirm_name_prompt_text" xalign .5
            text "The gender of the protagonist is not decided in this game,so you are free to imagine them" style "confirm_name_prompt_subtext"
            text "as you like" style "confirm_name_prompt_subtext" xalign .5
            null height 20
            input:
                value FieldInputValue(persistent, "mcName")
                xalign 0.5
                length 20
            null height 20

            # Using multiple actions by encapsulating in square brackets.
            # fix_name will check if mcName is entered, if not then it will pull from a
            # list. Then the name_prompt is hidden or returns, depending on where it was
            # called from.
            imagebutton:
                auto "gui/button/prompt_confirm_%s.png"
                action [
                    Function(fix_name),
                    If(_menu, true=Hide("name_prompt"), false=Return())
                ]
                xalign 0.5
                hover_sound audio.choose activate_sound audio.confirm

style confirm_name_prompt_text:
    font "ABeeZee-Regular.ttf"
    color u"#fff"
    size 42
    outlines [ (12, u"#ffffff20", 0, 0),
        (11, u"#ffffff20", 0, 0),
        (10, u"#ffffff20", 0, 0),
        (9, u"#ffffff20", 0, 0),
        (4, u"#c984c0", 0, 0) ]

style confirm_name_prompt_subtext:
    font "ABeeZee-Regular.ttf"
    color u"#c984c0"
    size 32

## Skip indicator screen #######################################################
##
## The skip_indicator screen is displayed to indicate that skipping is in
## progress.
##
## https://www.renpy.org/doc/html/screen_special.html#skip-indicator

screen skip_indicator():

    zorder 100
    style_prefix "skip"

    frame:

        hbox:
            spacing 9

            text _("Skipping")

            text "▸" at delayed_blink(0.0, 1.0) style "skip_triangle"
            text "▸" at delayed_blink(0.2, 1.0) style "skip_triangle"
            text "▸" at delayed_blink(0.4, 1.0) style "skip_triangle"


## This transform is used to blink the arrows one after another.
transform delayed_blink(delay, cycle):
    alpha .5

    pause delay

    block:
        linear .2 alpha 1.0
        pause .2
        linear .2 alpha 0.5
        pause (cycle - .4)
        repeat


style skip_frame is empty
style skip_text is gui_text
style skip_triangle is skip_text

style skip_frame:
    ypos gui.skip_ypos
    background Frame("gui/skip.png", gui.skip_frame_borders, tile=gui.frame_tile)
    padding gui.skip_frame_borders.padding

style skip_text:
    size gui.notify_text_size

style skip_triangle:
    ## We have to use a font that has the BLACK RIGHT-POINTING SMALL TRIANGLE
    ## glyph in it.
    font "DejaVuSans.ttf"


## Notify screen ###############################################################
##
## The notify screen is used to show the player a message. (For example, when
## the game is quicksaved or a screenshot has been taken.)
##
## https://www.renpy.org/doc/html/screen_special.html#notify-screen

screen notify(message):

    zorder 100
    style_prefix "notify"

    frame at notify_appear:
        if "screenshot" in message:
            text "Better be careful. If we hadn't changed this, it would have shown your computer username."
        else:
            text "[message!tq]"

    timer 3.25 action Hide('notify')


transform notify_appear:
    on show:
        alpha 0
        linear .25 alpha 1.0
    on hide:
        linear .5 alpha 0.0


style notify_frame is empty
style notify_text is gui_text

style notify_frame:
    ypos gui.notify_ypos

    background Frame("gui/notify.png", gui.notify_frame_borders, tile=gui.frame_tile)
    padding gui.notify_frame_borders.padding

style notify_text:
    properties gui.text_properties("notify")


## NVL screen ##################################################################
##
## This screen is used for NVL-mode dialogue and menus.
##
## https://www.renpy.org/doc/html/screen_special.html#nvl


screen nvl(dialogue, items=None):

    window:
        style "nvl_window"

        has vbox:
            spacing gui.nvl_spacing

        ## Displays dialogue in either a vpgrid or the vbox.
        if gui.nvl_height:

            vpgrid:
                cols 1
                yinitial 1.0

                use nvl_dialogue(dialogue)

        else:

            use nvl_dialogue(dialogue)

        ## Displays the menu, if given. The menu may be displayed incorrectly if
        ## config.narrator_menu is set to True, as it is above.
        for i in items:

            textbutton i.caption:
                action i.action
                style "nvl_button"

    add SideImage() xalign 0.0 yalign 1.0


screen nvl_dialogue(dialogue):

    for d in dialogue:

        window:
            id d.window_id

            fixed:
                yfit gui.nvl_height is None

                if d.who is not None:

                    text d.who:
                        id d.who_id

                text d.what:
                    id d.what_id


## This controls the maximum number of NVL-mode entries that can be displayed at
## once.
define config.nvl_list_length = gui.nvl_list_length

style nvl_window is default
style nvl_entry is default

style nvl_label is say_label
style nvl_dialogue is say_dialogue

style nvl_button is button
style nvl_button_text is button_text

style nvl_window:
    xfill True
    yfill True

    background "gui/nvl.png"
    padding gui.nvl_borders.padding

style nvl_entry:
    xfill True
    ysize gui.nvl_height

style nvl_label:
    xpos gui.nvl_name_xpos
    xanchor gui.nvl_name_xalign
    ypos gui.nvl_name_ypos
    yanchor 0.0
    xsize gui.nvl_name_width
    min_width gui.nvl_name_width
    text_align gui.nvl_name_xalign

style nvl_dialogue:
    xpos gui.nvl_text_xpos
    xanchor gui.nvl_text_xalign
    ypos gui.nvl_text_ypos
    xsize gui.nvl_text_width
    min_width gui.nvl_text_width
    text_align gui.nvl_text_xalign
    layout ("subtitle" if gui.nvl_text_xalign else "tex")

style nvl_thought:
    xpos gui.nvl_thought_xpos
    xanchor gui.nvl_thought_xalign
    ypos gui.nvl_thought_ypos
    xsize gui.nvl_thought_width
    min_width gui.nvl_thought_width
    text_align gui.nvl_thought_xalign
    layout ("subtitle" if gui.nvl_text_xalign else "tex")

style nvl_button:
    properties gui.button_properties("nvl_button")
    xpos gui.nvl_button_xpos
    xanchor gui.nvl_button_xalign

style nvl_button_text:
    properties gui.button_text_properties("nvl_button")



################################################################################
## Mobile Variants
################################################################################

style pref_vbox:
    variant "medium"
    xsize 675

## Since a mouse may not be present, we replace the quick menu with a version
## that uses fewer and bigger buttons that are easier to touch.
screen quick_menu():
    variant "touch"

    zorder 100

    if quick_menu:

        hbox:
            style_prefix "quick"

            xalign 0.5
            yalign 1.0

            textbutton _("Back") action Rollback()
            textbutton _("Skip") action Skip() alternate Skip(fast=True, confirm=True)
            textbutton _("Auto") action Preference("auto-forward", "toggle")
            textbutton _("Menu") action ShowMenu()


style window:
    variant "small"
    background "gui/phone/textbox.png"

style radio_button:
    variant "small"
    foreground "gui/phone/button/radio_[prefix_]foreground.png"

style check_button:
    variant "small"
    foreground "gui/phone/button/check_[prefix_]foreground.png"

style nvl_window:
    variant "small"
    background "gui/phone/nvl.png"

style main_menu_frame:
    variant "small"
    background "gui/phone/overlay/main_menu.png"

style game_menu_outer_frame:
    variant "small"
    background "gui/phone/overlay/game_menu.png"

style game_menu_navigation_frame:
    variant "small"
    xsize 510

style game_menu_content_frame:
    variant "small"
    top_margin 0

style pref_vbox:
    variant "small"
    xsize 600

style bar:
    variant "small"
    ysize gui.bar_size
    left_bar Frame("gui/phone/bar/left.png", gui.bar_borders, tile=gui.bar_tile)
    right_bar Frame("gui/phone/bar/right.png", gui.bar_borders, tile=gui.bar_tile)

style vbar:
    variant "small"
    xsize gui.bar_size
    top_bar Frame("gui/phone/bar/top.png", gui.vbar_borders, tile=gui.bar_tile)
    bottom_bar Frame("gui/phone/bar/bottom.png", gui.vbar_borders, tile=gui.bar_tile)

style scrollbar:
    variant "small"
    ysize gui.scrollbar_size
    base_bar Frame("gui/phone/scrollbar/horizontal_[prefix_]bar.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/phone/scrollbar/horizontal_[prefix_]thumb.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)

style vscrollbar:
    variant "small"
    xsize gui.scrollbar_size
    base_bar Frame("gui/phone/scrollbar/vertical_[prefix_]bar.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/phone/scrollbar/vertical_[prefix_]thumb.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)

style slider:
    variant "small"
    ysize gui.slider_size
    base_bar Frame("gui/phone/slider/horizontal_[prefix_]bar.png", gui.slider_borders, tile=gui.slider_tile)
    thumb "gui/phone/slider/horizontal_[prefix_]thumb.png"

style vslider:
    variant "small"
    xsize gui.slider_size
    base_bar Frame("gui/phone/slider/vertical_[prefix_]bar.png", gui.vslider_borders, tile=gui.slider_tile)
    thumb "gui/phone/slider/vertical_[prefix_]thumb.png"

style slider_vbox:
    variant "small"
    xsize None

style slider_slider:
    variant "small"
    xsize 900
