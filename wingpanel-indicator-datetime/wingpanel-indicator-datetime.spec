%define rev 63
%define debug_package %{nil}

Summary: A datetime indicator for wingpanel
Name: wingpanel-indicator-datetime
Version: 0.1~rev%{rev}
Release: 1%{?dist}
License: GPLv3
URL: http://launchpad.net/wingpanel-indicator-ayatana

Source0: %{name}-%{version}.tar.gz

BuildRequires: cmake pkgconfig
BuildRequires: vala gettext

BuildRequires: pkgconfig(granite)
BuildRequires: pkgconfig(gthread-2.0)
BuildRequires: pkgconfig(gtk+-3.0) 
BuildRequires: pkgconfig(indicator3-0.4)
BuildRequires: pkgconfig(wingpanel-2.0)


%description
A datetime indicator for wingpanel


%prep
%setup -q


%build
%cmake


%install
make install DESTDIR=$RPM_BUILD_ROOT

%find_lang datetime-indicator

%clean
rm -rf $RPM_BUILD_ROOT


%post
/sbin/ldconfig


%postun
/sbin/ldconfig



%files -f datetime-indicator.lang
%{_libdir}/wingpanel/libdatetime.so


%changelog
* Sat Aug 01 2015 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev63-1
- Update to bzr snapshot revno 63.

* Thu Jul 16 2015 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev55-1
- Update to bzr snapshot revno 55.

* Tue Jul 14 2015 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev54-1
- Initial package.


