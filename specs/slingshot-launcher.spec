%global debug_package %{nil}

Summary:        Lightweight and stylish app launcher
Name:           slingshot-launcher
Version:        0.9.0~rev%{rev}
Release:        1%{?dist}
License:        GPLv3
URL:            http://launchpad.net/slingshot

Source0:        %{name}-%{version}.tar.gz
Source1:        %{name}.conf

BuildRequires:  cmake
BuildRequires:  gettext
BuildRequires:  pkgconfig
BuildRequires:  vala >= 0.26.2
BuildRequires:  vala-tools

BuildRequires:  pkgconfig(gee-0.8)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(granite)
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.12.0
BuildRequires:  pkgconfig(json-glib-1.0)
BuildRequires:  pkgconfig(libgnome-menu-3.0)
BuildRequires:  pkgconfig(libsoup-2.4)
BuildRequires:  pkgconfig(plank) >= 0.10.9
BuildRequires:  pkgconfig(switchboard-2.0)
BuildRequires:  pkgconfig(wingpanel-2.0)
BuildRequires:  pkgconfig(zeitgeist-2.0)


%description
The lightweight and stylish app launcher from elementary.

Designed for elementary OS.


%prep
%autosetup


%build
%cmake -DUSE_UNITY:BOOL=OFF -DUSE_ZEITGEIST:BOOL=ON
%make_build


%install
%make_install
%find_lang slingshot


%clean
rm -rf %{buildroot}


%postun
if [ $1 -eq 0 ] ; then
    /usr/bin/glib-compile-schemas %{_datadir}/glib-2.0/schemas &> /dev/null || :
fi

%posttrans
/usr/bin/glib-compile-schemas %{_datadir}/glib-2.0/schemas &> /dev/null || :


%files -f slingshot.lang
%doc AUTHORS
%license COPYING

%{_sysconfdir}/xdg/menus/pantheon-applications.menu

%{_libdir}/wingpanel/libslingshot.so

%{_datadir}/glib-2.0/schemas/org.pantheon.desktop.slingshot.gschema.xml


%changelog
* Thu May 12 2016 Fabio Valentini <decathorpe@gmail.com> - 0.9.0~rev655-1
- Update to latest snapshot.

* Wed May 11 2016 Fabio Valentini <decathorpe@gmail.com> - 0.9.0~rev654-1
- Update to latest snapshot.

* Tue May 10 2016 Fabio Valentini <decathorpe@gmail.com> - 0.9.0~rev653-1
- Update to latest snapshot.

* Sun May 08 2016 Fabio Valentini <decathorpe@gmail.com> - 0.9.0~rev652-1
- Update to latest snapshot.

* Sat May 07 2016 Fabio Valentini <decathorpe@gmail.com> - 0.9.0~rev651-1
- Update for packaging changes.


