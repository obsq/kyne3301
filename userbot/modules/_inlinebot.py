from math import ceil
import asyncio
import json
import random
import re
from telethon import events, errors, custom
from userbot import CMD_HELP
import io
from userbot import bot as kyne
import os
from config2 import Var as Config
Var = Config

from userbot import CMD_HELP, ALIVE_NAME, PM_MESSAGE, KYNE_NAME, KYNE_MSG, ORI_MSG
KYNE_NNAME = str(KYNE_NAME) if KYNE_NAME else str(KYNE_MSG)


if Var.TG_BOT_USER_NAME_BF_HER is not None and kyneee is not None:
    @kyneee.on(events.InlineQuery)  # pylint:disable=E0602
    async def inline_handler(event):
        builder = event.builder
        result = None
        query = event.text
        if event.query.user_id == kyne.uid and query.startswith("Userbot"):
            rev_text = query[::-1]
            buttons = paginate_help(0, CMD_HELP, "helpme")
            result = builder.article(
                "`{KYNE_NNAME} :` --HELP MODULE--",
                text="{}\nCurrently Loaded modules: {}".format(
                    query, len(CMD_HELP)),
                buttons=buttons,
                link_preview=False
            )
        await event.answer([result] if result else None)
    @kyneee.on(events.callbackquery.CallbackQuery(  # pylint:disable=E0602
        data=re.compile(b"helpme_next\((.+?)\)")
    ))
    async def on_plug_in_callback_query_handler(event):
        if event.query.user_id == kyne.uid:  # pylint:disable=E0602
            current_page_number = int(
                event.data_match.group(1).decode("UTF-8"))
            buttons = paginate_help(
                current_page_number + 1, CMD_HELP, "helpme")
            # https://t.me/TelethonChat/115200
            await event.edit(buttons=buttons)
        else:
            reply_pop_up_alert = "kyne : Try deploying your own kyne"
            await event.answer(reply_pop_up_alert, cache_time=0, alert=True)


    @kyneee.on(events.callbackquery.CallbackQuery(  # pylint:disable=E0602
        data=re.compile(b"helpme_prev\((.+?)\)")
    ))
    async def on_plug_in_callback_query_handler(event):
        if event.query.user_id == kyne.uid:  # pylint:disable=E0602
            current_page_number = int(
                event.data_match.group(1).decode("UTF-8"))
            buttons = paginate_help(
                current_page_number - 1,
                CMD_HELP,  # pylint:disable=E0602
                "helpme"
            )
            # https://t.me/TelethonChat/115200
            await event.edit(buttons=buttons)
        else:
            reply_pop_up_alert = "kyne : Try deploying your own kyne"
            await event.answer(reply_pop_up_alert, cache_time=0, alert=True)
    @kyneee.on(events.callbackquery.CallbackQuery(  # pylint:disable=E0602
        data=re.compile(b"us_module_(.*)")
    ))
    async def on_plug_in_callback_query_handler(event):
        module_name = event.data_match.group(1).decode("UTF-8")
        help_string = ""
        try:
            for i in CMD_HELP[module_name]:
                help_string += i
                help_string += "\n"
        except:
            pass
        if help_string is "":
            reply_pop_up_alert = "{} is useless".format(module_name)
        else:
            reply_pop_up_alert = help_string
        reply_pop_up_alert += "\n `{KYNE_NNAME} :` Use !unload {} to remove this plugin\n\
            ©kyne".format(module_name)
        try:
            await event.answer(reply_pop_up_alert, cache_time=0, alert=True)
        except: 
            halps = "Do !help {} to get the list of commands.".format(module_name)
            await event.answer(halps, cache_time=0, alert=True)

def paginate_help(page_number, loaded_modules, prefix):
    number_of_rows = Config.NO_OF_BUTTONS_DISPLAYED_IN_H_ME_CMD
    number_of_cols = 2
    helpable_modules = []
    for p in loaded_modules:
        if not p.startswith("_"):
            helpable_modules.append(p)
    helpable_modules = sorted(helpable_modules)
    modules = [custom.Button.inline(
        "{} {}".format("🛡", x),
        data="us_module_{}".format(x))
        for x in helpable_modules]
    pairs = list(zip(modules[::number_of_cols], modules[1::number_of_cols]))
    if len(modules) % number_of_cols == 1:
        pairs.append((modules[-1],))
    max_num_pages = ceil(len(pairs) / number_of_rows)
    modulo_page = page_number % max_num_pages
    if len(pairs) > number_of_rows:
        pairs = pairs[modulo_page * number_of_rows:number_of_rows * (modulo_page + 1)] + \
            [
            (custom.Button.inline("⏪", data="{}_prev({})".format(prefix, modulo_page)),
             custom.Button.inline("⏩", data="{}_next({})".format(prefix, modulo_page)))
        ]
    return pairs
