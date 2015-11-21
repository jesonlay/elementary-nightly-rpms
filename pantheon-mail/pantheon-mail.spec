%define rev 1874

Summary: Mail is an email client for elementary OS
Name: pantheon-mail
Version: 1.0.0~rev%{rev}
Release: 0%{?dist}
License: LGPLv2.1
URL: http://launchpad.net/pantheon-mail

Source0: %{name}-%{version}.tar.gz
Source1: %{name}.conf

BuildRequires: cmake
BuildRequires: desktop-file-utils
BuildRequires: gettext
BuildRequires: vala

#BuildRequires: pkgconfig(dbus-glib-1)
#BuildRequires: pkgconfig(gail-3.0)
#BuildRequires: pkgconfig(gee-0.8)
#BuildRequires: pkgconfig(gio-2.0)
#BuildRequires: pkgconfig(gio-unix-2.0)
#BuildRequires: pkgconfig(glib-2.0) >= 2.29
#BuildRequires: pkgconfig(gmodule-2.0)
#BuildRequires: pkgconfig(granite) >= 0.3.0
#BuildRequires: pkgconfig(gthread-2.0)
#BuildRequires: pkgconfig(gtk+-3.0) >= 3.10
#BuildRequires: pkgconfig(libnotify) >= 0.7.2
#BuildRequires: pkgconfig(pango) >= 1.1.2
#BuildRequires: pkgconfig(plank)
#BuildRequires: pkgconfig(sqlite3)
#BuildRequires: pkgconfig(zeitgeist-2.0)


%description
Mail is an email client for elementary OS

Originally written by Yorba (yorba.org)


%package devel
Summary: pantheon-mail development headers
%description devel
Mail is an email client for elementary OS
Originally written by Yorba (yorba.org)
This package contains the development headers.


%prep
%autosetup


%build
%cmake
%make_build


%install
%make_install
%find_lang pantheon-mail


%check
# this does fail spectacularly
# desktop-file-validate $RPM_BUILD_ROOT/%%{_datadir}/applications/pantheon-files.desktop


%clean
rm -rf $RPM_BUILD_ROOT


%post
/sbin/ldconfig
/usr/bin/glib-compile-schemas %{_datadir}/glib-2.0/schemas &> /dev/null

%postun
/sbin/ldconfig
/usr/bin/glib-compile-schemas %{_datadir}/glib-2.0/schemas &> /dev/null


%post devel
/sbin/ldconfig

%postun devel
/sbin/ldconfig


%files -f pantheon-mail.lang

%files devel


%changelog


