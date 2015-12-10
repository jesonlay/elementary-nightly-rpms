%define rev 851

Summary: The official elementary calendar
Name: maya-calendar
Version: 0.3.1.1~rev%{rev}
Release: 1%{?dist}
License: GPLv3
URL: http://launchpad.net/maya

Source0: %{name}-%{version}.tar.gz
Source1: %{name}.conf

BuildRequires: cmake
BuildRequires: desktop-file-utils
BuildRequires: gettext
BuildRequires: pkgconfig
BuildRequires: vala

BuildRequires: pkgconfig(champlain-0.12)
BuildRequires: pkgconfig(champlain-gtk-0.12)
BuildRequires: pkgconfig(clutter-1.0)
BuildRequires: pkgconfig(folks)
BuildRequires: pkgconfig(gee-0.8)
BuildRequires: pkgconfig(geocode-glib-1.0)
BuildRequires: pkgconfig(gio-2.0)
BuildRequires: pkgconfig(glib-2.0)
BuildRequires: pkgconfig(gobject-2.0)
BuildRequires: pkgconfig(gmodule-2.0)
BuildRequires: pkgconfig(granite)
BuildRequires: pkgconfig(gthread-2.0)
BuildRequires: pkgconfig(gtk+-3.0) >= 3.11.6
BuildRequires: pkgconfig(libecal-1.2) >= 3.8.0
BuildRequires: pkgconfig(libical)


%description
A slim, lightweight GTK+3 calendar app written in Vala, designed for elementary OS. Also looks and works great on other GTK+ desktops.

In elementary OS, Maya is known as Calendar.


%package devel
Summary: The official elementary calendar (devel files)
%description devel
A slim, lightweight GTK+3 calendar app written in Vala, designed for elementary OS. Also looks and works great on other GTK+ desktops.

In elementary OS, Maya is known as Calendar.

This package contains the development files.


%prep
%autosetup


%build
%cmake
%make_build


%install
%make_install
%find_lang maya-calendar


%check
#desktop-file-validate $RPM_BUILD_ROOT/%{_datadir}/applications/maya-calendar.desktop
#desktop-file-validate $RPM_BUILD_ROOT/%{_datadir}/applications/maya-calendar-daemon.desktop


%clean
rm -rf $RPM_BUILD_ROOT


%post
/usr/sbin/ldconfig
/usr/bin/glib-compile-schemas %{_datadir}/glib-2.0/schemas &> /dev/null

%postun
/usr/sbin/ldconfig
if [ $1 -eq 0 ] ; then
    /usr/bin/glib-compile-schemas %{_datadir}/glib-2.0/schemas &> /dev/null || :
fi

%posttrans
/usr/bin/glib-compile-schemas %{_datadir}/glib-2.0/schemas &> /dev/null || :


%post devel
/usr/sbin/ldconfig

%postun devel
/usr/sbin/ldconfig


%files -f maya-calendar.lang
%doc AUTHORS
%license COPYING

%{_bindir}/maya-calendar
%{_bindir}/maya-calendar-daemon

%{_libdir}/libmaya-calendar.so.0
%{_libdir}/libmaya-calendar.so.0.1
%{_libdir}/maya-calendar/

%{_datadir}/applications/maya-calendar.desktop
%{_datadir}/applications/maya-calendar-daemon.desktop

%{_datadir}/glib-2.0/schemas/org.pantheon.maya.gschema.xml
%{_datadir}/icons/hicolor/scalable/actions/calendar-go-today.svg
%{_datadir}/maya-calendar/


%files devel
%{_includedir}/maya-calendar/

%{_libdir}/libmaya-calendar.so
%{_libdir}/pkgconfig/maya-calendar.pc

%{_datadir}/vala/vapi/maya-calendar.deps
%{_datadir}/vala/vapi/maya-calendar.vapi


%changelog
* Tue Dec 08 2015 Fabio Valentini <decathorpe@gmail.com> - 0.3.1.1~rev851-1
- Update to new upstream snapshot.

* Mon Dec 07 2015 Fabio Valentini <decathorpe@gmail.com> - 0.3.1.1~rev850-1
- Update to new upstream snapshot.

* Sun Dec 06 2015 Fabio Valentini <decathorpe@gmail.com> - 0.3.1.1~rev849-1
- Update to new upstream snapshot.

* Thu Dec 03 2015 Fabio Valentini <decathorpe@gmail.com> - 0.3.1.1~rev847-1
- Update to new upstream snapshot.

* Tue Dec 01 2015 Fabio Valentini <decathorpe@gmail.com> - 0.3.1.1~rev846-1
- Update to new upstream snapshot.

* Mon Nov 30 2015 Fabio Valentini <decathorpe@gmail.com> - 0.3.1.1~rev845-1
- Update to new upstream snapshot.

* Sun Nov 29 2015 Fabio Valentini <decathorpe@gmail.com> - 0.3.1.1~rev844-1
- Update to new upstream snapshot.

* Sat Nov 28 2015 Fabio Valentini <decathorpe@gmail.com> - 0.3.1.1~rev842-1
- Update to new upstream snapshot.

* Tue Nov 24 2015 Fabio Valentini <decathorpe@gmail.com> - 0.3.1.1~rev841-1
- Update to new upstream snapshot.

* Mon Nov 16 2015 Fabio Valentini <decathorpe@gmail.com> - 0.3.1.1~rev840-1
- Update to new upstream snapshot.

* Sun Nov 15 2015 Fabio Valentini <decathorpe@gmail.com> - 0.3.1.1~rev839-1
- Update to new upstream snapshot.

* Fri Nov 13 2015 Fabio Valentini <decathorpe@gmail.com> - 0.3.1.1~rev838-1
- Update to new upstream snapshot.

* Mon Nov 09 2015 Fabio Valentini <decathorpe@gmail.com> - 0.3.1.1~rev837-1
- Initial package.



