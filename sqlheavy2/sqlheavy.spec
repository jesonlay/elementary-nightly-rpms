Summary: SQLHeavy
Name: sqlheavy
Version: 0.1.2~git
Release: 1%{?dist}
License: LGPLv3
URL: http://code.google.com/p/sqlheavy

Source0: %{name}-%{version}.tar.gz
Source1: make-srpm.sh

BuildRequires: libtool pkgconfig
BuildRequires: vala gettext

BuildRequires: pkgconfig(glib-2.0)
BuildRequires: pkgconfig(gobject-introspection-1.0)
BuildRequires: pkgconfig(sqlite3)


%description
SQLHeavy is a wrapper on top of SQLite with a GObject-based interface.


%package devel
Summary: sqlheavy development headers
%description devel
SQLHeavy development headers



%prep
%setup -q


%build
./autogen.sh

%configure


%install
rm -rf $RPM_BUILD_ROOT

make install DESTDIR=$RPM_BUILD_ROOT

rm $RPM_BUILD_ROOT/%{_libdir}/libsqlheavy0.2.a
rm $RPM_BUILD_ROOT/%{_libdir}/libsqlheavy0.2.la


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
%{_libdir}/libsqlheavy0.2.so.0
%{_libdir}/libsqlheavy0.2.so.0.0.0
%{_libdir}/girepository-1.0/SQLHeavy-0.2.typelib


%files devel
%{_libdir}/libsqlheavy0.2.so
%{_libdir}/pkgconfig/sqlheavy-0.2.pc

%{_includedir}/sqlheavy/

%{_datarootdir}/gir-1.0/SQLHeavy-0.2.gir
%{_datarootdir}/vala/vapi/sqlheavy-0.2.deps
%{_datarootdir}/vala/vapi/sqlheavy-0.2.vapi

%{_mandir}/man1/sqlheavy-gen-orm.1.gz


%changelog
* Sat Jan 03 2015 Fabio Valentini <fafatheone@gmail.com> - 0.1.2~git-1
- Initial package.


