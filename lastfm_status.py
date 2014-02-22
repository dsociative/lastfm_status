# -*- coding: utf-8 -*-

import thread
from .api import check_track
import time

from common import gajim
from plugins import GajimPlugin
from plugins.helpers import log_calls


def update_status_thread():
    while 1:
        track = check_track()
        if track:
            for account in gajim.connections.keys():
                gajim.interface.roster.send_status(
                    account, gajim.connections[account].get_status(), track
                )
        time.sleep(30)


class LastFmStatus(GajimPlugin):
    @log_calls('LastFmStatus')
    def init(self):
        self.description = _(
            'Checkout status from lastfm'
        )
        self.config_dialog = None

    @log_calls('LastFmStatusActivate')
    def activate(self):
        thread.start_new_thread(update_status_thread, ())

