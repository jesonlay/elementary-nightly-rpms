%define rev 769

Summary: The terminal of the 21st century.
Name: pantheon-terminal
Version: 0.3.1.3~rev%{rev}
Release: 1%{?dist}
License: GPLv3
URL: http://launchpad.net/pantheon-terminal

Source0: %{name}-%{version}.tar.gz
Source1: %{name}.conf

BuildRequires: cmake pkgconfig
BuildRequires: vala gettext

BuildRequires: pkgconfig(gdk-3.0)
BuildRequires: pkgconfig(granite) >= 0.3.0
BuildRequires: pkgconfig(gthread-2.0)
BuildRequires: pkgconfig(gtk+-3.0) >= 3.9.10
BuildRequires: pkgconfig(libnotify)
BuildRequires: pkgconfig(vte-2.91)


#Requires: contractor


%description
A super lightweight, beautiful, and simple terminal. It's designed to be setup with sane defaults and little to no configuration. It's just a terminal, nothing more, nothing less.

Designed for elementary OS.


%prep
%autosetup


%build
export CFLAGS="-fPIC"
export CXXFLAGS="-fPIC"
export LDFLAGS="-fPIC"

%cmake
%make_build


%install
%make_install
%find_lang pantheon-terminal


%clean
rm -rf $RPM_BUILD_ROOT


%post
/usr/bin/glib-compile-schemas %{_datadir}/glib-2.0/schemas &> /dev/null

%postun
/usr/bin/glib-compile-schemas %{_datadir}/glib-2.0/schemas &> /dev/null


%files -f pantheon-terminal.lang
%{_bindir}/pantheon-terminal

%{_datadir}/applications/open-pantheon-terminal-here.desktop
%{_datadir}/applications/pantheon-terminal.desktop

%{_datadir}/glib-2.0/schemas/org.pantheon.terminal.gschema.xml

%dir %{_datadir}/pantheon-terminal
%{_datadir}/pantheon-terminal/enable-fish-completion-notifications
%{_datadir}/pantheon-terminal/enable-zsh-completion-notifications


%changelog
* Sun Nov 15 2015 Fabio Valentini <decathorpe@gmail.com> - 0.3.1.3~rev769-1
- Update to new upstream snapshot.

* Sat Nov 14 2015 Fabio Valentini <decathorpe@gmail.com> - 0.3.1.3~rev768-1
- Update to new upstream snapshot.

* Fri Nov 13 2015 Fabio Valentini <decathorpe@gmail.com> - 0.3.1.3~rev767-1
- Update to new upstream snapshot.

* Mon Nov 09 2015 Fabio Valentini <decathorpe@gmail.com> - 0.3.1.3~rev766-1
- Update to new upstream snapshot.

* Fri Oct 23 2015 Fabio Valentini <decathorpe@gmail.com> - 0.3.1.3~rev765-1
- Update to new upstream snapshot.

* Wed Oct 21 2015 Fabio Valentini <decathorpe@gmail.com> - 0.3.1.3~rev764-1
- Update to new upstream snapshot.

* Mon Oct 19 2015 Fabio Valentini <decathorpe@gmail.com> - 0.3.1.3~rev763-1
- Update to new upstream snapshot.

* Sun Oct 18 2015 Fabio Valentini <decathorpe@gmail.com> - 0.3.1.3~rev762-1
- Update to new upstream snapshot.

* Wed Oct 14 2015 Fabio Valentini <decathorpe@gmail.com> - 0.3.1.3~rev761-1
- Update to new upstream snapshot.

* Thu Oct 08 2015 Fabio Valentini <decathorpe@gmail.com> - 0.3.1.3~rev760-1
- Update to new upstream snapshot.

* Sat Oct 03 2015 Fabio Valentini <decathorpe@gmail.com> - 0.3.1.3~rev758-1
- Update to new upstream snapshot.

* Fri Oct 02 2015 Fabio Valentini <decathorpe@gmail.com> - 0.3.1.3~rev757-1
- Update to new upstream snapshot.

* Tue Sep 29 2015 Fabio Valentini <decathorpe@gmail.com> - 0.3.1.3~rev756-1
- Update to new upstream snapshot.

* Sun Sep 27 2015 Fabio Valentini <decathorpe@gmail.com> - 0.3.1.3~rev755-1
- Update to new upstream snapshot.

* Fri Sep 25 2015 Fabio Valentini <decathorpe@gmail.com> - 0.3.1.3~rev754-3
- Try to fix f23-x64 build.

* Tue Sep 22 2015 Fabio Valentini <decathorpe@gmail.com> - 0.3.1.3~rev754-2
- Change BR:vte-2.90 to BR:vte-291.

* Mon Sep 21 2015 Fabio Valentini <decathorpe@gmail.com> - 0.3.1.3~rev754-1
- Update to new upstream snapshot.

* Sun Sep 06 2015 Fabio Valentini <decathorpe@gmail.com> - 0.3.1.3~rev752-1
- Update to new upstream snapshot.

* Fri Sep 04 2015 Fabio Valentini <decathorpe@gmail.com> - 0.3.1.3~rev751-2
- rebuild trigger for granite soname bump

* Thu Sep 03 2015 Fabio Valentini <decathorpe@gmail.com> - 0.3.1.3~rev751-1
- Update to new upstream snapshot.

* Tue Sep 01 2015 Fabio Valentini <decathorpe@gmail.com> - 0.3.1.3~rev750-1
- Update to new upstream snapshot.

* Thu Aug 20 2015 Fabio Valentini <decathorpe@gmail.com> - 0.3.1.3~rev749-1
- Update to new upstream snapshot.

* Wed Aug 19 2015 Fabio Valentini <decathorpe@gmail.com> - 0.3.1.3~rev748-1
- Initial package.



