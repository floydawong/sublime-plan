# -*- coding: utf-8 -*-
# -*- author: Floyda -*-

import sublime
import datetime

from .libs import storage


def compare_ternary_array(a, b):
    for x in range(0, 3):
        if a[x] >= b[x]:
            return True
    return False


def compare_ternary_string(a, b):
    return compare_ternary_array(a.split(":"), b.split(":"))


def get_today_day():
    return datetime.datetime.now().strftime("%Y-%m-%d")


def get_time_now():
    return datetime.datetime.now().strftime("%H:%M:%S")


# ----------------------------------------------------------
# message
# ----------------------------------------------------------
messages = []


def add_message(msg):
    messages.append(msg)


def get_message():
    if len(messages) == 0:
        return None
    return messages.pop()


def show_message():
    msg = get_message()
    if msg is None:
        return
    # sublime.DIALOG_YES
    sublime.set_timeout_async(lambda: sublime.ok_cancel_dialog(msg, ok_title="ok"), 10)
    show_message()


# ----------------------------------------------------------
SETTINGS_FILE = "sublime-plan.sublime-settings"
local_setting = storage.StorageSetting("sublime_plan_cache")


def get_task():
    settings = sublime.load_settings(SETTINGS_FILE)
    return settings.get("tasks")


def check_plan():
    tasks = get_task()
    for (name, config) in tasks.items():
        finish_date = local_setting.get(name, "00-00-00")
        if finish_date == get_today_day():
            continue
        overtime = config.get("overtime")
        message = config.get("message")
        if compare_ternary_string(get_time_now(), overtime):
            add_message(message)
            local_setting.set(name, get_today_day())
            local_setting.save()
    show_message()
