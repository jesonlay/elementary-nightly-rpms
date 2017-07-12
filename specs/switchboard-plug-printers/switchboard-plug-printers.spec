%global debug_package %{nil}

Summary:        Switchboard Printers Plug
Name:           switchboard-plug-printers
Version:        0.1+rev%{rev}
Release:        1%{?dist}
License:        GPLv3
URL:            https://launchpad.net/switchboard-plug-printers

Source0:        %{name}-%{version}.tar.gz
Source1:        %{name}.conf

BuildRequires:  cmake
BuildRequires:  gettext
BuildRequires:  pkgconfig
BuildRequires:  vala >= 0.22.0
BuildRequires:  vala-tools

BuildRequires:  cups-devel

BuildRequires:  pkgconfig(glib-2.0) >= 2.32
BuildRequires:  pkgconfig(granite)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(switchboard-2.0)

Supplements:    switchboard


%description
A printers plug for Switchboard.

Designed for elementary OS.


%prep
%autosetup


%build
%cmake
%make_build


%install
%make_install
%find_lang pantheon-printers-plug


%files -f pantheon-printers-plug.lang
%doc AUTHORS
%license COPYING

%{_libdir}/switchboard/hardware/pantheon-printers/


%changelog
* Wed Jul 12 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1+rev177-1
- Update to latest snapshot.

* Tue Jul 04 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1+rev173-1
- Update to latest snapshot.

* Sun Jun 18 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1+rev169-1
- Update to latest snapshot.

* Sat Jun 03 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1+rev168-1
- Update to latest snapshot.

* Sat Apr 29 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1+rev142-1
- Update to latest snapshot.

* Thu Apr 27 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1+rev141-1
- Update to latest snapshot.

* Sat Apr 15 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1+rev140-1
- Update to latest snapshot.

* Wed Apr 05 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1+rev139-1
- Update to latest snapshot.

* Sun Mar 19 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1+rev138-1
- Update to latest snapshot.

* Tue Mar 07 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1+rev137-1
- Update to latest snapshot.

* Mon Feb 27 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1+rev136-1
- Update to latest snapshot.

* Wed Feb 22 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1+rev134-1
- Update to latest snapshot.

* Mon Feb 20 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1+rev133-1
- Update to latest snapshot.

* Sat Feb 18 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1+rev132-1
- Update to latest snapshot.

* Wed Feb 15 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1+rev131-1
- Update to latest snapshot.

* Sun Feb 12 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1+rev130-1
- Update to latest snapshot.

* Sat Feb 11 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1+rev129-1
- Update to latest snapshot.

* Thu Feb 09 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1+rev128-1
- Update to latest snapshot.

* Sat Jan 28 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1+rev127-1
- Update to latest snapshot.

* Fri Jan 27 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1+rev126-1
- Update to latest snapshot.

* Thu Jan 26 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1+rev125-1
- Update to latest snapshot.

* Sat Jan 21 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1+rev124-1
- Update to latest snapshot.

* Mon Jan 09 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1+rev123-1
- Update to version 0.1.

* Sun Jan 08 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1+rev122-1
- Update to version 0.1.

* Fri Jan 06 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1+rev121-1
- Update to version 0.1.

* Tue Jan 03 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1+rev120-1
- Update to version 0.1.

* Mon Jan 02 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1+rev119-1
- Update to latest snapshot.

* Thu Dec 22 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1+rev118-1
- Update to latest snapshot.

* Wed Dec 14 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1+rev117-1
- Update to latest snapshot.

* Wed Nov 23 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1+rev116-1
- Update to version 0.1.


