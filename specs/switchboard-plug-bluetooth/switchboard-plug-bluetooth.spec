%global __provides_exclude_from ^%{_libdir}/switchboard/.*\\.so$

Name:           switchboard-plug-bluetooth
Summary:        Switchboard Bluetooth plug
Version:        0.1.0.99+git%{date}.%{commit}
Release:        1%{?dist}
License:        GPLv3+

URL:            https://github.com/elementary/%{name}

Source0:        %{name}-%{version}.tar.gz

BuildRequires:  gettext
BuildRequires:  meson
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
%meson
%meson_build


%install
%meson_install

%find_lang bluetooth-plug


%files -f bluetooth-plug.lang
%doc README.md
%license COPYING

%{_libdir}/switchboard/network/libbluetooth.so


%changelog
* Thu Mar 08 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.99+git180308.144040.79195263-1
- Update to latest snapshot.

* Thu Mar 08 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.99+git180308.094859.778b7e40-1
- Update to latest snapshot.

* Wed Mar 07 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.99+git180307.062339.b8d99fe3-1
- Update to latest snapshot.

* Wed Mar 07 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.99+git180306.231538.c0dd8d36-1
- Update to latest snapshot.

* Tue Mar 06 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.99+git180306.195342.edcbd660-1
- Update to latest snapshot.

* Tue Mar 06 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.99+git180306.185020.d0fd423b-1
- Update to latest snapshot.

* Tue Mar 06 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.99+git180306.172544.d4cf1348-1
- Update to latest snapshot.

* Mon Mar 05 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.99+git180303.000302.f62aec7b-1
- Update to latest snapshot.

* Mon Feb 26 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.99+git180226.203409.ab37350e-1
- Update to latest snapshot.

* Mon Feb 26 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.99+git180225.164413.853cc6b2-1
- Update to latest snapshot.

* Sun Feb 25 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.99+git180225.000953.15f2035d-1
- Update to latest snapshot.

* Sat Feb 24 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.99+git180224.113409.0d8cc756-2
- Adapt to cmake -> meson switch.

* Sat Feb 24 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.99+git180224.113409.0d8cc756-1
- Update to latest snapshot.

* Thu Feb 22 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.99+git180221.221426.7d2e0608-1
- Update to latest snapshot.

* Wed Feb 21 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.99+git180221.145109.8827100b-1
- Update to latest snapshot.

* Wed Feb 21 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.99+git180221.074418.f7e7e019-1
- Update to latest snapshot.

* Mon Feb 05 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.99+git180205.001208.a22d0f31-1
- Update to latest snapshot.

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


