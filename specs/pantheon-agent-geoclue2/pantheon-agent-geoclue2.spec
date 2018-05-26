Name:           pantheon-agent-geoclue2
Summary:        Pantheon Geoclue2 Agent
Version:        0+git%{date}.%{commit}
Release:        1%{?dist}
License:        GPLv3

URL:            https://github.com/elementary/pantheon-agent-geoclue2
Source0:        %{name}-%{version}.tar.gz
Source1:        %{name}.conf

BuildRequires:  cmake
BuildRequires:  cmake-elementary
BuildRequires:  desktop-file-utils
BuildRequires:  vala >= 0.34.1

BuildRequires:  pkgconfig(dbus-glib-1)
BuildRequires:  pkgconfig(gio-unix-2.0)
BuildRequires:  pkgconfig(glib-2.0) >= 2.32.0
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(libgeoclue-2.0)


%description
Provides a dialog asking for the user's permission when an application
requests access to location services.


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

%find_lang pantheon-agent-geoclue2


%check
desktop-file-validate %{buildroot}/%{_datadir}/applications/*.desktop


%files -f pantheon-agent-geoclue2.lang
%{_libexecdir}/geoclue2-1-pantheon/

%{_datadir}/applications/io.elementary.desktop.agent-geoclue2.desktop
%{_datadir}/glib-2.0/schemas/io.elementary.desktop.agent-geoclue2.gschema.xml


%changelog
* Sat May 26 2018 Fabio Valentini <decathorpe@gmail.com> - 0+git180526.080401.1effca6d-1
- Update to latest snapshot.

* Thu May 24 2018 Fabio Valentini <decathorpe@gmail.com> - 0+git180518.175450.80448d99-1
- Update to latest snapshot.

* Fri May 18 2018 Fabio Valentini <decathorpe@gmail.com> - 0+git180518.142130.a609cf74-1
- Update to latest snapshot.

* Thu May 10 2018 Fabio Valentini <decathorpe@gmail.com> - 0+git180510.171645.c7ccdabd-1
- Update to latest snapshot.

* Sun Mar 25 2018 Fabio Valentini <decathorpe@gmail.com> - 0+git180325.000904.261360f1-1
- Update to latest snapshot.

* Sat Mar 17 2018 Fabio Valentini <decathorpe@gmail.com> - 0+git180317.000928.5baec76b-1
- Update to latest snapshot.

* Sat Feb 24 2018 Fabio Valentini <decathorpe@gmail.com> - 0+git180223.205534.426e0234-1
- Update to latest snapshot.

* Mon Feb 12 2018 Fabio Valentini <decathorpe@gmail.com> - 0+git180211.000811.5414fb94-1
- Update to latest snapshot.

* Sat Feb 03 2018 Fabio Valentini <decathorpe@gmail.com> - 0+git180203.000627.a7e6cd15-1
- Update to latest snapshot.

* Fri Feb 02 2018 Fabio Valentini <decathorpe@gmail.com> - 0+git180202.194401.ebdc0e5e-1
- Update to latest snapshot.

* Sat Jan 06 2018 Fabio Valentini <decathorpe@gmail.com> - 0+git180106.001704.829369f3-1
- Update to latest snapshot.

* Fri Dec 29 2017 Fabio Valentini <decathorpe@gmail.com> - 0+git171228.234201.9e1e3292-1
- Update to latest snapshot.

* Tue Dec 19 2017 Fabio Valentini <decathorpe@gmail.com> - 0+git171219.084105.b7ddc262-1
- Update to latest snapshot.

* Fri Dec 15 2017 Fabio Valentini <decathorpe@gmail.com> - 0+git171215.001055.8aeda9bc-1
- Update to latest snapshot.

* Mon Jul 24 2017 Fabio Valentini <decathorpe@gmail.com> - 0+git170724.025352.c25fa8d9-1
- Update to latest snapshot.

* Sun Jul 02 2017 Fabio Valentini <decathorpe@gmail.com> - 0+git170702.101747.3f26f0c8-1
- Update to latest snapshot.

* Mon Jun 19 2017 Fabio Valentini <decathorpe@gmail.com> - 0+git170619.135343.c7cd564f-1
- Update to latest snapshot.

* Sun Jun 18 2017 Fabio Valentini <decathorpe@gmail.com> - 0+git170617.153024.106622e0-1
- Update to latest snapshot.

* Thu Jun 08 2017 Fabio Valentini <decathorpe@gmail.com> - 0+git170607.160948.6de1e776-1
- Update to latest snapshot.

* Thu Jun 01 2017 Fabio Valentini <decathorpe@gmail.com> - 0+git170531.215421.d2d45cf7-1
- Update to latest snapshot.

* Tue May 30 2017 Fabio Valentini <decathorpe@gmail.com> - 0+git170529.165431.35467052-2
- Adapt to upstream file changes.

* Mon May 29 2017 Fabio Valentini <decathorpe@gmail.com> - 0+git170529.165431.35467052-1
- Update to latest snapshot.

* Thu May 25 2017 Fabio Valentini <decathorpe@gmail.com> - 0+git170525.031021.b0ba8ce6-1
- Update to latest snapshot.

* Wed May 24 2017 Fabio Valentini <decathorpe@gmail.com> - 0+git170524.135009.054add6f-1
- Update to latest snapshot.

* Mon May 01 2017 Fabio Valentini <decathorpe@gmail.com> - 0+git170430.102728.b77d163f-2
- Adapt to upstream file changes.

* Sun Apr 30 2017 Fabio Valentini <decathorpe@gmail.com> - 0+git170430.102728.b77d163f-1
- Update to latest snapshot.

* Sat Apr 29 2017 Fabio Valentini <decathorpe@gmail.com> - 0+git170424.172841.1b407d1b-1
- Initial package.


