Summary: libindicate library
Name: libindicate
Version: 12.10.1
Release: 1%{?dist}
License: LGPLv2.1, LGPLv3
URL: http://launchpad.net/libindicate

Source0: %{name}-%{version}.tar.gz

BuildRequires: libtool pkgconfig
BuildRequires: vala vala-tools gettext

BuildRequires: pkgconfig(dbus-glib-1)
BuildRequires: pkgconfig(dbusmenu-glib-0.4)
BuildRequires: pkgconfig(glib-2.0)
BuildRequires: pkgconfig(gtk+-3.0)
BuildRequires: pkgconfig(gobject-introspection-1.0)


%description
A small library for applications to raise "flags" on DBus for other components of the desktop to pick up and visualize. Currently used by the messaging indicator.


%package gtk3
Summary: libindicate gtk3 library
%description gtk3
A small library for applications to raise "flags" on DBus for other components of the desktop to pick up and visualize. Currently used by the messaging indicator.


%package gtk3-devel
Summary: libindicate gtk3 development headers
%description gtk3-devel
A small library for applications to raise "flags" on DBus for other components of the desktop to pick up and visualize. Currently used by the messaging indicator.


%package devel
Summary: libindicate development headers
%description devel
A small library for applications to raise "flags" on DBus for other components of the desktop to pick up and visualize. Currently used by the messaging indicator.


%package devel-docs
Summary: libindicate development documentation
%description devel-docs
A small library for applications to raise "flags" on DBus for other components of the desktop to pick up and visualize. Currently used by the messaging indicator.


%prep
%setup -q


%build
%configure --enable-introspection --disable-doc --disable-python


%install
make install DESTDIR=$RPM_BUILD_ROOT

rm $RPM_BUILD_ROOT/%{_libdir}/*.a
rm $RPM_BUILD_ROOT/%{_libdir}/*.la


%clean
rm -rf $RPM_BUILD_ROOT


%post
/sbin/ldconfig
%postun
/sbin/ldconfig


%post gtk3
/sbin/ldconfig
%postun gtk3
/sbin/ldconfig


%post gtk3-devel
/sbin/ldconfig
%postun gtk3-devel
/sbin/ldconfig


%post devel
/sbin/ldconfig
%postun devel
/sbin/ldconfig


%files
%{_libdir}/libindicate.so.5
%{_libdir}/libindicate.so.5.0.7
%{_libdir}/girepository-1.0/Indicate-0.7.typelib
%{_datarootdir}/gir-1.0/Indicate-0.7.gir


%files gtk3
%{_libdir}/libindicate-gtk3.so.3
%{_libdir}/libindicate-gtk3.so.3.0.3
%{_libdir}/girepository-1.0/IndicateGtk3-0.7.typelib
%{_datarootdir}/gir-1.0/IndicateGtk3-0.7.gir


%files gtk3-devel
%{_libdir}/libindicate-gtk3.so
%{_libdir}/pkgconfig/indicate-gtk3-0.7.pc
%{_includedir}/libindicate-gtk3-0.7/
%{_datarootdir}/vala/vapi/IndicateGtk3-0.7.vapi


%files devel
%{_libdir}/libindicate.so
%{_libdir}/pkgconfig/indicate-0.7.pc
%{_includedir}/libindicate-0.7/
%{_datarootdir}/vala/vapi/Indicate-0.7.vapi


%files devel-docs
%{_datarootdir}/doc/libindicate/


%changelog
* Fri Jan 09 2015 Fabio Valentini <fafatheone@gmail.com> - 12.10.1-1
- Initial package.


