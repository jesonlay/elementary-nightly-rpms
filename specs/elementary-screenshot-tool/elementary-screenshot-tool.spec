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
* Tue May 29 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.4+git180529.001208.6e1de003-1
- Update to latest snapshot.

* Sun May 27 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.4+git180527.113015.8acdd38a-1
- Update to latest snapshot.

* Fri May 18 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.4+git180518.000732.4f8a1108-1
- Update to latest snapshot.

* Sun May 13 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.4+git180513.001128.46a949d8-1
- Update to latest snapshot.

* Tue May 08 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.4+git180507.215816.0ba42167-1
- Update to latest snapshot.

* Sun May 06 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.4+git180506.001000.f8110a94-1
- Update to latest snapshot.

* Wed Apr 25 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.4+git180425.083937.7e946af4-1
- Update to latest snapshot.

* Thu Apr 19 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.4+git180419.153025.f2278d6c-1
- Update to latest snapshot.

* Sun Apr 08 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.4+git180407.000903.dfeb7dfb-1
- Update to latest snapshot.

* Thu Mar 08 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.4+git180308.162924.290c75ed-1
- Update to latest snapshot.

* Wed Mar 07 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.4+git180307.001008.64a5308b-1
- Update to latest snapshot.

* Thu Mar 01 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.4+git180301.214806.93c15b55-1
- Update to latest snapshot.

* Sun Feb 18 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.4+git180218.110923.bf4263fa-1
- Update to latest snapshot.

* Sat Feb 17 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.4+git180217.101022.f6dcd849-1
- Update to latest snapshot.

* Tue Feb 13 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.4+git180213.094409.716b2c04-1
- Update to latest snapshot.

* Fri Feb 09 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.4+git180209.001008.a90b1b63-1
- Update to latest snapshot.

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


