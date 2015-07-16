%define rev 36
%define debug_package %{nil}

Summary: A notifications indicator for wingpanel
Name: wingpanel-indicator-notifications
Version: 0.1~rev%{rev}
Release: 1%{?dist}
License: GPLv3
URL: http://launchpad.net/wingpanel-indicator-notifications

Source0: %{name}-%{version}.tar.gz

BuildRequires: cmake pkgconfig
BuildRequires: vala gettext

BuildRequires: pkgconfig(gdk-pixbuf-2.0)
BuildRequires: pkgconfig(gio-2.0)
BuildRequires: pkgconfig(granite)
BuildRequires: pkgconfig(libwnck-3.0)
BuildRequires: pkgconfig(wingpanel-2.0)


%description
A notifications indicator for wingpanel.


%prep
%setup -q


%build
%cmake


%install
make install DESTDIR=$RPM_BUILD_ROOT
%find_lang notifications-indicator-indicator


%clean
rm -rf $RPM_BUILD_ROOT


%post
/sbin/ldconfig
/usr/bin/glib-compile-schemas %{_datadir}/glib-2.0/schemas &> /dev/null


%postun
/sbin/ldconfig
/usr/bin/glib-compile-schemas %{_datadir}/glib-2.0/schemas &> /dev/null


%files -f notifications-indicator-indicator.lang
%{_libdir}/wingpanel/libnotifications-indicator.so
%{_datadir}/glib-2.0/schemas/org.pantheon.desktop.wingpanel.indicators.notifications.gschema.xml


%changelog
* Thu Jul 16 2015 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev36-1
- Update to bzr snapshot revno 36.

* Tue Jul 14 2015 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev35-1
- Initial package.


