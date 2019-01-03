%global srcname code
%global appname io.elementary.code

%global __provides_exclude_from ^%{_libdir}/%{appname}/.*\\.so$

Name:           elementary-code
Summary:        Code editor from elementary
Version:        3.0.1+git%{date}.%{commit}
Release:        1%{?dist}
License:        GPLv3

URL:            https://github.com/elementary/%{srcname}
Source0:        %{name}-%{version}.tar.gz

BuildRequires:  desktop-file-utils
BuildRequires:  gettext
BuildRequires:  meson
BuildRequires:  vala
BuildRequires:  vala-devel

BuildRequires:  /usr/bin/appstream-util

BuildRequires:  pkgconfig(editorconfig)
BuildRequires:  pkgconfig(fontconfig)
BuildRequires:  pkgconfig(gee-0.8) >= 0.8.5
BuildRequires:  pkgconfig(gio-unix-2.0) >= 2.20
BuildRequires:  pkgconfig(glib-2.0) >= 2.30.0
BuildRequires:  pkgconfig(granite)
BuildRequires:  pkgconfig(gtksourceview-3.0) >= 3.24
BuildRequires:  pkgconfig(gtkspell3-3.0)
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.6.0
BuildRequires:  pkgconfig(libgit2-glib-1.0)
BuildRequires:  pkgconfig(libpeas-1.0)
BuildRequires:  pkgconfig(libpeas-gtk-1.0)
BuildRequires:  pkgconfig(libsoup-2.4)
BuildRequires:  pkgconfig(pangoft2)
BuildRequires:  pkgconfig(vte-2.91)
BuildRequires:  pkgconfig(webkit2gtk-4.0)
BuildRequires:  pkgconfig(zeitgeist-2.0)

%if 0%{?mageia}
BuildRequires:  pkgconfig(libvala-0.40)
%else
BuildRequires:  pkgconfig(libvala-0.42)
%endif

Requires:       hicolor-icon-theme

Obsoletes:      scratch-text-editor
Provides:       scratch-text-editor


%description
%{summary}.


%package        devel
Summary:        The text editor that works (development files)
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description    devel
%{summary}.

This package contains the development headers.


%prep
%autosetup

chmod +x meson/post_install.py


%build
%meson
%meson_build


%install
%meson_install

%find_lang %{appname}


%if 0%{?suse_version}
%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig
%endif


%check
desktop-file-validate \
    %{buildroot}/%{_datadir}/applications/%{appname}.desktop

appstream-util validate-relax --nonet \
    %{buildroot}/%{_datadir}/metainfo/%{appname}.appdata.xml


%files -f %{appname}.lang
%doc README.md
%license COPYING

%{_bindir}/%{appname}

%{_libdir}/%{appname}/
%{_libdir}/libcodecore.so.0
%{_libdir}/libcodecore.so.0.0

%{_datadir}/applications/%{appname}.desktop
%{_datadir}/glib-2.0/schemas/%{appname}*.gschema.xml
%{_datadir}/icons/hicolor/*/apps/%{appname}.svg
%{_datadir}/%{appname}/
%{_datadir}/metainfo/%{appname}.appdata.xml


%files devel
%{_includedir}/codecore.h

%{_libdir}/libcodecore.so
%{_libdir}/pkgconfig/codecore.pc

%{_datadir}/vala/vapi/codecore.deps
%{_datadir}/vala/vapi/codecore.vapi


%changelog
* Thu Jan 03 2019 Fabio Valentini <decathorpe@gmail.com> - 3.0.1+git190103.063428.c9c363ed-1
- Update to latest snapshot.

* Wed Jan 02 2019 Fabio Valentini <decathorpe@gmail.com> - 3.0.1+git190102.180047.b81086d0-1
- Update to latest snapshot.

* Wed Dec 19 2018 Fabio Valentini <decathorpe@gmail.com> - 3.0.1+git181219.181209.7cafbb53-1
- Update to latest snapshot.

* Wed Dec 19 2018 Fabio Valentini <decathorpe@gmail.com> - 3.0.1+git181219.171059.a7a43cdb-1
- Update to latest snapshot.

* Wed Dec 19 2018 Fabio Valentini <decathorpe@gmail.com> - 3.0.1+git181219.165456.05cba1b3-1
- Update to latest snapshot.

* Tue Dec 18 2018 Fabio Valentini <decathorpe@gmail.com> - 3.0.1+git181216.192437.d40820e8-1
- Update to version 3.0.1.

* Sun Dec 16 2018 Fabio Valentini <decathorpe@gmail.com> - 3.0+git181216.192437.d40820e8-1
- Update to latest snapshot.

* Sun Dec 09 2018 Fabio Valentini <decathorpe@gmail.com> - 3.0+git181209.000032.11903ec6-1
- Update to latest snapshot.

* Sat Dec 08 2018 Fabio Valentini <decathorpe@gmail.com> - 3.0+git181208.163037.1d8cf998-1
- Update to latest snapshot.

* Thu Dec 06 2018 Fabio Valentini <decathorpe@gmail.com> - 3.0+git181206.220907.cce8e298-1
- Update to latest snapshot.

* Mon Dec 03 2018 Fabio Valentini <decathorpe@gmail.com> - 3.0+git181203.000834.bd311260-1
- Update to latest snapshot.

* Sun Dec 02 2018 Fabio Valentini <decathorpe@gmail.com> - 3.0+git181202.061919.98d8933e-1
- Update to latest snapshot.

* Fri Nov 30 2018 Fabio Valentini <decathorpe@gmail.com> - 3.0+git181130.140636.1f008823-1
- Update to latest snapshot.

* Thu Nov 29 2018 Fabio Valentini <decathorpe@gmail.com> - 3.0+git181129.000206.40b0c7ee-1
- Update to latest snapshot.

* Wed Nov 28 2018 Fabio Valentini <decathorpe@gmail.com> - 3.0+git181128.143435.44d1014a-1
- Update to latest snapshot.

* Sat Nov 24 2018 Fabio Valentini <decathorpe@gmail.com> - 3.0+git181124.072306.78e96c9b-1
- Update to latest snapshot.

* Fri Nov 23 2018 Fabio Valentini <decathorpe@gmail.com> - 3.0+git181123.000145.61e4b85c-1
- Update to latest snapshot.

* Thu Nov 22 2018 Fabio Valentini <decathorpe@gmail.com> - 3.0+git181122.000203.93f9b34a-1
- Update to latest snapshot.

* Wed Nov 21 2018 Fabio Valentini <decathorpe@gmail.com> - 3.0+git181121.125412.c8c16842-1
- Update to latest snapshot.

* Wed Nov 21 2018 Fabio Valentini <decathorpe@gmail.com> - 3.0+git181121.112852.95074987-1
- Update to latest snapshot.

* Wed Nov 21 2018 Fabio Valentini <decathorpe@gmail.com> - 3.0+git181121.000353.f2370c9b-1
- Update to latest snapshot.

* Tue Nov 20 2018 Fabio Valentini <decathorpe@gmail.com> - 3.0+git181120.130005.62772d8a-1
- Update to latest snapshot.

* Mon Nov 19 2018 Fabio Valentini <decathorpe@gmail.com> - 3.0+git181119.173359.4540a289-1
- Update to latest snapshot.

* Sun Nov 18 2018 Fabio Valentini <decathorpe@gmail.com> - 3.0+git181118.200940.9256568e-1
- Update to latest snapshot.

* Sat Nov 17 2018 Fabio Valentini <decathorpe@gmail.com> - 3.0+git181117.002304.d0fa69b3-1
- Update to latest snapshot.

* Fri Nov 16 2018 Fabio Valentini <decathorpe@gmail.com> - 3.0+git181116.115052.fb35ed1e-1
- Update to latest snapshot.

* Fri Nov 16 2018 Fabio Valentini <decathorpe@gmail.com> - 3.0+git181116.083948.9dd98697-1
- Update to latest snapshot.

* Thu Nov 15 2018 Fabio Valentini <decathorpe@gmail.com> - 3.0+git181115.155848.caf757ee-1
- Update to latest snapshot.

* Tue Nov 06 2018 Fabio Valentini <decathorpe@gmail.com> - 3.0+git181106.161923.478e19be-1
- Update to latest snapshot.

* Mon Nov 05 2018 Fabio Valentini <decathorpe@gmail.com> - 3.0+git181105.000916.a12b4f23-1
- Update to latest snapshot.

* Sun Nov 04 2018 Fabio Valentini <decathorpe@gmail.com> - 3.0+git181104.110941.1320ddef-1
- Update to latest snapshot.

* Sun Nov 04 2018 Fabio Valentini <decathorpe@gmail.com> - 3.0+git181104.105823.57a8c527-1
- Update to latest snapshot.

* Sun Nov 04 2018 Fabio Valentini <decathorpe@gmail.com> - 3.0+git181104.000303.efe76c85-1
- Update to latest snapshot.

* Fri Nov 02 2018 Fabio Valentini <decathorpe@gmail.com> - 3.0+git181101.232404.1b5ffc54-2
- Occasional mass rebuild.

* Fri Nov 02 2018 Fabio Valentini <decathorpe@gmail.com> - 3.0+git181101.232404.1b5ffc54-1
- Update to latest snapshot.

* Thu Nov 01 2018 Fabio Valentini <decathorpe@gmail.com> - 3.0+git181101.101701.12796cda-1
- Update to latest snapshot.

* Tue Oct 30 2018 Fabio Valentini <decathorpe@gmail.com> - 3.0+git181030.000026.7ec4b1f8-1
- Update to latest snapshot.

* Mon Oct 29 2018 Fabio Valentini <decathorpe@gmail.com> - 3.0+git181029.192625.3a34bbe0-1
- Update to latest snapshot.

* Mon Oct 29 2018 Fabio Valentini <decathorpe@gmail.com> - 3.0+git181029.000942.a8ece41c-2
- Adapt to cauldron/tumbleweed/fedora differences.

* Mon Oct 29 2018 Fabio Valentini <decathorpe@gmail.com> - 3.0+git181029.000942.a8ece41c-1
- Update to latest snapshot.

* Sun Oct 28 2018 Fabio Valentini <decathorpe@gmail.com> - 3.0+git181028.000535.7cda144b-1
- Update to latest snapshot.

* Sat Oct 27 2018 Fabio Valentini <decathorpe@gmail.com> - 3.0+git181027.224451.ec7aa5b9-1
- Update to latest snapshot.

* Fri Oct 26 2018 Fabio Valentini <decathorpe@gmail.com> - 3.0+git181026.175412.8e1a55d1-1
- Update to latest snapshot.

* Fri Oct 26 2018 Fabio Valentini <decathorpe@gmail.com> - 3.0+git181026.000434.c1cc935a-1
- Update to latest snapshot.

* Thu Oct 25 2018 Fabio Valentini <decathorpe@gmail.com> - 3.0+git181025.072525.8718e175-1
- Update to latest snapshot.

* Thu Oct 25 2018 Fabio Valentini <decathorpe@gmail.com> - 3.0+git181025.060933.c8d48382-1
- Update to latest snapshot.

* Thu Oct 25 2018 Fabio Valentini <decathorpe@gmail.com> - 3.0+git181025.000910.04daec9d-1
- Update to latest snapshot.

* Wed Oct 24 2018 Fabio Valentini <decathorpe@gmail.com> - 3.0+git181024.133336.6f16d110-1
- Update to latest snapshot.

* Tue Oct 23 2018 Fabio Valentini <decathorpe@gmail.com> - 3.0+git181023.000258.16e5fe67-1
- Update to latest snapshot.

* Mon Oct 22 2018 Fabio Valentini <decathorpe@gmail.com> - 3.0+git181022.000301.6cb4bfe6-1
- Update to latest snapshot.

* Sun Oct 21 2018 Fabio Valentini <decathorpe@gmail.com> - 3.0+git181021.113908.f67b3e7d-1
- Update to latest snapshot.

* Sun Oct 21 2018 Fabio Valentini <decathorpe@gmail.com> - 3.0+git181021.101948.01194d24-1
- Update to latest snapshot.

* Sun Oct 21 2018 Fabio Valentini <decathorpe@gmail.com> - 3.0+git181021.000706.50951bc0-1
- Update to latest snapshot.

* Sat Oct 20 2018 Fabio Valentini <decathorpe@gmail.com> - 3.0+git181020.001023.0ae051d0-1
- Update to latest snapshot.

* Fri Oct 19 2018 Fabio Valentini <decathorpe@gmail.com> - 3.0+git181019.173514.f2af1811-1
- Update to latest snapshot.

* Thu Oct 18 2018 Fabio Valentini <decathorpe@gmail.com> - 3.0+git181018.212803.44f85c16-1
- Update to latest snapshot.

* Thu Oct 18 2018 Fabio Valentini <decathorpe@gmail.com> - 3.0+git181018.000926.ef9cd754-1
- Update to version 3.0.

* Thu Oct 18 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git181018.000926.ef9cd754-1
- Update to latest snapshot.

* Tue Oct 16 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git181016.093813.ec222a7a-1
- Update to latest snapshot.

* Tue Oct 16 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git181016.000826.040aeb5f-1
- Update to latest snapshot.

* Mon Oct 15 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git181015.141947.683bd57c-1
- Update to latest snapshot.

* Mon Oct 15 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git181015.035735.f388ccd5-1
- Update to latest snapshot.

* Sun Oct 14 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git181014.182725.9c548b23-1
- Update to latest snapshot.

* Sat Oct 13 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git181013.172030.7a978934-1
- Update to latest snapshot.

* Sat Oct 13 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git181013.000855.7e4ea3bb-1
- Update to latest snapshot.

* Wed Oct 10 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git181010.182529.baf32f3c-1
- Update to latest snapshot.

* Wed Oct 10 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git181010.122011.a7043899-1
- Update to latest snapshot.

* Sun Oct 07 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git181007.023648.893c4c21-1
- Update to latest snapshot.

* Fri Oct 05 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git181005.100045.3f4cde09-1
- Update to latest snapshot.

* Fri Oct 05 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git181005.000805.42423b04-1
- Update to latest snapshot.

* Wed Oct 03 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git181003.142415.cd3e50b2-1
- Update to latest snapshot.

* Wed Oct 03 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git181003.001033.f4033cf1-1
- Update to latest snapshot.

* Tue Oct 02 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git181002.191327.ca453574-1
- Update to latest snapshot.

* Sun Sep 30 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180930.000925.dc5cc29e-1
- Update to latest snapshot.

* Fri Sep 28 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180928.000655.22e8dc1b-1
- Update to latest snapshot.

* Thu Sep 27 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180927.000955.6d180931-1
- Update to latest snapshot.

* Wed Sep 26 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180926.212100.2d23f582-1
- Update to latest snapshot.

* Tue Sep 25 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180925.000135.abb3cd0f-1
- Update to latest snapshot.

* Mon Sep 24 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180924.071733.93ecb0b1-1
- Update to latest snapshot.

* Mon Sep 24 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180924.000459.7d2949e4-1
- Update to latest snapshot.

* Fri Sep 21 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180921.181906.fa9668a1-1
- Update to latest snapshot.

* Wed Sep 19 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180919.142014.2091cb54-1
- Update to latest snapshot.

* Wed Sep 19 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180919.112543.a27054ad-1
- Update to latest snapshot.

* Wed Sep 19 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180919.102017.5feaf3dc-1
- Update to latest snapshot.

* Wed Sep 19 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180919.075609.d18135cf-1
- Update to latest snapshot.

* Wed Sep 19 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180918.234815.093cb61a-1
- Update to latest snapshot.

* Tue Sep 18 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180918.212746.b07f182b-1
- Update to latest snapshot.

* Tue Sep 18 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180918.181436.5b17ffdc-1
- Update to latest snapshot.

* Tue Sep 18 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180918.175315.d11c501d-1
- Update to latest snapshot.

* Tue Sep 18 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180918.154547.241c7579-1
- Update to latest snapshot.

* Tue Sep 18 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180918.070149.2ed1477d-1
- Update to latest snapshot.

* Tue Sep 18 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180918.003506.2fccf1d6-1
- Update to latest snapshot.

* Mon Sep 17 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180917.215938.1c3b9b92-1
- Update to latest snapshot.

* Sun Sep 16 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180916.105037.81b503eb-1
- Update to latest snapshot.

* Tue Sep 11 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180911.171723.6a0c5d4e-1
- Update to latest snapshot.

* Thu Sep 06 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180906.000849.74e42c3a-1
- Update to latest snapshot.

* Tue Sep 04 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180904.000554.7554101b-1
- Update to latest snapshot.

* Sat Sep 01 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180901.000807.696e2ceb-1
- Update to latest snapshot.

* Fri Aug 31 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180831.130415.0c6093c6-1
- Update to latest snapshot.

* Fri Aug 31 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180831.115906.a265f9f2-1
- Update to latest snapshot.

* Fri Aug 31 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180831.025118.92086580-1
- Update to latest snapshot.

* Wed Aug 29 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180829.194029.27fecd61-1
- Update to latest snapshot.

* Wed Aug 29 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180829.182358.6e69e299-1
- Update to latest snapshot.

* Wed Aug 29 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180829.054758.6c46c77b-2
- Adapt to upstream dependency changes.

* Wed Aug 29 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180829.054758.6c46c77b-1
- Update to latest snapshot.

* Mon Aug 27 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180826.000409.df6691cb-1
- Update to latest snapshot.

* Thu Aug 23 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180823.170549.24b4a60f-1
- Update to latest snapshot.

* Mon Aug 20 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180820.211957.477faeae-1
- Update to latest snapshot.

* Mon Aug 20 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180820.174319.e55d48c4-1
- Update to latest snapshot.

* Sun Aug 19 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180819.000847.98e6edea-1
- Update to latest snapshot.

* Sat Aug 18 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180818.134306.275970c6-1
- Update to latest snapshot.

* Thu Aug 16 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180816.150514.7d984752-1
- Update to latest snapshot.

* Thu Aug 16 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180816.031621.591cb429-3
- Fix building by being less smart.

* Thu Aug 16 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180816.031621.591cb429-2
- Occasional mass rebuild.

* Thu Aug 16 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180816.031621.591cb429-1
- Update to latest snapshot.

* Tue Aug 14 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180813.000248.959b5715-2
- Adapt to libvala bump.

* Mon Aug 13 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180813.000248.959b5715-1
- Update to latest snapshot.

* Sun Aug 12 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180812.112418.4c9c72f8-1
- Update to latest snapshot.

* Sun Aug 12 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180812.000533.02084e1a-1
- Update to latest snapshot.

* Thu Aug 09 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180809.125811.5b7fbfda-1
- Update to latest snapshot.

* Thu Aug 09 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180809.000504.3b318b31-1
- Update to latest snapshot.

* Wed Aug 08 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180808.151542.322c2eec-1
- Update to latest snapshot.

* Wed Aug 08 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180808.135615.608fcae3-1
- Update to latest snapshot.

* Wed Aug 08 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180808.091545.1439bb9d-1
- Update to latest snapshot.

* Wed Aug 08 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180808.080835.12a5e22a-1
- Update to latest snapshot.

* Wed Aug 08 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180808.062727.911932b0-1
- Update to latest snapshot.

* Fri Aug 03 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180803.000350.d3a45b28-1
- Update to latest snapshot.

* Thu Aug 02 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180802.181951.8c5f17da-1
- Update to latest snapshot.

* Tue Jul 31 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180731.223701.e0004a34-1
- Update to latest snapshot.

* Mon Jul 30 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180730.000718.a62fa1ea-1
- Update to latest snapshot.

* Sun Jul 22 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180722.000325.07b93fd1-1
- Update to latest snapshot.

* Sat Jul 21 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180721.190302.8cf17e8b-1
- Update to latest snapshot.

* Sat Jul 21 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180721.121900.83ee0290-1
- Update to latest snapshot.

* Sat Jul 21 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180721.104145.60be3c97-1
- Update to latest snapshot.

* Sat Jul 21 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180721.000707.f5cd46f4-1
- Update to latest snapshot.

* Fri Jul 20 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180720.111147.63e4f159-1
- Update to latest snapshot.

* Fri Jul 20 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180720.000650.3ff1e5c8-1
- Update to latest snapshot.

* Thu Jul 19 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180719.170336.a28ca0d0-1
- Update to latest snapshot.

* Thu Jul 19 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180719.000331.17b6ff9f-1
- Update to latest snapshot.

* Wed Jul 18 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180718.185919.91033659-1
- Update to latest snapshot.

* Wed Jul 18 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180718.122448.b000917b-1
- Update to latest snapshot.

* Wed Jul 18 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180718.101018.8870817d-1
- Update to latest snapshot.

* Wed Jul 18 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180718.082404.afe66381-1
- Update to latest snapshot.

* Wed Jul 18 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180718.073221.6fd4b53b-1
- Update to latest snapshot.

* Tue Jul 17 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180717.183506.7c281376-1
- Update to latest snapshot.

* Tue Jul 17 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180717.173400.b277fda3-1
- Update to latest snapshot.

* Sun Jul 15 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180715.000959.e90959dc-1
- Update to latest snapshot.

* Fri Jul 13 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180713.000329.d3492b37-1
- Update to latest snapshot.

* Tue Jul 10 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180710.143312.12e5dd6a-1
- Update to latest snapshot.

* Tue Jul 10 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180710.000325.78d6a211-1
- Update to latest snapshot.

* Sat Jul 07 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180706.000757.d147cbec-2
- Adapt to upstream file changes.

* Fri Jul 06 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180706.000757.d147cbec-1
- Update to latest snapshot.

* Thu Jul 05 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180704.210827.bcefca30-1
- Update to latest snapshot.

* Wed Jul 04 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180703.000557.6d626625-1
- Update to latest snapshot.

* Fri Jun 15 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180615.001000.737256ff-1
- Update to latest snapshot.

* Thu Jun 14 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180614.000708.9a4a16ea-1
- Update to latest snapshot.

* Wed Jun 13 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180613.152600.0d8de916-1
- Update to latest snapshot.

* Wed Jun 13 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180613.121936.b566cec3-1
- Update to latest snapshot.

* Wed Jun 13 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180613.000241.3c1cb848-1
- Update to latest snapshot.

* Tue Jun 12 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180612.162950.a24e9566-1
- Update to latest snapshot.

* Sun Jun 10 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180610.001105.6e22c031-1
- Update to latest snapshot.

* Fri Jun 08 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180608.001112.14471ee3-1
- Update to latest snapshot.

* Wed Jun 06 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180606.205953.6a5cc8fd-1
- Update to latest snapshot.

* Wed Jun 06 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180606.000759.60471b55-1
- Update to latest snapshot.

* Tue Jun 05 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180605.092434.5bdc20c9-1
- Update to latest snapshot.

* Tue Jun 05 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180605.000521.bc6e2d91-1
- Update to latest snapshot.

* Mon Jun 04 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180604.000827.df6bc66e-1
- Update to latest snapshot.

* Sun Jun 03 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180603.162531.d1618141-1
- Update to latest snapshot.

* Sat Jun 02 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180602.000435.f63a2d78-1
- Update to latest snapshot.

* Fri Jun 01 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180601.000652.06bd1c68-1
- Update to latest snapshot.

* Thu May 31 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180531.150917.46f6cee7-1
- Update to latest snapshot.

* Thu May 31 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180531.144958.ca362b18-1
- Update to latest snapshot.

* Thu May 31 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180531.000206.372c3b67-1
- Update to latest snapshot.

* Tue May 29 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180529.001104.68360211-1
- Update to latest snapshot.

* Mon May 28 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180528.123800.b237d932-1
- Update to latest snapshot.

* Sun May 27 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180527.000443.47159cf0-1
- Update to latest snapshot.

* Sat May 26 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180526.073944.9cfeffa8-1
- Update to latest snapshot.

* Thu May 24 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180524.160358.21d512a8-1
- Update to latest snapshot.

* Fri May 18 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180518.082357.0c987928-1
- Update to latest snapshot.

* Thu May 17 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180517.000131.1160c09a-1
- Update to latest snapshot.

* Wed May 16 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180516.184432.86040600-1
- Update to latest snapshot.

* Tue May 15 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180515.000540.f25153e8-1
- Update to latest snapshot.

* Mon May 14 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180514.145252.dc765970-1
- Update to latest snapshot.

* Sat May 12 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180512.001056.370e422d-1
- Update to latest snapshot.

* Fri May 11 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180511.061657.4d0fc620-1
- Update to latest snapshot.

* Thu May 10 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180510.064254.d3effc13-1
- Fix build due to bogus changelog entries.

* Sun Apr 22 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180421.162355.9329bf5b-1
- Update to latest snapshot.

* Sun Apr 22 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180421.001026.9209d900-1
- Update to latest snapshot.

* Fri Apr 20 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180420.001116.92d67c54-1
- Update to latest snapshot.

* Thu Apr 19 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180419.172746.ca7a24f6-1
- Update to latest snapshot.

* Tue Apr 17 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180417.183345.622afc32-1
- Update to latest snapshot.

* Mon Apr 16 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180416.000339.13d09286-1
- Update to latest snapshot.

* Sun Apr 15 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180415.171917.abac84b8-1
- Update to latest snapshot.

* Tue Apr 03 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180403.000528.88639b83-1
- Update to latest snapshot.

* Wed Mar 28 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180328.000336.2d04e755-1
- Update to latest snapshot.

* Tue Mar 27 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180327.000137.86513d03-1
- Update to latest snapshot.

* Mon Mar 26 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180326.072358.fefa07b2-1
- Update to latest snapshot.

* Sun Mar 25 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180324.151817.64db28f9-1
- Update to latest snapshot.

* Thu Mar 22 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180322.191347.8ff356a4-1
- Update to latest snapshot.
- Adapt to upstream dependency changes.

* Thu Mar 22 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180322.185628.7ea0aac1-1
- Update to latest snapshot.

* Thu Mar 22 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180322.134356.17216658-1
- Update to latest snapshot.

* Thu Mar 22 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180322.021758.e59a69a2-1
- Update to latest snapshot.

* Wed Mar 21 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180321.160405.0a830c14-1
- Update to latest snapshot.

* Tue Mar 20 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180320.191932.91728fda-1
- Update to latest snapshot.

* Tue Mar 20 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180320.182241.89dd92f5-1
- Update to latest snapshot.

* Tue Mar 20 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180320.034656.d06bc802-1
- Update to latest snapshot.

* Mon Mar 19 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180319.225618.af5b02ea-1
- Update to latest snapshot.

* Mon Mar 19 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180319.204714.6f545742-1
- Update to latest snapshot.

* Mon Mar 19 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180319.182316.4eb6bf78-1
- Update to latest snapshot.

* Mon Mar 19 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180319.155402.0a03186c-1
- Update to latest snapshot.

* Mon Mar 19 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180319.000143.c263fa22-1
- Update to latest snapshot.

* Sun Mar 18 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180318.014452.600d44ae-1
- Update to latest snapshot.

* Sat Mar 17 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180317.225504.5197da96-1
- Update to latest snapshot.

* Sat Mar 17 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180317.193317.53c41de6-1
- Update to latest snapshot.

* Sat Mar 17 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180317.101513.e0a7cdc9-1
- Update to latest snapshot.

* Sat Mar 17 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180317.091702.61f4b86b-1
- Update to latest snapshot.

* Sat Mar 17 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180317.001124.40c0b8b3-1
- Update to latest snapshot.

* Fri Mar 16 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180316.182314.a4212caa-1
- Update to latest snapshot.

* Fri Mar 16 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180316.004052.b29a98a5-1
- Update to latest snapshot.

* Thu Mar 15 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180315.180805.2e970910-1
- Update to latest snapshot.

* Thu Mar 15 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180315.004730.9a1b77ca-1
- Update to latest snapshot.

* Wed Mar 14 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180314.000156.e16b5795-1
- Update to latest snapshot.

* Tue Mar 13 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180312.202140.d65721e2-1
- Update to latest snapshot.

* Sat Mar 10 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180310.000330.a44720c2-1
- Update to latest snapshot.

* Fri Mar 09 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180309.112149.a400d30b-1
- Update to latest snapshot.

* Wed Mar 07 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180307.000931.3fe16b80-1
- Update to latest snapshot.

* Tue Mar 06 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180306.000445.5b84a413-1
- Update to latest snapshot.

* Mon Mar 05 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180304.000738.1c5e17af-1
- Update to latest snapshot.

* Thu Mar 01 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180301.000317.1599c6fa-1
- Update to latest snapshot.

* Tue Feb 27 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180227.185938.5312a6a6-1
- Update to latest snapshot.

* Tue Feb 27 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180227.000356.827a5d89-1
- Update to latest snapshot.

* Mon Feb 26 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180226.105909.8b98c54e-1
- Update to latest snapshot.

* Mon Feb 26 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180225.165330.c726d965-1
- Update to latest snapshot.

* Sun Feb 25 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180225.023324.d7ef7e5d-1
- Update to latest snapshot.

* Sat Feb 24 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180224.115243.1a4af761-1
- Update to latest snapshot.

* Fri Feb 23 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180223.181222.6e77ae1b-1
- Update to latest snapshot.

* Thu Feb 22 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180222.000758.26f3b776-1
- Update to latest snapshot.

* Wed Feb 21 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180221.143240.251c99b9-1
- Update to latest snapshot.

* Wed Feb 21 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180221.123443.c8e53c66-1
- Update to latest snapshot.

* Wed Feb 21 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180221.074128.83155730-1
- Update to latest snapshot.

* Tue Feb 20 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180220.192202.59278f0c-1
- Update to latest snapshot.

* Tue Feb 20 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180220.022714.e305f284-1
- Update to latest snapshot.

* Mon Feb 19 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180219.175143.82a1697f-1
- Update to latest snapshot.

* Sun Feb 18 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180218.145615.edc1200c-1
- Update to latest snapshot.

* Fri Feb 16 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180216.125400.069696a9-1
- Update to latest snapshot.

* Fri Feb 16 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180216.000253.9691592b-1
- Update to latest snapshot.

* Wed Feb 14 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180214.182858.2d3f62bd-1
- Update to latest snapshot.

* Wed Feb 14 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180214.013747.b4951d12-1
- Update to latest snapshot.

* Tue Feb 13 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180213.213524.e3686e34-1
- Update to latest snapshot.

* Tue Feb 13 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180213.005517.891c74fa-1
- Update to latest snapshot.

* Mon Feb 12 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180212.212015.b3353b8f-1
- Update to latest snapshot.

* Mon Feb 12 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180212.160234.0954ba6d-2
- Adapt to cmake -> meson switch.

* Mon Feb 12 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180212.160234.0954ba6d-1
- Update to latest snapshot.

* Fri Feb 09 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180209.001000.2d369a0a-1
- Update to latest snapshot.

* Tue Feb 06 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180206.200848.714fc767-1
- Update to latest snapshot.

* Wed Jan 31 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180129.195832.b8629598-2
- Be lazy about undefined symbols in plugins.

* Mon Jan 29 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180129.195832.b8629598-1
- Update to latest snapshot.

* Mon Jan 29 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180129.185322.b15ff49d-1
- Update to latest snapshot.

* Sun Jan 28 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180125.000833.ad688fc4-1
- Update to latest snapshot.

* Wed Jan 24 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180124.123947.d3ab6ba9-1
- Update to latest snapshot.

* Tue Jan 23 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180123.221341.4969d443-1
- Update to latest snapshot.

* Mon Jan 22 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180122.060359.dc426bee-1
- Update to latest snapshot.

* Sat Jan 20 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180120.020812.e959a13c-1
- Update to latest snapshot.

* Wed Jan 17 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180117.192407.07d814d5-1
- Update to latest snapshot.

* Tue Jan 16 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180116.180121.cc9cd0ba-1
- Update to latest snapshot.

* Mon Jan 15 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180112.191811.9961a070-1
- Update to latest snapshot.

* Thu Jan 11 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180111.160157.63bf2a42-1
- Update to latest snapshot.

* Wed Jan 10 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180109.231632.616f30af-1
- Update to latest snapshot.

* Tue Jan 09 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180109.222901.cefbdb61-1
- Update to latest snapshot.

* Tue Jan 09 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180109.170232.0d7cbb8a-1
- Update to latest snapshot.

* Mon Jan 08 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180108.201726.899b0b68-2
- Adapt to upstream file changes.

* Mon Jan 08 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180108.201726.899b0b68-1
- Update to latest snapshot.

* Sat Jan 06 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180106.000312.b62cbf36-2
- Remove icon cache scriptlets.

* Sat Jan 06 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180106.000312.b62cbf36-1
- Update to latest snapshot.

* Fri Jan 05 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180105.001608.fc57a13d-1
- Update to latest snapshot.

* Wed Jan 03 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git171219.151614.17101d60-1
- Initial package.


