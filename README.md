# Ranger DBus Service

## Use ranger as org.freedesktop.FileManager to open files and directories in it

### Installation

#### Install dependencies:

**Debian/Ubuntu:**

`sudo apt install libgirepository1.0-dev gcc libcairo2-dev pkg-config python3-dev gir1.2-gtk-3.0`

**Fedora:**

`sudo dnf install gcc gobject-introspection-devel cairo-devel pkg-config python3-devel gtk3`

**ArchLinux:**

`sudo pacman -S python cairo pkgconf gobject-introspection gtk3`

**OpenSUSE:**

`sudo zypper install cairo-devel pkg-config python3-devel gcc gobject-introspection-devel`

#### Install python dependencies:

Run `./install.sh`

### Configuration

Change the `terminal_cmd` variable to whatever you use, for example if you're using gnome-terminal:
`terminal_cmd=['gnome-terminal', '-x']`

### Running

`setsid -f ./run.sh`

You can also add this script to run it at start to ~/.xprofile or ~/.xinitrc, for example

`$HOME/python-scripts/ranger-dbus/run.sh &`
