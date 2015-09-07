%define rev 1388

Summary: Stupidly simple Dock
Name: plank
Version: 0.9.1~rev%{rev}
Release: 1%{?dist}
License: GPLv3
URL: http://launchpad.net/plank

Source0: %{name}-%{version}.tar.gz
Source1: %{name}.conf

BuildRequires: desktop-file-utils
BuildRequires: gettext
BuildRequires: libappstream-glib
BuildRequires: libtool
BuildRequires: vala
BuildRequires: vala-tools

BuildRequires: pkgconfig(cairo) >= 1.10
BuildRequires: pkgconfig(dbusmenu-glib-0.4)
BuildRequires: pkgconfig(dbusmenu-gtk3-0.4)
BuildRequires: pkgconfig(gdk-x11-3.0) >= 3.4.0
BuildRequires: pkgconfig(gdk-pixbuf-2.0) >= 2.26.0
BuildRequires: pkgconfig(gee-0.8)
BuildRequires: pkgconfig(gio-2.0) >= 2.32.0
BuildRequires: pkgconfig(gio-unix-2.0) >= 2.32.0
BuildRequires: pkgconfig(glib-2.0) >= 2.32.0
BuildRequires: pkgconfig(gobject-2.0) >= 2.32.0
BuildRequires: pkgconfig(gthread-2.0) >= 2.32.0
BuildRequires: pkgconfig(gtk+-3.0) >= 3.4.0
BuildRequires: pkgconfig(libbamf3) >= 0.2.92
BuildRequires: pkgconfig(libwnck-3.0)
BuildRequires: pkgconfig(x11)


%description
Plank is meant to be the simplest dock on the planet. The goal is to provide just what a dock needs and absolutely nothing more. It is, however, a library which can be extended to create other dock programs with more advanced features.
Thus, Plank is the underlying technology for Docky (starting in version 3.0.0) and aims to provide all the core features while Docky extends it to add fancier things like Docklets, painters, settings dialogs, etc.


%package libs
Summary: Stupidly simple Dock (shared libraries)
%description libs
Plank is meant to be the simplest dock on the planet. The goal is to provide just what a dock needs and absolutely nothing more. It is, however, a library which can be extended to create other dock programs with more advanced features.
Thus, Plank is the underlying technology for Docky (starting in version 3.0.0) and aims to provide all the core features while Docky extends it to add fancier things like Docklets, painters, settings dialogs, etc.
This package contains the shared libraries.


%package devel
Summary: Stupidly simple Dock (development files)
%description devel
Plank is meant to be the simplest dock on the planet. The goal is to provide just what a dock needs and absolutely nothing more. It is, however, a library which can be extended to create other dock programs with more advanced features.
Thus, Plank is the underlying technology for Docky (starting in version 3.0.0) and aims to provide all the core features while Docky extends it to add fancier things like Docklets, painters, settings dialogs, etc.
This package contains development headers and files.


%prep
%setup -q


%build
./autogen.sh
%configure
%make_build


%install
%make_install
rm -r $RPM_BUILD_ROOT/%{_sysconfdir}
rm -r $RPM_BUILD_ROOT/%{_libdir}/libplank.la
rm -r $RPM_BUILD_ROOT/%{_datadir}/apport
%find_lang plank


%check
desktop-file-validate $RPM_BUILD_ROOT/%{_datadir}/applications/plank.desktop
appstream-util validate-relax --nonet $RPM_BUILD_ROOT/%{_datadir}/appdata/plank.appdata.xml


%clean
rm -rf $RPM_BUILD_ROOT


%post
/sbin/ldconfig
/usr/bin/glib-compile-schemas %{_datadir}/glib-2.0/schemas &> /dev/null

%postun
/sbin/ldconfig
/usr/bin/glib-compile-schemas %{_datadir}/glib-2.0/schemas &> /dev/null


%post libs
/sbin/ldconfig

%postun libs
/sbin/ldconfig


%post devel
/sbin/ldconfig

%postun devel
/sbin/ldconfig


%files -f plank.lang
%{_bindir}/plank

%{_datadir}/appdata/plank.appdata.xml
%{_datadir}/applications/plank.desktop
%{_datadir}/icons/hicolor/16x16/apps/plank.svg
%{_datadir}/icons/hicolor/22x22/apps/plank.svg
%{_datadir}/icons/hicolor/24x24/apps/plank.svg
%{_datadir}/icons/hicolor/32x32/apps/plank.svg
%{_datadir}/icons/hicolor/48x48/apps/plank.svg
%{_datadir}/icons/hicolor/64x64/apps/plank.svg
%{_datadir}/icons/hicolor/128x128/apps/plank.svg
%{_datadir}/plank

%{_mandir}/man1/plank.1.gz

%files libs
%{_libdir}/libplank.so.0
%{_libdir}/libplank.so.0.0.0

%files devel
%{_includedir}/plank
%{_libdir}/libplank.so
%{_libdir}/pkgconfig/plank.pc

%{_datadir}/vala/vapi/plank.deps
%{_datadir}/vala/vapi/plank.vapi


%changelog
* Mon Sep 07 2015 Fabio Valentini <decathorpe@gmail.com> - 0.9.1~rev1388-1
- Update to new upstream snapshot.

* Thu Sep 03 2015 Fabio Valentini <decathorpe@gmail.com> - 0.9.1~rev1384-1
- Initial package.


