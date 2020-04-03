# -*- coding: utf-8 -*-
# -*- author: Floyda -*-

import sys
import os
from imp import reload

from .libs import log
from .libs import timer

from .sublime_plan import check_plan

dirname = os.path.split(os.path.dirname(__file__))[1]
timer_handler = None

all_modules = ["sublime_plan"]


def reload_module():
    for module in all_modules:
        name = "%s.%s" % (dirname, module)
        if name in sys.modules:
            reload(sys.modules[name])


def plugin_loaded():
    log.init(True)
    log.debug("---------- plugin_loaded ----------")
    global timer_handler
    timer_handler = timer.MiniTimer(5.0, check_plan)
    reload_module()


def plugin_unloaded():
    log.debug("---------- plugin_unloaded ----------")
    log.clear()
    global timer_handler
    timer_handler.stop()
