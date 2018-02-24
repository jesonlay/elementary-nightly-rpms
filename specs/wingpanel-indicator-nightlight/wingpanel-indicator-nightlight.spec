%global __provides_exclude_from ^%{_libdir}/wingpanel/.*\\.so$

Name:           wingpanel-indicator-nightlight
Summary:        Night Light Indicator for wingpanel
Version:        0+git%{date}.%{commit}
Release:        1%{?dist}
License:        GPLv2+

URL:            https://github.com/elementary/%{name}
Source0:        %{name}-%{version}.tar.gz

BuildRequires:  gettext
BuildRequires:  meson
BuildRequires:  vala >= 0.22.0
BuildRequires:  vala-tools

BuildRequires:  pkgconfig(glib-2.0) >= 2.32
BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  pkgconfig(granite)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(wingpanel-2.0)

Supplements:    wingpanel%{?_isa}


%description
A wingpanel indicator for Night Light.


%prep
%autosetup


%build
%meson
%meson_build


%install
%meson_install

%find_lang nightlight-indicator


%files -f nightlight-indicator.lang
%doc README.md
%license COPYING

%{_libdir}/wingpanel/libnightlight.so


%changelog
* Sat Feb 24 2018 Fabio Valentini <decathorpe@gmail.com> - 0+git180224.112225.4f7d7cca-1
- Update to latest snapshot.

* Sat Feb 24 2018 Fabio Valentini <decathorpe@gmail.com> - 0+git180224.074955.c01ac54f-1
- Update to latest snapshot.

* Wed Feb 21 2018 Fabio Valentini <decathorpe@gmail.com> - 0+git180221.011152.c52e4866-1
- Update to latest snapshot.

* Mon Feb 19 2018 Fabio Valentini <decathorpe@gmail.com> - 0+git180219.175435.c436f01d-1
- Update to latest snapshot.

* Mon Feb 19 2018 Fabio Valentini <decathorpe@gmail.com> - 0+git180219.123825.6a8eb84d-1
- Update to latest snapshot.

* Mon Feb 19 2018 Fabio Valentini <decathorpe@gmail.com> - 0+git180219.091152.931ce11f-1
- Update to latest snapshot.

* Sun Feb 18 2018 Fabio Valentini <decathorpe@gmail.com> - 0+git180218.213110.91421484-1
- Update to latest snapshot.

* Sun Feb 18 2018 Fabio Valentini <decathorpe@gmail.com> - 0+git180218.202425.d177a29f-1
- Update to latest snapshot.

* Mon Feb 12 2018 Fabio Valentini <decathorpe@gmail.com> - 0+git180211.001114.946ff0b4-1
- Update to latest snapshot.

* Fri Feb 02 2018 Fabio Valentini <decathorpe@gmail.com> - 0+git180202.195218.6b0d2e3b-1
- Update to latest snapshot.

* Tue Jan 23 2018 Fabio Valentini <decathorpe@gmail.com> - 0+git180123.175742.1f3f46b7-1
- Update to latest snapshot.

* Sun Jan 21 2018 Fabio Valentini <decathorpe@gmail.com> - 0+git180118.000409.8316cf51-1
- Update to latest snapshot.

* Tue Jan 09 2018 Fabio Valentini <decathorpe@gmail.com> - 0+git180109.214125.d8aa6add-1
- Update to latest snapshot.

* Tue Jan 09 2018 Fabio Valentini <decathorpe@gmail.com> - 0+git180109.002758.a4acf10d-1
- Update to latest snapshot.

* Mon Jan 08 2018 Fabio Valentini <decathorpe@gmail.com> - 0+git180108.194503.342f0cbf-1
- Update to latest snapshot.

* Fri Jan 05 2018 Fabio Valentini <decathorpe@gmail.com> - 0+git180105.004430.7398c3e6-1
- Initial package.


