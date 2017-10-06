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

import soco
import threading

from device_handler import DeviceHandler as _DeviceHandler
from service_handler import ServiceHandler as _ServiceHandler

DeviceHandler = _DeviceHandler
ServiceHandler = _ServiceHandler


class EventHandler(object):
    def __init__(self, plugin):
        self._event = threading.Event()
        self.plugin = plugin
        self.TriggerEvent = plugin.TriggerEvent
        self.thread = threading.Thread(name=__name__, target=self.run)
        self.thread.start()

    def run(self):
        global DeviceHandler
        global ServiceHandler

        self._event.clear()
        for device in soco.discover():
            DeviceHandler += device
            ServiceHandler += device

        while not self._event.isSet():
            old_devices = DeviceHandler.copy_devices()
            new_devices = soco.discover()
            for new_device in new_devices[:]:
                for old_device in old_devices:
                    if old_device.uid == new_device.uid:
                        old_devices.remove(old_device)
                        new_devices.remove(new_device)
                        break

            for old_device in old_devices:
                self.TriggerEvent(
                    'Player.Removed',
                    payload=old_device.player_name
                )

                DeviceHandler -= old_device
                ServiceHandler -= old_device

            for new_device in new_devices:
                self.TriggerEvent(
                    'Player.Added',
                    payload=new_device.player_name
                )

                DeviceHandler += new_device
                ServiceHandler += new_device

            self._event.wait(0.2)

    def stop(self):
        self._event.set()
        self.thread.join(3)
