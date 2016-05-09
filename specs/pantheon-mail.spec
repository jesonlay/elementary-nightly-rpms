Summary:        Mail is an email client for elementary OS
Name:           pantheon-mail
Version:        1.0.0~rev%{rev}
Release:        1%{?dist}
License:        LGPLv2.1
URL:            http://launchpad.net/pantheon-mail

Source0:        %{name}-%{version}.tar.gz
Source1:        %{name}.conf

BuildRequires:  cmake
BuildRequires:  desktop-file-utils
BuildRequires:  gettext
BuildRequires:  libappstream-glib
BuildRequires:  vala >= 0.22.1
BuildRequires:  vala-tools

BuildRequires:  pkgconfig(gcr-3) >= 3.10.1
BuildRequires:  pkgconfig(gee-0.8) >= 0.8.5
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(glib-2.0) >= 2.40.0
BuildRequires:  pkgconfig(gmime-2.6) >= 2.6.14
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(granite)
BuildRequires:  pkgconfig(gthread-2.0)
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.10.0
BuildRequires:  pkgconfig(libcanberra) >= 0.28
BuildRequires:  pkgconfig(libsecret-1) >= 0.11
BuildRequires:  pkgconfig(libsoup-2.4)
BuildRequires:  pkgconfig(libxml-2.0) >= 2.7.8
BuildRequires:  pkgconfig(sqlite3) >= 3.7.4
BuildRequires:  pkgconfig(webkitgtk-3.0) >= 2.3.0

Requires:       contractor


%description
Mail is an email client for elementary OS

Originally written by Yorba (yorba.org)


%prep
%autosetup


%build
%cmake
%make_build


%install
%make_install
%find_lang pantheon-mail


%check
desktop-file-validate $RPM_BUILD_ROOT/%{_datadir}/applications/pantheon-mail.desktop
desktop-file-validate $RPM_BUILD_ROOT/%{_datadir}/applications/pantheon-mail-autostart.desktop

# appstream-util validate-relax --nonet $RPM_BUILD_ROOT/%{_datadir}/appdata/*.appdata.xml


%clean
rm -rf $RPM_BUILD_ROOT


%post
/usr/bin/update-desktop-database &> /dev/null || :

%postun
/usr/bin/update-desktop-database &> /dev/null || :
if [ $1 -eq 0 ] ; then
    /usr/bin/glib-compile-schemas %{_datadir}/glib-2.0/schemas &> /dev/null || :
fi

%posttrans
/usr/bin/glib-compile-schemas %{_datadir}/glib-2.0/schemas &> /dev/null || :


%files -f pantheon-mail.lang
%doc AUTHORS HACKING THANKS
%license COPYING

%{_bindir}/pantheon-mail
%{_bindir}/mail-attach

%{_datadir}/appdata/pantheon-mail.appdata.xml
%{_datadir}/applications/pantheon-mail.desktop
%{_datadir}/applications/pantheon-mail-autostart.desktop
%{_datadir}/contractor/mail-attach.contract
%{_datadir}/glib-2.0/schemas/org.pantheon.mail.gschema.xml
%{_datadir}/pantheon-mail/


%changelog
* Mon May 09 2016 Fabio Valentini <decathorpe@gmail.com> - 1.0.0~rev2047-1
- Update to latest snapshot.

* Sun May 08 2016 Fabio Valentini <decathorpe@gmail.com> - 1.0.0~rev2046-1
- Update to latest snapshot.

* Fri May 06 2016 Fabio Valentini <decathorpe@gmail.com> - 1.0.0~rev2045-1
- Update to latest snapshot.

* Wed May 04 2016 Fabio Valentini <decathorpe@gmail.com> - 1.0.0~rev2043-1
- Update to latest snapshot.

* Wed May 04 2016 Fabio Valentini <decathorpe@gmail.com> - 1.0.0~rev2043-1
- Update to latest snapshot.

* Tue May 03 2016 Fabio Valentini <decathorpe@gmail.com> - 1.0.0~rev2042-1
- Update to new upstream snapshot.

* Sat Apr 30 2016 Fabio Valentini <decathorpe@gmail.com> - 1.0.0~rev2041-1
- Update to new upstream snapshot.

* Sun Apr 24 2016 Fabio Valentini <decathorpe@gmail.com> - 1.0.0~rev2040-1
- Update to new upstream snapshot.

* Fri Apr 22 2016 Fabio Valentini <decathorpe@gmail.com> - 1.0.0~rev2039-1
- Update to new upstream snapshot.

* Wed Apr 20 2016 Fabio Valentini <decathorpe@gmail.com> - 1.0.0~rev2038-1
- Update to new upstream snapshot.

* Sun Apr 17 2016 Fabio Valentini <decathorpe@gmail.com> - 1.0.0~rev2036-1
- Update to new upstream snapshot.

* Tue Apr 12 2016 Fabio Valentini <decathorpe@gmail.com> - 1.0.0~rev2035-1
- Update to new upstream snapshot.

* Sun Apr 10 2016 Fabio Valentini <decathorpe@gmail.com> - 1.0.0~rev2034-1
- Update to new upstream snapshot.

* Thu Apr 07 2016 Fabio Valentini <decathorpe@gmail.com> - 1.0.0~rev2032-1
- Update to new upstream snapshot.

* Thu Mar 31 2016 Fabio Valentini <decathorpe@gmail.com> - 1.0.0~rev2031-1
- Update to new upstream snapshot.

* Tue Mar 29 2016 Fabio Valentini <decathorpe@gmail.com> - 1.0.0~rev2030-1
- Update to new upstream snapshot.

* Sun Mar 27 2016 Fabio Valentini <decathorpe@gmail.com> - 1.0.0~rev2028-1
- Update to new upstream snapshot.

* Fri Mar 25 2016 Fabio Valentini <decathorpe@gmail.com> - 1.0.0~rev2026-1
- Update to new upstream snapshot.

* Thu Mar 24 2016 Fabio Valentini <decathorpe@gmail.com> - 1.0.0~rev2024-1
- Update to new upstream snapshot.

* Tue Mar 22 2016 Fabio Valentini <decathorpe@gmail.com> - 1.0.0~rev2023-1
- Update to new upstream snapshot.

* Mon Mar 21 2016 Fabio Valentini <decathorpe@gmail.com> - 1.0.0~rev2020-1
- Update to new upstream snapshot.

* Sat Mar 19 2016 Fabio Valentini <decathorpe@gmail.com> - 1.0.0~rev2019-1
- Update to new upstream snapshot.

* Fri Mar 18 2016 Fabio Valentini <decathorpe@gmail.com> - 1.0.0~rev2017-1
- Update to new upstream snapshot.

* Thu Mar 17 2016 Fabio Valentini <decathorpe@gmail.com> - 1.0.0~rev2015-1
- Update to new upstream snapshot.

* Tue Mar 15 2016 Fabio Valentini <decathorpe@gmail.com> - 1.0.0~rev2013-1
- Update to new upstream snapshot.

* Mon Mar 14 2016 Fabio Valentini <decathorpe@gmail.com> - 1.0.0~rev2008-1
- Update to new upstream snapshot.

* Sun Mar 13 2016 Fabio Valentini <decathorpe@gmail.com> - 1.0.0~rev2004-1
- Update to new upstream snapshot.

* Sat Mar 12 2016 Fabio Valentini <decathorpe@gmail.com> - 1.0.0~rev2002-1
- Update to new upstream snapshot.

* Thu Mar 10 2016 Fabio Valentini <decathorpe@gmail.com> - 1.0.0~rev2001-1
- Update to new upstream snapshot.

* Wed Mar 09 2016 Fabio Valentini <decathorpe@gmail.com> - 1.0.0~rev2000-1
- Update to new upstream snapshot.

* Tue Mar 08 2016 Fabio Valentini <decathorpe@gmail.com> - 1.0.0~rev1999-1
- Update to new upstream snapshot.

* Mon Mar 07 2016 Fabio Valentini <decathorpe@gmail.com> - 1.0.0~rev1998-1
- Update to new upstream snapshot.

* Sat Mar 05 2016 Fabio Valentini <decathorpe@gmail.com> - 1.0.0~rev1996-1
- Update to new upstream snapshot.

* Fri Mar 04 2016 Fabio Valentini <decathorpe@gmail.com> - 1.0.0~rev1995-1
- Update to new upstream snapshot.

* Thu Mar 03 2016 Fabio Valentini <decathorpe@gmail.com> - 1.0.0~rev1994-1
- Update to new upstream snapshot.

* Wed Mar 02 2016 Fabio Valentini <decathorpe@gmail.com> - 1.0.0~rev1992-1
- Update to new upstream snapshot.

* Wed Mar 02 2016 Fabio Valentini <decathorpe@gmail.com> - 1.0.0~rev1991-1
- Update to new upstream snapshot.

* Tue Mar 01 2016 Fabio Valentini <decathorpe@gmail.com> - 1.0.0~rev1990-1
- Update to new upstream snapshot.

* Mon Feb 29 2016 Fabio Valentini <decathorpe@gmail.com> - 1.0.0~rev1989-1
- Update to new upstream snapshot.

* Sat Feb 27 2016 Fabio Valentini <decathorpe@gmail.com> - 1.0.0~rev1987-1
- Update to new upstream snapshot.

* Fri Feb 26 2016 Fabio Valentini <decathorpe@gmail.com> - 1.0.0~rev1986-1
- Update to new upstream snapshot.

* Wed Feb 24 2016 Fabio Valentini <decathorpe@gmail.com> - 1.0.0~rev1984-1
- Update to new upstream snapshot.

* Wed Feb 24 2016 Fabio Valentini <decathorpe@gmail.com> - 1.0.0~rev1983-1
- Update to new upstream snapshot.

* Tue Feb 23 2016 Fabio Valentini <decathorpe@gmail.com> - 1.0.0~rev1980-1
- Update to new upstream snapshot.

* Sun Feb 21 2016 Fabio Valentini <decathorpe@gmail.com> - 1.0.0~rev1978-1
- Update to new upstream snapshot.

* Sat Feb 20 2016 Fabio Valentini <decathorpe@gmail.com> - 1.0.0~rev1977-1
- Update to new upstream snapshot.

* Thu Feb 18 2016 Fabio Valentini <decathorpe@gmail.com> - 1.0.0~rev1974-2
- Update packaging to fix build.
- Remove Conflicts: geary.

* Thu Feb 18 2016 Fabio Valentini <decathorpe@gmail.com> - 1.0.0~rev1974-1
- Update to new upstream snapshot.

* Sat Feb 13 2016 Fabio Valentini <decathorpe@gmail.com> - 1.0.0~rev1969-2
- Add BR: granite-devel.

* Sat Feb 13 2016 Fabio Valentini <decathorpe@gmail.com> - 1.0.0~rev1969-1
- Update to new upstream snapshot.

* Thu Feb 11 2016 Fabio Valentini <decathorpe@gmail.com> - 1.0.0~rev1968-1
- Update to new upstream snapshot.

* Wed Feb 10 2016 Fabio Valentini <decathorpe@gmail.com> - 1.0.0~rev1967-1
- Update to new upstream snapshot.

* Mon Feb 08 2016 Fabio Valentini <decathorpe@gmail.com> - 1.0.0~rev1962-1
- Update to new upstream snapshot.

* Sun Feb 07 2016 Fabio Valentini <decathorpe@gmail.com> - 1.0.0~rev1957-1
- Update to new upstream snapshot.

* Sat Feb 06 2016 Fabio Valentini <decathorpe@gmail.com> - 1.0.0~rev1956-1
- Update to new upstream snapshot.

* Thu Feb 04 2016 Fabio Valentini <decathorpe@gmail.com> - 1.0.0~rev1955-1
- Update to new upstream snapshot.

* Tue Feb 02 2016 Fabio Valentini <decathorpe@gmail.com> - 1.0.0~rev1954-1
- Update to new upstream snapshot.

* Sun Jan 31 2016 Fabio Valentini <decathorpe@gmail.com> - 1.0.0~rev1953-1
- Update to new upstream snapshot.

* Sat Jan 30 2016 Fabio Valentini <decathorpe@gmail.com> - 1.0.0~rev1952-1
- Update to new upstream snapshot.

* Fri Jan 29 2016 Fabio Valentini <decathorpe@gmail.com> - 1.0.0~rev1948-1
- Update to new upstream snapshot.

* Thu Jan 28 2016 Fabio Valentini <decathorpe@gmail.com> - 1.0.0~rev1947-2
- Remove no longer existant gnome help files.

* Thu Jan 28 2016 Fabio Valentini <decathorpe@gmail.com> - 1.0.0~rev1947-1
- Update to new upstream snapshot.

* Tue Jan 26 2016 Fabio Valentini <decathorpe@gmail.com> - 1.0.0~rev1945-1
- Update to new upstream snapshot.

* Fri Jan 22 2016 Fabio Valentini <decathorpe@gmail.com> - 1.0.0~rev1944-1
- Update to new upstream snapshot.

* Thu Jan 21 2016 Fabio Valentini <decathorpe@gmail.com> - 1.0.0~rev1943-1
- Update to new upstream snapshot.

* Mon Jan 18 2016 Fabio Valentini <decathorpe@gmail.com> - 1.0.0~rev1941-1
- Update to new upstream snapshot.

* Sun Jan 17 2016 Fabio Valentini <decathorpe@gmail.com> - 1.0.0~rev1940-1
- Update to new upstream snapshot.

* Thu Jan 14 2016 Fabio Valentini <decathorpe@gmail.com> - 1.0.0~rev1939-1
- Update to new upstream snapshot.

* Tue Jan 12 2016 Fabio Valentini <decathorpe@gmail.com> - 1.0.0~rev1938-1
- Update to new upstream snapshot.

* Mon Jan 11 2016 Fabio Valentini <decathorpe@gmail.com> - 1.0.0~rev1937-1
- Update to new upstream snapshot.

* Thu Jan 07 2016 Fabio Valentini <decathorpe@gmail.com> - 1.0.0~rev1935-1
- Update to new upstream snapshot.

* Wed Jan 06 2016 Fabio Valentini <decathorpe@gmail.com> - 1.0.0~rev1934-1
- Update to new upstream snapshot.

* Mon Jan 04 2016 Fabio Valentini <decathorpe@gmail.com> - 1.0.0~rev1933-1
- Update to new upstream snapshot.

* Sun Jan 03 2016 Fabio Valentini <decathorpe@gmail.com> - 1.0.0~rev1932-1
- Update to new upstream snapshot.

* Sat Dec 26 2015 Fabio Valentini <decathorpe@gmail.com> - 1.0.0~rev1931-1
- Update to new upstream snapshot.

* Thu Dec 24 2015 Fabio Valentini <decathorpe@gmail.com> - 1.0.0~rev1929-1
- Update to new upstream snapshot.

* Wed Dec 23 2015 Fabio Valentini <decathorpe@gmail.com> - 1.0.0~rev1928-1
- Update to new upstream snapshot.

* Tue Dec 22 2015 Fabio Valentini <decathorpe@gmail.com> - 1.0.0~rev1926-1
- Update to new upstream snapshot.

* Mon Dec 21 2015 Fabio Valentini <decathorpe@gmail.com> - 1.0.0~rev1924-1
- Update to new upstream snapshot.

* Sun Dec 20 2015 Fabio Valentini <decathorpe@gmail.com> - 1.0.0~rev1923-1
- Update to new upstream snapshot.

* Fri Dec 18 2015 Fabio Valentini <decathorpe@gmail.com> - 1.0.0~rev1922-1
- Update to new upstream snapshot.

* Thu Dec 17 2015 Fabio Valentini <decathorpe@gmail.com> - 1.0.0~rev1921-1
- Update to new upstream snapshot.

* Wed Dec 16 2015 Fabio Valentini <decathorpe@gmail.com> - 1.0.0~rev1920-1
- Update to new upstream snapshot.

* Tue Dec 15 2015 Fabio Valentini <decathorpe@gmail.com> - 1.0.0~rev1919-1
- Update to new upstream snapshot.

* Sat Dec 12 2015 Fabio Valentini <decathorpe@gmail.com> - 1.0.0~rev1918-1
- Update to new upstream snapshot.

* Fri Dec 11 2015 Fabio Valentini <decathorpe@gmail.com> - 1.0.0~rev1917-1
- Update to new upstream snapshot.

* Wed Dec 09 2015 Fabio Valentini <decathorpe@gmail.com> - 1.0.0~rev1916-1
- Update to new upstream snapshot.

* Tue Dec 08 2015 Fabio Valentini <decathorpe@gmail.com> - 1.0.0~rev1915-1
- Update to new upstream snapshot.

* Mon Dec 07 2015 Fabio Valentini <decathorpe@gmail.com> - 1.0.0~rev1914-1
- Update to new upstream snapshot.

* Sun Dec 06 2015 Fabio Valentini <decathorpe@gmail.com> - 1.0.0~rev1913-1
- Update to new upstream snapshot.

* Thu Dec 03 2015 Fabio Valentini <decathorpe@gmail.com> - 1.0.0~rev1909-2
- Add Conflicts: geary until they cannot be installed side-by-side.

* Thu Dec 03 2015 Fabio Valentini <decathorpe@gmail.com> - 1.0.0~rev1909-1
- Update to new upstream snapshot.

* Wed Dec 02 2015 Fabio Valentini <decathorpe@gmail.com> - 1.0.0~rev1908-1
- Update to new upstream snapshot.

* Tue Dec 01 2015 Fabio Valentini <decathorpe@gmail.com> - 1.0.0~rev1905-2
- Fix FTBFS. Binary renamed, contract added, added R:contractor.

* Tue Dec 01 2015 Fabio Valentini <decathorpe@gmail.com> - 1.0.0~rev1905-1
- Update to new upstream snapshot.

* Tue Dec 01 2015 Fabio Valentini <decathorpe@gmail.com> - 1.0.0~rev1904-1
- Update to new upstream snapshot.

* Mon Nov 30 2015 Fabio Valentini <decathorpe@gmail.com> - 1.0.0~rev1898-1
- Update to new upstream snapshot.

* Sun Nov 29 2015 Fabio Valentini <decathorpe@gmail.com> - 1.0.0~rev1896-1
- Update to new upstream snapshot.

* Sat Nov 28 2015 Fabio Valentini <decathorpe@gmail.com> - 1.0.0~rev1895-1
- Update to new upstream snapshot.

* Fri Nov 27 2015 Fabio Valentini <decathorpe@gmail.com> - 1.0.0~rev1894-1
- Update to new upstream snapshot.

* Thu Nov 26 2015 Fabio Valentini <decathorpe@gmail.com> - 1.0.0~rev1893-3
- Add required gsettings compiling scriptlet.

* Thu Nov 26 2015 Fabio Valentini <decathorpe@gmail.com> - 1.0.0~rev1893-2
- Update spec to represent geary -> pantheon-mail renaming.

* Thu Nov 26 2015 Fabio Valentini <decathorpe@gmail.com> - 1.0.0~rev1893-1
- Update to new upstream snapshot.

* Tue Nov 24 2015 Fabio Valentini <decathorpe@gmail.com> - 1.0.0~rev1885-1
- Update to new upstream snapshot.

* Mon Nov 23 2015 Fabio Valentini <decathorpe@gmail.com> - 1.0.0~rev1882-1
- Update to new upstream snapshot.

* Sat Nov 21 2015 Fabio Valentini <decathorpe@gmail.com> - 1.0.0~rev1874-1
- Initial package.



