%global debug_package %{nil}

Summary:        Keyboard indicator for wingpanel
Name:           wingpanel-indicator-keyboard
Version:        2.0.1+rev%{rev}
Release:        1%{?dist}
License:        GPLv3
URL:            https://launchpad.net/wingpanel-indicator-keyboard

Source0:        %{name}-%{version}.tar.gz
Source1:        %{name}.conf

BuildRequires:  cmake
BuildRequires:  gettext
BuildRequires:  pkgconfig
BuildRequires:  vala >= 0.22.0
BuildRequires:  vala-tools

BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(granite)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(wingpanel-2.0)

Supplements:    wingpanel


%description
A keyboard indicator for wingpanel.


%prep
%autosetup


%build
%cmake
%make_build


%install
%make_install
%find_lang keyboard-indicator


%files -f keyboard-indicator.lang
%{_libdir}/wingpanel/libkeyboard.so


%changelog
* Sat Dec 17 2016 Fabio Valentini <decathorpe@gmail.com> - 2.0.1+rev60-1
- Update to latest snapshot.

* Fri Dec 16 2016 Fabio Valentini <decathorpe@gmail.com> - 2.0.1+rev59-1
- Update to latest snapshot.

* Thu Dec 08 2016 Fabio Valentini <decathorpe@gmail.com> - 2.0.1+rev58-1
- Update to latest snapshot.

* Fri Dec 02 2016 Fabio Valentini <decathorpe@gmail.com> - 2.0.1+rev57-1
- Update to latest snapshot.

* Wed Nov 23 2016 Fabio Valentini <decathorpe@gmail.com> - 2.0.1+rev56-1
- Update to version 2.0.1.


