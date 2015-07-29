%define rev 1900

Summary: Pantheon file manager
Name: pantheon-files
Version: 0.2.2.1~rev%{rev}
Release: 4%{?dist}
License: GPLv3
URL: http://launchpad.net/pantheon-files

Source0: %{name}-%{version}.tar.gz
Patch0: 00-no-marlincore-C-deps.patch

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
%patch0 -p1


%build
%cmake
%make_build


%install
%make_install

# pantheon-files installs libs/plugins in /usr/lib, no matter the arch ...
# mv $RPM_BUILD_ROOT/usr/lib/* $RPM_BUILD_ROOT//usr/lib/

# this does fail spectacularly
# desktop-file-validate $RPM_BUILD_ROOT/%%{_datadir}/applications/pantheon-files.desktop

%find_lang pantheon-files


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


%files -f pantheon-files.lang
%{_bindir}/pantheon-files
%{_bindir}/pantheon-files-daemon
%{_bindir}/pantheon-files-pkexec

/usr/lib/pantheon-files

%{_libdir}/gtk-3.0/modules/libpantheon-filechooser-module.so

/usr/lib/libpantheon-files-core.so.0
/usr/lib/libpantheon-files-core.so.0.1
/usr/lib/libpantheon-files-widgets.so.0
/usr/lib/libpantheon-files-widgets.so.0.1

%{_datadir}/applications/pantheon-files.desktop
%{_datadir}/dbus-1/services/pantheon-files.service
%{_datadir}/glib-2.0/schemas/org.pantheon.files.gschema.xml

%{_datadir}/pantheon-files
%{_datadir}/pixmaps/pantheon-files

%{_datadir}/polkit-1/actions/net.launchpad.pantheon-files.policy


%files devel
%{_includedir}/pantheon-files-core

/usr/lib/libpantheon-files-core.so
/usr/lib/libpantheon-files-widgets.so

/usr/lib/pkgconfig/pantheon-files-core.pc

%{_datadir}/vala/vapi/pantheon-files-core-C.vapi
%{_datadir}/vala/vapi/pantheon-files-core.deps
%{_datadir}/vala/vapi/pantheon-files-core.vapi


%changelog
* Wed Jul 29 2015 Fabio Valentini <decathorpe@gmail.com> - 0.2.2.1~rev1900-4
- Fix build.

* Wed Jul 29 2015 Fabio Valentini <decathorpe@gmail.com> - 0.2.2.1~rev1900-3
- Update to bzr snapshot revno 1900.

