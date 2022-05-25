
# Definitions file to facilitate easier renpy scripting usage
# Here various things that will be commonly done in the renpy programming will be done

# One example is resizing and defining backgrounds/CGs for scene use. The following is
# required before you can use one:

# image bg abandonedpark day = Image("bg_abandonedpark_day.webp", xanchor=.5, yanchor=.5, xsize=1920, ysize=1080)
# ... later
# scene bg abandonedpark day

# Instead of doing it in the scripts, we do all of them here.

########################################################################################

######
# Backgrounds
######

# note that these are all currenty in the Backgrounds folder so Backgrounds/<foo>

# BGs with proper aspect ratio (mostly 2560x1440)

# abandoned park
image bg abandonedpark day = "Backgrounds/bg_abandonedpark_day.webp"
image bg abandonedpark night = "Backgrounds/bg_abandonedpark_night.webp"
image bg abandonedpark sunset = "Backgrounds/bg_abandonedpark_sunset.webp"

# river
image bg river day = "Backgrounds/bg_river_day.webp"
image bg river sunset = "Backgrounds/bg_river_sunset.webp"

# mc room
image bg mc room day = "Backgrounds/bg_mc_room_day.webp"
image bg mc room sunset = "Backgrounds/bg_mc_room_sunset.webp"
image bg mc room night = "Backgrounds/bg_mc_room_night.webp"

# school rooftop
image bg school rooftop day = "Backgrounds/bg_school_rooftop_day.webp"
image bg school rooftop night = "Backgrounds/bg_school_rooftop_night.webp"

# streets
image bg streets day = "Backgrounds/bg_streets_day.webp"
image bg streets sunset = "Backgrounds/bg_streets_sunset.webp"

# one offs
image bg karaoke = "Backgrounds/bg_karaoke.webp"
image bg keyboardstore = "Backgrounds/bg_keyboardstore.webp"
image bg lazulightstage = "Backgrounds/bg_lazulightstage.webp"
image bg festival = "Backgrounds/bg_festival.webp"
image bg fortunetellerbooth night = "Backgrounds/bg_fortunetellerbooth_night.webp"
image bg maid cafe = "Backgrounds/bg_maid_cafe.webp"
image bg mall = "Backgrounds/bg_mall.webp"
image bg park = "Backgrounds/bg_park.webp"
image bg classroom back view = "Backgrounds/bg_classroom_back_view.webp"
image bg camping spot by river day = "Backgrounds/bg_camping_spot_by_river_day.webp"
image bg school courtyard = "Backgrounds/bg_school_courtyard_day.webp"
image bg sunny sky = "Backgrounds/bg_sunny_sky.webp"
image bg sunny sky2 = "Backgrounds/bg_sunny_skyupward.webp"


# Improper aspect ratios (first batch is 4093x2894)
# For this batch, images are slightly too tall so tops and bottoms will be clipped
# Currently the image is centered, but you can create a new transform with yoffset to
# adjust individual images if required.

image bg kitchen = "Backgrounds/bg_kitchen.webp"
image bg vendingmachine = "Backgrounds/bg_vendingmachine.webp"
image bg clubroom day = "Backgrounds/bg_clubroom_day.webp"
image bg clubroom night = "Backgrounds/bg_clubroom_night.webp"
image bg clubroom plush = "Backgrounds/bg_clubroom_plush.webp"
image bg hallway day = "Backgrounds/bg_hallway_day.webp"
image bg hallway sunset = "Backgrounds/bg_hallway_sunset.webp"
image bg track and field day = "Backgrounds/bg_track_and_field_day.webp"


# Exactly 1920x1080, no transform needed (mostly placeholders)

image bg none = Solid("#000")
image bg haunted house = "Backgrounds/bg_hauntedhouse.webp"
image bg library = "Backgrounds/bg_library.webp"

######
# CGs
######

# Most CGs have correct aspect ratio

# Elira

image cg elira classroom hair tuck = "CG/Elira/cg_elira_classroom_hair_tuck.webp"
image cg elira paper slip white = "CG/Elira/cg_elira_paper_slip_white.webp"
image cg elira paper slip yellow = "CG/Elira/cg_elira_paper_slip_yellow.webp"
image cg elira pettingpikl = "CG/Elira/cg_elira_pettingpikl.webp"
image cg elira river = "CG/Elira/cg_elira_river.webp"
image cg elira tanabata = "CG/Elira/cg_elira_tanabata.webp"
image cg elira violin = "CG/Elira/cg_elira_violin.webp"
image cg elira glasses 1 = "CG/Elira/cg_elira_glasses/cg_elira_glasses_1.webp"
image cg elira glasses 2 = "CG/Elira/cg_elira_glasses/cg_elira_glasses_2.webp"
image cg elira glasses 3 = "CG/Elira/cg_elira_glasses/cg_elira_glasses_3.webp"

# Finana

image cg finana studying cookies = "CG/Finana/cg_finana_studying_cookies.webp"
image cg finana studying finatos = "CG/Finana/cg_finana_studying_finatos.webp"
image cg finana studying granolabar = "CG/Finana/cg_finana_studying_granolabar.webp"
image cg finana gaming casual = "CG/Finana/cg_finana_gaming_casual.webp"
image cg finana rooftop = "CG/Finana/cg_finana_rooftop.webp"
image cg finana rooftop lunch = "CG/Finana/cg_finana_rooftop_lunch.webp"
image cg finana keyboard = "CG/Finana/cg_finana_keyboard.webp"

# Pomu

image cg pomu polevault = "CG/Pomu/cg_pomu_polevault.webp"
image cg pomu broken platform = "CG/Pomu/cg_pomu_broken_platform.webp"
# these were on treetop but 'on' is a keyword in renpy script
image cg pomu close up treetop 1 = "CG/Pomu/cg_pomu_close_up_on_treetop_1.webp"
image cg pomu close up treetop 2 = "CG/Pomu/cg_pomu_close_up_on_treetop_2.webp"
image cg pomu tree platform daytime = "CG/Pomu/cg_pomu_tree_platform_daytime.webp"
image cg pomu haunted house = "CG/Pomu/cg_pomu_haunted_house.webp"
image cg pomu maidcafe1 = "CG/Pomu/cg_pomu_maidcafe1.webp"
image cg pomu maidcafe2 = "CG/Pomu/cg_pomu_maidcafe2.webp"
image cg pomu maidcafe3 = "CG/Pomu/cg_pomu_maidcafe3.webp"
image cg pomu pomusuke ver1 = "CG/Pomu/cg_pomu_pomusuke_ver1.webp"
image cg pomu pomusuke ver2 = "CG/Pomu/cg_pomu_pomusuke_ver2.webp"

# general - no girls or multiple

# these were at night but 'at' is a keyword in renpy script
image cg lazulight camping night = "CG/General/cg_lazulight_camping_at_night.webp"
image cg lazulight camping night ver2 = "CG/General/cg_lazulight_camping_at_night_ver2.webp"
image cg lazulight camping night ver3 = "CG/General/cg_lazulight_camping_at_night_ver3.webp"
image cg lazulight idol = "CG/General/cg_lazulight_idol.webp"
image cg magic rock = "CG/General/cg_magic_rock.webp"
image cg lazulight by the river = "CG/General/cg_lazulight_by_the_river.webp"

######
# Sprites
######

# There are the sprite height and width

# define SPRITE_HEIGHT = 4000
# define SPRITE_WIDTH = 3600

# There are the maximum height and width possible

# define MAX_HEIGHT = 2100
# define MAX_WIDTH = MAX_HEIGHT * 0.9

# This is the height required to achieve the biggest size

# define TOTAL_HEIGHT = 180.0

# First we need to define the height ratio of each character

# define POMU_RATIO = 156.0 / TOTAL_HEIGHT
# define ELIRA_RATIO = 160.0 / TOTAL_HEIGHT
# define FINANA_RATIO = 140.0 / TOTAL_HEIGHT
# define OLIVER_RATIO = 180.0 / TOTAL_HEIGHT # Reduced by 10 cm so he isn't a giant

# Pomu

image pomu school neutral = "Sprites/Pomu/school/pomu school neutral.webp"
image pomu school concerned = "Sprites/Pomu/school/pomu school concerned.webp"
image pomu school excited = "Sprites/Pomu/school/pomu school excited.webp"
image pomu school flustered = "Sprites/Pomu/school/pomu school flustered.webp"
image pomu school happy = "Sprites/Pomu/school/pomu school happy.webp"
image pomu school overjoyed = "Sprites/Pomu/school/pomu school overjoyed.webp"
image pomu school pout = "Sprites/Pomu/school/pomu school pout.webp"
image pomu school sad = "Sprites/Pomu/school/pomu school sad.webp"
image pomu school serious = "Sprites/Pomu/school/pomu school serious.webp"
image pomu school surprised = "Sprites/Pomu/school/pomu school surprised.webp"

image pomu casual neutral = "Sprites/Pomu/casual/pomu casual neutral.webp"
image pomu casual concerned = "Sprites/Pomu/casual/pomu casual concerned.webp"
image pomu casual excited = "Sprites/Pomu/casual/pomu casual excited.webp"
image pomu casual flustered = "Sprites/Pomu/casual/pomu casual flustered.webp"
image pomu casual happy = "Sprites/Pomu/casual/pomu casual happy.webp"
image pomu casual overjoyed = "Sprites/Pomu/casual/pomu casual overjoyed.webp"
image pomu casual pout = "Sprites/Pomu/casual/pomu casual pout.webp"
image pomu casual sad = "Sprites/Pomu/casual/pomu casual sad.webp"
image pomu casual serious = "Sprites/Pomu/casual/pomu casual serious.webp"
image pomu casual surprised = "Sprites/Pomu/casual/pomu casual surprised.webp"

image pomu track neutral = "Sprites/Pomu/track/pomu track neutral.webp"
image pomu track concerned = "Sprites/Pomu/track/pomu track concerned.webp"
image pomu track excited = "Sprites/Pomu/track/pomu track excited.webp"
image pomu track flustered = "Sprites/Pomu/track/pomu track flustered.webp"
image pomu track happy = "Sprites/Pomu/track/pomu track happy.webp"
image pomu track overjoyed = "Sprites/Pomu/track/pomu track overjoyed.webp"
image pomu track pout = "Sprites/Pomu/track/pomu track pout.webp"
image pomu track sad = "Sprites/Pomu/track/pomu track sad.webp"
image pomu track serious = "Sprites/Pomu/track/pomu track serious.webp"
image pomu track surprised = "Sprites/Pomu/track/pomu track surprised.webp"

# Elira

image elira school neutral = "Sprites/Elira/school/elira school neutral.webp"
image elira school angry = "Sprites/Elira/school/elira school angry.webp"
image elira school blushing = "Sprites/Elira/school/elira school blushing.webp"
image elira school giggle = "Sprites/Elira/school/elira school giggle.webp"
image elira school loudlaugh = "Sprites/Elira/school/elira school loudlaugh.webp"
image elira school murderous = "Sprites/Elira/school/elira school murderous.webp"
image elira school sad = "Sprites/Elira/school/elira school sad.webp"
image elira school serious = "Sprites/Elira/school/elira school serious.webp"
image elira school sigh = "Sprites/Elira/school/elira school sigh.webp"
image elira school smile = "Sprites/Elira/school/elira school smile.webp"
image elira school straightface = "Sprites/Elira/school/elira school straightface.webp"
image elira school worried = "Sprites/Elira/school/elira school worried.webp"
image elira school shocked = "Sprites/Elira/school/elira school shocked.webp"

image elira casual neutral = "Sprites/Elira/casual/elira casual neutral.webp"
image elira casual annoyed = "Sprites/Elira/casual/elira casual annoyed.webp"
image elira casual blushing = "Sprites/Elira/casual/elira casual blushing.webp"
image elira casual giggle = "Sprites/Elira/casual/elira casual giggle.webp"
image elira casual loudlaugh = "Sprites/Elira/casual/elira casual loudlaugh.webp"
image elira casual murderous = "Sprites/Elira/casual/elira casual murderous.webp"
image elira casual sad = "Sprites/Elira/casual/elira casual sad.webp"
image elira casual serious = "Sprites/Elira/casual/elira casual serious.webp"
image elira casual sigh = "Sprites/Elira/casual/elira casual sigh.webp"
image elira casual smile = "Sprites/Elira/casual/elira casual smile.webp"
image elira casual straightface = "Sprites/Elira/casual/elira casual straightface.webp"
image elira casual worried = "Sprites/Elira/casual/elira casual worried.webp"
image elira casual shocked = "Sprites/Elira/casual/elira casual shocked.webp"

# Finana

image finana school neutral = "Sprites/Finana/school/finana school neutral.webp"
image finana school confused = "Sprites/Finana/school/finana school confused.webp"
image finana school curious = "Sprites/Finana/school/finana school curious.webp"
image finana school embarrassed = "Sprites/Finana/school/finana school embarrassed.webp"
image finana school excited = "Sprites/Finana/school/finana school excited.webp"
image finana school happy = "Sprites/Finana/school/finana school happy.webp"
image finana school nervous = "Sprites/Finana/school/finana school nervous.webp"
image finana school shocked = "Sprites/Finana/school/finana school shocked.webp"
image finana school worried = "Sprites/Finana/school/finana school worried.webp"
image finana school angry = "Sprites/Finana/school/finana school angry.webp"

image finana casual neutral = "Sprites/Finana/casual/finana casual neutral.webp"
image finana casual confused = "Sprites/Finana/casual/finana casual confused.webp"
image finana casual angry = "Sprites/Finana/casual/finana casual angry.webp"
image finana casual embarrassed = "Sprites/Finana/casual/finana casual embarrassed.webp"
image finana casual happy = "Sprites/Finana/casual/finana casual happy.webp"
image finana casual nervous = "Sprites/Finana/casual/finana casual nervous.webp"
image finana casual shocked = "Sprites/Finana/casual/finana casual shocked.webp"
image finana casual sleepy = "Sprites/Finana/casual/finana casual sleepy.webp"

# Oliver

image oliver neutral = "Sprites/Oliver-sensei/oliver sensei neutral.webp"
image oliver happy = "Sprites/Oliver-sensei/oliver sensei happy.webp"
image oliver nervous = "Sprites/Oliver-sensei/oliver sensei nervous.webp"
image oliver shy = "Sprites/Oliver-sensei/oliver sensei shy.webp"

#Pomusuke

image pomusuke = "Sprites/Misc/pomusuke.webp"
transform pomusuke_caught:
    xalign 0.5
    yalign 1.0
    yoffset 150

#EliraFish

image elirafish = "Sprites/Misc/elirafish.webp"
transform fish_slight_right:
    xalign 0.5
    xoffset 220
    yalign 0.5
transform fish_center:
    xalign 0.5
    xoffset -50
    yalign 0.5


##############
# Transitions
##############
define sweepright = MultipleTransition([
    False, ImageDissolve("gui/transitions/sweep.png", 0.5, ramplen=64),
    Solid("#000"), Pause(0.25),
    Solid("#000"), ImageDissolve("gui/transitions/sweep.png", 0.5, ramplen=64),
    True])

define sweepleft = MultipleTransition([
    False, ImageDissolve("gui/transitions/sweep.png", 0.5, ramplen=64,reverse=True),
    Solid("#000"), Pause(0.25),
    Solid("#000"), ImageDissolve("gui/transitions/sweep.png", 0.5, ramplen=64,reverse=True),
    True])

define sweepclock = MultipleTransition([
    False, ImageDissolve("gui/transitions/clock.png", 1.0, ramplen=64),
    Solid("#000"), Pause(0.25),
    Solid("#000"), ImageDissolve("gui/transitions/clock.png", 1.0, ramplen=64),
    True])

define slidingblind = ImageDissolve("gui/transitions/slidingblinds.png", 1.0, ramplen=64)

define slidingblinds = MultipleTransition([
    False, ImageDissolve("gui/transitions/slidingblinds.png", 1.0, ramplen=64),
    Solid("#000"), Pause(0.25),
    Solid("#000"), ImageDissolve("gui/transitions/slidingblinds.png", 1.0, ramplen=64),
    True])


define slowdissolve = Dissolve(1.0)

########################################################################################

######
# Auido
######

# BGM

define audio.bgm_clubtime01 = "audio/bgm/bgm_clubtime01.opus"
define audio.bgm_flashback01 = "audio/bgm/bgm_flashback01.opus"
define audio.bgm_goinghome01 = "audio/bgm/bgm_goinghome01L.opus"
define audio.bgm_hangout01 = "audio/bgm/bgm_hangout01.opus"
define audio.bgm_hectic01 = "audio/bgm/bgm_hectic01L.opus"

define audio.bgm_karaokea = "audio/bgm/bgm_karaokea.opus"
define audio.bgm_karaokeb = "audio/bgm/bgm_karaokebL.opus"
define audio.bgm_karaokec = "audio/bgm/bgm_karaokec.opus"

define audio.bgm_lazulight01 = "audio/bgm/bgm_lazulight01.opus"
define audio.bgm_morning01 = "audio/bgm/bgm_morning01.opus"
define audio.bgm_schooltime01 = "audio/bgm/bgm_schooltime01.opus"

define audio.bgm_shopping01 = "audio/bgm/bgm_shopping01.opus"
define audio.bgm_soft01 = "audio/bgm/bgm_soft01L.opus"
define audio.bgm_trouble01 = "audio/bgm/bgm_trouble01.opus"

define audio.bgm_pomu01 = "audio/bgm/bgm_pomu01.opus"

define audio.bgm_elira01 = "audio/bgm/bgm_elira01.opus"

define audio.bgm_finana01 = "audio/bgm/bgm_finana01.opus"

define audio.bgm_main_menu = "audio/bgm/bgm_main_menu.opus"

# SFX

define audio.sfx_buttonui01 = "audio/sfx/sfx_buttonui01.opus"
define audio.sfx_buttonui02 = "audio/sfx/sfx_buttonui02.opus"
define audio.sfx_windowcloseui = "audio/sfx/sfx_windowcloseui.opus"

define audio.sfx_ambulance = "audio/sfx/sfx_ambulance.opus"
define audio.sfx_birds = "audio/sfx/sfx_birds.opus"
define audio.sfx_campfire = "audio/sfx/sfx_campfire.opus"
define audio.sfx_crowdnoise = "audio/sfx/sfx_crowdnoise.opus"
define audio.sfx_dooropen01 = "audio/sfx/sfx_dooropen01.opus"
define audio.sfx_dooropen02 = "audio/sfx/sfx_dooropen02.opus"
define audio.sfx_heartbeat60 = "audio/sfx/sfx_heartbeat60.opus"
define audio.sfx_knifeslash = "audio/sfx/sfx_knifeslash.opus"
define audio.sfx_river = "audio/sfx/sfx_river.opus"
define audio.sfx_schoolbell = "audio/sfx/sfx_schoolbell.opus"
define audio.sfx_splash = "audio/sfx/sfx_splash.opus"
define audio.sfx_thud01 = "audio/sfx/sfx_thud01.opus"
define audio.sfx_train = "audio/sfx/sfx_train.opus"
define audio.sfx_whistle = "audio/sfx/sfx_whistle.opus"
define audio.sfx_whoosh = "audio/sfx/sfx_whoosh.opus"
define audio.sfx_windsoft = "audio/sfx/sfx_windsoft.opus"
define audio.sfx_windstrong = "audio/sfx/sfx_windstrong.opus"

define audio.choose = "audio/ui/ui_button_choose.opus"
define audio.confirm = "audio/ui/ui_button_confirm.opus"
define audio.close = "audio/ui/ui_window_close.opus"
