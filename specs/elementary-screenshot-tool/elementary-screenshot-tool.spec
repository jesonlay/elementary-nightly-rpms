%global srcname screenshot-tool
%global appname io.elementary.screenshot-tool

Name:           elementary-screenshot-tool
Summary:        Simple screen capture tool
Version:        0.1.4+git%{date}.%{commit}
Release:        1%{?dist}
License:        LGPLv3

URL:            http://github.com/elementary/%{srcname}
Source0:        %{name}-%{version}.tar.gz

BuildRequires:  desktop-file-utils
BuildRequires:  gettext
BuildRequires:  libappstream-glib
BuildRequires:  meson
BuildRequires:  vala >= 0.24
BuildRequires:  vala-tools

BuildRequires:  pkgconfig(gdk-pixbuf-2.0)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(granite)
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.12
BuildRequires:  pkgconfig(libcanberra)

Requires:       hicolor-icon-theme

Provides:       screenshot-tool
Obsoletes:      screenshot-tool


%description
A simple screen capture tool made for the Pantheon desktop environment.


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
    %{buildroot}/%{_datadir}/applications/%{srcname}.desktop

appstream-util validate-relax --nonet \
    %{buildroot}/%{_datadir}/metainfo/%{appname}.appdata.xml || :


%files -f %{appname}.lang
%doc README.md
%license COPYING

%{_bindir}/%{appname}

%{_datadir}/applications/%{srcname}.desktop
%{_datadir}/glib-2.0/schemas/%{appname}.gschema.xml
%{_datadir}/icons/hicolor/*/apps/accessories-screenshot.svg
%{_datadir}/metainfo/%{appname}.appdata.xml


%changelog
* Sun Jan 28 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.4+git180104.235035.3e856b65-1
- Update to latest snapshot.

* Sat Jan 06 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.4+git180104.235028.8fc0ea56-3
- Remove icon cache scriptlets.

* Fri Jan 05 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.4+git180104.235028.8fc0ea56-2
- Clean up .spec file.

* Fri Jan 05 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.4+git180104.235028.8fc0ea56-1
- Update to latest snapshot.

* Wed Jan 03 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.4+git171229.084210.c2983fa6-1
- Initial package.


