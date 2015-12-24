%define rev 195
%define debug_package %{nil}

Summary: Switchboard System Settings Networking Plug
Name: switchboard-plug-networking
Version: 0.1~rev%{rev}
Release: 1%{?dist}
License: GPLv3
URL: http://launchpad.net/switchboard-plug-networking

Source0: %{name}-%{version}.tar.gz
Source1: %{name}.conf

BuildRequires: cmake
BuildRequires: gettext
BuildRequires: vala

BuildRequires: pkgconfig(granite)
BuildRequires: pkgconfig(gthread-2.0)
BuildRequires: pkgconfig(gtk+-3.0) >= 3.12
BuildRequires: pkgconfig(libnm-glib)
BuildRequires: pkgconfig(libnm-gtk)
BuildRequires: pkgconfig(polkit-gobject-1)
BuildRequires: pkgconfig(switchboard-2.0)


%description
Modular Desktop Settings Hub Network Plug


%prep
%setup -q


%build
%cmake
%make_build


%install
%make_install
%find_lang pantheon-network-plug


%check


%clean
rm -rf $RPM_BUILD_ROOT


%post
%postun


%files -f pantheon-network-plug.lang
%{_libdir}/switchboard/network/pantheon-network


%changelog
* Thu Dec 24 2015 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev195-1
- Update to new upstream snapshot.

* Wed Dec 23 2015 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev194-1
- Update to new upstream snapshot.

* Tue Dec 22 2015 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev193-1
- Update to new upstream snapshot.

* Sun Dec 20 2015 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev191-1
- Update to new upstream snapshot.

* Tue Dec 15 2015 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev189-1
- Update to new upstream snapshot.

* Sun Dec 13 2015 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev188-1
- Update to new upstream snapshot.

* Fri Dec 11 2015 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev187-1
- Update to new upstream snapshot.

* Wed Dec 09 2015 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev186-1
- Update to new upstream snapshot.

* Tue Dec 08 2015 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev185-1
- Update to new upstream snapshot.

* Mon Dec 07 2015 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev184-1
- Update to new upstream snapshot.

* Sun Dec 06 2015 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev183-1
- Update to new upstream snapshot.

* Tue Dec 01 2015 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev182-1
- Update to new upstream snapshot.

* Mon Nov 30 2015 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev181-1
- Update to new upstream snapshot.

* Thu Nov 26 2015 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev180-1
- Update to new upstream snapshot.

* Thu Nov 19 2015 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev178-1
- Update to new upstream snapshot.

* Tue Nov 17 2015 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev177-1
- Update to new upstream snapshot.

* Fri Nov 13 2015 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev176-1
- Update to new upstream snapshot.

* Tue Nov 10 2015 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev175-1
- Update to new upstream snapshot.

* Mon Nov 09 2015 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev174-1
- Update to new upstream snapshot.

* Sat Oct 31 2015 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev173-1
- Update to new upstream snapshot.

* Thu Oct 29 2015 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev171-1
- Update to new upstream snapshot.

* Wed Oct 21 2015 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev170-1
- Update to new upstream snapshot.

* Tue Oct 20 2015 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev168-1
- Update to new upstream snapshot.

* Thu Oct 15 2015 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev167-1
- Update to new upstream snapshot.

* Sat Oct 10 2015 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev166-1
- Update to new upstream snapshot.

* Sat Oct 10 2015 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev165-1
- Update to new upstream snapshot.

* Mon Sep 28 2015 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev164-1
- Update to new upstream snapshot.

* Sun Sep 27 2015 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev163-1
- Update to new upstream snapshot.

* Wed Sep 23 2015 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev162-1
- Update to new upstream snapshot.

* Fri Sep 11 2015 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev160-1
- Update to new upstream snapshot.

* Mon Sep 07 2015 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev158-1
- Update to new upstream snapshot.

* Fri Sep 04 2015 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev156-1
- Update to new upstream snapshot.

* Fri Sep 04 2015 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev155-1
- rebuild trigger for granite soname bump

* Sat Aug 22 2015 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev155-1
- Update to new upstream snapshot.

* Fri Aug 21 2015 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev154-1
- Initial package.



