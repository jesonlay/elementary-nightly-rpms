%define rev 31
%define debug_package %{nil}

Summary: A session indicator for wingpanel
Name: wingpanel-indicator-session
Version: 0.1~rev%{rev}
Release: 0%{?dist}
License: GPLv3
URL: http://launchpad.net/wingpanel-indicator-session

Source0: %{name}-%{version}.tar.gz
Source1: %{name}.conf

BuildRequires: cmake pkgconfig
BuildRequires: vala gettext

BuildRequires: pkgconfig(accountsservice)
BuildRequires: pkgconfig(gio-2.0)
BuildRequires: pkgconfig(gobject-introspection-1.0)
BuildRequires: pkgconfig(granite)
BuildRequires: pkgconfig(gthread-2.0)
BuildRequires: pkgconfig(gtk+-3.0)
BuildRequires: pkgconfig(wingpanel-2.0)


%description
A session indicator for wingpanel.


%prep
%setup -q


%build
%cmake


%install
make install DESTDIR=$RPM_BUILD_ROOT
%find_lang session-indicator


%clean
rm -rf $RPM_BUILD_ROOT


%post
/sbin/ldconfig


%postun
/sbin/ldconfig


%files -f session-indicator.lang
%{_libdir}/wingpanel/libsession.so


%changelog
* Fri Aug 21 2015 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev31-1
- Update to new upstream snapshot.

* Mon Aug 17 2015 Fabio Valentini - 0.1~rev30-1
- Update to new upstream snapshot.

* Sat Aug 01 2015 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev30-1
- Update to bzr snapshot revno 30.

* Thu Jul 16 2015 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev28-1
- Update to bzr snapshot revno 28.

* Tue Jul 14 2015 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev23-1
- Initial package.


