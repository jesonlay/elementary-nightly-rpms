%global srcname screenshot-tool
%global appname io.elementary.screenshot-tool

Name:           elementary-screenshot-tool
Summary:        Simple screen capture tool
Version:        0.1.5+git%{date}.%{commit}
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
    %{buildroot}/%{_datadir}/applications/%{appname}.desktop

appstream-util validate-relax --nonet \
    %{buildroot}/%{_datadir}/metainfo/%{appname}.appdata.xml || :


%files -f %{appname}.lang
%doc README.md
%license COPYING

%{_bindir}/%{appname}

%{_datadir}/applications/%{appname}.desktop
%{_datadir}/glib-2.0/schemas/%{appname}.gschema.xml
%{_datadir}/icons/hicolor/*/apps/accessories-screenshot.svg
%{_datadir}/metainfo/%{appname}.appdata.xml


%changelog
* Fri Jun 15 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.5+git180615.001049.c9e12a74-1
- Update to latest snapshot.

* Thu Jun 14 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.5+git180614.000858.7b4e96cd-1
- Update to latest snapshot.

* Wed Jun 13 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.5+git180613.105225.6d3bef7b-1
- Update to latest snapshot.

* Tue Jun 12 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.5+git180612.071757.bcfeea9e-1
- Update to latest snapshot.

* Mon Jun 11 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.5+git180611.192858.db324645-1
- Update to latest snapshot.

* Mon Jun 11 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.5+git180608.102315.711f4b5c-1
- Update to version 0.1.5.

* Fri Jun 08 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.4+git180608.102315.711f4b5c-1
- Update to latest snapshot.

* Fri Jun 08 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.4+git180608.081311.db263f52-1
- Update to latest snapshot.

* Thu Jun 07 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.4+git180607.000924.0081c14c-1
- Update to latest snapshot.

* Wed Jun 06 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.4+git180606.131627.31be7f14-1
- Update to latest snapshot.

* Wed Jun 06 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.4+git180606.061441.911d6201-2
- Adapt to upstream file changes.

* Wed Jun 06 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.4+git180606.061441.911d6201-1
- Update to latest snapshot.

* Tue Jun 05 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.4+git180605.175219.0dc2a7f7-1
- Update to latest snapshot.

* Tue Jun 05 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.4+git180605.165623.46b695b3-1
- Update to latest snapshot.

* Tue Jun 05 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.4+git180605.090829.e835fe49-1
- Update to latest snapshot.

* Mon Jun 04 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.4+git180604.000918.49cdceba-1
- Update to latest snapshot.

* Sun Jun 03 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.4+git180603.130959.2a7f457c-1
- Update to latest snapshot.

* Thu May 31 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.4+git180531.155714.03d4deae-1
- Update to latest snapshot.

* Thu May 31 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.4+git180530.173335.f8e8d43d-1
- Update to latest snapshot.

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


