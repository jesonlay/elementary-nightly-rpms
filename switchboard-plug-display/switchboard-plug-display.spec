%define rev 125
%define debug_package %{nil}

Summary: Switchboard System Settings Display Plug
Name: switchboard-plug-display
Version: 0.1.1.1~rev%{rev}
Release: 1%{?dist}
License: LGPLv3
URL: http://launchpad.net/switchboard-plug-display

Source0: %{name}-%{version}.tar.gz
Source1: %{name}.conf

BuildRequires: cmake
BuildRequires: desktop-file-utils
BuildRequires: gettext
BuildRequires: vala

BuildRequires: pkgconfig(clutter-1.0)
BuildRequires: pkgconfig(clutter-gtk-1.0)
BuildRequires: pkgconfig(gnome-desktop-3.0)
BuildRequires: pkgconfig(granite)
BuildRequires: pkgconfig(gthread-2.0)
BuildRequires: pkgconfig(gtk+-3.0) >= 3.12
BuildRequires: pkgconfig(switchboard-2.0)


%description
Modular Desktop Settings Hub Display Plug


%prep
%setup -q


%build
%cmake
%make_build


%install
%make_install
%find_lang pantheon-display-plug


%check


%clean
rm -rf $RPM_BUILD_ROOT


%post
%postun


%files -f pantheon-display-plug.lang
%{_libdir}/switchboard/hardware/pantheon-display


%changelog
* Sat Dec 26 2015 Fabio Valentini <decathorpe@gmail.com> - 0.1.1.1~rev125-1
- Update to new upstream snapshot.

* Thu Dec 24 2015 Fabio Valentini <decathorpe@gmail.com> - 0.1.1.1~rev123-1
- Update to new upstream snapshot.

* Wed Dec 23 2015 Fabio Valentini <decathorpe@gmail.com> - 0.1.1.1~rev122-1
- Update to new upstream snapshot.

* Tue Dec 22 2015 Fabio Valentini <decathorpe@gmail.com> - 0.1.1.1~rev121-1
- Update to new upstream snapshot.

* Mon Dec 21 2015 Fabio Valentini <decathorpe@gmail.com> - 0.1.1.1~rev119-1
- Update to new upstream snapshot.

* Tue Dec 08 2015 Fabio Valentini <decathorpe@gmail.com> - 0.1.1.1~rev118-1
- Update to new upstream snapshot.

* Sun Nov 29 2015 Fabio Valentini <decathorpe@gmail.com> - 0.1.1.1~rev117-1
- Update to new upstream snapshot.

* Sat Nov 21 2015 Fabio Valentini <decathorpe@gmail.com> - 0.1.1.1~rev116-1
- Update to new upstream snapshot.

* Sat Nov 21 2015 Fabio Valentini <decathorpe@gmail.com> - 0.1.1.1~rev115-1
- omment=Update version tag to represent upstream version.

* Sun Nov 15 2015 Fabio Valentini <decathorpe@gmail.com> - 0.1.1~rev115-1
- Update to new upstream snapshot.

* Fri Oct 23 2015 Fabio Valentini <decathorpe@gmail.com> - 0.1.1~rev114-1
- Update to new upstream snapshot.

* Wed Oct 21 2015 Fabio Valentini <decathorpe@gmail.com> - 0.1.1~rev113-1
- Update to new upstream snapshot.

* Wed Oct 14 2015 Fabio Valentini <decathorpe@gmail.com> - 0.1.1~rev112-1
- Update to new upstream snapshot.

* Thu Oct 08 2015 Fabio Valentini <decathorpe@gmail.com> - 0.1.1~rev111-1
- Update to new upstream snapshot.

* Tue Sep 22 2015 Fabio Valentini <decathorpe@gmail.com> - 0.1.1~rev109-1
- Update to new upstream snapshot.

* Mon Sep 21 2015 Fabio Valentini <decathorpe@gmail.com> - 0.1.1~rev108-1
- Remove no longer shipped desktop file. Modernize spec.

* Fri Sep 04 2015 Fabio Valentini <decathorpe@gmail.com> - 0.1.1~rev107-2
- rebuild trigger for granite soname bump

* Fri Aug 21 2015 Fabio Valentini <decathorpe@gmail.com> - 0.1.1~rev107-1
- Initial package.


