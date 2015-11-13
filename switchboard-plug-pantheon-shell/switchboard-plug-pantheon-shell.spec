%define rev 400
%define debug_package %{nil}

Summary: Switchboard System Settings Pantheon Shell Plug
Name: switchboard-plug-pantheon-shell
Version: 0.2.1~rev%{rev}
Release: 1%{?dist}
License: GPLv3
URL: http://launchpad.net/switchboard-plug-pantheon-shell

Source0: %{name}-%{version}.tar.gz
Source1: %{name}.conf

BuildRequires: cmake
BuildRequires: desktop-file-utils
BuildRequires: gettext
BuildRequires: vala

BuildRequires: pkgconfig(glib-2.0)
BuildRequires: pkgconfig(gnome-desktop-3.0)
BuildRequires: pkgconfig(granite)
BuildRequires: pkgconfig(gtk+-3.0) >= 3.14
BuildRequires: pkgconfig(plank) >= 0.7.1.1137
BuildRequires: pkgconfig(switchboard-2.0)

Requires: contractor


%description
Modular Desktop Settings Hub Pantheon Shell Plug


%prep
%setup -q


%build
%cmake
%make_build


%install
%make_install
%find_lang pantheon-desktop-plug


%check


%clean
rm -rf $RPM_BUILD_ROOT


%post
%postun


%files -f pantheon-desktop-plug.lang
%{_bindir}/set-wallpaper
%{_libdir}/switchboard/personal/pantheon-desktop
%{_datadir}/contractor/set-wallpaper.contract


%changelog
* Fri Nov 13 2015 Fabio Valentini <decathorpe@gmail.com> - 0.2.1~rev400-1
- Update to new upstream snapshot.

* Wed Nov 11 2015 Fabio Valentini <decathorpe@gmail.com> - 0.2.1~rev399-1
- Update to new upstream snapshot.

* Sat Nov 07 2015 Fabio Valentini <decathorpe@gmail.com> - 0.2.1~rev398-1
- Update to new upstream snapshot.

* Thu Nov 05 2015 Fabio Valentini <decathorpe@gmail.com> - 0.2.1~rev397-1
- Update to new upstream snapshot.

* Mon Nov 02 2015 Fabio Valentini <decathorpe@gmail.com> - 0.2.1~rev396-1
- Update to new upstream snapshot.

* Sat Oct 31 2015 Fabio Valentini <decathorpe@gmail.com> - 0.2.1~rev394-1
- Update to new upstream snapshot.

* Fri Oct 23 2015 Fabio Valentini <decathorpe@gmail.com> - 0.2.1~rev392-1
- Update to new upstream snapshot.

* Thu Oct 22 2015 Fabio Valentini <decathorpe@gmail.com> - 0.2.1~rev391-1
- Update to new upstream snapshot.

* Wed Oct 21 2015 Fabio Valentini <decathorpe@gmail.com> - 0.2.1~rev390-1
- Update to new upstream snapshot.

* Tue Oct 20 2015 Fabio Valentini <decathorpe@gmail.com> - 0.2.1~rev389-1
- Update to new upstream snapshot.

* Sat Oct 10 2015 Fabio Valentini <decathorpe@gmail.com> - 0.2.1~rev388-1
- Update to new upstream snapshot.

* Thu Oct 08 2015 Fabio Valentini <decathorpe@gmail.com> - 0.2.1~rev386-1
- Update to new upstream snapshot.

* Mon Oct 05 2015 Fabio Valentini <decathorpe@gmail.com> - 0.2.1~rev385-1
- Update to new upstream snapshot.

* Sat Oct 03 2015 Fabio Valentini <decathorpe@gmail.com> - 0.2.1~rev384-1
- Update to new upstream snapshot.

* Mon Sep 28 2015 Fabio Valentini <decathorpe@gmail.com> - 0.2.1~rev383-1
- Update to new upstream snapshot.

* Sun Sep 27 2015 Fabio Valentini <decathorpe@gmail.com> - 0.2.1~rev382-1
- Update to new upstream snapshot.

* Sat Sep 26 2015 Fabio Valentini <decathorpe@gmail.com> - 0.2.1~rev381-1
- Update to new upstream snapshot.

* Wed Sep 23 2015 Fabio Valentini <decathorpe@gmail.com> - 0.2.1~rev380-1
- Update to new upstream snapshot.

* Tue Sep 22 2015 Fabio Valentini <decathorpe@gmail.com> - 0.2.1~rev379-2
- Add Req:contractor, new contract file and new set-wallpaper binary to spec.

* Mon Sep 21 2015 Fabio Valentini <decathorpe@gmail.com> - 0.2.1~rev379-1
- Update to new upstream snapshot.

* Mon Sep 21 2015 Fabio Valentini <decathorpe@gmail.com> - 0.2.1~rev377-1
- Remove no longer shipped desktop file. Modernize spec.

* Mon Sep 07 2015 Fabio Valentini <decathorpe@gmail.com> - 0.2.1~rev369-1
- Update to new upstream snapshot.

* Fri Sep 04 2015 Fabio Valentini <decathorpe@gmail.com> - 0.2.1~rev368-1
- Update to new upstream snapshot.

* Fri Sep 04 2015 Fabio Valentini <decathorpe@gmail.com> - 0.2.1~rev367-2
- rebuild trigger for granite soname bump

* Thu Sep 03 2015 Fabio Valentini <decathorpe@gmail.com> - 0.2.1~rev367-1
- Bump to version 0.2.1.

* Thu Sep 03 2015 Fabio Valentini <decathorpe@gmail.com> - 0.2.0.3~rev367-1
- Update to new upstream snapshot.

* Fri Aug 21 2015 Fabio Valentini <decathorpe@gmail.com> - 0.2.0.3~rev365-1
- Initial package.



