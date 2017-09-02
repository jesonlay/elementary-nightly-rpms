Summary:        Scratch - the text editor that works.
Name:           scratch-text-editor
Version:        2.4.1+rev%{rev}
Release:        1%{?dist}
License:        GPLv3

URL:            http://launchpad.net/scratch
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
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(granite) >= 0.3.0
BuildRequires:  pkgconfig(gtksourceview-3.0) >= 3.10
BuildRequires:  pkgconfig(gtkspell3-3.0)
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.10
BuildRequires:  pkgconfig(libpeas-1.0)
BuildRequires:  pkgconfig(libpeas-gtk-1.0)
BuildRequires:  pkgconfig(libsoup-2.4)

%if %{?fedora} == 24
BuildRequires:  pkgconfig(libvala-0.32)
%endif

%if %{?fedora} == 25
BuildRequires:  pkgconfig(libvala-0.34)
%endif

%if %{?fedora} == 26
BuildRequires:  pkgconfig(libvala-0.36)
%endif

%if %{?fedora} > 26
BuildRequires:  pkgconfig(libvala-0.38)
%endif

BuildRequires:  pkgconfig(vte-2.91)
BuildRequires:  pkgconfig(webkit2gtk-4.0)
BuildRequires:  pkgconfig(zeitgeist-2.0)

Requires:       hicolor-icon-theme


%description
Scratch is the text editor that works for you. It auto-saves your files,
meaning they're always up-to-date. Plus it remembers your tabs so you
never lose your spot, even in between sessions.

Make it yours. Scratch is written from the ground up to be extensible.
Keep things super lightweight and simple, or install extensions to turn
Scratch into a full-blown IDE; it's your choice. And with a handful of
useful preferences, you can tweak the behavior and interface to your
liking.

It's elementary. Scratch is made to be the perfect text editor for
elementary, meaning it closely follows the high standards of design,
speed, and consistency. It's sexy, but not distracting.

Works with your language. Whether you're crafting code in Vala,
scripting with PHP, or marking things up in HTML, Scratch has you
covered. Experience full syntax highlighting with nearly all
programming, scripting, and markup languages.

Other syntax-highlighted languages: Bash, C, C#, C++. Cmake, CSS,
.Desktop, Diff, Fortran, Gettext, ini, Java, JavaScript, LaTex, Lua,
Makefile, Objective C, Pascal, Perl, Python, Ruby, XML.

Additional features include:

 * syntax highlighting with gtksourceview-3
 * a find bar to search the words in the files
 * strong integration with Granite framework by elementary-team
 * tab and split documents system
 * lots of others

Scratch needs to be translated. Go to Translations to help us providing
this software in your language!

Designed for elementary OS. Works and looks great on any GTK+ desktop.


%package        devel
Summary:        Scratch - the text editor that works.
%description    devel
Scratch is the text editor that works for you. It auto-saves your files,
meaning they're always up-to-date. Plus it remembers your tabs so you
never lose your spot, even in between sessions.

This package contains the development headers.


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

%find_lang io.elementary.code

mv %{buildroot}/%{_datadir}/metainfo %{buildroot}/%{_datadir}/appdata


%check
desktop-file-validate %{buildroot}/%{_datadir}/applications/*.desktop
appstream-util validate-relax --nonet %{buildroot}/%{_datadir}/appdata/*.appdata.xml


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


%files -f io.elementary.code.lang
%doc README.md
%license COPYING

%{_bindir}/io.elementary.code

%{_libdir}/io.elementary.code/
%{_libdir}/libscratchcore.so.0
%{_libdir}/libscratchcore.so.0.0

%{_datadir}/appdata/io.elementary.code.appdata.xml
%{_datadir}/applications/org.pantheon.scratch.desktop
%{_datadir}/glib-2.0/schemas/org.pantheon.scratch.*
%{_datadir}/icons/hicolor/*/apps/io.elementary.code.svg
%{_datadir}/io.elementary.code/


%files          devel
%{_includedir}/scratch/

%{_libdir}/libscratchcore.so
%{_libdir}/pkgconfig/scratchcore.pc

%{_datadir}/vala/vapi/scratchcore.deps
%{_datadir}/vala/vapi/scratchcore.vapi


%changelog
* Sat Sep 02 2017 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+rev1951-1
- Update to latest snapshot.

* Thu Aug 31 2017 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+rev1949-2
- Adapt to vala pkgconfig change.

* Thu Aug 31 2017 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+rev1949-1
- Update to latest snapshot.

* Wed Aug 30 2017 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+rev1948-1
- Update to latest snapshot.

* Fri Aug 25 2017 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+rev1947-1
- Update to latest snapshot.

* Fri Aug 25 2017 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+rev1946-1
- Update to latest snapshot.

* Thu Aug 24 2017 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+rev1942-1
- Update to latest snapshot.

* Wed Aug 23 2017 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+rev1940-1
- Update to latest snapshot.

* Wed Aug 23 2017 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+rev1939-1
- Update to latest snapshot.

* Mon Aug 21 2017 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+rev1936-1
- Update to latest snapshot.

* Sun Aug 20 2017 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+rev1935-1
- Update to latest snapshot.

* Sat Aug 19 2017 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+rev1933-1
- Update to latest snapshot.

* Fri Aug 18 2017 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+rev1931-1
- Update to latest snapshot.

* Thu Aug 17 2017 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+rev1930-1
- Update to latest snapshot.

* Mon Aug 14 2017 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+rev1927-1
- Update to latest snapshot.

* Sun Aug 13 2017 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+rev1926-1
- Update to latest snapshot.

* Sun Aug 06 2017 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+rev1925-1
- Update to latest snapshot.

* Fri Jul 28 2017 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+rev1923-1
- Update to latest snapshot.

* Wed Jul 12 2017 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+rev1918-1
- Update to latest snapshot.

* Sat Jul 08 2017 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+rev1915-1
- Update to latest snapshot.

* Sun Jul 02 2017 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+rev1908-1
- Update to latest snapshot.

* Sat Jul 01 2017 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+rev1906-1
- Update to latest snapshot.

* Wed Jun 28 2017 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+rev1903-1
- Update to latest snapshot.

* Tue Jun 27 2017 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+rev1901-1
- Update to latest snapshot.

* Tue Jun 20 2017 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+rev1896-1
- Update to latest snapshot.

* Sun Jun 18 2017 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+rev1885-1
- Update to latest snapshot.

* Sat Jun 17 2017 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+rev1881-1
- Update to latest snapshot.

* Fri Jun 16 2017 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+rev1880-1
- Update to latest snapshot.

* Fri Jun 16 2017 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+rev1876-1
- Update to latest snapshot.

* Thu Jun 15 2017 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+rev1875-1
- Update to latest snapshot.

* Wed Jun 14 2017 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+rev1871-1
- Update to latest snapshot.

* Tue Jun 13 2017 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+rev1870-1
- Update to latest snapshot.

* Fri Jun 02 2017 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+rev1869-2
- Adapt to upstream file changes.

* Thu Jun 01 2017 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+rev1869-1
- Update to latest snapshot.

* Thu Jun 01 2017 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+rev1868-1
- Update to latest snapshot.

* Thu May 18 2017 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+rev1866-1
- Update to latest snapshot.

* Wed May 17 2017 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+rev1865-1
- Update to latest snapshot.

* Sat May 13 2017 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+rev1864-1
- Update to latest snapshot.

* Thu May 11 2017 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+rev1863-2
- Adapt to upstream file changes.

* Thu May 11 2017 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+rev1863-1
- Update to latest snapshot.

* Wed May 10 2017 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+rev1862-2
- Adapt to upstream file changes.

* Wed May 10 2017 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+rev1862-1
- Update to latest snapshot.

* Tue May 09 2017 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+rev1858-1
- Update to version 2.4.1.

* Tue May 09 2017 Fabio Valentini <decathorpe@gmail.com> - 2.4+rev1858-2
- Adapt to upstream file changes.

* Tue May 09 2017 Fabio Valentini <decathorpe@gmail.com> - 2.4+rev1858-1
- Update to latest snapshot.

* Sun May 07 2017 Fabio Valentini <decathorpe@gmail.com> - 2.4+rev1856-1
- Update to latest snapshot.

* Sat May 06 2017 Fabio Valentini <decathorpe@gmail.com> - 2.4+rev1855-2
- Adapt to upstream file changes.

* Sat May 06 2017 Fabio Valentini <decathorpe@gmail.com> - 2.4+rev1855-1
- Update to latest snapshot.

* Wed May 03 2017 Fabio Valentini <decathorpe@gmail.com> - 2.4+rev1846-1
- Update to latest snapshot.

* Tue May 02 2017 Fabio Valentini <decathorpe@gmail.com> - 2.4+rev1845-1
- Update to latest snapshot.

* Fri Apr 14 2017 Fabio Valentini <decathorpe@gmail.com> - 2.4+rev1843-1
- Update to latest snapshot.

* Wed Apr 05 2017 Fabio Valentini <decathorpe@gmail.com> - 2.4+rev1842-1
- Update to latest snapshot.

* Sun Mar 26 2017 Fabio Valentini <decathorpe@gmail.com> - 2.4+rev1841-1
- Update to latest snapshot.

* Wed Mar 22 2017 Fabio Valentini <decathorpe@gmail.com> - 2.4+rev1839-1
- Update to latest snapshot.

* Mon Mar 20 2017 Fabio Valentini <decathorpe@gmail.com> - 2.4+rev1838-1
- Update to latest snapshot.

* Sun Mar 19 2017 Fabio Valentini <decathorpe@gmail.com> - 2.4+rev1837-1
- Update to latest snapshot.

* Wed Mar 15 2017 Fabio Valentini <decathorpe@gmail.com> - 2.4+rev1836-1
- Update to latest snapshot.

* Thu Mar 09 2017 Fabio Valentini <decathorpe@gmail.com> - 2.4+rev1835-1
- Update to latest snapshot.

* Tue Mar 07 2017 Fabio Valentini <decathorpe@gmail.com> - 2.4+rev1834-1
- Update to latest snapshot.

* Sun Mar 05 2017 Fabio Valentini <decathorpe@gmail.com> - 2.4+rev1833-1
- Update to latest snapshot.

* Fri Mar 03 2017 Fabio Valentini <decathorpe@gmail.com> - 2.4+rev1832-1
- Update to latest snapshot.

* Thu Mar 02 2017 Fabio Valentini <decathorpe@gmail.com> - 2.4+rev1831-1
- Update to latest snapshot.

* Wed Mar 01 2017 Fabio Valentini <decathorpe@gmail.com> - 2.4+rev1830-1
- Update to latest snapshot.

* Tue Feb 28 2017 Fabio Valentini <decathorpe@gmail.com> - 2.4+rev1829-1
- Update to latest snapshot.

* Mon Feb 27 2017 Fabio Valentini <decathorpe@gmail.com> - 2.4+rev1828-1
- Update to latest snapshot.

* Thu Feb 23 2017 Fabio Valentini <decathorpe@gmail.com> - 2.4+rev1826-1
- Update to latest snapshot.

* Mon Feb 20 2017 Fabio Valentini <decathorpe@gmail.com> - 2.4+rev1825-1
- Update to latest snapshot.

* Sat Feb 18 2017 Fabio Valentini <decathorpe@gmail.com> - 2.4+rev1823-1
- Update to latest snapshot.

* Fri Feb 17 2017 Fabio Valentini <decathorpe@gmail.com> - 2.4+rev1821-1
- Update to latest snapshot.

* Thu Feb 16 2017 Fabio Valentini <decathorpe@gmail.com> - 2.4+rev1820-1
- Update to latest snapshot.

* Wed Feb 15 2017 Fabio Valentini <decathorpe@gmail.com> - 2.4+rev1819-1
- Update to latest snapshot.

* Sun Feb 12 2017 Fabio Valentini <decathorpe@gmail.com> - 2.4+rev1818-1
- Update to version 2.4.

* Sun Feb 12 2017 Fabio Valentini <decathorpe@gmail.com> - 2.3+rev1818-1
- Update to latest snapshot.

* Sat Feb 11 2017 Fabio Valentini <decathorpe@gmail.com> - 2.3+rev1817-1
- Update to latest snapshot.

* Fri Feb 10 2017 Fabio Valentini <decathorpe@gmail.com> - 2.3+rev1816-1
- Update to latest snapshot.

* Mon Jan 30 2017 Fabio Valentini <decathorpe@gmail.com> - 2.3+rev1814-1
- Update to latest snapshot.

* Sun Jan 29 2017 Fabio Valentini <decathorpe@gmail.com> - 2.3+rev1813-1
- Update to latest snapshot.

* Sat Jan 28 2017 Fabio Valentini <decathorpe@gmail.com> - 2.3+rev1812-1
- Update to latest snapshot.

* Fri Jan 27 2017 Fabio Valentini <decathorpe@gmail.com> - 2.3+rev1811-1
- Update to latest snapshot.

* Thu Jan 26 2017 Fabio Valentini <decathorpe@gmail.com> - 2.3+rev1810-1
- Update to latest snapshot.

* Wed Jan 25 2017 Fabio Valentini <decathorpe@gmail.com> - 2.3+rev1809-1
- Update to latest snapshot.

* Sun Jan 22 2017 Fabio Valentini <decathorpe@gmail.com> - 2.3+rev1808-1
- Update to latest snapshot.

* Sat Jan 21 2017 Fabio Valentini <decathorpe@gmail.com> - 2.3+rev1806-1
- Update to latest snapshot.

* Sat Jan 14 2017 Fabio Valentini <decathorpe@gmail.com> - 2.3+rev1805-1
- Update to version 2.3.

* Fri Jan 13 2017 Fabio Valentini <decathorpe@gmail.com> - 2.3+rev1804-1
- Update to version 2.3.

* Thu Jan 12 2017 Fabio Valentini <decathorpe@gmail.com> - 2.3+rev1803-1
- Update to version 2.3.

* Wed Jan 11 2017 Fabio Valentini <decathorpe@gmail.com> - 2.3+rev1802-1
- Update to version 2.3.

* Mon Jan 09 2017 Fabio Valentini <decathorpe@gmail.com> - 2.3+rev1801-1
- Update to version 2.3.

* Sun Jan 08 2017 Fabio Valentini <decathorpe@gmail.com> - 2.3+rev1800-1
- Update to version 2.3.

* Sat Jan 07 2017 Fabio Valentini <decathorpe@gmail.com> - 2.3+rev1799-1
- Update to version 2.3.

* Fri Jan 06 2017 Fabio Valentini <decathorpe@gmail.com> - 2.3+rev1797-1
- Update to version 2.3.

* Sat Dec 31 2016 Fabio Valentini <decathorpe@gmail.com> - 2.3+rev1796-1
- Update to latest snapshot.

* Fri Dec 30 2016 Fabio Valentini <decathorpe@gmail.com> - 2.3+rev1795-1
- Update to latest snapshot.

* Wed Dec 28 2016 Fabio Valentini <decathorpe@gmail.com> - 2.3+rev1794-1
- Update to latest snapshot.

* Tue Dec 27 2016 Fabio Valentini <decathorpe@gmail.com> - 2.3+rev1793-1
- Update to latest snapshot.

* Thu Dec 22 2016 Fabio Valentini <decathorpe@gmail.com> - 2.3+rev1792-1
- Update to latest snapshot.

* Wed Dec 21 2016 Fabio Valentini <decathorpe@gmail.com> - 2.3+rev1791-1
- Update to latest snapshot.

* Wed Dec 14 2016 Fabio Valentini <decathorpe@gmail.com> - 2.3+rev1790-1
- Update to latest snapshot.

* Tue Dec 13 2016 Fabio Valentini <decathorpe@gmail.com> - 2.3+rev1789-1
- Update to latest snapshot.

* Tue Dec 13 2016 Fabio Valentini <decathorpe@gmail.com> - 2.3+rev1788-1
- Update to latest snapshot.

* Mon Dec 12 2016 Fabio Valentini <decathorpe@gmail.com> - 2.3+rev1785-1
- Update to latest snapshot.

* Sun Dec 11 2016 Fabio Valentini <decathorpe@gmail.com> - 2.3+rev1784-1
- Update to latest snapshot.

* Sat Dec 10 2016 Fabio Valentini <decathorpe@gmail.com> - 2.3+rev1783-1
- Update to latest snapshot.

* Thu Dec 08 2016 Fabio Valentini <decathorpe@gmail.com> - 2.3+rev1782-1
- Update to latest snapshot.

* Mon Dec 05 2016 Fabio Valentini <decathorpe@gmail.com> - 2.3+rev1781-1
- Update to latest snapshot.

* Sun Dec 04 2016 Fabio Valentini <decathorpe@gmail.com> - 2.3+rev1780-1
- Update to latest snapshot.

* Fri Dec 02 2016 Fabio Valentini <decathorpe@gmail.com> - 2.3+rev1778-1
- Update to latest snapshot.

* Mon Nov 21 2016 Fabio Valentini <decathorpe@gmail.com> - 2.3+rev1777-1
- Update to latest snapshot.

* Sun Nov 20 2016 Fabio Valentini <decathorpe@gmail.com> - 2.3+rev1776-1
- Update to latest snapshot.

* Sat Nov 19 2016 Fabio Valentini <decathorpe@gmail.com> - 2.3+rev1775-1
- Update to latest snapshot.

* Sat Nov 12 2016 Fabio Valentini <decathorpe@gmail.com> - 2.3+rev1774-1
- Update to latest snapshot.

* Tue Nov 08 2016 Fabio Valentini <decathorpe@gmail.com> - 2.3+rev1773-1
- Update to latest snapshot.

* Mon Nov 07 2016 Fabio Valentini <decathorpe@gmail.com> - 2.3+rev1772-1
- Update to latest snapshot.

* Mon Oct 31 2016 Fabio Valentini <decathorpe@gmail.com> - 2.3+rev1771-1
- Update to latest snapshot.

* Mon Oct 17 2016 Fabio Valentini <decathorpe@gmail.com> - 2.3+rev1770-1
- Update to latest snapshot.

* Sun Oct 16 2016 Fabio Valentini <decathorpe@gmail.com> - 2.3+rev1769-1
- Update to latest snapshot.

* Thu Oct 13 2016 Fabio Valentini <decathorpe@gmail.com> - 2.3+rev1768-1
- Update to latest snapshot.

* Tue Oct 11 2016 Fabio Valentini <decathorpe@gmail.com> - 2.3+rev1767-1
- Update to latest snapshot.

* Mon Oct 10 2016 Fabio Valentini <decathorpe@gmail.com> - 2.3+rev1766-1
- Update to latest snapshot.

* Mon Oct 10 2016 Fabio Valentini <decathorpe@gmail.com> - 2.3+rev1765-1
- Update to latest snapshot.

* Thu Oct 06 2016 Fabio Valentini <decathorpe@gmail.com> - 2.3+rev1764-2
- "Fix" ldconfig path in scriptlets.

* Sat Oct 01 2016 Fabio Valentini <decathorpe@gmail.com> - 2.3+rev1764-1
- Update to latest snapshot.

* Thu Sep 29 2016 Fabio Valentini <decathorpe@gmail.com> - 2.3+rev1763-4
- Fix typo in BRs.

* Thu Sep 29 2016 Fabio Valentini <decathorpe@gmail.com> - 2.3+rev1763-3
- Spec file cleanups.

* Thu Sep 29 2016 Fabio Valentini <decathorpe@gmail.com> - 2.3+rev1763-2
- Spec file cleanups.

* Sat Sep 24 2016 Fabio Valentini <decathorpe@gmail.com> - 2.3+rev1763-1
- Update to latest snapshot.

* Fri Sep 23 2016 Fabio Valentini <decathorpe@gmail.com> - 2.3+rev1762-1
- Update to version 2.3.

* Tue Sep 20 2016 Fabio Valentini <decathorpe@gmail.com> - 2.3~rev1761-1
- Update to latest snapshot.

* Fri Sep 16 2016 Fabio Valentini <decathorpe@gmail.com> - 2.3~rev1760-2
- Update for packaging changes.

* Fri Sep 16 2016 Fabio Valentini <decathorpe@gmail.com>
- Adapt spec for renamed appdata and desktop files.

* Fri Sep 16 2016 Fabio Valentini <decathorpe@gmail.com> - 2.3~rev1760-1
- Update to latest snapshot.

* Thu Sep 15 2016 Fabio Valentini <decathorpe@gmail.com> - 2.3~rev1759-1
- Update to latest snapshot.

* Wed Sep 14 2016 Fabio Valentini <decathorpe@gmail.com> - 2.3~rev1757-1
- Update to latest snapshot.

* Tue Sep 13 2016 Fabio Valentini <decathorpe@gmail.com> - 2.3~rev1756-1
- Update to latest snapshot.

* Mon Sep 12 2016 Fabio Valentini <decathorpe@gmail.com> - 2.3~rev1755-1
- Update to latest snapshot.

* Sun Sep 11 2016 Fabio Valentini <decathorpe@gmail.com> - 2.3~rev1754-1
- Update to latest snapshot.

* Sat Sep 10 2016 Fabio Valentini <decathorpe@gmail.com> - 2.3~rev1753-1
- Update to latest snapshot.

* Fri Sep 09 2016 Fabio Valentini <decathorpe@gmail.com> - 2.3~rev1752-1
- Update to latest snapshot.

* Sun Sep 04 2016 Fabio Valentini <decathorpe@gmail.com> - 2.3~rev1751-2
- Update for packaging changes.

* Sun Sep 04 2016 Fabio Valentini <decathorpe@gmail.com>
- Change BR: webkit2gtk-3.0 to webkit2gtk-4.0.

* Sun Sep 04 2016 Fabio Valentini <decathorpe@gmail.com> - 2.3~rev1751-1
- Update to latest snapshot.

* Sun Sep 04 2016 Fabio Valentini <decathorpe@gmail.com> - 2.3~rev1750-1
- Update to latest snapshot.

* Sat Sep 03 2016 Fabio Valentini <decathorpe@gmail.com> - 2.3~rev1749-1
- Update to latest snapshot.

* Sat Sep 03 2016 Fabio Valentini <decathorpe@gmail.com> - 2.3~rev1747-1
- Update to latest snapshot.

* Thu Sep 01 2016 Fabio Valentini <decathorpe@gmail.com> - 2.3~rev1746-1
- Update to latest snapshot.

* Fri Aug 26 2016 Fabio Valentini <decathorpe@gmail.com> - 2.3~rev1745-1
- Update to latest snapshot.

* Thu Aug 25 2016 Fabio Valentini <decathorpe@gmail.com> - 2.3~rev1744-1
- Update to latest snapshot.

* Wed Aug 24 2016 Fabio Valentini <decathorpe@gmail.com> - 2.3~rev1743-1
- Update to latest snapshot.

* Fri Aug 19 2016 Fabio Valentini <decathorpe@gmail.com> - 2.3~rev1742-1
- Update to latest snapshot.

* Thu Aug 18 2016 Fabio Valentini <decathorpe@gmail.com> - 2.3~rev1741-1
- Update to latest snapshot.

* Wed Aug 17 2016 Fabio Valentini <decathorpe@gmail.com> - 2.3~rev1740-1
- Update to latest snapshot.

* Tue Aug 16 2016 Fabio Valentini <decathorpe@gmail.com> - 2.3~rev1739-1
- Update to latest snapshot.

* Mon Aug 15 2016 Fabio Valentini <decathorpe@gmail.com> - 2.3~rev1738-1
- Update to version 2.3.

* Sun Aug 14 2016 Fabio Valentini <decathorpe@gmail.com> - 2.2.1~rev1737-1
- Update to latest snapshot.

* Sat Aug 13 2016 Fabio Valentini <decathorpe@gmail.com> - 2.2.1~rev1736-1
- Update to latest snapshot.

* Fri Aug 12 2016 Fabio Valentini <decathorpe@gmail.com> - 2.2.1~rev1735-1
- Update to latest snapshot.

* Thu Aug 11 2016 Fabio Valentini <decathorpe@gmail.com> - 2.2.1~rev1734-1
- Update to latest snapshot.

* Thu Aug 11 2016 Fabio Valentini <decathorpe@gmail.com> - 2.2.1~rev1733-1
- Update to latest snapshot.

* Wed Aug 10 2016 Fabio Valentini <decathorpe@gmail.com> - 2.2.1~rev1732-1
- Update to latest snapshot.

* Tue Aug 09 2016 Fabio Valentini <decathorpe@gmail.com> - 2.2.1~rev1731-1
- Update to latest snapshot.

* Mon Aug 08 2016 Fabio Valentini <decathorpe@gmail.com> - 2.2.1~rev1730-1
- Update to latest snapshot.

* Sun Aug 07 2016 Fabio Valentini <decathorpe@gmail.com> - 2.2.1~rev1729-2
- Update for packaging changes.

* Sun Aug 07 2016 Fabio Valentini <decathorpe@gmail.com> - 2.2.1~rev1729-1
- Update to latest snapshot.

* Sat Aug 06 2016 Fabio Valentini <decathorpe@gmail.com> - 2.2.1~rev1728-1
- Update to latest snapshot.

* Fri Aug 05 2016 Fabio Valentini <decathorpe@gmail.com> - 2.2.1~rev1727-2
- Update for packaging changes.

* Fri Aug 05 2016 Fabio Valentini <decathorpe@gmail.com>
- Add BR: intltool to fix build.

* Fri Aug 05 2016 Fabio Valentini <decathorpe@gmail.com> - 2.2.1~rev1727-1
- Update to latest snapshot.

* Thu Aug 04 2016 Fabio Valentini <decathorpe@gmail.com> - 2.2.1~rev1726-1
- Update to latest snapshot.

* Tue Aug 02 2016 Fabio Valentini <decathorpe@gmail.com> - 2.2.1~rev1722-1
- Update to latest snapshot.

* Mon Aug 01 2016 Fabio Valentini <decathorpe@gmail.com> - 2.2.1~rev1721-1
- Update to latest snapshot.

* Sun Jul 31 2016 Fabio Valentini <decathorpe@gmail.com> - 2.2.1~rev1720-1
- Update to latest snapshot.

* Sat Jul 30 2016 Fabio Valentini <decathorpe@gmail.com> - 2.2.1~rev1719-1
- Update to latest snapshot.

* Tue Jul 26 2016 Fabio Valentini <decathorpe@gmail.com> - 2.2.1~rev1718-1
- Update to latest snapshot.

* Mon Jul 25 2016 Fabio Valentini <decathorpe@gmail.com> - 2.2.1~rev1717-1
- Update to latest snapshot.

* Fri Jul 22 2016 Fabio Valentini <decathorpe@gmail.com> - 2.2.1~rev1715-1
- Update to latest snapshot.

* Thu Jul 21 2016 Fabio Valentini <decathorpe@gmail.com> - 2.2.1~rev1714-1
- Update to latest snapshot.

* Mon Jul 18 2016 Fabio Valentini <decathorpe@gmail.com> - 2.2.1~rev1713-1
- Update to latest snapshot.

* Wed Jul 13 2016 Fabio Valentini <decathorpe@gmail.com> - 2.2.1~rev1711-1
- Update to latest snapshot.

* Mon Jul 11 2016 Fabio Valentini <decathorpe@gmail.com> - 2.2.1~rev1710-1
- Update to latest snapshot.

* Sun Jul 10 2016 Fabio Valentini <decathorpe@gmail.com> - 2.2.1~rev1708-1
- Update to latest snapshot.

* Sat Jul 09 2016 Fabio Valentini <decathorpe@gmail.com> - 2.2.1~rev1707-1
- Update to latest snapshot.

* Fri Jul 08 2016 Fabio Valentini <decathorpe@gmail.com> - 2.2.1~rev1706-1
- Update to latest snapshot.

* Wed Jul 06 2016 Fabio Valentini <decathorpe@gmail.com> - 2.2.1~rev1705-2
- Update for packaging changes.

* Fri Jun 24 2016 Fabio Valentini <decathorpe@gmail.com> - 2.2.1~rev1695-1
- Update to latest snapshot.

* Thu Jun 23 2016 Fabio Valentini <decathorpe@gmail.com> - 2.2.1~rev1694-1
- Update to latest snapshot.

* Mon Jun 20 2016 Fabio Valentini <decathorpe@gmail.com> - 2.2.1~rev1693-1
- Update to latest snapshot.

* Sun Jun 19 2016 Fabio Valentini <decathorpe@gmail.com> - 2.2.1~rev1692-1
- Update to latest snapshot.

* Sat Jun 18 2016 Fabio Valentini <decathorpe@gmail.com> - 2.2.1~rev1691-1
- Update to latest snapshot.

* Fri Jun 17 2016 Fabio Valentini <decathorpe@gmail.com> - 2.2.1~rev1690-1
- Update to latest snapshot.

* Thu Jun 16 2016 Fabio Valentini <decathorpe@gmail.com> - 2.2.1~rev1689-1
- Update to latest snapshot.

* Wed Jun 15 2016 Fabio Valentini <decathorpe@gmail.com> - 2.2.1~rev1688-1
- Update to latest snapshot.

* Tue Jun 14 2016 Fabio Valentini <decathorpe@gmail.com> - 2.2.1~rev1687-1
- Update to latest snapshot.

* Mon Jun 13 2016 Fabio Valentini <decathorpe@gmail.com> - 2.2.1~rev1686-1
- Update to latest snapshot.

* Sat Jun 11 2016 Fabio Valentini <decathorpe@gmail.com> - 2.2.1~rev1685-1
- Update to latest snapshot.

* Thu Jun 09 2016 Fabio Valentini <decathorpe@gmail.com> - 2.2.1~rev1684-1
- Update to latest snapshot.

* Mon Jun 06 2016 Fabio Valentini <decathorpe@gmail.com> - 2.2.1~rev1683-1
- Update to latest snapshot.

* Sun Jun 05 2016 Fabio Valentini <decathorpe@gmail.com> - 2.2.1~rev1682-1
- Update to latest snapshot.

* Sat Jun 04 2016 Fabio Valentini <decathorpe@gmail.com> - 2.2.1~rev1681-1
- Update to latest snapshot.

* Fri Jun 03 2016 Fabio Valentini <decathorpe@gmail.com> - 2.2.1~rev1680-1
- Update to latest snapshot.

* Thu Jun 02 2016 Fabio Valentini <decathorpe@gmail.com> - 2.2.1~rev1679-1
- Update to latest snapshot.

* Tue May 31 2016 Fabio Valentini <decathorpe@gmail.com> - 2.2.1~rev1677-1
- Update to latest snapshot.

* Mon May 30 2016 Fabio Valentini <decathorpe@gmail.com> - 2.2.1~rev1676-1
- Update to latest snapshot.

* Sun May 29 2016 Fabio Valentini <decathorpe@gmail.com> - 2.2.1~rev1675-2
- Update for packaging changes.

* Thu May 26 2016 Fabio Valentini <decathorpe@gmail.com> - 2.2.1~rev1675-1
- Update to latest snapshot.

* Wed May 25 2016 Fabio Valentini <decathorpe@gmail.com> - 2.2.1~rev1674-1
- Update to latest snapshot.

* Tue May 24 2016 Fabio Valentini <decathorpe@gmail.com> - 2.2.1~rev1673-1
- Update to latest snapshot.

* Mon May 23 2016 Fabio Valentini <decathorpe@gmail.com> - 2.2.1~rev1672-1
- Update to latest snapshot.

* Sat May 21 2016 Fabio Valentini <decathorpe@gmail.com> - 2.2.1~rev1671-1
- Update to latest snapshot.

* Mon May 16 2016 Fabio Valentini <decathorpe@gmail.com> - 2.2.1~rev1670-1
- Update to latest snapshot.

* Sun May 15 2016 Fabio Valentini <decathorpe@gmail.com> - 2.2.1~rev1669-1
- Update to latest snapshot.

* Tue May 10 2016 Fabio Valentini <decathorpe@gmail.com> - 2.2.1~rev1668-1
- Update to latest snapshot.

* Mon May 09 2016 Fabio Valentini <decathorpe@gmail.com> - 2.2.1~rev1666-1
- Update to latest snapshot.

* Fri May 06 2016 Fabio Valentini <decathorpe@gmail.com> - 2.2.1~rev1665-1
- Update to latest snapshot.

* Wed May 04 2016 Fabio Valentini <decathorpe@gmail.com> - 2.2.1~rev1664-1
- Update to latest snapshot.

* Wed May 04 2016 Fabio Valentini <decathorpe@gmail.com> - 2.2.1~rev1664-1
- Update to latest snapshot.

* Wed May 04 2016 Fabio Valentini <decathorpe@gmail.com> - 2.2.1~rev1662-3
- Remove desktop-file-edit, fix accepted upstream.

* Tue May 03 2016 Fabio Valentini <decathorpe@gmail.com> - 2.2.1~rev1662-2
- Update for packaging changes.

* Tue May 03 2016 Fabio Valentini <decathorpe@gmail.com> - 2.2.1~rev1662-1
- Update to new upstream snapshot.

* Mon May 02 2016 Fabio Valentini <decathorpe@gmail.com> - 2.2.1~rev1661-1
- Update to new upstream snapshot.

* Sun May 01 2016 Fabio Valentini <decathorpe@gmail.com> - 2.2.1~rev1660-1
- Update to new upstream snapshot.

* Sat Apr 30 2016 Fabio Valentini <decathorpe@gmail.com> - 2.2.1~rev1659-1
- Update to new upstream snapshot.

* Fri Apr 29 2016 Fabio Valentini <decathorpe@gmail.com> - 2.2.1~rev1658-1
- Update to new upstream snapshot.

* Thu Apr 28 2016 Fabio Valentini <decathorpe@gmail.com> - 2.2.1~rev1657-1
- Update to new upstream snapshot.

* Sat Apr 23 2016 Fabio Valentini <decathorpe@gmail.com> - 2.2.1~rev1656-1
- Update to new upstream snapshot.

* Thu Apr 14 2016 Fabio Valentini <decathorpe@gmail.com> - 2.2.1~rev1654-1
- Update to new upstream snapshot.

* Wed Apr 13 2016 Fabio Valentini <decathorpe@gmail.com> - 2.2.1~rev1653-1
- Update to new upstream snapshot.

* Tue Mar 29 2016 Fabio Valentini <decathorpe@gmail.com> - 2.2.1~rev1652-1
- Update to new upstream snapshot.

* Sun Mar 27 2016 Fabio Valentini <decathorpe@gmail.com> - 2.2.1~rev1650-1
- Update to new upstream snapshot.

* Fri Mar 25 2016 Fabio Valentini <decathorpe@gmail.com> - 2.2.1~rev1649-1
- Update to new upstream snapshot.

* Mon Mar 21 2016 Fabio Valentini <decathorpe@gmail.com> - 2.2.1~rev1648-1
- Update to new upstream snapshot.

* Sat Mar 19 2016 Fabio Valentini <decathorpe@gmail.com> - 2.2.1~rev1646-1
- Update to new upstream snapshot.

* Thu Mar 17 2016 Fabio Valentini <decathorpe@gmail.com> - 2.2.1~rev1645-1
- Update to new upstream snapshot.

* Tue Mar 15 2016 Fabio Valentini <decathorpe@gmail.com> - 2.2.1~rev1644-1
- Update to new upstream snapshot.

* Mon Mar 14 2016 Fabio Valentini <decathorpe@gmail.com> - 2.2.1~rev1643-1
- Update to new upstream snapshot.

* Sun Mar 13 2016 Fabio Valentini <decathorpe@gmail.com> - 2.2.1~rev1642-1
- Update to new upstream snapshot.

* Sat Mar 12 2016 Fabio Valentini <decathorpe@gmail.com> - 2.2.1~rev1641-1
- Update to new upstream snapshot.

* Mon Mar 07 2016 Fabio Valentini <decathorpe@gmail.com> - 2.2.1~rev1640-1
- Update to new upstream snapshot.

* Sat Mar 05 2016 Fabio Valentini <decathorpe@gmail.com> - 2.2.1~rev1639-1
- Update to new upstream snapshot.

* Fri Mar 04 2016 Fabio Valentini <decathorpe@gmail.com> - 2.2.1~rev1638-1
- Update to new upstream snapshot.

* Wed Mar 02 2016 Fabio Valentini <decathorpe@gmail.com> - 2.2.1~rev1637-1
- Update to new upstream snapshot.

* Fri Feb 26 2016 Fabio Valentini <decathorpe@gmail.com> - 2.2.1~rev1636-1
- Update to new upstream snapshot.

* Wed Feb 24 2016 Fabio Valentini <decathorpe@gmail.com> - 2.2.1~rev1635-1
- Update to new upstream snapshot.

* Sat Feb 20 2016 Fabio Valentini <decathorpe@gmail.com> - 2.2.1~rev1634-1
- Update to new upstream snapshot.

* Thu Feb 18 2016 Fabio Valentini <decathorpe@gmail.com> - 2.2.1~rev1631-1
- Update to new upstream snapshot.

* Mon Feb 15 2016 Fabio Valentini <decathorpe@gmail.com> - 2.2.1~rev1630-1
- Update to new upstream snapshot.

* Sat Feb 13 2016 Fabio Valentini <decathorpe@gmail.com> - 2.2.1~rev1629-1
- Update to new upstream snapshot.

* Thu Feb 11 2016 Fabio Valentini <decathorpe@gmail.com> - 2.2.1~rev1627-1
- Update to new upstream snapshot.

* Wed Jan 27 2016 Fabio Valentini <decathorpe@gmail.com> - 2.2.1~rev1626-1
- Update to new upstream snapshot.

* Tue Jan 26 2016 Fabio Valentini <decathorpe@gmail.com> - 2.2.1~rev1625-1
- Update to new upstream snapshot.

* Sun Jan 24 2016 Fabio Valentini <decathorpe@gmail.com> - 2.2.1~rev1624-1
- Update to new upstream snapshot.

* Sat Jan 23 2016 Fabio Valentini <decathorpe@gmail.com> - 2.2.1~rev1623-1
- Update to new upstream snapshot.

* Fri Jan 22 2016 Fabio Valentini <decathorpe@gmail.com> - 2.2.1~rev1622-1
- Update to new upstream snapshot.

* Mon Jan 18 2016 Fabio Valentini <decathorpe@gmail.com> - 2.2.1~rev1621-1
- Update to new upstream snapshot.

* Sun Jan 17 2016 Fabio Valentini <decathorpe@gmail.com> - 2.2.1~rev1620-1
- Update to new upstream snapshot.

* Sat Jan 16 2016 Fabio Valentini <decathorpe@gmail.com> - 2.2.1~rev1619-1
- Update to new upstream snapshot.

* Thu Jan 14 2016 Fabio Valentini <decathorpe@gmail.com> - 2.2.1~rev1618-1
- Update to new upstream snapshot.

* Tue Jan 12 2016 Fabio Valentini <decathorpe@gmail.com> - 2.2.1~rev1617-1
- Update to new upstream snapshot.

* Mon Jan 11 2016 Fabio Valentini <decathorpe@gmail.com> - 2.2.1~rev1616-1
- Update to new upstream snapshot.

* Tue Jan 05 2016 Fabio Valentini <decathorpe@gmail.com> - 2.2.1~rev1614-1
- Update to new upstream snapshot.

* Sun Jan 03 2016 Fabio Valentini <decathorpe@gmail.com> - 2.2.1~rev1613-1
- Update to new upstream snapshot.

* Fri Jan 01 2016 Fabio Valentini <decathorpe@gmail.com> - 2.2.1~rev1612-1
- Update to new upstream snapshot.

* Thu Dec 31 2015 Fabio Valentini <decathorpe@gmail.com> - 2.2.1~rev1611-1
- Update to new upstream snapshot.

* Mon Dec 28 2015 Fabio Valentini <decathorpe@gmail.com> - 2.2.1~rev1610-1
- Update to new upstream snapshot.

* Sun Dec 27 2015 Fabio Valentini <decathorpe@gmail.com> - 2.2.1~rev1609-1
- Update to new upstream snapshot.

* Tue Dec 22 2015 Fabio Valentini <decathorpe@gmail.com> - 2.2.1~rev1608-1
- Update to new upstream snapshot.

* Mon Dec 21 2015 Fabio Valentini <decathorpe@gmail.com> - 2.2.1~rev1607-2
- Add BR: pkgconfig(gtkspell3-3.0), enable spell checking support, fix build by
  including new gschema file.

* Mon Dec 21 2015 Fabio Valentini <decathorpe@gmail.com> - 2.2.1~rev1607-1
- Update to new upstream snapshot.

* Sun Dec 20 2015 Fabio Valentini <decathorpe@gmail.com> - 2.2.1~rev1606-1
- Update to new upstream snapshot.

* Fri Dec 18 2015 Fabio Valentini <decathorpe@gmail.com> - 2.2.1~rev1604-1
- Update to new upstream snapshot.

* Sun Dec 13 2015 Fabio Valentini <decathorpe@gmail.com> - 2.2.1~rev1602-1
- Update to new upstream snapshot.

* Sun Dec 13 2015 Fabio Valentini <decathorpe@gmail.com> - 2.2.1~rev1601-2
- Add appdata file and check to spec. Modernize spec.

* Sat Dec 12 2015 Fabio Valentini <decathorpe@gmail.com> - 2.2.1~rev1601-1
- Update to new upstream snapshot.

* Tue Dec 08 2015 Fabio Valentini <decathorpe@gmail.com> - 2.2.1~rev1600-1
- Update to new upstream snapshot.

* Mon Dec 07 2015 Fabio Valentini <decathorpe@gmail.com> - 2.2.1~rev1599-1
- Update to new upstream snapshot.

* Sun Dec 06 2015 Fabio Valentini <decathorpe@gmail.com> - 2.2.1~rev1598-1
- Update to new upstream snapshot.

* Mon Nov 30 2015 Fabio Valentini <decathorpe@gmail.com> - 2.2.1~rev1596-1
- Update to new upstream snapshot.

* Thu Nov 26 2015 Fabio Valentini <decathorpe@gmail.com> - 2.2.1~rev1595-1
- Update to new upstream snapshot.

* Mon Nov 23 2015 Fabio Valentini <decathorpe@gmail.com> - 2.2.1~rev1594-1
- Update to new upstream snapshot.

* Sun Nov 22 2015 Fabio Valentini <decathorpe@gmail.com> - 2.2.1~rev1593-1
- Update to new upstream snapshot.

* Tue Nov 17 2015 Fabio Valentini <decathorpe@gmail.com> - 2.2.1~rev1592-1
- Update to new upstream snapshot.

* Mon Nov 16 2015 Fabio Valentini <decathorpe@gmail.com> - 2.2.1~rev1591-1
- Update to new upstream snapshot.

* Sat Nov 14 2015 Fabio Valentini <decathorpe@gmail.com> - 2.2.1~rev1590-1
- Update to new upstream snapshot.

* Tue Nov 10 2015 Fabio Valentini <decathorpe@gmail.com> - 2.2.1~rev1589-1
- Update to new upstream snapshot.

* Wed Nov 04 2015 Fabio Valentini <decathorpe@gmail.com> - 2.2.1~rev1586-1
- Update to new upstream snapshot.

* Tue Nov 03 2015 Fabio Valentini <decathorpe@gmail.com> - 2.2.1~rev1584-1
- Update to new upstream snapshot.

* Mon Nov 02 2015 Fabio Valentini <decathorpe@gmail.com> - 2.2.1~rev1583-1
- Update to new upstream snapshot.

* Sat Oct 31 2015 Fabio Valentini <decathorpe@gmail.com> - 2.2.1~rev1582-1
- Update to new upstream snapshot.

* Wed Oct 28 2015 Fabio Valentini <decathorpe@gmail.com> - 2.2.1~rev1580-1
- Update to new upstream snapshot.

* Sat Oct 24 2015 Fabio Valentini <decathorpe@gmail.com> - 2.2.1~rev1579-1
- Update to new upstream snapshot.

* Wed Oct 21 2015 Fabio Valentini <decathorpe@gmail.com> - 2.2.1~rev1578-1
- Update to new upstream snapshot.

* Tue Oct 20 2015 Fabio Valentini <decathorpe@gmail.com> - 2.2.1~rev1577-1
- Update to new upstream snapshot.

* Sun Oct 18 2015 Fabio Valentini <decathorpe@gmail.com> - 2.2.1~rev1576-1
- Update to new upstream snapshot.

* Sat Oct 17 2015 Fabio Valentini <decathorpe@gmail.com> - 2.2.1~rev1574-1
- Update to new upstream snapshot.

* Thu Oct 15 2015 Fabio Valentini <decathorpe@gmail.com> - 2.2.1~rev1573-1
- Update to new upstream snapshot.

* Wed Oct 14 2015 Fabio Valentini <decathorpe@gmail.com> - 2.2.1~rev1572-1
- Update to new upstream snapshot.

* Sun Oct 11 2015 Fabio Valentini <decathorpe@gmail.com> - 2.2.1~rev1571-1
- Update to new upstream snapshot.

* Sat Oct 10 2015 Fabio Valentini <decathorpe@gmail.com> - 2.2.1~rev1570-1
- Update to new upstream snapshot.

* Thu Oct 08 2015 Fabio Valentini <decathorpe@gmail.com> - 2.2.1~rev1569-1
- Update to new upstream snapshot.

* Sat Oct 03 2015 Fabio Valentini <decathorpe@gmail.com> - 2.2.1~rev1568-1
- Update to new upstream snapshot.

* Fri Oct 02 2015 Fabio Valentini <decathorpe@gmail.com> - 2.2.1~rev1567-1
- Update to new upstream snapshot.

* Wed Sep 30 2015 Fabio Valentini <decathorpe@gmail.com> - 2.2.1~rev1562-1
- Update to new upstream snapshot.

* Tue Sep 29 2015 Fabio Valentini <decathorpe@gmail.com> - 2.2.1~rev1561-1
- Update to new upstream snapshot.

* Sun Sep 27 2015 Fabio Valentini <decathorpe@gmail.com> - 2.2.1~rev1560-1
- Update to new upstream snapshot.

* Mon Sep 21 2015 Fabio Valentini <decathorpe@gmail.com> - 2.2.1~rev1559-1
- Update to new upstream snapshot.

* Sat Sep 19 2015 Fabio Valentini <decathorpe@gmail.com> - 2.2.1~rev1558-1
- Update to new upstream snapshot.

* Fri Sep 18 2015 Fabio Valentini <decathorpe@gmail.com> - 2.2.1~rev1557-1
- Update to new upstream snapshot.

* Wed Sep 16 2015 Fabio Valentini <decathorpe@gmail.com> - 2.2.1~rev1556-1
- Update to new upstream snapshot.

* Mon Sep 14 2015 Fabio Valentini <decathorpe@gmail.com> - 2.2.1~rev1554-1
- Update to new upstream snapshot.

* Sun Sep 13 2015 Fabio Valentini <decathorpe@gmail.com> - 2.2.1~rev1553-2
- Update spec for f23.

* Fri Sep 11 2015 Fabio Valentini <decathorpe@gmail.com> - 2.2.1~rev1553-1
- Update to new upstream snapshot.

* Fri Sep 04 2015 Fabio Valentini <decathorpe@gmail.com> - 2.2.1~rev1552-2
- rebuild trigger for granite soname bump

* Thu Sep 03 2015 Fabio Valentini <decathorpe@gmail.com> - 2.2.1~rev1552-1
- Bump to version 2.2.1.

* Thu Sep 03 2015 Fabio Valentini <decathorpe@gmail.com> - 2.2.0~rev1552-1
- Update to new upstream snapshot.

* Tue Sep 01 2015 Fabio Valentini <decathorpe@gmail.com> - 2.2.0~rev1549-1
- Update to new upstream snapshot.

* Fri Aug 21 2015 Fabio Valentini <decathorpe@gmail.com> - 2.2.0~rev1547-1
- Update to new upstream snapshot.

* Thu Aug 20 2015 Fabio Valentini <decathorpe@gmail.com> - 2.2.0~rev1546-1
- Update to new upstream snapshot.

* Tue Aug 18 2015 Fabio Valentini - 2.2.0~rev1544-1
- Update to new upstream snapshot.

* Tue Aug 18 2015 Fabio Valentini - 2.2.0~rev1544-1
- Update to new upstream snapshot.

* Mon Aug 17 2015 Fabio Valentini - 2.2.0~rev1542-1
- Update to new upstream snapshot.

* Sat Aug 01 2015 Fabio Valentini - 2.2.0~rev1534-1
- Update to bzr snapshot revno 1534.

* Thu Jul 30 2015 Fabio Valentini <decathorpe@gmail.com> - 2.2.0~rev1533-1
- Update to bzr snapshot revno 1533.

* Wed Jul 29 2015 Fabio Valentini <decathorpe@gmail.com> - 2.2.0~rev1532-1
- Update to bzr snapshot revno 1532.

* Thu Jul 23 2015 Fabio Valentini <decathorpe@gmail.com> - 2.2.0~rev1529-1
- Update to bzr snapshot revno 1529.

* Sat Jul 18 2015 Fabio Valentini <decathorpe@gmail.com> - 2.2.0~rev1527-1
- Initial package.


