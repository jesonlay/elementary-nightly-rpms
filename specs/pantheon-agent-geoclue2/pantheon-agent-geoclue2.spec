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


