#!/usr/bin/python

import git

data = [
  {
    "name": "foxmagiskmodulemanager",
    "url": "https://github.com/Fox2Code/FoxMagiskModuleManager"
  },
  {
    "name": "croc",
    "url": "https://github.com/schollz/croc"
  },
  {
    "name": "tldr",
    "url": "https://github.com/tldr-pages/tldr"
  },
  {
    "name": "crocgui",
    "url": "https://github.com/howeyc/crocgui"
  },
  {
    "name": "srv",
    "url": "https://github.com/joshuarli/srv"
  },
  {
    "name": "caddy-ftp",
    "url": "https://github.com/n0trace/caddy-ftp"
  },
  {
    "name": "rpcs3",
    "url": "https://github.com/RPCS3/rpcs3"
  },
  {
    "name": "diff-so-fancy",
    "url": "https://github.com/so-fancy/diff-so-fancy"
  },
  {
    "name": "gogs",
    "url": "https://github.com/gogs/gogs"
  },
  {
    "name": "telegram-foss",
    "url": "https://github.com/Telegram-FOSS-Team/Telegram-FOSS"
  },
  {
    "name": "jtar",
    "url": "https://github.com/topjohnwu/jtar"
  },
  {
    "name": "libsu",
    "url": "https://github.com/topjohnwu/libsu"
  },
  {
    "name": "magisk",
    "url": "https://github.com/topjohnwu/Magisk"
  },
  {
    "name": "magisk-files",
    "url": "https://github.com/topjohnwu/magisk-files"
  },
  {
    "name": "restsms",
    "url": "https://github.com/Xcreen/RestSMS"
  },
  {
    "name": "simplert",
    "url": "https://github.com/robinpaulson/SimpleRT"
  },
  {
    "name": "simple-notes",
    "url": "https://github.com/RafhaanShah/Simple-Notes"
  },
  {
    "name": "ariang",
    "url": "https://github.com/mayswind/AriaNg"
  },
  {
    "name": "termux-exec",
    "url": "https://github.com/termux/termux-exec"
  },
  {
    "name": "android-shell-scripts",
    "url": "https://github.com/sujaydavalgi/android-shell-scripts"
  },
  {
    "name": "awesome-ssh",
    "url": "https://github.com/moul/awesome-ssh"
  },
  {
    "name": "sophiapp",
    "url": "https://github.com/Sophia-Community/SophiApp"
  },
  {
    "name": "jumpfm",
    "url": "https://github.com/JumpFm/jumpfm"
  },
  {
    "name": "fastforward",
    "url": "https://github.com/FastForwardTeam/FastForward"
  },
  {
    "name": "softx",
    "url": "https://github.com/DiscordStyles/SoftX"
  },
  {
    "name": "gtkcord3",
    "url": "https://github.com/diamondburned/gtkcord3"
  },
  {
    "name": "holehe",
    "url": "https://github.com/megadose/holehe"
  },
  {
    "name": "css",
    "url": "https://github.com/primer/css"
  },
  {
    "name": "bd-scss",
    "url": "https://github.com/Gibbu/bd-scss"
  },
  {
    "name": "create-cert",
    "url": "https://github.com/lukechilds/create-cert"
  },
  {
    "name": "s",
    "url": "https://github.com/grobertson/s"
  },
  {
    "name": "audacium",
    "url": "https://github.com/SartoxSoftware/audacium"
  },
  {
    "name": "zrythm",
    "url": "https://git.sr.ht/~alextee/zrythm"
  },
  {
    "name": "foxmagiskmodulemanager",
    "url": "https://github.com/Fox2Code/FoxMagiskModuleManager"
  },
  {
    "name": "croc",
    "url": "https://github.com/schollz/croc"
  },
  {
    "name": "tldr",
    "url": "https://github.com/tldr-pages/tldr"
  },
  {
    "name": "crocgui",
    "url": "https://github.com/howeyc/crocgui"
  },
  {
    "name": "srv",
    "url": "https://github.com/joshuarli/srv"
  },
  {
    "name": "caddy-ftp",
    "url": "https://github.com/n0trace/caddy-ftp"
  },
  {
    "name": "rpcs3",
    "url": "https://github.com/RPCS3/rpcs3"
  },
  {
    "name": "diff-so-fancy",
    "url": "https://github.com/so-fancy/diff-so-fancy"
  },
  {
    "name": "gogs",
    "url": "https://github.com/gogs/gogs"
  },
  {
    "name": "telegram-foss",
    "url": "https://github.com/Telegram-FOSS-Team/Telegram-FOSS"
  },
  {
    "name": "jtar",
    "url": "https://github.com/topjohnwu/jtar"
  },
  {
    "name": "libsu",
    "url": "https://github.com/topjohnwu/libsu"
  },
  {
    "name": "magisk",
    "url": "https://github.com/topjohnwu/Magisk"
  },
  {
    "name": "magisk-files",
    "url": "https://github.com/topjohnwu/magisk-files"
  },
  {
    "name": "restsms",
    "url": "https://github.com/Xcreen/RestSMS"
  },
  {
    "name": "simplert",
    "url": "https://github.com/robinpaulson/SimpleRT"
  },
  {
    "name": "simple-notes",
    "url": "https://github.com/RafhaanShah/Simple-Notes"
  },
  {
    "name": "ariang",
    "url": "https://github.com/mayswind/AriaNg"
  },
  {
    "name": "termux-exec",
    "url": "https://github.com/termux/termux-exec"
  },
  {
    "name": "android-shell-scripts",
    "url": "https://github.com/sujaydavalgi/android-shell-scripts"
  },
  {
    "name": "awesome-ssh",
    "url": "https://github.com/moul/awesome-ssh"
  },
  {
    "name": "sophiapp",
    "url": "https://github.com/Sophia-Community/SophiApp"
  },
  {
    "name": "jumpfm",
    "url": "https://github.com/JumpFm/jumpfm"
  },
  {
    "name": "fastforward",
    "url": "https://github.com/FastForwardTeam/FastForward"
  },
  {
    "name": "softx",
    "url": "https://github.com/DiscordStyles/SoftX"
  },
  {
    "name": "gtkcord3",
    "url": "https://github.com/diamondburned/gtkcord3"
  },
  {
    "name": "holehe",
    "url": "https://github.com/megadose/holehe"
  },
  {
    "name": "css",
    "url": "https://github.com/primer/css"
  },
  {
    "name": "bd-scss",
    "url": "https://github.com/Gibbu/bd-scss"
  },
  {
    "name": "create-cert",
    "url": "https://github.com/lukechilds/create-cert"
  },
  {
    "name": "s",
    "url": "https://github.com/grobertson/s"
  },
  {
    "name": "audacium",
    "url": "https://github.com/SartoxSoftware/audacium"
  }
]

repos_dir = "repos"

if __name__ == '__main__':
    print("Preparing to clone " + str(len(data)) + " repo(s)..")
    for entry in data:
        try:
            print(f"Cloning {entry['name']}\nfrom {entry['url']}\nto {repos_dir}")
            git.Repo.clone_from(entry["url"], repos_dir + "/" + entry["name"])
        except git.exc.GitError as e:
            print("Error while cloning " + entry["name"])
