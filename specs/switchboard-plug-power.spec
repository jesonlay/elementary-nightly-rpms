%global debug_package %{nil}

Summary:        Switchboard Power Plug
Name:           switchboard-plug-power
Version:        0.3+rev%{rev}
Release:        1%{?dist}
License:        GPLv3
URL:            https://launchpad.net/switchboard-plug-power

Source0:        %{name}-%{version}.tar.gz
Source1:        %{name}.conf

BuildRequires:  cmake
BuildRequires:  gettext
BuildRequires:  pkgconfig
BuildRequires:  vala >= 0.34.1
BuildRequires:  vala-tools

BuildRequires:  pkgconfig(glib-2.0) >= 2.32
BuildRequires:  pkgconfig(gnome-settings-daemon)
BuildRequires:  pkgconfig(granite)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(polkit-gobject-1)
BuildRequires:  pkgconfig(switchboard-2.0)

Supplements:    switchboard

Requires:       elementary-dpms-helper


%description
Control system power consumption with this Switchboard preference plug.

Designed for elementary OS.


%prep
%autosetup


%build
%cmake
%make_build


%install
%make_install
%find_lang pantheon-power-plug


%files -f pantheon-power-plug.lang
%{_libdir}/switchboard/hardware/pantheon-power/

%{_datadir}/polkit-1/actions/org.pantheon.switchboard.power.policy


%changelog
* Wed Dec 28 2016 Fabio Valentini <decathorpe@gmail.com> - 0.3+rev390-1
- Update to latest snapshot.

* Tue Dec 27 2016 Fabio Valentini <decathorpe@gmail.com> - 0.3+rev389-1
- Update to latest snapshot.

* Mon Dec 26 2016 Fabio Valentini <decathorpe@gmail.com> - 0.3+rev388-1
- Update to latest snapshot.

* Sun Dec 25 2016 Fabio Valentini <decathorpe@gmail.com> - 0.3+rev387-1
- Update to latest snapshot.

* Sat Dec 24 2016 Fabio Valentini <decathorpe@gmail.com> - 0.3+rev386-1
- Update to latest snapshot.

* Tue Dec 20 2016 Fabio Valentini <decathorpe@gmail.com> - 0.3+rev385-1
- Update to latest snapshot.

* Sat Dec 17 2016 Fabio Valentini <decathorpe@gmail.com> - 0.3+rev384-1
- Update to latest snapshot.

* Thu Dec 15 2016 Fabio Valentini <decathorpe@gmail.com> - 0.3+rev383-1
- Update to latest snapshot.

* Wed Dec 14 2016 Fabio Valentini <decathorpe@gmail.com> - 0.3+rev382-1
- Update to latest snapshot.

* Wed Dec 14 2016 Fabio Valentini <decathorpe@gmail.com> - 0.3+rev381-1
- Update to latest snapshot.

* Tue Dec 13 2016 Fabio Valentini <decathorpe@gmail.com> - 0.3+rev380-1
- Update to latest snapshot.

* Mon Dec 12 2016 Fabio Valentini <decathorpe@gmail.com> - 0.3+rev379-1
- Update to latest snapshot.

* Sun Dec 11 2016 Fabio Valentini <decathorpe@gmail.com> - 0.3+rev378-1
- Update to latest snapshot.

* Sat Dec 10 2016 Fabio Valentini <decathorpe@gmail.com> - 0.3+rev377-1
- Update to latest snapshot.

* Fri Dec 09 2016 Fabio Valentini <decathorpe@gmail.com> - 0.3+rev376-1
- Update to latest snapshot.

* Fri Dec 02 2016 Fabio Valentini <decathorpe@gmail.com> - 0.3+rev375-1
- Update to latest snapshot.

* Thu Dec 01 2016 Fabio Valentini <decathorpe@gmail.com> - 0.3+rev374-1
- Update to latest snapshot.

* Wed Nov 30 2016 Fabio Valentini <decathorpe@gmail.com> - 0.3+rev373-1
- Update to latest snapshot.

* Tue Nov 29 2016 Fabio Valentini <decathorpe@gmail.com> - 0.3+rev372-1
- Update to latest snapshot.

* Mon Nov 28 2016 Fabio Valentini <decathorpe@gmail.com> - 0.3+rev371-1
- Update to latest snapshot.

* Wed Nov 23 2016 Fabio Valentini <decathorpe@gmail.com> - 0.3+rev370-1
- Update to version 0.3.


