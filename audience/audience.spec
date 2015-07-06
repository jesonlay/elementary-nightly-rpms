%define rev 529

Summary: Audience video player
Name: audience
Version: 0.1.0.1~rev%{rev}
Release: 0%{?dist}
License: GPLv3
URL: http://launchpad.net/audience

Source0: %{name}-%{version}.tar.gz

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


%install
make install DESTDIR=$RPM_BUILD_ROOT

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
%{_bindir}/audience

%{_datadir}/applications/audience.desktop
%{_datadir}/glib-2.0/schemas/org.pantheon.audience.gschema.xml


%changelog
* Sat Mar 07 2015 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev498-5
- Update to latest bzr snapshot.

* Sun Feb 01 2015 Fabio Valentini (fafa) <decathorpe@gmail.com> - 0.1~rev485-4
- Update to latest bzr snapshot.

* Sun Jan 18 2015 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev482-3
- Update to latest bzr snapshot.

* Thu Jan 08 2015 Fabio Valentini <fafatheone@gmail.com> - 0.1~rev481-2
- Update to latest bzr snapshot.

* Mon Jan 05 2015 Fabio Valentini <fafatheone@gmail.com> - 0.1~rev479-1
- Update to bzr revision 479.

* Sat Jan 03 2015 Fabio Valentini <fafatheone@gmail.com> - 0.1~rev477-1
- Initial package.
