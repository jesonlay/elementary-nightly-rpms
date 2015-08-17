%define rev 310

Summary: GLib-based client library for Online Accounts Single Sign-On service
Name: libgsignon-glib
Version: 2.1.0~rev%{rev}
Release: 1%{?dist}
License: LGPLv2.1
URL: http://launchpad.net/libgsignon-glib

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


%install
make install DESTDIR=$RPM_BUILD_ROOT

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
* Sat Jul 04 2015 Fabio Valentini <decathorpe@gmail.com> - 2.1.0~rev310-1
- Initial package.


