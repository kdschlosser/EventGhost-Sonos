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
from exception import PlayerNotFound


class _DeviceHandler(object):
    _devices = {}
    _name_cross_reference = {}

    def copy_devices(self):
        return list(device for device in self)

    def __iter__(self):
        results = sorted(
            list(
                (device.player_name, device)
                for device in self._devices.values()
            )
        )

        for _, device in results:
            yield device

    def __iadd__(self, device):
        self.__setitem__(device.player_name, device)

    def __isub__(self, device):
        self.__delitem__(device.player_name)

    def __contains__(self, item):
        if item in self._name_cross_reference:
            return True
        if item in self._devices:
            return True
        return False

    def __getitem__(self, item):

        if item in self._name_cross_reference:
            uids = self._name_cross_reference[item]
            if len(uids) > 1:
                eg.PrintNotice(
                    'Sonos: Multiple devices with the same player name {}. '
                    'Only returning the first found device.'
                    'Please have all devices have a unique name.'
                )
            item = uids[0]

        if item in self._devices:
            return self._devices[item]

        raise PlayerNotFound(item)

    def __setitem__(self, player_name, device):
        self._devices[device.uid] = device

        if player_name not in self._name_cross_reference:
            self._name_cross_reference[player_name] = []

        self._name_cross_reference[player_name] += [device.uid]

    def __delitem__(self, device):
        del self._devices[device.uid]

        self._name_cross_reference[device.player_name].remove(device.uid)
        if not self._name_cross_reference[device.player_name]:
            del self._name_cross_reference[device.player_name]


DeviceHandler = _DeviceHandler()
