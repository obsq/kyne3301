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
