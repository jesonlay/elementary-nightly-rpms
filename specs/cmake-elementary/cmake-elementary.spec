Summary:        CMake modules for elementary
Name:           cmake-elementary
Version:        0+rev%{rev}
Release:        1%{?dist}
License:        GPLv3
URL:            https://code.launchpad.net/~elementary-os/+junk/cmake-modules

Source0:        %{name}-%{version}.tar.gz
Source1:        %{name}.conf

BuildRequires:  cmake
BuildRequires:  pkgconfig

Requires:       intltool

BuildArch:      noarch


%description
Most recent version of elementary's CMake modules.

Used across various projects.


%prep
%autosetup


%build
%cmake
%make_build


%install
%make_install


%files
%{_datadir}/cmake/Modules/*.cmake


%changelog
* Mon Apr 17 2017 Fabio Valentini <decathorpe@gmail.com> - 0+rev31-1
- Update to latest snapshot.

* Mon Apr 10 2017 Fabio Valentini <decathorpe@gmail.com> - 0+rev30-1
- Update to latest snapshot.

* Sat Apr 01 2017 Fabio Valentini <decathorpe@gmail.com> - 0+rev28-1
- Update to latest snapshot.

* Thu Sep 29 2016 Fabio Valentini <decathorpe@gmail.com> - 0+rev27-1
- Initial package.


