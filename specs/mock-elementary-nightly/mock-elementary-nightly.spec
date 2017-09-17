Name:           mock-elementary-nightly
Summary:        Configuration files for elementary-nightly mock builds
Version:        0+git%{date}.%{commit}
Release:        1%{?dist}
License:        Unlicense

URL:            https://github.com/decathorpe/mock-elementary-nightly
Source0:        %{name}-%{version}.tar.gz
Source1:        %{name}.conf

BuildArch:      noarch

BuildRequires:  coreutils

Requires:       mock


%description
This package contains configuration files that make it possible to build
packages against the decathorpe/elementary-nightly COPR repository locally.


%prep
%autosetup


%build


%install
mkdir -p %{buildroot}/%{_sysconfdir}/mock
cp -pav configs/* %{buildroot}/%{_sysconfdir}/mock/


%files
%config(noreplace) %{_sysconfdir}/mock/*.cfg


%changelog
* Sun Sep 17 2017 Fabio Valentini <decathorpe@gmail.com> - 0+git170917.092344.5464ea09-1
- Initial package.

