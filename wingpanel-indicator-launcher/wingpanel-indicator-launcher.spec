%define rev 2
%define debug_package %{nil}

Summary: A launcher indicator for wingpanel
Name: wingpanel-indicator-launcher
Version: 0.1~rev%{rev}
Release: 1%{?dist}
License: GPLv3
URL: http://launchpad.net/wingpanel-indicator-launcher

Source0: %{name}-%{version}.tar.gz
Source1: %{name}.conf

BuildRequires: cmake pkgconfig
BuildRequires: vala gettext

BuildRequires: pkgconfig(granite)
BuildRequires: pkgconfig(gthread-2.0)
BuildRequires: pkgconfig(gtk+-3.0)
BuildRequires: pkgconfig(wingpanel-2.0)


%description
A launcher indicator for wingpanel.


%prep
%setup -q


%build
%cmake


%install
make install DESTDIR=$RPM_BUILD_ROOT


%clean
rm -rf $RPM_BUILD_ROOT


%post
/sbin/ldconfig


%postun
/sbin/ldconfig



%files
%{_libdir}/wingpanel/liblauncher.so


%changelog
* Fri Sep 04 2015 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev2-1
- rebuild trigger for granite soname bump

* Mon Aug 17 2015 Fabio Valentini - 0.1~rev2-1
- Update to new upstream snapshot.

* Tue Jul 14 2015 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev2-1
- Initial package.


