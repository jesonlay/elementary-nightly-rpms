%global __provides_exclude_from ^%{_libdir}/switchboard/.*\\.so$

%global plug_type hardware
%global plug_name mouse-touchpad

Name:           switchboard-plug-mouse-touchpad
Summary:        Switchboard Mouse and Touchpad plug
Version:        2.1.4+git%{date}.%{commit}
Release:        1%{?dist}
License:        GPLv3+

URL:            https://github.com/elementary/%{name}
Source0:        %{name}-%{version}.tar.gz

BuildRequires:  gettext
BuildRequires:  meson
BuildRequires:  vala >= 0.22.0

BuildRequires:  pkgconfig(glib-2.0) >= 2.32
BuildRequires:  pkgconfig(granite)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(switchboard-2.0)

Requires:       switchboard%{?_isa}
Supplements:    switchboard%{?_isa}


%description
A switchboard plug to configure the behavior of mice and touchpads.


%prep
%autosetup -p1


%build
%meson
%meson_build


%install
%meson_install

%find_lang %{plug_name}-plug


%files -f %{plug_name}-plug.lang
%doc README.md
%license COPYING

%{_libdir}/switchboard/%{plug_type}/lib%{plug_name}.so


%changelog
* Tue Nov 06 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.4+git181106.213609.a8a95816-1
- Update to latest snapshot.

* Tue Nov 06 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.4+git181105.234408.1945dc97-1
- Update to latest snapshot.

* Fri Nov 02 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.4+git181101.100739.a20ffcfd-2
- Occasional mass rebuild.

* Thu Nov 01 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.4+git181101.100739.a20ffcfd-1
- Update to latest snapshot.

* Mon Oct 29 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.4+git181029.030039.dfd6bed3-1
- Update to latest snapshot.

* Thu Oct 25 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.4+git181025.071553.29256cc0-1
- Update to latest snapshot.

* Wed Oct 24 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.4+git181024.221024.dfc7415d-1
- Update to latest snapshot.

* Wed Oct 24 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.4+git181023.231001.6227a39f-1
- Update to latest snapshot.

* Sun Oct 21 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.4+git181021.155448.ff1f583e-1
- Update to latest snapshot.

* Sat Oct 20 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.4+git181020.030025.eedf1335-1
- Update to latest snapshot.

* Fri Oct 19 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.4+git181018.203429.4833b591-1
- Update to version 2.1.4.

* Thu Oct 18 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.3+git181018.203429.4833b591-1
- Update to latest snapshot.

* Thu Oct 18 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.3+git181018.065828.cf654af9-1
- Update to latest snapshot.

* Wed Oct 17 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.3+git181017.000734.9e28d483-1
- Update to latest snapshot.

* Tue Oct 16 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.3+git181016.195140.11da7a7e-1
- Update to latest snapshot.

* Tue Oct 16 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.3+git181016.181206.ad511220-1
- Update to latest snapshot.

* Tue Oct 16 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.3+git181016.164105.74e7f54f-1
- Update to latest snapshot.

* Tue Oct 16 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.3+git181016.134314.108495af-1
- Update to latest snapshot.

* Tue Oct 16 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.3+git181016.124905.c0639f22-1
- Update to latest snapshot.

* Tue Oct 16 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.3+git181016.102857.c38366cb-1
- Update to latest snapshot.

* Tue Oct 16 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.3+git181016.091946.2e2a9a86-1
- Update to latest snapshot.

* Tue Oct 16 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.3+git181016.005750.c1a6699e-1
- Update to latest snapshot.

* Mon Oct 15 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.3+git181015.215110.cb4d0eef-1
- Update to latest snapshot.

* Sat Oct 13 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.3+git181013.220355.c24b0757-1
- Update to latest snapshot.

* Tue Oct 09 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.3+git181009.154142.2f8cb6eb-1
- Update to latest snapshot.

* Sun Oct 07 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.3+git181007.000955.618ca98a-1
- Update to latest snapshot.

* Sat Oct 06 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.3+git181006.034139.da18ba44-1
- Update to latest snapshot.

* Wed Sep 19 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.3+git180919.000922.84eb7078-1
- Update to latest snapshot.

* Thu Sep 06 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.3+git180906.043521.42e46854-1
- Update to latest snapshot.

* Sat Sep 01 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.3+git180901.000851.b00a4f06-1
- Update to latest snapshot.

* Wed Aug 29 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.3+git180829.162527.121f1e7d-1
- Update to latest snapshot.

* Mon Aug 27 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.3+git180825.000317.9860d543-1
- Update to latest snapshot.

* Thu Aug 23 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.3+git180823.185915.c54e7468-1
- Update to latest snapshot.

* Thu Aug 16 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.3+git180813.000347.07691471-2
- Occasional mass rebuild.

* Mon Aug 13 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.3+git180813.000347.07691471-1
- Update to latest snapshot.

* Sun Jul 22 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.3+git180722.120635.cec99ed1-1
- Update to latest snapshot.

* Sun Jul 22 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.3+git180722.000349.d1848581-1
- Update to latest snapshot.

* Wed Jul 18 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.3+git180718.000623.f614e4a7-1
- Update to latest snapshot.

* Tue Jul 10 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.3+git180709.205729.48586e39-1
- Update to latest snapshot.

* Wed Jul 04 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.3+git180702.000706.126b4b14-1
- Update to latest snapshot.

* Fri Jun 15 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.3+git180615.001109.c0b6fb68-1
- Update to latest snapshot.

* Thu Jun 14 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.3+git180614.000911.3ed8e375-1
- Update to latest snapshot.

* Wed Jun 13 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.3+git180613.000746.21967c73-1
- Update to latest snapshot.

* Sat Jun 09 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.3+git180609.125902.ce56e6f6-1
- Update to latest snapshot.

* Fri Jun 08 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.3+git180607.140200.b2574562-1
- Update to version 0.1.3.

* Thu Jun 07 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.2+git180607.140200.b2574562-1
- Update to latest snapshot.

* Mon Jun 04 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.2+git180604.000933.2aca6764-1
- Update to latest snapshot.

* Sun Jun 03 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.2+git180603.070506.5d272b74-1
- Update to latest snapshot.

* Fri Jun 01 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.2+git180601.000809.24ca3acc-1
- Update to latest snapshot.

* Thu May 31 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.2+git180531.000305.ece22c72-1
- Update to latest snapshot.

* Wed May 30 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.2+git180530.113541.37f98533-1
- Update to latest snapshot.

* Wed May 30 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.2+git180530.000409.86227ae0-1
- Update to latest snapshot.

* Mon May 28 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.2+git180527.190937.01a8ff68-1
- Update to latest snapshot.

* Sun May 27 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.2+git180527.000547.c54bd491-1
- Update to latest snapshot.

* Thu May 24 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.2+git180520.000458.bf48daa7-1
- Update to latest snapshot.

* Sat May 12 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.2+git180512.001155.20217fea-1
- Update to latest snapshot.

* Fri May 11 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.2+git180511.113739.a5c6e91c-1
- Update to latest snapshot.

* Fri May 11 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.2+git180511.000627.e356424b-1
- Update to latest snapshot.

* Tue May 08 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.2+git180508.171058.3de59574-1
- Update to latest snapshot.

* Mon May 07 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.2+git180507.000308.c324634d-1
- Update to latest snapshot.

* Sun May 06 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.2+git180504.000625.232072ac-1
- Update to latest snapshot.

* Tue May 01 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.2+git180501.165916.abcbe31e-1
- Update to latest snapshot.

* Tue May 01 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.2+git180429.115401.3372c970-1
- Update to latest snapshot.

* Thu Apr 26 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.2+git180426.000340.725807bc-1
- Update to latest snapshot.

* Wed Apr 25 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.2+git180425.103212.d5f14cf9-1
- Update to latest snapshot.

* Sat Apr 21 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.2+git180421.001127.a343f429-1
- Update to latest snapshot.

* Tue Apr 17 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.2+git180416.204812.d35b2931-1
- Update to latest snapshot.

* Sat Apr 14 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.2+git180414.123403.999c27b1-1
- Update to latest snapshot.

* Thu Apr 05 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.2+git180405.143536.1cd0a0c2-1
- Update to latest snapshot.

* Tue Apr 03 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.2+git180403.142515.2111a8d4-1
- Update to latest snapshot.

* Wed Mar 28 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.2+git180328.195954.b2b65ee1-1
- Update to latest snapshot.

* Tue Mar 27 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.2+git180327.000229.b0377d7f-1
- Update to latest snapshot.

* Mon Mar 26 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.2+git180326.102640.505e2e7c-2
- Adapt to CMake -> meson switch.

* Mon Mar 26 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.2+git180326.102640.505e2e7c-1
- Update to latest snapshot.

* Thu Mar 22 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.2+git180322.134135.567df840-1
- Update to latest snapshot.

* Thu Mar 15 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.2+git180314.231543.5157d3c5-1
- Update to latest snapshot.

* Fri Mar 09 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.2+git180309.000608.2eed8d9a-1
- Update to latest snapshot.

* Mon Mar 05 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.2+git180303.000250.89f4699c-1
- Update to latest snapshot.

* Sat Feb 24 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.2+git180218.191214.ff9b15dd-2
- Adapt patch to upstream changes.

* Sun Feb 18 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.2+git180218.191214.ff9b15dd-1
- Update to latest snapshot.

* Sat Feb 17 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.2+git180217.101024.fbbc5743-1
- Update to latest snapshot.

* Mon Feb 12 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.2+git180211.000850.8c6d0019-1
- Update to latest snapshot.

* Sat Jan 27 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.2+git180109.001810.bc910226-1
- Update to latest snapshot.

* Thu Jan 04 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.2+git171118.015919.d8633d55-2
- Merge .spec file from fedora.

* Sat Nov 18 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.2+git171118.015919.d8633d55-1
- Update to latest snapshot.

* Wed Nov 15 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.2+git171115.173431.25cff6b6-1
- Update to latest snapshot.

* Sun Nov 12 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.2+git171112.174349.189cbb64-1
- Update to latest snapshot.

* Mon Sep 25 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.2+git170925.083359.6fbb3e6d-1
- Update to latest snapshot.

* Sat Sep 16 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.2+git170707.025535.d81c25aa-1
- Update to version 0.1.2.

* Sun Jul 16 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.1.2+rev191-1
- Update to latest snapshot.

* Sun Jul 02 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.1.2+rev190-1
- Update to latest snapshot.

* Sun Jun 18 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.1.2+rev187-1
- Update to latest snapshot.

* Sat Jun 03 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.1.2+rev186-1
- Update to latest snapshot.

* Wed Apr 26 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.1.2+rev166-1
- Update to latest snapshot.

* Tue Apr 18 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.1.2+rev165-1
- Update to latest snapshot.

* Wed Apr 05 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.1.2+rev164-1
- Update to latest snapshot.

* Wed Mar 22 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.1.2+rev163-1
- Update to latest snapshot.

* Wed Mar 15 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.1.2+rev162-1
- Update to latest snapshot.

* Fri Mar 03 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.1.2+rev161-1
- Update to latest snapshot.

* Mon Feb 20 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.1.2+rev160-1
- Update to latest snapshot.

* Fri Feb 17 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.1.2+rev159-1
- Update to latest snapshot.

* Thu Feb 16 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.1.2+rev158-1
- Update to latest snapshot.

* Wed Feb 15 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.1.2+rev157-1
- Update to latest snapshot.

* Mon Feb 13 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.1.2+rev156-1
- Update to latest snapshot.

* Sun Feb 12 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.1.2+rev155-1
- Update to latest snapshot.

* Sat Feb 11 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.1.2+rev154-1
- Update to latest snapshot.

* Fri Feb 10 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.1.2+rev153-1
- Update to latest snapshot.

* Wed Feb 08 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.1.2+rev152-1
- Update to latest snapshot.

* Tue Feb 07 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.1.2+rev151-1
- Update to latest snapshot.

* Sun Jan 29 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.1.2+rev149-1
- Update to latest snapshot.

* Sat Jan 28 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.1.2+rev148-1
- Update to latest snapshot.

* Sat Jan 07 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.1.2+rev147-1
- Update to version 0.1.1.2.

* Fri Jan 06 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.1.2+rev146-1
- Update to version 0.1.1.2.

* Sun Jan 01 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.1.2+rev145-1
- Update to latest snapshot.

* Sat Dec 31 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.1.2+rev144-1
- Update to latest snapshot.

* Thu Dec 29 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.1.2+rev143-1
- Update to latest snapshot.

* Thu Dec 22 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.1.2+rev142-1
- Update to latest snapshot.

* Wed Dec 21 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.1.2+rev141-1
- Update to latest snapshot.

* Tue Dec 20 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.1.2+rev140-1
- Update to latest snapshot.

* Mon Dec 19 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.1.2+rev139-1
- Update to latest snapshot.

* Sun Dec 18 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.1.2+rev138-1
- Update to latest snapshot.

* Thu Dec 15 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.1.2+rev136-1
- Update to latest snapshot.

* Wed Dec 14 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.1.2+rev135-1
- Update to latest snapshot.

* Thu Dec 08 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.1.2+rev134-1
- Update to latest snapshot.

* Fri Dec 02 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.1.2+rev133-1
- Update to latest snapshot.

* Wed Nov 30 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.1.2+rev132-1
- Update to latest snapshot.

* Tue Nov 29 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.1.2+rev131-1
- Update to latest snapshot.

* Mon Nov 28 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.1.2+rev130-1
- Update to latest snapshot.

* Wed Nov 23 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.1.2+rev129-1
- Update to latest snapshot.

* Wed Nov 16 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.1.2+rev128-3
- Fix patch.

* Wed Nov 16 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.1.2+rev128-2
- Port patch to new upstream changes.

* Wed Nov 16 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.1.2+rev128-1
- Update to latest snapshot.

* Mon Nov 14 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.1.2+rev127-1
- Update to latest snapshot.

* Wed Nov 09 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.1.2+rev126-1
- Update to latest snapshot.

* Fri Nov 04 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.1.2+rev125-1
- Update to latest snapshot.

* Thu Nov 03 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.1.2+rev124-1
- Update to latest snapshot.

* Wed Nov 02 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.1.2+rev123-1
- Update to latest snapshot.

* Tue Nov 01 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.1.2+rev122-1
- Update to latest snapshot.

* Mon Oct 31 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.1.2+rev121-1
- Update to version 0.1.1.2.

* Wed Oct 26 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.1.1+rev118-2
- Adapt patch to upstream changes.

* Mon Oct 24 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.1.1+rev118-1
- Update to latest snapshot.

* Fri Oct 21 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.1.1+rev117-1
- Update to latest snapshot.

* Thu Oct 20 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.1.1+rev116-1
- Update to latest snapshot.

* Sun Oct 16 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.1.1+rev114-1
- Update to latest snapshot.

* Tue Oct 04 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.1.1+rev113-1
- Update to version 0.1.1.1.

* Sat Sep 17 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.1~rev113-1
- Update to latest snapshot.

* Fri Sep 16 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.1~rev112-1
- Update to latest snapshot.

* Fri Sep 16 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.1~rev110-1
- Update to latest snapshot.

* Thu Sep 15 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.1~rev107-1
- Update to latest snapshot.

* Sat Aug 20 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.1~rev97-4
- Update for packaging changes.

* Sat Aug 20 2016 Fabio Valentini <decathorpe@gmail.com>
- Fix applying patch.

* Sat Aug 20 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.1~rev97-3
- Update for packaging changes.

* Sat Aug 20 2016 Fabio Valentini <decathorpe@gmail.com>
- Fix applying patch.

* Sat Aug 20 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.1~rev97-2
- Update for packaging changes.

* Sun Aug 14 2016 Fabio Valentini <decathorpe@gmail.com>
- Add patch to fix SEGFAULT (wrong gsettings path).

* Sun Aug 14 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.1~rev97-1
- Update to latest snapshot.

* Fri Aug 12 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.1~rev96-1
- Update to latest snapshot.

* Thu Aug 11 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.1~rev95-1
- Update to latest snapshot.

* Wed Aug 10 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.1~rev94-1
- Update to latest snapshot.

* Mon Aug 08 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.1~rev93-1
- Update to latest snapshot.

* Sun Aug 07 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.1~rev92-2
- Update for packaging changes.

* Sun Aug 07 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.1~rev92-1
- Update to latest snapshot.

* Fri Aug 05 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.1~rev91-1
- Update to latest snapshot.

* Thu Aug 04 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.1~rev90-1
- Update to latest snapshot.

* Tue Aug 02 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.1~rev88-1
- Update to latest snapshot.

* Mon Aug 01 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.1~rev87-1
- Update to latest snapshot.

* Wed Jul 27 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.1~rev83-1
- Update to latest snapshot.

* Tue Jul 26 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.1~rev82-1
- Update to latest snapshot.

* Mon Jul 25 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.1~rev81-1
- Update to latest snapshot.

* Fri Jul 22 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.1~rev78-1
- Update to latest snapshot.

* Thu Jul 21 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.1~rev77-1
- Update to latest snapshot.

* Tue Jul 19 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.1~rev75-1
- Update to latest snapshot.

* Mon Jul 18 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.1~rev74-1
- Update to latest snapshot.

* Sun Jul 17 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.1~rev73-1
- Update to latest snapshot.

* Thu Jul 14 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.1~rev72-1
- Update to latest snapshot.

* Fri Jul 08 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.1~rev71-1
- Update to latest snapshot.

* Wed Jul 06 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.1~rev70-2
- Update for packaging changes.

* Tue Jun 21 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.1~rev65-1
- Update to latest snapshot.

* Mon Jun 20 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.1~rev64-1
- Update to latest snapshot.

* Sun Jun 19 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.1~rev63-1
- Update to latest snapshot.

* Sat Jun 18 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.1~rev60-1
- Update to latest snapshot.

* Sat Jun 18 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.1~rev59-1
- Update to latest snapshot.

* Fri Jun 17 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.1~rev58-1
- Update to latest snapshot.

* Tue Jun 14 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.1~rev57-1
- Update to latest snapshot.

* Mon May 30 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.1~rev56-4
- Update for packaging changes.

* Sun May 29 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.1~rev56-3
- Update for packaging changes.

* Fri May 13 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.1~rev56-2
- Update for packaging changes.

* Tue May 10 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev56-1
- Initial package.


