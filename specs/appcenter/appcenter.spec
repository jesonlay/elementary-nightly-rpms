%global appname io.elementary.appcenter

Name:           appcenter
Summary:        Software Center for the Pantheon desktop
Version:        0.2.6+git%{date}.%{commit}
Release:        1%{?dist}
License:        GPLv3

URL:            https://github.com/elementary/%{name}
Source0:        %{name}-%{version}.tar.gz

# Upstream elementaryOS blacklist adapted to fedora
Source1:        appcenter.blacklist

BuildRequires:  cmake
BuildRequires:  cmake-elementary
BuildRequires:  desktop-file-utils
BuildRequires:  gettext
BuildRequires:  intltool
BuildRequires:  libappstream-glib
BuildRequires:  vala >= 0.26

BuildRequires:  appstream-vala

BuildRequires:  pkgconfig(appstream) >= 0.10.0
BuildRequires:  pkgconfig(gee-0.8)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(granite)
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


%prep
%autosetup


%build
mkdir build && pushd build
%cmake ..
%make_build
popd


%install
pushd build
%make_install
popd

%find_lang %{appname}

# override empty blacklist with one for fedora
cp -pav %{SOURCE1} %{buildroot}/%{_sysconfdir}/%{appname}/appcenter.blacklist


%check
desktop-file-validate \
    %{buildroot}/%{_datadir}/applications/%{appname}.desktop

appstream-util validate-relax --nonet \
    %{buildroot}/%{_datadir}/metainfo/%{appname}.appdata.xml


%files -f %{appname}.lang
%doc AUTHORS README.md
%license COPYING

%dir %{_sysconfdir}/%{appname}
%config(noreplace) %{_sysconfdir}/%{appname}/appcenter.blacklist

%{_bindir}/%{appname}

%{_datadir}/applications/%{appname}.desktop
%{_datadir}/applications/%{appname}-daemon.desktop
%{_datadir}/dbus-1/services/%{appname}.service
%{_datadir}/glib-2.0/schemas/%{appname}.gschema.xml
%{_datadir}/metainfo/%{appname}.appdata.xml


%changelog
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


