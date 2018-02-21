%global __provides_exclude_from ^%{_libdir}/switchboard/.*\\.so$

Name:           switchboard-plug-sharing
Summary:        Switchboard Sharing Plug
Version:        0.1.1+git%{date}.%{commit}
Release:        1%{?dist}
License:        GPLv3

URL:            https://github.com/elementary/%{name}
Source0:        %{name}-%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  gettext
BuildRequires:  vala >= 0.22.0
BuildRequires:  vala-tools

BuildRequires:  pkgconfig(glib-2.0) >= 2.32
BuildRequires:  pkgconfig(granite)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(switchboard-2.0)

Requires:       switchboard%{?_isa}
Supplements:    switchboard%{?_isa}


%description
Configure the sharing of system services.

Designed for elementary OS.


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

%find_lang pantheon-sharing


%files -f pantheon-sharing.lang
%doc AUTHORS README.md
%license COPYING

%{_libdir}/switchboard/network/pantheon-sharing/


%changelog
* Wed Feb 21 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+git180221.124411.4dd5d8e7-1
- Update to latest snapshot.

* Wed Feb 21 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+git180221.003242.e054b612-1
- Update to latest snapshot.

* Sun Feb 18 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+git180218.110912.b491819f-1
- Update to latest snapshot.

* Sat Feb 17 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+git180217.101011.0f076a56-1
- Update to latest snapshot.

* Mon Feb 12 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+git180211.000921.1140debe-1
- Update to latest snapshot.

* Fri Jan 05 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+git180104.220308.dea75de7-2
- Merge .spec file from elementary-stable.

* Fri Jan 05 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+git180104.220308.dea75de7-1
- Update to latest snapshot.

* Fri Nov 17 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+git171117.184048.28864217-1
- Update to latest snapshot.

* Mon Sep 25 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+git170925.084846.589c0194-1
- Update to latest snapshot.

* Sat Sep 16 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+git170817.000750.706ab299-1
- Update to version 0.1.1.

* Sat Aug 19 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1+rev149-1
- Update to latest snapshot.

* Sun Jul 16 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1+rev148-1
- Update to latest snapshot.

* Sun Jul 02 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1+rev145-1
- Update to latest snapshot.

* Sat Jun 24 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1+rev143-1
- Update to latest snapshot.

* Sun Jun 18 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1+rev142-1
- Update to latest snapshot.

* Sat Jun 03 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1+rev141-1
- Update to latest snapshot.

* Wed May 03 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1+rev123-1
- Update to latest snapshot.

* Wed Apr 12 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1+rev122-1
- Update to latest snapshot.

* Sun Mar 26 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1+rev121-1
- Update to latest snapshot.

* Thu Feb 23 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1+rev120-1
- Update to latest snapshot.

* Sat Feb 18 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1+rev119-1
- Update to latest snapshot.

* Thu Feb 16 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1+rev118-1
- Update to latest snapshot.

* Wed Feb 15 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1+rev117-1
- Update to latest snapshot.

* Wed Feb 15 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1+rev116-1
- Update to latest snapshot.

* Fri Feb 10 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1+rev115-1
- Update to latest snapshot.

* Thu Feb 09 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1+rev114-1
- Update to latest snapshot.

* Tue Feb 07 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1+rev113-1
- Update to latest snapshot.

* Wed Jan 25 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1+rev112-1
- Update to latest snapshot.

* Mon Jan 23 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1+rev111-1
- Update to latest snapshot.

* Sat Jan 21 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1+rev110-1
- Update to latest snapshot.

* Sat Jan 07 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1+rev109-1
- Update to version 0.1.

* Fri Jan 06 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1+rev108-1
- Update to version 0.1.

* Tue Jan 03 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1+rev107-1
- Update to version 0.1.

* Mon Jan 02 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1+rev106-1
- Update to latest snapshot.

* Thu Dec 15 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1+rev105-1
- Update to latest snapshot.

* Wed Dec 14 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1+rev104-1
- Update to latest snapshot.

* Wed Dec 14 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1+rev103-1
- Update to latest snapshot.

* Wed Nov 23 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1+rev102-1
- Update to version 0.1.


