# elementary-nightly-rpms

I use this repository to keep track of files related to packaging / building
nightly snapshots of elementaryOS / pantheon desktop components and applications
for fedora.


## Package Status

The current build status can be seen at
<https://copr.fedorainfracloud.org/coprs/decathorpe/elementary-nightly/monitor/>.


### official elementary apps

| package name                 | f28  | f29  | rawhide |
| ---------------------------- | ---- | ---- | ------- |
| [appcenter]                  | DONE | DONE | DONE    |
| [elementary-calculator]      | ---- | DONE | DONE    |
| [elementary-calendar]        | ---- | DONE | DONE    |
| [elementary-camera]          | ---- | DONE | DONE    |
| [elementary-code]            | ---- | DONE | DONE    |
| [elementary-files]           | ---- | DONE | DONE    |
| [elementary-mail]            | ---- | DONE | DONE    |
| [elementary-music]           | ---- | DONE | DONE    |
| [elementary-photos]          | ---- | DONE | DONE    |
| [elementary-screenshot-tool] | ---- | DONE | DONE    |
| [elementary-terminal]        | ---- | DONE | DONE    |
| [elementary-videos]          | ---- | DONE | DONE    |
| [switchboard]                | DONE | DONE | DONE    |


### Pantheon desktop

| package name                | f28  | f29  | rawhide |
| --------------------------- | ---- | ---- | ------- |
| [cerbere]                   | ---- | ---- | ------- |
| [contractor]                | DONE | DONE | DONE    |
| [elementary-capnet-assist]  | DONE | DONE | DONE    |
| [elementary-dpms-helper]    | DONE | DONE | DONE    |
| [elementary-greeter]        | DONE | DONE | DONE    |
| [gala]                      | DONE | DONE | DONE    |
| [pantheon-agent-geoclue2]   | DONE | DONE | DONE    |
| [pantheon-agent-polkit]     | DONE | DONE | DONE    |
| [pantheon-session-settings] | ---- | ---- | ------- |
| [plank]                     | DONE | DONE | DONE    |
| [wingpanel]                 | DONE | DONE | DONE    |

`cerbere` is currently not built for the nightly repository due to differences
between the currently supported fedora releases and rawhide. However, the latest
version of `cerbere` from the official fedora repositories should be recent
enough.

`greeter` currently doesn't compile on fedora rawhide due to missing support for
the latest releases of mutter (`>= 3.29`).

`pantheon-session-settings` is a sensitive component that has to be tailored
specifically to every fedora release, so there are no nightly builds for it.


### elementary artwork

| package name            | f28  | f29  | rawhide |
| ----------------------- | ---- | ---- | ------- |
| [elementary-icon-theme] | DONE | DONE | DONE    |
| [elementary-theme]      | DONE | DONE | DONE    |
| [elementary-wallpapers] | ---- | ---- | ------- |

`elementary-wallpapers` is a project that changes very rarely, and has regular
releases, so nightly builds are not necessary.


### switchboard plugs

| package name                         | f28  | f29  | rawhide |
| ------------------------------------ | ---- | ---- | ------- |
| [switchboard-plug-a11y]              | DONE | DONE | DONE    |
| [switchboard-plug-about]             | DONE | DONE | DONE    |
| [switchboard-plug-applications]      | DONE | DONE | DONE    |
| [switchboard-plug-bluetooth]         | DONE | DONE | DONE    |
| [switchboard-plug-datetime]          | DONE | DONE | DONE    |
| [switchboard-plug-display]           | DONE | DONE | DONE    |
| [switchboard-plug-keyboard]          | DONE | DONE | DONE    |
| [switchboard-plug-locale]            | DONE | DONE | DONE    |
| [switchboard-plug-mouse-touchpad]    | DONE | DONE | DONE    |
| [switchboard-plug-networking]        | DONE | DONE | DONE    |
| [switchboard-plug-notifications]     | DONE | DONE | DONE    |
| [switchboard-plug-onlineaccounts]    | DONE | DONE | DONE    |
| [switchboard-plug-pantheon-shell]    | DONE | DONE | DONE    |
| [switchboard-plug-parental-controls] | DONE | DONE | DONE    |
| [switchboard-plug-power]             | DONE | DONE | DONE    |
| [switchboard-plug-printers]          | DONE | DONE | DONE    |
| [switchboard-plug-security-privacy]  | DONE | DONE | DONE    |
| [switchboard-plug-sharing]           | DONE | DONE | DONE    |
| [switchboard-plug-sound]             | DONE | DONE | DONE    |
| [switchboard-plug-useraccounts]      | DONE | DONE | DONE    |


### wingpanel indicators

| package name                        | f28  | f29  | rawhide |
| ----------------------------------- | ---- | ---- | ------- |
| [wingpanel-applications-menu]       | DONE | DONE | DONE    |
| [wingpanel-indicator-ayatana]       | DONE | DONE | DONE    |
| [wingpanel-indicator-bluetooth]     | DONE | DONE | DONE    |
| [wingpanel-indicator-datetime]      | ---- | DONE | DONE    |
| [wingpanel-indicator-keyboard]      | DONE | DONE | DONE    |
| [wingpanel-indicator-network]       | DONE | DONE | DONE    |
| [wingpanel-indicator-nightlight]    | DONE | DONE | DONE    |
| [wingpanel-indicator-notifications] | DONE | DONE | DONE    |
| [wingpanel-indicator-power]         | DONE | DONE | DONE    |
| [wingpanel-indicator-session]       | DONE | DONE | DONE    |
| [wingpanel-indicator-sound]         | DONE | DONE | DONE    |


### elementary / pantheon libraries and other shared dependencies

| package name            | f28  | f29  | rawhide |
| ----------------------- | ---- | ---- | ------- |
| [granite]               | ---- | DONE | DONE    |

The `granite` library changed its soname with the update to `5.0`, which is only
available on rawhide, and nightly builds using granite `5.0` and later are only
available for the rawhide elementary-nightly repository, too.


[appcenter]: https://github.com/elementary/appcenter
[elementary-calculator]: https://github.com/elementary/calculator
[elementary-calendar]: https://github.com/elementary/calendar
[elementary-camera]: https://github.com/elementary/camera
[elementary-code]: https://github.com/elementary/code
[elementary-files]: https://github.com/elementary/files
[elementary-mail]: https://github.com/elementary/mail
[elementary-music]: https://github.com/elementary/music
[elementary-photos]: https://github.com/elementary/photos
[elementary-screenshot-tool]: https://github.com/elementary/screenshot-tool
[elementary-terminal]: https://github.com/elementary/terminal
[elementary-videos]: https://github.com/elementary/videos
[switchboard]: https://github.com/elementary/switchboard

[cerbere]: https://github.com/elementary/cerbere
[contractor]: https://github.com/elementary/contractor
[elementary-capnet-assist]: https://github.com/elementary/capnet-assist
[elementary-dpms-helper]: https://github.com/elementary/dpms-helper
[elementary-greeter]: https://github.com/elementary/greeter
[gala]: https://github.com/elementary/gala
[pantheon-agent-geoclue2]: https://github.com/elementary/pantheon-agent-geoclue2
[pantheon-agent-polkit]: https://github.com/elementary/pantheon-agent-polkit
[pantheon-session-settings]: https://github.com/decathorpe/pantheon-session-settings
[plank]: https://launchpad.net/plank
[wingpanel]: https://github.com/elementary/wingpanel

[elementary-icon-theme]: https://github.com/elementary/icons
[elementary-theme]: https://github.com/elementary/stylesheet
[elementary-wallpapers]: https://github.com/elementary/wallpapers

[switchboard-plug-a11y]: https://github.com/elementary/switchboard-plug-a11y
[switchboard-plug-about]: https://github.com/elementary/switchboard-plug-about
[switchboard-plug-applications]: https://github.com/elementary/switchboard-plug-applications
[switchboard-plug-bluetooth]: https://github.com/elementary/switchboard-plug-bluetooth
[switchboard-plug-datetime]: https://github.com/elementary/switchboard-plug-datetime
[switchboard-plug-display]: https://github.com/elementary/switchboard-plug-display
[switchboard-plug-keyboard]: https://github.com/elementary/switchboard-plug-keyboard
[switchboard-plug-locale]: https://github.com/elementary/switchboard-plug-locale
[switchboard-plug-mouse-touchpad]: https://github.com/elementary/switchboard-plug-mouse-touchpad
[switchboard-plug-networking]: https://github.com/elementary/switchboard-plug-networking
[switchboard-plug-notifications]: https://github.com/elementary/switchboard-plug-notifications
[switchboard-plug-onlineaccounts]: https://github.com/elementary/switchboard-plug-onlineaccounts
[switchboard-plug-pantheon-shell]: https://github.com/elementary/switchboard-plug-pantheon-shell
[switchboard-plug-parental-controls]: https://github.com/elementary/switchboard-plug-parental-controls
[switchboard-plug-power]: https://github.com/elementary/switchboard-plug-power
[switchboard-plug-printers]: https://github.com/elementary/switchboard-plug-printers
[switchboard-plug-security-privacy]: https://github.com/elementary/switchboard-plug-security-privacy
[switchboard-plug-sharing]: https://github.com/elementary/switchboard-plug-sharing
[switchboard-plug-sound]: https://github.com/elementary/switchboard-plug-sound
[switchboard-plug-useraccounts]: https://github.com/elementary/switchboard-plug-useraccounts

[wingpanel-applications-menu]: https://github.com/elementary/applications-menu
[wingpanel-indicator-ayatana]: https://github.com/elementary/wingpanel-indicator-ayatana
[wingpanel-indicator-bluetooth]: https://github.com/elementary/wingpanel-indicator-bluetooth
[wingpanel-indicator-datetime]: https://github.com/elementary/wingpanel-indicator-datetime
[wingpanel-indicator-keyboard]: https://github.com/elementary/wingpanel-indicator-keyboard
[wingpanel-indicator-network]: https://github.com/elementary/wingpanel-indicator-network
[wingpanel-indicator-nightlight]: https://github.com/elementary/wingpanel-indicator-nightlight
[wingpanel-indicator-notifications]: https://github.com/elementary/wingpanel-indicator-notifications
[wingpanel-indicator-power]: https://github.com/elementary/wingpanel-indicator-power
[wingpanel-indicator-session]: https://github.com/elementary/wingpanel-indicator-session
[wingpanel-indicator-sound]: https://github.com/elementary/wingpanel-indicator-sound

[granite]: https://github.com/elementary/granite

[elementary/mail#8]: https://github.com/elementary/mail/issues/8

