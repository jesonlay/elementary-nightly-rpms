Summary: Vocal Podcatcher
Name: vocal
Version: 1.0
Release: 1%{?dist}
License: GPLv3
URL: http://launchpad.net/vocal

Source0: vocal_1.0.tar.gz
Source1: %{name}.conf

BuildRequires: cmake pkgconfig
BuildRequires: vala gettext
BuildRequires: desktop-file-utils
BuildRequires: libappstream-glib

BuildRequires: pkgconfig(clutter-gtk-1.0)
BuildRequires: pkgconfig(glib-2.0)
BuildRequires: pkgconfig(granite)
BuildRequires: pkgconfig(gstreamer-1.0)
BuildRequires: pkgconfig(gstreamer-pbutils-1.0)
BuildRequires: pkgconfig(gtk+-3.0)
BuildRequires: pkgconfig(libnotify)
BuildRequires: pkgconfig(sqlite3)


Requires: hicolor-icon-theme


%description
Vocal is a podcatcher designed for elementaryOS.


%prep
%setup -q -n vocal-1.0+r284


%build
%cmake
%make_build


%install
%make_install

mv $RPM_BUILD_ROOT/%{_datadir}/locale-langpack $RPM_BUILD_ROOT/%{_datadir}/locale

%find_lang vocal


%check


%clean
rm -rf $RPM_BUILD_ROOT


%post
/sbin/ldconfig
/usr/bin/glib-compile-schemas %{_datadir}/glib-2.0/schemas &> /dev/null

%postun
/sbin/ldconfig
/usr/bin/glib-compile-schemas %{_datadir}/glib-2.0/schemas &> /dev/null


%files -f vocal.lang
%{_bindir}/vocal

%{_datadir}/appdata/*

%{_datadir}/applications/vocal.desktop

%{_datadir}/glib-2.0/schemas/net.launchpad.vocal.gschema.xml

%{_datadir}/icons/hicolor/*/apps/vocal.svg

%{_datadir}/vocal


%changelog
* Sun Nov 22 2015 Fabio Valentini <decathorpe@gmail.com> - 1.0-1
- Unretire vocal package. Downgrade to version 1.0. Git snapshots coming soon.

