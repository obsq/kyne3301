from datetime import datetime
from random import randint
from asyncio import sleep
from os import execl
import sys
import os
from userbot import bot
from userbot.events import admin_cmd, command
import io
import heroku3
from userbot import CMD_HELP, ALIVE_NAME, PM_MESSAGE, KYNE_NAME, KYNE_MSG, ORI_MSG
import asyncio
from asyncio import create_subprocess_shell as asyncSubprocess
from asyncio.subprocess import PIPE as asyncPIPE
from userbot import CMD_HELP, LOGS, HEROKU_APPNAME, HEROKU_APIKEY
import sys
import json
from userbot import BOTLOG, BOTLOG_CHATID, CMD_HELP, bot, UPSTREAM_REPO_URL
from speedtest import Speedtest
from telethon import functions
from os import remove, execle, path, makedirs, getenv, environ
from shutil import rmtree
import asyncio
import json
from asyncio import sleep
from telethon.errors import rpcbaseerrors
from userbot import BOTLOG, BOTLOG_CHATID, CMD_HELP
import os
import subprocess
import time
import math
from pySmartDL import SmartDL
import asyncio
from hachoir.metadata import extractMetadata
from hachoir.parser import createParser
from telethon.tl.types import DocumentAttributeVideo
from userbot import LOGS, CMD_HELP, TEMP_DOWNLOAD_DIRECTORY
import sys
from git import Repo
from git.exc import GitCommandError, InvalidGitRepositoryError, NoSuchPathError
from userbot import CMD_HELP, bot, HEROKU_APIKEY, HEROKU_APPNAME, UPSTREAM_REPO_URL
from userbot import CMD_HELP, LOGS, HEROKU_APP_NAME, HEROKU_API_KEY
from asyncio import create_subprocess_shell as asyncrunapp
from asyncio.subprocess import PIPE as asyncPIPE
from platform import python_version, uname
from shutil import which
from os import remove
from telethon import version
from userbot import CMD_HELP, ALIVE_NAME
from userbot.events import kyne3301
import heroku3
import asyncio
import os
import requests
import math

from userbot import CMD_HELP, HEROKU_APP_NAME, HEROKU_API_KEY
from userbot.events import kyne3301
from userbot.prettyjson import prettyjson
from userbot import CMD_HELP, ALIVE_NAME, PM_MESSAGE, KYNE_NAME, KYNE_MSG, ORI_MSG, ALIVE_S_MESSAGE, ALIVE_E_MESSAGE, ALIVE_S_MSG, ALIVE_E_MSG
Heroku = heroku3.from_key(HEROKU_API_KEY)
heroku_api = "https://api.heroku.com"


# ================= CONSTANT =================
KYNE_NNAME = str(KYNE_NAME) if KYNE_NAME else str(KYNE_MSG)
ALIVE_S_MMSG = str(ALIVE_S_MESSAGE) if ALIVE_S_MESSAGE else str(ALIVE_S_MSG)
ALIVE_E_MMSG = str(ALIVE_E_MESSAGE) if ALIVE_E_MESSAGE else str(ALIVE_E_MSG)
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else uname().node
# ============================================

Heroku = heroku3.from_key(HEROKU_API_KEY)


async def subprocess_run(cmd, heroku):
    subproc = await asyncSubprocess(cmd, stdout=asyncPIPE, stderr=asyncPIPE)
    stdout, stderr = await subproc.communicate()
    exitCode = subproc.returncode
    if exitCode != 0:
        await heroku.edit(
            '**An error was detected while running subprocess**\n'
            f'```exitCode: {exitCode}\n'
            f'stdout: {stdout.decode().strip()}\n'
            f'stderr: {stderr.decode().strip()}```')
        return exitCode
    return stdout.decode().strip(), stderr.decode().strip(), exitCode



@kyne3301(outgoing=True, pattern=r"^!heroku(?: |$)(.*)")
async def heroku_manager(heroku):
    await heroku.edit("`Processing...`")
    await asyncio.sleep(3)
    conf = heroku.pattern_match.group(1)
    result = await subprocess_run(f'heroku ps -a {HEROKU_APP_NAME}', heroku)
    if result[2] != 0:
        return
    hours_remaining = result[0]
    await heroku.edit('`' + hours_remaining + '`')
    return



@kyne3301(outgoing=True, pattern="^\!sysd$")
async def sysdetails(sysd):
    """ For .sysd command, get system info using neofetch. """
    try:
        neo = "neofetch --stdout"
        fetch = await asyncrunapp(
            neo,
            stdout=asyncPIPE,
            stderr=asyncPIPE,
        )

        stdout, stderr = await fetch.communicate()
        result = str(stdout.decode().strip()) \
            + str(stderr.decode().strip())

        await sysd.edit("`" + result + "`")
    except FileNotFoundError:
        await sysd.edit("`Install neofetch first !!`")





@kyne3301(outgoing=True, pattern="^\!pip(?: |$)(.*)")
async def pipcheck(pip):
    """ For .pip command, do a pip search. """
    pipmodule = pip.pattern_match.group(1)
    if pipmodule:
        await pip.edit("`Searching . . .`")
        invokepip = f"pip3 search {pipmodule}"
        pipc = await asyncrunapp(
            invokepip,
            stdout=asyncPIPE,
            stderr=asyncPIPE,
        )

        stdout, stderr = await pipc.communicate()
        pipout = str(stdout.decode().strip()) \
            + str(stderr.decode().strip())

        if pipout:
            if len(pipout) > 4096:
                await pip.edit("`Output too large, sending as file`")
                file = open("output.txt", "w+")
                file.write(pipout)
                file.close()
                await pip.client.send_file(
                    pip.chat_id,
                    "output.txt",
                    reply_to=pip.id,
                )
                remove("output.txt")
                return
            await pip.edit("**Query: **\n`"
                           f"{invokepip}"
                           "`\n**Result: **\n`"
                           f"{pipout}"
                           "`")
        else:
            await pip.edit("**Query: **\n`"
                           f"{invokepip}"
                           "`\n**Result: **\n`No Result Returned/False`")
    else:
        await pip.edit("`Use .help pip to see an example`")


@kyne3301(outgoing=True, pattern="^\!kyne$")
async def amireallyalive(alive):
    """ For .kyne command, check if the bot is running.  """
    await alive.edit(""
                    f" **{ALIVE_S_MMSG}**\n" 
                    f"---------------------------\n"
                    f"  >`{KYNE_NNAME}`: ** 2.5.1**\n"
                    f"  >`Telethon`: ** {version.__version__} **\n"
                    f"  >`Python` : ** {python_version()} **\n"
                    f"  >`User:` ** {DEFAULTUSER} **\n"
                    f"---------------------------\n"
                    f" **{ALIVE_E_MMSG}**")




@bot.on(admin_cmd(pattern=f"sudo$", allow_sudo=True))
async def iqless(e):
    await e.reply(""
                    f" **Hello Sir Iam Alive!**\n" 
                    f"---------------------------\n"
                    f"  >`{KYNE_NNAME}`: ** 2.5.1**\n"
                    f"  >`Telethon`: ** {version.__version__} **\n"
                    f"  >`Python` : ** {python_version()} **\n"
                    f"  >`User:` ** Sudo **\n"
                    f"---------------------------")








requirements_path = path.join(
    path.dirname(path.dirname(path.dirname(__file__))), 'requirements.txt')


async def gen_chlog(repo, diff):
    ch_log = ''
    d_form = "%d/%m/%y"
    for c in repo.iter_commits(diff):
        ch_log += f'•[{c.committed_datetime.strftime(d_form)}]: {c.summary} <{c.author}>\n'
    return ch_log


async def update_requirements():
    reqs = str(requirements_path)
    try:
        process = await asyncio.create_subprocess_shell(
            ' '.join([sys.executable, "-m", "pip", "install", "-r", reqs]),
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE)
        await process.communicate()
        return process.returncode
    except Exception as e:
        return repr(e)


@kyne3301(outgoing=True, pattern="^\!update(?: |$)(.*)")
async def upstream(ups):
    "For .update command, check if the bot is up to date, update if specified"
    await ups.edit("`Checking for updates, please wait....`")
    conf = ups.pattern_match.group(1)
    off_repo = UPSTREAM_REPO_URL
    force_update = False

    try:
        txt = "`Oops.. Updater cannot continue "
        txt += "please add heroku apikey, name`\n\n**LOGTRACE:**\n"
        repo = Repo()
    except NoSuchPathError as error:
        await ups.edit(f'{txt}\n`directory {error} is not found`')
        repo.__del__()
        return
    except GitCommandError as error:
        await ups.edit(f'{txt}\n`Early failure! {error}`')
        repo.__del__()
        return
    except InvalidGitRepositoryError as error:
        if conf != "now":
            await ups.edit(
                f"`Unfortunately, the directory {error} does not seem to be a git repository.\
            \nBut we can fix that by force updating the userbot using .update now.`"
            )
            return
        repo = Repo.init()
        origin = repo.create_remote('upstream', off_repo)
        origin.fetch()
        force_update = True
        repo.create_head('master', origin.refs.master)
        repo.heads.master.set_tracking_branch(origin.refs.master)
        repo.heads.master.checkout(True)

    ac_br = repo.active_branch.name
    if ac_br != 'master':
        await ups.edit(
            f'**[UPDATER]:**` Looks like you are using your own custom branch ({ac_br}). '
            'in that case, Updater is unable to identify '
            'which branch is to be merged. '
            'please checkout to any official branch`')
        repo.__del__()
        return

    try:
        repo.create_remote('upstream', off_repo)
    except BaseException:
        pass

    ups_rem = repo.remote('upstream')
    ups_rem.fetch(ac_br)

    changelog = await gen_chlog(repo, f'HEAD..upstream/{ac_br}')

    if not changelog and not force_update:
        await ups.edit(
            f'\n`{KYNE_NNAME} is`  **up-to-date**  \n')
        repo.__del__()
        return

    if conf != "now" and not force_update:
        changelog_str = f'**New UPDATE available for {KYNE_NNAME}\n\nCHANGELOG:**\n`{changelog}`'
        if len(changelog_str) > 4096:
            await ups.edit("`Changelog is too big, view the file to see it.`")
            file = open("output.txt", "w+")
            file.write(changelog_str)
            file.close()
            await ups.client.send_file(
                ups.chat_id,
                "output.txt",
                reply_to=ups.id,
            )
            remove("output.txt")
        else:
            await ups.edit(changelog_str)
        await ups.respond('`do \"!update now\" to update`')
        return

    if force_update:
        await ups.edit(
            '`Force-Syncing to latest stable userbot code, please wait...`')
    else:
        await ups.edit('`Finiding your heroku app.....`')
    # We're in a Heroku Dyno, handle it's memez.
    if HEROKU_APIKEY is not None:
        import heroku3
        heroku = heroku3.from_key(HEROKU_APIKEY)
        heroku_app = None
        heroku_applications = heroku.apps()
        if not HEROKU_APPNAME:
            await ups.edit(
                '`Please set up the HEROKU_APPNAME variable to be able to update userbot.`'
            )
            repo.__del__()
            return
        for app in heroku_applications:
            if app.name == HEROKU_APPNAME:
                heroku_app = app
                break
        if heroku_app is None:
            await ups.edit(
                f'{txt}\n`Invalid Heroku credentials for updating userbot dyno.`'
            )
            repo.__del__()
            return
        await ups.edit(f'`[Updater]\
                        {KYNE_NNAME} dyno build in progress, please wait for it to complete.\nIt may take 7 minutes `'
                       )
        ups_rem.fetch(ac_br)
        repo.git.reset("--hard", "FETCH_HEAD")
        heroku_git_url = heroku_app.git_url.replace(
            "https://", "https://api:" + HEROKU_APIKEY + "@")
        if "heroku" in repo.remotes:
            remote = repo.remote("heroku")
            remote.set_url(heroku_git_url)
        else:
            remote = repo.create_remote("heroku", heroku_git_url)
        try:
            remote.push(refspec="HEAD:refs/heads/master", force=True)
        except GitCommandError as error:
            await ups.edit(f'{txt}\n`Here is the error log:\n{error}`')
            repo.__del__()
            return
        await ups.edit('Successfully Updated!\n'
                       'Restarting.......')
    else:
        # Classic Updater, pretty straightforward.
        try:
            ups_rem.pull(ac_br)
        except GitCommandError:
            repo.git.reset("--hard", "FETCH_HEAD")
        reqs_upgrade = await update_requirements()
        await ups.edit('`Successfully Updated!\n'
                       'restarting......`')
        # Spin a new instance of bot
        args = [sys.executable, "-m", "userbot"]
        execle(sys.executable, *args, environ)
        return
