%global __provides_exclude_from ^%{_libdir}/wingpanel/.*\\.so$

Name:           wingpanel-indicator-keyboard
Summary:        Keyboard Indicator for wingpanel
Version:        2.0.2+git%{date}.%{commit}
Release:        1%{?dist}
License:        LGPLv2+

URL:            https://github.com/elementary/%{name}
Source0:        %{name}-%{version}.tar.gz

BuildRequires:  gettext
BuildRequires:  meson
BuildRequires:  vala >= 0.22.0
BuildRequires:  vala-tools

BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(granite)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(wingpanel-2.0)

Supplements:    wingpanel%{?_isa}


%description
A keyboard indicator for wingpanel.


%prep
%autosetup


%build
%meson
%meson_build


%install
%meson_install

%find_lang keyboard-indicator


%files -f keyboard-indicator.lang
%doc README.md
%license COPYING

%{_libdir}/wingpanel/libkeyboard.so


%changelog
* Tue May 29 2018 Fabio Valentini <decathorpe@gmail.com> - 2.0.2+git180528.170143.df3d7c12-1
- Update to latest snapshot.

* Sat May 26 2018 Fabio Valentini <decathorpe@gmail.com> - 2.0.2+git180525.202218.b2f96177-1
- Update to latest snapshot.

* Tue May 01 2018 Fabio Valentini <decathorpe@gmail.com> - 2.0.2+git180429.150007.d19c9e09-1
- Update to latest snapshot.

* Fri Apr 20 2018 Fabio Valentini <decathorpe@gmail.com> - 2.0.2+git180420.001410.eec71a81-1
- Update to latest snapshot.

* Tue Apr 17 2018 Fabio Valentini <decathorpe@gmail.com> - 2.0.2+git180416.204622.4659c771-1
- Update to latest snapshot.

* Sun Apr 15 2018 Fabio Valentini <decathorpe@gmail.com> - 2.0.2+git180414.230333.21a87456-1
- Update to latest snapshot.

* Wed Apr 04 2018 Fabio Valentini <decathorpe@gmail.com> - 2.0.2+git180329.233608.b294f018-2
- Adapt to CMake -> meson switch.

* Tue Apr 03 2018 Fabio Valentini <decathorpe@gmail.com> - 2.0.2+git180329.233608.b294f018-1
- Update to latest snapshot.

* Sun Mar 25 2018 Fabio Valentini <decathorpe@gmail.com> - 2.0.2+git180325.001127.094c7faf-1
- Update to latest snapshot.

* Tue Mar 20 2018 Fabio Valentini <decathorpe@gmail.com> - 2.0.2+git180320.001414.7bd892f9-1
- Update to latest snapshot.

* Sat Mar 10 2018 Fabio Valentini <decathorpe@gmail.com> - 2.0.2+git180310.000620.8d831baf-1
- Update to latest snapshot.

* Fri Mar 09 2018 Fabio Valentini <decathorpe@gmail.com> - 2.0.2+git180309.000755.514f0266-1
- Update to latest snapshot.

* Thu Feb 22 2018 Fabio Valentini <decathorpe@gmail.com> - 2.0.2+git180222.161116.69f3c609-1
- Update to latest snapshot.

* Sun Feb 18 2018 Fabio Valentini <decathorpe@gmail.com> - 2.0.2+git180218.201541.c53100df-1
- Update to latest snapshot.

* Tue Feb 13 2018 Fabio Valentini <decathorpe@gmail.com> - 2.0.2+git180213.200056.f6c7d51d-1
- Update to latest snapshot.

* Mon Feb 12 2018 Fabio Valentini <decathorpe@gmail.com> - 2.0.2+git180211.001110.638fdf84-1
- Update to latest snapshot.

* Fri Feb 09 2018 Fabio Valentini <decathorpe@gmail.com> - 2.0.2+git180209.001221.684cc672-1
- Update to latest snapshot.

* Tue Feb 06 2018 Fabio Valentini <decathorpe@gmail.com> - 2.0.2+git180206.202531.640306b1-1
- Update to latest snapshot.

* Mon Feb 05 2018 Fabio Valentini <decathorpe@gmail.com> - 2.0.2+git180205.001353.67e463cd-1
- Update to latest snapshot.

* Thu Jan 18 2018 Fabio Valentini <decathorpe@gmail.com> - 2.0.2+git180118.180122.d53c0da0-1
- Update to latest snapshot.

* Fri Jan 05 2018 Fabio Valentini <decathorpe@gmail.com> - 2.0.2+git180105.085319.1f52cbd4-2
- Merge .spec file from fedora.

* Fri Jan 05 2018 Fabio Valentini <decathorpe@gmail.com> - 2.0.2+git180105.085319.1f52cbd4-1
- Update to latest snapshot.

* Fri Jan 05 2018 Fabio Valentini <decathorpe@gmail.com> - 2.0.2+git180104.220732.a2805961-1
- Update to latest snapshot.

* Thu Dec 28 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0.2+git171228.215358.730bbbd3-1
- Update to latest snapshot.

* Wed Oct 11 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0.2+git171011.173150.0369cc30-1
- Update to latest snapshot.

* Wed Aug 30 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0.2+git170829.215012.2844c257-1
- Update to latest snapshot.

* Fri Jul 14 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0.2+git170709.024955.de992315-1
- Update to latest snapshot.

* Sun Jul 02 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0.2+git170702.180442.134f279f-1
- Update to latest snapshot.

* Sun Jun 18 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0.2+git170617.151454.cd4ba404-1
- Update to latest snapshot.

* Sun May 14 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0.2+git170514.131906.ef6139f9-1
- Update to latest snapshot.

* Tue May 09 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0.2+git170508.121656.f441632c-1
- Update to latest snapshot.

* Thu May 04 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0.2+git170503.171235.7e9d9ee8-1
- Update to version 2.0.2.

* Thu May 04 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0.1+rev87-1
- Update to latest snapshot.

* Wed May 03 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0.1+rev86-1
- Update to latest snapshot.

* Sat Apr 29 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0.1+rev85-1
- Update to latest snapshot.

* Thu Apr 27 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0.1+rev73-1
- Update to latest snapshot.

* Thu Apr 27 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0.1+rev72-1
- Update to latest snapshot.

* Wed Apr 05 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0.1+rev70-1
- Update to latest snapshot.

* Sat Mar 18 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0.1+rev69-1
- Update to latest snapshot.

* Wed Mar 15 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0.1+rev68-1
- Update to latest snapshot.

* Tue Mar 07 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0.1+rev67-1
- Update to latest snapshot.

* Tue Feb 28 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0.1+rev66-2
- Add BR: pkgconfig(libxml-2.0).

* Sun Feb 26 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0.1+rev66-1
- Update to latest snapshot.

* Wed Feb 08 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0.1+rev65-1
- Update to latest snapshot.

* Sat Jan 28 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0.1+rev64-1
- Update to latest snapshot.

* Sat Jan 07 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0.1+rev63-1
- Update to version 2.0.1.

* Fri Jan 06 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0.1+rev62-1
- Update to version 2.0.1.

* Sun Dec 18 2016 Fabio Valentini <decathorpe@gmail.com> - 2.0.1+rev61-1
- Update to latest snapshot.

* Sat Dec 17 2016 Fabio Valentini <decathorpe@gmail.com> - 2.0.1+rev60-1
- Update to latest snapshot.

* Fri Dec 16 2016 Fabio Valentini <decathorpe@gmail.com> - 2.0.1+rev59-1
- Update to latest snapshot.

* Thu Dec 08 2016 Fabio Valentini <decathorpe@gmail.com> - 2.0.1+rev58-1
- Update to latest snapshot.

* Fri Dec 02 2016 Fabio Valentini <decathorpe@gmail.com> - 2.0.1+rev57-1
- Update to latest snapshot.

* Wed Nov 23 2016 Fabio Valentini <decathorpe@gmail.com> - 2.0.1+rev56-1
- Update to version 2.0.1.


