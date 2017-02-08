%global debug_package %{nil}

Summary:        Bluetooth plug for Switchboard
Name:           switchboard-plug-bluetooth
Version:        0.1.0+rev%{rev}
Release:        1%{?dist}
License:        LGPLv3
URL:            https://launchpad.net/switchboard-plug-bluetooth

# The tarball is generated from a checkout of the specified branch and
# by executing 'bzr export' and has the usual format
# ('%{name}-%{version}.tar.gz'), where %{version} contains the upstream
# version number with a '+bzr%{rev}' suffix specifying the bzr revision.
Source0:        %{name}-%{version}.tar.gz
Source1:        %{name}.conf

BuildRequires:  cmake
BuildRequires:  gettext
BuildRequires:  pkgconfig
BuildRequires:  vala >= 0.22.0
BuildRequires:  vala-tools

BuildRequires:  pkgconfig(glib-2.0) >= 2.32
BuildRequires:  pkgconfig(granite)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  switchboard-devel >= 2.2.0+rev717

Supplements:    switchboard


%description
A Switchboard plug for configuring Bluetooth.

Built for elementary OS.


%prep
%autosetup


%build
%cmake
%make_build


%install
%make_install
%find_lang pantheon-bluetooth-plug


%files -f pantheon-bluetooth-plug.lang
%{_libdir}/switchboard/network/pantheon-bluetooth/


%changelog
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


