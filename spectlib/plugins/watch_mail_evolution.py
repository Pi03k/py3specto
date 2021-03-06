# -*- coding: utf-8 -*-

# Specto , Unobtrusive event notifier
#
#       watch_mail_evolution.py
#
# See the AUTHORS file for copyright ownership information

# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public
# License as published by the Free Software Foundation; either
# version 2 of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public
# License along with this program; if not, write to the
# Free Software Foundation, Inc., 59 Temple Place - Suite 330,
# Boston, MA 02111-1307, USA.

from spectlib.watch import Watch

import dbus

type = "Watch_mail_evolution"
type_desc = _("Evolution")
icon = 'evolution'
category = _("Mail")
dbus_watch = True

class Watch_mail_evolution(Watch):
    """
    Watch class that will check if a new mail is received in evolution.
    """

    def __init__(self, specto, id, values):

        watch_values = []
        self.icon = icon
        self.standard_open_command = 'evolution'
        self.type_desc = type_desc

        #Init the superclass and set some specto values
        Watch.__init__(self, specto, id, values, watch_values)
        
        self.dbus = True
        self.message = ""
        self.extra_info = ""
        # Use the dbus interface we saw in dbus-notify
        self.dbus_interface = "org.gnome.evolution.mail.dbus.Signal"
        self.dbus_path = "/org/gnome/evolution/mail/newmail"
        self.dbus_name = "org.gnome.evolution.mail.dbus.Signal"

        self.signals = {"NewMail": self.new_mail}
        
        
    def new_mail(self, mbox_path, folder_name, some_int=None):
        self.message = "New mail in %s" % folder_name
        self.watch_changed()
    
    def get_balloon_text(self):
        """ create the text for the balloon """
        return _("New message in %s.") % self.message

    def get_gui_info(self):
        return [(_('Name'), self.name),
                (_('Last changed'), self.last_changed)]
