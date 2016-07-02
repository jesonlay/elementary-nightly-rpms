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


Requires:       zeitgeist


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
* Sat Jul 02 2016 Fabio Valentini <decathorpe@gmail.com> - 0.9.0~rev666-1
- Update to latest snapshot.

* Fri Jul 01 2016 Fabio Valentini <decathorpe@gmail.com> - 0.9.0~rev665-1
- Update to latest snapshot.

* Wed Jun 29 2016 Fabio Valentini <decathorpe@gmail.com> - 0.9.0~rev664-1
- Update to latest snapshot.

* Tue Jun 28 2016 Fabio Valentini <decathorpe@gmail.com> - 0.9.0~rev663-1
- Update to latest snapshot.

* Thu Jun 23 2016 Fabio Valentini <decathorpe@gmail.com> - 0.9.0~rev662-1
- Update to latest snapshot.

* Tue Jun 21 2016 Fabio Valentini <decathorpe@gmail.com> - 0.9.0~rev661-1
- Update to latest snapshot.

* Sat Jun 18 2016 Fabio Valentini <decathorpe@gmail.com> - 0.9.0~rev660-1
- Update to latest snapshot.

* Wed Jun 15 2016 Fabio Valentini <decathorpe@gmail.com> - 0.9.0~rev659-1
- Update to latest snapshot.

* Tue Jun 14 2016 Fabio Valentini <decathorpe@gmail.com> - 0.9.0~rev658-1
- Update to latest snapshot.

* Mon May 30 2016 Fabio Valentini <decathorpe@gmail.com> - 0.9.0~rev657-4
- Update for packaging changes.

* Sun May 29 2016 Fabio Valentini <decathorpe@gmail.com> - 0.9.0~rev657-3
- Update for packaging changes.

* Mon May 23 2016 Fabio Valentini <decathorpe@gmail.com> - 0.9.0~rev657-2
- Add missing "Requires: zeigeist" to fix crash at startup

* Sat May 21 2016 Fabio Valentini <decathorpe@gmail.com> - 0.9.0~rev657-1
- Update to latest snapshot.

* Sun May 15 2016 Fabio Valentini <decathorpe@gmail.com> - 0.9.0~rev656-1
- Update to latest snapshot.

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


