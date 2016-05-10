# elementary-rpms
I use this repository to keep track of files related to packaging / building nightly
snapshots of elementaryOS / pantheon desktop components and applications for fedora.


## packaging progress

The tables list the packaging status of elementary software.


### official elementary apps

| package name          | status                | comment                   | URL                                           | related bugs      |
| --------------------- | --------------------- | ------------------------- | --------------------------------------------- | ----------------- |
| appcenter             | TBD                   |                           | <https://launchpad.net/appcenter>             |                   |
| audience              | DONE                  | appdata invalid           | <https://launchpad.net/audience>              |                   |
| maya-calendar         | DONE                  | appdata, desktop invalid  | <https://launchpad.net/maya>                  | [1] [2]           |
| midori                | TBD                   |                           | <https://launchpad.net/midori>                |                   |
| noise                 | DONE                  | appdata, desktop invalid  | <https://launchpad.net/noise>                 |                   |
| pantheon-calculator   | DONE                  | appdata invalid           | <https://launchpad.net/pantheon-calculator>   |                   |
| pantheon-files        | DONE                  | appdata invalid           | <https://launchpad.net/pantheon-files>        |                   |
| pantheon-mail         | DONE                  | appdata invalid           | <https://launchpad.net/pantheon-mail>         |                   |
| pantheon-notes        | DONE                  |                           | <https://launchpad.net/pantheon-notes>        |                   |
| pantheon-photos       | DONE                  | appdata, desktop invalid  | <https://launchpad.net/pantheon-photos>       |                   |
| pantheon-print        | TBD                   |                           | <https://launchpad.net/pantheon-print>        |                   |
| pantheon-snap         | TBD                   |                           | <https://launchpad.net/snap-elementary>       |                   |
| pantheon-terminal     | DONE                  | appdata invalid           | <https://launchpad.net/pantheon-terminal>     |                   |
| power-manager         | to be decided         |                           | <https://launchpad.net/power-manager>         |                   |
| scratch-text-editor   | DONE                  | appdata invalid           | <https://launchpad.net/scratch>               |                   |
| switchboard           | DONE                  | plus plugs                | <https://launchpad.net/switchboard>           |                   |
| screenshot-tool       | TBD                   |                           | <https://launchpad.net/screenshot-tool>       |                   |

[1] <https://bugs.freedesktop.org/show_bug.cgi?id=51258>

[2] <https://bugzilla.redhat.com/show_bug.cgi?id=1333550>


### third-party "made for elementary" apps

| package name          | status                | comment                   | URL                                           | related bugs      |
| --------------------- | --------------------- | ------------------------- | --------------------------------------------- | ----------------- |
| vocal                 | DONE                  | appdata invalid           | <https://github.com/vocalapp/vocal>           |                   |


### pantheon desktop core

| package name                      | status            | comment           | URL                                           | related bugs      |
| --------------------------------- | ----------------- | ----------------- | --------------------------------------------- | ----------------- |
| capnet-assist                     | TBD               |                   | <https://launchpad.net/capnet-assist>         |                   |
| cerbere                           | DONE              | desktop invalid   | <https://launchpad.net/cerbere>               |                   |
| contractor                        | DONE              |                   | <https://launchpad.net/contractor>            |                   |
| gala                              | DONE              |                   | <https://launchpad.net/gala>                  |                   |
| pantheon-dock                     | to be decided     | copy of plank?    | <https://launchpad.net/pantheon-dock>         |                   |
| plank                             | DONE              |                   | <https://launchpad.net/plank>                 |                   |
| pantheon-greeter                  | TBD               |                   | <https://launchpad.net/pantheon-greeter>      |                   |
| pantheon-xsession-settings        | DONE              |                   |                                               |                   |
| slingshot-launcher                | DONE              |                   | <https://launchpad.net/slingshot>             |                   |
| wingpanel                         | DONE              | plus indicators   | <https://launchpad.net/wingpanel>             |                   |


### elementary artwork


| package name          | status                | comment                   | URL                                           | related bugs      |
| --------------------- | --------------------- | ------------------------- | --------------------------------------------- | ----------------- |
| egtk                  | DONE                  |                           | <https://launchpad.net/egtk>                  |                   |
| elementary-icons      | TBD                   |                           | <https://launchpad.net/elementaryicons>       |                   |
| elementary-wallpapers | TBD                   |                           | <https://launchpad.net/elementaryos>          |                   |


### switchboard plugs

| package name                      | status        | comment   | URL                                                       | related bugs      |
| --------------------------------- | ------------- | --------- | --------------------------------------------------------- | ----------------- |
| pantheon-plugs                    | TBD           |           | <https://launchpad.net/pantheon-plugs>                    |                   |
| switchboard-plug-about            | TBD           |           | <https://launchpad.net/switchboard-plug-about>            |                   |
| switchboard-plug-a11y             | TBD           |           | <https://launchpad.net/switchboard-plug-a11y>             |                   |
| switchboard-plug-applications     | TBD           |           | <https://launchpad.net/switchboard-plug-applications>     |                   |
| switchboard-plug-datetime         | TBD           |           | <https://launchpad.net/switchboard-plug-datetime>         |                   |
| switchboard-plug-pantheon-shell   | TBD           |           | <https://launchpad.net/switchboard-plug-pantheon-shell>   |                   |
| switchboard-plug-display          | TBD           |           | <https://launchpad.net/switchboard-plug-display>          |                   |
| switchboard-plug-keyboard         | TBD           |           | <https://launchpad.net/switchboard-plug-keyboard>         |                   |
| switchboard-plug-locale           | TBD           |           | <https://launchpad.net/switchboard-plug-locale>           |                   |
| switchboard-plug-mouse-touchpad   | TBD           |           | <https://launchpad.net/switchboard-plug-mouse-touchpad>   |                   |
| switchboard-plug-networking       | TBD           |           | <https://launchpad.net/switchboard-plug-networking>       |                   |
| switchboard-plug-notifications    | TBD           |           | <https://launchpad.net/switchboard-plug-notifications>    |                   |
| switchboard-plug-onlineaccounts   | TBD           |           | <https://launchpad.net/switchboard-plug-onlineaccounts>   |                   |
| switchboard-plug-parental-controls| TBD           |           | <https://launchpad.net/switchboard-plug-parental-controls>|                   |
| switchboard-plug-power            | TBD           |           | <https://launchpad.net/switchboard-plug-power>            |                   |
| switchboard-plug-printers         | TBD           |           | <https://launchpad.net/switchboard-plug-printers>         |                   |
| switchboard-plug-security-privacy | TBD           |           | <https://launchpad.net/switchboard-plug-security-privacy> |                   |
| switchboard-plug-sharing          | TBD           |           | <https://launchpad.net/switchboard-plug-sharing>          |                   |
| switchboard-plug-useraccounts     | TBD           |           | <https://launchpad.net/switchboard-plug-useraccounts>     |                   |


### wingpanel indicators

| package name                      | status        | comment   | URL                                                       | related bugs      |
| --------------------------------- | ------------- | --------- | --------------------------------------------------------- | ----------------- |
| wingpanel-indicator-a11y          | TBD           |           | <https://launchpad.net/wingpanel-indicator-a11y>          |                   |
| wingpanel-indicator-ayatana       | TBD           |           | <https://launchpad.net/wingpanel-indicator-ayatana>       |                   |
| wingpanel-indicator-bluetooth     | TBD           |           | <https://launchpad.net/wingpanel-indicator-bluetooth>     |                   |
| wingpanel-indicator-datetime      | TBD           |           | <https://launchpad.net/wingpanel-indicator-datetime>      |                   |
| wingpanel-indicator-keyboard      | TBD           |           | <https://launchpad.net/wingpanel-indicator-keyboard>      |                   |
| wingpanel-indicator-network       | DONE          |           | <https://launchpad.net/wingpanel-indicator-network>       |                   |
| wingpanel-indicator-notifications | TBD           |           | <https://launchpad.net/wingpanel-indicator-notifications> |                   |
| wingpanel-indicator-power         | DONE          |           | <https://launchpad.net/wingpanel-indicator-power>         |                   |
| wingpanel-indicator-session       | DONE          |           | <https://launchpad.net/wingpanel-indicator-session>       |                   |
| wingpanel-indicator-sound         | DONE          |           | <https://launchpad.net/wingpanel-indicator-sound>         |                   |


### elementary / pantheon libraries

| package name          | status                | comment                   | URL                                           | related bugs      |
| --------------------- | --------------------- | ------------------------- | --------------------------------------------- | ----------------- |
| granite               | DONE                  |                           | <https://launchpad.net/granite>               |                   |


## USAGE

- Get my build tool (kentauros) from copr or github
- configure copr for your copr account if you want to upload
- change settings in the configs as you wish (e.g. change copr repository name)
- run:

```sh
ktr --verbose chain --all
```

- or, if you want to force actions on all packages:

```sh
ktr --verbose chain --force --all
```

