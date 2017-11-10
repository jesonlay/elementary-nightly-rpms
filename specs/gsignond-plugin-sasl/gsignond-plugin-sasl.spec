%global __provides_exclude_from ^%{_libdir}/gsignond/.*\\.so$

Name:           gsignond-plugin-sasl
Summary:        SASL plugin for gsignond
Version:        0+git%{date}.%{commit}
Release:        1%{?dist}
License:        LGPLv2+

URL:            https://gitlab.com/accounts-sso/%{name}
Source0:        %{name}-%{version}.tar.gz

BuildRequires:  gtk-doc
BuildRequires:  meson

BuildRequires:  pkgconfig(check) >= 0.9.4
BuildRequires:  pkgconfig(glib-2.0) >= 2.30
BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  pkgconfig(gsignond)
BuildRequires:  pkgconfig(libgsasl)


%description
This plugin for the Accounts-SSO gSignOn daemon handles the SASL
authentication protocol.


%package        docs
Summary:        SASL plugin for gsignond (documentation)
Requires:       %{name} = %{version}-%{release}
BuildArch:      noarch
%description    docs
This plugin for the Accounts-SSO gSignOn daemon handles the SASL
authentication protocol.

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

%{_libdir}/gsignond/gplugins/libsasl.so

%files docs
%{_datadir}/gtk-doc/html/%{name}/*


%changelog
* Fri Nov 10 2017 Fabio Valentini <decathorpe@gmail.com> - 0+git171105.234017.bd611362-1
- Initial package.


