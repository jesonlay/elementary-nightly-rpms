Summary:        Scratch - the text editor that works.
Name:           scratch-text-editor
Version:        2.3~rev%{rev}
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
BuildRequires:  vala-devel

BuildRequires:  pkgconfig(gee-0.8)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(granite) >= 0.3.0
BuildRequires:  pkgconfig(gtksourceview-3.0) >= 3.10
BuildRequires:  pkgconfig(gtkspell3-3.0)
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.10
BuildRequires:  pkgconfig(libpeas-1.0)
BuildRequires:  pkgconfig(libpeas-gtk-1.0)
BuildRequires:  pkgconfig(libsoup-2.4)
BuildRequires:  pkgconfig(vte-2.91)
BuildRequires:  pkgconfig(webkitgtk-3.0)
BuildRequires:  pkgconfig(zeitgeist-2.0)


%description
Scratch is the text editor that works for you. It auto-saves your files, meaning they're always up-to-date. Plus it remembers your tabs so you never lose your spot, even in between sessions.

Make it yours. Scratch is written from the ground up to be extensible. Keep things super lightweight and simple, or install extensions to turn Scratch into a full-blown IDE; it's your choice. And with a handful of useful preferences, you can tweak the behavior and interface to your liking.

It's elementary. Scratch is made to be the perfect text editor for elementary, meaning it closely follows the high standards of design, speed, and consistency. It's sexy, but not distracting.

Works with your language. Whether you're crafting code in Vala, scripting with PHP, or marking things up in HTML, Scratch has you covered. Experience full syntax highlighting with nearly all programming, scripting, and markup languages.

Other syntax-highlighted languages: Bash, C, C%#, C++. Cmake, CSS, .Desktop, Diff, Fortran, Gettext, ini, Java, JavaScript, LaTex, Lua, Makefile, Objective C, Pascal, Perl, Python, Ruby, XML.

Additional features include:

 * syntax highlighting with gtksourceview-3
 * a find bar to search the words in the files
 * strong integration with Granite framework by elementary-team
 * tab and split documents system
 * lots of others

Scratch needs to be translated. Go to Translations to help us providing this software in your language!

Designed for elementary OS. Works and looks great on any GTK+ desktop.


%package        devel
Summary: Scratch - the text editor that works.
%description    devel
Scratch is the text editor that works for you. It auto-saves your files, meaning they're always up-to-date. Plus it remembers your tabs so you never lose your spot, even in between sessions. This package contains the development headers.


%prep
%autosetup


%build
%cmake
%make_build


%install
%make_install
%find_lang scratch-text-editor


%check
desktop-file-validate %{buildroot}/%{_datadir}/applications/*.desktop

# appstream-util validate-relax --nonet $RPM_BUILD_ROOT/%{_datadir}/appdata/*.appdata.xml


%clean
rm -rf %{buildroot}


%post
/usr/sbin/ldconfig
/usr/bin/update-desktop-database &> /dev/null || :

%postun
/usr/sbin/ldconfig
/usr/bin/update-desktop-database &> /dev/null || :
if [ $1 -eq 0 ] ; then
    /usr/bin/glib-compile-schemas %{_datadir}/glib-2.0/schemas &> /dev/null || :
fi

%posttrans
/usr/bin/glib-compile-schemas %{_datadir}/glib-2.0/schemas &> /dev/null || :


%post   devel -p /usr/sbin/ldconfig
%postun devel -p /usr/sbin/ldconfig


%files -f scratch-text-editor.lang
%doc HACKING README
%license COPYING

%{_bindir}/scratch-text-editor

%{_libdir}/scratch/
%{_libdir}/libscratchcore.so.0
%{_libdir}/libscratchcore.so.0.0

%{_datadir}/appdata/scratch-text-editor.appdata.xml
%{_datadir}/applications/scratch-text-editor.desktop

%{_datadir}/glib-2.0/schemas/org.pantheon.scratch.gschema.xml
%{_datadir}/glib-2.0/schemas/org.pantheon.scratch.plugins.file-manager.gschema.xml
%{_datadir}/glib-2.0/schemas/org.pantheon.scratch.plugins.folder-manager.gschema.xml
%{_datadir}/glib-2.0/schemas/org.pantheon.scratch.plugins.spell.gschema.xml
%{_datadir}/glib-2.0/schemas/org.pantheon.scratch.plugins.terminal.gschema.xml

%{_datadir}/scratch/


%files          devel
%{_includedir}/scratch

%{_libdir}/libscratchcore.so
%{_libdir}/pkgconfig/scratchcore.pc

%{_datadir}/vala/vapi/scratchcore.deps
%{_datadir}/vala/vapi/scratchcore.vapi


%changelog
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


