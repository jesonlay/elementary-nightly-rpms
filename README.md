# elementary-rpms
I use this repository to keep track of files related to packaging / building nightly
snapshots of elementaryOS / pantheon desktop components and applications for fedora.


## packaging progress

The tables list the packaging status of elementary software.

The current build status for each DONE package can be seen at <https://copr.fedorainfracloud.org/coprs/decathorpe/elementary-nightly/monitor/>.


### official elementary apps

| package name          | status                | comment                   | URL                                           | related bugs  |
| --------------------- | --------------------- | ------------------------- | --------------------------------------------- | ------------- |
| appcenter             | TBD                   |                           | <https://launchpad.net/appcenter>             |               |
| audience              | DONE                  | appdata invalid           | <https://launchpad.net/audience>              | [1]           |
| maya-calendar         | DONE                  |                           | <https://launchpad.net/maya>                  |               |
| midori                | TBD                   |                           | <https://launchpad.net/midori>                |               |
| noise                 | DONE                  | desktop invalid           | <https://launchpad.net/noise>                 |               |
| pantheon-calculator   | DONE                  |                           | <https://launchpad.net/pantheon-calculator>   |               |
| pantheon-files        | DONE                  | appdata invalid           | <https://launchpad.net/pantheon-files>        | [2]           |
| pantheon-mail         | DONE                  |                           | <https://launchpad.net/pantheon-mail>         |               |
| pantheon-notes        | DONE                  |                           | <https://launchpad.net/pantheon-notes>        |               |
| pantheon-photos       | DONE                  |                           | <https://launchpad.net/pantheon-photos>       |               |
| pantheon-print        | TBD                   |                           | <https://launchpad.net/pantheon-print>        |               |
| pantheon-snap         | TBD                   |                           | <https://launchpad.net/snap-elementary>       |               |
| pantheon-terminal     | DONE                  | appdata invalid           | <https://launchpad.net/pantheon-terminal>     | [3]           |
| power-manager         | to be decided         |                           | <https://launchpad.net/power-manager>         |               |
| scratch-text-editor   | DONE                  | appdata invalid           | <https://launchpad.net/scratch>               | [4]           |
| switchboard           | DONE                  |                           | <https://launchpad.net/switchboard>           |               |
| screenshot-tool       | TBD                   |                           | <https://launchpad.net/screenshot-tool>       |               |


[1] <https://bugs.launchpad.net/audience/+bug/1595641>

[2] <https://bugs.launchpad.net/pantheon-files/+bug/1595642>

[3] <https://bugs.launchpad.net/pantheon-terminal/+bug/1595643>

[4] <https://bugs.launchpad.net/scratch/+bug/1595645>


### third-party "made for elementary" apps

| package name          | status                | comment                   | URL                                           | related bugs  |
| --------------------- | --------------------- | ------------------------- | --------------------------------------------- | ------------- |
| vocal                 | DONE                  | appdata invalid           | <https://github.com/vocalapp/vocal>           |               |


### pantheon desktop core

| package name                      | status            | comment           | URL                                           | related bugs  |
| --------------------------------- | ----------------- | ----------------- | --------------------------------------------- | ------------- |
| capnet-assist                     | TBD               |                   | <https://launchpad.net/capnet-assist>         |               |
| cerbere                           | DONE              | desktop invalid   | <https://launchpad.net/cerbere>               |               |
| contractor                        | DONE              |                   | <https://launchpad.net/contractor>            |               |
| gala                              | DONE              |                   | <https://launchpad.net/gala>                  |               |
| plank                             | DONE              |                   | <https://launchpad.net/plank>                 |               |
| pantheon-greeter                  | TBD               |                   | <https://launchpad.net/pantheon-greeter>      |               |
| pantheon-xsession-settings        | DONE              |                   |                                               |               |
| slingshot-launcher                | DONE              |                   | <https://launchpad.net/slingshot>             |               |
| wingpanel                         | DONE              |                   | <https://launchpad.net/wingpanel>             |               |


### elementary artwork


| package name          | status                | comment                   | URL                                           | related bugs  |
| --------------------- | --------------------- | ------------------------- | --------------------------------------------- | ------------- |
| egtk                  | DONE                  |                           | <https://launchpad.net/egtk>                  |               |
| elementary-icons      | TBD                   |                           | <https://launchpad.net/elementaryicons>       |               |
| elementary-wallpapers | TBD                   |                           | <https://launchpad.net/elementaryos>          |               |


### switchboard plugs

| package name                      | status        | comment   | URL                                                       | related bugs  |
| --------------------------------- | ------------- | --------- | --------------------------------------------------------- | ------------- |
| pantheon-plugs                    | TBD           |           | <https://launchpad.net/pantheon-plugs>                    |               |
| switchboard-plug-about            | TBD           |           | <https://launchpad.net/switchboard-plug-about>            |               |
| switchboard-plug-a11y             | TBD           |           | <https://launchpad.net/switchboard-plug-a11y>             |               |
| switchboard-plug-applications     | DONE          |           | <https://launchpad.net/switchboard-plug-applications>     |               |
| switchboard-plug-datetime         | TBD           |           | <https://launchpad.net/switchboard-plug-datetime>         |               |
| switchboard-plug-pantheon-shell   | DONE          |           | <https://launchpad.net/switchboard-plug-pantheon-shell>   |               |
| switchboard-plug-display          | TBD           |           | <https://launchpad.net/switchboard-plug-display>          |               |
| switchboard-plug-keyboard         | TBD           |           | <https://launchpad.net/switchboard-plug-keyboard>         |               |
| switchboard-plug-locale           | TBD           |           | <https://launchpad.net/switchboard-plug-locale>           |               |
| switchboard-plug-mouse-touchpad   | DONE          |           | <https://launchpad.net/switchboard-plug-mouse-touchpad>   |               |
| switchboard-plug-networking       | TBD           |           | <https://launchpad.net/switchboard-plug-networking>       |               |
| switchboard-plug-notifications    | DONE          |           | <https://launchpad.net/switchboard-plug-notifications>    |               |
| switchboard-plug-onlineaccounts   | TBD           |           | <https://launchpad.net/switchboard-plug-onlineaccounts>   |               |
| switchboard-plug-parental-controls| TBD           |           | <https://launchpad.net/switchboard-plug-parental-controls>|               |
| switchboard-plug-power            | TBD           |           | <https://launchpad.net/switchboard-plug-power>            |               |
| switchboard-plug-printers         | TBD           |           | <https://launchpad.net/switchboard-plug-printers>         |               |
| switchboard-plug-security-privacy | TBD           |           | <https://launchpad.net/switchboard-plug-security-privacy> |               |
| switchboard-plug-sharing          | TBD           |           | <https://launchpad.net/switchboard-plug-sharing>          |               |
| switchboard-plug-useraccounts     | TBD           |           | <https://launchpad.net/switchboard-plug-useraccounts>     |               |


### wingpanel indicators

| package name                      | status        | comment   | URL                                                       | related bugs  |
| --------------------------------- | ------------- | --------- | --------------------------------------------------------- | ------------- |
| wingpanel-indicator-a11y          | DONE          |           | <https://launchpad.net/wingpanel-indicator-a11y>          |               |
| wingpanel-indicator-ayatana       | FTBFS         |           | <https://launchpad.net/wingpanel-indicator-ayatana>       |               |
| wingpanel-indicator-bluetooth     | DONE          |           | <https://launchpad.net/wingpanel-indicator-bluetooth>     |               |
| wingpanel-indicator-datetime      | DONE          |           | <https://launchpad.net/wingpanel-indicator-datetime>      |               |
| wingpanel-indicator-keyboard      | TBD           |           | <https://launchpad.net/wingpanel-indicator-keyboard>      |               |
| wingpanel-indicator-network       | DONE          |           | <https://launchpad.net/wingpanel-indicator-network>       |               |
| wingpanel-indicator-notifications | DONE          |           | <https://launchpad.net/wingpanel-indicator-notifications> |               |
| wingpanel-indicator-power         | DONE          |           | <https://launchpad.net/wingpanel-indicator-power>         |               |
| wingpanel-indicator-session       | DONE          |           | <https://launchpad.net/wingpanel-indicator-session>       |               |
| wingpanel-indicator-sound         | DONE          |           | <https://launchpad.net/wingpanel-indicator-sound>         |               |


### elementary / pantheon libraries

| package name          | status                | comment                   | URL                                           | related bugs  |
| --------------------- | --------------------- | ------------------------- | --------------------------------------------- | ------------- |
| granite               | DONE                  |                           | <https://launchpad.net/granite>               |               |


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

