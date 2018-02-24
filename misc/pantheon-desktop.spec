Summary:        Metapackage to pull in pantheon desktop components
Name:           pantheon-desktop
Version:        0.1.1
Release:        2%{?dist}
License:        GPLv2
URL:            https://copr.fedorainfracloud.org/coprs/decathorpe/elementary-stable/

Requires:       pantheon-session

Recommends:     appcenter
Recommends:     elementary-calculator
Recommends:     elementary-calendar
Recommends:     elementary-camera
Recommends:     elementary-code
Recommends:     elementary-files
Recommends:     elementary-icon-theme
Recommends:     elementary-music
Recommends:     elementary-photos
Recommends:     elementary-screenshot-tool
Recommends:     elementary-terminal
Recommends:     elementary-theme
Recommends:     elementary-videos
Recommends:     pandora-wallpapers
Recommends:     switchboard

BuildArch:      noarch


%description
This metapackage pulls in all packages that are part of a pantheon
desktop.


%files


%changelog
* Sat Feb 24 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.1-2
- Adapt to renamed packages.

* Sat Oct 29 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.1-1
- Adapt to renamed elementary-theme package.

* Sat Oct 29 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1-1
- Initial package.

