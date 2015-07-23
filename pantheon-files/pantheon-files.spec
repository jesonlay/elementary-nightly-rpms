%define rev 1898

Summary: Pantheon file manager
Name: pantheon-files
Version: 0.2.2.1~rev%{rev}
Release: 0%{?dist}
License: GPLv3
URL: http://launchpad.net/pantheon-files

Source0: %{name}-%{version}.tar.gz

BuildRequires: cmake pkgconfig
BuildRequires: vala gettext

BuildRequires: desktop-file-utils


%description
The simple, powerful, and sexy file manager from elementary.
Designed for elementary OS.


%package devel
Summary: pantheon-files development headers
%description devel
The simple, powerful, and sexy file manager from elementary.
This package contains the development headers.


%prep
%setup -q


%build
%cmake


%install
# desktop-file-validate $RPM_BUILD_ROOT/%{_datadir}/applications/noise.desktop

# %%find_lang noise


%clean
rm -rf $RPM_BUILD_ROOT


%post
/sbin/ldconfig
/usr/bin/glib-compile-schemas %{_datarootdir}/glib-2.0/schemas &> /dev/null

%postun
/sbin/ldconfig
/usr/bin/glib-compile-schemas %{_datarootdir}/glib-2.0/schemas &> /dev/null


%post devel
/sbin/ldconfig

%postun devel
/sbin/ldconfig


%files
# %%files -f noise.lang


%files devel


%changelog

