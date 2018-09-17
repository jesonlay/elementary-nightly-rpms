%global __provides_exclude_from ^%{_libdir}/io.elementary.photos/.*\\.so$

%global srcname photos
%global appname io.elementary.photos

Name:           elementary-photos
Summary:        elementary photo manager and viewer
Version:        0.2.5+git%{date}.%{commit}
Release:        1%{?dist}
License:        LGPLv2+

URL:            https://github.com/elementary/%{srcname}
Source0:        %{name}-%{version}.tar.gz

BuildRequires:  desktop-file-utils
BuildRequires:  gettext
BuildRequires:  libappstream-glib
BuildRequires:  meson
BuildRequires:  vala

BuildRequires:  pkgconfig(gee-0.8)
BuildRequires:  pkgconfig(geocode-glib-1.0)
BuildRequires:  pkgconfig(gexiv2)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(granite)
BuildRequires:  pkgconfig(gstreamer-1.0)
BuildRequires:  pkgconfig(gstreamer-base-1.0)
BuildRequires:  pkgconfig(gstreamer-plugins-base-1.0)
BuildRequires:  pkgconfig(gstreamer-pbutils-1.0)
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.10
BuildRequires:  pkgconfig(gudev-1.0) >= 145
BuildRequires:  pkgconfig(json-glib-1.0)
BuildRequires:  pkgconfig(libgphoto2) >= 2.4.2
BuildRequires:  pkgconfig(libexif) >= 0.6.16
BuildRequires:  pkgconfig(libraw) >= 0.13.2
BuildRequires:  pkgconfig(libsoup-2.4) >= 2.26.0
BuildRequires:  pkgconfig(libwebp) >= 0.4.4
BuildRequires:  pkgconfig(libxml-2.0) >= 2.6.32
BuildRequires:  pkgconfig(rest-0.7) >= 0.7
BuildRequires:  pkgconfig(sqlite3) >= 3.5.9
BuildRequires:  pkgconfig(unity) >= 4.0.0
BuildRequires:  pkgconfig(webkit2gtk-4.0) >= 2.0.0

Requires:       hicolor-icon-theme

Provides:       pantheon-photos
Obsoletes:      pantheon-photos


%description
The elementary continuation of Shotwell, originally written by Yorba
Foundation.


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

desktop-file-validate \
    %{buildroot}/%{_datadir}/applications/%{appname}-viewer.desktop

# Validation currently fails due to a bug (?) in appstream-glib
# https://bugzilla.redhat.com/show_bug.cgi?id=1492566
appstream-util validate-relax --nonet \
    %{buildroot}/%{_datadir}/metainfo/%{appname}.appdata.xml || :


%files -f %{appname}.lang
%doc AUTHORS README.md THANKS
%license COPYING

%{_bindir}/%{appname}

%{_libdir}/%{appname}/

%{_libexecdir}/%{appname}/

%{_datadir}/applications/%{appname}.desktop
%{_datadir}/applications/%{appname}-viewer.desktop
%{_datadir}/glib-2.0/schemas/%{appname}.gschema.xml
%{_datadir}/glib-2.0/schemas/%{appname}-extras.gschema.xml
%{_datadir}/metainfo/%{appname}.appdata.xml


%changelog
* Mon Sep 17 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.5+git180917.154423.285b333a-1
- Update to latest snapshot.

* Mon Sep 17 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.5+git180917.061625.c7a9c218-1
- Update to latest snapshot.

* Wed Sep 12 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.5+git180912.191318.55654241-1
- Update to latest snapshot.

* Wed Sep 12 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.5+git180912.184419.0da7d1c7-1
- Update to latest snapshot.

* Wed Sep 12 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.5+git180912.103649.4befc0cc-1
- Update to latest snapshot.

* Wed Sep 12 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.5+git180912.094145.b5e46113-1
- Update to latest snapshot.

* Tue Sep 11 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.5+git180911.190447.c001516b-1
- Update to latest snapshot.

* Tue Sep 11 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.5+git180911.185253.f64ca80b-1
- Update to latest snapshot.

* Mon Sep 10 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.5+git180910.215115.8b81593a-1
- Update to latest snapshot.

* Sun Sep 09 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.5+git180909.181118.b87cd697-1
- Update to latest snapshot.

* Fri Sep 07 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.5+git180907.100255.0db2dc04-1
- Update to latest snapshot.

* Thu Sep 06 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.5+git180906.201144.332ce03a-1
- Update to latest snapshot.

* Thu Sep 06 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.5+git180906.183033.53c5070b-1
- Update to latest snapshot.

* Thu Sep 06 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.5+git180906.153016.a552e528-1
- Update to latest snapshot.

* Thu Sep 06 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.5+git180906.074114.e7a8648b-1
- Update to latest snapshot.

* Wed Sep 05 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.5+git180905.210140.ca73fcb2-1
- Update to latest snapshot.

* Wed Sep 05 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.5+git180905.182312.33df6116-1
- Update to latest snapshot.

* Wed Sep 05 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.5+git180905.165519.94ff5a13-1
- Update to latest snapshot.

* Wed Sep 05 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.5+git180905.143920.80dd67aa-1
- Update to latest snapshot.

* Wed Sep 05 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.5+git180905.111012.b5a378f9-1
- Update to latest snapshot.

* Tue Sep 04 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.5+git180904.051345.44f56456-1
- Update to latest snapshot.

* Sun Sep 02 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.5+git180902.075158.85574e35-1
- Update to latest snapshot.

* Sat Sep 01 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.5+git180901.000828.e268e03f-1
- Update to latest snapshot.

* Fri Aug 31 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.5+git180831.180757.1a6e907f-1
- Update to latest snapshot.

* Fri Aug 31 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.5+git180831.174647.e794c174-1
- Update to latest snapshot.

* Fri Aug 31 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.5+git180831.141357.96119177-1
- Update to latest snapshot.

* Fri Aug 31 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.5+git180831.130114.e8d73c3e-1
- Update to latest snapshot.

* Fri Aug 31 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.5+git180831.104236.f42a39c2-1
- Update to latest snapshot.

* Fri Aug 31 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.5+git180831.060436.9c22694c-1
- Update to latest snapshot.

* Thu Aug 30 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.5+git180830.170252.81b57c08-1
- Update to latest snapshot.

* Thu Aug 30 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.5+git180830.165521.2e9fdbee-1
- Update to latest snapshot.

* Thu Aug 30 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.5+git180830.092736.e96a2018-1
- Update to latest snapshot.

* Wed Aug 29 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.5+git180829.192524.7f92947e-1
- Update to latest snapshot.

* Wed Aug 29 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.5+git180829.175327.7a61c8d0-1
- Update to latest snapshot.

* Wed Aug 29 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.5+git180829.164742.8202ae3f-1
- Update to latest snapshot.

* Wed Aug 29 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.5+git180829.152805.31ad7d4d-1
- Update to latest snapshot.

* Wed Aug 29 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.5+git180829.042813.c193d5f4-1
- Update to latest snapshot.

* Mon Aug 27 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.5+git180827.170805.720dd399-1
- Update to latest snapshot.

* Mon Aug 27 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.5+git180827.162249.0a4f6f52-1
- Update to latest snapshot.

* Thu Aug 23 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.5+git180823.201518.c70055d9-1
- Update to latest snapshot.

* Thu Aug 23 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.5+git180823.164117.4d012920-1
- Update to latest snapshot.

* Thu Aug 23 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.5+git180823.121022.9127d22f-1
- Update to latest snapshot.

* Thu Aug 23 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.5+git180823.000309.96931d8c-1
- Update to latest snapshot.

* Wed Aug 22 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.5+git180822.000857.930456dc-1
- Update to latest snapshot.

* Tue Aug 21 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.5+git180821.000336.9c28aac0-1
- Update to latest snapshot.

* Mon Aug 20 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.5+git180820.155841.5291fdd9-1
- Update to latest snapshot.

* Sun Aug 19 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.5+git180819.000921.c2018d74-1
- Update to latest snapshot.

* Sat Aug 18 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.5+git180817.183418.41dcfbc2-1
- Update to latest snapshot.

* Thu Aug 16 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.5+git180816.183616.f745621d-1
- Update to latest snapshot.

* Thu Aug 16 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.5+git180816.174409.e3f54f88-1
- Update to latest snapshot.

* Thu Aug 16 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.5+git180816.165357.ca0ba2ee-1
- Update to latest snapshot.

* Thu Aug 16 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.5+git180816.150644.83136dd5-1
- Update to latest snapshot.

* Thu Aug 16 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.5+git180815.223128.56785e55-2
- Occasional mass rebuild.

* Thu Aug 16 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.5+git180815.223128.56785e55-1
- Update to latest snapshot.

* Wed Aug 15 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.5+git180815.144710.f758dbd7-1
- Update to latest snapshot.

* Wed Aug 15 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.5+git180815.003331.1b518385-1
- Update to latest snapshot.

* Mon Aug 13 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.5+git180813.145346.a22b2e97-1
- Update to latest snapshot.

* Mon Aug 13 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.5+git180813.000328.fd70241e-1
- Update to latest snapshot.

* Sun Aug 12 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.5+git180812.105423.edff5026-1
- Update to latest snapshot.

* Sat Aug 11 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.5+git180811.204244.77d46987-1
- Update to latest snapshot.

* Sat Aug 11 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.5+git180811.094439.6c8d5c73-1
- Update to latest snapshot.

* Fri Aug 10 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.5+git180810.204327.59dc7bff-1
- Update to latest snapshot.

* Fri Aug 10 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.5+git180809.225046.230298e2-1
- Update to latest snapshot.

* Thu Aug 09 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.5+git180808.192639.f77ff27a-1
- Update to latest snapshot.

* Wed Aug 08 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.5+git180808.031044.316faea5-1
- Update to latest snapshot.

* Fri Aug 03 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.5+git180803.171308.51d03046-1
- Update to latest snapshot.

* Thu Aug 02 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.5+git180802.191810.c95df27b-1
- Update to latest snapshot.

* Thu Aug 02 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.5+git180802.173259.b4670c1e-1
- Update to latest snapshot.

* Mon Jul 30 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.5+git180730.083401.cb6a4377-1
- Update to latest snapshot.

* Sat Jul 28 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.5+git180728.000922.95970841-1
- Update to latest snapshot.

* Fri Jul 27 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.5+git180727.112857.2fe650f2-1
- Update to latest snapshot.

* Fri Jul 27 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.5+git180727.065852.2fa46c18-1
- Update to latest snapshot.

* Thu Jul 26 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.5+git180726.000042.351cdd64-1
- Update to latest snapshot.

* Wed Jul 25 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.5+git180725.004610.ec46a149-1
- Update to latest snapshot.

* Tue Jul 24 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.5+git180724.000536.1553cfcb-1
- Update to latest snapshot.

* Sun Jul 22 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.5+git180722.000343.1b97a104-1
- Update to latest snapshot.

* Fri Jul 20 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.5+git180720.114930.13b3d532-1
- Update to latest snapshot.

* Fri Jul 20 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.5+git180720.000713.690a400e-1
- Update to latest snapshot.

* Wed Jul 18 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.5+git180718.000613.2d05d97c-1
- Update to latest snapshot.

* Sun Jul 15 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.5+git180715.001011.c01b64e6-1
- Update to latest snapshot.

* Fri Jul 13 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.5+git180713.000358.0957f2af-1
- Update to latest snapshot.

* Wed Jul 11 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.5+git180711.054825.223e30d5-1
- Update to latest snapshot.

* Tue Jul 10 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.5+git180710.000344.7a6107e4-1
- Update to latest snapshot.

* Sat Jul 07 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.5+git180706.000811.6e8d7d3d-2
- Adapt to CMake -> meson switch.

* Fri Jul 06 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.5+git180706.000811.6e8d7d3d-1
- Update to version 0.2.5.

* Fri Jul 06 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.4+git180706.000811.6e8d7d3d-1
- Update to latest snapshot.

* Thu Jul 05 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.4+git180705.000721.033ffd0a-1
- Update to latest snapshot.

* Wed Jul 04 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.4+git180703.000640.81eba898-1
- Update to latest snapshot.

* Fri Jun 15 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.4+git180615.001045.decbd6cd-1
- Update to latest snapshot.

* Thu Jun 14 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.4+git180614.090934.4cad9f93-1
- Update to latest snapshot.

* Wed Jun 13 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.4+git180613.000729.d8fce1df-1
- Update to latest snapshot.

* Sun Jun 10 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.4+git180610.001144.ca0b2a07-1
- Update to latest snapshot.

* Fri Jun 08 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.4+git180608.001211.c668db7d-1
- Update to latest snapshot.

* Wed Jun 06 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.4+git180606.000857.b1fb89d4-1
- Update to latest snapshot.

* Mon Jun 04 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.4+git180604.014014.378dd7b4-1
- Update to latest snapshot.

* Sun Jun 03 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.4+git180603.160305.5eaf62f7-1
- Update to latest snapshot.

* Sat Jun 02 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.4+git180601.201548.c48d8473-1
- Update to latest snapshot.

* Fri Jun 01 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.4+git180601.000747.aeda60fe-1
- Update to latest snapshot.

* Thu May 31 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.4+git180531.000238.1da351e5-1
- Update to latest snapshot.

* Tue May 29 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.4+git180529.080347.2f338354-1
- Update to latest snapshot.

* Mon May 28 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.4+git180528.000248.8ed76f41-1
- Update to latest snapshot.

* Sun May 27 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.4+git180527.000522.3778e7e0-1
- Update to latest snapshot.

* Sat May 26 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.4+git180526.113321.2e3c0432-1
- Update to latest snapshot.

* Sat May 26 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.4+git180526.102238.8f28afd9-1
- Update to latest snapshot.

* Sat May 26 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.4+git180526.093004.91c183ec-1
- Update to latest snapshot.

* Sat May 26 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.4+git180525.223208.dd0282d6-1
- Update to latest snapshot.

* Thu May 24 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.4+git180524.001024.4021795b-1
- Update to latest snapshot.

* Wed May 16 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.4+git180516.132053.74e3b238-1
- Update to latest snapshot.

* Sun May 13 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.4+git180513.001124.516244d6-1
- Update to latest snapshot.

* Sat May 12 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.4+git180512.120806.13693b65-1
- Update to latest snapshot.

* Sat May 12 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.4+git180512.001130.8cd0d6a0-1
- Update to latest snapshot.

* Tue May 08 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.4+git180508.001055.9b328659-1
- Update to latest snapshot.

* Mon May 07 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.4+git180507.155608.4c35372b-1
- Update to latest snapshot.

* Mon May 07 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.4+git180507.000248.b023889e-1
- Update to latest snapshot.

* Sun May 06 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.4+git180506.000954.92bebca1-1
- Update to latest snapshot.

* Thu May 03 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.4+git180503.080210.2c709da1-1
- Update to latest snapshot.

* Tue May 01 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.4+git180427.000259.307fffb6-1
- Update to latest snapshot.

* Thu Apr 26 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.4+git180426.000328.a28e8ed8-1
- Update to latest snapshot.

* Wed Apr 25 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.4+git180425.000326.0ab89d26-1
- Update to latest snapshot.

* Tue Apr 24 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.4+git180424.204113.34bd84f8-1
- Update to latest snapshot.

* Sun Apr 22 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.4+git180422.000415.a44776c6-1
- Update to latest snapshot.

* Fri Apr 20 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.4+git180420.001153.d8adf62b-1
- Update to latest snapshot.

* Sun Apr 15 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.4+git180415.001005.23008bd3-1
- Update to latest snapshot.

* Sat Apr 14 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.4+git180414.001125.e8229e98-1
- Update to latest snapshot.

* Fri Apr 13 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.4+git180413.000625.6173ccc7-1
- Update to latest snapshot.

* Tue Apr 10 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.4+git180410.000648.318d48e8-1
- Update to latest snapshot.

* Mon Apr 09 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.4+git180409.140831.37e01d91-1
- Update to latest snapshot.

* Sun Apr 08 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.4+git180408.184134.6c9db543-1
- Update to latest snapshot.

* Thu Apr 05 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.4+git180405.101732.b7f31f32-2
- Adapt to upstream file changes.

* Thu Apr 05 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.4+git180405.101732.b7f31f32-1
- Update to latest snapshot.

* Tue Apr 03 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.4+git180330.173315.7ce3bfc7-1
- Update to latest snapshot.

* Tue Mar 27 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.4+git180327.175340.5fa0c8d2-1
- Update to latest snapshot.

* Tue Mar 27 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.4+git180327.000214.3fafedeb-1
- Update to latest snapshot.

* Sun Mar 25 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.4+git180324.001137.1582cbf3-1
- Update to latest snapshot.

* Thu Mar 22 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.4+git180322.175440.bbc20a13-1
- Update to latest snapshot.

* Tue Mar 20 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.4+git180320.001140.f884ae9e-1
- Update to latest snapshot.

* Fri Mar 16 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.4+git180316.000402.98fbe885-1
- Update to latest snapshot.

* Sun Mar 11 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.4+git180311.000612.a5730199-1
- Update to latest snapshot.

* Fri Mar 09 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.4+git180309.000551.6e1a6548-1
- Update to latest snapshot.

* Wed Mar 07 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.4+git180307.000958.11124944-1
- Update to latest snapshot.

* Mon Feb 26 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.4+git180225.215521.d2230cc1-1
- Update to latest snapshot.

* Sat Feb 24 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.4+git180224.192126.4ec9a01a-1
- Update to latest snapshot.

* Sat Feb 24 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.4+git180224.151118.f6e83337-1
- Update to latest snapshot.

* Sat Feb 24 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.4+git180224.000408.90ed1c54-1
- Update to latest snapshot.

* Fri Feb 23 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.4+git180223.172740.7697078c-1
- Update to latest snapshot.

* Fri Feb 23 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.4+git180223.164140.7d0f8841-1
- Update to latest snapshot.

* Fri Feb 23 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.4+git180222.235332.04f2e91d-1
- Update to latest snapshot.

* Thu Feb 22 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.4+git180222.020851.1baa9791-1
- Update to latest snapshot.

* Mon Feb 19 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.4+git180219.074729.6d50d687-1
- Update to latest snapshot.

* Fri Feb 16 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.4+git180215.234249.5ddd938f-1
- Update to latest snapshot.

* Tue Feb 13 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.4+git180213.094320.66e9b6ff-1
- Update to latest snapshot.

* Mon Feb 12 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.4+git180211.000838.06a140ea-1
- Update to latest snapshot.

* Fri Feb 09 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.4+git180209.000952.16d1e7c2-1
- Update to latest snapshot.

* Wed Feb 07 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.4+git180207.173134.81465c26-1
- Update to latest snapshot.

* Sun Feb 04 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.4+git180202.211411.607bd847-3
- Update for packaging changes.

* Sun Feb 04 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.4+git180202.211411.607bd847-2
- Adapt to upstream file changes.

* Fri Feb 02 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.4+git180202.211411.607bd847-1
- Update to latest snapshot.

* Fri Feb 02 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.4+git180202.204802.cd46b71b-1
- Update to latest snapshot.

* Wed Jan 31 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.4+git180131.000935.26bb0331-1
- Update to latest snapshot.

* Sun Jan 28 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.4+git180125.164951.1ef2492e-1
- Update to latest snapshot.

* Fri Jan 26 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.4+git180125.164948.cdce74af-2
- Be lazy about undefined symbols in plugins.

* Thu Jan 25 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.4+git180125.164948.cdce74af-1
- Update to latest snapshot.

* Mon Jan 22 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.4+git180122.145746.8d765102-1
- Update to latest snapshot.

* Sun Jan 21 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.4+git180121.013249.e7fdc59c-1
- Update to latest snapshot.

* Fri Jan 19 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.4+git180119.190020.c20a59cb-1
- Update to latest snapshot.

* Wed Jan 03 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.4+git171229.222002.65512d02-1
- Initial package.


