%global srcname     gsignond-plugin-oa

%global __provides_exclude_from ^%{_libdir}/gsignond/.*\\.so$

Name:           gsignond-plugin-oauth
Summary:        OAuth plugin for gsignond
Version:        0+git%{date}.%{commit}
Release:        1%{?dist}
License:        LGPLv2+

URL:            https://gitlab.com/accounts-sso/%{srcname}
Source0:        %{name}-%{version}.tar.gz

BuildRequires:  gtk-doc
BuildRequires:  meson

BuildRequires:  pkgconfig(check)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gnutls)
BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  pkgconfig(gsignond)
BuildRequires:  pkgconfig(json-glib-1.0)
BuildRequires:  pkgconfig(libsoup-2.4)


%description
This plugin for the Accounts-SSO gSignOn daemon handles the OAuth 1.0
and 2.0 authentication protocols.


%package        docs
Summary:        OAuth plugin for gsignond (documentation)
Requires:       %{name} = %{version}-%{release}
BuildArch:      noarch
%description    docs
This plugin for the Accounts-SSO gSignOn daemon handles the OAuth 1.0
and 2.0 authentication protocols.

This package contains the documentation.


%prep
%autosetup


%build
%meson
%meson_build


%install
%meson_install


%check
%meson_test


%files
%license COPYING.LIB
%doc README.md

%{_libdir}/gsignond/gplugins/liboauth.so

%files docs
%{_datadir}/gtk-doc/html/%{name}/


%changelog
* Sun May 13 2018 Fabio Valentini <decathorpe@gmail.com> - 0+git180513.133709.24c1c6da-1
- Update to latest snapshot.

* Sat Nov 11 2017 Fabio Valentini <decathorpe@gmail.com> - 0+git171111.202603.b36060b7-1
- Update to latest snapshot.

* Fri Nov 10 2017 Fabio Valentini <decathorpe@gmail.com> - 0+git171105.234149.787e8bc5-1
- Initial package.


