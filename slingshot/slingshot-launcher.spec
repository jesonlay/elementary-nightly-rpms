%define rev 558

Summary: Slingshot application launcher
Name: slingshot-launcher
Version: 0.8.1~rev%{rev}
Release: 1%{?dist}
License: GPLv3
URL: http://launchpad.net/slingshot

Source0: %{name}-%{version}.tar.gz

BuildRequires: cmake pkgconfig
BuildRequires: vala vala-tools gettext

BuildRequires: pkgconfig(glib-2.0)
BuildRequires: pkgconfig(gtk+-3.0)
BuildRequires: pkgconfig(granite)
BuildRequires: pkgconfig(gee-0.8)

BuildRequires: pkgconfig(libsoup-2.4)
BuildRequires: pkgconfig(zeitgeist-2.0)
BuildRequires: pkgconfig(json-glib-1.0)
BuildRequires: pkgconfig(libgnome-menu-3.0)

# Requires: redhat-menus
Requires: zeitgeist


%description
Slingshot is Pantheon's application launcher, part of the elementary project.


%prep
%setup -q


%build
%cmake -DUSE_UNITY=OFF


%install
make install DESTDIR=$RPM_BUILD_ROOT

%find_lang slingshot


%clean
rm -rf $RPM_BUILD_ROOT


%post
/sbin/ldconfig
/usr/bin/glib-compile-schemas %{_datadir}/glib-2.0/schemas &> /dev/null
 
%postun
/sbin/ldconfig
/usr/bin/glib-compile-schemas %{_datadir}/glib-2.0/schemas &> /dev/null


%files -f slingshot.lang
%{_bindir}/slingshot-launcher

%{_sysconfdir}/xdg/menus/pantheon-applications.menu
%{_datadir}/glib-2.0/schemas/org.pantheon.desktop.slingshot.gschema.xml


%changelog
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
