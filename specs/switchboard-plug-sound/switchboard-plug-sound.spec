%global __provides_exclude_from ^%{_libdir}/switchboard/.*\\.so$

Name:           switchboard-plug-sound
Summary:        Switchboard Sound Plug
Version:        0.1.1+git%{date}.%{commit}
Release:        1%{?dist}
License:        GPLv3

URL:            https://github.com/elementary/%{name}
Source0:        %{name}-%{version}.tar.gz

BuildRequires:  gettext
BuildRequires:  meson
BuildRequires:  vala >= 0.34.1
BuildRequires:  vala-tools

BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(granite)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(libcanberra)
BuildRequires:  pkgconfig(libcanberra-gtk)
BuildRequires:  pkgconfig(libpulse)
BuildRequires:  pkgconfig(libpulse-mainloop-glib)
BuildRequires:  pkgconfig(switchboard-2.0)

Requires:       switchboard%{?_isa}
Supplements:    switchboard%{?_isa}


%description
Switchboard Sound Plug.


%prep
%autosetup


%build
%meson
%meson_build


%install
%meson_install

%find_lang sound-plug


%files -f sound-plug.lang
%doc README.md
%license COPYING

%{_libdir}/switchboard/system/libsound.so


%changelog
* Wed Sep 26 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+git180926.122137.0dc8b778-1
- Update to latest snapshot.

* Thu Sep 06 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+git180906.043952.2cac046c-1
- Update to latest snapshot.

* Sat Sep 01 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+git180901.000919.97eb934f-1
- Update to latest snapshot.

* Fri Aug 31 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+git180831.131020.c0461580-1
- Update to latest snapshot.

* Wed Aug 29 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+git180829.162055.06766a65-1
- Update to latest snapshot.

* Wed Aug 29 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+git180829.155230.8a7b1da5-1
- Update to latest snapshot.

* Wed Aug 29 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+git180829.000401.a5bc5194-1
- Update to latest snapshot.

* Mon Aug 27 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+git180827.095359.aea90dd0-1
- Update to version 0.1.1.

* Mon Aug 27 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1+git180827.095359.aea90dd0-1
- Update to latest snapshot.

* Sat Aug 18 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1+git180818.142102.4007d53c-1
- Update to latest snapshot.

* Thu Aug 16 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1+git180813.000410.526dda2c-2
- Occasional mass rebuild.

* Mon Aug 13 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1+git180813.000410.526dda2c-1
- Update to latest snapshot.

* Fri Aug 03 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1+git180803.134847.df25aefc-1
- Update to latest snapshot.

* Tue Jul 24 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1+git180724.030908.fccebce3-1
- Update to latest snapshot.

* Sun Jul 22 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1+git180722.120536.fa991cb1-1
- Update to latest snapshot.

* Sun Jul 22 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1+git180722.000404.2bb84cd6-1
- Update to latest snapshot.

* Sat Jul 21 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1+git180721.123205.8ba69242-1
- Update to latest snapshot.

* Sat Jul 21 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1+git180721.000754.cc4314a2-1
- Update to latest snapshot.

* Wed Jul 18 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1+git180718.000648.920d1421-1
- Update to latest snapshot.

* Tue Jul 17 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1+git180716.203633.c10fada9-1
- Update to latest snapshot.

* Fri Jul 13 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1+git180713.181434.ea9546d8-1
- Update to latest snapshot.

* Fri Jul 13 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1+git180713.173146.56d05340-1
- Update to latest snapshot.

* Fri Jul 13 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1+git180713.014015.9e29fc96-1
- Update to latest snapshot.

* Thu Jul 12 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1+git180712.195533.901b506d-1
- Update to latest snapshot.

* Tue Jul 10 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1+git180709.201604.91862079-1
- Update to latest snapshot.

* Sun Jul 08 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1+git180708.000922.0d293216-1
- Update to latest snapshot.

* Wed Jul 04 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1+git180702.160226.a38c4fd2-1
- Update to latest snapshot.

* Mon Jun 11 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1+git180608.160923.c7ba44ec-1
- Update to version 0.1.

* Fri Jun 08 2018 Fabio Valentini <decathorpe@gmail.com> - 0+git180608.160923.c7ba44ec-1
- Update to latest snapshot.

* Sat Jun 02 2018 Fabio Valentini <decathorpe@gmail.com> - 0+git180602.195251.ac81eda0-1
- Update to latest snapshot.

* Thu May 31 2018 Fabio Valentini <decathorpe@gmail.com> - 0+git180531.122228.67969cbc-1
- Update to latest snapshot.

* Thu May 31 2018 Fabio Valentini <decathorpe@gmail.com> - 0+git180531.000347.fdce91a8-1
- Update to latest snapshot.

* Sun May 27 2018 Fabio Valentini <decathorpe@gmail.com> - 0+git180527.131815.3f67d041-1
- Update to latest snapshot.

* Thu May 24 2018 Fabio Valentini <decathorpe@gmail.com> - 0+git180521.000947.0958572d-1
- Update to latest snapshot.

* Thu May 17 2018 Fabio Valentini <decathorpe@gmail.com> - 0+git180517.000443.be5275f9-1
- Update to latest snapshot.

* Sat May 12 2018 Fabio Valentini <decathorpe@gmail.com> - 0+git180512.001228.5d7c648e-1
- Update to latest snapshot.

* Fri May 11 2018 Fabio Valentini <decathorpe@gmail.com> - 0+git180511.025616.ee1aa720-1
- Update to latest snapshot.

* Thu May 10 2018 Fabio Valentini <decathorpe@gmail.com> - 0+git180510.083614.97a6b4f6-1
- Update to latest snapshot.

* Tue May 08 2018 Fabio Valentini <decathorpe@gmail.com> - 0+git180508.132519.aba33e67-1
- Update to latest snapshot.

* Sun May 06 2018 Fabio Valentini <decathorpe@gmail.com> - 0+git180505.221011.bffd5fa6-1
- Update to latest snapshot.

* Thu May 03 2018 Fabio Valentini <decathorpe@gmail.com> - 0+git180503.143223.9e814dcb-1
- Update to latest snapshot.

* Tue Apr 10 2018 Fabio Valentini <decathorpe@gmail.com> - 0+git180410.173908.69bf56f7-1
- Update to latest snapshot.

* Tue Apr 03 2018 Fabio Valentini <decathorpe@gmail.com> - 0+git180331.212842.427a8c69-1
- Update to latest snapshot.

* Sun Mar 25 2018 Fabio Valentini <decathorpe@gmail.com> - 0+git180325.000948.19ada98d-1
- Update to latest snapshot.

* Thu Mar 08 2018 Fabio Valentini <decathorpe@gmail.com> - 0+git180308.162515.28fbfeae-1
- Update to latest snapshot.

* Sat Feb 24 2018 Fabio Valentini <decathorpe@gmail.com> - 0+git180224.000454.49f6ade1-2
- Adapt to cmake -> meson switch.

* Sat Feb 24 2018 Fabio Valentini <decathorpe@gmail.com> - 0+git180224.000454.49f6ade1-1
- Update to latest snapshot.

* Wed Feb 21 2018 Fabio Valentini <decathorpe@gmail.com> - 0+git180220.231707.86c178aa-1
- Update to latest snapshot.

* Mon Feb 12 2018 Fabio Valentini <decathorpe@gmail.com> - 0+git180211.000924.a1810189-1
- Update to latest snapshot.

* Fri Feb 09 2018 Fabio Valentini <decathorpe@gmail.com> - 0+git180209.001031.69ec18ae-1
- Update to latest snapshot.

* Mon Feb 05 2018 Fabio Valentini <decathorpe@gmail.com> - 0+git180205.001218.fb9e079b-1
- Update to latest snapshot.

* Sat Feb 03 2018 Fabio Valentini <decathorpe@gmail.com> - 0+git180203.114909.4016eb2f-1
- Update to latest snapshot.

* Fri Feb 02 2018 Fabio Valentini <decathorpe@gmail.com> - 0+git180202.201104.d9a903ec-1
- Update to latest snapshot.

* Sat Jan 27 2018 Fabio Valentini <decathorpe@gmail.com> - 0+git180104.001457.650fc7d0-1
- Update to latest snapshot.

* Fri Jan 05 2018 Fabio Valentini <decathorpe@gmail.com> - 0+git171104.070953.c277c501-2
- Clean up .spec file.

* Sat Nov 04 2017 Fabio Valentini <decathorpe@gmail.com> - 0+git171104.070953.c277c501-1
- Update to latest snapshot.

* Sat Oct 07 2017 Fabio Valentini <decathorpe@gmail.com> - 0+git171007.070521.3030e160-1
- Update to latest snapshot.

* Sat Aug 19 2017 Fabio Valentini <decathorpe@gmail.com> - 0+git170818.000142.91c5935f-1
- Update to latest snapshot.

* Sat Jul 15 2017 Fabio Valentini <decathorpe@gmail.com> - 0+git170715.154411.c206bbcd-1
- Update to latest snapshot.

* Wed Jul 05 2017 Fabio Valentini <decathorpe@gmail.com> - 0+git170702.102802.983900fc-1
- Initial package.


