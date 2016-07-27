Summary:        The official elementary calendar
Name:           maya-calendar
Version:        0.3.1.1~rev%{rev}
Release:        1%{?dist}
License:        GPLv3
URL:            http://launchpad.net/maya

Source0:        %{name}-%{version}.tar.gz
Source1:        %{name}.conf

BuildRequires:  cmake
BuildRequires:  desktop-file-utils
BuildRequires:  gettext
BuildRequires:  intltool
BuildRequires:  libappstream-glib
BuildRequires:  pkgconfig
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
BuildRequires:  pkgconfig(granite)
BuildRequires:  pkgconfig(gthread-2.0)
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.11.6
BuildRequires:  pkgconfig(libecal-1.2) >= 3.8.0
BuildRequires:  pkgconfig(libical)


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
desktop-file-validate $RPM_BUILD_ROOT/%{_datadir}/applications/maya-calendar.desktop
# desktop-file-validate $RPM_BUILD_ROOT/%{_datadir}/applications/maya-calendar-daemon.desktop
# appstream-util validate-relax --nonet $RPM_BUILD_ROOT/%{_datadir}/appdata/*.appdata.xml


%clean
rm -rf %{buildroot}/RPM_BUILD_ROOT


%post
/sbin/ldconfig
/usr/bin/update-desktop-database &> /dev/null || :


%postun
/sbin/ldconfig
/usr/bin/update-desktop-database &> /dev/null || :
if [ $1 -eq 0 ] ; then
    /usr/bin/glib-compile-schemas %{_datadir}/glib-2.0/schemas &> /dev/null || :
fi


%posttrans
/usr/bin/glib-compile-schemas %{_datadir}/glib-2.0/schemas &> /dev/null || :


%post           devel -p /sbin/ldconfig
%postun         devel -p /sbin/ldconfig


%files       -f maya-calendar.lang
%doc AUTHORS COPYRIGHT HACKING
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
* Wed Jul 27 2016 Fabio Valentini <decathorpe@gmail.com> - 0.3.1.1~rev933-1
- Update to latest snapshot.

* Tue Jul 26 2016 Fabio Valentini <decathorpe@gmail.com> - 0.3.1.1~rev932-1
- Update to latest snapshot.

* Mon Jul 25 2016 Fabio Valentini <decathorpe@gmail.com> - 0.3.1.1~rev931-1
- Update to latest snapshot.

* Fri Jul 22 2016 Fabio Valentini <decathorpe@gmail.com> - 0.3.1.1~rev928-1
- Update to latest snapshot.

* Fri Jul 22 2016 Fabio Valentini <decathorpe@gmail.com> - 0.3.1.1~rev927-1
- Update to latest snapshot.

* Thu Jul 21 2016 Fabio Valentini <decathorpe@gmail.com> - 0.3.1.1~rev926-1
- Update to latest snapshot.

* Tue Jul 19 2016 Fabio Valentini <decathorpe@gmail.com> - 0.3.1.1~rev925-1
- Update to latest snapshot.

* Sun Jul 17 2016 Fabio Valentini <decathorpe@gmail.com> - 0.3.1.1~rev924-1
- Update to latest snapshot.

* Sat Jul 09 2016 Fabio Valentini <decathorpe@gmail.com> - 0.3.1.1~rev923-1
- Update to latest snapshot.

* Fri Jul 08 2016 Fabio Valentini <decathorpe@gmail.com> - 0.3.1.1~rev922-1
- Update to latest snapshot.

* Wed Jul 06 2016 Fabio Valentini <decathorpe@gmail.com> - 0.3.1.1~rev921-2
- Update for packaging changes.

* Fri Jun 17 2016 Fabio Valentini <decathorpe@gmail.com> - 0.3.1.1~rev916-1
- Update to latest snapshot.

* Fri Jun 17 2016 Fabio Valentini <decathorpe@gmail.com> - 0.3.1.1~rev915-1
- Update to latest snapshot.

* Wed Jun 15 2016 Fabio Valentini <decathorpe@gmail.com> - 0.3.1.1~rev914-1
- Update to latest snapshot.

* Tue Jun 14 2016 Fabio Valentini <decathorpe@gmail.com> - 0.3.1.1~rev913-1
- Update to latest snapshot.

* Wed Jun 08 2016 Fabio Valentini <decathorpe@gmail.com> - 0.3.1.1~rev912-1
- Update to latest snapshot.

* Tue Jun 07 2016 Fabio Valentini <decathorpe@gmail.com> - 0.3.1.1~rev911-1
- Update to latest snapshot.

* Fri Jun 03 2016 Fabio Valentini <decathorpe@gmail.com> - 0.3.1.1~rev%{rev}-2
- Partly enable desktop file validation.

* Fri Jun 03 2016 Fabio Valentini <decathorpe@gmail.com> - 0.3.1.1~rev910-1
- Update to latest snapshot.

* Thu Jun 02 2016 Fabio Valentini <decathorpe@gmail.com> - 0.3.1.1~rev909-1
- Update to latest snapshot.

* Wed Jun 01 2016 Fabio Valentini <decathorpe@gmail.com> - 0.3.1.1~rev908-1
- Update to latest snapshot.

* Mon May 30 2016 Fabio Valentini <decathorpe@gmail.com> - 0.3.1.1~rev907-3
- Update for packaging changes.

* Sun May 29 2016 Fabio Valentini <decathorpe@gmail.com> - 0.3.1.1~rev907-2
- Update for packaging changes.

* Wed May 25 2016 Fabio Valentini <decathorpe@gmail.com> - 0.3.1.1~rev907-1
- Update to latest snapshot.

* Thu May 12 2016 Fabio Valentini <decathorpe@gmail.com> - 0.3.1.1~rev906-1
- Update to latest snapshot.

* Wed May 11 2016 Fabio Valentini <decathorpe@gmail.com> - 0.3.1.1~rev905-1
- Update to latest snapshot.

* Fri May 06 2016 Fabio Valentini <decathorpe@gmail.com> - 0.3.1.1~rev904-1
- Update to latest snapshot.

* Wed May 04 2016 Fabio Valentini <decathorpe@gmail.com> - 0.3.1.1~rev902-1
- Update to latest snapshot.

* Wed May 04 2016 Fabio Valentini <decathorpe@gmail.com> - 0.3.1.1~rev902-1
- Update to latest snapshot.

* Tue May 03 2016 Fabio Valentini <decathorpe@gmail.com> - 0.3.1.1~rev901-1
- Update to latest snapshot.

* Mon May 02 2016 Fabio Valentini <decathorpe@gmail.com> - 0.3.1.1~rev900-2
- Update for packaging changes.

* Tue Apr 26 2016 Fabio Valentini <decathorpe@gmail.com> - 0.3.1.1~rev900-1
- Update to new upstream snapshot.

* Sun Apr 24 2016 Fabio Valentini <decathorpe@gmail.com> - 0.3.1.1~rev898-1
- Update to new upstream snapshot.

* Thu Apr 14 2016 Fabio Valentini <decathorpe@gmail.com> - 0.3.1.1~rev897-1
- Update to new upstream snapshot.

* Wed Apr 13 2016 Fabio Valentini <decathorpe@gmail.com> - 0.3.1.1~rev896-1
- Update to new upstream snapshot.

* Thu Mar 24 2016 Fabio Valentini <decathorpe@gmail.com> - 0.3.1.1~rev895-1
- Update to new upstream snapshot.

* Tue Mar 15 2016 Fabio Valentini <decathorpe@gmail.com> - 0.3.1.1~rev894-1
- Update to new upstream snapshot.

* Mon Mar 14 2016 Fabio Valentini <decathorpe@gmail.com> - 0.3.1.1~rev893-1
- Update to new upstream snapshot.

* Sun Mar 13 2016 Fabio Valentini <decathorpe@gmail.com> - 0.3.1.1~rev892-1
- Update to new upstream snapshot.

* Thu Mar 10 2016 Fabio Valentini <decathorpe@gmail.com> - 0.3.1.1~rev891-1
- Update to new upstream snapshot.

* Wed Mar 09 2016 Fabio Valentini <decathorpe@gmail.com> - 0.3.1.1~rev890-1
- Update to new upstream snapshot.

* Tue Mar 08 2016 Fabio Valentini <decathorpe@gmail.com> - 0.3.1.1~rev889-1
- Update to new upstream snapshot.

* Sat Mar 05 2016 Fabio Valentini <decathorpe@gmail.com> - 0.3.1.1~rev888-1
- Update to new upstream snapshot.

* Mon Feb 29 2016 Fabio Valentini <decathorpe@gmail.com> - 0.3.1.1~rev887-1
- Update to new upstream snapshot.

* Tue Feb 23 2016 Fabio Valentini <decathorpe@gmail.com> - 0.3.1.1~rev885-1
- Update to new upstream snapshot.

* Mon Feb 22 2016 Fabio Valentini <decathorpe@gmail.com> - 0.3.1.1~rev884-1
- Update to new upstream snapshot.

* Thu Feb 18 2016 Fabio Valentini <decathorpe@gmail.com> - 0.3.1.1~rev883-1
- Update to new upstream snapshot.

* Sat Feb 13 2016 Fabio Valentini <decathorpe@gmail.com> - 0.3.1.1~rev882-1
- Update to new upstream snapshot.

* Thu Feb 11 2016 Fabio Valentini <decathorpe@gmail.com> - 0.3.1.1~rev881-1
- Update to new upstream snapshot.

* Sat Feb 06 2016 Fabio Valentini <decathorpe@gmail.com> - 0.3.1.1~rev880-1
- Update to new upstream snapshot.

* Thu Feb 04 2016 Fabio Valentini <decathorpe@gmail.com> - 0.3.1.1~rev879-1
- Update to new upstream snapshot.

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



