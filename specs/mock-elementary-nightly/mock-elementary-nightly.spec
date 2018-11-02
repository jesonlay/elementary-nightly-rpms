Name:           mock-elementary-nightly
Summary:        Configuration files for elementary-nightly mock builds
Version:        0+git%{date}.%{commit}
Release:        2%{?dist}
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
* Fri Nov 02 2018 Fabio Valentini <decathorpe@gmail.com> - 0+git180910.143404.9720fa88-2
- Occasional mass rebuild.

* Mon Sep 10 2018 Fabio Valentini <decathorpe@gmail.com> - 0+git180910.143404.9720fa88-1
- Update to latest snapshot.

* Thu Aug 16 2018 Fabio Valentini <decathorpe@gmail.com> - 0+git180507.132007.9b39eca3-2
- Occasional mass rebuild.

* Mon May 07 2018 Fabio Valentini <decathorpe@gmail.com> - 0+git180507.132007.9b39eca3-1
- Update to latest snapshot.

* Sun Sep 17 2017 Fabio Valentini <decathorpe@gmail.com> - 0+git170917.092344.5464ea09-1
- Initial package.

