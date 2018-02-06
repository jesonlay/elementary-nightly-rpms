%global appname io.elementary.capnet-assist

Name:           capnet-assist
Summary:        Captive Portal Assistant for Pantheon
Version:        0.2.1+git%{date}.%{commit}
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

%find_lang captive-login


%check
desktop-file-validate \
    %{buildroot}/%{_datadir}/applications/%{appname}.desktop


%files -f captive-login.lang
%license COPYING
%doc AUTHORS README.md

%{_bindir}/%{appname}

%{_sysconfdir}/NetworkManager/dispatcher.d/90captive_portal_test

%{_datadir}/applications/%{appname}.desktop
%{_datadir}/glib-2.0/schemas/%{appname}.gschema.xml


%changelog
* Tue Feb 06 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.1+git180206.201107.f2f49553-1
- Update to latest snapshot.

* Sat Feb 03 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.1+git180203.125329.16c44f28-1
- Update to latest snapshot.

* Tue Jan 30 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.1+git180130.172949.3f70c27e-1
- Update to latest snapshot.

* Sat Jan 27 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.1+git180127.212837.be680967-1
- Update to latest snapshot.

* Sun Dec 31 2017 Fabio Valentini <decathorpe@gmail.com> - 0.2.1+git171010.183301.bbfc271b-2
- Merge .spec file from fedora.

* Wed Oct 11 2017 Fabio Valentini <decathorpe@gmail.com> - 0.2.1+git171010.183301.bbfc271b-1
- Update to latest snapshot.

* Fri Oct 06 2017 Fabio Valentini <decathorpe@gmail.com> - 0.2.1+git171005.224736.1af6498b-1
- Update to latest snapshot.

* Thu Oct 05 2017 Fabio Valentini <decathorpe@gmail.com> - 0.2.1+git171004.215816.f65fa25b-2
- Adapt to upstream file changes.

* Thu Oct 05 2017 Fabio Valentini <decathorpe@gmail.com> - 0.2.1+git171004.215816.f65fa25b-1
- Update to latest snapshot.

* Wed Oct 04 2017 Fabio Valentini <decathorpe@gmail.com> - 0.2.1+git171004.145415.e103f237-1
- Update to latest snapshot.

* Wed Oct 04 2017 Fabio Valentini <decathorpe@gmail.com> - 0.2.1+git171002.200931.a25dfffc-2
- Switch build to meson.

* Tue Oct 03 2017 Fabio Valentini <decathorpe@gmail.com> - 0.2.1+git171002.200931.a25dfffc-1
- Update to latest snapshot.

* Mon Sep 25 2017 Fabio Valentini <decathorpe@gmail.com> - 0.2.1+git170925.140440.8a594453-1
- Update to latest snapshot.

* Mon Jul 03 2017 Fabio Valentini <decathorpe@gmail.com> - 0.2.1+git170703.164315.a30ac586-1
- Update to latest snapshot.

* Sun Jun 18 2017 Fabio Valentini <decathorpe@gmail.com> - 0.2.1+git170617.153400.177f0db7-1
- Update to latest snapshot.

* Sun Jun 11 2017 Fabio Valentini <decathorpe@gmail.com> - 0.2.1+git170611.162432.2f6acbe6-1
- Update to latest snapshot.

* Sun Apr 30 2017 Fabio Valentini <decathorpe@gmail.com> - 0.2.1+git170429.143603.d08b6b5e-1
- Update to latest snapshot.

* Sat Apr 29 2017 Fabio Valentini <decathorpe@gmail.com> - 0.2.1+git170422.003919.c20f8dcb-1
- Initial package.


