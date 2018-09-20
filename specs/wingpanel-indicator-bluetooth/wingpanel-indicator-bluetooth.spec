%global __provides_exclude_from ^%{_libdir}/wingpanel/.*\\.so$

Name:           wingpanel-indicator-bluetooth
Summary:        Bluetooth Indicator for wingpanel
Version:        2.1.0+git%{date}.%{commit}
Release:        1%{?dist}
License:        LGPLv2+

URL:            https://github.com/elementary/%{name}
Source0:        %{name}-%{version}.tar.gz

BuildRequires:  gettext
BuildRequires:  meson
BuildRequires:  vala >= 0.22.0
BuildRequires:  vala-tools

BuildRequires:  pkgconfig(glib-2.0) >= 2.32
BuildRequires:  pkgconfig(granite)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(libnotify)
BuildRequires:  pkgconfig(wingpanel-2.0)

Requires:       bluez

Supplements:    (bluez and wingpanel%{?_isa})


%description
A bluetooth indicator for wingpanel.


%prep
%autosetup


%build
%meson
%meson_build


%install
%meson_install

%find_lang bluetooth-indicator


%files -f bluetooth-indicator.lang
%doc README.md
%license COPYING

%{_libdir}/wingpanel/libbluetooth.so

%{_datadir}/glib-2.0/schemas/io.elementary.desktop.wingpanel.bluetooth.gschema.xml


%changelog
* Thu Sep 20 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.0+git180920.000546.2f0a985f-1
- Update to latest snapshot.

* Thu Aug 30 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.0+git180830.000855.f3abc0b2-1
- Update to latest snapshot.

* Sun Aug 19 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.0+git180819.001024.4ae3f1ea-1
- Update to latest snapshot.

* Thu Aug 16 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.0+git180627.164117.0f5e52b6-2
- Occasional mass rebuild.

* Wed Jul 04 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.0+git180627.164117.0f5e52b6-1
- Update to latest snapshot.

* Mon Jun 11 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.0+git180611.184140.332cf732-1
- Update to version 2.1.0.

* Mon Jun 11 2018 Fabio Valentini <decathorpe@gmail.com> - 2.0.3+git180611.184140.332cf732-1
- Update to latest snapshot.

* Sat Jun 09 2018 Fabio Valentini <decathorpe@gmail.com> - 2.0.3+git180609.122607.79a96371-1
- Update to latest snapshot.

* Wed Jun 06 2018 Fabio Valentini <decathorpe@gmail.com> - 2.0.3+git180606.152824.c6d5322d-2
- Adapt to upstream file changes.

* Wed Jun 06 2018 Fabio Valentini <decathorpe@gmail.com> - 2.0.3+git180606.152824.c6d5322d-1
- Update to latest snapshot.

* Wed Jun 06 2018 Fabio Valentini <decathorpe@gmail.com> - 2.0.3+git180606.141250.afbb5799-1
- Update to latest snapshot.

* Thu May 31 2018 Fabio Valentini <decathorpe@gmail.com> - 2.0.3+git180531.080340.e333276d-1
- Update to latest snapshot.

* Tue May 29 2018 Fabio Valentini <decathorpe@gmail.com> - 2.0.3+git180529.001552.fd92da2c-1
- Update to latest snapshot.

* Sun May 13 2018 Fabio Valentini <decathorpe@gmail.com> - 2.0.3+git180513.001332.98c201b8-1
- Update to latest snapshot.

* Thu May 10 2018 Fabio Valentini <decathorpe@gmail.com> - 2.0.3+git180510.172313.e29bff95-1
- Update to latest snapshot.

* Tue May 08 2018 Fabio Valentini <decathorpe@gmail.com> - 2.0.3+git180507.160415.9ae24fdf-1
- Update to latest snapshot.

* Wed May 02 2018 Fabio Valentini <decathorpe@gmail.com> - 2.0.3+git180502.153729.63857308-1
- Update to latest snapshot.

* Tue Apr 10 2018 Fabio Valentini <decathorpe@gmail.com> - 2.0.3+git180409.231640.6aabb441-1
- Update to latest snapshot.

* Mon Apr 09 2018 Fabio Valentini <decathorpe@gmail.com> - 2.0.3+git180409.174655.52eb71be-1
- Update to latest snapshot.

* Sun Apr 08 2018 Fabio Valentini <decathorpe@gmail.com> - 2.0.3+git180408.095806.8985e839-1
- Update to latest snapshot.

* Thu Apr 05 2018 Fabio Valentini <decathorpe@gmail.com> - 2.0.3+git180405.210138.d2f40078-1
- Update to latest snapshot.

* Wed Apr 04 2018 Fabio Valentini <decathorpe@gmail.com> - 2.0.3+git180404.005820.ac21f7c4-1
- Adapt to CMake -> meson switch.

* Tue Apr 03 2018 Fabio Valentini <decathorpe@gmail.com> - 2.0.3+git180403.165341.2f380096-1
- Update to latest snapshot.

* Sun Mar 25 2018 Fabio Valentini <decathorpe@gmail.com> - 2.0.3+git180325.001123.4d476f5e-1
- Update to latest snapshot.

* Thu Mar 08 2018 Fabio Valentini <decathorpe@gmail.com> - 2.0.3+git180308.142216.e283df3d-1
- Update to latest snapshot.

* Tue Mar 06 2018 Fabio Valentini <decathorpe@gmail.com> - 2.0.3+git180306.173924.2185d263-1
- Update to latest snapshot.

* Wed Feb 14 2018 Fabio Valentini <decathorpe@gmail.com> - 2.0.3+git180213.234841.1d4a841d-1
- Update to latest snapshot.

* Tue Feb 13 2018 Fabio Valentini <decathorpe@gmail.com> - 2.0.3+git180213.024026.0a121f0e-1
- Update to latest snapshot.

* Fri Jan 05 2018 Fabio Valentini <decathorpe@gmail.com> - 2.0.3+git180103.001654.63c872fe-2
- Merge .spec file from fedora.

* Wed Jan 03 2018 Fabio Valentini <decathorpe@gmail.com> - 2.0.3+git180103.001654.63c872fe-1
- Update to latest snapshot.

* Wed Jan 03 2018 Fabio Valentini <decathorpe@gmail.com> - 2.0.3+git180103.000111.31365cbb-1
- Update to latest snapshot.

* Tue Dec 19 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0.3+git171219.060709.bacbd1c8-1
- Update to latest snapshot.

* Sat Aug 19 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0.3+git170818.222502.ca2c16ea-1
- Update to version 2.0.3.

* Sat Aug 19 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0.2+git170818.222502.ca2c16ea-1
- Update to latest snapshot.

* Sat Jul 15 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0.2+git170709.011937.5d7701e1-1
- Update to latest snapshot.

* Sun Jul 02 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0.2+git170702.101808.562f7a27-1
- Update to latest snapshot.

* Tue Jun 20 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0.2+git170620.155347.f064927a-1
- Update to latest snapshot.

* Sun Jun 18 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0.2+git170617.175639.e5aa1019-1
- Update to latest snapshot.

* Sun Jun 04 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0.2+git170604.161730.94afb215-1
- Update to latest snapshot.

* Tue May 23 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0.2+git170522.231337.8244c4c2-1
- Update to version 2.0.2.

* Tue May 23 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0+rev89-1
- Update to latest snapshot.

* Fri May 19 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0+rev88-1
- Update to latest snapshot.

* Wed May 17 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0+rev87-1
- Update to latest snapshot.

* Sun May 14 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0+rev86-1
- Update to latest snapshot.

* Wed May 03 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0+rev85-1
- Update to latest snapshot.

* Wed Apr 05 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0+rev82-1
- Update to latest snapshot.

* Tue Mar 21 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0+rev81-1
- Update to latest snapshot.

* Sun Mar 19 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0+rev80-1
- Update to latest snapshot.

* Wed Mar 15 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0+rev79-1
- Update to latest snapshot.

* Sat Feb 25 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0+rev78-1
- Update to latest snapshot.

* Fri Feb 10 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0+rev77-1
- Update to latest snapshot.

* Fri Feb 03 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0+rev76-1
- Update to latest snapshot.

* Sat Jan 28 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0+rev75-1
- Update to latest snapshot.

* Mon Jan 23 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0+rev74-1
- Update to latest snapshot.

* Sun Jan 22 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0+rev73-1
- Update to latest snapshot.

* Sat Jan 07 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0+rev72-1
- Update to version 2.0.

* Fri Jan 06 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0+rev71-1
- Update to version 2.0.

* Sat Dec 31 2016 Fabio Valentini <decathorpe@gmail.com> - 2.0+rev70-1
- Update to latest snapshot.

* Mon Dec 26 2016 Fabio Valentini <decathorpe@gmail.com> - 2.0+rev69-1
- Update to latest snapshot.

* Mon Dec 19 2016 Fabio Valentini <decathorpe@gmail.com> - 2.0+rev68-1
- Update to latest snapshot.

* Thu Dec 15 2016 Fabio Valentini <decathorpe@gmail.com> - 2.0+rev67-1
- Update to latest snapshot.

* Thu Sep 29 2016 Fabio Valentini <decathorpe@gmail.com> - 2.0+rev66-1
- Update to version 2.0.

* Thu Sep 29 2016 Fabio Valentini <decathorpe@gmail.com> - 2.0~rev66-2
- Spec file cleanups.

* Tue Aug 16 2016 Fabio Valentini <decathorpe@gmail.com> - 2.0~rev66-1
- Update to version 2.0.

* Sun Aug 14 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev65-1
- Update to latest snapshot.

* Fri Aug 12 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev63-1
- Update to latest snapshot.

* Mon Aug 08 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev62-1
- Update to latest snapshot.

* Sun Aug 07 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev61-2
- Update for packaging changes.

* Sun Aug 07 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev61-1
- Update to latest snapshot.

* Fri Aug 05 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev60-1
- Update to latest snapshot.

* Thu Aug 04 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev59-1
- Update to latest snapshot.

* Tue Aug 02 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev58-1
- Update to latest snapshot.

* Thu Jul 28 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev57-1
- Update to latest snapshot.

* Mon Jul 25 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev56-1
- Update to latest snapshot.

* Tue Jul 19 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev55-1
- Update to latest snapshot.

* Sun Jul 17 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev54-1
- Update to latest snapshot.

* Fri Jul 08 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev53-1
- Update to latest snapshot.

* Wed Jul 06 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev52-2
- Update for packaging changes.

* Sat Jun 18 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev48-1
- Update to latest snapshot.

* Wed Jun 15 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev47-1
- Update to latest snapshot.

* Tue Jun 14 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev46-1
- Update to latest snapshot.

* Wed Jun 08 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev45-1
- Update to latest snapshot.

* Tue Jun 07 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev43-1
- Update to latest snapshot.

* Thu Jun 02 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev42-1
- Update to latest snapshot.

* Wed Jun 01 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev41-1
- Update to latest snapshot.

* Mon May 30 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev40-3
- Update for packaging changes.

* Sun May 29 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev40-2
- Update for packaging changes.

* Thu May 26 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev40-1
- Update to latest snapshot.

* Wed May 25 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev39-1
- Update to latest snapshot.

* Tue May 24 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev37-1
- Update to latest snapshot.

* Wed May 11 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev36-2
- Update for packaging changes.

* Tue May 10 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev36-1
- Initial package.


