%global appname io.elementary.capnet-assist

Name:           elementary-capnet-assist
Summary:        Captive Portal Assistant for elementary
Version:        0.2.2+git%{date}.%{commit}
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
* Thu Jul 05 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.2+git180705.000702.6686dc59-1
- Update to latest snapshot.

* Wed Jul 04 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.2+git180703.190346.f1fbb7b4-1
- Update to latest snapshot.

* Thu Jun 14 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.2+git180613.000652.07fe8155-1
- Update to version 0.2.2.

