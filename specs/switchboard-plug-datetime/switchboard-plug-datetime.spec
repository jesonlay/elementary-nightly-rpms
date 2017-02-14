%global debug_package %{nil}

Summary:        Switchboard plug to configure DateTime settings
Name:           switchboard-plug-datetime
Version:        0.1.1.1+rev%{rev}
Release:        1%{?dist}
License:        GPLv3
URL:            https://launchpad.net/switchboard-plug-datetime

Source0:        %{name}-%{version}.tar.gz
Source1:        %{name}.conf

BuildRequires:  cmake
BuildRequires:  gettext
BuildRequires:  pkgconfig
BuildRequires:  vala >= 0.22.0
BuildRequires:  vala-tools

BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(granite)
BuildRequires:  pkgconfig(gthread-2.0)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(switchboard-2.0)

Supplements:    switchboard


%description
Configure the date & time of the user.

Designed for elementary OS.


%prep
%autosetup


%build
%cmake
%make_build


%install
%make_install
%find_lang pantheon-datetime-plug


%files -f pantheon-datetime-plug.lang
%{_libdir}/switchboard/system/pantheon-datetime/


%changelog
* Tue Feb 14 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.1.1+rev203-1
- Update to latest snapshot.

* Mon Feb 13 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.1.1+rev202-1
- Update to latest snapshot.

* Sat Feb 11 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.1.1+rev201-1
- Update to latest snapshot.

* Fri Feb 10 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.1.1+rev200-1
- Update to latest snapshot.

* Thu Feb 09 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.1.1+rev199-1
- Update to latest snapshot.

* Wed Feb 08 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.1.1+rev198-1
- Update to latest snapshot.

* Sun Jan 29 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.1.1+rev197-1
- Update to latest snapshot.

* Sat Jan 28 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.1.1+rev196-1
- Update to latest snapshot.

* Fri Jan 27 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.1.1+rev195-1
- Update to latest snapshot.

* Sat Jan 21 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.1.1+rev194-1
- Update to latest snapshot.

* Sat Jan 14 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.1.1+rev193-1
- Update to version 0.1.1.1.

* Thu Jan 12 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.1.1+rev192-1
- Update to version 0.1.1.1.

* Wed Jan 11 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.1.1+rev191-1
- Update to version 0.1.1.1.

* Mon Jan 09 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.1.1+rev190-1
- Update to version 0.1.1.1.

* Sun Jan 08 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.1.1+rev189-1
- Update to version 0.1.1.1.

* Tue Dec 27 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.1.1+rev188-1
- Update to latest snapshot.

* Wed Dec 21 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.1.1+rev187-1
- Update to latest snapshot.

* Sun Dec 18 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.1.1+rev186-1
- Update to latest snapshot.

* Sat Dec 17 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.1.1+rev185-1
- Update to latest snapshot.

* Fri Dec 16 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.1.1+rev184-1
- Update to latest snapshot.

* Thu Dec 15 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.1.1+rev183-1
- Update to latest snapshot.

* Sun Dec 11 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.1.1+rev182-1
- Update to latest snapshot.

* Fri Nov 25 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.1.1+rev181-1
- Update to latest snapshot.

* Wed Nov 23 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.1.1+rev180-1
- Update to version 0.1.1.1.


