%global __provides_exclude_from ^%{_libdir}/switchboard/.*\\.so$

Name:           switchboard-plug-bluetooth
Summary:        Switchboard Bluetooth plug
Version:        0.1.0.99+git%{date}.%{commit}
Release:        1%{?dist}
License:        GPLv3+

URL:            https://github.com/elementary/%{name}

Source0:        %{name}-%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  gettext
BuildRequires:  vala >= 0.22.0
BuildRequires:  vala-tools

BuildRequires:  pkgconfig(glib-2.0) >= 2.32
BuildRequires:  pkgconfig(granite)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(switchboard-2.0)

Requires:       bluez

Supplements:    (bluez and switchboard%{?_isa})


%description
The Bluetooth plug is a section in the Switchboard (System Settings)
that allows the user to manage bluetooth settings and connected
devices.


%prep
%autosetup


%build
mkdir build && pushd build
%cmake ..
%make_build
popd


%install
pushd build
%make_install
popd

%find_lang pantheon-bluetooth-plug


%files -f pantheon-bluetooth-plug.lang
%doc README.md
%license COPYING

%{_libdir}/switchboard/network/pantheon-bluetooth/


%changelog
* Tue Jan 23 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.99+git180123.170518.8c9b08dd-1
- Update to latest snapshot.

* Tue Jan 16 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.99+git180116.193107.f647e121-1
- Update to latest snapshot.

* Thu Jan 04 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.99+git171111.174242.a1000f53-2
- Merge .spec file from fedora.

* Thu Nov 23 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.99+git171111.174242.a1000f53-1
- Switch to git snapshots.

* Sat Nov 11 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.0+rev82-1
- Update to latest snapshot.

* Fri Nov 10 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.0+rev81-1
- Update to latest snapshot.

* Sun Jul 16 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.0+rev79-1
- Update to latest snapshot.

* Sun Jul 02 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.0+rev78-1
- Update to latest snapshot.

* Sun Jun 18 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.0+rev77-1
- Update to latest snapshot.

* Mon Apr 17 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.0+rev57-1
- Update to latest snapshot.

* Mon Apr 17 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.0+rev56-1
- Update to latest snapshot.

* Sat Apr 08 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.0+rev52-1
- Update to latest snapshot.

* Sun Mar 19 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.0+rev51-1
- Update to latest snapshot.

* Wed Mar 15 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.0+rev50-1
- Update to latest snapshot.

* Tue Mar 14 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.0+rev49-1
- Update to latest snapshot.

* Thu Mar 02 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.0+rev47-1
- Update to latest snapshot.

* Wed Feb 22 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.0+rev46-1
- Update to latest snapshot.

* Mon Feb 20 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.0+rev45-1
- Update to latest snapshot.

* Mon Feb 20 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.0+rev44-1
- Update to latest snapshot.

* Sun Feb 19 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.0+rev43-1
- Update to latest snapshot.

* Sat Feb 11 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.0+rev42-1
- Update to latest snapshot.

* Wed Feb 08 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.0+rev41-1
- Update to latest snapshot.

* Sun Jan 29 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.0+rev40-1
- Update to latest snapshot.

* Sat Jan 28 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.0+rev39-1
- Update to latest snapshot.

* Fri Jan 27 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.0+rev38-1
- Update to latest snapshot.

* Sat Jan 21 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.0+rev37-1
- Update to latest snapshot.

* Thu Jan 12 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.0+rev36-1
- Update to version 0.1.0.

* Sat Jan 07 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.0+rev35-1
- Update to version 0.1.0.

* Sun Jan 01 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.0+rev34-1
- Update to latest snapshot.

* Sat Dec 31 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.0+rev33-1
- Update to latest snapshot.

* Thu Dec 29 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.0+rev31-1
- Update to latest snapshot.

* Sun Dec 25 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.0+rev30-1
- Update to latest snapshot.

* Sat Dec 24 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.0+rev29-1
- Update to latest snapshot.

* Thu Dec 22 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.0+rev28-1
- Update to latest snapshot.

* Wed Dec 21 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.0+rev27-1
- Update to latest snapshot.

* Tue Dec 20 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.0+rev26-2
- Make sure switchboard is new enough.
- Fix plug directory.

* Tue Dec 20 2016 Cody Garver <cody@elementary.io> - 0.1.0+rev26-1
- Initial package.


