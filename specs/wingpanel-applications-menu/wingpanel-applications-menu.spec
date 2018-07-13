%global __provides_exclude_from ^%{_libdir}/wingpanel/.*\\.so$

%global srcname applications-menu
%global appname io.elementary.desktop.wingpanel.applications-menu

Name:           wingpanel-applications-menu
Summary:        Lightweight and stylish app launcher
Version:        2.3.0+git%{date}.%{commit}
Release:        1%{?dist}
License:        GPLv3

URL:            https://github.com/elementary/%{srcname}
Source0:        %{name}-%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  gettext
BuildRequires:  vala >= 0.26.2
BuildRequires:  vala-tools

BuildRequires:  appstream-vala

BuildRequires:  pkgconfig(appstream) >= 0.10.0
BuildRequires:  pkgconfig(gee-0.8)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(granite)
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.12.0
BuildRequires:  pkgconfig(json-glib-1.0)
BuildRequires:  pkgconfig(libgnome-menu-3.0)
BuildRequires:  pkgconfig(libsoup-2.4)
BuildRequires:  pkgconfig(plank) >= 0.10.9
BuildRequires:  pkgconfig(switchboard-2.0)
BuildRequires:  pkgconfig(unity)
BuildRequires:  pkgconfig(wingpanel-2.0)
BuildRequires:  pkgconfig(zeitgeist-2.0)

Requires:       redhat-menus
Requires:       zeitgeist

Requires:       wingpanel%{?_isa}
Supplements:    wingpanel%{?_isa}

Provides:       slingshot-launcher
Obsoletes:      slingshot-launcher


%description
The lightweight and stylish app launcher from elementary.


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

%find_lang slingshot


%files -f slingshot.lang
%doc README.md
%license COPYING

%config(noreplace) %{_sysconfdir}/xdg/menus/pantheon-applications.menu

%{_libdir}/wingpanel/libslingshot.so

%{_datadir}/glib-2.0/schemas/%{appname}.gschema.xml


%changelog
* Fri Jul 13 2018 Fabio Valentini <decathorpe@gmail.com> - 2.3.0+git180713.000449.d3e7e3bd-1
- Update to latest snapshot.

* Wed Jul 11 2018 Fabio Valentini <decathorpe@gmail.com> - 2.3.0+git180709.205554.436f4342-1
- Update to version 2.3.0.


