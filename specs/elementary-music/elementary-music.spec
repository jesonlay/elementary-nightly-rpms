%global __provides_exclude_from ^%{_libdir}/io.elementary.music/.*\\.so$
%undefine _strict_symbol_defs_build

%global srcname music
%global appname io.elementary.music

Name:           elementary-music
Summary:        Music player and library from elementary
Version:        0.4.2+git%{date}.%{commit}
Release:        1%{?dist}
License:        LGPLv2+

URL:            https://github.com/elementary/%{srcname}
Source0:        %{name}-%{version}.tar.gz

BuildRequires:  appstream
BuildRequires:  desktop-file-utils
BuildRequires:  gettext
BuildRequires:  meson
BuildRequires:  libappstream-glib
BuildRequires:  vala >= 0.26

BuildRequires:  pkgconfig(gee-0.8)
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(glib-2.0) >= 2.39
BuildRequires:  pkgconfig(granite)
BuildRequires:  pkgconfig(gstreamer-1.0)
BuildRequires:  pkgconfig(gstreamer-pbutils-1.0)
BuildRequires:  pkgconfig(gstreamer-tag-1.0)
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.11.6
BuildRequires:  pkgconfig(json-glib-1.0)
BuildRequires:  pkgconfig(libaccounts-glib)
BuildRequires:  pkgconfig(libgda-5.0)
BuildRequires:  pkgconfig(libgpod-1.0)
BuildRequires:  pkgconfig(libgsignon-glib)
BuildRequires:  pkgconfig(libnotify)
BuildRequires:  pkgconfig(libpeas-1.0)
BuildRequires:  pkgconfig(libpeas-gtk-1.0)
BuildRequires:  pkgconfig(libsoup-2.4)
BuildRequires:  pkgconfig(taglib_c)
BuildRequires:  pkgconfig(zeitgeist-2.0)

Requires:       hicolor-icon-theme

# elementary-music explicitly requires the sqlite libgda database provider
Requires:       libgda-sqlite%{?_isa}


Provides:       noise
Obsoletes:      noise


%description
Music is a fast and beautiful GTK3 audio player with a focus on music
and libraries. It handles external devices, CDs, and album art. Music
utilizes Granite for a consistent and slick UI.


%package        devel
Summary:        The official elementary music player (development headers)
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description    devel
Music is a fast and beautiful GTK3 audio player with a focus on music
and libraries. It handles external devices, CDs, and album art. Music
utilizes Granite for a consistent and slick UI.

This package contains files needed for developing with Music.


%prep
%autosetup


%build
%meson
%meson_build


%install
%meson_install

%find_lang %{appname}


%check
desktop-file-validate \
    %{buildroot}/%{_datadir}/applications/%{appname}.desktop

appstream-util validate-relax --nonet \
    %{buildroot}/%{_datadir}/metainfo/%{appname}.appdata.xml


%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig


%files -f %{appname}.lang
%doc README.md
%license COPYING

%{_bindir}/%{appname}

# FIXME
%{_libdir}/lib%{appname}-core.so

%{_libdir}/%{appname}/

%{_datadir}/accounts/applications/noise-lastfm.application
%{_datadir}/applications/%{appname}.desktop
%{_datadir}/glib-2.0/schemas/%{appname}.gschema.xml

# FIXME
%{_datadir}/icons/hicolor/multimedia-audio-player.svg
%{_datadir}/metainfo/%{appname}.appdata.xml


%files devel
# FIXME
#%%{_libdir}/lib%%{appname}-core.so
%{_libdir}/pkgconfig/%{appname}-core.pc

%{_includedir}/%{appname}-core.h

%{_datadir}/vala/vapi/%{appname}-core.deps
%{_datadir}/vala/vapi/%{appname}-core.vapi


%changelog
* Thu Feb 08 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.2+git180208.154545.6cddd85c-1
- Update to latest snapshot.

* Thu Feb 08 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.2+git180208.063023.1bfc27f9-1
- Update to latest snapshot.

* Tue Feb 06 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.2+git180206.205106.116b5497-2
- Adapt to upstream file changes.

* Tue Feb 06 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.2+git180206.205106.116b5497-1
- Update to latest snapshot.

* Tue Feb 06 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.2+git180206.001054.91ad20f9-2
- Adapt to cmake -> meson switch.

* Tue Feb 06 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.2+git180206.001054.91ad20f9-1
- Update to latest snapshot.

* Mon Feb 05 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.2+git180205.193157.99d7c302-1
- Update to latest snapshot.

* Mon Feb 05 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.2+git180205.154515.e8cb1611-1
- Update to latest snapshot.

* Mon Feb 05 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.2+git180205.001129.34dc472f-1
- Update to latest snapshot.

* Wed Jan 31 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.2+git180129.000226.e57fd5df-2
- Be lazy about undefined symbols in plugins.

* Mon Jan 29 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.2+git180129.000226.e57fd5df-1
- Update to latest snapshot.

* Sun Jan 28 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.2+git180128.000820.e83d5432-1
- Update to latest snapshot.

* Thu Jan 18 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.2+git180118.191215.f51a1caf-1
- Update to latest snapshot.

* Mon Jan 15 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.2+git180115.162712.65746c64-1
- Update to latest snapshot.

* Mon Jan 15 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.2+git180114.203828.063d3ef8-1
- Initial package.


