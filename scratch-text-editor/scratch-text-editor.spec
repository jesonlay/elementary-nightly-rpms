%define rev 1553

Summary: Scratch - the text editor that works.
Name: scratch-text-editor
Version: 2.2.1~rev%{rev}
Release: 2%{?dist}
License: GPLv3
URL: http://launchpad.net/scratch

Source0: %{name}-%{version}.tar.gz
Source1: %{name}.conf

BuildRequires: cmake pkgconfig
BuildRequires: vala gettext
BuildRequires: desktop-file-utils

BuildRequires: pkgconfig(gee-0.8)
BuildRequires: pkgconfig(gio-2.0)
BuildRequires: pkgconfig(glib-2.0)
BuildRequires: pkgconfig(gobject-2.0)
BuildRequires: pkgconfig(granite) >= 0.3.0
BuildRequires: pkgconfig(gthread-2.0)
BuildRequires: pkgconfig(gtksourceview-3.0) >= 3.10
BuildRequires: pkgconfig(gtk+-3.0) >= 3.10
BuildRequires: pkgconfig(libpeas-1.0)
BuildRequires: pkgconfig(libpeas-gtk-1.0)
BuildRequires: pkgconfig(libsoup-2.4)

%if %{fedora} > 22
BuildRequires: pkgconfig(libvala-0.30)
%else
BuildRequires: pkgconfig(libvala-0.28)
%endif

BuildRequires: pkgconfig(vte-2.91)
BuildRequires: pkgconfig(webkitgtk-3.0)
BuildRequires: pkgconfig(zeitgeist-2.0)


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


%package devel
Summary: Scratch - the text editor that works.
%description devel
Scratch is the text editor that works for you. It auto-saves your files, meaning they're always up-to-date. Plus it remembers your tabs so you never lose your spot, even in between sessions. This package contains the development headers.


%prep
%setup -q


%build
%cmake


%install
make install DESTDIR=$RPM_BUILD_ROOT

desktop-file-edit $RPM_BUILD_ROOT/%{_datadir}/applications/scratch-text-editor.desktop --set-key=Keywords --set-value='Notepad;IDE;Plain;'

desktop-file-validate $RPM_BUILD_ROOT/%{_datadir}/applications/scratch-text-editor.desktop

%find_lang scratch-text-editor


%clean
rm -rf $RPM_BUILD_ROOT


%post
/sbin/ldconfig
/usr/bin/glib-compile-schemas %{_datadir}/glib-2.0/schemas &> /dev/null

%postun
/sbin/ldconfig
/usr/bin/glib-compile-schemas %{_datadir}/glib-2.0/schemas &> /dev/null


%post devel
/sbin/ldconfig

%postun devel
/sbin/ldconfig


%files -f scratch-text-editor.lang
%{_bindir}/scratch-text-editor

%{_libdir}/scratch
%{_libdir}/libscratchcore.so.0
%{_libdir}/libscratchcore.so.0.0

%{_datadir}/applications/scratch-text-editor.desktop

%{_datadir}/glib-2.0/schemas/org.pantheon.scratch.gschema.xml
%{_datadir}/glib-2.0/schemas/org.pantheon.scratch.plugins.file-manager.gschema.xml
%{_datadir}/glib-2.0/schemas/org.pantheon.scratch.plugins.folder-manager.gschema.xml
%{_datadir}/glib-2.0/schemas/org.pantheon.scratch.plugins.terminal.gschema.xml

%{_datadir}/scratch


%files devel
%{_includedir}/scratch

%{_libdir}/libscratchcore.so
%{_libdir}/pkgconfig/scratchcore.pc

%{_datadir}/vala/vapi/scratchcore.deps
%{_datadir}/vala/vapi/scratchcore.vapi


%changelog
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


