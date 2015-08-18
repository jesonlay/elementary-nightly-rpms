%define rev 12
%define debug_package %{nil}

Summary: A meta plugin for ayatana application indicator support for wingpanel
Name: wingpanel-indicator-ayatana
Version: 0.1~rev%{rev}
Release: 1%{?dist}
License: GPLv3
URL: http://launchpad.net/wingpanel-indicator-ayatana

Source0: %{name}-%{version}.tar.gz
Source1: %{name}.conf

BuildRequires: cmake pkgconfig
BuildRequires: vala gettext

BuildRequires: pkgconfig(granite)
BuildRequires: pkgconfig(indicator3-0.4)
BuildRequires: pkgconfig(wingpanel-2.0)


%description
A meta plugin for ayatana application indicator support for wingpanel.


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
%{_libdir}/wingpanel/libayatana_compatibility.so


%changelog
* Mon Aug 17 2015 Fabio Valentini - 0.1~rev12-1
- Update to new upstream snapshot.

* Sat Aug 01 2015 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev11-1
- Update to bzr snapshot revno 11.

* Tue Jul 14 2015 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev10-1
- Initial package.


