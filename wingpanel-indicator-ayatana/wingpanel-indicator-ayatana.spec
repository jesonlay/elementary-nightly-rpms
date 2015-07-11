%define rev 10

Summary: A meta plugin for ayatana application indicator support for wingpanel
Name: wingpanel-indicator-ayatana
Version: 0.1~rev%{rev}
Release: 0%{?dist}
License: GPLv3
URL: http://launchpad.net/wingpanel-indicator-ayatana

Source0: %{name}-%{version}.tar.gz

BuildRequires: cmake pkgconfig
BuildRequires: vala gettext


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


%changelog

