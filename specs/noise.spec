Summary:        The official elementary music player
Name:           noise
Version:        0.3.1~rev%{rev}
Release:        1%{?dist}
License:        GPLv3
URL:            http://launchpad.net/noise

Source0:        %{name}-%{version}.tar.gz
Source1:        %{name}.conf

BuildRequires:  cmake
BuildRequires:  desktop-file-utils
BuildRequires:  gettext
BuildRequires:  intltool
BuildRequires:  libappstream-glib
BuildRequires:  pkgconfig
BuildRequires:  vala

BuildRequires:  pkgconfig(gee-0.8)
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(glib-2.0) >= 2.32
BuildRequires:  pkgconfig(granite)
BuildRequires:  pkgconfig(gstreamer-1.0)
BuildRequires:  pkgconfig(gstreamer-pbutils-1.0)
BuildRequires:  pkgconfig(gstreamer-tag-1.0)
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.11.6
BuildRequires:  pkgconfig(libgda-5.0)
BuildRequires:  pkgconfig(libnotify)
BuildRequires:  pkgconfig(libpeas-1.0)
BuildRequires:  pkgconfig(libpeas-gtk-1.0)
BuildRequires:  pkgconfig(taglib_c)
BuildRequires:  pkgconfig(zeitgeist-2.0)

Requires:       hicolor-icon-theme
Requires:       libgda-sqlite


%description
Noise is a fast and beautiful GTK3 audio player with a focus on music and libraries. It handles external devices, CDs, and album art. Noise utilizes Granite for a consistent and slick UI.

In elementary OS, Noise is known as Music.


%package        devel
Summary:        noise development headers
%description    devel
Noise is a fast and beautiful GTK3 audio player with a focus on music and libraries. It handles external devices, CDs, and album art. Noise utilizes Granite for a consistent and slick UI.

In elementary OS, Noise is known as Music.

This package contains files needed for developing with noise.


%prep
%autosetup


%build
%cmake
%make_build


%install
%make_install
%find_lang noise


%check
# desktop-file-validate $RPM_BUILD_ROOT/%{_datadir}/applications/*.desktop
# appstream-util validate-relax --nonet $RPM_BUILD_ROOT/%{_datadir}/appdata/*.appdata.xml


%clean
rm -rf %{buildroot}


%post
/sbin/ldconfig
/usr/bin/update-desktop-database &> /dev/null || :
/bin/touch --no-create %{_datadir}/icons/hicolor &>/dev/null || :

%postun
/sbin/ldconfig
/usr/bin/update-desktop-database &> /dev/null || :
if [ $1 -eq 0 ] ; then
    /bin/touch --no-create %{_datadir}/icons/hicolor &>/dev/null
    /usr/bin/glib-compile-schemas %{_datadir}/glib-2.0/schemas &> /dev/null || :
    /usr/bin/gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :
fi

%posttrans
/usr/bin/glib-compile-schemas %{_datadir}/glib-2.0/schemas &> /dev/null || :
/usr/bin/gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :


%post           devel -p /usr/sbin/ldconfig
%postun         devel -p /usr/sbin/ldconfig


%files       -f noise.lang
%doc AUTHORS NEWS README
%license COPYING

%{_bindir}/noise

%{_libdir}/libnoise-core.so.0
%{_libdir}/libnoise-core.so.0.1

%{_libdir}/noise/

%{_datadir}/appdata/noise.appdata.xml
%{_datadir}/applications/org.pantheon.noise.desktop
%{_datadir}/glib-2.0/schemas/org.pantheon.noise.gschema.xml
%{_datadir}/icons/hicolor/*/apps/multimedia-audio-player.svg
%{_datadir}/noise/


%files          devel
%{_libdir}/libnoise-core.so
%{_libdir}/pkgconfig/noise-core.pc

%{_includedir}/noise-core/

%{_datadir}/vala/vapi/noise-core.deps
%{_datadir}/vala/vapi/noise-core.vapi


%changelog
* Mon Jul 11 2016 Fabio Valentini <decathorpe@gmail.com> - 0.3.1~rev1952-1
- Update to latest snapshot.

* Sat Jul 09 2016 Fabio Valentini <decathorpe@gmail.com> - 0.3.1~rev1950-1
- Update to latest snapshot.

* Fri Jul 08 2016 Fabio Valentini <decathorpe@gmail.com> - 0.3.1~rev1949-1
- Update to latest snapshot.

* Thu Jul 07 2016 Fabio Valentini <decathorpe@gmail.com> - 0.3.1~rev1948-1
- Update to latest snapshot.

* Wed Jul 06 2016 Fabio Valentini <decathorpe@gmail.com> - 0.3.1~rev1947-2
- Update for packaging changes.

* Wed Jul 06 2016 Fabio Valentini <decathorpe@gmail.com> - 0.3.1~rev1947-1
- Update to latest snapshot.

* Tue Jul 05 2016 Fabio Valentini <decathorpe@gmail.com> - 0.3.1~rev1946-1
- Update to latest snapshot.

* Mon Jul 04 2016 Fabio Valentini <decathorpe@gmail.com> - 0.3.1~rev1945-1
- Update to latest snapshot.

* Sun Jul 03 2016 Fabio Valentini <decathorpe@gmail.com> - 0.3.1~rev1944-1
- Update to latest snapshot.

* Sat Jul 02 2016 Fabio Valentini <decathorpe@gmail.com> - 0.3.1~rev1943-1
- Update to latest snapshot.

* Fri Jul 01 2016 Fabio Valentini <decathorpe@gmail.com> - 0.3.1~rev1942-1
- Update to latest snapshot.

* Thu Jun 30 2016 Fabio Valentini <decathorpe@gmail.com> - 0.3.1~rev1941-1
- Update to latest snapshot.

* Thu Jun 23 2016 Fabio Valentini <decathorpe@gmail.com> - 0.3.1~rev1940-1
- Update to latest snapshot.

* Tue Jun 21 2016 Fabio Valentini <decathorpe@gmail.com> - 0.3.1~rev1939-1
- Update to latest snapshot.

* Sat Jun 18 2016 Fabio Valentini <decathorpe@gmail.com> - 0.3.1~rev1938-1
- Update to latest snapshot.

* Fri Jun 17 2016 Fabio Valentini <decathorpe@gmail.com> - 0.3.1~rev1937-1
- Update to latest snapshot.

* Thu Jun 16 2016 Fabio Valentini <decathorpe@gmail.com> - 0.3.1~rev1936-1
- Update to latest snapshot.

* Wed Jun 15 2016 Fabio Valentini <decathorpe@gmail.com> - 0.3.1~rev1935-1
- Update to latest snapshot.

* Tue Jun 14 2016 Fabio Valentini <decathorpe@gmail.com> - 0.3.1~rev1934-1
- Update to latest snapshot.

* Tue Jun 14 2016 Fabio Valentini <decathorpe@gmail.com> - 0.3.1~rev1933-1
- Update to latest snapshot.

* Thu Jun 09 2016 Fabio Valentini <decathorpe@gmail.com> - 0.3.1~rev1932-1
- Update to latest snapshot.

* Tue Jun 07 2016 Fabio Valentini <decathorpe@gmail.com> - 0.3.1~rev1931-2
- Update for packaging changes.

* Tue Jun 07 2016 Fabio Valentini <decathorpe@gmail.com> - 0.3.1~rev1931-1
- Update to latest snapshot.

* Sun Jun 05 2016 Fabio Valentini <decathorpe@gmail.com> - 0.3.1~rev1930-1
- Update to latest snapshot.

* Sat Jun 04 2016 Fabio Valentini <decathorpe@gmail.com> - 0.3.1~rev1929-1
- Update to latest snapshot.

* Fri Jun 03 2016 Fabio Valentini <decathorpe@gmail.com> - 0.3.1~rev1928-1
- Update to latest snapshot.

* Thu Jun 02 2016 Fabio Valentini <decathorpe@gmail.com> - 0.3.1~rev1927-1
- Update to latest snapshot.

* Mon May 30 2016 Fabio Valentini <decathorpe@gmail.com> - 0.3.1~rev1926-3
- Update for packaging changes.

* Sun May 29 2016 Fabio Valentini <decathorpe@gmail.com> - 0.3.1~rev1926-2
- Update for packaging changes.

* Sat May 28 2016 Fabio Valentini <decathorpe@gmail.com> - 0.3.1~rev1926-1
- Update to latest snapshot.

* Fri May 27 2016 Fabio Valentini <decathorpe@gmail.com> - 0.3.1~rev1925-1
- Update to latest snapshot.

* Thu May 26 2016 Fabio Valentini <decathorpe@gmail.com> - 0.3.1~rev1924-1
- Update to latest snapshot.

* Wed May 25 2016 Fabio Valentini <decathorpe@gmail.com> - 0.3.1~rev1923-1
- Update to latest snapshot.

* Tue May 24 2016 Fabio Valentini <decathorpe@gmail.com> - 0.3.1~rev1922-1
- Update to latest snapshot.

* Sun May 08 2016 Fabio Valentini <decathorpe@gmail.com> - 0.3.1~rev1921-1
- Update to latest snapshot.

* Sat May 07 2016 Fabio Valentini <decathorpe@gmail.com> - 0.3.1~rev1920-1
- Update to latest snapshot.

* Wed May 04 2016 Fabio Valentini <decathorpe@gmail.com> - 0.3.1~rev1919-1
- Update to latest snapshot.

* Mon May 02 2016 Fabio Valentini <decathorpe@gmail.com> - 0.3.1~rev1919-2
- Update for packaging changes.

* Sat Apr 30 2016 Fabio Valentini <decathorpe@gmail.com> - 0.3.1~rev1919-1
- Update to new upstream snapshot.

* Sat Apr 23 2016 Fabio Valentini <decathorpe@gmail.com> - 0.3.1~rev1918-1
- Update to new upstream snapshot.

* Sun Apr 17 2016 Fabio Valentini <decathorpe@gmail.com> - 0.3.1~rev1917-1
- Update to new upstream snapshot.

* Thu Mar 24 2016 Fabio Valentini <decathorpe@gmail.com> - 0.3.1~rev1916-1
- Update to new upstream snapshot.

* Mon Mar 21 2016 Fabio Valentini <decathorpe@gmail.com> - 0.3.1~rev1915-1
- Update to new upstream snapshot.

* Sat Mar 19 2016 Fabio Valentini <decathorpe@gmail.com> - 0.3.1~rev1913-1
- Update to new upstream snapshot.

* Tue Mar 15 2016 Fabio Valentini <decathorpe@gmail.com> - 0.3.1~rev1912-1
- Update to new upstream snapshot.

* Mon Mar 14 2016 Fabio Valentini <decathorpe@gmail.com> - 0.3.1~rev1911-1
- Update to new upstream snapshot.

* Sun Mar 13 2016 Fabio Valentini <decathorpe@gmail.com> - 0.3.1~rev1910-1
- Update to new upstream snapshot.

* Fri Mar 04 2016 Fabio Valentini <decathorpe@gmail.com> - 0.3.1~rev1909-1
- Update to new upstream snapshot.

* Wed Mar 02 2016 Fabio Valentini <decathorpe@gmail.com> - 0.3.1~rev1908-1
- Update to new upstream snapshot.

* Tue Mar 01 2016 Fabio Valentini <decathorpe@gmail.com> - 0.3.1~rev1907-1
- Update to new upstream snapshot.

* Tue Feb 23 2016 Fabio Valentini <decathorpe@gmail.com> - 0.3.1~rev1906-1
- Update to new upstream snapshot.

* Sat Feb 20 2016 Fabio Valentini <decathorpe@gmail.com> - 0.3.1~rev1905-1
- Update to new upstream snapshot.

* Thu Feb 18 2016 Fabio Valentini <decathorpe@gmail.com> - 0.3.1~rev1904-1
- Update to new upstream snapshot.

* Mon Feb 15 2016 Fabio Valentini <decathorpe@gmail.com> - 0.3.1~rev1903-1
- Update to new upstream snapshot.

* Sat Feb 13 2016 Fabio Valentini <decathorpe@gmail.com> - 0.3.1~rev1902-1
- Update to new upstream snapshot.

* Thu Feb 11 2016 Fabio Valentini <decathorpe@gmail.com> - 0.3.1~rev1899-1
- Update to new upstream snapshot.

* Mon Feb 08 2016 Fabio Valentini <decathorpe@gmail.com> - 0.3.1~rev1897-1
- Update to new upstream snapshot.

* Sat Feb 06 2016 Fabio Valentini <decathorpe@gmail.com> - 0.3.1~rev1894-1
- Update to new upstream snapshot.

* Wed Feb 03 2016 Fabio Valentini <decathorpe@gmail.com> - 0.3.1~rev1893-1
- Update to new upstream snapshot.

* Tue Feb 02 2016 Fabio Valentini <decathorpe@gmail.com> - 0.3.1~rev1892-1
- Update to new upstream snapshot.

* Mon Feb 01 2016 Fabio Valentini <decathorpe@gmail.com> - 0.3.1~rev1891-1
- Update to new upstream snapshot.

* Tue Jan 26 2016 Fabio Valentini <decathorpe@gmail.com> - 0.3.1~rev1890-2
- Add BR:intltool to fix build. Clean up spec.

* Sun Jan 24 2016 Fabio Valentini <decathorpe@gmail.com> - 0.3.1~rev1890-1
- Update to new upstream snapshot.

* Wed Jan 13 2016 Fabio Valentini <decathorpe@gmail.com> - 0.3.1~rev1888-1
- Update to new upstream snapshot.

* Tue Jan 12 2016 Fabio Valentini <decathorpe@gmail.com> - 0.3.1~rev1887-1
- Update to new upstream snapshot.

* Mon Jan 11 2016 Fabio Valentini <decathorpe@gmail.com> - 0.3.1~rev1885-1
- Update to new upstream snapshot.

* Sat Jan 09 2016 Fabio Valentini <decathorpe@gmail.com> - 0.3.1~rev1883-1
- Update to new upstream snapshot.

* Fri Jan 08 2016 Fabio Valentini <decathorpe@gmail.com> - 0.3.1~rev1882-1
- Update to new upstream snapshot.

* Thu Jan 07 2016 Fabio Valentini <decathorpe@gmail.com> - 0.3.1~rev1881-1
- Update to new upstream snapshot.

* Wed Jan 06 2016 Fabio Valentini <decathorpe@gmail.com> - 0.3.1~rev1880-1
- Update to new upstream snapshot.

* Tue Jan 05 2016 Fabio Valentini <decathorpe@gmail.com> - 0.3.1~rev1879-1
- Update to new upstream snapshot.

* Mon Jan 04 2016 Fabio Valentini <decathorpe@gmail.com> - 0.3.1~rev1877-1
- Update to new upstream snapshot.

* Sun Jan 03 2016 Fabio Valentini <decathorpe@gmail.com> - 0.3.1~rev1875-1
- Update to new upstream snapshot.

* Mon Dec 28 2015 Fabio Valentini <decathorpe@gmail.com> - 0.3.1~rev1874-1
- Update to new upstream snapshot.

* Sat Dec 26 2015 Fabio Valentini <decathorpe@gmail.com> - 0.3.1~rev1873-1
- Update to new upstream snapshot.

* Wed Dec 23 2015 Fabio Valentini <decathorpe@gmail.com> - 0.3.1~rev1871-1
- Update to new upstream snapshot.

* Tue Dec 22 2015 Fabio Valentini <decathorpe@gmail.com> - 0.3.1~rev1870-1
- Update to new upstream snapshot.

* Mon Dec 21 2015 Fabio Valentini <decathorpe@gmail.com> - 0.3.1~rev1868-1
- Update to new upstream snapshot.

* Sun Dec 20 2015 Fabio Valentini <decathorpe@gmail.com> - 0.3.1~rev1867-1
- Update to new upstream snapshot.

* Sat Dec 19 2015 Fabio Valentini <decathorpe@gmail.com> - 0.3.1~rev1866-1
- Update to new upstream snapshot.

* Fri Dec 18 2015 Fabio Valentini <decathorpe@gmail.com> - 0.3.1~rev1865-1
- Update to new upstream snapshot.

* Thu Dec 17 2015 Fabio Valentini <decathorpe@gmail.com> - 0.3.1~rev1864-1
- Update to new upstream snapshot.

* Wed Dec 16 2015 Fabio Valentini <decathorpe@gmail.com> - 0.3.1~rev1863-1
- Update to new upstream snapshot.

* Sun Dec 13 2015 Fabio Valentini <decathorpe@gmail.com> - 0.3.1~rev1862-2
- Remove (not even working) last.fm support. Remove BRs: libaccounts,
  libgsignon-glib, dbusmenu-glib, ...

* Sun Dec 13 2015 Fabio Valentini <decathorpe@gmail.com> - 0.3.1~rev1862-1
- Update to new upstream snapshot.

* Sun Dec 13 2015 Fabio Valentini <decathorpe@gmail.com> - 0.3.1~rev1861-2
- fix build. add appdata file and check to spec.

* Sat Dec 12 2015 Fabio Valentini <decathorpe@gmail.com> - 0.3.1~rev1861-1
- Update to new upstream snapshot.

* Fri Dec 11 2015 Fabio Valentini <decathorpe@gmail.com> - 0.3.1~rev1860-1
- Update to new upstream snapshot.

* Tue Dec 08 2015 Fabio Valentini <decathorpe@gmail.com> - 0.3.1~rev1859-1
- Update to new upstream snapshot.

* Mon Dec 07 2015 Fabio Valentini <decathorpe@gmail.com> - 0.3.1~rev1858-1
- Update to new upstream snapshot.

* Sun Dec 06 2015 Fabio Valentini <decathorpe@gmail.com> - 0.3.1~rev1857-1
- Update to new upstream snapshot.

* Mon Nov 30 2015 Fabio Valentini <decathorpe@gmail.com> - 0.3.1~rev1856-1
- Update to new upstream snapshot.

* Sun Nov 29 2015 Fabio Valentini <decathorpe@gmail.com> - 0.3.1~rev1855-1
- Update to new upstream snapshot.

* Wed Nov 18 2015 Fabio Valentini <decathorpe@gmail.com> - 0.3.1~rev1854-1
- Update to new upstream snapshot.

* Fri Nov 13 2015 Fabio Valentini <decathorpe@gmail.com> - 0.3.1~rev1853-1
- Update to new upstream snapshot.

* Wed Nov 04 2015 Fabio Valentini <decathorpe@gmail.com> - 0.3.1~rev1852-1
- Update to new upstream snapshot.

* Mon Nov 02 2015 Fabio Valentini <decathorpe@gmail.com> - 0.3.1~rev1851-1
- Update to new upstream snapshot.

* Sat Oct 31 2015 Fabio Valentini <decathorpe@gmail.com> - 0.3.1~rev1849-1
- Update to new upstream snapshot.

* Thu Oct 22 2015 Fabio Valentini <decathorpe@gmail.com> - 0.3.1~rev1848-1
- Update to new upstream snapshot.

* Wed Oct 21 2015 Fabio Valentini <decathorpe@gmail.com> - 0.3.1~rev1847-1
- Update to new upstream snapshot.

* Tue Oct 20 2015 Fabio Valentini <decathorpe@gmail.com> - 0.3.1~rev1846-1
- Update to new upstream snapshot.

* Fri Oct 02 2015 Fabio Valentini <decathorpe@gmail.com> - 0.3.1~rev1845-1
- Update to new upstream snapshot.

* Thu Oct 01 2015 Fabio Valentini <decathorpe@gmail.com> - 0.3.1~rev1844-1
- Update to new upstream snapshot.

* Wed Sep 30 2015 Fabio Valentini <decathorpe@gmail.com> - 0.3.1~rev1843-1
- Update to new upstream snapshot.

* Tue Sep 29 2015 Fabio Valentini <decathorpe@gmail.com> - 0.3.1~rev1842-1
- Update to new upstream snapshot.

* Mon Sep 28 2015 Fabio Valentini <decathorpe@gmail.com> - 0.3.1~rev1841-1
- Update to new upstream snapshot.

* Sat Sep 26 2015 Fabio Valentini <decathorpe@gmail.com> - 0.3.1~rev1840-1
- Update to new upstream snapshot.

* Thu Sep 24 2015 Fabio Valentini <decathorpe@gmail.com> - 0.3.1~rev1839-1
- Update to new upstream snapshot.

* Wed Sep 23 2015 Fabio Valentini <decathorpe@gmail.com> - 0.3.1~rev1838-1
- Update to new upstream snapshot.

* Fri Sep 18 2015 Fabio Valentini <decathorpe@gmail.com> - 0.3.1~rev1837-1
- Update to new upstream snapshot.

* Thu Sep 17 2015 Fabio Valentini <decathorpe@gmail.com> - 0.3.1~rev1836-1
- Update to new upstream snapshot.

* Wed Sep 16 2015 Fabio Valentini <decathorpe@gmail.com> - 0.3.1~rev1834-1
- Update to new upstream snapshot.

* Tue Sep 15 2015 Fabio Valentini <decathorpe@gmail.com> - 0.3.1~rev1833-1
- Update to new upstream snapshot.

* Mon Sep 14 2015 Fabio Valentini <decathorpe@gmail.com> - 0.3.1~rev1831-1
- Update to new upstream snapshot.

* Sun Sep 13 2015 Fabio Valentini <decathorpe@gmail.com> - 0.3.1~rev1830-3
- Remove BR on libindicate.

* Thu Sep 10 2015 Fabio Valentini <decathorpe@gmail.com> - 0.3.1~rev1830-2
- Update spec and add Req: libgda-sqlite for new DB backend.

* Tue Sep 08 2015 Fabio Valentini <decathorpe@gmail.com> - 0.3.1~rev1830-1
- Update to new upstream snapshot.

* Sun Sep 06 2015 Fabio Valentini <decathorpe@gmail.com> - 0.3.1~rev1829-1
- Update to new upstream snapshot.

* Fri Sep 04 2015 Fabio Valentini <decathorpe@gmail.com> - 0.3.1~rev1828-2
- rebuild trigger for granite soname bump

* Thu Sep 03 2015 Fabio Valentini <decathorpe@gmail.com> - 0.3.1~rev1828-1
- Update to new upstream snapshot.

* Thu Sep 03 2015 Fabio Valentini <decathorpe@gmail.com> - 0.3.1~rev1827-1
- Update spec to reflect BR changes and use make_build and make_install macros.

* Thu Sep 03 2015 Fabio Valentini <decathorpe@gmail.com> - 0.3.1~rev1827-1
- Update to new upstream snapshot.

* Tue Sep 01 2015 Fabio Valentini <decathorpe@gmail.com> - 0.3.1~rev1826-1
- Update to new upstream snapshot.

* Thu Aug 20 2015 Fabio Valentini <decathorpe@gmail.com> - 0.3.1~rev1825-1
- Update to new upstream snapshot.

* Tue Aug 18 2015 Fabio Valentini - 0.3.1~rev1823-1
- Update to new upstream snapshot.

* Mon Jul 13 2015 Fabio Valentini <decathorpe@gmail.com> - 0.3.1~rev1822-1
- Update to bzr snapshot revno 1822.

* Sat Jul 04 2015 Fabio Valentini <decathorpe@gmail.com> - 0.3.1~rev1821-1
- Initial package.


