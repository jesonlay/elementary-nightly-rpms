%define rev 1828

Summary: Noise audio player
Name: noise
Version: 0.3.1~rev%{rev}
Release: 1%{?dist}
License: GPLv3
URL: http://launchpad.net/noise

Source0: %{name}-%{version}.tar.gz
Source1: %{name}.conf

BuildRequires: cmake pkgconfig
BuildRequires: vala gettext

BuildRequires: desktop-file-utils

BuildRequires: pkgconfig(dbusmenu-glib-0.4)
BuildRequires: pkgconfig(gee-0.8)
BuildRequires: pkgconfig(glib-2.0)
BuildRequires: pkgconfig(granite)
BuildRequires: pkgconfig(gstreamer-1.0)
BuildRequires: pkgconfig(gstreamer-pbutils-1.0)
BuildRequires: pkgconfig(gstreamer-tag-1.0)
BuildRequires: pkgconfig(gtk+-3.0)
BuildRequires: pkgconfig(indicate-0.7)
BuildRequires: pkgconfig(json-glib-1.0)
BuildRequires: pkgconfig(libaccounts-glib)
BuildRequires: pkgconfig(libgda-5.0)
BuildRequires: pkgconfig(libgpod-1.0)
BuildRequires: pkgconfig(libgsignon-glib)
BuildRequires: pkgconfig(libnotify)
BuildRequires: pkgconfig(libpeas-1.0)
BuildRequires: pkgconfig(libpeas-gtk-1.0)
BuildRequires: pkgconfig(libsoup-2.4)
BuildRequires: pkgconfig(libxml-2.0)
BuildRequires: pkgconfig(taglib_c)
BuildRequires: pkgconfig(zeitgeist-2.0)

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
%make_build


%install
%make_install

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
* Thu Sep 03 2015 Fabio Valentini <decathorpe@gmail.com> - 0.3.1~rev1828-1
- Update to new upstream snapshot.

* Thu Sep 03 2015 Fabio Valentini <decathorpe@gmail.com> - 0.3.1~rev1827-1
- Update spec to reflect BR changes and use make_build and make_install macros.

* Thu Sep 03 2015 Fabio Valentini <decathorpe@gmail.com> - 0.3.1~rev1827-1
- Update to new upstream snapshot.

* Tue Sep 01 2015 Fabio Valentini <decathorpe@gmail.com> - 0.3.1~rev1826-1
- Update to new upstream snapshot.

* Thu Aug 20 2015 Fabio Valentini <decathorpe@gmail.com> - 0.3.1~rev1825-1
- Update to new upstream snapshot.

* Tue Aug 18 2015 Fabio Valentini - 0.3.1~rev1823-1
- Update to new upstream snapshot.

* Mon Jul 13 2015 Fabio Valentini <decathorpe@gmail.com> - 0.3.1~rev1822-1
- Update to bzr snapshot revno 1822.

* Sat Jul 04 2015 Fabio Valentini <decathorpe@gmail.com> - 0.3.1~rev1821-1
- Initial package.


