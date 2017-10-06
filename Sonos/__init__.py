# -*- coding: utf-8 -*-
#
# This file is part of EventGhost.
# Copyright Â© 2005-2016 EventGhost Project <http://www.eventghost.org/>
#
# EventGhost is free software: you can redistribute it and/or modify it under
# the terms of the GNU General Public License as published by the Free
# Software Foundation, either version 2 of the License, or (at your option)
# any later version.
#
# EventGhost is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or
# FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for
# more details.
#
# You should have received a copy of the GNU General Public License along
# with EventGhost. If not, see <http://www.gnu.org/licenses/>.

import eg


eg.RegisterPlugin(
    name=u'Sonos Media Player',
    author=u'K',
    version=u'0.1a',
    description=(
        '<h1>Interface for the Sonos Media Player<br><br></h1>'
        '<h2>Features</h2>'
        '<ul>'
        '   <li>Play</li>'
        '   <li>Pause</li>'
        '   <li>Stop</li>'
        '   <li>Next track</li>'
        '   <li>Previous track</li>'
        '   <li>'
        '       Get current transport information'
        '       (if speaker is playing, paused, stopped)'
        '   </li>'
        '   <li>Get information about the currently playing track'
        '       <ul>'
        '           <li>Track title</li>'
        '           <li>Artist</li>'
        '           <li>Album</li>'
        '           <li>Album Art (if available)</li>'
        '           <li>Track length</li>'
        '           <li>'
        '               Duration played '
        '               (for example, 30 seconds into a 3 minute song)'
        '           </li>'
        '           <li>'
        '               Playlist position '
        '               (for example, item 5 in the playlist)'
        '           </li>'
        '           <li>Track URI</li>'
        '       </ul>'
        '   </li>'
        '   <li>Mute (or unmute) the speaker</li>'
        '   <li>Get or set the speaker\'s volume</li>'
        '   <li>Get or set the speaker\'s bass EQ</li>'
        '   <li>Get or set the speaker\'s treble EQ</li>'
        '   <li>Toggle the speaker\'s loudness compensation</li>'
        '   <li>Toggle the speaker\'s night mode</li>'
        '   <li>Toggle the speaker\'s dialog mode</li>'
        '   <li>Turn on (or off) the white status light on the unit</li>'
        '   <li>'
        '       Switch the speaker\'s source to line-in or TV input '
        '       (if the Zone Player supports it)'
        '   </li>'
        '   <li>Get the speaker’s information'
        '       <ul>'
        '           <li>Zone Name</li>'
        '           <li>Zone Icon</li>'
        '           <li>'
        '               UID '
        '               (usually something like RINCON_XXXXXXXXXXXXXXXXX)'
        '           </li>'
        '           <li>Serial Number</li>'
        '           <li>Software version</li>'
        '           <li>Hardware version</li>'
        '           <li>MAC Address</li>'
        '       </ul>'
        '   </li>'
        '   <li>Set the speaker\'s Zone Name</li>'
        '   <li>Find all the Sonos speakers in a network.</li>'
        '   <li>Put all Sonos speakers in a network into “party mode”.</li>'
        '   <li>“Unjoin” speakers from a group.</li>'
        '   <li>'
        '       Manage the Sonos queue (get the items in it, '
        '       add to it, clear it, play a specific song from it)'
        '   </li>'
        '   <li>'
        '       Get the saved favorite radio stations and shows '
        '       (title and stream URI)'
        '   </li>'
        '   <li>Search for and play item from your music library</li>'
        '   <li>'
        '       Start a music library update and '
        '       determine if one is in progress'
        '   </li>'
        '</ul>'
        '<p>'
        '   supports lower level access from Python to all Sonos services '
        '   (eg Alarms)'
        '</p>'
    ),
    kind=u'external',
    canMultiLoad=True,
    createMacrosOnAdd=True,
    guid=u'{588DAF91-20F8-470E-A58D-65077165AAFB}',
    icon=(
        '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'
        'PvumRSP4LCjP6nuS/jz0AAAAASUVORK5CYII='
    )
)


import wx  # NOQA
import wx_controls # NOQA
from . import soco # NOQA
from device_handler import DeviceHandler # NOQA
from event_handler import EventHandler # NOQA
from .soco.events import event_listener # NOQA
from exception import PlayerNotFound # NOQA
from utils import dialog_line as _dialog_line # NOQA


class Text(eg.TranslatableStrings):
    class SetPlayerName:
        name = 'Set Players Name'
        description = 'Sets the user friendly name of the player.'
        player_lbl = 'New Player Name:'

    class SetSleepTimer:
        name = 'Set Sleep Timer'
        description = 'Sets the sleep timer for a player.'
        hours_lbl = 'Hours:'
        minutes_lbl = 'Minutes:'
        seconds_lbl = 'Seconds:'

    class GetSleepTimer:
        name = 'Get Sleep Timer'
        description = 'Returns the remaining sleep timer time on a player.'


class SonosMedia(eg.PluginBase):
    PlayerNotFound = PlayerNotFound
    text = Text

    def __init__(self):
        self._event_thread = None
        eg.PluginBase.__init__(self)
        self.AddAction(SetPlayerName)
        self.AddAction(SetSleepTimer)
        self.AddAction(GetSleepTimer)

    def __start__(self):
        self._event_thread = EventHandler(self)

    def __close__(self):
        pass

    def __stop__(self):
        self._event_thread.stop()

    def Configure(self, *args):
        eg.PluginBase.Configure(self, *args)


class GetSleepTimer(eg.ActionBase):

    def __call__(self, device):
        time_remaining = DeviceHandler[device].get_sleep_timer()
        return 0 if time_remaining is None else time_remaining

    def Configure(self, device=None):
        panel = eg.ConfigPanel()
        device_ctrl = wx_controls.DeviceCtrl(panel, device)

        panel.sizer.Add(device_ctrl, 0, wx.EXPAND)

        while panel.Affirmed():
            panel.SetResult(device_ctrl.GetUID())


class SetSleepTimer(eg.ActionBase):

    def __call__(self, device, hours=0, minutes=0, seconds=0):
        seconds += ((hours * 60) + minutes) * 60
        DeviceHandler[device].set_sleep_timer(min([86399, seconds]))
        return DeviceHandler[device].get_sleep_timer()

    def Configure(self, device=None, hours=2, minutes=0, seconds=0):
        text = self.text
        panel = eg.ConfigPanel()

        def create_controls(label, value):
            st = wx.StaticText(label)
            ctrl = panel.SpinIntCtrl(value=value, min=0, max=60)
            panel.sizer.Add(_dialog_line(st, ctrl), 0, wx.EXPAND)
            return st, ctrl

        device_ctrl = wx_controls.DeviceCtrl(panel, device)
        panel.sizer.Add(device_ctrl, 0, wx.EXPAND)

        hours_st, hours_ctrl = create_controls(text.hours_lbl, hours)
        minutes_st, minutes_ctrl = create_controls(text.minutes_lbl, minutes)
        seconds_st, seconds_ctrl = create_controls(text.seconds_lbl, seconds)

        hours_ctrl.numCtrl.SetMax(24)
        eg.EqualizeWidths((device_ctrl.st, hours_st, minutes_st, seconds_st))

        while panel.Affirmed():
            panel.SetResult(
                device_ctrl.GetUID(),
                hours_ctrl.GetValue(),
                minutes_ctrl.GetValue(),
                seconds_ctrl.GetValue()
            )


class SetPlayerName(eg.ActionBase):

    def __call__(self, device, player_name):
        DeviceHandler[device].player_name = player_name

    def Configure(self, device=None, player_name=''):
        text = self.text
        panel = eg.ConfigPanel()

        name_st = panel.StaticText(text.player_lbl)
        device_ctrl = wx_controls.DeviceCtrl(panel, device)
        name_ctrl = panel.TextCtrl(player_name)

        eg.EqualizeWidths((device_ctrl.st, name_st))
        eg.EqualizeWidths((device_ctrl.ctrl, name_ctrl))

        name_sizer = _dialog_line(name_st, name_ctrl, proportion=1)

        panel.sizer.Add(device_ctrl, 0, wx.EXPAND)
        panel.sizer.Add(name_sizer, 0, wx.EXPAND)

        while panel.Affirmed():
            panel.SetResult(
                device_ctrl.GetUID(),
                name_ctrl.GetValue()
            )


class ZoneGroup(eg.ActionBase):

    def __call__(self, group_label, action):
        pass

    def Configure(self, group_label=None, actions=()):
        text = self.text
        panel = eg.ConfigPanel()

        groups = {}

        for dev in DeviceHandler:
            if dev.is_coordinator:
                groups[dev.group.label] = dev.group


# class NowPlaying(eg.ActionBase):
#     get_current_track_info
#
# class Play(eg.ActionBase):
#
# class PlayURI(eg.ActionBase):
#
# class Queue(eg.ActionBase):
#     get_queue
#     create_sonos_playlist_from_queue
#     get_item_album_art_uri
#     PlayFromQueue
#
#
#
# class Pause(eg.ActionBase):
# class Stop(eg.ActionBase):
# class Seek(eg.ActionBase):
# class Next(eg.ActionBase):
# class Previous(eg.ActionBase):
# class Input(eg.ActionBase):
#     # switch_to_line_in
#     # switch_to_tv
#
#
# class Audio(eg.ActionBase):
#     get_speaker_info
#
# class PartyMode(eg.ActionBase):
# class join(eg.ActionBase):
# class unjoin(eg.ActionBase):
#
# class get_current_transport_info(eg.ActionBase):
#
# class Queue(eg.ActionBase):
#     play_from_queue
#     add_uri_to_queue
#     remove_from_queue
#     clear_queue
#     add_to_queue
#
# class Favorites(eg.ActionBase):
#     get_favorite_radio_shows
#     get_favorite_radio_stations
#     get_sonos_favorites
#
# class Playlist(eg.ActionBase):
#     create_sonos_playlist
#     create_sonos_playlist_from_queue
#     remove_sonos_playlist
#     add_item_to_sonos_playlist
#
#     get_item_album_art_uri
