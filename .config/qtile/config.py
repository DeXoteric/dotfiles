# Copyright (c) 2010 Aldo Cortesi
# Copyright (c) 2010, 2014 dequis
# Copyright (c) 2012 Randall Ma
# Copyright (c) 2012-2014 Tycho Andersen
# Copyright (c) 2012 Craig Barnes
# Copyright (c) 2013 horsik
# Copyright (c) 2013 Tao Sauvage
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
import os
import subprocess

import colortheme
from libqtile import bar, hook, layout
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from qtile_extras import widget
from qtile_extras.widget.decorations import RectDecoration

mod = "mod4"
terminal = "ghostty"


@hook.subscribe.startup_once
def autostart():
    subprocess.Popen(["/bin/zsh", os.path.expanduser("~/.config/qtile/autostart.sh")])


def increase_volume():
    # Get the current volume
    result = subprocess.run(
        ["pactl", "get-sink-volume", "@DEFAULT_SINK@"], capture_output=True, text=True
    )

    # Extract the volume percentage (assuming left and right channels are the same)
    if result.stdout:
        volume = int(result.stdout.split()[4].strip("%"))
        if volume < 100:
            subprocess.run(["pactl", "set-sink-volume", "@DEFAULT_SINK@", "+5%"])


### Keybindings ###

keys = [
    # Switch between windows
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "Left", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "Right", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "Down", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "Up", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "space", lazy.layout.next(), desc="Move window focus to other window"),
    # Move windows between left/right columns or move up/down in current stack.
    Key(
        [mod, "shift"], "h", lazy.layout.shuffle_left(), desc="Move window to the left"
    ),
    Key(
        [mod, "shift"],
        "l",
        lazy.layout.shuffle_right(),
        desc="Move window to the right",
    ),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),
    Key(
        [mod, "shift"],
        "Left",
        lazy.layout.shuffle_left(),
        desc="Move window to the left",
    ),
    Key(
        [mod, "shift"],
        "Right",
        lazy.layout.shuffle_right(),
        desc="Move window to the right",
    ),
    Key([mod, "shift"], "Down", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "Up", lazy.layout.shuffle_up(), desc="Move window up"),
    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([mod, "control"], "h", lazy.layout.grow_left(), desc="Grow window to the left"),
    Key(
        [mod, "control"], "l", lazy.layout.grow_right(), desc="Grow window to the right"
    ),
    Key([mod, "control"], "j", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),
    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key(
        [mod, "shift"],
        "Return",
        lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack",
    ),
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    # Toggle between different layouts as defined below
    Key([mod], "w", lazy.window.kill(), desc="Kill focused window"),
    Key(
        [mod],
        "f",
        lazy.window.toggle_fullscreen(),
        desc="Toggle fullscreen on the focused window",
    ),
    Key(
        [mod],
        "t",
        lazy.window.toggle_floating(),
        desc="Toggle floating on the focused window",
    ),
    Key([mod, "Shift"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "Shift"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([mod], "d", lazy.spawn("rofi -show drun")),
    Key([mod, "Shift"], "s", lazy.spawn("flameshot gui")),
    # Mute/Unmute
    Key(
        [],
        "XF86AudioMute",
        lazy.spawn("pactl set-sink-mute @DEFAULT_SINK@ toggle"),
    ),
    # Volume Down
    Key(
        [],
        "XF86AudioLowerVolume",
        lazy.spawn("pactl set-sink-volume @DEFAULT_SINK@ -5%"),
    ),
    # Volume Up
    Key([], "XF86AudioRaiseVolume", lazy.function(lambda qtile: increase_volume())),
]

groups = [
    # Screen affinity here is used to make
    # sure the groups startup on the right screens
    Group(name="1", screen_affinity=0),
    Group(name="2", screen_affinity=0),
    Group(name="3", screen_affinity=0),
    Group(name="4", screen_affinity=0),
    Group(name="5", screen_affinity=0),
    Group(name="6", screen_affinity=0),
    Group(name="7", screen_affinity=0),
    Group(name="8", screen_affinity=0),
    Group(name="9", screen_affinity=1),
    Group(name="0", screen_affinity=1),
]


def go_to_group(name: str):
    def _inner(qtile):
        if len(qtile.screens) == 1:
            qtile.groups_map[name].toscreen()
            return

        if name in "12345678":
            qtile.focus_screen(0)
            qtile.groups_map[name].toscreen()
        else:
            qtile.focus_screen(1)
            qtile.groups_map[name].toscreen()

    return _inner


for i in groups:
    keys.append(Key([mod], i.name, lazy.function(go_to_group(i.name))))


def go_to_group_and_move_window(name: str):
    def _inner(qtile):
        if len(qtile.screens) == 1:
            qtile.current_window.togroup(name, switch_group=True)
            return

        if name in "12345678":
            qtile.current_window.togroup(name, switch_group=False)
            qtile.focus_screen(0)
            qtile.groups_map[name].toscreen()
        else:
            qtile.current_window.togroup(name, switch_group=False)
            qtile.focus_screen(1)
            qtile.groups_map[name].toscreen()

    return _inner


for i in groups:
    keys.append(
        Key([mod, "shift"], i.name, lazy.function(go_to_group_and_move_window(i.name)))
    )

colors = colortheme.catppuccin_macchiato

layout_theme = {
    "border_width": 2,
    "margin": 15,
    "border_focus": colors[3],
    "border_normal": colors[2],
}


layouts = [
    layout.MonadTall(**layout_theme),
    layout.Floating(**layout_theme),
]


def create_decoration(color, is_grouped=False):
    return [
        RectDecoration(
            filled=True,
            line_colour=colors[color],
            line_width=2,
            colour=colors[11],
            radius=10,
            group=is_grouped,
        ),
    ]


widget_defaults = dict(
    font="CaskaydiaMono Nerd Font",
    fontsize=16,
    foreground=colors[1],
    padding=20,
    # fmt="<b>{}</b>",
    markup=True,
)
extension_defaults = widget_defaults.copy()


screens = [
    Screen(
        top=bar.Bar(
            [
                widget.Spacer(length=15),
                widget.Spacer(
                    decorations=create_decoration(7, True),
                    length=12,
                ),
                widget.GroupBox(
                    decorations=create_decoration(7, True),
                    active=colors[7],
                    block_highlight_text_color=colors[0],
                    visible_groups=["1", "2", "3", "4", "5", "6", "7", "8"],
                    highlight_method="block",
                    this_screen_border=colors[7],
                    this_current_screen_border=colors[7],
                    padding=3,
                    disable_drag=True,
                    toggle=False,
                ),
                widget.Spacer(
                    decorations=create_decoration(7, True),
                    length=12,
                ),
                widget.Spacer(
                    length=10,
                ),
                widget.Spacer(
                    decorations=create_decoration(8, True),
                    length=12,
                ),
                widget.GroupBox(
                    decorations=create_decoration(8, True),
                    active=colors[8],
                    block_highlight_text_color=colors[0],
                    visible_groups=["9", "0"],
                    highlight_method="block",
                    other_screen_border=colors[8],
                    other_current_screen_border=colors[8],
                    padding=3,
                    disable_drag=True,
                    toggle=False,
                ),
                widget.Spacer(
                    decorations=create_decoration(8, True),
                    length=12,
                ),
                widget.Spacer(
                    lenght="center",
                ),
                widget.Clock(
                    decorations=create_decoration(9),
                    foreground=colors[9],
                    format="  %A, %d %B",
                ),
                widget.Spacer(
                    length=12,
                ),
                widget.Clock(
                    decorations=create_decoration(3),
                    foreground=colors[3],
                    format="  %H:%M",
                ),
                widget.Spacer(
                    lenght="center",
                ),
                widget.PulseVolume(
                    decorations=create_decoration(5),
                    foreground=colors[5],
                    limit_max_volume=True,
                    mute_format="  0%",
                    unmute_format="  {volume}%",
                ),
                widget.Spacer(
                    length=12,
                ),
                widget.CPU(
                    decorations=create_decoration(6),
                    foreground=colors[6],
                    format="  {freq_current}GHz {load_percent}%",
                ),
                widget.Spacer(
                    length=12,
                ),
                widget.Memory(
                    decorations=create_decoration(7),
                    foreground=colors[7],
                    format="  {MemPercent}%",
                ),
                widget.Spacer(
                    length=12,
                ),
                widget.NvidiaSensors(
                    decorations=create_decoration(8),
                    foreground=colors[8],
                    format="  {temp}°C",
                ),
                widget.Spacer(length=15),
            ],
            size=32,
            background="#00000000",
            margin=[5, 0, -5, 0],
        ),
    ),
]

# Drag floating layouts.
mouse = [
    Drag(
        [mod],
        "Button1",
        lazy.window.set_position_floating(),
        start=lazy.window.get_position(),
    ),
    Drag(
        [mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()
    ),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
floats_kept_above = True
cursor_warp = False
floating_layout = layout.Floating(
    **layout_theme,
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
    ],
)
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# When using the Wayland backend, this can be used to configure input devices.
wl_input_rules = None

# xcursor theme (string or None) and size (integer) for Wayland backend
wl_xcursor_theme = None
wl_xcursor_size = 24

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"
