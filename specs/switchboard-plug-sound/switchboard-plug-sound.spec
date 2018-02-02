%global __provides_exclude_from ^%{_libdir}/switchboard/.*\\.so$

Name:           switchboard-plug-sound
Summary:        Switchboard Sound Plug
Version:        0+git%{date}.%{commit}
Release:        1%{?dist}
License:        GPLv3

URL:            https://github.com/elementary/%{name}
Source0:        %{name}-%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  gettext
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
mkdir build && pushd build
%cmake ..
%make_build
popd


%install
pushd build
%make_install
popd

%find_lang sound-plug


%files -f sound-plug.lang
%doc README.md
%license COPYING

%{_libdir}/switchboard/system/pantheon-sound/


%changelog
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


