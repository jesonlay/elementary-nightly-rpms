Name:           maya-calendar
Summary:        The official elementary calendar
Version:        0.4.0.2+rev%{rev}
Release:        1%{?dist}
License:        GPLv3+
URL:            https://launchpad.net/maya

Source0:        %{name}-%{version}.tar.gz

# Include the appropriate icon from elementary-icon-theme so appdata metadata generation works.
# A Bug about the missing icon is reported upstream:
# https://bugs.launchpad.net/maya/+bug/1658325

Source1:        org.pantheon.maya.svg

Source2:        %{name}.conf

# Patch the .desktop file to not use the generic icon name but the bundled icon
Patch0:         00-rename-icon.patch


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
BuildRequires:  pkgconfig(granite)
BuildRequires:  pkgconfig(gthread-2.0)
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.11.6
BuildRequires:  pkgconfig(libecal-1.2) >= 3.8.0
BuildRequires:  pkgconfig(libical)

# maya-calendar also provides a generic symbolic icon (actions/calendar-go-today)
Requires:       hicolor-icon-theme


%description
A slim, lightweight GTK+3 calendar app written in Vala, designed for
elementary OS. Also looks and works great on other GTK+ desktops.

In elementary OS, Maya is known as Calendar.


%package        devel
Summary:        The official elementary calendar (devel files)
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description    devel
A slim, lightweight GTK+3 calendar app written in Vala, designed for
elementary OS. Also looks and works great on other GTK+ desktops.

In elementary OS, Maya is known as Calendar.

This package contains the development files.


%prep
%autosetup -p1


%build
mkdir build && pushd build
%cmake -DBUILD_FOR_ELEMENTARY:BOOL=OFF ..
%make_build
popd


%install
pushd build
%make_install
popd

%find_lang maya-calendar

mkdir -p %{buildroot}/%{_datadir}/icons/hicolor/scalable/apps
cp -p %{SOURCE1} %{buildroot}/%{_datadir}/icons/hicolor/scalable/apps/


%check
desktop-file-validate %{buildroot}/%{_datadir}/applications/org.pantheon.maya.desktop
desktop-file-validate %{buildroot}/%{_datadir}/applications/org.pantheon.maya-daemon.desktop

appstream-util validate-relax --nonet %{buildroot}/%{_datadir}/appdata/org.pantheon.maya.appdata.xml


%post
/sbin/ldconfig
/bin/touch --no-create %{_datadir}/icons/hicolor &>/dev/null || :

%postun
/sbin/ldconfig

if [ $1 -eq 0 ] ; then
    /bin/touch --no-create %{_datadir}/icons/hicolor &>/dev/null
    /usr/bin/gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :
fi

%posttrans
/usr/bin/gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :


%files -f maya-calendar.lang
%doc AUTHORS README.md
%license COPYING

%{_bindir}/maya-calendar
%{_bindir}/maya-calendar-daemon

%{_libdir}/libmaya-calendar.so.0
%{_libdir}/libmaya-calendar.so.0.1
%{_libdir}/maya-calendar/

%{_datadir}/appdata/org.pantheon.maya.appdata.xml
%{_datadir}/applications/org.pantheon.maya.desktop
%{_datadir}/applications/org.pantheon.maya-daemon.desktop
%{_datadir}/glib-2.0/schemas/org.pantheon.maya.gschema.xml
%{_datadir}/icons/hicolor/scalable/actions/calendar-go-today.svg
%{_datadir}/icons/hicolor/scalable/apps/org.pantheon.maya.svg
%{_datadir}/maya-calendar/


%files          devel
%{_includedir}/maya-calendar/

%{_libdir}/libmaya-calendar.so
%{_libdir}/pkgconfig/maya-calendar.pc

%{_datadir}/vala/vapi/maya-calendar.deps
%{_datadir}/vala/vapi/maya-calendar.vapi


%changelog
* Sat Jul 01 2017 Fabio Valentini <decathorpe@gmail.com> - 0.4.0.2+rev1047-1
- Update to latest snapshot.

* Sun Jun 18 2017 Fabio Valentini <decathorpe@gmail.com> - 0.4.0.2+rev1044-1
- Update to latest snapshot.

* Tue Jun 06 2017 Fabio Valentini <decathorpe@gmail.com> - 0.4.0.2+rev1039-1
- Update to latest snapshot.

* Mon May 08 2017 Fabio Valentini <decathorpe@gmail.com> - 0.4.0.2+rev1032-1
- Update to latest snapshot.

* Fri May 05 2017 Fabio Valentini <decathorpe@gmail.com> - 0.4.0.2+rev1014-1
- Update to latest snapshot.

* Fri Apr 28 2017 Fabio Valentini <decathorpe@gmail.com> - 0.4.0.2+rev1013-1
- Update to latest snapshot.

* Tue Apr 25 2017 Fabio Valentini <decathorpe@gmail.com> - 0.4.0.2+rev1012-2
- Adapt to upstream changes.

* Tue Apr 25 2017 Fabio Valentini <decathorpe@gmail.com> - 0.4.0.2+rev1012-1
- Update to latest snapshot.

* Wed Apr 12 2017 Fabio Valentini <decathorpe@gmail.com> - 0.4.0.2+rev1010-1
- Update to latest snapshot.

* Fri Apr 07 2017 Fabio Valentini <decathorpe@gmail.com> - 0.4.0.2+rev1009-1
- Update to latest snapshot.

* Wed Mar 22 2017 Fabio Valentini <decathorpe@gmail.com> - 0.4.0.2+rev1008-1
- Update to latest snapshot.

* Mon Mar 20 2017 Fabio Valentini <decathorpe@gmail.com> - 0.4.0.2+rev1007-1
- Update to latest snapshot.

* Sun Mar 19 2017 Fabio Valentini <decathorpe@gmail.com> - 0.4.0.2+rev1006-1
- Update to latest snapshot.

* Wed Mar 15 2017 Fabio Valentini <decathorpe@gmail.com> - 0.4.0.2+rev1005-1
- Update to latest snapshot.

* Fri Mar 03 2017 Fabio Valentini <decathorpe@gmail.com> - 0.4.0.2+rev1004-1
- Update to latest snapshot.

* Tue Feb 28 2017 Fabio Valentini <decathorpe@gmail.com> - 0.4.0.2+rev1003-1
- Update to latest snapshot.

* Mon Feb 27 2017 Fabio Valentini <decathorpe@gmail.com> - 0.4.0.2+rev1002-1
- Update to latest snapshot.

* Sat Feb 25 2017 Fabio Valentini <decathorpe@gmail.com> - 0.4.0.2+rev1001-1
- Update to latest snapshot.

* Thu Feb 23 2017 Fabio Valentini <decathorpe@gmail.com> - 0.4.0.2+rev1000-1
- Update to latest snapshot.

* Wed Feb 22 2017 Fabio Valentini <decathorpe@gmail.com> - 0.4.0.2+rev999-1
- Update to latest snapshot.

* Sat Feb 11 2017 Fabio Valentini <decathorpe@gmail.com> - 0.4.0.2+rev998-1
- Update to latest snapshot.

* Fri Feb 10 2017 Fabio Valentini <decathorpe@gmail.com> - 0.4.0.2+rev997-1
- Update to latest snapshot.

* Thu Feb 09 2017 Fabio Valentini <decathorpe@gmail.com> - 0.4.0.2+rev996-1
- Update to latest snapshot.

* Wed Feb 08 2017 Fabio Valentini <decathorpe@gmail.com> - 0.4.0.2+rev995-2
- Sync spec with the fedora package.

* Mon Jan 30 2017 Fabio Valentini <decathorpe@gmail.com> - 0.4.0.2+rev995-1
- Update to latest snapshot.

* Sun Jan 29 2017 Fabio Valentini <decathorpe@gmail.com> - 0.4.0.2+rev994-1
- Update to latest snapshot.

* Sat Jan 28 2017 Fabio Valentini <decathorpe@gmail.com> - 0.4.0.2+rev993-1
- Update to latest snapshot.

* Wed Jan 25 2017 Fabio Valentini <decathorpe@gmail.com> - 0.4.0.2+rev992-1
- Update to latest snapshot.

* Mon Jan 23 2017 Fabio Valentini <decathorpe@gmail.com> - 0.4.0.2+rev991-1
- Update to latest snapshot.

* Sun Jan 22 2017 Fabio Valentini <decathorpe@gmail.com> - 0.4.0.2+rev990-1
- Update to latest snapshot.

* Sat Jan 21 2017 Fabio Valentini <decathorpe@gmail.com> - 0.4.0.2+rev989-1
- Update to latest snapshot.

* Sat Jan 07 2017 Fabio Valentini <decathorpe@gmail.com> - 0.4.0.2+rev988-1
- Update to version 0.4.0.2.

* Fri Jan 06 2017 Fabio Valentini <decathorpe@gmail.com> - 0.4.0.2+rev987-1
- Update to version 0.4.0.2.

* Wed Jan 04 2017 Fabio Valentini <decathorpe@gmail.com> - 0.4.0.2+rev986-1
- Update to version 0.4.0.2.

* Tue Jan 03 2017 Fabio Valentini <decathorpe@gmail.com> - 0.4.0.2+rev985-1
- Update to version 0.4.0.2.

* Mon Jan 02 2017 Fabio Valentini <decathorpe@gmail.com> - 0.4.0.2+rev984-1
- Update to latest snapshot.

* Sun Jan 01 2017 Fabio Valentini <decathorpe@gmail.com> - 0.4.0.2+rev983-1
- Update to latest snapshot.

* Wed Dec 28 2016 Fabio Valentini <decathorpe@gmail.com> - 0.4.0.2+rev982-1
- Update to latest snapshot.

* Sun Dec 04 2016 Fabio Valentini <decathorpe@gmail.com> - 0.4.0.2+rev981-1
- Update to latest snapshot.

* Sat Nov 19 2016 Fabio Valentini <decathorpe@gmail.com> - 0.4.0.2+rev980-1
- Update to latest snapshot.

* Fri Nov 18 2016 Fabio Valentini <decathorpe@gmail.com> - 0.4.0.2+rev979-1
- Update to latest snapshot.

* Tue Nov 08 2016 Fabio Valentini <decathorpe@gmail.com> - 0.4.0.2+rev978-1
- Update to latest snapshot.

* Mon Nov 07 2016 Fabio Valentini <decathorpe@gmail.com> - 0.4.0.2+rev977-1
- Update to latest snapshot.

* Tue Nov 01 2016 Fabio Valentini <decathorpe@gmail.com> - 0.4.0.2+rev976-1
- Update to latest snapshot.

* Mon Oct 31 2016 Fabio Valentini <decathorpe@gmail.com> - 0.4.0.2+rev975-1
- Update to latest snapshot.

* Mon Oct 31 2016 Fabio Valentini <decathorpe@gmail.com> - 0.4.0.2+rev974-1
- Update to latest snapshot.

* Fri Oct 21 2016 Fabio Valentini <decathorpe@gmail.com> - 0.4.0.2+rev970-1
- Update to latest snapshot.

* Thu Oct 20 2016 Fabio Valentini <decathorpe@gmail.com> - 0.4.0.2+rev969-1
- Update to latest snapshot.

* Wed Oct 19 2016 Fabio Valentini <decathorpe@gmail.com> - 0.4.0.2+rev968-1
- Update to latest snapshot.

* Sun Oct 09 2016 Fabio Valentini <decathorpe@gmail.com> - 0.4.0.2+rev967-1
- Update to latest snapshot.

* Fri Sep 30 2016 Fabio Valentini <decathorpe@gmail.com> - 0.4.0.2+rev966-1
- Update to latest snapshot.

* Thu Sep 29 2016 Fabio Valentini <decathorpe@gmail.com> - 0.4.0.2+rev965-2
- Spec file cleanups.

* Fri Sep 23 2016 Fabio Valentini <decathorpe@gmail.com> - 0.4.0.2+rev965-1
- Update to latest snapshot.

* Thu Sep 22 2016 Fabio Valentini <decathorpe@gmail.com> - 0.4.0.2+rev964-1
- Update to version 0.4.0.2.

* Fri Sep 16 2016 Fabio Valentini <decathorpe@gmail.com> - 0.4.0.2~rev963-2
- Update for packaging changes.

* Fri Sep 16 2016 Fabio Valentini <decathorpe@gmail.com>
- Adapt spec for renamed appdata and desktop files.

* Fri Sep 16 2016 Fabio Valentini <decathorpe@gmail.com> - 0.4.0.2~rev963-1
- Update to latest snapshot.

* Thu Sep 15 2016 Fabio Valentini <decathorpe@gmail.com> - 0.4.0.2~rev962-1
- Update to latest snapshot.

* Wed Sep 14 2016 Fabio Valentini <decathorpe@gmail.com> - 0.4.0.2~rev961-1
- Update to latest snapshot.

* Fri Sep 09 2016 Fabio Valentini <decathorpe@gmail.com> - 0.4.0.2~rev960-1
- Update to latest snapshot.

* Thu Sep 08 2016 Fabio Valentini <decathorpe@gmail.com> - 0.4.0.2~rev959-1
- Update to version 0.4.0.2.

* Tue Sep 06 2016 Fabio Valentini <decathorpe@gmail.com> - 0.4.0.1~rev958-1
- Update to latest snapshot.

* Sun Sep 04 2016 Fabio Valentini <decathorpe@gmail.com> - 0.4.0.1~rev957-1
- Update to latest snapshot.

* Sun Sep 04 2016 Fabio Valentini <decathorpe@gmail.com> - 0.4.0.1~rev956-1
- Update to latest snapshot.

* Sun Sep 04 2016 Fabio Valentini <decathorpe@gmail.com> - 0.4.0.1~rev955-1
- Update to latest snapshot.

* Fri Sep 02 2016 Fabio Valentini <decathorpe@gmail.com> - 0.4.0.1~rev954-1
- Update to latest snapshot.

* Sun Aug 28 2016 Fabio Valentini <decathorpe@gmail.com> - 0.4.0.1~rev953-1
- Update to latest snapshot.

* Fri Aug 26 2016 Fabio Valentini <decathorpe@gmail.com> - 0.4.0.1~rev952-1
- Update to latest snapshot.

* Thu Aug 25 2016 Fabio Valentini <decathorpe@gmail.com> - 0.4.0.1~rev951-1
- Update to latest snapshot.

* Thu Aug 18 2016 Fabio Valentini <decathorpe@gmail.com> - 0.4.0.1~rev950-1
- Update to version 0.4.0.1.

* Mon Aug 15 2016 Fabio Valentini <decathorpe@gmail.com> - 0.4~rev949-2
- Update for packaging changes.

* Mon Aug 15 2016 Fabio Valentini <decathorpe@gmail.com>
- Add new css files and icon to spec.

* Mon Aug 15 2016 Fabio Valentini <decathorpe@gmail.com> - 0.4~rev949-1
- Update to latest snapshot.

* Sun Aug 14 2016 Fabio Valentini <decathorpe@gmail.com> - 0.4~rev948-1
- Update to version 0.4.

* Sun Aug 14 2016 Fabio Valentini <decathorpe@gmail.com> - 0.3.1.1~rev946-1
- Update to latest snapshot.

* Sat Aug 13 2016 Fabio Valentini <decathorpe@gmail.com> - 0.3.1.1~rev945-1
- Update to latest snapshot.

* Thu Aug 11 2016 Fabio Valentini <decathorpe@gmail.com> - 0.3.1.1~rev944-1
- Update to latest snapshot.

* Thu Aug 11 2016 Fabio Valentini <decathorpe@gmail.com> - 0.3.1.1~rev943-1
- Update to latest snapshot.

* Tue Aug 09 2016 Fabio Valentini <decathorpe@gmail.com> - 0.3.1.1~rev942-1
- Update to latest snapshot.

* Sun Aug 07 2016 Fabio Valentini <decathorpe@gmail.com> - 0.3.1.1~rev941-2
- Update for packaging changes.

* Sun Aug 07 2016 Fabio Valentini <decathorpe@gmail.com> - 0.3.1.1~rev941-1
- Update to latest snapshot.

* Sat Aug 06 2016 Fabio Valentini <decathorpe@gmail.com> - 0.3.1.1~rev940-1
- Update to latest snapshot.

* Fri Aug 05 2016 Fabio Valentini <decathorpe@gmail.com> - 0.3.1.1~rev939-1
- Update to latest snapshot.

* Thu Aug 04 2016 Fabio Valentini <decathorpe@gmail.com> - 0.3.1.1~rev938-1
- Update to latest snapshot.

* Tue Aug 02 2016 Fabio Valentini <decathorpe@gmail.com> - 0.3.1.1~rev936-1
- Update to latest snapshot.

* Fri Jul 29 2016 Fabio Valentini <decathorpe@gmail.com> - 0.3.1.1~rev935-1
- Update to latest snapshot.

* Thu Jul 28 2016 Fabio Valentini <decathorpe@gmail.com> - 0.3.1.1~rev934-1
- Update to latest snapshot.

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

* Fri Jun 03 2016 Fabio Valentini <decathorpe@gmail.com> - 0.3.1.1~rev910-2
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


