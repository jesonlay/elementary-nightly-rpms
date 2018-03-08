%global __provides_exclude_from ^%{_libdir}/switchboard/.*\\.so$

Name:           switchboard-plug-about
Summary:        Switchboard System Information plug
Version:        0.2.4+git%{date}.%{commit}
Release:        1%{?dist}
License:        GPLv3+

URL:            https://github.com/elementary/%{name}
Source0:        %{name}-%{version}.tar.gz

# Use official logo in the system details view
Patch0:         00-fedora-logo.patch

BuildRequires:  gettext
BuildRequires:  meson
BuildRequires:  vala >= 0.22.0
BuildRequires:  vala-tools

BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(granite)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(switchboard-2.0)

Supplements:    switchboard%{?_isa}

Requires:       system-logos


%description
This switchboard plug shows system information.


%prep
%autosetup -p1


%build
%meson
%meson_build


%install
%meson_install

%find_lang about-plug


%files -f about-plug.lang
%doc README.md
%license COPYING

%{_libdir}/switchboard/hardware/libabout.so


%changelog
* Thu Mar 08 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.4+git180308.151649.c2a1a877-1
- Update to latest snapshot.

* Mon Mar 05 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.4+git180305.115050.a207098e-1
- Update to latest snapshot.

* Wed Feb 28 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.4+git180228.105809.51f68389-1
- Update to latest snapshot.

* Mon Feb 26 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.4+git180226.201759.559a1d2d-1
- Update to latest snapshot.

* Sun Feb 25 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.4+git180225.121246.4b751a9d-1
- Update to latest snapshot.

* Sun Feb 25 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.4+git180225.000927.ee1153eb-1
- Update to latest snapshot.

* Sat Feb 24 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.4+git180224.113435.5f0030c9-1
- Update to latest snapshot.

* Sat Feb 24 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.4+git180224.000412.12612fb3-1
- Update to latest snapshot.

* Fri Feb 23 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.4+git180223.184238.00d0a928-1
- Update to latest snapshot.

* Fri Feb 23 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.4+git180221.221857.fc251650-2
- Adapt to cmake -> meson switch.

* Thu Feb 22 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.4+git180221.221857.fc251650-1
- Update to latest snapshot.

* Wed Feb 21 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.4+git180221.144707.f2506d79-1
- Update to latest snapshot.

* Wed Feb 21 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.4+git180221.074327.6423fa39-1
- Update to latest snapshot.

* Tue Feb 20 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.4+git180220.212715.ae2f2225-1
- Update to latest snapshot.

* Sun Feb 18 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.4+git180218.110914.ffc3cd35-1
- Update to latest snapshot.

* Tue Feb 13 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.4+git180213.201203.eea5ebf6-1
- Update to latest snapshot.

* Mon Feb 05 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.4+git180205.001138.de9123ea-1
- Update to latest snapshot.

* Sat Jan 27 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.4+git180117.181133.6877ed0b-1
- Update to latest snapshot.

* Wed Jan 17 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.4+git180117.181130.1d19504f-1
- Update to latest snapshot.

* Mon Jan 15 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.4+git180114.114129.1c705944-2
- Adapt patch for upstream changes.

* Mon Jan 15 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.4+git180114.114129.1c705944-1
- Update to latest snapshot.

* Thu Jan 04 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.4+git170921.170550.974d3f19-2
- Merge .spec file from fedora.

* Fri Nov 10 2017 Fabio Valentini <decathorpe@gmail.com> - 0.2.4+git170921.170550.974d3f19-1
- Initial package.


