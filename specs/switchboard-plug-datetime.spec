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
* Sun Dec 11 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.1.1+rev182-1
- Update to latest snapshot.

* Fri Nov 25 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.1.1+rev181-1
- Update to latest snapshot.

* Wed Nov 23 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.1.1+rev180-1
- Update to version 0.1.1.1.


