#! /usr/bin/python3
# -*- coding: utf-8 -*-

from gi.repository import GObject
from gi.repository import Gio, Gtk

class App(object):
    BASE_KEY = "apps.specto"
    newWorldOrderKey = "newworldorder"
    def __init__(self):
        path = './'
        schemaSource = Gio.Settings.SchemaSource.new_from_directory(path, null, false, null);
        settingsSchema = schemaSource.lookup(self.BASE_KEY, false);

        settings = Gio.Settings.new(self.BASE_KEY)

        checkButton = Gtk.CheckButton("My boolean setting")
        checkButton.set_active(settings.get_boolean(self.newWorldOrderKey))
        settings.connect('changed::' + self.newWorldOrderKey, self.settingsChanged, checkButton)
        checkButton.connect('toggled', self.buttonToggled, settings)

        window = Gtk.Window(type=Gtk.WindowType.TOPLEVEL)
        window.set_title('GSettings Example')
        window.set_border_width(24)
        window.connect('delete-event', self.windowDestroy)
        window.add(checkButton)
        window.show_all()
        Gtk.main()
    def settingsChanged(self, settings, key, button):
        print("settingsChanged")
        button.set_active(settings.get_boolean(self.newWorldOrderKey))
    def buttonToggled(self, button, settings):
        print("A")
        settings.set_boolean(self.newWorldOrderKey, button.get_active())
    def windowDestroy(self, widget, data=None):
        Gtk.main_quit()

if __name__ == "__main__":
    app = App()
