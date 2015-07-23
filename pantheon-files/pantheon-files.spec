%define rev 1898

Summary: Pantheon file manager
Name: pantheon-files
Version: 0.2.2.1~rev%{rev}
Release: 0%{?dist}
License: GPLv3
URL: http://launchpad.net/pantheon-files

Source0: %{name}-%{version}.tar.gz

BuildRequires: cmake
BuildRequires: desktop-file-utils
BuildRequires: gettext
BuildRequires: vala

BuildRequires: pkgconfig(dbus-glib-1)
BuildRequires: pkgconfig(gail-3.0)
BuildRequires: pkgconfig(gee-0.8)
BuildRequires: pkgconfig(gio-2.0)
BuildRequires: pkgconfig(gio-unix-2.0)
BuildRequires: pkgconfig(glib-2.0) >= 2.29
BuildRequires: pkgconfig(gmodule-2.0)
BuildRequires: pkgconfig(granite) >= 0.3.0
BuildRequires: pkgconfig(gthread-2.0)
BuildRequires: pkgconfig(gtk+-3.0) >= 3.10
BuildRequires: pkgconfig(libnotify) >= 0.7.2
BuildRequires: pkgconfig(pango) >= 1.1.2
BuildRequires: pkgconfig(plank)
BuildRequires: pkgconfig(sqlite3)
BuildRequires: pkgconfig(zeitgeist-2.0)


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

# -DUSE_UNITY=no


%install
make install DESTDIR=$RPM_BUILD_ROOT

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

