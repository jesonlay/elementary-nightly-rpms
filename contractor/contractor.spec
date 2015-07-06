%define rev 136

Summary: Desktop-wide extension service
Name: contractor
Version: 0.3.1~rev%{rev}
Release: 0%{?dist}
License: GPLv3
URL: http://launchpad.net/contractor

Source0: %{name}-%{version}.tar.gz

BuildRequires: cmake pkgconfig
BuildRequires: vala vala-tools gettext

BuildRequires: pkgconfig(gee-0.8)
BuildRequires: pkgconfig(gio-2.0)
BuildRequires: pkgconfig(gio-unix-2.0)
BuildRequires: pkgconfig(glib-2.0)


%description
An extension service that allows apps to use the exposed functionality of registered apps. This way, apps don't have to have the functions hard coded into them.

Designed for elementary OS.


%prep
%setup -q


%build
%cmake


%install
make install DESTDIR=$RPM_BUILD_ROOT


%clean
rm -rf $RPM_BUILD_ROOT


%post

%postun


%files
%{_bindir}/contractor
%{_datadir}/dbus-1/services/org.elementary.contractor.service


%changelog

