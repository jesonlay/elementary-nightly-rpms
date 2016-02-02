%define rev 878

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
BuildRequires: intltool
BuildRequires: libappstream-glib
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

# missing ";" at end of OnlyShowIn line
# desktop-file-edit $RPM_BUILD_ROOT/%{_datadir}/applications/maya-calendar-daemon.desktop --set-key="OnlyShowIn" --set-value="Pantheon;"


%check
# desktop-file-validate $RPM_BUILD_ROOT/%{_datadir}/applications/maya-calendar.desktop

# desktop-file-validate $RPM_BUILD_ROOT/%{_datadir}/applications/maya-calendar-daemon.desktop
# maya-calendar-daemon.desktop: warning: key "OnlyShowIn" is a list and does not have a semicolon as trailing character, fixing
# maya-calendar-daemon.desktop: warning: key "Categories" is a list and does not have a semicolon as trailing character, fixing
# maya-calendar-daemon.desktop: error: value "Pantheon;" for key "OnlyShowIn" in group "Desktop Entry" contains an unregistered value "Pantheon"; values extending the format should start with "X-"

# appstream-util validate-relax --nonet $RPM_BUILD_ROOT/%{_datadir}/appdata/*.appdata.xml
# appdata/maya-calendar.appdata.xml: FAILED:
# ? tag-invalid           : <icon> not allowed in appdata
# ? tag-invalid           : stock icon is not valid [office-calendar]


%clean
rm -rf $RPM_BUILD_ROOT


%post
/usr/sbin/ldconfig

%postun
/usr/sbin/ldconfig
if [ $1 -eq 0 ] ; then
    /usr/bin/glib-compile-schemas %{_datadir}/glib-2.0/schemas &> /dev/null || :
fi

%posttrans
/usr/bin/glib-compile-schemas %{_datadir}/glib-2.0/schemas &> /dev/null || :


%post devel -p /usr/sbin/ldconfig
%postun devel -p /usr/sbin/ldconfig


%files -f maya-calendar.lang
%doc AUTHORS
%license COPYING

%{_bindir}/maya-calendar
%{_bindir}/maya-calendar-daemon

%{_libdir}/libmaya-calendar.so.0
%{_libdir}/libmaya-calendar.so.0.1
%{_libdir}/maya-calendar/

%{_datadir}/appdata/maya-calendar.appdata.xml
%{_datadir}/applications/maya-calendar.desktop
%{_datadir}/applications/maya-calendar-daemon.desktop

%{_datadir}/glib-2.0/schemas/org.pantheon.maya.gschema.xml


%files devel
%{_includedir}/maya-calendar/

%{_libdir}/libmaya-calendar.so
%{_libdir}/pkgconfig/maya-calendar.pc

%{_datadir}/vala/vapi/maya-calendar.deps
%{_datadir}/vala/vapi/maya-calendar.vapi


%changelog
* Tue Feb 02 2016 Fabio Valentini <decathorpe@gmail.com> - 0.3.1.1~rev878-1
- Update to new upstream snapshot.

* Mon Feb 01 2016 Fabio Valentini <decathorpe@gmail.com> - 0.3.1.1~rev877-1
- Update to new upstream snapshot.

* Wed Jan 27 2016 Fabio Valentini <decathorpe@gmail.com> - 0.3.1.1~rev876-2
- Disable desktop file validation.

* Wed Jan 27 2016 Fabio Valentini <decathorpe@gmail.com> - 0.3.1.1~rev876-1
- Update to new upstream snapshot.

* Tue Jan 26 2016 Fabio Valentini <decathorpe@gmail.com> - 0.3.1.1~rev875-2
- Add BR: intltool. Remove no longer included files.

* Tue Jan 26 2016 Fabio Valentini <decathorpe@gmail.com> - 0.3.1.1~rev875-1
- Update to new upstream snapshot.

* Tue Jan 19 2016 Fabio Valentini <decathorpe@gmail.com> - 0.3.1.1~rev872-1
- Update to new upstream snapshot.

* Mon Jan 18 2016 Fabio Valentini <decathorpe@gmail.com> - 0.3.1.1~rev868-1
- Update to new upstream snapshot.

* Mon Jan 11 2016 Fabio Valentini <decathorpe@gmail.com> - 0.3.1.1~rev866-1
- Update to new upstream snapshot.

* Fri Jan 01 2016 Fabio Valentini <decathorpe@gmail.com> - 0.3.1.1~rev864-1
- Update to new upstream snapshot.

* Thu Dec 31 2015 Fabio Valentini <decathorpe@gmail.com> - 0.3.1.1~rev863-1
- Update to new upstream snapshot.

* Wed Dec 23 2015 Fabio Valentini <decathorpe@gmail.com> - 0.3.1.1~rev862-1
- Update to new upstream snapshot.

* Wed Dec 16 2015 Fabio Valentini <decathorpe@gmail.com> - 0.3.1.1~rev859-1
- Update to new upstream snapshot.

* Tue Dec 15 2015 Fabio Valentini <decathorpe@gmail.com> - 0.3.1.1~rev858-1
- Update to new upstream snapshot.

* Mon Dec 14 2015 Fabio Valentini <decathorpe@gmail.com> - 0.3.1.1~rev857-1
- Update to new upstream snapshot.

* Sun Dec 13 2015 Fabio Valentini <decathorpe@gmail.com> - 0.3.1.1~rev856-1
- Update to new upstream snapshot.

* Sun Dec 13 2015 Fabio Valentini <decathorpe@gmail.com> - 0.3.1.1~rev855-2
- Add appdate file and check to spec.

* Sat Dec 12 2015 Fabio Valentini <decathorpe@gmail.com> - 0.3.1.1~rev855-1
- Update to new upstream snapshot.

* Fri Dec 11 2015 Fabio Valentini <decathorpe@gmail.com> - 0.3.1.1~rev853-1
- Update to new upstream snapshot.

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



