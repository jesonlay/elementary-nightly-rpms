%global appname io.elementary.appcenter

Name:           appcenter
Summary:        Software Center from elementary
Version:        3.0+git%{date}.%{commit}
Release:        1%{?dist}
License:        GPLv3

URL:            https://github.com/elementary/%{name}
Source0:        %{name}-%{version}.tar.gz

# blacklist from elementaryOS
# https://github.com/elementary/default-settings/blob/master/appcenter.blacklist
Source1:        appcenter.blacklist

BuildRequires:  desktop-file-utils
BuildRequires:  gettext
BuildRequires:  libappstream-glib
BuildRequires:  meson
BuildRequires:  vala

BuildRequires:  appstream-vala

BuildRequires:  pkgconfig(appstream) >= 0.10.0
BuildRequires:  pkgconfig(gee-0.8)
BuildRequires:  pkgconfig(glib-2.0) >= 2.32
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(granite) >= 0.5
BuildRequires:  pkgconfig(gthread-2.0)
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.12
BuildRequires:  pkgconfig(json-glib-1.0)
BuildRequires:  pkgconfig(libsoup-2.4)
BuildRequires:  pkgconfig(packagekit-glib2)
BuildRequires:  pkgconfig(unity) >= 4.0.0

Requires:       PackageKit
Requires:       hicolor-icon-theme


%description
AppCenter is a native Gtk+ app store built on AppStream and Packagekit.


%package        gnome-shell-search-provider
Summary:        Software Center from elementary (gnome-shell search provider)

BuildArch:      noarch

Requires:       %{name} = %{version}-%{release}
Requires:       gnome-shell

Supplements:    (%{name} and gnome-shell)

%description    gnome-shell-search-provider
AppCenter is a native Gtk+ app store built on AppStream and Packagekit.

This package contains the gnome-shell search provider.


%prep
%autosetup -p1


%build
%meson -Dpayments=false -Dcurated=false
%meson_build


%install
%meson_install

%find_lang %{appname}

# override empty blacklist
cp -pav %{SOURCE1} %{buildroot}/%{_sysconfdir}/%{appname}/appcenter.blacklist

# create autostart entry symlink
mkdir -p %{buildroot}/%{_sysconfdir}/xdg/autostart/
ln -s %{_datadir}/applications/%{appname}-daemon.desktop \
    %{buildroot}/%{_sysconfdir}/xdg/autostart/%{appname}-daemon.desktop


%check
desktop-file-validate \
    %{buildroot}/%{_datadir}/applications/%{appname}.desktop

appstream-util validate-relax --nonet \
    %{buildroot}/%{_datadir}/metainfo/%{appname}.appdata.xml


%files -f %{appname}.lang
%doc README.md
%license COPYING

%dir %{_sysconfdir}/%{appname}
%config(noreplace) %{_sysconfdir}/%{appname}/appcenter.blacklist
%config(noreplace) %{_sysconfdir}/xdg/autostart/%{appname}-daemon.desktop

%{_bindir}/%{appname}

%{_datadir}/applications/%{appname}.desktop
%{_datadir}/applications/%{appname}-daemon.desktop
%{_datadir}/dbus-1/services/%{appname}.service
%{_datadir}/glib-2.0/schemas/%{appname}.gschema.xml
%{_datadir}/metainfo/%{appname}.appdata.xml

%files gnome-shell-search-provider
%{_datadir}/gnome-shell/search-providers/%{appname}.search-provider.ini


%changelog
* Fri Oct 19 2018 Fabio Valentini <decathorpe@gmail.com> - 3.0+git181019.161530.2f55e8e2-1
- Update to latest snapshot.

* Thu Oct 18 2018 Fabio Valentini <decathorpe@gmail.com> - 3.0+git181018.163652.5a19928d-1
- Update to latest snapshot.

* Thu Oct 18 2018 Fabio Valentini <decathorpe@gmail.com> - 3.0+git181018.101804.34433b32-1
- Update to latest snapshot.

* Thu Oct 18 2018 Fabio Valentini <decathorpe@gmail.com> - 3.0+git181018.005440.54215dea-1
- Update to latest snapshot.

* Wed Oct 17 2018 Fabio Valentini <decathorpe@gmail.com> - 3.0+git181017.000601.cbfde668-1
- Update to latest snapshot.

* Tue Oct 16 2018 Fabio Valentini <decathorpe@gmail.com> - 3.0+git181016.103333.21ab46a3-1
- Update to version 3.0.

* Tue Oct 16 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.9+git181016.103333.21ab46a3-1
- Update to latest snapshot.

* Tue Oct 16 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.9+git181016.094656.1857dd38-1
- Update to latest snapshot.

* Tue Oct 16 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.9+git181016.000812.5dea00f6-1
- Update to latest snapshot.

* Mon Oct 15 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.9+git181015.160000.ef34c295-1
- Update to latest snapshot.

* Mon Oct 15 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.9+git181015.140340.dd5ac7bb-1
- Update to latest snapshot.

* Mon Oct 15 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.9+git181015.092442.b21bbaf5-1
- Update to latest snapshot.

* Mon Oct 15 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.9+git181015.000501.1bb73af3-1
- Update to latest snapshot.

* Sun Oct 14 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.9+git181014.221036.2dacb154-1
- Update to latest snapshot.

* Sun Oct 14 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.9+git181014.193825.a3678889-1
- Update to latest snapshot.

* Sun Oct 14 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.9+git181014.170353.716afe4d-1
- Update to latest snapshot.

* Sun Oct 14 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.9+git181014.164215.e83ceaf6-1
- Update to latest snapshot.

* Sun Oct 14 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.9+git181014.154408.6748f41e-1
- Update to latest snapshot.

* Sat Oct 13 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.9+git181013.181353.bb3ebe9e-1
- Update to latest snapshot.

* Sat Oct 13 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.9+git181013.175609.2fbad40f-1
- Update to latest snapshot.

* Fri Oct 12 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.9+git181012.164208.0d41e63b-1
- Update to latest snapshot.

* Fri Oct 12 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.9+git181012.091810.0917cb24-1
- Update to latest snapshot.

* Thu Oct 11 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.9+git181011.182224.f8ea4e92-1
- Update to latest snapshot.

* Wed Oct 10 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.9+git181010.110909.be2eae57-1
- Update to latest snapshot.

* Tue Oct 09 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.9+git181009.223922.ceecf58a-1
- Update to latest snapshot.

* Tue Oct 09 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.9+git181009.000101.a866a561-1
- Update to latest snapshot.

* Mon Oct 08 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.9+git181008.062734.4bd0f492-1
- Update to latest snapshot.

* Mon Oct 08 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.9+git181008.000350.44804262-1
- Update to latest snapshot.

* Sun Oct 07 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.9+git181007.094216.b06b2b25-1
- Update to latest snapshot.

* Fri Oct 05 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.9+git181005.000738.dd601be4-1
- Update to latest snapshot.

* Wed Oct 03 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.9+git181003.140743.1e08433f-1
- Update to latest snapshot.

* Tue Oct 02 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.9+git181002.214300.4e7aa089-1
- Update to latest snapshot.

* Mon Oct 01 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.9+git181001.000824.1541e237-1
- Update to latest snapshot.

* Sun Sep 30 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.9+git180930.000907.69140578-1
- Update to latest snapshot.

* Sat Sep 29 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.9+git180929.180051.46141d82-1
- Update to latest snapshot.

* Fri Sep 28 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.9+git180928.065334.d26212ea-1
- Update to latest snapshot.

* Fri Sep 28 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.9+git180927.233025.e1edbaed-1
- Update to latest snapshot.

* Thu Sep 27 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.9+git180927.205144.37c3b233-1
- Update to latest snapshot.

* Thu Sep 27 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.9+git180927.192958.c65d5e1d-1
- Update to latest snapshot.

* Thu Sep 27 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.9+git180927.182416.ed0c040f-1
- Update to latest snapshot.

* Thu Sep 27 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.9+git180927.122016.eb2ca9c2-1
- Update to latest snapshot.

* Thu Sep 27 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.9+git180927.113754.c82d0e34-1
- Update to latest snapshot.

* Thu Sep 27 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.9+git180927.000938.98a4e081-1
- Update to latest snapshot.

* Wed Sep 26 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.9+git180926.204536.0ad5a5a5-1
- Update to latest snapshot.

* Tue Sep 25 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.9+git180925.111752.893e7947-1
- Update to latest snapshot.

* Mon Sep 24 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.9+git180924.220054.665c8b14-1
- Update to latest snapshot.

* Mon Sep 24 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.9+git180924.170322.db24557a-1
- Update to latest snapshot.

* Mon Sep 24 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.9+git180924.124825.8482fbfb-1
- Update to latest snapshot.

* Mon Sep 24 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.9+git180924.072957.637ebea7-1
- Update to latest snapshot.

* Mon Sep 24 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.9+git180924.061859.759cd337-1
- Update to latest snapshot.

* Mon Sep 24 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.9+git180924.022907.308b2c35-1
- Update to latest snapshot.

* Sun Sep 23 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.9+git180923.225825.3d3aeeb5-1
- Update to latest snapshot.

* Sat Sep 22 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.9+git180922.001015.1dc8a908-1
- Update to latest snapshot.

* Mon Sep 17 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.9+git180917.162913.0bdef4b8-1
- Update to latest snapshot.

* Mon Sep 17 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.9+git180917.061502.29a8420a-1
- Update to latest snapshot.

* Fri Sep 14 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.9+git180914.054318.f57a7dc6-1
- Update to latest snapshot.

* Thu Sep 13 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.9+git180913.000158.ce4fdf6c-1
- Update to latest snapshot.

* Wed Sep 12 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.9+git180912.065335.a5b652d9-1
- Update to latest snapshot.

* Wed Sep 12 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.9+git180912.002251.63b69a92-1
- Update to latest snapshot.

* Tue Sep 11 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.9+git180911.171640.dd5eb7af-1
- Update to latest snapshot.

* Tue Sep 11 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.9+git180911.143646.7cb7c967-1
- Update to latest snapshot.

* Tue Sep 11 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.9+git180911.051802.2e8e5051-1
- Update to latest snapshot.

* Mon Sep 10 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.9+git180910.224114.7511b09e-1
- Update to latest snapshot.

* Mon Sep 10 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.9+git180910.215026.c44ea18f-1
- Update to latest snapshot.

* Mon Sep 10 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.9+git180910.202009.e9667822-1
- Update to latest snapshot.

* Mon Sep 10 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.9+git180910.174129.c5ad5185-1
- Update to latest snapshot.

* Mon Sep 10 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.9+git180910.163119.d05fb6d8-1
- Update to latest snapshot.

* Sun Sep 09 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.9+git180909.191518.dfe4039d-1
- Update to latest snapshot.

* Sun Sep 09 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.9+git180909.154716.d2836340-1
- Update to latest snapshot.

* Sun Sep 09 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.9+git180909.000237.9dd8f0bb-1
- Update to latest snapshot.

* Sat Sep 08 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.9+git180908.160020.18355e68-1
- Update to latest snapshot.

* Sat Sep 08 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.9+git180908.160016.4d399fde-1
- Update to latest snapshot.

* Sat Sep 08 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.9+git180908.045218.8d49198f-1
- Update to latest snapshot.

* Fri Sep 07 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.9+git180907.000542.26654617-1
- Update to latest snapshot.

* Thu Sep 06 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.9+git180906.000835.676448aa-1
- Update to latest snapshot.

* Wed Sep 05 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.9+git180904.230342.e2917f65-1
- Update to latest snapshot.

* Sun Sep 02 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.9+git180902.084659.b75ac84e-1
- Update to latest snapshot.

* Sat Sep 01 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.9+git180901.000755.beba0d51-1
- Update to latest snapshot.

* Fri Aug 31 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.9+git180831.000423.e6b6d63a-1
- Update to latest snapshot.

* Thu Aug 30 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.9+git180830.065916.f4085f9b-1
- Update to latest snapshot.

* Wed Aug 29 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.9+git180829.192545.3d2a4015-1
- Update to latest snapshot.

* Wed Aug 29 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.9+git180829.000305.19789e93-1
- Update to latest snapshot.

* Tue Aug 28 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.9+git180828.152220.713a1157-1
- Update to latest snapshot.

* Mon Aug 27 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.9+git180826.163915.95a7a70f-1
- Update to latest snapshot.

* Wed Aug 22 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.9+git180822.172922.12e4630a-1
- Update to latest snapshot.

* Tue Aug 21 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.9+git180821.215028.5345d18f-1
- Update to latest snapshot.

* Tue Aug 21 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.9+git180821.000255.3d245234-1
- Update to latest snapshot.

* Sat Aug 18 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.9+git180818.134557.5c9d6f86-1
- Update to latest snapshot.

* Sat Aug 18 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.9+git180818.091435.2c7b010f-1
- Update to latest snapshot.

* Thu Aug 16 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.9+git180816.150127.ca0bc768-1
- Update to latest snapshot.

* Thu Aug 16 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.9+git180814.170045.4a3ab1a9-2
- Occasional mass rebuild.

* Wed Aug 15 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.9+git180814.170045.4a3ab1a9-1
- Update to latest snapshot.

* Mon Aug 13 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.9+git180813.000229.502f26b0-1
- Update to latest snapshot.

* Sun Aug 12 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.9+git180812.105845.2b53ae9c-1
- Update to latest snapshot.

* Fri Aug 10 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.9+git180810.101824.e799a5f7-1
- Update to latest snapshot.

* Fri Aug 03 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.9+git180803.000507.c196f948-1
- Update to latest snapshot.

* Tue Jul 31 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.9+git180731.212533.ec699324-1
- Update to latest snapshot.

* Tue Jul 31 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.9+git180730.201241.f5a90f60-1
- Update to latest snapshot.

* Sun Jul 29 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.9+git180729.102854.1e67a8a2-1
- Update to latest snapshot.

* Fri Jul 27 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.9+git180727.000909.01c013e3-1
- Update to latest snapshot.

* Wed Jul 25 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.9+git180725.121214.8ef71280-1
- Update to latest snapshot.

* Wed Jul 25 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.9+git180725.000024.2051ce0e-1
- Update to latest snapshot.

* Tue Jul 24 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.9+git180724.000513.cbb61bec-1
- Update to latest snapshot.

* Sun Jul 22 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.9+git180722.000308.5eed6efb-1
- Update to latest snapshot.

* Sat Jul 21 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.9+git180721.000651.daa72481-1
- Update to latest snapshot.

* Fri Jul 20 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.9+git180720.000754.3abc668a-1
- Update to latest snapshot.

* Thu Jul 19 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.9+git180719.201540.b52ec6df-1
- Update to latest snapshot.

* Wed Jul 18 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.9+git180718.000515.d2e66a3f-1
- Update to latest snapshot.

* Mon Jul 16 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.9+git180716.110435.195dfc50-1
- Update to latest snapshot.

* Mon Jul 16 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.9+git180716.050851.282a65f2-1
- Update to latest snapshot.

* Sun Jul 15 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.9+git180715.195946.667e4b10-1
- Update to latest snapshot.

* Fri Jul 13 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.9+git180713.000318.047d9b7a-1
- Update to latest snapshot.

* Tue Jul 10 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.9+git180710.000300.ebb89343-1
- Update to latest snapshot.

* Mon Jul 09 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.9+git180709.140044.9c7705dc-1
- Update to latest snapshot.

* Sun Jul 08 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.9+git180708.144630.ac978c3a-1
- Update to latest snapshot.

* Sat Jul 07 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.9+git180707.185948.4034f1ff-1
- Update to latest snapshot.

* Fri Jul 06 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.9+git180706.000743.c06665ed-1
- Update to latest snapshot.

* Wed Jul 04 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.9+git180703.000544.933e2c52-1
- Update to latest snapshot.

* Fri Jun 15 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.9+git180615.000918.04088468-1
- Update to latest snapshot.

* Thu Jun 14 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.9+git180614.085342.d52fcee3-1
- Update to latest snapshot.

* Wed Jun 13 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.9+git180613.000556.ce815f5e-1
- Update to latest snapshot.

* Tue Jun 12 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.9+git180612.071256.8667b8c9-1
- Update to latest snapshot.

* Sun Jun 10 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.9+git180610.001007.05278754-1
- Update to latest snapshot.

* Fri Jun 08 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.9+git180608.164127.94564b1f-1
- Update to latest snapshot.

* Thu Jun 07 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.9+git180607.101228.7f972588-1
- Update to latest snapshot.

* Thu Jun 07 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.9+git180607.001147.a5fd8000-1
- Update to latest snapshot.

* Wed Jun 06 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.9+git180606.000654.ea1a9b7f-1
- Update to latest snapshot.

* Tue Jun 05 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.9+git180605.164426.a10b20e2-1
- Update to latest snapshot.

* Tue Jun 05 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.9+git180605.134634.80a4e68c-1
- Update to latest snapshot.

* Tue Jun 05 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.9+git180605.085653.7880bd3c-1
- Update to latest snapshot.

* Mon Jun 04 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.9+git180604.080750.2f49a777-1
- Update to latest snapshot.

* Sun Jun 03 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.9+git180603.162228.c53835cf-1
- Update to latest snapshot.

* Sun Jun 03 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.9+git180603.061609.b9d6f6eb-1
- Update to latest snapshot.

* Sat Jun 02 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.9+git180602.000756.17210430-1
- Update to latest snapshot.

* Fri Jun 01 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.9+git180601.000602.ecffdaee-1
- Update to latest snapshot.

* Thu May 31 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.9+git180530.160616.2170a0dc-1
- Update to latest snapshot.

* Wed May 30 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.9+git180530.041322.988d67e2-1
- Update to latest snapshot.

* Tue May 29 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.9+git180529.001803.68355738-1
- Update to latest snapshot.

* Mon May 28 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.9+git180528.050807.7173d0e2-1
- Update to latest snapshot.

* Sun May 27 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.9+git180527.120312.3c1517b1-1
- Update to latest snapshot.

* Sat May 26 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.9+git180525.125314.859ed97d-1
- Update to latest snapshot.

* Thu May 24 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.9+git180524.000910.113b4749-1
- Update to latest snapshot.

* Fri May 18 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.9+git180518.000628.6db60462-1
- Update to latest snapshot.

* Thu May 17 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.9+git180517.000304.4fcd29fb-1
- Update to latest snapshot.

* Wed May 16 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.9+git180516.194251.5d972c97-1
- Update to latest snapshot.

* Wed May 16 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.9+git180516.124415.a450f90d-1
- Update to latest snapshot.

* Wed May 16 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.9+git180516.090935.94223281-1
- Update to latest snapshot.

* Wed May 16 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.9+git180516.075514.c3bcf4fa-1
- Update to latest snapshot.

* Sun May 13 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.9+git180513.175222.08c9e7de-1
- Update to latest snapshot.

* Sun May 13 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.9+git180512.234453.bf0581d1-1
- Update to latest snapshot.

* Sat May 12 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.9+git180512.001420.eb5d7486-1
- Update to latest snapshot.

* Thu May 10 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.9+git180510.160626.e9e9585a-1
- Update to latest snapshot.

* Thu May 10 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.9+git180510.115629.7477951e-1
- Update to latest snapshot.

* Tue May 08 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.9+git180508.194236.4fb2e72d-1
- Update to latest snapshot.

* Tue May 08 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.9+git180508.152518.c1f586bc-1
- Update to latest snapshot.

* Tue May 08 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.9+git180508.001318.b18fa169-2
- Adapt to CMake -> meson switch.

* Tue May 08 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.9+git180508.001318.b18fa169-1
- Update to latest snapshot.

* Sun May 06 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.9+git180504.000941.41f3fbfc-1
- Update to latest snapshot.

* Thu Apr 26 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.9+git180426.194146.26005cb2-1
- Update to latest snapshot.

* Wed Apr 25 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.9+git180425.212157.a1eb6f03-1
- Update to latest snapshot.

* Fri Apr 20 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.9+git180420.001419.1afa61a8-1
- Update to latest snapshot.

* Fri Apr 13 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.9+git180412.214129.9ef60588-1
- Update to latest snapshot.

* Thu Apr 12 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.9+git180412.155329.582b5b27-1
- Update to latest snapshot.

* Thu Apr 12 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.9+git180412.042405.fd75c11c-1
- Update to latest snapshot.

* Sun Apr 08 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.9+git180407.203206.6c546fd9-1
- Update to latest snapshot.

* Wed Apr 04 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.9+git180404.000916.695e0840-1
- Update to latest snapshot.

* Tue Apr 03 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.9+git180402.000732.b8bdbbb4-1
- Update to latest snapshot.

* Wed Mar 28 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.9+git180328.000610.5fdd5824-1
- Update to latest snapshot.

* Sun Mar 25 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.9+git180323.224948.eaff25c9-1
- Update to latest snapshot.

* Thu Mar 22 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.9+git180322.045216.67198cfa-1
- Update to latest snapshot.

* Wed Mar 21 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.9+git180321.212416.3eb7d273-1
- Update to latest snapshot.

* Tue Mar 20 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.9+git180320.001433.91a465f7-1
- Update to latest snapshot.

* Mon Mar 19 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.9+git180319.044218.ecccab11-1
- Update to latest snapshot.

* Sun Mar 18 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.9+git180318.144104.f4b1a30f-1
- Update to latest snapshot.

* Sun Mar 18 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.9+git180318.135720.96d6a75c-1
- Update to latest snapshot.

* Sun Mar 18 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.9+git180318.124459.0d123816-1
- Update to latest snapshot.

* Sun Mar 18 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.9+git180317.203820.692f5423-2
- Remove upstreamed patch.

* Sat Mar 17 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.9+git180317.203820.692f5423-1
- Update to latest snapshot.

* Sat Mar 17 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.9+git180317.164242.a24e57a7-1
- Update to latest snapshot.

* Sat Mar 17 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.9+git180315.001711.2121b8c6-1
- Update to version 0.2.9.
- Add patch to fix building against vala 0.40 and new PackageKit.

* Thu Mar 15 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.6+git180315.001711.2121b8c6-1
- Update to latest snapshot.

* Wed Mar 14 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.6+git180314.183001.3b2e6e1c-1
- Update to latest snapshot.

* Wed Mar 14 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.6+git180314.162233.c3dfdfcf-1
- Update to latest snapshot.

* Wed Mar 14 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.6+git180314.073200.7ef40b5b-1
- Update to latest snapshot.

* Tue Mar 13 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.6+git180313.075618.dfaf4f24-2
- Adapt to upstream file changes.

* Tue Mar 13 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.6+git180313.075618.dfaf4f24-1
- Update to latest snapshot.

* Mon Mar 12 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.6+git180312.000907.0e65dc55-1
- Update to latest snapshot.

* Sat Mar 10 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.6+git180310.183738.d15d4f58-1
- Update to latest snapshot.

* Sat Mar 10 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.6+git180310.121547.51729b22-1
- Update to latest snapshot.

* Sat Mar 10 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.6+git180310.100711.61fb2d53-1
- Update to latest snapshot.

* Fri Mar 09 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.6+git180309.175736.df1cd2da-1
- Update to latest snapshot.

* Fri Mar 09 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.6+git180309.164648.9ee14d88-1
- Update to latest snapshot.

* Fri Mar 09 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.6+git180309.131125.7089aa7b-1
- Update to latest snapshot.

* Fri Mar 09 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.6+git180309.093215.599ac078-1
- Update to latest snapshot.

* Thu Mar 08 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.6+git180308.060423.a5b4dde7-1
- Update to latest snapshot.

* Tue Mar 06 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.6+git180306.194839.dd9f0109-1
- Update to latest snapshot.

* Tue Mar 06 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.6+git180306.000406.0aa8b8a6-1
- Update to latest snapshot.

* Mon Mar 05 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.6+git180305.183819.ad7fad3c-1
- Update to latest snapshot.

* Thu Mar 01 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.6+git180301.000240.071e2807-1
- Update to latest snapshot.

* Wed Feb 28 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.6+git180228.110208.0f821406-1
- Update to latest snapshot.

* Tue Feb 27 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.6+git180227.191132.5fc80c03-1
- Update to latest snapshot.

* Mon Feb 26 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.6+git180226.095318.1f74ccb3-1
- Update to latest snapshot.

* Sun Feb 25 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.6+git180225.080834.9b1ec3fa-1
- Update to latest snapshot.

* Sat Feb 24 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.6+git180224.112148.4369636b-1
- Update to latest snapshot.

* Fri Feb 23 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.6+git180223.192609.8f45dc5a-1
- Update to latest snapshot.

* Fri Feb 23 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.6+git180223.185445.19cd7df8-1
- Update to latest snapshot.

* Fri Feb 23 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.6+git180223.000348.36e919fd-1
- Update to latest snapshot.

* Thu Feb 22 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.6+git180221.221618.37b547ae-1
- Update to latest snapshot.

* Wed Feb 21 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.6+git180221.000642.3006a65a-1
- Update to latest snapshot.

* Tue Feb 20 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.6+git180220.000928.629bc395-1
- Update to latest snapshot.

* Mon Feb 19 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.6+git180219.175308.9a9f37cb-1
- Update to latest snapshot.

* Mon Feb 19 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.6+git180219.081632.87032c69-1
- Update to latest snapshot.

* Sun Feb 18 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.6+git180218.193755.b42bc5ea-1
- Update to latest snapshot.

* Sun Feb 18 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.6+git180218.185623.e801186d-1
- Update to latest snapshot.

* Sun Feb 18 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.6+git180218.000056.b78ab94d-1
- Update to latest snapshot.

* Thu Feb 15 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.6+git180215.204626.de86be5b-1
- Update to latest snapshot.

* Wed Feb 14 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.6+git180214.172809.63ce7d33-1
- Update to latest snapshot.

* Tue Feb 13 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.6+git180213.000843.d16c39b2-1
- Update to latest snapshot.

* Mon Feb 12 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.6+git180212.213601.343f7e45-1
- Update to latest snapshot.

* Mon Feb 12 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.6+git180212.000337.358f5cfa-1
- Update to latest snapshot.

* Fri Feb 09 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.6+git180209.000851.e8637463-1
- Update to latest snapshot.

* Tue Feb 06 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.6+git180205.235746.b2b77757-1
- Update to latest snapshot.

* Mon Feb 05 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.6+git180205.001002.8f499069-1
- Update to latest snapshot.

* Sun Feb 04 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.6+git180204.000624.9c7c38b6-1
- Update to latest snapshot.

* Sat Feb 03 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.6+git180203.215502.5f5a1aa0-1
- Update to latest snapshot.

* Sat Feb 03 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.6+git180203.000541.a5697610-1
- Update to latest snapshot.

* Wed Jan 31 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.6+git180131.152620.90b23867-1
- Update to latest snapshot.

* Tue Jan 30 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.6+git180130.143318.7890f52a-1
- Update to latest snapshot.

* Tue Jan 30 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.6+git180130.000820.555a0701-1
- Update to latest snapshot.

* Mon Jan 29 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.6+git180129.000122.3a11759c-1
- Update to latest snapshot.

* Sun Jan 28 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.6+git180128.000648.4b594c93-1
- Update to latest snapshot.

* Sat Jan 27 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.6+git180127.170820.b9effd52-1
- Update to latest snapshot.

* Thu Jan 25 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.6+git180125.170038.94b4fb1a-1
- Update to latest snapshot.

* Sat Jan 20 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.6+git180120.193845.a0b001ee-1
- Update to latest snapshot.

* Tue Jan 16 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.6+git180116.185634.738959cb-1
- Update to latest snapshot.

* Wed Jan 10 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.6+git180110.040207.6aa44990-1
- Update to latest snapshot.

* Tue Jan 09 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.6+git180109.180237.856fb2bd-1
- Update to latest snapshot.

* Sun Jan 07 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.6+git180107.020946.9dd43eec-1
- Update to latest snapshot.

* Sat Jan 06 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.6+git180106.032641.6df82f38-1
- Update to latest snapshot.

* Wed Jan 03 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.6+git180103.061910.fc648f73-1
- Update to latest snapshot.

* Sun Dec 31 2017 Fabio Valentini <decathorpe@gmail.com> - 0.2.6+git171227.185100.723c8f03-2
- Merge .spec file from fedora.

* Wed Dec 27 2017 Fabio Valentini <decathorpe@gmail.com> - 0.2.6+git171227.185100.723c8f03-1
- Update to latest snapshot.

* Sun Dec 24 2017 Fabio Valentini <decathorpe@gmail.com> - 0.2.6+git171222.103844.22508f22-1
- Update to latest snapshot.

* Sat Nov 18 2017 Fabio Valentini <decathorpe@gmail.com> - 0.2.6+git171118.062211.0f398415-1
- Update to latest snapshot.

* Wed Nov 15 2017 Fabio Valentini <decathorpe@gmail.com> - 0.2.6+git171114.213935.e957877e-1
- Update to latest snapshot.

* Tue Nov 14 2017 Fabio Valentini <decathorpe@gmail.com> - 0.2.6+git171114.073733.017a7a02-1
- Update to latest snapshot.

* Sun Nov 12 2017 Fabio Valentini <decathorpe@gmail.com> - 0.2.6+git171112.005829.7e593a42-1
- Update to latest snapshot.

* Thu Nov 09 2017 Fabio Valentini <decathorpe@gmail.com> - 0.2.6+git171109.205832.22a5e551-1
- Update to latest snapshot.

* Wed Nov 08 2017 Fabio Valentini <decathorpe@gmail.com> - 0.2.6+git171108.044803.40e296c8-1
- Update to latest snapshot.

* Tue Nov 07 2017 Fabio Valentini <decathorpe@gmail.com> - 0.2.6+git171107.121838.053c345c-1
- Update to latest snapshot.

* Wed Nov 01 2017 Fabio Valentini <decathorpe@gmail.com> - 0.2.6+git171101.025104.098a1b86-1
- Update to latest snapshot.

* Tue Oct 31 2017 Fabio Valentini <decathorpe@gmail.com> - 0.2.6+git171031.074726.75044a65-1
- Update to latest snapshot.

* Mon Oct 30 2017 Fabio Valentini <decathorpe@gmail.com> - 0.2.6+git171030.155900.8f2ee894-1
- Update to latest snapshot.

* Mon Oct 30 2017 Fabio Valentini <decathorpe@gmail.com> - 0.2.6+git171030.004743.415dd58c-1
- Update to latest snapshot.

* Sun Oct 29 2017 Fabio Valentini <decathorpe@gmail.com> - 0.2.6+git171029.151629.b0ee2e50-1
- Update to latest snapshot.

* Sun Oct 29 2017 Fabio Valentini <decathorpe@gmail.com> - 0.2.6+git171029.103731.24188893-1
- Update to latest snapshot.

* Sat Oct 28 2017 Fabio Valentini <decathorpe@gmail.com> - 0.2.6+git171028.045311.e2d40d70-1
- Update to latest snapshot.

* Fri Oct 27 2017 Fabio Valentini <decathorpe@gmail.com> - 0.2.6+git171027.030407.932b095c-1
- Update to latest snapshot.

* Tue Oct 24 2017 Fabio Valentini <decathorpe@gmail.com> - 0.2.6+git171024.015602.e7f0ae6b-1
- Update to latest snapshot.

* Tue Oct 10 2017 Fabio Valentini <decathorpe@gmail.com> - 0.2.6+git171010.000929.8e85b24d-1
- Update to latest snapshot.

* Wed Sep 27 2017 Fabio Valentini <decathorpe@gmail.com> - 0.2.6+git170927.181545.bf042057-1
- Update to latest snapshot.

* Tue Sep 26 2017 Fabio Valentini <decathorpe@gmail.com> - 0.2.6+git170926.154106.5db65beb-1
- Update to latest snapshot.

* Mon Sep 25 2017 Fabio Valentini <decathorpe@gmail.com> - 0.2.6+git170925.175511.7b9cd220-1
- Update to latest snapshot.

* Mon Sep 18 2017 Fabio Valentini <decathorpe@gmail.com> - 0.2.6+git170918.120132.ddf31ddf-1
- Update to version 0.2.6.

* Mon Sep 18 2017 Fabio Valentini <decathorpe@gmail.com> - 0.2.5+git170918.120132.ddf31ddf-1
- Update to latest snapshot.

* Tue Sep 12 2017 Fabio Valentini <decathorpe@gmail.com> - 0.2.5+git170912.054017.faa8ab69-2
- Adapt to upstream file changes.

* Tue Sep 12 2017 Fabio Valentini <decathorpe@gmail.com> - 0.2.5+git170912.054017.faa8ab69-1
- Update to latest snapshot.

* Sun Sep 03 2017 Fabio Valentini <decathorpe@gmail.com> - 0.2.5+git170903.172706.bae49ce1-1
- Update to latest snapshot.

* Sun Aug 27 2017 Fabio Valentini <decathorpe@gmail.com> - 0.2.5+git170827.175930.e19701b3-1
- Update to latest snapshot.

* Sun Aug 13 2017 Fabio Valentini <decathorpe@gmail.com> - 0.2.5+git170813.155655.c6cf867a-1
- Update to latest snapshot.

* Sat Aug 12 2017 Fabio Valentini <decathorpe@gmail.com> - 0.2.5+git170812.175949.1c6b7ae4-1
- Update to latest snapshot.

* Thu Aug 10 2017 Fabio Valentini <decathorpe@gmail.com> - 0.2.5+git170810.215512.0e177955-2
- Adapt to upstream file changes.

* Thu Aug 10 2017 Fabio Valentini <decathorpe@gmail.com> - 0.2.5+git170810.215512.0e177955-1
- Update to latest snapshot.

* Wed Aug 09 2017 Fabio Valentini <decathorpe@gmail.com> - 0.2.5+git170809.192952.ce5ada7f-1
- Update to latest snapshot.

* Tue Aug 08 2017 Fabio Valentini <decathorpe@gmail.com> - 0.2.5+git170808.180903.10b564fb-1
- Update to latest snapshot.

* Tue Aug 08 2017 Fabio Valentini <decathorpe@gmail.com> - 0.2.5+git170807.222059.baded6e3-1
- Update to latest snapshot.

* Mon Aug 07 2017 Fabio Valentini <decathorpe@gmail.com> - 0.2.5+git170807.174100.a08d30fb-1
- Update to latest snapshot.

* Sat Aug 05 2017 Fabio Valentini <decathorpe@gmail.com> - 0.2.5+git170804.110814.126340bc-1
- Update to version 0.2.5.

* Fri Aug 04 2017 Fabio Valentini <decathorpe@gmail.com> - 0.2.4+git170804.110814.126340bc-1
- Update to latest snapshot.

* Fri Aug 04 2017 Fabio Valentini <decathorpe@gmail.com> - 0.2.4+git170804.090836.0d17178e-1
- Update to latest snapshot.

* Thu Aug 03 2017 Fabio Valentini <decathorpe@gmail.com> - 0.2.4+git170803.113426.527555e7-1
- Update to latest snapshot.

* Thu Aug 03 2017 Fabio Valentini <decathorpe@gmail.com> - 0.2.4+git170803.003400.d1531957-1
- Update to latest snapshot.

* Mon Jul 31 2017 Fabio Valentini <decathorpe@gmail.com> - 0.2.4+git170731.093655.90429bd1-1
- Update to latest snapshot.

* Mon Jul 31 2017 Fabio Valentini <decathorpe@gmail.com> - 0.2.4+git170731.001829.9751452c-1
- Update to latest snapshot.

* Mon Jul 24 2017 Fabio Valentini <decathorpe@gmail.com> - 0.2.4+git170723.220333.3356ab2f-2
- Adapt to upstream file changes.

* Mon Jul 24 2017 Fabio Valentini <decathorpe@gmail.com> - 0.2.4+git170723.220333.3356ab2f-1
- Update to latest snapshot.

* Thu Jul 20 2017 Fabio Valentini <decathorpe@gmail.com> - 0.2.4+git170720.054139.cf31a22b-1
- Update to latest snapshot.

* Wed Jul 19 2017 Fabio Valentini <decathorpe@gmail.com> - 0.2.4+git170718.175216.16372710-2
- Adapt to upstream file changes.

* Tue Jul 18 2017 Fabio Valentini <decathorpe@gmail.com> - 0.2.4+git170718.175216.16372710-1
- Update to latest snapshot.

* Sat Jul 15 2017 Fabio Valentini <decathorpe@gmail.com> - 0.2.4+git170714.230959.591bb445-1
- Update to latest snapshot.

* Thu Jul 13 2017 Fabio Valentini <decathorpe@gmail.com> - 0.2.4+git170713.205109.9ea3933b-1
- Update to latest snapshot.

* Wed Jul 12 2017 Fabio Valentini <decathorpe@gmail.com> - 0.2.4+git170712.170737.138f4d4f-1
- Update to latest snapshot.

* Tue Jul 11 2017 Fabio Valentini <decathorpe@gmail.com> - 0.2.4+git170711.040555.698d965a-1
- Update to latest snapshot.

* Tue Jul 04 2017 Fabio Valentini <decathorpe@gmail.com> - 0.2.4+git170704.071253.a19a8ed0-1
- Update to version 0.2.4.

* Tue Jul 04 2017 Fabio Valentini <decathorpe@gmail.com> - 0.2.3+git170704.071253.a19a8ed0-1
- Update to latest snapshot.

* Mon Jul 03 2017 Fabio Valentini <decathorpe@gmail.com> - 0.2.3+git170703.175000.3c715889-1
- Update to latest snapshot.

* Sat Jul 01 2017 Fabio Valentini <decathorpe@gmail.com> - 0.2.3+git170630.165357.34d6bae0-1
- Update to latest snapshot.

* Thu Jun 29 2017 Fabio Valentini <decathorpe@gmail.com> - 0.2.3+git170629.080704.4b6a0b28-1
- Update to latest snapshot.

* Wed Jun 28 2017 Fabio Valentini <decathorpe@gmail.com> - 0.2.3+git170628.153224.2db4ee39-1
- Update to latest snapshot.

* Wed Jun 28 2017 Fabio Valentini <decathorpe@gmail.com> - 0.2.3+git170627.230748.471b0dc6-1
- Update to latest snapshot.

* Tue Jun 27 2017 Fabio Valentini <decathorpe@gmail.com> - 0.2.3+git170627.174257.a06ee6bb-1
- Update to latest snapshot.

* Tue Jun 27 2017 Fabio Valentini <decathorpe@gmail.com> - 0.2.3+git170627.031850.07b11b49-1
- Update to latest snapshot.

* Mon Jun 26 2017 Fabio Valentini <decathorpe@gmail.com> - 0.2.3+git170626.150803.e1f5348f-1
- Update to latest snapshot.

* Sun Jun 25 2017 Fabio Valentini <decathorpe@gmail.com> - 0.2.3+git170625.182444.91ec20dc-1
- Update to latest snapshot.

* Sun Jun 25 2017 Fabio Valentini <decathorpe@gmail.com> - 0.2.3+git170625.175109.22c794f7-1
- Update to latest snapshot.

* Sun Jun 25 2017 Fabio Valentini <decathorpe@gmail.com> - 0.2.3+git170625.165352.cb934f4c-1
- Update to latest snapshot.

* Sun Jun 25 2017 Fabio Valentini <decathorpe@gmail.com> - 0.2.3+git170625.001649.c418324d-1
- Update to latest snapshot.

* Sat Jun 24 2017 Fabio Valentini <decathorpe@gmail.com> - 0.2.3+git170623.195358.092b3c97-1
- Update to latest snapshot.

* Wed Jun 21 2017 Fabio Valentini <decathorpe@gmail.com> - 0.2.3+git170621.155642.99aff8ba-1
- Update to latest snapshot.

* Tue Jun 20 2017 Fabio Valentini <decathorpe@gmail.com> - 0.2.3+git170620.185636.cafdd5d1-1
- Update to latest snapshot.

* Sun Jun 18 2017 Fabio Valentini <decathorpe@gmail.com> - 0.2.3+git170617.180441.589f8e33-1
- Update to latest snapshot.

* Fri Jun 16 2017 Fabio Valentini <decathorpe@gmail.com> - 0.2.3+git170616.210038.c4c03ab8-1
- Update to latest snapshot.

* Mon Jun 12 2017 Fabio Valentini <decathorpe@gmail.com> - 0.2.3+git170612.165127.7f4cf6a7-1
- Update to latest snapshot.

* Thu Jun 08 2017 Fabio Valentini <decathorpe@gmail.com> - 0.2.3+git170607.162037.dfeda7bb-1
- Update to latest snapshot.

* Thu Jun 01 2017 Fabio Valentini <decathorpe@gmail.com> - 0.2.3+git170531.221524.125e08de-1
- Update to version 0.2.3.

* Thu Jun 01 2017 Fabio Valentini <decathorpe@gmail.com> - 0.2.2+git170531.221524.125e08de-1
- Update to latest snapshot.

* Tue May 30 2017 Fabio Valentini <decathorpe@gmail.com> - 0.2.2+git170530.015919.616ab29a-1
- Update to latest snapshot.

* Sat May 27 2017 Fabio Valentini <decathorpe@gmail.com> - 0.2.2+git170527.161220.d0507512-1
- Update to latest snapshot.

* Fri May 26 2017 Fabio Valentini <decathorpe@gmail.com> - 0.2.2+git170526.014646.7b3948b0-1
- Update to latest snapshot.

* Thu May 25 2017 Fabio Valentini <decathorpe@gmail.com> - 0.2.2+git170525.173221.baa7a2f0-1
- Update to latest snapshot.

* Thu May 25 2017 Fabio Valentini <decathorpe@gmail.com> - 0.2.2+git170525.153047.6e2bc083-1
- Update to latest snapshot.

* Wed May 24 2017 Fabio Valentini <decathorpe@gmail.com> - 0.2.2+git170523.211034.125f06aa-1
- Update to latest snapshot.

* Tue May 23 2017 Fabio Valentini <decathorpe@gmail.com> - 0.2.2+git170523.072723.789f1fdf-1
- Update to latest snapshot.

* Mon May 22 2017 Fabio Valentini <decathorpe@gmail.com> - 0.2.2+git170522.152445.73b8f3b7-1
- Update to version 0.2.2.

* Mon May 22 2017 Fabio Valentini <decathorpe@gmail.com> - 0.2.1+git170522.152445.73b8f3b7-1
- Update to latest snapshot.

* Mon May 22 2017 Fabio Valentini <decathorpe@gmail.com> - 0.2.1+git170522.061740.586c1690-1
- Update to latest snapshot.

* Sun May 21 2017 Fabio Valentini <decathorpe@gmail.com> - 0.2.1+git170521.214503.dfefe9d8-1
- Update to latest snapshot.

* Sun May 21 2017 Fabio Valentini <decathorpe@gmail.com> - 0.2.1+git170521.161028.fb2287e5-1
- Update to latest snapshot.

* Sat May 20 2017 Fabio Valentini <decathorpe@gmail.com> - 0.2.1+git170520.165836.1598debe-1
- Update to version 0.2.1.

* Sat May 20 2017 Fabio Valentini <decathorpe@gmail.com> - 0.2+git170520.165836.1598debe-1
- Update to latest snapshot.

* Sat May 20 2017 Fabio Valentini <decathorpe@gmail.com> - 0.2+git170520.145331.f89bc0bb-1
- Update to latest snapshot.

* Sat May 20 2017 Fabio Valentini <decathorpe@gmail.com> - 0.2+git170520.023328.c45c11ee-1
- Update to latest snapshot.

* Fri May 19 2017 Fabio Valentini <decathorpe@gmail.com> - 0.2+git170519.193742.00c3fe0f-1
- Update to latest snapshot.

* Thu May 18 2017 Fabio Valentini <decathorpe@gmail.com> - 0.2+git170518.142122.a1f3e3f5-1
- Update to latest snapshot.

* Thu May 18 2017 Fabio Valentini <decathorpe@gmail.com> - 0.2+git170517.113513.8e5c70f9-1
- Update to version 0.2.

* Wed May 17 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.4+rev628-1
- Update to latest snapshot.

* Wed May 17 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.4+rev627-1
- Update to latest snapshot.

* Tue May 16 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.4+rev623-1
- Update to latest snapshot.

* Tue May 09 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.4+rev621-1
- Update to latest snapshot.

* Sun May 07 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.4+rev658-1
- Update to latest snapshot.

* Sun May 07 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.4+rev651-1
- Update to latest snapshot.

* Fri May 05 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.4+rev650-1
- Update to latest snapshot.

* Sun Apr 30 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.4+rev592-1
- Update to latest snapshot.

* Thu Apr 27 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.4+rev591-1
- Update to latest snapshot.

* Tue Apr 25 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.4+rev588-1
- Update to latest snapshot.

* Fri Apr 21 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.4+rev587-1
- Update to latest snapshot.

* Fri Apr 21 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.4+rev585-1
- Update to latest snapshot.

* Tue Apr 18 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.4+rev584-1
- Update to latest snapshot.

* Sun Apr 16 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.4+rev583-1
- Update to latest snapshot.

* Sun Apr 16 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.4+rev582-1
- Update to latest snapshot.

* Sat Apr 15 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.4+rev581-1
- Update to latest snapshot.

* Sat Apr 15 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.4+rev580-1
- Update to latest snapshot.

* Tue Apr 11 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.4+rev564-1
- Update to latest snapshot.

* Mon Apr 10 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.4+rev557-1
- Update to latest snapshot.

* Mon Apr 10 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.4+rev555-1
- Update to latest snapshot.

* Sun Apr 09 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.4+rev538-1
- Update to latest snapshot.

* Sun Apr 09 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.4+rev535-1
- Update to latest snapshot.

* Sun Apr 09 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.4+rev525-1
- Update to latest snapshot.

* Sat Apr 08 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.4+rev509-1
- Update to latest snapshot.

* Sat Apr 08 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.4+rev501-1
- Update to latest snapshot.

* Sat Apr 08 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.4+rev481-1
- Update to latest snapshot.

* Fri Apr 07 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.4+rev477-1
- Update to latest snapshot.

* Fri Apr 07 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.4+rev475-1
- Update to latest snapshot.

* Thu Apr 06 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.4+rev471-1
- Update to latest snapshot.

* Tue Apr 04 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.4+rev466-1
- Update to latest snapshot.

* Mon Apr 03 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.4+rev464-1
- Update to latest snapshot.

* Sat Apr 01 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.4+rev456-1
- Update to latest snapshot.

* Thu Mar 30 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.4+rev454-1
- Update to latest snapshot.

* Thu Mar 30 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.4+rev452-1
- Update to latest snapshot.

* Thu Mar 30 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.4+rev448-1
- Update to latest snapshot.

* Wed Mar 29 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.4+rev446-1
- Update to latest snapshot.

* Tue Mar 28 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.4+rev445-2
- Adapt to upstream file name changes.

* Tue Mar 28 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.4+rev445-1
- Update to latest snapshot.

* Mon Mar 27 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.4+rev444-1
- Update to latest snapshot.

* Sun Mar 26 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.4+rev443-1
- Update to latest snapshot.

* Sun Mar 26 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.4+rev441-1
- Update to latest snapshot.

* Wed Mar 22 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.4+rev437-1
- Update to latest snapshot.

* Wed Mar 22 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.4+rev433-1
- Update to latest snapshot.

* Tue Mar 21 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.4+rev431-1
- Update to latest snapshot.

* Tue Mar 21 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.4+rev430-2
- Add new missing BRs json-glib and libsoup.

* Tue Mar 21 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.4+rev430-1
- Update to latest snapshot.

* Thu Mar 16 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.4+rev415-1
- Update to version 0.1.4.

* Thu Mar 16 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.3+rev415-1
- Update to latest snapshot.

* Thu Mar 16 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.3+rev414-1
- Update to latest snapshot.

* Wed Mar 15 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.3+rev413-1
- Update to latest snapshot.

* Tue Mar 14 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.3+rev412-1
- Update to latest snapshot.

* Thu Mar 09 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.3+rev411-1
- Update to latest snapshot.

* Wed Mar 08 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.3+rev410-2
- Move appdata to approved location.

* Tue Mar 07 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.3+rev410-1
- Update to latest snapshot.

* Thu Mar 02 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.3+rev409-1
- Update to latest snapshot.

* Tue Feb 28 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.3+rev408-1
- Update to latest snapshot.

* Mon Feb 27 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.3+rev407-1
- Update to latest snapshot.

* Sat Feb 25 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.3+rev406-1
- Update to latest snapshot.

* Mon Feb 20 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.3+rev405-1
- Update to latest snapshot.

* Mon Feb 20 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.3+rev404-1
- Update to latest snapshot.

* Sat Feb 18 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.3+rev403-1
- Update to latest snapshot.

* Sat Feb 18 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.3+rev402-1
- Update to latest snapshot.

* Thu Feb 16 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.3+rev401-1
- Update to latest snapshot.

* Wed Feb 15 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.3+rev400-1
- Update to latest snapshot.

* Mon Feb 13 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.3+rev399-1
- Update to latest snapshot.

* Sun Feb 12 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.3+rev398-1
- Update to latest snapshot.

* Sat Feb 11 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.3+rev397-1
- Update to latest snapshot.

* Fri Feb 10 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.3+rev394-1
- Update to latest snapshot.

* Thu Feb 09 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.3+rev393-1
- Update to latest snapshot.

* Mon Feb 06 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.3+rev392-1
- Update to latest snapshot.

* Sun Feb 05 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.3+rev391-1
- Update to latest snapshot.

* Sat Feb 04 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.3+rev390-1
- Update to latest snapshot.

* Thu Feb 02 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.3+rev388-1
- Update to latest snapshot.

* Mon Jan 30 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.3+rev387-1
- Update to latest snapshot.

* Sun Jan 29 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.3+rev386-1
- Update to latest snapshot.

* Sat Jan 28 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.3+rev385-1
- Update to latest snapshot.

* Fri Jan 27 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.3+rev384-1
- Update to latest snapshot.

* Thu Jan 26 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.3+rev383-2
- Sync with fedora packaging.

* Thu Jan 26 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.3+rev383-1
- Update to latest snapshot.

* Wed Jan 25 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.3+rev382-1
- Update to latest snapshot.

* Tue Jan 24 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.3+rev381-1
- Update to latest snapshot.

* Mon Jan 23 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.3+rev379-1
- Update to latest snapshot.

* Sat Jan 21 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.3+rev378-1
- Update to latest snapshot.

* Thu Jan 19 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.3+rev377-1
- Update to latest snapshot.

* Wed Jan 18 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.3+rev376-1
- Update to latest snapshot.

* Tue Jan 17 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.3+rev375-1
- Update to latest snapshot.

* Thu Jan 12 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.3+rev374-1
- Update to latest snapshot.

* Wed Jan 11 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.3+rev373-1
- Update to latest snapshot.

* Tue Jan 10 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.3+rev372-1
- Update to latest snapshot.

* Mon Jan 09 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.3+rev371-1
- Update to latest snapshot.

* Sun Jan 08 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.3+rev370-1
- Update to latest snapshot.

* Sat Jan 07 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.3+rev369-1
- Update to latest snapshot.

* Fri Jan 06 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.3+rev368-1
- Update to latest snapshot.

* Wed Jan 04 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.3+rev367-1
- Update to latest snapshot.

* Tue Jan 03 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.3+rev366-1
- Update to latest snapshot.

* Mon Jan 02 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.3+rev365-1
- Update to latest snapshot.

* Sun Jan 01 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.3+rev364-1
- Update to latest snapshot.

* Sat Dec 31 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.3+rev362-1
- Update to latest snapshot.

* Fri Dec 30 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.3+rev361-1
- Update to latest snapshot.

* Wed Dec 28 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.3+rev358-1
- Update to latest snapshot.

* Tue Dec 27 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.3+rev355-1
- Update to latest snapshot.

* Sat Dec 24 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.3+rev354-2
- Enable libunity support.

* Thu Dec 22 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.3+rev354-1
- Update to latest snapshot.

* Wed Dec 21 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.3+rev353-1
- Update to latest snapshot.

* Sun Dec 18 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.3+rev352-1
- Update to latest snapshot.

* Sat Dec 17 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.3+rev351-1
- Update to latest snapshot.

* Fri Dec 09 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.3+rev350-1
- Update to latest snapshot.

* Thu Dec 08 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.3+rev349-1
- Update to latest snapshot.

* Wed Dec 07 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.3+rev348-1
- Update to latest snapshot.

* Tue Dec 06 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.3+rev347-1
- Update to latest snapshot.

* Mon Dec 05 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.3+rev346-1
- Update to version 0.1.3.

* Mon Dec 05 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+rev346-1
- Update to latest snapshot.

* Sun Dec 04 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+rev344-1
- Update to latest snapshot.

* Fri Dec 02 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+rev343-1
- Update to latest snapshot.

* Fri Dec 02 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+rev342-1
- Update to latest snapshot.

* Fri Nov 25 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+rev341-1
- Update to latest snapshot.

* Wed Nov 23 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+rev340-1
- Update to latest snapshot.

* Tue Nov 22 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+rev339-1
- Update to latest snapshot.

* Sun Nov 20 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+rev338-1
- Update to latest snapshot.

* Fri Nov 18 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+rev337-1
- Update to latest snapshot.

* Wed Nov 16 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+rev336-1
- Update to latest snapshot.

* Mon Nov 07 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+rev335-1
- Update to latest snapshot.

* Sun Nov 06 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+rev334-1
- Update to latest snapshot.

* Sat Nov 05 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+rev333-1
- Update to latest snapshot.

* Fri Nov 04 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+rev332-1
- Update to latest snapshot.

* Tue Nov 01 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+rev331-1
- Update to latest snapshot.

* Sat Oct 29 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+rev330-1
- Update to latest snapshot.

* Fri Oct 28 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+rev329-1
- Update to latest snapshot.

* Thu Oct 27 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+rev328-2
- Remove patch. Only build on f25 now.

* Wed Oct 26 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+rev328-1
- Update to latest snapshot.

* Sun Oct 23 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+rev327-1
- Update to latest snapshot.

* Sat Oct 22 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+rev326-1
- Update to latest snapshot.

* Fri Oct 21 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+rev325-1
- Update to latest snapshot.

* Mon Oct 17 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+rev324-1
- Update to latest snapshot.

* Sun Oct 16 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+rev323-1
- Update to latest snapshot.

* Sat Oct 15 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+rev322-1
- Update to version 0.1.1.


