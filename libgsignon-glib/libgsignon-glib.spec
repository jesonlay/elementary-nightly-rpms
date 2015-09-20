%define rev ccbb6376
%define date 150920

Summary: GLib-based client library for Online Accounts Single Sign-On service
Name: libgsignon-glib
Version: 2.4.0~git%{date}~%{rev}
Release: 0%{?dist}
License: LGPLv2.1
URL: https://01.org/gSSO

Source0: %{name}-%{version}.tar.gz
Source1: %{name}.conf

BuildRequires: libtool pkgconfig
BuildRequires: gtk-doc

BuildRequires: pkgconfig(gio-2.0) >= 2.30
BuildRequires: pkgconfig(gio-unix-2.0)
BuildRequires: pkgconfig(glib-2.0) >= 2.32
BuildRequires: pkgconfig(gobject-2.0)
BuildRequires: pkgconfig(gobject-introspection-1.0)
BuildRequires: pkgconfig(gthread-2.0)


%description
gSSO is a glib-based reimplementation of the single sign-on daemon and authentication plugins with advanced access control and other improvements.


%package devel
Summary: libgsignon-glib development headers
%description devel
gSSO is a glib-based reimplementation of the single sign-on daemon and authentication plugins with advanced access control and other improvements.


%prep
%setup -q


%build
./autogen.sh
%configure
%make_build


%install
%make_install

rm $RPM_BUILD_ROOT/%{_libdir}/libgsignon-glib.la


%clean
rm -rf $RPM_BUILD_ROOT


%post
/sbin/ldconfig

%postun
/sbin/ldconfig


%post devel
/sbin/ldconfig

%postun devel
/sbin/ldconfig


%files
%{_libdir}/libgsignon-glib.so.1
%{_libdir}/libgsignon-glib.so.1.0.0
%{_libdir}/girepository-1.0/gSignon-1.0.typelib


%files devel
%{_bindir}/gsso-example
%{_libdir}/libgsignon-glib.so
%{_libdir}/pkgconfig/libgsignon-glib.pc
%{_includedir}/libgsignon-glib
%{_datadir}/gir-1.0/gSignon-1.0.gir


%changelog
* Sat Sep 19 2015 Fabio Valentini <decathorpe@gmail.com> - 2.4.0~git150919~ccbb6376-1
- Update to git snapshot of 2.4.0.

* Sat Jul 04 2015 Fabio Valentini <decathorpe@gmail.com> - 2.2.0-1
- Initial package.


