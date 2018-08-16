%global __provides_exclude_from ^%{_libdir}/wingpanel/.*\\.so$

Name:           wingpanel-indicator-ayatana
Summary:        an ayatana indicator for wingpanel
Version:        2.0.3+git%{date}.%{commit}
Release:        3%{?dist}
License:        GPLv3

URL:            https://github.com/elementary/%{name}
Source0:        %{name}-%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  gettext
BuildRequires:  vala >= 0.24.0
BuildRequires:  vala-tools

BuildRequires:  pkgconfig(glib-2.0) >= 2.32
BuildRequires:  pkgconfig(granite)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(indicator3-0.4)
BuildRequires:  pkgconfig(wingpanel-2.0)

Supplements:    wingpanel%{?_isa}


%description
An ayatana indicator for wingpanel.


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
%license COPYING

%{_libdir}/wingpanel/libayatana_compatibility.so


%changelog
* Thu Aug 16 2018 Fabio Valentini <decathorpe@gmail.com> - 2.0.3+git170703.192035.f324e542-3
- Occasional mass rebuild.

* Fri Jan 05 2018 Fabio Valentini <decathorpe@gmail.com> - 2.0.3+git170703.192035.f324e542-2
- Merge .spec file from fedora.

* Mon Jul 03 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0.3+git170703.192035.f324e542-1
- Update to latest snapshot.

* Sun Jun 18 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0.3+git170617.175152.6cbe7b53-1
- Update to latest snapshot.

* Sat May 27 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0.3+git170526.212756.8533b038-1
- Update to version 2.0.3.

* Sat May 27 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0.2+rev27-1
- Update to latest snapshot.

* Sat Apr 29 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0.2+rev26-1
- Update to latest snapshot.

* Thu Apr 27 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0.2+rev25-1
- Update to latest snapshot.

* Sun Mar 26 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0.2+rev23-1
- Update to latest snapshot.

* Sun Feb 05 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0.2+rev22-1
- Update to latest snapshot.

* Tue Oct 04 2016 Fabio Valentini <decathorpe@gmail.com> - 2.0.2+rev21-1
- Update to version 2.0.2.

* Tue Oct 04 2016 Fabio Valentini <decathorpe@gmail.com> - 2.0.1+rev21-1
- Update to latest snapshot.

* Thu Sep 29 2016 Fabio Valentini <decathorpe@gmail.com> - 2.0.1+rev20-1
- Update to version 2.0.1.


