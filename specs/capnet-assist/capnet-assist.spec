Name:           capnet-assist
Summary:        Captive Portal Assistant for Pantheon
Version:        0.2.1+git%{date}.%{commit}
Release:        1%{?dist}
License:        GPLv3+

URL:            https://github.com/elementary/capnet-assist
Source0:        %{name}-%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  desktop-file-utils
BuildRequires:  gettext
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
mkdir build && pushd build
%cmake ..
%make_build
popd


%install
pushd build
%make_install
popd

%find_lang captive-login


%check
desktop-file-validate %{buildroot}/%{_datadir}/applications/io.elementary.capnet-assist.desktop


%files -f captive-login.lang
%license COPYING
%doc AUTHORS README.md

%{_bindir}/captive-login

%{_sysconfdir}/NetworkManager/dispatcher.d/90captive_portal_test

%{_datadir}/applications/io.elementary.capnet-assist.desktop
%{_datadir}/glib-2.0/schemas/io.elementary.capnet-assist.gschema.xml


%changelog
* Sun Jun 18 2017 Fabio Valentini <decathorpe@gmail.com> - 0.2.1+git170617.153400.177f0db7-1
- Update to latest snapshot.

* Sun Jun 11 2017 Fabio Valentini <decathorpe@gmail.com> - 0.2.1+git170611.162432.2f6acbe6-1
- Update to latest snapshot.

* Sun Apr 30 2017 Fabio Valentini <decathorpe@gmail.com> - 0.2.1+git170429.143603.d08b6b5e-1
- Update to latest snapshot.

* Sat Apr 29 2017 Fabio Valentini <decathorpe@gmail.com> - 0.2.1+git170422.003919.c20f8dcb-1
- Initial package.


