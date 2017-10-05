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


from Queue import Empty


class ServiceEvent(object):
    subscription = None

    def __init__(self, device):
        self.device = device

    def get_events(self):
        try:
            event = self.subscription.events.get(timeout=0.1)
            print event
            print event.sid
            print event.seq

        except Empty:
            pass

    def subscribe(self):
        sub_name = self.__class__.__name__
        sub_name = sub_name[0].lower() + sub_name[1:]
        self.subscription = getattr(self.device, sub_name).subscribe()

    def unsubscribe(self):
        self.subscription.unsubscribe()


class AlarmClock(ServiceEvent):
    pass


class MusicServices(ServiceEvent):
    pass


class DeviceProperties(ServiceEvent):
    pass


class SystemProperties(ServiceEvent):
    pass


class ZoneGroupTopology(ServiceEvent):
    pass


class GroupManagement(ServiceEvent):
    pass


class QPlay(ServiceEvent):
    pass


class ContentDirectory(ServiceEvent):
    pass


class MS_ConnectionManager(ServiceEvent):
    pass


class RenderingControl(ServiceEvent):
    pass


class MR_ConnectionManager(ServiceEvent):
    pass


class AVTransport(ServiceEvent):
    pass


class Queue(ServiceEvent):
    pass


class GroupRenderingControl(ServiceEvent):
    pass


class _ServiceHandler(object):
    _registered_devices = {}

    def __iadd__(self, device):
        self._registered_devices[device.uid] = services = (
            AlarmClock(device),
            MusicServices(device),
            DeviceProperties(device),
            SystemProperties(device),
            ZoneGroupTopology(device),
            GroupManagement(device),
            QPlay(device),
            ContentDirectory(device),
            MS_ConnectionManager(device),
            RenderingControl(device),
            MR_ConnectionManager(device),
            AVTransport(device),
            Queue(device),
            GroupRenderingControl(device)
        )
        for service in services:
            service.subscribe()

    def __isub__(self, device):
        services = self._registered_devices.pop(device.uid)
        for service in services:
            service.unsubscribe()


ServiceHandler = _ServiceHandler()

