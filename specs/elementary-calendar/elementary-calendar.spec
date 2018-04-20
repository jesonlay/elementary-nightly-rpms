%global __provides_exclude_from ^%{_libdir}/maya-calendar/.*\\.so$

%global srcname calendar
%global appname io.elementary.calendar
%global oldname maya-calendar

Name:           elementary-calendar
Summary:        Desktop calendar app from elementary
Version:        0.4.1+git%{date}.%{commit}
Release:        1%{?dist}
License:        GPLv3+

URL:            https://github.com/elementary/%{srcname}
Source0:        %{name}-%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  desktop-file-utils
BuildRequires:  gettext
BuildRequires:  intltool
BuildRequires:  libappstream-glib
BuildRequires:  vala

BuildRequires:  pkgconfig(champlain-0.12)
BuildRequires:  pkgconfig(champlain-gtk-0.12)
BuildRequires:  pkgconfig(clutter-1.0)
BuildRequires:  pkgconfig(folks)
BuildRequires:  pkgconfig(gee-0.8)
BuildRequires:  pkgconfig(geocode-glib-1.0)
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  pkgconfig(gmodule-2.0)
BuildRequires:  pkgconfig(granite) >= 0.5
BuildRequires:  pkgconfig(gthread-2.0)
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.11.6
BuildRequires:  pkgconfig(libecal-1.2) >= 3.8.0
BuildRequires:  pkgconfig(libical)
BuildRequires:  pkgconfig(libnotify)

# elementary-calendar also provides a generic symbolic icon (actions/calendar-go-today)
Requires:       hicolor-icon-theme

Provides:       maya-calendar
Obsoletes:      maya-calendar


%description
A slim, lightweight GTK+3 calendar app written in Vala, designed for
elementary OS. Also looks and works great on other GTK+ desktops.


%package        devel
Summary:        The official elementary calendar (devel files)
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description    devel
A slim, lightweight GTK+3 calendar app written in Vala, designed for
elementary OS. Also looks and works great on other GTK+ desktops.

This package contains the development files.


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

%find_lang %{oldname}


%check
desktop-file-validate \
    %{buildroot}/%{_datadir}/applications/%{appname}.desktop
desktop-file-validate \
    %{buildroot}/%{_datadir}/applications/%{appname}-daemon.desktop

appstream-util validate-relax --nonet \
    %{buildroot}/%{_datadir}/metainfo/%{appname}.appdata.xml


%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig


%files -f %{oldname}.lang
%doc README.md
%license COPYING

%{_bindir}/%{oldname}
%{_bindir}/%{oldname}-daemon

%{_libdir}/lib%{oldname}.so.0
%{_libdir}/lib%{oldname}.so.0.1
%{_libdir}/%{oldname}/

%{_datadir}/applications/%{appname}.desktop
%{_datadir}/applications/%{appname}-daemon.desktop
%{_datadir}/glib-2.0/schemas/org.pantheon.maya.gschema.xml
%{_datadir}/metainfo/%{appname}.appdata.xml


%files devel
%{_includedir}/%{oldname}/

%{_libdir}/lib%{oldname}.so
%{_libdir}/pkgconfig/%{oldname}.pc

%{_datadir}/vala/vapi/%{oldname}.deps
%{_datadir}/vala/vapi/%{oldname}.vapi


%changelog
* Fri Apr 20 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.1+git180420.181014.a820e08c-1
- Update to latest snapshot.

* Fri Apr 20 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.1+git180420.001105.8d053678-1
- Update to latest snapshot.

* Thu Mar 22 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.1+git180322.183805.f86347ae-2
- Adapt to upstream file changes.

* Thu Mar 22 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.1+git180322.183805.f86347ae-1
- Update to latest snapshot.

* Tue Mar 20 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.1+git180320.001106.fce14afd-1
- Update to latest snapshot.

* Sun Mar 18 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.1+git180318.000758.9963bc7c-1
- Update to latest snapshot.

* Fri Mar 16 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.1+git180316.000135.9753182b-1
- Update to latest snapshot.

* Wed Mar 07 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.1+git180306.185646.c47dec04-2
- Adapt to upstream file changes.

* Tue Mar 06 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.1+git180306.185646.c47dec04-1
- Update to latest snapshot.

* Mon Mar 05 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.1+git180305.200209.e03204ba-1
- Update to latest snapshot.

* Wed Feb 28 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.1+git180228.000732.56ab3464-1
- Update to latest snapshot.

* Tue Feb 27 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.1+git180227.081048.174f147d-1
- Update to latest snapshot.

* Fri Feb 23 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.1+git180220.210223.5dec77cf-1
- Initial package.


