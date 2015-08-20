%define rev 864

Summary: Granite Toolkit
Name: granite
Version: 0.3.0~rev%{rev}
Release: 1%{?dist}
License: LGPLv3
URL: http://launchpad.net/granite

Source0: %{name}-%{version}.tar.gz
Source1: %{name}.conf

BuildRequires: cmake
BuildRequires: vala gettext
BuildRequires: desktop-file-utils

BuildRequires: pkgconfig(gee-0.8)
BuildRequires: pkgconfig(glib-2.0)
BuildRequires: pkgconfig(gtk+-3.0)
BuildRequires: pkgconfig(gobject-introspection-1.0)

Requires: hicolor-icon-theme


%description
Granite is a library of toolkit addons to GTK+ and is part of the elementary project.


%package devel
Summary: Granite Toolkit development headers
%description devel
Granite Toolkit development headers


%prep
%setup -q


%build
%cmake


%install
make install DESTDIR=$RPM_BUILD_ROOT
%find_lang granite

desktop-file-validate $RPM_BUILD_ROOT/%{_datadir}/applications/granite-demo.desktop


%clean
rm -rf $RPM_BUILD_ROOT


%post
/sbin/ldconfig

%postun
/sbin/ldconfig


%files -f granite.lang
%{_libdir}/libgranite.so.2
%{_libdir}/libgranite.so.2.0.1
%{_libdir}/girepository-1.0/Granite-1.0.typelib

%{_datadir}/icons/hicolor/16x16/actions/appointment.svg
%{_datadir}/icons/hicolor/16x16/actions/open-menu.svg
%{_datadir}/icons/hicolor/22x22/actions/open-menu.svg
%{_datadir}/icons/hicolor/24x24/actions/appointment.svg
%{_datadir}/icons/hicolor/24x24/actions/open-menu.svg
%{_datadir}/icons/hicolor/32x32/actions/open-menu.svg
%{_datadir}/icons/hicolor/48x48/actions/open-menu.svg
%{_datadir}/icons/hicolor/scalable/actions/open-menu-symbolic.svg


%files devel
%{_bindir}/granite-demo
%{_libdir}/libgranite.so
%{_libdir}/pkgconfig/granite.pc

%{_includedir}/granite

%{_datadir}/applications/granite-demo.desktop
%{_datadir}/gir-1.0/Granite-1.0.gir
%{_datadir}/vala/vapi/granite.deps
%{_datadir}/vala/vapi/granite.vapi


%changelog
* Thu Aug 20 2015 Fabio Valentini <decathorpe@gmail.com> - 0.3.0~rev864-1
- Update to new upstream snapshot.

* Thu Jun 25 2015 Fabio Valentini <decathorpe@gmail.com> - 0.3.0~rev861-1
- Update to bzr snapshot revno861.

* Sat Mar 07 2015 Fabio Valentini <decathorpe@gmail.com> - 0.3.0~rev839-5
- Update to latest bzr snapshot.

* Sun Feb 08 2015 Fabio Valentini <decathorpe@gmail.com> - 0.3.0~rev831-4
- Update to latest bzr snapshot.

* Sun Feb 01 2015 Fabio Valentini <decathorpe@gmail.com> - 0.3.0~rev829-3
- Update to latest bzr snapshot.

* Thu Jan 08 2015 Fabio Valentini <fafatheone@gmail.com> - 0.3.0~rev826-2
- Update to latest bzr snapshot.

* Mon Jan 05 2015 Fabio Valentini <fafatheone@gmail.com> - 0.3.0~rev825-1
- Fix upstream version.

* Sat Jan 03 2015 Fabio Valentini <fafatheone@gmail.com> - 0.2.3~rev825-1
- Initial package (new).
