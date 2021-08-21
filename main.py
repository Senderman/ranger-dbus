import subprocess

from gi.repository import GLib
from pydbus import SessionBus

# change this variable if you are using another terminal emulator
terminal_cmd = 'st'


class RangerService(object):
    """
        <node>
            <interface name='org.freedesktop.FileManager1'>
                <method name='ShowFolders'>
                    <arg type='as' name='URIs' direction='in'/>
                    <arg type='s' name='StartupId' direction='in'/>
                </method>
                <method name='ShowItems'>
                    <arg type='as' name='URIs' direction='in'/>
                    <arg type='s' name='StartupId' direction='in'/>
                </method>
                <method name='ShowItemProperties'>
                    <arg type='as' name='URIs' direction='in'/>
                    <arg type='s' name='StartupId' direction='in'/>
                </method>
            </interface>
        </node>
    """

    def ShowFolders(self, uris, startup_id):
        uri = format_uri(uris[0])
        subprocess.Popen([terminal_cmd, 'ranger', uri])

    def ShowItems(self, uris, startup_id):
        uri = format_uri(uris[0])
        subprocess.Popen([terminal_cmd, 'ranger', '--select', uri])

    def ShowItemProperties(self, uris, startup_id):
        self.ShowItems(uris, startup_id)


def format_uri(uri: str):
    return uri.replace('file://', '').replace('%20', ' ')


session_bus = SessionBus()
session_bus.publish('org.freedesktop.FileManager1', RangerService())
loop = GLib.MainLoop()
loop.run()
