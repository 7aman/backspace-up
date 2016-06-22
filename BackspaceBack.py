#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# by Ricardo Lenz, 2016-jun
# riclc@hotmail.com
#

import os, gi
gi.require_version('Nautilus', '3.0')
from gi.repository import GObject, Nautilus, Gtk, Gio, GLib

def ok():
    app = Gtk.Application.get_default()
    print app.set_accels_for_action( "win.up", ["BackSpace"] )
    #print app.get_actions_for_accel("BackSpace")
    #print app.get_actions_for_accel("<alt>Up")
   
class BackspaceBack(GObject.GObject, Nautilus.MenuProvider):
    def __init__(self):
        print "--- Plugin BackspaceBack ---"
        GLib.timeout_add( 3000, ok )

