%global appname io.elementary.capnet-assist

Name:           elementary-capnet-assist
Summary:        Captive Portal Assistant for elementary
Version:        2.2.1+git%{date}.%{commit}
Release:        1%{?dist}
License:        GPLv3+

URL:            https://github.com/elementary/%{name}
Source0:        %{name}-%{version}.tar.gz

BuildRequires:  desktop-file-utils
BuildRequires:  gettext
BuildRequires:  meson
BuildRequires:  vala >= 0.26

BuildRequires:  pkgconfig(gcr-3)
BuildRequires:  pkgconfig(gcr-ui-3)
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(granite) >= 0.3
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(webkit2gtk-4.0)

Requires:       NetworkManager

Provides:       capnet-assist = %{version}-%{release}
Obsoletes:      capnet-assist < 0.2.2-1


%description
Assists users in connective to Captive Portals such as those found on
public access points in train stations, coffee shops, universities,
etc.

Upon detection, the assistant appears showing the captive portal. Once
a connection is known to have been established, it dismisses itself.

Written in Vala and using WebkitGtk+.


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


%files -f %{appname}.lang
%license COPYING
%doc README.md

%{_bindir}/%{appname}

%{_sysconfdir}/NetworkManager/dispatcher.d/90captive_portal_test

%{_datadir}/applications/%{appname}.desktop
%{_datadir}/glib-2.0/schemas/%{appname}.gschema.xml


%changelog
* Fri Oct 05 2018 Fabio Valentini <decathorpe@gmail.com> - 2.2.1+git181005.101404.2e49e2c3-1
- Update to latest snapshot.

* Thu Oct 04 2018 Fabio Valentini <decathorpe@gmail.com> - 2.2.1+git181003.115905.7205fa27-1
- Update to version 2.2.1.

* Wed Oct 03 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.2+git181003.115905.7205fa27-1
- Update to latest snapshot.

* Fri Sep 21 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.2+git180921.000620.5646bc72-1
- Update to latest snapshot.

* Thu Sep 06 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.2+git180906.043026.3347dd93-1
- Update to latest snapshot.

* Fri Aug 31 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.2+git180831.000436.a4f98330-1
- Update to latest snapshot.

* Thu Aug 30 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.2+git180830.000651.13540736-1
- Update to latest snapshot.

* Wed Aug 29 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.2+git180829.060452.3c8c6314-1
- Update to latest snapshot.

* Tue Aug 28 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.2+git180828.183235.054c9384-1
- Update to latest snapshot.

* Mon Aug 27 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.2+git180826.000415.0c4d3146-1
- Update to latest snapshot.

* Wed Aug 22 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.2+git180822.000842.900373ea-1
- Update to latest snapshot.

* Sat Aug 18 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.2+git180818.124545.d5090432-1
- Update to latest snapshot.

* Thu Aug 16 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.2+git180812.120121.35c08eb5-2
- Occasional mass rebuild.

* Sun Aug 12 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.2+git180812.120121.35c08eb5-1
- Update to latest snapshot.

* Fri Jul 20 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.2+git180720.111411.552d4be2-1
- Update to latest snapshot.

* Wed Jul 18 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.2+git180718.000542.44abc781-1
- Update to latest snapshot.

* Tue Jul 17 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.2+git180716.214233.b869a547-1
- Update to latest snapshot.

* Tue Jul 10 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.2+git180710.000329.4e03e93d-1
- Update to latest snapshot.

* Mon Jul 09 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.2+git180709.200041.185cf071-1
- Update to latest snapshot.

* Sat Jul 07 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.2+git180705.000702.6686dc59-2
- Adapt to upstream file changes.

* Thu Jul 05 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.2+git180705.000702.6686dc59-1
- Update to latest snapshot.

* Wed Jul 04 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.2+git180703.190346.f1fbb7b4-1
- Update to latest snapshot.

* Thu Jun 14 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.2+git180613.000652.07fe8155-1
- Update to version 0.2.2.

