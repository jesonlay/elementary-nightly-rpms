%define rev 1821

Summary: Noise audio player
Name: noise
Version: 0.3.1~rev%{rev}
Release: 1%{?dist}
License: GPLv3
URL: http://launchpad.net/noise

Source0: %{name}-%{version}.tar.gz

BuildRequires: cmake pkgconfig
BuildRequires: vala gettext

BuildRequires: desktop-file-utils

BuildRequires: pkgconfig(glib-2.0)
BuildRequires: pkgconfig(gtk+-3.0)
BuildRequires: pkgconfig(granite)
BuildRequires: pkgconfig(gee-0.8)

BuildRequires: pkgconfig(libpeas-1.0)
BuildRequires: pkgconfig(libpeas-gtk-1.0)
BuildRequires: pkgconfig(gstreamer-1.0)
BuildRequires: pkgconfig(gstreamer-tag-1.0)
BuildRequires: pkgconfig(gstreamer-pbutils-1.0)
BuildRequires: pkgconfig(taglib_c)

BuildRequires: pkgconfig(libnotify)
BuildRequires: pkgconfig(libgpod-1.0)
BuildRequires: pkgconfig(libxml-2.0)
BuildRequires: pkgconfig(json-glib-1.0)
BuildRequires: pkgconfig(libsoup-2.4)

BuildRequires: pkgconfig(dbusmenu-glib-0.4)
BuildRequires: pkgconfig(zeitgeist-2.0)
BuildRequires: pkgconfig(indicate-0.7)
BuildRequires: pkgconfig(sqlheavy-0.2)

BuildRequires: pkgconfig(libaccounts-glib)
BuildRequires: pkgconfig(libgsignon-glib)

Requires: hicolor-icon-theme


%description
The official elementary music player.


%package devel
Summary: noise development headers
%description devel
The official elementary music player. This package contains the development headers.


%prep
%setup -q


%build
%cmake


%install
make install DESTDIR=$RPM_BUILD_ROOT

desktop-file-validate $RPM_BUILD_ROOT/%{_datadir}/applications/noise.desktop

%find_lang noise


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



%files -f noise.lang
%{_bindir}/noise

%{_libdir}/libnoise-core.so.0
%{_libdir}/libnoise-core.so.0.1

%{_libdir}/noise/

%dir %{_datadir}/accounts/applications
%{_datadir}/accounts/applications/noise-lastfm.application

%{_datadir}/applications/noise.desktop
%{_datadir}/glib-2.0/schemas/org.pantheon.noise.gschema.xml
%{_datadir}/noise/

%{_datadir}/icons/hicolor/16x16/apps/multimedia-audio-player.svg
%{_datadir}/icons/hicolor/22x22/apps/multimedia-audio-player.svg
%{_datadir}/icons/hicolor/24x24/apps/multimedia-audio-player.svg
%{_datadir}/icons/hicolor/32x32/apps/multimedia-audio-player.svg
%{_datadir}/icons/hicolor/48x48/apps/multimedia-audio-player.svg
%{_datadir}/icons/hicolor/64x64/apps/multimedia-audio-player.svg
%{_datadir}/icons/hicolor/128x128/apps/multimedia-audio-player.svg
%{_datadir}/icons/hicolor/scalable/apps/multimedia-audio-player.svg


%files devel
%{_libdir}/libnoise-core.so
%{_libdir}/pkgconfig/noise-core.pc

%{_includedir}/noise-core/

%{_datadir}/vala/vapi/noise-core.deps
%{_datadir}/vala/vapi/noise-core.vapi


%changelog
* Sat Jul 04 2015 Fabio Valentini <decathorpe@gmail.com> - 0.3.1~rev1821-1
- Initial package.


