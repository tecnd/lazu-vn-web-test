## This file contains options that can be changed to customize your game.
##
## Lines beginning with two '#' marks are comments, and you shouldn't uncomment
## them. Lines beginning with a single '#' mark are commented-out code, and you
## may want to uncomment them when appropriate.


## Basics ######################################################################

## A human-readable name of the game. This is used to set the default window
## title, and shows up in the interface and error reports.
##
## The _() surrounding the string marks it as eligible for translation.

define config.name = _("Lazulight: By Your Side")


## Determines if the title given above is shown on the main menu screen. Set
## this to False to hide the title.

define gui.show_name = False


## The version of the game.

define config.version = "1.0-DEMO"


## Text that is placed on the game's about screen. Place the text between the
## triple-quotes, and leave a blank line between paragraphs.

define gui.about.management = _p(u"""
{u}{size=+10}Management Team:{/size}{/u}

Organizer & Producer:{p}
Kiro

VN Team Leader & Producer:{p}
SinSin

VN Team Assistant Leader:{p}
Carateca
""")

define gui.about.writing = _p(u"""
{u}{size=+10}Writing Team:{/size}{/u}

Writing Team Leader:{p}
Zephyr Monochrome

Scenario:{p}
Zephyr Monochrome{p}
Akatsukin

Common Route Writer:{p}
Zephyr Monochrome

Elira Route Writer:{p}
ShittyDrawer’s Den

Pomu Route Writer:{p}
Akatsukin

Finana Route Writer:{p}
Keektang{p}
The Holy Wooomy with 69 Nuggets of Toasted Squidies

??? Route Writer:{p}
Akatsukin

Proofreaders:{p}
Johnny Lacone{p}
wildnexus{p}
Zephyr Kitten{p}
JFND{p}
Saeren{p}
Calix{p}
Erawan
""")

define gui.about.art = _p("""
{u}{size=+10}Art Team:{/size}{/u}

Art Team Leader (Organizational):{p}
The Holy Wooomy with 69 Nuggets of Toasted Squidies

Art Team Leader (Art QC & Feedback):{p}
Ann_TeaSocial

{u}Sprite Artists:{/u}

Elira Sprites:{p}
Ann_TeaSocial{p}
Lost B'unny

Pomu Sprites:{p}
MizMillificent

Finana Sprites:{p}
Amechi (Lineart){p}
Vitaminechan (Colouring)

Selen Sprites:{p}
Grim

Rosemi Sprites:{p}
Yuki Baskerville{p}
Arien

Petra Sprites:{p}
Amechi

Oliver-sensei Sprites:{p}
Bee

Pikl Sprites:{p}
ShittyDrawer’s Den

{u}CG Artists:{/u}{p}
Anatom{p}
Guda{p}
R5{p}
Squish{p}
Syxh{p}
VonB{p}
Nattsume{p}
Aeri{p}
tsukinaga{p}
Dokuro_DX{p}
naokomama{p}
sleepy{p}
Takezo{p}
A.Cat{p}
{font=MSGothic.ttf}ひつじ{/font}{p}
Name Taken{p}
Alice Vu{p}
Arien{p}
FragileQ{p}
Neroshi{p}
RockyBirdy

{u}Backgrounds:{/u}{p}
Ajani Akasakaspicy{p}
Arien{p}
arqo{p}
Bee{p}
fyretruck{p}
Lost B'unny{p}
Michi{p}
Squish{p}
wizwaaz

{u}UI/Assets:{/u}{p}
A.Cat{p}
juice{p}
Michi{p}
mrj{p}
Takezo{p}
The Holy Wooomy with 69 Nuggets of Toasted Squidies{p}
questipher{p}
Zephyr Monochrome
""")

define gui.about.programming = _p("""
{u}{size=+10}Programming Team:{/size}{/u}

Programming Team Leader:{p}
Usaruru{p}
tecnd

Programmers:{p}
tecnd{p}
kana²{p}
BadScribbler{p}
mrj{p}
SinSin{p}
tsukinaga

Visual Novel Engine:{p}
Ren’Py
""")

define gui.about.bgm = _p("""
{u}{size=+10}BGM Team:{/size}{/u}

BGM Team Leader:{p}
Kiro

BGM Team Assistant Leader:{p}
breeziness

Composers:{p}
Nikolai Levnekov{p}
breeziness{p}
SonicFan53

Instrumentalists:{p}
Pendora’s Box (Guitar){p}
Hiiragi Emuri (Violin)

Sound Effects:{p}
freesound.org under the CC0 license
""")

define gui.about.video = _p("""
{u}{size=+10}Video Team:{/size}{/u}

Video Team Leaders:{p}
Kiro{p}
kana²

Video Editors:{p}
PomuPower Distribution Center (Opening Video){p}
Pendora’s Box (Credits)
""")

define gui.about.misc = _p("""
{u}{size=+10}Community Feedback:{/size}{/u}

Initial Scenario Ideas:{p}
Zephyr Monochrome{p}
suminoja{p}
Akatsukin{p}
ShittyDrawer’s Den{p}
Kei Shiromiya

Feedback:{p}
Gonxaleo{p}
Feetman69{p}
JFND{p}
kana²{p}
All VN Team Members

Feet Quality Inspector:{p}
Feetman69

{u}{size=+10}Special Thanks To:{/size}{/u}{p}
LazuLight 1st Anniversary Website Team{p}
Nijisanji EN Fan Discord Server{p}
Elicord Discord Server{p}
Pomucord Discord Server{p}
Finanacord Discord Server{p}
PPDC’s Right Hand

And every member of the NijiEN community who helped us out, or showed their support for our project!
""")

## additional persistent variables here
# handles textbox opacity
default persistent.TextBoxAlpha = 0.9

# handles skip speed
default persistent.skip_speed = 75

## A short name for the game used for executables and directories in the built
## distribution. This must be ASCII-only, and must not contain spaces, colons,
## or semicolons.

define build.name = "LazulightVN"


## Sounds and music ############################################################

## These three variables control, among other things, which mixers are shown
## to the player by default. Setting one of these to False will hide the
## appropriate mixer.

define config.has_sound = True
define config.has_music = True
define config.has_voice = False


## To allow the user to play a test sound on the sound or voice channel,
## uncomment a line below and use it to set a sample sound to play.

# define config.sample_sound = "sample-sound.ogg"
# define config.sample_voice = "sample-voice.ogg"


## Uncomment the following line to set an audio file that will be played while
## the player is at the main menu. This file will continue playing into the
## game, until it is stopped or another file is played.

define config.main_menu_music = audio.bgm_main_menu


## Transitions #################################################################
##
## These variables set transitions that are used when certain events occur.
## Each variable should be set to a transition, or None to indicate that no
## transition should be used.

## Entering or exiting the game menu.

define config.enter_transition = dissolve
define config.exit_transition = dissolve


## Between screens of the game menu.

define config.intra_transition = dissolve


## A transition that is used after a game has been loaded.

define config.after_load_transition = None


## Used when entering the main menu after the game has ended.

define config.end_game_transition = None


## A variable to set the transition used when the game starts does not exist.
## Instead, use a with statement after showing the initial scene.


## Window management ###########################################################
##
## This controls when the dialogue window is displayed. If "show", it is always
## displayed. If "hide", it is only displayed when dialogue is present. If
## "auto", the window is hidden before scene statements and shown again once
## dialogue is displayed.
##
## After the game has started, this can be changed with the "window show",
## "window hide", and "window auto" statements.

define config.window = "auto"


## Transitions used to show and hide the dialogue window

define config.window_show_transition = Dissolve(.2)
define config.window_hide_transition = Dissolve(.2)


## Preference defaults #########################################################

## Controls the default text speed. The default, 0, is infinite, while any other
## number is the number of characters per second to type out.

default preferences.text_cps = 40


## The default auto-forward delay. Larger numbers lead to longer waits, with 0
## to 30 being the valid range.

default preferences.afm_time = 15

define config.default_music_volume = 0.4
define config.default_sfx_volume = 0.4


## Save directory ##############################################################
##
## Controls the platform-specific place Ren'Py will place the save files for
## this game. The save files will be placed in:
##
## Windows: %APPDATA\RenPy\<config.save_directory>
##
## Macintosh: $HOME/Library/RenPy/<config.save_directory>
##
## Linux: $HOME/.renpy/<config.save_directory>
##
## This generally should not be changed, and if it is, should always be a
## literal string, not an expression.

define config.save_directory = "LazulightVN-1643777295"


## Icon ########################################################################
##
## The icon displayed on the taskbar or dock.

define config.window_icon = "gui/window_icon.png"


## Build configuration #########################################################
##
## This section controls how Ren'Py turns your project into distribution files.

init python:

    ## The following functions take file patterns. File patterns are case-
    ## insensitive, and matched against the path relative to the base directory,
    ## with and without a leading /. If multiple patterns match, the first is
    ## used.
    ##
    ## In a pattern:
    ##
    ## / is the directory separator.
    ##
    ## * matches all characters, except the directory separator.
    ##
    ## ** matches all characters, including the directory separator.
    ##
    ## For example, "*.txt" matches txt files in the base directory, "game/
    ## **.ogg" matches ogg files in the game directory or any of its
    ## subdirectories, and "**.psd" matches psd files anywhere in the project.

    ## Classify files as None to exclude them from the built distributions.

    build.classify('**~', None)
    build.classify('**.bak', None)
    build.classify('**/.**', None)
    build.classify('**/#**', None)
    build.classify('**/thumbs.db', None)

    ## To archive files, classify them as 'archive'.

    build.classify('game/**.webm', 'archive')
    build.classify('game/**.webp', 'archive')
    build.classify('game/**.png', 'archive')
    build.classify('game/**.mp3', 'archive')
    build.classify('game/**.rpy', 'archive')
    build.classify('game/**.rpyc', 'archive')
    build.classify('game/**.ttf', 'archive')
    build.classify('game/**.otf', 'archive')

    ## Files matching documentation patterns are duplicated in a mac app build,
    ## so they appear in both the app and the zip file.

    build.documentation('*.html')
    build.documentation('*.txt')


## A Google Play license key is required to download expansion files and perform
## in-app purchases. It can be found on the "Services & APIs" page of the Google
## Play developer console.

# define build.google_play_key = "..."


## The username and project name associated with an itch.io project, separated
## by a slash.

# define build.itch_project = "renpytom/test-project"
