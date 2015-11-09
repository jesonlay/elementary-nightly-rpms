%define rev 595
%define debug_package %{nil}

Summary: Slingshot application launcher
Name: slingshot-launcher
Version: 0.8.1.1~rev%{rev}
Release: 1%{?dist}
License: GPLv3
URL: http://launchpad.net/slingshot

Source0: %{name}-%{version}.tar.gz
Source1: %{name}.conf

BuildRequires: cmake pkgconfig
BuildRequires: vala vala-tools gettext

BuildRequires: pkgconfig(glib-2.0)
BuildRequires: pkgconfig(gtk+-3.0)
BuildRequires: pkgconfig(granite)
BuildRequires: pkgconfig(gee-0.8)
BuildRequires: pkgconfig(switchboard-2.0)

BuildRequires: pkgconfig(libsoup-2.4)
BuildRequires: pkgconfig(zeitgeist-2.0)
BuildRequires: pkgconfig(json-glib-1.0)
BuildRequires: pkgconfig(libgnome-menu-3.0)

# Requires: redhat-menus
Requires: gala
Requires: zeitgeist


%description
Slingshot is Pantheon's application launcher, part of the elementary project.


%prep
%setup -q


%build
export CFLAGS="-fPIC"
export CXXFLAGS="-fPIC"
export LDFLAGS="-fPIC"

%cmake -DUSE_UNITY=OFF
%make_build


%install
%make_install
%find_lang slingshot


%clean
rm -rf $RPM_BUILD_ROOT


%post
/usr/bin/glib-compile-schemas %{_datadir}/glib-2.0/schemas &> /dev/null
 
%postun
/usr/bin/glib-compile-schemas %{_datadir}/glib-2.0/schemas &> /dev/null


%files -f slingshot.lang
%{_bindir}/slingshot-launcher

%{_sysconfdir}/xdg/menus/pantheon-applications.menu
%{_datadir}/glib-2.0/schemas/org.pantheon.desktop.slingshot.gschema.xml


%changelog
* Sat Nov 07 2015 Fabio Valentini <decathorpe@gmail.com> - 0.8.1.1~rev595-1
- Update to new upstream snapshot.

* Mon Nov 02 2015 Fabio Valentini <decathorpe@gmail.com> - 0.8.1.1~rev594-1
- Update to new upstream snapshot.

* Sat Oct 31 2015 Fabio Valentini <decathorpe@gmail.com> - 0.8.1.1~rev592-1
- Update to new upstream snapshot.

* Mon Oct 26 2015 Fabio Valentini <decathorpe@gmail.com> - 0.8.1.1~rev591-1
- Update to new upstream snapshot.

* Thu Oct 22 2015 Fabio Valentini <decathorpe@gmail.com> - 0.8.1.1~rev590-1
- Update to new upstream snapshot.

* Wed Oct 21 2015 Fabio Valentini <decathorpe@gmail.com> - 0.8.1.1~rev589-1
- Update to new upstream snapshot.

* Tue Oct 20 2015 Fabio Valentini <decathorpe@gmail.com> - 0.8.1.1~rev588-1
- Update to new upstream snapshot.

* Thu Oct 08 2015 Fabio Valentini <decathorpe@gmail.com> - 0.8.1.1~rev587-1
- Update to new upstream snapshot.

* Fri Oct 02 2015 Fabio Valentini <decathorpe@gmail.com> - 0.8.1.1~rev586-1
- Update to new upstream snapshot.

* Tue Sep 29 2015 Fabio Valentini <decathorpe@gmail.com> - 0.8.1.1~rev584-1
- Update to new upstream snapshot.

* Mon Sep 28 2015 Fabio Valentini <decathorpe@gmail.com> - 0.8.1.1~rev583-1
- Update to new upstream snapshot.

* Sat Sep 26 2015 Fabio Valentini <decathorpe@gmail.com> - 0.8.1.1~rev581-1
- Update to new upstream snapshot.

* Fri Sep 25 2015 Fabio Valentini <decathorpe@gmail.com> - 0.8.1.1~rev580-2
- Try to fix f23-x64 build.

* Fri Sep 25 2015 Fabio Valentini <decathorpe@gmail.com> - 0.8.1.1~rev580-1
- Update to new upstream snapshot.

* Thu Sep 24 2015 Fabio Valentini <decathorpe@gmail.com> - 0.8.1.1~rev579-1
- Update to new upstream snapshot.

* Wed Sep 23 2015 Fabio Valentini <decathorpe@gmail.com> - 0.8.1.1~rev577-1
- Update to new upstream snapshot.

* Sat Sep 19 2015 Fabio Valentini <decathorpe@gmail.com> - 0.8.1.1~rev576-1
- Update to new upstream snapshot.

* Fri Sep 18 2015 Fabio Valentini <decathorpe@gmail.com> - 0.8.1.1~rev575-1
- Update to new upstream snapshot.

* Thu Sep 17 2015 Fabio Valentini <decathorpe@gmail.com> - 0.8.1.1~rev574-1
- Update to new upstream snapshot.

* Mon Sep 14 2015 Fabio Valentini <decathorpe@gmail.com> - 0.8.1.1~rev572-1
- Update to new upstream snapshot.

* Sun Sep 13 2015 Fabio Valentini <decathorpe@gmail.com> - 0.8.1.1~rev571-2
- Add BR: pkgconfig(switchboard-2.0) to fix build.

* Sun Sep 13 2015 Fabio Valentini <decathorpe@gmail.com> - 0.8.1.1~rev571-1
- Update to new upstream snapshot.

* Sun Sep 13 2015 Fabio Valentini <decathorpe@gmail.com> - 0.8.1.1~rev570-1
- Update to new upstream snapshot.

* Mon Sep 07 2015 Fabio Valentini <decathorpe@gmail.com> - 0.8.1.1~rev569-1
- Update to new upstream snapshot.

* Sun Sep 06 2015 Fabio Valentini <decathorpe@gmail.com> - 0.8.1.1~rev568-1
- Update to new upstream snapshot.

* Fri Sep 04 2015 Fabio Valentini <decathorpe@gmail.com> - 0.8.1.1~rev567-2
- rebuild trigger for granite soname bump

* Thu Sep 03 2015 Fabio Valentini <decathorpe@gmail.com> - 0.8.1.1~rev567-1
- Bump to version 0.8.1.1.

* Thu Sep 03 2015 Fabio Valentini <decathorpe@gmail.com> - 0.8.1~rev567-1
- Update to new upstream snapshot.

* Tue Sep 01 2015 Fabio Valentini <decathorpe@gmail.com> - 0.8.1~rev566-1
- Update to new upstream snapshot.

* Thu Aug 20 2015 Fabio Valentini <decathorpe@gmail.com> - 0.8.1~rev564-1
- Update to new upstream snapshot.

* Wed Aug 19 2015 Fabio Valentini <decathorpe@gmail.com> - 0.8.1~rev562-2
- Add Requires: gala to fix crash.

* Mon Aug 17 2015 Fabio Valentini - 0.8.1~rev562-1
- Update to new upstream snapshot.

* Wed Jul 29 2015 Fabio Valentini <decathorpe@gmail.com> - 0.8.1~rev559-1
- Update to bzr snapshot revno 559.

* Mon Jul 13 2015 Fabio Valentini <decathorpe@gmail.com> - 0.8.1~rev558-1
- Update to bzr snapshot revno 558.

* Tue Jul 07 2015 Fabio Valentini <decathorpe@gmail.com> - 0.8.1~rev557-1
- Update to bzr revno 557.

* Sun Jul 05 2015 Fabio Valentini <decathorpe@gmail.com> - 0.8.1~rev556-1
- Cleanup .spec file. Update to new bzr snapshot.

* Sat Mar 07 2015 Fabio Valentini <decathorpe@gmail.com> - 0.7.6.1~rev512-6
- Update to latest bzr snapshot.

* Wed Feb 04 2015 Fabio Valentini <decathorpe@gmail.com> - 0.7.6.1~rev502-5
- Update to latest bzr snapshot.

* Tue Jan 13 2015 Fabio Valentini <fafatheone@gmail.com> - 0.7.6.1~rev499-4
- Update to latest bzr snapshot.

* Mon Jan 05 2015 Fabio Valentini <fafatheone@gmail.com> - 0.7.6.1~rev497-3
- Require zeitgeist for it's dbus service.

* Mon Jan 05 2015 Fabio Valentini <fafatheone@gmail.com> - 0.7.6.1~rev497-2
- Fix BuildRequires to include pkgconfig(libsoup-2.4).

* Mon Jan 05 2015 Fabio Valentini <fafatheone@gmail.com> - 0.7.6.1~rev497-1
- Initial package.
