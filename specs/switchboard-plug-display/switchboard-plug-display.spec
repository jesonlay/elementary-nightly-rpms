%global debug_package %{nil}

Summary:        Switchboard plug to show displays information
Name:           switchboard-plug-display
Version:        0.1.2.1+rev%{rev}
Release:        1%{?dist}
License:        LGPLv3
URL:            https://launchpad.net/switchboard-plug-display

Source0:        %{name}-%{version}.tar.gz
Source1:        %{name}.conf

BuildRequires:  cmake
BuildRequires:  gettext
BuildRequires:  pkgconfig
BuildRequires:  vala >= 0.22.0
BuildRequires:  vala-tools

BuildRequires:  pkgconfig(glib-2.0) >= 2.32
BuildRequires:  pkgconfig(gnome-desktop-3.0)
BuildRequires:  pkgconfig(granite)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(switchboard-2.0)

Supplements:    switchboard


%description
A switchboard plug to show displays information.

Built for elementary OS.


%prep
%autosetup


%build
%cmake
%make_build


%install
%make_install
%find_lang pantheon-display-plug


%files -f pantheon-display-plug.lang
%{_libdir}/switchboard/hardware/pantheon-display/


%changelog
* Wed Mar 15 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.2.1+rev188-1
- Update to latest snapshot.

* Thu Feb 23 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.2.1+rev187-1
- Update to latest snapshot.

* Wed Feb 22 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.2.1+rev186-1
- Update to latest snapshot.

* Sat Feb 18 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.2.1+rev185-1
- Update to latest snapshot.

* Wed Feb 15 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.2.1+rev184-1
- Update to latest snapshot.

* Sun Jan 29 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.2.1+rev183-1
- Update to latest snapshot.

* Sat Jan 28 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.2.1+rev182-1
- Update to latest snapshot.

* Tue Jan 17 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.2.1+rev181-1
- Update to latest snapshot.

* Sat Jan 07 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.2.1+rev180-1
- Update to version 0.1.2.1.

* Fri Jan 06 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.2.1+rev179-1
- Update to version 0.1.2.1.

* Tue Jan 03 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.2.1+rev178-1
- Update to version 0.1.2.1.

* Mon Jan 02 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.2.1+rev177-1
- Update to latest snapshot.

* Thu Dec 22 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.2.1+rev176-1
- Update to latest snapshot.

* Wed Dec 14 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.2.1+rev175-1
- Update to latest snapshot.

* Wed Nov 23 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.2.1+rev174-1
- Update to version 0.1.2.1.


