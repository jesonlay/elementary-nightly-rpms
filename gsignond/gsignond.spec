%define rev 466

Summary: Online Accounts Sign-on glib daemon
Name: gsignond
Version: 1.0.4~rev%{rev}
Release: 0%{?dist}
License: LGPLv2.1
URL: http://launchpad.net/gsignond

Source0: %{name}-%{version}.tar.gz

BuildRequires: libtool pkgconfig
BuildRequires: gtk-doc gettext

BuildRequires: pkgconfig(glib-2.0) >= 2.32


%description
gSSO is a glib-based reimplementation of the single sign-on daemon and authentication plugins with advanced access control and other improvements. The original SSO daemon is written using Qt.


%package devel
Summary: libgsignon-glib development headers
%description devel
gSSO is a glib-based reimplementation of the single sign-on daemon and authentication plugins with advanced access control and other improvements. The original SSO daemon is written using Qt. This package contains the development headers. 


%prep
%setup -q


%build
./autogen.sh --verbose
%configure --verbose


%install
make install DESTDIR=$RPM_BUILD_ROOT


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


%files devel


%changelog

