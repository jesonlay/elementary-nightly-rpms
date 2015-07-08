Summary: Indicator Display Objects
Name: ido
Version: 12.10.2
Release: 0%{?dist}
License: LGPLv3
URL: http://launchpad.net/ido

Source0: %{name}-%{version}.tar.gz
Source1: make-srpm.sh

BuildRequires: libtool pkgconfig
BuildRequires: pkgconfig(gtk+-3.0)


%description
Widgets and other objects used for indicators.


%package devel
Summary: Indicator Display Objects development headers
%description devel
Widgets and other objects used for indicators. This package contains the development headers.


%prep
%setup -q


%build
# export CFLAGS="-Wno-error"
%configure


%install
make install DESTDIR=$RPM_BUILD_ROOT
rm $RPM_BUILD_ROOT/%{_libdir}/*.la


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
%{_libdir}/libido3-0.1.so.0
%{_libdir}/libido3-0.1.so.0.0.0


%files devel
%{_libdir}/libido3-0.1.so
%{_libdir}/pkgconfig/libido3-0.1.pc

%{_includedir}/libido3-0.1/

%changelog
* Sat Jan 03 2015 Fabio Valentini <fafatheone@gmail.com> - 0.3.4-2
- Clean up spec file.

* Fri Jan 02 2015 Fabio Valentini <fafatheone@gmail.com> - 0.3.4-1
- Initial package.


