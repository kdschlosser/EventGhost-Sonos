# -*- coding: utf-8 -*-
#
# This file is part of EventGhost.
# Copyright © 2005-2016 EventGhost Project <http://www.eventghost.net/>
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
import wx
from device_handler import DeviceHandler
from utils import dialog_line


class Text(eg.TranslatableStrings):
    device_lbl = 'Device:'


class DeviceCtrl(wx.Panel):
    def __init__(self, parent, device):
        wx.Panel.__init__(self, parent)

        self.ctrl = wx.Choice(
            self,
            choices=sorted(
                '{} ({})'.format(dev.player_name, dev.ip_address)
                for dev in DeviceHandler
            )
        )
        self.st = wx.StaticText(self, -1, Text.device_lbl)

        for dev in DeviceHandler:
            if device in (dev.player_name, dev.ip_address, dev.uid):
                self.ctrl.SetStringSelection(dev.player_name)
                break
        else:
            self.ctrl.SetSelection(0)

        sizer = dialog_line(self.st, self.ctrl, proportion=1)
        self.SetSizer(sizer)

    def GetSplit(self):
        return self.ctrl.GetStringSelection()[:-1].split(' (')

    def GetUID(self):
        return DeviceHandler[self.GetSplit()[1]].uid

    def GetIP(self):
        return self.GetSplit()[1]

    def GetPlayerName(self):
        return self.GetSplit()[0]
