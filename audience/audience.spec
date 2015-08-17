%define rev 534

Summary: Audience video player
Name: audience
Version: 0.1.0.2~rev%{rev}
Release: 1%{?dist}
License: GPLv3
URL: http://launchpad.net/audience

Source0: %{name}-%{version}.tar.gz
Source1: %{name}.conf

BuildRequires: cmake pkgconfig
BuildRequires: vala gettext

BuildRequires: pkgconfig(clutter-gtk-1.0)
BuildRequires: pkgconfig(glib-2.0)
BuildRequires: pkgconfig(granite)
BuildRequires: pkgconfig(gstreamer-1.0)
BuildRequires: pkgconfig(gstreamer-pbutils-1.0)
BuildRequires: pkgconfig(gstreamer-tag-1.0)
BuildRequires: pkgconfig(gtk+-3.0)
BuildRequires: pkgconfig(libnotify)


%description
A modern video player that brings the lessons learned from the web home to the desktop.


%prep
%setup -q


%build
%cmake
%make_build


%install
%make_install

%find_lang audience


%clean
rm -rf $RPM_BUILD_ROOT


%post
/sbin/ldconfig
/usr/bin/glib-compile-schemas %{_datadir}/glib-2.0/schemas &> /dev/null

%postun
/sbin/ldconfig
/usr/bin/glib-compile-schemas %{_datadir}/glib-2.0/schemas &> /dev/null


%files -f audience.lang
%doc AUTHORS README
%license COPYING

%{_bindir}/audience

%{_datadir}/applications/audience.desktop
%{_datadir}/glib-2.0/schemas/org.pantheon.audience.gschema.xml


%changelog
* Sun Aug 16 2015 Fabio Valentini - 0.1.0.2~rev534-1
- Bump to correct upstream version (0.1.0.2).

* Sun Aug 16 2015 Fabio Valentini - 0.1.0.1~rev534-1
- Update to upstream bzr snapshot revno 534.

* Wed Jul 29 2015 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.1~rev531-1
- Update to bzr snapshot revno 531.

* Fri Jul 24 2015 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.1~rev529-2
- Use %doc and %license macros.

* Fri Jul 24 2015 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.1~rev529-1
- Update to bzr snapshot revno 529.
- Use more spec macros.

* Sat Mar 07 2015 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev498-5
- Update to latest bzr snapshot.

* Sun Feb 01 2015 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev485-4
- Update to latest bzr snapshot.

* Sun Jan 18 2015 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev482-3
- Update to latest bzr snapshot.

* Thu Jan 08 2015 Fabio Valentini <fafatheone@gmail.com> - 0.1~rev481-2
- Update to latest bzr snapshot.

* Mon Jan 05 2015 Fabio Valentini <fafatheone@gmail.com> - 0.1~rev479-1
- Update to bzr revision 479.

* Sat Jan 03 2015 Fabio Valentini <fafatheone@gmail.com> - 0.1~rev477-1
- Initial package.
