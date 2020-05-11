from asyncio import sleep
from os import remove
from userbot.modules.sql_helper.mute_sql import is_muted, mute, unmute
from asyncio import sleep
from telethon.tl.functions.contacts import BlockRequest, UnblockRequest
import asyncio
from telethon import events
from datetime import datetime, timedelta
from telethon.tl.types import UserStatusEmpty, UserStatusLastMonth, UserStatusLastWeek, UserStatusOffline, UserStatusOnline, UserStatusRecently, ChannelParticipantsKicked, ChatBannedRights
from telethon.tl import functions, types
from time import sleep
from telethon import events
from telethon.utils import pack_bot_file_id
from userbot.modules.sql_helper.oqwelcome_sql import get_current_oqwelcome_settings, \
    add_oqwelcome_setting, rm_oqwelcome_setting, update_previous_oqwelcome
from telethon import events, utils
from telethon.tl import types
from userbot import BOTLOG, BOTLOG_CHATID, CMD_HELP, bot
from userbot.events import kyne3301
from userbot import CMD_HELP, bot, LOGS, CLEAN_WELCOME, BOTLOG_CHATID
from telethon.events import ChatAction
import datetime
from datetime import datetime
from emoji import emojize
from math import sqrt
from telethon.tl.functions.channels import GetFullChannelRequest, GetParticipantsRequest
from telethon.tl.functions.messages import GetHistoryRequest, CheckChatInviteRequest, GetFullChatRequest
from telethon.tl.types import MessageActionChannelMigrateFrom, ChannelParticipantsAdmins
from telethon.errors import (ChannelInvalidError, ChannelPrivateError, ChannelPublicGroupNaError, InviteHashEmptyError, InviteHashExpiredError, InviteHashInvalidError)
from telethon.utils import get_input_location
from userbot import CMD_HELP
from telethon.tl import functions, types
from telethon import functions
from userbot.events import kyne3301
import asyncio
from telethon import events
from telethon.tl.types import ChannelParticipantsAdmins
import html
from telethon.tl.functions.channels import EditBannedRequest
import userbot.modules.sql_helper.warns_sql as sql
from telethon.tl.types import MessageEntityMentionName
from os import remove
import asyncio
from telethon import events
from telethon.tl.types import ChannelParticipantsAdmins
from telethon.errors import (BadRequestError, ChatAdminRequiredError,ImageProcessFailedError, PhotoCropSizeSmallError,UserAdminInvalidError)
from telethon.errors.rpcerrorlist import (UserIdInvalidError,MessageTooLongError)
from telethon.tl.functions.channels import (EditAdminRequest,EditBannedRequest,EditPhotoRequest)
from telethon.tl.functions.messages import UpdatePinnedMessageRequest
from telethon.tl.types import (PeerChannel, ChannelParticipantsAdmins,ChatAdminRights, ChatBannedRights,MessageEntityMentionName, MessageMediaPhoto,ChannelParticipantsBots)
from userbot import BOTLOG, BOTLOG_CHATID, CMD_HELP, bot
from userbot import CMD_HELP, bot, LOGS, CLEAN_WELCOME, BOTLOG_CHATID
from telethon.events import ChatAction
from asyncio import sleep
import asyncio
import io
import re
import userbot.modules.sql_helper.blacklist_sql as sql
from telethon import events, utils
from telethon.tl import types, functions
from userbot import CMD_HELP, bot
from userbot import BOTLOG, BOTLOG_CHATID, CMD_HELP
from asyncio import sleep
from telethon.tl.functions.messages import EditChatDefaultBannedRightsRequest
from telethon.tl.types import ChatBannedRights
from userbot import CMD_HELP
from re import fullmatch, IGNORECASE, escape
from userbot import BOTLOG, BOTLOG_CHATID, CMD_HELP
from requests import get
from telethon.events import ChatAction
from telethon.tl.types import ChannelParticipantsAdmins, Message
import asyncio
import re
from userbot.events import kyne3301
from telethon import events, utils
from telethon.tl import types
from userbot.modules.sql_helper.oqfilter_sql import get_filter, add_filter, remove_filter, get_all_oqfilters, remove_all_oqfilters
from userbot import BOTLOG, BOTLOG_CHATID, CMD_HELP, ANTI_SPAMBOT, ANTI_SPAMBOT_SHOUT, bot
from telethon.errors import (BadRequestError, ChatAdminRequiredError,ImageProcessFailedError, PhotoCropSizeSmallError,UserAdminInvalidError)
from telethon.errors.rpcerrorlist import (UserIdInvalidError,MessageTooLongError)
from telethon.tl.functions.channels import (EditAdminRequest,EditBannedRequest,EditPhotoRequest)
from telethon.tl.functions.messages import UpdatePinnedMessageRequest
from telethon.tl.types import (PeerChat, PeerChannel,ChannelParticipantsAdmins, ChatAdminRights,ChatBannedRights, MessageEntityMentionName,MessageMediaPhoto, ChannelParticipantsBots)
from userbot import BOTLOG, BOTLOG_CHATID, CMD_HELP, bot
from userbot import bot
from userbot.events import obsq, command
from userbot.events import kyne3301
from telethon.tl.functions.messages import EditChatDefaultBannedRightsRequest
from telethon.tl.types import ChatBannedRights
from userbot import CMD_HELP
from userbot import CMD_HELP, ALIVE_NAME, PM_MESSAGE, KYNE_NAME, KYNE_MSG, ORI_MSG
KYNE_NNAME = str(KYNE_NAME) if KYNE_NAME else str(KYNE_MSG)
kyne = bot
# =================== CONSTANT ===================
PP_TOO_SMOL = f"`{KYNE_NNAME}:`**The image is too small**"
PP_ERROR = f"`{KYNE_NNAME}:`**Failure while processing the image**"
NO_ADMIN = f"`{KYNE_NNAME}:`**Sorry, I can't able to get admin rights here!**"
NO_PERM = f"`{KYNE_NNAME}:`**I don't have sufficient permissions!**"
NO_SQL = f"`{KYNE_NNAME}:`**Running on Non-SQL mode!**"
CHAT_PP_CHANGED = f"`{KYNE_NNAME}:`**Chat Picture Changed**"
CHAT_PP_ERROR = f"`{KYNE_NNAME}:`**Some issue with updating the pic,**" \
                "**maybe coz I'm not an admin,**" \
                "**or don't have enough rights.**"
INVALID_MEDIA = "`Invalid Extension`"

BANNED_RIGHTS = ChatBannedRights(
    until_date=None,
    view_messages=True,
    send_messages=True,
    send_media=True,
    send_stickers=True,
    send_gifs=True,
    send_games=True,
    send_inline=True,
    embed_links=True,
)

UNBAN_RIGHTS = ChatBannedRights(
    until_date=None,
    send_messages=None,
    send_media=None,
    send_stickers=None,
    send_gifs=None,
    send_games=None,
    send_inline=None,
    embed_links=None,
)

MUTE_RIGHTS = ChatBannedRights(until_date=None, send_messages=True)

UNMUTE_RIGHTS = ChatBannedRights(until_date=None, send_messages=False)
# ================================================



DELETE_TIMEOUT = 0
TYPE_TEXT = 0
TYPE_PHOTO = 1
TYPE_DOCUMENT = 2



global last_triggered_oqfilters
last_triggered_oqfilters = {}  # pylint:disable=E0602
#filters logic
@kyne.on(events.NewMessage(incoming=True))
async def on_snip(event):
    global last_triggered_oqfilters
    name = event.raw_text
    if event.chat_id in last_triggered_oqfilters:
        if name in last_triggered_oqfilters[event.chat_id]:
            # avoid userbot spam
            # "I demand rights for us bots, we are equal to you humans." -Henri Koivuneva (t.me/UserbotTesting/2698)
            return False
    snips = get_all_oqfilters(event.chat_id)
    if snips:
        for snip in snips:
            pattern = r"( |^|[^\w])" + re.escape(snip.keyword) + r"( |$|[^\w])"
            if re.search(pattern, name, flags=re.IGNORECASE):
                if snip.snip_type == TYPE_PHOTO:
                    media = types.InputPhoto(
                        int(snip.media_id),
                        int(snip.media_access_hash),
                        snip.media_file_reference
                    )
                elif snip.snip_type == TYPE_DOCUMENT:
                    media = types.InputDocument(
                        int(snip.media_id),
                        int(snip.media_access_hash),
                        snip.media_file_reference
                    )
                else:
                    media = None
                message_id = event.message.id
                if event.reply_to_msg_id:
                    message_id = event.reply_to_msg_id
                await event.reply(
                    snip.reply,
                    file=media
                )
                if event.chat_id not in last_triggered_oqfilters:
                    last_triggered_oqfilters[event.chat_id] = []
                last_triggered_oqfilters[event.chat_id].append(name)
                await asyncio.sleep(DELETE_TIMEOUT)
                last_triggered_oqfilters[event.chat_id].remove(name)

@kyne.on(ChatAction)
async def welcome_to_chat(event):
	#welcome logic
    try:
        from userbot.modules.sql_helper.welcome_sql import get_current_welcome_settings
        from userbot.modules.sql_helper.welcome_sql import update_previous_welcome
    except AttributeError:
        return
    cws = get_current_welcome_settings(event.chat_id)
    if cws:
        """user_added=True,
        user_joined=True,
        user_left=False,
        user_kicked=False"""
        if (event.user_joined
                or event.user_added) and not (await event.get_user()).bot:
            if CLEAN_WELCOME:
                try:
                    await event.client.delete_messages(event.chat_id,
                                                       cws.previous_welcome)
                except Exception as e:
                    LOGS.warn(str(e))
            a_user = await event.get_user()
            chat = await event.get_chat()
            me = await event.client.get_me()

            title = chat.title if chat.title else "this chat"
            participants = await event.client.get_participants(chat)
            count = len(participants)
            mention = "[{}](tg://user?id={})".format(a_user.first_name,
                                                     a_user.id)
            my_mention = "[{}](tg://user?id={})".format(me.first_name, me.id)
            first = a_user.first_name
            last = a_user.last_name
            if last:
                fullname = f"{first} {last}"
            else:
                fullname = first
            username = f"@{a_user.username}" if a_user.username else mention
            userid = a_user.id
            my_first = me.first_name
            my_last = me.last_name
            if my_last:
                my_fullname = f"{my_first} {my_last}"
            else:
                my_fullname = my_first
            my_username = f"@{me.username}" if me.username else my_mention
            file_media = None
            current_saved_welcome_message = None
            if cws and cws.f_mesg_id:
                msg_o = await event.client.get_messages(entity=BOTLOG_CHATID,
                                                        ids=int(cws.f_mesg_id))
                file_media = msg_o.media
                current_saved_welcome_message = msg_o.message
            elif cws and cws.reply:
                current_saved_welcome_message = cws.reply
            current_message = await event.reply(
                current_saved_welcome_message.format(mention=mention,
                                                     title=title,
                                                     count=count,
                                                     first=first,
                                                     last=last,
                                                     fullname=fullname,
                                                     username=username,
                                                     userid=userid,
                                                     my_first=my_first,
                                                     my_last=my_last,
                                                     my_fullname=my_fullname,
                                                     my_username=my_username,
                                                     my_mention=my_mention),
                file=file_media)
            update_previous_welcome(event.chat_id, current_message.id)


@kyne.on(events.NewMessage(incoming=True))
async def filter_incoming_handler(handler):
    #filters logic
    try:
        if not (await handler.get_sender()).bot:
            try:
                from userbot.modules.sql_helper.filter_sql import get_filters
            except AttributeError:
                await handler.edit("`Running on Non-SQL mode!`")
                return
            name = handler.raw_text
            filters = get_filters(handler.chat_id)
            if not filters:
                return
            for trigger in filters:
                pro = fullmatch(trigger.keyword, name, flags=IGNORECASE)
                if pro and trigger.f_mesg_id:
                    msg_o = await handler.client.get_messages(
                        entity=BOTLOG_CHATID, ids=int(trigger.f_mesg_id))
                    await handler.reply(msg_o.message, file=msg_o.media)
                elif pro and trigger.reply:
                    await handler.reply(trigger.reply)
    except AttributeError:
        pass



@kyne.on(events.NewMessage(incoming=True))
async def muter(moot):
#gban logic
    try:
        from userbot.modules.sql_helper.spam_mute_sql import is_muted
        from userbot.modules.sql_helper.gmute_sql import is_gmuted
    except AttributeError:
        return
    muted = is_muted(moot.chat_id)
    gmuted = is_gmuted(moot.sender_id)
    me = await moot.client.get_me()
    my_mention = "[{}](tg://user?id={})".format(me.first_name, me.id)
    my_username = f"@{me.username}" if me.username else my_mention
    BANNED_RIGHTS = ChatBannedRights(
    until_date=None,
    view_messages=True,
    send_messages=True,
    send_media=True,
    send_stickers=True,
    send_gifs=True,
    send_games=True,
    send_inline=True,
    embed_links=True,
)
    rights = ChatBannedRights(
        until_date=None,
        send_messages=True,
        send_media=True,
        send_stickers=True,
        send_gifs=True,
        send_games=True,
        send_inline=True,
        embed_links=True,
    )    
    if gmuted:
        for i in gmuted:
            if i.sender == str(moot.sender_id):
            	#fix bug , block gbaned user in pm
                if moot.is_private:       
                    #await moot.delete()  let him send last message :0
                    await moot.client(BlockRequest(moot.sender_id))
                    await moot.reply(
                     f"`{KYNE_NNAME}:` ** Gban User Found!!** \n" 
                     f"`GbanAdmin`: **{my_username}**\n\n"
                     f"**Victim Id**: [{moot.sender_id}](tg://user?id={moot.sender_id})\n"
                     #f"**Victim ID** : `{user.id}`\n"                     
                     #f"**Chat** :  `{gspdr.chat.title}`\n"
                     #f"**Reason**  : `{reason}`\n"
                     f"**Ban user **  : `False`\n"
                     f"**block user **  : `True`\n"
                     f"**Report user **  : `True`\n")
                     #f"**Add user gban list **  : `True`\n")
                    return 
                chat = await moot.get_chat()
                admin = chat.admin_rights
                creator = chat.creator   
                if not admin and not creator:
                	return
                try:
                    await moot.delete()
                    await moot.client(EditBannedRequest(moot.chat_id, moot.sender_id,BANNED_RIGHTS))
                    await moot.reply(
                     f"`{KYNE_NNAME}:` ** Gban User Found!!** \n" 
                     f"`GbanAdmin`: **{my_username}**\n\n"
                     f"**Victim Id**: [{moot.sender_id}](tg://user?id={moot.sender_id})\n"
                     #f"**Victim ID** : `{user.id}`\n"                     
                     #f"**Chat** :  `{gspdr.chat.title}`\n"
                     #f"**Reason**  : `{reason}`\n"
                     f"**Ban user **  : `True`\n"
                     f"**block user **  : `False`\n"
                     f"**Report user **  : `True`\n")
                     #f"**Add user gban list **  : `True`\n")
                except (BadRequestError, UserAdminInvalidError,ChatAdminRequiredError, UserIdInvalidError):
                    await moot.client.send_read_acknowledge(
                        moot.chat_id, moot.id)








@kyne3301(outgoing=True, disable_errors=True, pattern=r"^\!savewelcome(?: |$)(.*)")
async def save_welcome(event):
    try:
        from userbot.modules.sql_helper.welcome_sql import add_welcome_setting
    except AttributeError:
        await event.edit("`Running on Non-SQL mode!`")
        return
    msg = await event.get_reply_message()
    string = event.pattern_match.group(1)
    msg_id = None
    if msg and msg.media and not string:
        if BOTLOG_CHATID:
            await event.client.send_message(
                BOTLOG_CHATID, f"#WELCOME_NOTE\
            \nCHAT ID: {event.chat_id}\
            \nThe following message is saved as the new welcome note for the chat, please do NOT delete it !!"
            )
            msg_o = await event.client.forward_messages(
                entity=BOTLOG_CHATID,
                messages=msg,
                from_peer=event.chat_id,
                silent=True)
            msg_id = msg_o.id
        else:
            await event.edit(
                f"`{KYNE_NNAME}`: **Saving media as part of the welcome note requires the BOTLOG_CHATID to be set.**"
            )
            return
    elif event.reply_to_msg_id and not string:
        rep_msg = await event.get_reply_message()
        string = rep_msg.text
    success = " Welcome note {} for this chat."
    if add_welcome_setting(event.chat_id, 0, string, msg_id) is True:
        await event.edit(success.format('saved'))
    else:
        await event.edit(f"`{KYNE_NNAME}`: **Ops, old welcome message found, i deleted it Sucessfully now you can save new welcome message!**")




@kyne.on(obsq(pattern=f"savewelcome(?: |$)(.*)", allow_sudo=True))
async def save_welcome(event):
    try:
        from userbot.modules.sql_helper.welcome_sql import add_welcome_setting
    except AttributeError:
        await event.reply("`Running on Non-SQL mode!`")
        return
    msg = await event.get_reply_message()
    string = event.pattern_match.group(1)
    msg_id = None
    if msg and msg.media and not string:
        if BOTLOG_CHATID:
            await event.client.send_message(
                BOTLOG_CHATID, f"#WELCOME_NOTE\
            \nCHAT ID: {event.chat_id}\
            \nThe following message is saved as the new welcome note for the chat, please do NOT delete it !!"
            )
            msg_o = await event.client.forward_messages(
                entity=BOTLOG_CHATID,
                messages=msg,
                from_peer=event.chat_id,
                silent=True)
            msg_id = msg_o.id
        else:
            await event.reply(
                f"`{KYNE_NNAME}`: **Saving media as part of the welcome note requires the BOTLOG_CHATID to be set.**"
            )
            return
    elif event.reply_to_msg_id and not string:
        rep_msg = await event.get_reply_message()
        string = rep_msg.text
    success = " Welcome note {} for this chat."
    if add_welcome_setting(event.chat_id, 0, string, msg_id) is True:
        await event.reply(success.format('saved'))
    else:
        await event.reply(f"`{KYNE_NNAME}`: **Ops, old welcome message found, i deleted it Sucessfully now you can save new welcome message!**")











@kyne3301(outgoing=True, disable_errors=True, pattern="^\!checkwelcome$")
async def show_welcome(event):
    try:
        from userbot.modules.sql_helper.welcome_sql import get_current_welcome_settings
    except AttributeError:
        await event.edit("`Running on Non-SQL mode!`")
        return
    cws = get_current_welcome_settings(event.chat_id)
    if not cws:
        await event.edit(f"`{KYNE_NNAME}`: **No welcome message saved here.**")
        return
    elif cws and cws.f_mesg_id:
        msg_o = await event.client.get_messages(entity=BOTLOG_CHATID,
                                                ids=int(cws.f_mesg_id))
        await event.edit(
            f"`{KYNE_NNAME}`: **I am currently welcoming new users with this welcome note.**")
        await event.reply(msg_o.message, file=msg_o.media)
    elif cws and cws.reply:
        await event.edit(
            f"`{KYNE_NNAME}`: **I am currently welcoming new users with this welcome note.**")
        await event.reply(cws.reply)



@kyne.on(obsq(pattern=f"checkwelcome$", allow_sudo=True))
async def show_welcome(event):
    try:
        from userbot.modules.sql_helper.welcome_sql import get_current_welcome_settings
    except AttributeError:
        await event.reply("`Running on Non-SQL mode!`")
        return
    cws = get_current_welcome_settings(event.chat_id)
    if not cws:
        await event.reply(f"`{KYNE_NNAME}`: **No welcome message saved here.**")
        return
    elif cws and cws.f_mesg_id:
        msg_o = await event.client.get_messages(entity=BOTLOG_CHATID,
                                                ids=int(cws.f_mesg_id))
        await event.reply(
            f"`{KYNE_NNAME}`: **I am currently welcoming new users with this welcome note.**")
        await event.reply(msg_o.message, file=msg_o.media)
    elif cws and cws.reply:
        await event.reply(
            f"`{KYNE_NNAME}`: **I am currently welcoming new users with this welcome note.**")
        await event.reply(cws.reply)







@kyne3301(outgoing=True, disable_errors=True, pattern="^\!clearwelcome$")
async def del_welcome(event):
    try:
        from userbot.modules.sql_helper.welcome_sql import rm_welcome_setting
    except AttributeError:
        await event.edit("`Running on Non-SQL mode!`")
        return
    if rm_welcome_setting(event.chat_id) is True:
        await event.edit(f"`{KYNE_NNAME}`: **Welcome note deleted for this chat.**")
    else:
        await event.edit(f"`{KYNE_NNAME}`: ** I Didnt have any welcome messages here **")


@kyne.on(obsq(pattern=f"clearwelcome$", allow_sudo=True))
async def del_welcome(event):
    try:
        from userbot.modules.sql_helper.welcome_sql import rm_welcome_setting
    except AttributeError:
        await event.reply("`Running on Non-SQL mode!`")
        return
    if rm_welcome_setting(event.chat_id) is True:
        await event.reply(f"`{KYNE_NNAME}`: **Welcome note deleted for this chat.**")
    else:
        await event.reply(f"`{KYNE_NNAME}`: ** I Didnt have any welcome messages here **")









@kyne3301(outgoing=True, disable_errors=True, pattern=r"^\!lock ?(.*)")
async def locks(event):
    input_str = event.pattern_match.group(1).lower()
    peer_id = event.chat_id
    msg = None
    media = None
    sticker = None
    gif = None
    gamee = None
    ainline = None
    gpoll = None
    adduser = None
    cpin = None
    changeinfo = None
    if input_str == "msg":
        msg = True
        what = "messages"
    elif input_str == "media":
        media = True
        what = "media"
    elif input_str == "sticker":
        sticker = True
        what = "stickers"
    elif input_str == "gif":
        gif = True
        what = "GIFs"
    elif input_str == "game":
        gamee = True
        what = "games"
    elif input_str == "inline":
        ainline = True
        what = "inline bots"
    elif input_str == "poll":
        gpoll = True
        what = "polls"
    elif input_str == "invite":
        adduser = True
        what = "invites"
    elif input_str == "pin":
        cpin = True
        what = "pins"
    elif input_str == "info":
        changeinfo = True
        what = "chat info"
    elif input_str == "all":
        msg = True
        media = True
        sticker = True
        gif = True
        gamee = True
        ainline = True
        gpoll = True
        adduser = True
        cpin = True
        changeinfo = True
        what = "everything"
    else:
        if not input_str:
            await event.edit(f"`{KYNE_NNAME}`: **I can't lock nothing !!**")
            return
        else:
            await event.edit(f"`Invalid lock type:` {input_str}")
            return

    lock_rights = ChatBannedRights(
        until_date=None,
        send_messages=msg,
        send_media=media,
        send_stickers=sticker,
        send_gifs=gif,
        send_games=gamee,
        send_inline=ainline,
        send_polls=gpoll,
        invite_users=adduser,
        pin_messages=cpin,
        change_info=changeinfo,
    )
    try:
        await event.client(
            EditChatDefaultBannedRightsRequest(peer=peer_id,
                                               banned_rights=lock_rights))
        await event.edit(f"`{KYNE_NNAME}`: **Locked {what} for this chat !!**")
    except BaseException as e:
        await event.edit(
            f"`{KYNE_NNAME}`: **Sorry i can't able to get admin  rights here**\n**Error:** {str(e)}")
        return



@kyne.on(obsq(pattern=f"lock ?(.*)", allow_sudo=True))
async def locks(event):
    input_str = event.pattern_match.group(1).lower()
    peer_id = event.chat_id
    msg = None
    media = None
    sticker = None
    gif = None
    gamee = None
    ainline = None
    gpoll = None
    adduser = None
    cpin = None
    changeinfo = None
    if input_str == "msg":
        msg = True
        what = "messages"
    elif input_str == "media":
        media = True
        what = "media"
    elif input_str == "sticker":
        sticker = True
        what = "stickers"
    elif input_str == "gif":
        gif = True
        what = "GIFs"
    elif input_str == "game":
        gamee = True
        what = "games"
    elif input_str == "inline":
        ainline = True
        what = "inline bots"
    elif input_str == "poll":
        gpoll = True
        what = "polls"
    elif input_str == "invite":
        adduser = True
        what = "invites"
    elif input_str == "pin":
        cpin = True
        what = "pins"
    elif input_str == "info":
        changeinfo = True
        what = "chat info"
    elif input_str == "all":
        msg = True
        media = True
        sticker = True
        gif = True
        gamee = True
        ainline = True
        gpoll = True
        adduser = True
        cpin = True
        changeinfo = True
        what = "everything"
    else:
        if not input_str:
            await event.reply(f"`{KYNE_NNAME}`: **I can't lock nothing !!**")
            return
        else:
            await event.reply(f"`Invalid lock type:` {input_str}")
            return

    lock_rights = ChatBannedRights(
        until_date=None,
        send_messages=msg,
        send_media=media,
        send_stickers=sticker,
        send_gifs=gif,
        send_games=gamee,
        send_inline=ainline,
        send_polls=gpoll,
        invite_users=adduser,
        pin_messages=cpin,
        change_info=changeinfo,
    )
    try:
        await event.client(
            EditChatDefaultBannedRightsRequest(peer=peer_id,
                                               banned_rights=lock_rights))
        await event.reply(f"`{KYNE_NNAME}`: **Locked {what} for this chat !!**")
    except BaseException as e:
        await event.reply(
            f"`{KYNE_NNAME}`: **Sorry i can't able to get admin  rights here**\n**Error:** {str(e)}")
        return



@kyne3301(outgoing=True, disable_errors=True, pattern=r"^!unlock ?(.*)")
async def rem_locks(event):
    input_str = event.pattern_match.group(1).lower()
    peer_id = event.chat_id
    msg = None
    media = None
    sticker = None
    gif = None
    gamee = None
    ainline = None
    gpoll = None
    adduser = None
    cpin = None
    changeinfo = None
    if input_str == "msg":
        msg = False
        what = "messages"
    elif input_str == "media":
        media = False
        what = "media"
    elif input_str == "sticker":
        sticker = False
        what = "stickers"
    elif input_str == "gif":
        gif = False
        what = "GIFs"
    elif input_str == "game":
        gamee = False
        what = "games"
    elif input_str == "inline":
        ainline = False
        what = "inline bots"
    elif input_str == "poll":
        gpoll = False
        what = "polls"
    elif input_str == "invite":
        adduser = False
        what = "invites"
    elif input_str == "pin":
        cpin = False
        what = "pins"
    elif input_str == "info":
        changeinfo = False
        what = "chat info"
    elif input_str == "all":
        msg = False
        media = False
        sticker = False
        gif = False
        gamee = False
        ainline = False
        gpoll = False
        adduser = False
        cpin = False
        changeinfo = False
        what = "everything"
    else:
        if not input_str:
            await event.edit(f"`{KYNE_NNAME}`: **I can't unlock nothing !!**")
            return
        else:
            await event.edit(f"`Invalid unlock type:` {input_str}")
            return

    unlock_rights = ChatBannedRights(
        until_date=None,
        send_messages=msg,
        send_media=media,
        send_stickers=sticker,
        send_gifs=gif,
        send_games=gamee,
        send_inline=ainline,
        send_polls=gpoll,
        invite_users=adduser,
        pin_messages=cpin,
        change_info=changeinfo,
    )
    try:
        await event.client(
            EditChatDefaultBannedRightsRequest(peer=peer_id,
                                               banned_rights=unlock_rights))
        await event.edit(f"`{KYNE_NNAME}`: **Unlocked {what} for this chat !!**")
    except BaseException as e:
        await event.edit(
            f"`{KYNE_NNAME}`: **Sorry i can't able to get admin rights here`\n**Error:** {str(e)}")
        return


@kyne.on(obsq(pattern=f"unlock ?(.*)", allow_sudo=True))
async def rem_locks(event):
    input_str = event.pattern_match.group(1).lower()
    peer_id = event.chat_id
    msg = None
    media = None
    sticker = None
    gif = None
    gamee = None
    ainline = None
    gpoll = None
    adduser = None
    cpin = None
    changeinfo = None
    if input_str == "msg":
        msg = False
        what = "messages"
    elif input_str == "media":
        media = False
        what = "media"
    elif input_str == "sticker":
        sticker = False
        what = "stickers"
    elif input_str == "gif":
        gif = False
        what = "GIFs"
    elif input_str == "game":
        gamee = False
        what = "games"
    elif input_str == "inline":
        ainline = False
        what = "inline bots"
    elif input_str == "poll":
        gpoll = False
        what = "polls"
    elif input_str == "invite":
        adduser = False
        what = "invites"
    elif input_str == "pin":
        cpin = False
        what = "pins"
    elif input_str == "info":
        changeinfo = False
        what = "chat info"
    elif input_str == "all":
        msg = False
        media = False
        sticker = False
        gif = False
        gamee = False
        ainline = False
        gpoll = False
        adduser = False
        cpin = False
        changeinfo = False
        what = "everything"
    else:
        if not input_str:
            await event.reply(f"`{KYNE_NNAME}`: **I can't unlock nothing !!**")
            return
        else:
            await event.reply(f"`Invalid unlock type:` {input_str}")
            return

    unlock_rights = ChatBannedRights(
        until_date=None,
        send_messages=msg,
        send_media=media,
        send_stickers=sticker,
        send_gifs=gif,
        send_games=gamee,
        send_inline=ainline,
        send_polls=gpoll,
        invite_users=adduser,
        pin_messages=cpin,
        change_info=changeinfo,
    )
    try:
        await event.client(
            EditChatDefaultBannedRightsRequest(peer=peer_id,
                                               banned_rights=unlock_rights))
        await event.reply(f"`{KYNE_NNAME}`: **Unlocked {what} for this chat !!**")
    except BaseException as e:
        await event.reply(
            f"`{KYNE_NNAME}`: **Sorry i can't able to get admin rights here`\n**Error:** {str(e)}")
        return







@kyne3301(outgoing=True, disable_errors=True, pattern="^\!userid$")
async def useridgetter(target):
    """ For .userid command, returns the ID of the target user. """
    message = await target.get_reply_message()
    if message:
        if not message.forward:
            user_id = message.sender.id
            if message.sender.username:
                name = "@" + message.sender.username
            else:
                name = "**" + message.sender.first_name + "**"
        else:
            user_id = message.forward.sender.id
            if message.forward.sender.username:
                name = "@" + message.forward.sender.username
            else:
                name = "*" + message.forward.sender.first_name + "*"
        await target.edit(" **Name:** {} \n**User ID:** `{}`".format(
            name, user_id))


@kyne.on(obsq(pattern=f"userid$", allow_sudo=True))
async def useridgetter(target):
    """ For .userid command, returns the ID of the target user. """
    message = await target.get_reply_message()
    if message:
        if not message.forward:
            user_id = message.sender.id
            if message.sender.username:
                name = "@" + message.sender.username
            else:
                name = "**" + message.sender.first_name + "**"
        else:
            user_id = message.forward.sender.id
            if message.forward.sender.username:
                name = "@" + message.forward.sender.username
            else:
                name = "*" + message.forward.sender.first_name + "*"
        await target.reply(" **Name:** {} \n**User ID:** `{}`".format(
            name, user_id))



@kyne3301(outgoing=True, disable_errors=True, pattern="^\!link(?: |$)(.*)")
async def permalink(mention):
    """ For .link command, generates a link to the user's PM with a custom text. """
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    if custom:
        await mention.edit(f"[{custom}](tg://user?id={user.id})")
    else:
        tag = user.first_name.replace("\u2060",
                                      "") if user.first_name else user.username
        await mention.edit(f"`{KYNE_NNAME}`: [{tag}](tg://user?id={user.id})")


@kyne.on(obsq(pattern=f"link(?: |$)(.*)", allow_sudo=True))
async def permalink(mention):
    """ For .link command, generates a link to the user's PM with a custom text. """
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    if custom:
        await mention.reply(f"[{custom}](tg://user?id={user.id})")
    else:
        tag = user.first_name.replace("\u2060",
                                      "") if user.first_name else user.username
        await mention.reply(f"`{KYNE_NNAME}`: [{tag}](tg://user?id={user.id})")



@kyne3301(outgoing=True, disable_errors=True, pattern="^\!chatid$")
async def chatidgetter(chat):
    """ For .chatid, returns the ID of the chat you are in at that moment. """
    await chat.edit(f"`{KYNE_NNAME}`: Chat ID: `" + str(chat.chat_id) + "`")


@kyne.on(obsq(pattern=f"chatid$", allow_sudo=True))
async def chatidgetter(chat):
    """ For .chatid, returns the ID of the chat you are in at that moment. """
    await chat.reply(f"`{KYNE_NNAME}`: Chat ID: `" + str(chat.chat_id) + "`")




@kyne3301(outgoing=True, disable_errors=True, pattern=r"^\!log(?: |$)([\s\S]*)")
async def log(log_text):
    """ For .log command, forwards a message or the command argument to the bot logs group """
    if BOTLOG:
        if log_text.reply_to_msg_id:
            reply_msg = await log_text.get_reply_message()
            await reply_msg.forward_to(BOTLOG_CHATID)
        elif log_text.pattern_match.group(1):
            user = f"#LOG / Chat ID: {log_text.chat_id}\n\n"
            textx = user + log_text.pattern_match.group(1)
            await bot.send_message(BOTLOG_CHATID, textx)
        else:
            await log_text.edit(f"`{KYNE_NNAME}`: **What am I supposed to log?**")
            return
        await log_text.edit(f"`{KYNE_NNAME}`: **Logged Successfully**")
    else:
        await log_text.edit(f"`{KYNE_NNAME}`: **This feature requires Logging to be enabled!**")
    await sleep(2)
    await log_text.delete()

@kyne.on(obsq(pattern=f"log$", allow_sudo=True))
async def iqless(e):
    await e.reply(f"`{KYNE_NNAME}`: **Privacy error! , Sorry sudo users dont have permission to access it!**")






@kyne3301(outgoing=True, disable_errors=True, pattern="^\!kickme$")
async def kickme(leave):
    """ Basically it's .kickme command """
    await leave.edit(f"`{KYNE_NNAME}`: **My master Didnt like this place......GoodBye!**")
    await leave.client.kick_participant(leave.chat_id, 'me')

@kyne.on(obsq(pattern=f"kickme$", allow_sudo=True))
async def iqless(e):
    await e.reply(f"`{KYNE_NNAME}`: **Privacy error! , Sorry sudo users dont have permission to access it!**")







@kyne3301(outgoing=True, disable_errors=True, pattern="^\!setgpic$", groups_only=True)
async def set_group_photo(gpic):
    if not gpic.is_group:
        await gpic.edit(f"`{KYNE_NNAME}:` **I don't think this is a group.**")
        return
    replymsg = await gpic.get_reply_message()
    chat = await gpic.get_chat()
    admin = chat.admin_rights
    creator = chat.creator
    photo = None
    if not admin and not creator:
        await gpic.edit(NO_ADMIN)
        return
    if replymsg and replymsg.media:
        if isinstance(replymsg.media, MessageMediaPhoto):
            photo = await gpic.client.download_media(message=replymsg.photo)
        elif "image" in replymsg.media.document.mime_type.split('/'):
            photo = await gpic.client.download_file(replymsg.media.document)
        else:
            await gpic.edit(INVALID_MEDIA)
    if photo:
        try:
            await gpic.client(
                EditPhotoRequest(gpic.chat_id, await
                                 gpic.client.upload_file(photo)))
            await gpic.edit(CHAT_PP_CHANGED)

        except PhotoCropSizeSmallError:
            await gpic.edit(PP_TOO_SMOL)
        except ImageProcessFailedError:
            await gpic.edit(PP_ERROR)



@kyne.on(obsq(pattern=f"setgpic$", allow_sudo=True))
async def set_group_photo(gpic):
    if not gpic.is_group:
        await gpic.reply(f"`{KYNE_NNAME}:` **I don't think this is a group.**")
        return
    replymsg = await gpic.get_reply_message()
    chat = await gpic.get_chat()
    admin = chat.admin_rights
    creator = chat.creator
    photo = None
    if not admin and not creator:
        await gpic.reply(NO_ADMIN)
        return
    if replymsg and replymsg.media:
        if isinstance(replymsg.media, MessageMediaPhoto):
            photo = await gpic.client.download_media(message=replymsg.photo)
        elif "image" in replymsg.media.document.mime_type.split('/'):
            photo = await gpic.client.download_file(replymsg.media.document)
        else:
            await gpic.reply(INVALID_MEDIA)
    if photo:
        try:
            await gpic.client(
                EditPhotoRequest(gpic.chat_id, await
                                 gpic.client.upload_file(photo)))
            await gpic.reply(CHAT_PP_CHANGED)

        except PhotoCropSizeSmallError:
            await gpic.reply(PP_TOO_SMOL)
        except ImageProcessFailedError:
            await gpic.reply(PP_ERROR)




@kyne3301(outgoing=True, disable_errors=True, pattern="^\!promote(?: |$)(.*)", groups_only=True)
async def promote(promt):
    """ For .promote command, promotes the replied/tagged person """
    # Get targeted chat
    chat = await promt.get_chat()
    # Grab admin status or creator in a chat
    admin = chat.admin_rights
    creator = chat.creator

    # If not admin and not creator, also return
    if not admin and not creator:
        await promt.edit(NO_ADMIN)
        return

    new_rights = ChatAdminRights(add_admins=False,
                                 invite_users=True,
                                 change_info=False,
                                 ban_users=True,
                                 delete_messages=True,
                                 pin_messages=True)

    await promt.edit(f"`{KYNE_NNAME}:` **Promoting User**")
    user, rank = await get_user_from_event(promt)
    if not rank:
        # Just in case.
        rank = "admin"
    if user:
        pass
    else:
        return

    # Try to promote if current user is admin or creator
    try:
        await promt.client(
            EditAdminRequest(promt.chat_id, user.id, new_rights, rank))
        await promt.edit(f"`{KYNE_NNAME}:` **Promoted user [{user.first_name}](tg://user?id={user.id}) to admin  Sucessfully in {promt.chat.title}**")

    # If Telethon spit BadRequestError, assume
    # we don't have Promote permission
    except BadRequestError:
        await promt.edit(NO_PERM)
        return

    # Announce to the logging group if we have promoted successfully
    if BOTLOG:
        await promt.client.send_message(
            BOTLOG_CHATID, "I HAVE PROMOTED\n"
            f"USER: [{user.first_name}](tg://user?id={user.id})\n"
            f"CHAT: {promt.chat.title}({promt.chat_id})")



@kyne.on(obsq(pattern=f"promote(?: |$)(.*)", allow_sudo=True))
async def promote(promt):
    """ For .promote command, promotes the replied/tagged person """
    # Get targeted chat
    chat = await promt.get_chat()
    # Grab admin status or creator in a chat
    admin = chat.admin_rights
    creator = chat.creator

    # If not admin and not creator, also return
    if not admin and not creator:
        await promt.reply(NO_ADMIN)
        return

    new_rights = ChatAdminRights(add_admins=False,
                                 invite_users=True,
                                 change_info=False,
                                 ban_users=True,
                                 delete_messages=True,
                                 pin_messages=True)

    await promt.reply(f"`{KYNE_NNAME}:` **Promoting User**")
    user, rank = await get_user_from_event(promt)
    if not rank:
        # Just in case.
        rank = "admin"
    if user:
        pass
    else:
        return

    # Try to promote if current user is admin or creator
    try:
        await promt.client(
            EditAdminRequest(promt.chat_id, user.id, new_rights, rank))
        await promt.reply(f"`{KYNE_NNAME}:` **Promoted user [{user.first_name}](tg://user?id={user.id}) to admin  Sucessfully in {promt.chat.title}**")

    # If Telethon spit BadRequestError, assume
    # we don't have Promote permission
    except BadRequestError:
        await promt.reply(NO_PERM)
        return

    # Announce to the logging group if we have promoted successfully
    if BOTLOG:
        await promt.client.send_message(
            BOTLOG_CHATID, "I HAVE PROMOTED\n"
            f"USER: [{user.first_name}](tg://user?id={user.id})\n"
            f"CHAT: {promt.chat.title}({promt.chat_id})")










@kyne3301(outgoing=True, disable_errors=True, pattern="^\!demote(?: |$)(.*)", groups_only=True)
async def demote(dmod):
    """ For .demote command, demotes the replied/tagged person """
    # Admin right check
    chat = await dmod.get_chat()
    admin = chat.admin_rights
    creator = chat.creator

    if not admin and not creator:
        await dmod.edit(NO_ADMIN)
        return

    # If passing, declare that we're going to demote
    await dmod.edit(f"`{KYNE_NNAME}:`** Demoting user......**")
    rank = "admin"  # dummy rank, lol.
    user = await get_user_from_event(dmod)
    user = user[0]
    if user:
        pass
    else:
        return

    # New rights after demotion
    newrights = ChatAdminRights(add_admins=None,
                                invite_users=None,
                                change_info=None,
                                ban_users=None,
                                delete_messages=None,
                                pin_messages=None)
    # Edit Admin Permission
    try:
        await dmod.client(
            EditAdminRequest(dmod.chat_id, user.id, newrights, rank))

    # If we catch BadRequestError from Telethon
    # Assume we don't have permission to demote
    except BadRequestError:
        await dmod.edit(NO_PERM)
        return
    await dmod.edit(f"`{KYNE_NNAME}:` **Demoted user [{user.first_name}](tg://user?id={user.id}) to admin  Sucessfully in {dmod.chat.title}**")

    # Announce to the logging group if we have demoted successfully
    if BOTLOG:
        await dmod.client.send_message(
            BOTLOG_CHATID, "#DEMOTE\n"
            f"USER: [{user.first_name}](tg://user?id={user.id})\n"
            f"CHAT: {dmod.chat.title}(`{dmod.chat_id}`)")

@kyne.on(obsq(pattern=f"demote(?: |$)(.*)", allow_sudo=True))
async def demote(dmod):
    """ For .demote command, demotes the replied/tagged person """
    # Admin right check
    chat = await dmod.get_chat()
    admin = chat.admin_rights
    creator = chat.creator

    if not admin and not creator:
        await dmod.reply(NO_ADMIN)
        return

    # If passing, declare that we're going to demote
    await dmod.reply(f"`{KYNE_NNAME}:`** Demoting user......**")
    rank = "admin"  # dummy rank, lol.
    user = await get_user_from_event(dmod)
    user = user[0]
    if user:
        pass
    else:
        return

    # New rights after demotion
    newrights = ChatAdminRights(add_admins=None,
                                invite_users=None,
                                change_info=None,
                                ban_users=None,
                                delete_messages=None,
                                pin_messages=None)
    # Edit Admin Permission
    try:
        await dmod.client(
            EditAdminRequest(dmod.chat_id, user.id, newrights, rank))

    # If we catch BadRequestError from Telethon
    # Assume we don't have permission to demote
    except BadRequestError:
        await dmod.reply(NO_PERM)
        return
    await dmod.reply(f"`{KYNE_NNAME}:` **Demoted user [{user.first_name}](tg://user?id={user.id}) to admin  Sucessfully in {dmod.chat.title}**")

    # Announce to the logging group if we have demoted successfully
    if BOTLOG:
        await dmod.client.send_message(
            BOTLOG_CHATID, "#DEMOTE\n"
            f"USER: [{user.first_name}](tg://user?id={user.id})\n"
            f"CHAT: {dmod.chat.title}(`{dmod.chat_id}`)")






@kyne3301(outgoing=True, disable_errors=True, pattern="^\!ban(?: |$)(.*)", groups_only=True)
async def ban(bon):
    """ For .ban command, bans the replied/tagged person """
    # Here laying the sanity check
    chat = await bon.get_chat()
    admin = chat.admin_rights
    creator = chat.creator

    # Well
    if not admin and not creator:
        await bon.edit(NO_ADMIN)
        return

    user, reason = await get_user_from_event(bon)
    if user:
        pass
    else:
        return

    # Announce that we're going to whack the pest
    await bon.edit(f"`{KYNE_NNAME}:` **Banning user......**")

    try:
        await bon.client(EditBannedRequest(bon.chat_id, user.id,
                                           BANNED_RIGHTS))
    except BadRequestError:
        await bon.edit(NO_PERM)
        return
    # Helps ban group join spammers more easily
    try:
        reply = await bon.get_reply_message()
        if reply:
            await reply.delete()
    except BadRequestError:
        await bon.edit(f"`{KYNE_NNAME}`: **User still banned!**")
        return
    # Delete message and then tell that the command
    # is done gracefully
    # Shout out the ID, so that fedadmins can fban later
    if reason:
        await bon.edit(f"`{KYNE_NNAME}`:  **{user.first_name} was banned in {bon.chat.title}**!!\
        \nID: `{str(user.id)}`\
        \nReason: {reason}**")
    else:
        await bon.edit(f"`{KYNE_NNAME}`: **{user.first_name} was banned in {bon.chat.title}**!!\
        \nUSERID: `{str(user.id)}`")
    # Announce to the logging group if we have banned the person
    # successfully!
    if BOTLOG:
        await bon.client.send_message(
            BOTLOG_CHATID, "#BANNED MEMBER\n"
            f"USER: [{user.first_name}](tg://user?id={user.id})\n"
            f"CHAT: {bon.chat.title}(`{bon.chat_id}`)")



@kyne.on(obsq(pattern=f"ban(?: |$)(.*)", allow_sudo=True))
async def ban(bon):
    """ For .ban command, bans the replied/tagged person """
    # Here laying the sanity check
    chat = await bon.get_chat()
    admin = chat.admin_rights
    creator = chat.creator

    # Well
    if not admin and not creator:
        await bon.reply(NO_ADMIN)
        return

    user, reason = await get_user_from_event(bon)
    if user:
        pass
    else:
        return

    # Announce that we're going to whack the pest
    await bon.reply(f"`{KYNE_NNAME}:` **Banning user......**")

    try:
        await bon.client(EditBannedRequest(bon.chat_id, user.id,
                                           BANNED_RIGHTS))
    except BadRequestError:
        await bon.reply(NO_PERM)
        return
    # Helps ban group join spammers more easily
    try:
        reply = await bon.get_reply_message()
        if reply:
            await reply.delete()
    except BadRequestError:
        await bon.reply(f"`{KYNE_NNAME}`: **User still banned!**")
        return
    # Delete message and then tell that the command
    # is done gracefully
    # Shout out the ID, so that fedadmins can fban later
    if reason:
        await bon.reply(f"`{KYNE_NNAME}`:  **{user.first_name} was banned in {bon.chat.title}**!!\
        \nID: `{str(user.id)}`\
        \nReason: {reason}**")
    else:
        await bon.reply(f"`{KYNE_NNAME}`: **{user.first_name} was banned in {bon.chat.title}**!!\
        \nUSERID: `{str(user.id)}`")
    # Announce to the logging group if we have banned the person
    # successfully!
    if BOTLOG:
        await bon.client.send_message(
            BOTLOG_CHATID, "#BANNED MEMBER\n"
            f"USER: [{user.first_name}](tg://user?id={user.id})\n"
            f"CHAT: {bon.chat.title}(`{bon.chat_id}`)")




@kyne3301(outgoing=True, disable_errors=True, pattern="^\!unban(?: |$)(.*)", groups_only=True)
async def nothanos(unbon):
    """ For .unban command, unbans the replied/tagged person """
    # Here laying the sanity check
    chat = await unbon.get_chat()
    admin = chat.admin_rights
    creator = chat.creator

    # Well
    if not admin and not creator:
        await unbon.edit(NO_ADMIN)
        return

    # If everything goes well...
    await unbon.edit(f"`{KYNE_NNAME}:` **UnbanningUser........**")

    user = await get_user_from_event(unbon)
    user = user[0]
    if user:
        pass
    else:
        return

    try:
        await unbon.client(
            EditBannedRequest(unbon.chat_id, user.id, UNBAN_RIGHTS))
        await unbon.edit(f"`{KYNE_NNAME}:` **{user.first_name} was unbanned in {unbon.chat.title}**")

        if BOTLOG:
            await unbon.client.send_message(
                BOTLOG_CHATID, "#UNBAN\n"
                f"USER: [{user.first_name}](tg://user?id={user.id})\n"
                f"CHAT: {unbon.chat.title}(`{unbon.chat_id}`)")
    except UserIdInvalidError:
        await unbon.edit(f"`{KYNE_NNAME}:` **Uh oh my unban logic broke!**")


@kyne.on(obsq(pattern=f"unban(?: |$)(.*)", allow_sudo=True))
async def nothanos(unbon):
    """ For .unban command, unbans the replied/tagged person """
    # Here laying the sanity check
    chat = await unbon.get_chat()
    admin = chat.admin_rights
    creator = chat.creator

    # Well
    if not admin and not creator:
        await unbon.reply(NO_ADMIN)
        return

    # If everything goes well...
    await unbon.reply(f"`{KYNE_NNAME}:` **UnbanningUser........**")

    user = await get_user_from_event(unbon)
    user = user[0]
    if user:
        pass
    else:
        return

    try:
        await unbon.client(
            EditBannedRequest(unbon.chat_id, user.id, UNBAN_RIGHTS))
        await unbon.reply(f"`{KYNE_NNAME}:` **{user.first_name} was unbanned in {unbon.chat.title}**")

        if BOTLOG:
            await unbon.client.send_message(
                BOTLOG_CHATID, "#UNBAN\n"
                f"USER: [{user.first_name}](tg://user?id={user.id})\n"
                f"CHAT: {unbon.chat.title}(`{unbon.chat_id}`)")
    except UserIdInvalidError:
        await unbon.reply(f"`{KYNE_NNAME}:` **Uh oh my unban logic broke!**")




@kyne3301(outgoing=True, disable_errors=True, pattern="^\!mute(?: |$)(.*)", groups_only=True)
async def spider(spdr):
    """
    This function is basically muting peeps
    """
    # Check if the function running under SQL mode
    try:
        from userbot.modules.sql_helper.spam_mute_sql import mute
    except AttributeError:
        await spdr.edit(NO_SQL)
        return

    # Admin or creator check
    chat = await spdr.get_chat()
    admin = chat.admin_rights
    creator = chat.creator

    # If not admin and not creator, return
    if not admin and not creator:
        await spdr.edit(NO_ADMIN)
        return

    user, reason = await get_user_from_event(spdr)
    if user:
        pass
    else:
        return

    self_user = await spdr.client.get_me()

    if user.id == self_user.id:
        await spdr.edit(
            f"`{KYNE_NNAME}:`**Sorry, I can't mute my self**")
        return

    # If everything goes well, do announcing and mute
    await spdr.edit(f"`{KYNE_NNAME}:` **Muting user........**")    
    if mute(spdr.chat_id, user.id) is False:
        return await spdr.edit('f"`{KYNE_NNAME}: ` **Error! User probably already muted.**`')
    else:
        try:
            await spdr.client(
                EditBannedRequest(spdr.chat_id, user.id, MUTE_RIGHTS))

            # Announce that the function is done
            if reason:
                await spdr.edit(f"`{KYNE_NNAME}: `**{user.first_name} was muted in {spdr.chat.title}**\n"
                                               f"`Reason:`**{reason}**")
            else:
                await spdr.edit(f"`{KYNE_NNAME}: `**{user.first_name} was muted in {spdr.chat.title}**")


            # Announce to logging group
            if BOTLOG:
                await spdr.client.send_message(
                    BOTLOG_CHATID, "#MUTE\n"
                    f"USER: [{user.first_name}](tg://user?id={user.id})\n"
                    f"CHAT: {spdr.chat.title}(`{spdr.chat_id}`)")
        except UserIdInvalidError:
            return await spdr.edit("`Uh oh my mute logic broke!`")

@kyne.on(obsq(pattern=f"mute(?: |$)(.*)", allow_sudo=True))
async def spider(spdr):
    """
    This function is basically muting peeps
    """
    # Check if the function running under SQL mode
    try:
        from userbot.modules.sql_helper.spam_mute_sql import mute
    except AttributeError:
        await spdr.reply(NO_SQL)
        return

    # Admin or creator check
    chat = await spdr.get_chat()
    admin = chat.admin_rights
    creator = chat.creator

    # If not admin and not creator, return
    if not admin and not creator:
        await spdr.reply(NO_ADMIN)
        return

    user, reason = await get_user_from_event(spdr)
    if user:
        pass
    else:
        return

    self_user = await spdr.client.get_me()

    if user.id == self_user.id:
        await spdr.reply(
            f"`{KYNE_NNAME}:`**Sorry, I can't mute my self**")
        return

    # If everything goes well, do announcing and mute
    await spdr.reply(f"`{KYNE_NNAME}:` **Muting user........**")    
    if mute(spdr.chat_id, user.id) is False:
        return await spdr.reply('f"`{KYNE_NNAME}: ` **Error! User probably already muted.**`')
    else:
        try:
            await spdr.client(
                EditBannedRequest(spdr.chat_id, user.id, MUTE_RIGHTS))

            # Announce that the function is done
            if reason:
                await spdr.reply(f"`{KYNE_NNAME}: `**{user.first_name} was muted in {spdr.chat.title}**\n"
                                               f"`Reason:`**{reason}**")
            else:
                await spdr.reply(f"`{KYNE_NNAME}: `**{user.first_name} was muted in {spdr.chat.title}**")


            # Announce to logging group
            if BOTLOG:
                await spdr.client.send_message(
                    BOTLOG_CHATID, "#MUTE\n"
                    f"USER: [{user.first_name}](tg://user?id={user.id})\n"
                    f"CHAT: {spdr.chat.title}(`{spdr.chat_id}`)")
        except UserIdInvalidError:
            return await spdr.reply("`Uh oh my mute logic broke!`")


      


@kyne3301(outgoing=True, disable_errors=True, pattern="^\!unmute(?: |$)(.*)", groups_only=True)
async def unmoot(unmot):
    """ For .unmute command, unmute the replied/tagged person """
    # Admin or creator check
    chat = await unmot.get_chat()
    admin = chat.admin_rights
    creator = chat.creator

    # If not admin and not creator, return
    if not admin and not creator:
        await unmot.edit(NO_ADMIN)
        return

    # Check if the function running under SQL mode
    try:
        from userbot.modules.sql_helper.spam_mute_sql import unmute
    except AttributeError:
        await unmot.edit(NO_SQL)
        return

    # If admin or creator, inform the user and start unmuting
    await unmot.edit(f"`{KYNE_NNAME}`**unmuting user........**")
    user = await get_user_from_event(unmot)
    user = user[0]
    if user:
        pass
    else:
        return

    if unmute(unmot.chat_id, user.id) is False:
        return await unmot.edit(f"`{KYNE_NNAME}: `**Error! User probably already unmuted.**")
    else:

        try:
            await unmot.client(
                EditBannedRequest(unmot.chat_id, user.id, UNBAN_RIGHTS))
            await unmot.edit(f"`{KYNE_NNAME}: `**{user.first_name} was unmuted in {unmot.chat.title}**")
        except UserIdInvalidError:
            await unmot.edit("`{KYNE_NNAME}: `**Uh oh my unmute logic broke!**")
            return

        if BOTLOG:
            await unmot.client.send_message(
                BOTLOG_CHATID, "#UNMUTE\n"
                f"USER: [{user.first_name}](tg://user?id={user.id})\n"
                f"CHAT: {unmot.chat.title}(`{unmot.chat_id}`)")


@kyne.on(obsq(pattern=f"unmute(?: |$)(.*)", allow_sudo=True))
async def unmoot(unmot):
    """ For .unmute command, unmute the replied/tagged person """
    # Admin or creator check
    chat = await unmot.get_chat()
    admin = chat.admin_rights
    creator = chat.creator

    # If not admin and not creator, return
    if not admin and not creator:
        await unmot.reply(NO_ADMIN)
        return

    # Check if the function running under SQL mode
    try:
        from userbot.modules.sql_helper.spam_mute_sql import unmute
    except AttributeError:
        await unmot.reply(NO_SQL)
        return

    # If admin or creator, inform the user and start unmuting
    await unmot.reply(f"`{KYNE_NNAME}`**unmuting user........**")
    user = await get_user_from_event(unmot)
    user = user[0]
    if user:
        pass
    else:
        return

    if unmute(unmot.chat_id, user.id) is False:
        return await unmot.reply(f"`{KYNE_NNAME}: `**Error! User probably already unmuted.**")
    else:

        try:
            await unmot.client(
                EditBannedRequest(unmot.chat_id, user.id, UNBAN_RIGHTS))
            await unmot.reply(f"`{KYNE_NNAME}: `**{user.first_name} was unmuted in {unmot.chat.title}**")
        except UserIdInvalidError:
            await unmot.reply("`{KYNE_NNAME}: `**Uh oh my unmute logic broke!**")
            return

        if BOTLOG:
            await unmot.client.send_message(
                BOTLOG_CHATID, "#UNMUTE\n"
                f"USER: [{user.first_name}](tg://user?id={user.id})\n"
                f"CHAT: {unmot.chat.title}(`{unmot.chat_id}`)")






@kyne3301(outgoing=True, disable_errors=False, pattern="^!ungban(?: |$)(.*)")
async def ungmoot(un_gmute):
    """ For .ungmute command, ungmutes the target in the userbot """
    # Admin or creator check
    me = await un_gmute.client.get_me()
    my_mention = "[{}](tg://user?id={})".format(me.first_name, me.id)
    my_username = f"@{me.username}" if me.username else my_mention
    chat = await un_gmute.get_chat()
    if un_gmute.is_private:       
       #await un_gmute.edit(f"`{KYNE_NNAME}:` **Gban user in group!!**")
       try:
            from userbot.modules.sql_helper.gmute_sql import ungmute
       except AttributeError:
            await un_gmute.edit(NO_SQL)
            return

       user, reason = await get_user_from_event(un_gmute)
       if user:
            pass
       else:
            return    
       await un_gmute.edit(f"`{KYNE_NNAME}:` **unGbaning User !! **")
       if ungmute(user.id) is False:
           await un_gmute.edit(
            f"`{KYNE_NNAME}:`**Error! User probably already ungbanned.**")
       else:
          if reason:
              await un_gmute.edit(f"`{KYNE_NNAME}:` **Admin {my_username} UnGbanned [{user.first_name}](tg://user?id={user.id})**")
          else:
              await un_gmute.edit(f"`{KYNE_NNAME}:` **Admin {my_username} UnGbanned [{user.first_name}](tg://user?id={user.id})**")      
       return                
    # If not admin and not creator, remove user from gbanned list
    admin = chat.admin_rights
    creator = chat.creator   
    if not admin and not creator:
        try:
            from userbot.modules.sql_helper.gmute_sql import ungmute
        except AttributeError:
            await un_gmute.edit(NO_SQL)
            return

        user, reason = await get_user_from_event(un_gmute)
        if user:
            pass
        else:
            return    
        await un_gmute.edit(f"`{KYNE_NNAME}:` **unGbaning User !! **")
        if ungmute(user.id) is False:
           await un_gmute.edit(
            f"`{KYNE_NNAME}:`**Error! User probably already ungbanned.**")
        else:
          if reason:
              await un_gmute.edit(f"`{KYNE_NNAME}:` **Admin {my_username} UnGbanned [{user.first_name}](tg://user?id={user.id})**")
          else:
              await un_gmute.edit(f"`{KYNE_NNAME}:` **Admin {my_username} UnGbanned [{user.first_name}](tg://user?id={user.id})**")      
        return                

    # Check if the function running under SQL mode
    try:
        from userbot.modules.sql_helper.gmute_sql import ungmute
    except AttributeError:
        await un_gmute.edit(NO_SQL)
        return

    user = await get_user_from_event(un_gmute)
    user = user[0]
    if user:
        pass
    else:
        return

    # If pass, inform and start ungmuting
    await un_gmute.edit(f"`{KYNE_NNAME}:` **UnGbaning User !! **")

    if ungmute(user.id) is False:
        await un_gmute.edit(f"`{KYNE_NNAME}:` **Error! User probably not ungbanned.**")
    else:    	
        try:
            await un_gmute.client(
                EditBannedRequest(un_gmute.chat_id, user.id, UNBAN_RIGHTS))
        # Inform about success
            await un_gmute.edit(f"`{KYNE_NNAME}:` **Admin {my_username} UnGbanned [{user.first_name}](tg://user?id={user.id})**")
        except UserIdInvalidError:
            return await un_gmute.edit(f"`{KYNE_NNAME}:` ** unGban failed!! ** ")


            if BOTLOG:
              await un_gmute.client.send_message(
                BOTLOG_CHATID, "#UNGBAN\n"
                f"USER: [{user.first_name}](tg://user?id={user.id})\n"
                f"CHAT: {un_gmute.chat.title}(`{un_gmute.chat_id}`)")
        

@kyne.on(obsq(pattern=f"ungban(?: |$)(.*)", allow_sudo=True))
async def ungmoot(un_gmute):
    """ For .ungmute command, ungmutes the target in the userbot """
    # Admin or creator check
    me = await un_gmute.client.get_me()
    my_mention = "[{}](tg://user?id={})".format(me.first_name, me.id)
    my_username = f"@{me.username}" if me.username else my_mention
    chat = await un_gmute.get_chat()
    if un_gmute.is_private:       
       #await un_gmute.reply(f"`{KYNE_NNAME}:` **Gban user in group!!**")
       try:
            from userbot.modules.sql_helper.gmute_sql import ungmute
       except AttributeError:
            await un_gmute.reply(NO_SQL)
            return

       user, reason = await get_user_from_event(un_gmute)
       if user:
            pass
       else:
            return    
       await un_gmute.reply(f"`{KYNE_NNAME}:` **UnGbaning User !! **")
       if ungmute(user.id) is False:
           await un_gmute.reply(
            f"`{KYNE_NNAME}:`**Error! User probably already ungbanned.**")
       else:
          if reason:
              await un_gmute.reply(f"`{KYNE_NNAME}:` **Admin {my_username} UnGbanned [{user.first_name}](tg://user?id={user.id})**")
          else:
              await un_gmute.reply(f"`{KYNE_NNAME}:` **Admin {my_username} UnGbanned [{user.first_name}](tg://user?id={user.id})**")      
       return                
    # If not admin and not creator, remove user from gbanned list
    admin = chat.admin_rights
    creator = chat.creator   
    if not admin and not creator:
        try:
            from userbot.modules.sql_helper.gmute_sql import ungmute
        except AttributeError:
            await un_gmute.reply(NO_SQL)
            return

        user, reason = await get_user_from_event(un_gmute)
        if user:
            pass
        else:
            return    
        await un_gmute.reply(f"`{KYNE_NNAME}:` **unGbaning User !! **")
        if ungmute(user.id) is False:
           await un_gmute.reply(
            f"`{KYNE_NNAME}:`**Error! User probably already ungbanned.**")
        else:
          if reason:
              await un_gmute.reply(f"`{KYNE_NNAME}:` **Admin {my_username} UnGbanned [{user.first_name}](tg://user?id={user.id})**")
          else:
              await un_gmute.reply(f"`{KYNE_NNAME}:` **Admin {my_username} UnGbanned [{user.first_name}](tg://user?id={user.id})**")      
        return                

    # Check if the function running under SQL mode
    try:
        from userbot.modules.sql_helper.gmute_sql import ungmute
    except AttributeError:
        await un_gmute.reply(NO_SQL)
        return

    user = await get_user_from_event(un_gmute)
    user = user[0]
    if user:
        pass
    else:
        return

    # If pass, inform and start ungmuting
    await un_gmute.reply(f"`{KYNE_NNAME}:` **UnGbaning User !! **")

    if ungmute(user.id) is False:
        await un_gmute.reply(f"`{KYNE_NNAME}:` **Error! User probably not gbanned.**")
    else:    	
        try:
            await un_gmute.client(
                EditBannedRequest(un_gmute.chat_id, user.id, UNBAN_RIGHTS))
        # Inform about success
            await un_gmute.reply(f"`{KYNE_NNAME}:` **Admin {my_username} UnGbanned [{user.first_name}](tg://user?id={user.id})**")
        except UserIdInvalidError:
            return await un_gmute.reply(f"`{KYNE_NNAME}:` ** unGban failed!! ** ")


            if BOTLOG:
              await un_gmute.client.send_message(
                BOTLOG_CHATID, "#UNGBAN\n"
                f"USER: [{user.first_name}](tg://user?id={user.id})\n"
                f"CHAT: {un_gmute.chat.title}(`{un_gmute.chat_id}`)")
        



       
@kyne3301(outgoing=True, disable_errors=False, pattern="^!gban(?: |$)(.*)")
async def gspider(gspdr):    
    me = await gspdr.client.get_me()
    my_mention = "[{}](tg://user?id={})".format(me.first_name, me.id)
    my_username = f"@{me.username}" if me.username else my_mention
    chat = await gspdr.get_chat()
    if gspdr.is_private:       
       #await gspdr.edit(f"`{KYNE_NNAME}:` **Gban user in group!!**")
       try:
            from userbot.modules.sql_helper.gmute_sql import gmute
       except AttributeError:
            await gspdr.edit(NO_SQL)
            return

       user, reason = await get_user_from_event(gspdr)
       if user:
            pass
       else:
            return    
       await gspdr.edit(f"`{KYNE_NNAME}:` **Gbaning User !! **")
       if gmute(user.id) is False:
           await gspdr.edit(
            f"`{KYNE_NNAME}:`**Error! User probably already gbanned.**")
       else:
          if reason:
              await gspdr.edit(
                     f"`{KYNE_NNAME}:` **New Gban !! ** \n" 
                     f"`GbanAdmin`: **{my_username}**\n\n"
                     f"**Victim Name**: [{user.first_name}](tg://user?id={user.id})\n"
                     f"**Victim ID** : `{user.id}`\n"                     
                   #  f"**Chat** :  `{gspdr.chat.title}`\n"
                     f"**Reason**  : `{reason}`\n"
                     f"**Ban user **  : `False`\n"
                     f"**block user **  : `True`\n"
                     f"**Report user **  : `True`\n"
                     f"**Add user gban list **  : `True`\n")
                    
          else:
              await gspdr.edit(
                     f"`{KYNE_NNAME}:` **New Gban !! ** \n" 
                     f"`GbanAdmin`: **{my_username}**\n\n"
                     f"**Victim Name**: [{user.first_name}](tg://user?id={user.id})\n"
                     f"**Victim ID** : `{user.id}`\n"                     
                     #f"**Chat** :  `{gspdr.chat.title}`\n"
                     f"**Reason**  : `Private!`\n"
                     f"**Ban user **  : `False`\n"
                     f"**block user **  : `True`\n"
                     f"**Report user **  : `True`\n"
                     f"**Add user gban list **  : `True`\n")       
       return                
    admin = chat.admin_rights
    creator = chat.creator   
    # If not admin and not creator add user in gban list
    if not admin and not creator:
        try:
            from userbot.modules.sql_helper.gmute_sql import gmute
        except AttributeError:
            await gspdr.edit(NO_SQL)
            return

        user, reason = await get_user_from_event(gspdr)
        if user:
            pass
        else:
            return    
        await gspdr.edit(f"`{KYNE_NNAME}:` **Gbaning User !! **")
        if gmute(user.id) is False:
           await gspdr.edit(
            f"`{KYNE_NNAME}:`**Error! User probably already gbanned.**")
        else:
          if reason:
              await gspdr.edit(
                     f"`{KYNE_NNAME}:` **New Gban !! ** \n" 
                     f"`GbanAdmin`: **{my_username}**\n\n"
                     f"**Victim Name**: [{user.first_name}](tg://user?id={user.id})\n"
                     f"**Victim ID** : `{user.id}`\n"                     
                     f"**Chat** :  `{gspdr.chat.title}`\n"
                     f"**Reason**  : `{reason}`\n"
                     f"**Ban user **  : `False`\n"
                     f"**block user **  : `True`\n"
                     f"**Report user **  : `True`\n"
                     f"**Add user gban list **  : `True`\n")
          else:
              await gspdr.edit(
                     f"`{KYNE_NNAME}:` **New Gban !! ** \n" 
                     f"`GbanAdmin`: **{my_username}**\n\n"
                     f"**Victim Name**: [{user.first_name}](tg://user?id={user.id})\n"
                     f"**Victim ID** : `{user.id}`\n"                     
                     f"**Chat** :  `{gspdr.chat.title}`\n"
                     f"**Reason**  : `Private!`\n"
                     f"**Ban user **  : `False`\n"
                     f"**block user **  : `True`\n"
                     f"**Report user **  : `True`\n"
                     f"**Add user gban list **  : `True`\n")
        return    
    try:
        from userbot.modules.sql_helper.gmute_sql import gmute
    except AttributeError:
        await gspdr.edit(NO_SQL)
        return

    user, reason = await get_user_from_event(gspdr)
    if user:
        pass
    else:
        return

    # If pass, inform and start gmuting
    await gspdr.edit(f"`{KYNE_NNAME}:` **Gbaning User !! **")
    if gmute(user.id) is False:
        await gspdr.edit(
            f"`{KYNE_NNAME}:`**Error! User probably already gmuted.**")
    else:    	
        try:
            await gspdr.client(
                EditBannedRequest(gspdr.chat_id, user.id, BANNED_RIGHTS))          
            if reason:
               await gspdr.edit(
                     f"`{KYNE_NNAME}:` **New Gban !! ** \n" 
                     f"`GbanAdmin`: **{my_username}**\n\n"
                     f"**Victim Name**: [{user.first_name}](tg://user?id={user.id})\n"
                     f"**Victim ID** : `{user.id}`\n"                     
                     f"**Chat** :  `{gspdr.chat.title}`\n"
                     f"**Reason**  : `{reason}`\n"
                     f"**Ban user **  : `True`\n"
                     f"**block user **  : `True`\n"
                     f"**Report user **  : `True`\n"
                     f"**Add user gban list **  : `True`\n")
                     
            else:
                  await gspdr.edit(
                     f"`{KYNE_NNAME}:` **New Gban !! ** \n" 
                     f"`GbanAdmin`: **{my_username}**\n\n"
                     f"**Victim Name**: [{user.first_name}](tg://user?id={user.id})\n"
                     f"**Victim ID** : `{user.id}`\n"                     
                     f"**Chat** :  `{gspdr.chat.title}`\n"
                     f"**Reason**  : `Private!`\n"
                     f"**Ban user **  : `True`\n"
                     f"**block user **  : `True`\n"
                     f"**Report user **  : `True`\n"
                     f"**Add user gban list **  : `True`\n")
            if BOTLOG:
                  await gspdr.client.send_message(
                     BOTLOG_CHATID, "#GBAN\n"
                        f"USER: [{user.first_name}](tg://user?id={user.id})\n"
                        f"CHAT: {gspdr.chat.title}(`{gspdr.chat_id}`)")
        except UserIdInvalidError:
            return await gspdr.edit(f"`{KYNE_NNAME}:` ** Gban failed!! ** ")

@kyne.on(obsq(pattern=f"gban(?: |$)(.*)", allow_sudo=True))
async def gspider(gspdr):    
    me = await gspdr.client.get_me()
    my_mention = "[{}](tg://user?id={})".format(me.first_name, me.id)
    my_username = f"@{me.username}" if me.username else my_mention
    chat = await gspdr.get_chat()
    if gspdr.is_private:       
       #await gspdr.reply(f"`{KYNE_NNAME}:` **Gban user in group!!**")
       try:
            from userbot.modules.sql_helper.gmute_sql import gmute
       except AttributeError:
            await gspdr.reply(NO_SQL)
            return

       user, reason = await get_user_from_event(gspdr)
       if user:
            pass
       else:
            return    
       await gspdr.reply(f"`{KYNE_NNAME}:` **Gbaning User !! **")
       if gmute(user.id) is False:
           await gspdr.reply(
            f"`{KYNE_NNAME}:`**Error! User probably already gbanned.**")
       else:
          if reason:
              await gspdr.reply(
                     f"`{KYNE_NNAME}:` **New Gban !! ** \n" 
                     f"`GbanAdmin`: **{my_username}**\n\n"
                     f"**Victim Name**: [{user.first_name}](tg://user?id={user.id})\n"
                     f"**Victim ID** : `{user.id}`\n"                     
                   #  f"**Chat** :  `{gspdr.chat.title}`\n"
                     f"**Reason**  : `{reason}`\n"
                     f"**Ban user **  : `False`\n"
                     f"**block user **  : `True`\n"
                     f"**Report user **  : `True`\n"
                     f"**Add user gban list **  : `True`\n")
                    
          else:
              await gspdr.reply(
                     f"`{KYNE_NNAME}:` **New Gban !! ** \n" 
                     f"`GbanAdmin`: **{my_username}**\n\n"
                     f"**Victim Name**: [{user.first_name}](tg://user?id={user.id})\n"
                     f"**Victim ID** : `{user.id}`\n"                     
                     #f"**Chat** :  `{gspdr.chat.title}`\n"
                     f"**Reason**  : `Private!`\n"
                     f"**Ban user **  : `False`\n"
                     f"**block user **  : `True`\n"
                     f"**Report user **  : `True`\n"
                     f"**Add user gban list **  : `True`\n")       
       return                
    admin = chat.admin_rights
    creator = chat.creator   
    # If not admin and not creator add user in gban list
    if not admin and not creator:
        try:
            from userbot.modules.sql_helper.gmute_sql import gmute
        except AttributeError:
            await gspdr.reply(NO_SQL)
            return

        user, reason = await get_user_from_event(gspdr)
        if user:
            pass
        else:
            return    
        await gspdr.reply(f"`{KYNE_NNAME}:` **Gbaning User !! **")
        if gmute(user.id) is False:
           await gspdr.reply(
            f"`{KYNE_NNAME}:`**Error! User probably already gbanned.**")
        else:
          if reason:
              await gspdr.reply(
                     f"`{KYNE_NNAME}:` **New Gban !! ** \n" 
                     f"`GbanAdmin`: **{my_username}**\n\n"
                     f"**Victim Name**: [{user.first_name}](tg://user?id={user.id})\n"
                     f"**Victim ID** : `{user.id}`\n"                     
                     f"**Chat** :  `{gspdr.chat.title}`\n"
                     f"**Reason**  : `{reason}`\n"
                     f"**Ban user **  : `False`\n"
                     f"**block user **  : `True`\n"
                     f"**Report user **  : `True`\n"
                     f"**Add user gban list **  : `True`\n")
          else:
              await gspdr.reply(
                     f"`{KYNE_NNAME}:` **New Gban !! ** \n" 
                     f"`GbanAdmin`: **{my_username}**\n\n"
                     f"**Victim Name**: [{user.first_name}](tg://user?id={user.id})\n"
                     f"**Victim ID** : `{user.id}`\n"                     
                     f"**Chat** :  `{gspdr.chat.title}`\n"
                     f"**Reason**  : `Private!`\n"
                     f"**Ban user **  : `False`\n"
                     f"**block user **  : `True`\n"
                     f"**Report user **  : `True`\n"
                     f"**Add user gban list **  : `True`\n")
        return    
    try:
        from userbot.modules.sql_helper.gmute_sql import gmute
    except AttributeError:
        await gspdr.reply(NO_SQL)
        return

    user, reason = await get_user_from_event(gspdr)
    if user:
        pass
    else:
        return

    # If pass, inform and start gmuting
    await gspdr.reply(f"`{KYNE_NNAME}:` **Gbaning User !! **")
    if gmute(user.id) is False:
        await gspdr.reply(
            f"`{KYNE_NNAME}:`**Error! User probably already gmuted.**")
    else:    	
        try:
            await gspdr.client(
                EditBannedRequest(gspdr.chat_id, user.id, BANNED_RIGHTS))          
            if reason:
               await gspdr.reply(
                     f"`{KYNE_NNAME}:` **New Gban !! ** \n" 
                     f"`GbanAdmin`: **{my_username}**\n\n"
                     f"**Victim Name**: [{user.first_name}](tg://user?id={user.id})\n"
                     f"**Victim ID** : `{user.id}`\n"                     
                     f"**Chat** :  `{gspdr.chat.title}`\n"
                     f"**Reason**  : `{reason}`\n"
                     f"**Ban user **  : `True`\n"
                     f"**block user **  : `True`\n"
                     f"**Report user **  : `True`\n"
                     f"**Add user gban list **  : `True`\n")
                     
            else:
                  await gspdr.reply(
                     f"`{KYNE_NNAME}:` **New Gban !! ** \n" 
                     f"`GbanAdmin`: **{my_username}**\n\n"
                     f"**Victim Name**: [{user.first_name}](tg://user?id={user.id})\n"
                     f"**Victim ID** : `{user.id}`\n"                     
                     f"**Chat** :  `{gspdr.chat.title}`\n"
                     f"**Reason**  : `Private!`\n"
                     f"**Ban user **  : `True`\n"
                     f"**block user **  : `True`\n"
                     f"**Report user **  : `True`\n"
                     f"**Add user gban list **  : `True`\n")
            if BOTLOG:
                  await gspdr.client.send_message(
                     BOTLOG_CHATID, "#GBAN\n"
                        f"USER: [{user.first_name}](tg://user?id={user.id})\n"
                        f"CHAT: {gspdr.chat.title}(`{gspdr.chat_id}`)")
        except UserIdInvalidError:
            return await gspdr.reply(f"`{KYNE_NNAME}:` ** Gban failed!! ** ")



@kyne3301(outgoing=True, disable_errors=True, pattern="^\!delusers(?: |$)(.*)", groups_only=True)
async def rm_deletedacc(show):
    """ For .delusers command, list all the ghost/deleted accounts in a chat. """
    if not show.is_group:
        await show.edit(f"`{KYNE_NNAME}:` ** This is not a group.**")
        return
    con = show.pattern_match.group(1).lower()
    del_u = 0
    del_status = f"`{KYNE_NNAME}:` **No deleted accounts found**"

    if con != "clean":
        await show.edit(f"`{KYNE_NNAME}:` ** Searching for deleted accounts...**")
        async for user in show.client.iter_participants(show.chat_id):
            if user.deleted:
                del_u += 1
                await sleep(1)
        if del_u > 0:
            del_status = f"`{KYNE_NNAME}:` Found **{del_u}** deleted account(s) in this group,\
            \nclean them by using `!delusers clean`"

        await show.edit(del_status)
        return

    # Here laying the sanity check
    chat = await show.get_chat()
    admin = chat.admin_rights
    creator = chat.creator

    # Well
    if not admin and not creator:
        await show.edit(f"`{KYNE_NNAME}:` **Sorry,  I can't able to get admin rights here**")
        return

    await show.edit(f"`{KYNE_NNAME}:` ** Removing deleted accounts...**")
    del_u = 0
    del_a = 0

    async for user in show.client.iter_participants(show.chat_id):
        if user.deleted:
            try:
                await show.client(
                    EditBannedRequest(show.chat_id, user.id, BANNED_RIGHTS))
            except ChatAdminRequiredError:
                await show.edit(f"`{KYNE_NNAME}:` **Sorry, I don't have ban rights in this group")
                return
            except UserAdminInvalidError:
                del_u -= 1
                del_a += 1
            await show.client(
                EditBannedRequest(show.chat_id, user.id, UNBAN_RIGHTS))
            del_u += 1

    if del_u > 0:
        del_status = f"`{KYNE_NNAME}`: Cleaned **{del_u}** deleted account(s)"

    if del_a > 0:
        del_status = f"`{KYNE_NNAME}`: Cleaned **{del_u}** deleted account(s) \
        \n**{del_a}** deleted admin accounts are not removed"

    await show.edit(del_status)
    await sleep(2)
    await show.delete()

    if BOTLOG:
        await show.client.send_message(
            BOTLOG_CHATID, "#CLEANUP\n"
            f"Cleaned **{del_u}** deleted account(s) !!\
            \nCHAT: {show.chat.title}(`{show.chat_id}`)")
