Name:           cmake-elementary
Summary:        CMake modules shared by elementary projects
Version:        0.1.0+git%{date}.%{commit}
Release:        1%{?dist}
License:        GPLv3

URL:            https://github.com/elementary/cmake-modules
Source0:        %{name}-%{version}.tar.gz


BuildRequires:  cmake

Requires:       cmake
Requires:       intltool
Requires:       pkgconfig

BuildArch:      noarch


%description
Most recent version of elementary's CMake modules.

Used across various projects.


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


%files
%doc README.md

%{_datadir}/cmake/Modules/*.cmake


%changelog
* Mon May 28 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.0+git180527.224703.8d39e503-1
- Update to latest snapshot.

* Sun Dec 31 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.0+git171229.154934.319ec533-2
- Merge .spec file from fedora.

* Fri Dec 29 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.0+git171229.154934.319ec533-1
- Update to latest snapshot.

* Sat Sep 16 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.0+git170726.221107.f8d0d309-1
- Update to version 0.1.0.

* Mon Apr 17 2017 Fabio Valentini <decathorpe@gmail.com> - 0+rev31-1
- Update to latest snapshot.

* Mon Apr 10 2017 Fabio Valentini <decathorpe@gmail.com> - 0+rev30-1
- Update to latest snapshot.

* Sat Apr 01 2017 Fabio Valentini <decathorpe@gmail.com> - 0+rev28-1
- Update to latest snapshot.

* Thu Sep 29 2016 Fabio Valentini <decathorpe@gmail.com> - 0+rev27-1
- Initial package.


