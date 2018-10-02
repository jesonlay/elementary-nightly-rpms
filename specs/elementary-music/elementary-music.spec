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

%{_libdir}/lib%{appname}-core.so.0
%{_libdir}/lib%{appname}-core.so.0.1

%{_libdir}/%{appname}/

%{_datadir}/accounts/applications/noise-lastfm.application
%{_datadir}/applications/%{appname}.desktop
%{_datadir}/glib-2.0/schemas/%{appname}.gschema.xml
%{_datadir}/icons/hicolor/*/apps/multimedia-audio-player.svg
%{_datadir}/metainfo/%{appname}.appdata.xml


%files devel
%{_libdir}/lib%%{appname}-core.so
%{_libdir}/pkgconfig/%{appname}-core.pc

%{_includedir}/%{appname}-core.h

%{_datadir}/vala/vapi/%{appname}-core.deps
%{_datadir}/vala/vapi/%{appname}-core.vapi


%changelog
* Tue Oct 02 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.2+git181002.000403.1f1da4e5-1
- Update to latest snapshot.

* Mon Oct 01 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.2+git181001.000842.fe1135f3-1
- Update to latest snapshot.

* Sun Sep 30 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.2+git180930.205339.352225ce-1
- Update to latest snapshot.

* Sun Sep 30 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.2+git180930.081329.78f7be76-1
- Update to latest snapshot.

* Sun Sep 30 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.2+git180930.000946.e189feaf-1
- Update to latest snapshot.

* Sat Sep 29 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.2+git180929.000924.846f3292-1
- Update to latest snapshot.

* Fri Sep 28 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.2+git180928.000709.30245d3f-1
- Update to latest snapshot.

* Thu Sep 27 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.2+git180927.001013.4f197b75-1
- Update to latest snapshot.

* Tue Sep 25 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.2+git180925.000214.ea1938ca-1
- Update to latest snapshot.

* Wed Sep 19 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.2+git180919.000855.c31e2342-1
- Update to latest snapshot.

* Tue Sep 18 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.2+git180918.224304.26470407-1
- Update to latest snapshot.

* Tue Sep 18 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.2+git180918.210005.1c01beae-1
- Update to latest snapshot.

* Tue Sep 18 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.2+git180918.171505.738925b7-1
- Update to latest snapshot.

* Mon Sep 17 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.2+git180917.151428.7f5ba85e-1
- Update to latest snapshot.

* Thu Sep 13 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.2+git180913.210929.2972fd13-1
- Update to latest snapshot.

* Thu Sep 13 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.2+git180913.162546.bc4bcf18-1
- Update to latest snapshot.

* Mon Sep 10 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.2+git180910.173857.5b7f42f2-1
- Update to latest snapshot.

* Thu Sep 06 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.2+git180906.132555.92c91519-1
- Update to latest snapshot.

* Thu Sep 06 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.2+git180906.000909.a8024428-1
- Update to latest snapshot.

* Wed Sep 05 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.2+git180905.000947.981d60f6-1
- Update to latest snapshot.

* Sat Sep 01 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.2+git180901.065231.ccede369-1
- Update to latest snapshot.

* Fri Aug 31 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.2+git180831.121003.7548c7c7-1
- Update to latest snapshot.

* Fri Aug 31 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.2+git180831.054334.3bc6be43-1
- Update to latest snapshot.

* Thu Aug 30 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.2+git180830.000715.dd4eb91a-1
- Update to latest snapshot.

* Wed Aug 29 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.2+git180829.193716.6deb8072-1
- Update to latest snapshot.

* Wed Aug 29 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.2+git180829.000344.ad6e167f-1
- Update to latest snapshot.

* Thu Aug 23 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.2+git180823.000302.67265b0f-1
- Update to latest snapshot.

* Wed Aug 22 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.2+git180822.163134.ec424461-1
- Update to latest snapshot.

* Tue Aug 21 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.2+git180821.084543.d812b0f1-1
- Update to latest snapshot.

* Sun Aug 19 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.2+git180819.000909.fa37145e-1
- Update to latest snapshot.

* Sat Aug 18 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.2+git180818.145755.091b82fd-1
- Update to latest snapshot.

* Thu Aug 16 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.2+git180816.161302.6a0a3034-1
- Update to latest snapshot.

* Thu Aug 16 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.2+git180816.150555.ce5bc1c9-1
- Update to latest snapshot.

* Thu Aug 16 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.2+git180815.173724.98f7d32e-2
- Occasional mass rebuild.

* Wed Aug 15 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.2+git180815.173724.98f7d32e-1
- Update to latest snapshot.

* Wed Aug 15 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.2+git180814.223603.fc1753de-1
- Update to latest snapshot.

* Tue Aug 14 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.2+git180814.093409.93400863-1
- Update to latest snapshot.

* Sun Aug 12 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.2+git180812.132415.185a86ca-1
- Update to latest snapshot.

* Thu Aug 09 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.2+git180809.175524.2373b667-1
- Update to latest snapshot.

* Wed Aug 08 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.2+git180808.000146.a46112b0-1
- Update to latest snapshot.

* Fri Aug 03 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.2+git180803.000418.e0003383-1
- Update to latest snapshot.

* Mon Jul 30 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.2+git180730.153133.72b16a00-1
- Update to latest snapshot.

* Sun Jul 29 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.2+git180729.103315.8966822b-1
- Update to latest snapshot.

* Tue Jul 24 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.2+git180724.000531.388cc837-1
- Update to latest snapshot.

* Sun Jul 22 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.2+git180722.000340.d3f8bf27-1
- Update to latest snapshot.

* Fri Jul 20 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.2+git180720.155502.a4de6857-1
- Update to latest snapshot.

* Fri Jul 20 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.2+git180720.113526.a0e61f1e-1
- Update to latest snapshot.

* Fri Jul 20 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.2+git180720.000709.3a174554-1
- Update to latest snapshot.

* Wed Jul 18 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.2+git180718.000548.fb5aaae9-1
- Update to latest snapshot.

* Tue Jul 17 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.2+git180717.152406.6cbc1e70-1
- Update to latest snapshot.

* Tue Jul 17 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.2+git180716.210834.bd48d6c7-1
- Update to latest snapshot.

* Mon Jul 16 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.2+git180716.085839.47fc42bf-1
- Update to latest snapshot.

* Sun Jul 15 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.2+git180715.200621.b2617447-1
- Update to latest snapshot.

* Sat Jul 14 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.2+git180713.205953.4ceb9f73-1
- Update to latest snapshot.

* Fri Jul 13 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.2+git180713.181351.0476632c-1
- Update to latest snapshot.

* Fri Jul 13 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.2+git180713.172808.6dc2688c-1
- Update to latest snapshot.

* Fri Jul 13 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.2+git180713.083410.5860f3fb-1
- Update to latest snapshot.

* Fri Jul 13 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.2+git180713.065647.4fc72ec6-1
- Update to latest snapshot.

* Tue Jul 10 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.2+git180710.150453.e7c8443c-1
- Update to latest snapshot.

* Tue Jul 10 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.2+git180709.202319.25b77108-1
- Update to latest snapshot.

* Mon Jul 09 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.2+git180709.001022.ec2f96eb-1
- Update to latest snapshot.

* Fri Jul 06 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.2+git180705.195011.ae6a30b2-1
- Update to latest snapshot.

* Thu Jul 05 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.2+git180705.000718.5a18847f-1
- Update to latest snapshot.

* Wed Jul 04 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.2+git180703.000632.449d9f02-1
- Update to latest snapshot.

* Thu Jun 14 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.2+git180614.153456.e4d57cfa-1
- Update to latest snapshot.

* Fri Jun 08 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.2+git180608.001159.c44d0942-1
- Update to latest snapshot.

* Wed Jun 06 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.2+git180606.000847.61bc85dd-1
- Update to latest snapshot.

* Sat Jun 02 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.2+git180602.000548.169d58bc-1
- Update to latest snapshot.

* Fri Jun 01 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.2+git180601.150419.c7d55442-1
- Update to latest snapshot.

* Fri Jun 01 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.2+git180601.000739.964d790c-1
- Update to latest snapshot.

* Tue May 29 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.2+git180529.001150.616f4863-1
- Update to latest snapshot.

* Mon May 28 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.2+git180528.105715.7f4cf490-1
- Update to latest snapshot.

* Sun May 27 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.2+git180527.085147.e0ba7451-1
- Update to latest snapshot.

* Sat May 26 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.2+git180526.110058.0d0bb4f6-1
- Update to latest snapshot.

* Sat May 26 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.2+git180525.000818.e74e6a24-1
- Update to latest snapshot.

* Thu May 24 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.2+git180524.001018.7a90c493-1
- Update to latest snapshot.

* Mon May 14 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.2+git180514.000221.8725ec4b-1
- Update to latest snapshot.

* Sun May 13 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.2+git180513.001118.b52faaa1-1
- Update to latest snapshot.

* Thu May 10 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.2+git180510.171609.d283d094-1
- Update to latest snapshot.

* Wed May 09 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.2+git180509.071452.da7397aa-1
- Update to latest snapshot.

* Sun May 06 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.2+git180505.001051.9dbf2cf8-1
- Update to latest snapshot.

* Tue May 01 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.2+git180429.170404.e85f6131-1
- Update to latest snapshot.

* Wed Apr 25 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.2+git180425.000322.c1aa9808-1
- Update to latest snapshot.

* Tue Apr 24 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.2+git180424.072921.6d085db0-1
- Update to latest snapshot.

* Fri Apr 20 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.2+git180420.165225.93b45982-1
- Update to latest snapshot.

* Fri Apr 20 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.2+git180420.001148.93b4c8c3-1
- Update to latest snapshot.

* Mon Apr 16 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.2+git180416.165436.d5d8bcba-1
- Update to latest snapshot.

* Tue Apr 10 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.2+git180410.154903.33f06372-1
- Update to latest snapshot.

* Thu Apr 05 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.2+git180404.234812.3ce84c92-1
- Update to latest snapshot.

* Tue Apr 03 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.2+git180401.175353.1aca3514-1
- Update to latest snapshot.

* Sun Mar 25 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.2+git180324.210744.56387fab-1
- Update to latest snapshot.

* Thu Mar 22 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.2+git180322.190826.51d96059-1
- Update to latest snapshot.

* Thu Mar 22 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.2+git180322.172750.4a177a77-1
- Update to latest snapshot.

* Tue Mar 20 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.2+git180320.181230.24f7f5cb-1
- Update to latest snapshot.

* Tue Mar 20 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.2+git180320.174527.3bfaa27e-1
- Update to latest snapshot.

* Tue Mar 20 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.2+git180320.001135.aac483a0-1
- Update to latest snapshot.

* Fri Mar 16 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.2+git180316.000359.ca9823d9-1
- Update to latest snapshot.

* Sat Mar 10 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.2+git180310.000407.ed7fef59-1
- Update to latest snapshot.

* Thu Mar 08 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.2+git180308.163436.b22c5d82-1
- Update to latest snapshot.

* Thu Mar 08 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.2+git180308.055720.e1a4a7aa-1
- Update to latest snapshot.

* Wed Mar 07 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.2+git180307.000949.701b40f3-1
- Update to latest snapshot.

* Mon Mar 05 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.2+git180303.184658.d05f01d4-1
- Update to latest snapshot.

* Thu Mar 01 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.2+git180301.000333.1568807b-1
- Update to latest snapshot.

* Wed Feb 28 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.2+git180228.105253.2014f665-1
- Update to latest snapshot.

* Mon Feb 26 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.2+git180226.000835.c6f9c138-1
- Update to latest snapshot.

* Sun Feb 25 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.2+git180225.000921.6753f5c7-1
- Update to latest snapshot.

* Thu Feb 22 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.2+git180222.000814.4bc138bc-1
- Update to latest snapshot.

* Wed Feb 21 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.2+git180221.000748.8a313c30-1
- Update to latest snapshot.

* Sun Feb 18 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.2+git180218.194010.6dcb0030-1
- Update to latest snapshot.

* Sun Feb 18 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.2+git180218.144516.38a3fff3-1
- Update to latest snapshot.

* Sat Feb 17 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.2+git180217.085028.49610203-1
- Update to latest snapshot.

* Fri Feb 16 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.2+git180216.072758.03db7ca8-1
- Update to latest snapshot.

* Thu Feb 15 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.2+git180215.211035.78ae9127-1
- Update to latest snapshot.

* Thu Feb 15 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.2+git180215.074732.4011544c-1
- Update to latest snapshot.

* Wed Feb 14 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.2+git180214.105255.73c23e77-1
- Update to latest snapshot.

* Tue Feb 13 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.2+git180213.095443.f2e6c45e-1
- Update to latest snapshot.

* Mon Feb 12 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.2+git180212.212448.aedb510d-1
- Update to latest snapshot.

* Mon Feb 12 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.2+git180211.072649.a71606ed-1
- Update to latest snapshot.

* Thu Feb 08 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.2+git180208.190328.99fed119-2
- Adapt to upstream file changes.

* Thu Feb 08 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.2+git180208.190328.99fed119-1
- Update to latest snapshot.

* Thu Feb 08 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.2+git180208.174354.e443a1b4-1
- Update to latest snapshot.

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


