Summary:        Desktop-wide extension service
Name:           contractor
Version:        0.3.2+rev%{rev}
Release:        1%{?dist}
License:        GPLv3+
URL:            https://launchpad.net/contractor

Source0:        %{name}-%{version}.tar.gz
Source1:        %{name}.conf

BuildRequires:  cmake
BuildRequires:  gettext
BuildRequires:  vala
BuildRequires:  vala-tools

BuildRequires:  pkgconfig(gee-0.8)
BuildRequires:  pkgconfig(glib-2.0)

Requires:       dbus


%description
An extension service that allows apps to use the exposed functionality
of registered apps. This way, apps don't have to have the functions hard
coded into them.

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


%files
%{_bindir}/contractor

%{_datadir}/contractor/
%{_datadir}/dbus-1/services/org.elementary.contractor.service


%changelog
* Wed May 03 2017 Fabio Valentini <decathorpe@gmail.com> - 0.3.2+rev144-1
- Update to latest snapshot.

* Wed Apr 12 2017 Fabio Valentini <decathorpe@gmail.com> - 0.3.2+rev143-2
- Adapt to upstream changes.

* Tue Apr 11 2017 Fabio Valentini <decathorpe@gmail.com> - 0.3.2+rev143-1
- Update to latest snapshot.

* Sun Jan 29 2017 Fabio Valentini <decathorpe@gmail.com> - 0.3.2+rev141-2
- Sync with fedora packaging.

* Tue Jan 03 2017 Fabio Valentini <decathorpe@gmail.com> - 0.3.2+rev141-1
- Update to version 0.3.2.

* Tue Nov 01 2016 Fabio Valentini <decathorpe@gmail.com> - 0.3.2+rev140-2
- Contract directory is now included upstream.

* Tue Nov 01 2016 Fabio Valentini <decathorpe@gmail.com> - 0.3.2+rev140-1
- Update to latest snapshot.

* Thu Sep 29 2016 Fabio Valentini <decathorpe@gmail.com> - 0.3.2+rev139-1
- Update to version 0.3.2.

* Thu Sep 29 2016 Fabio Valentini <decathorpe@gmail.com> - 0.3.1~rev139-2
- Spec file cleanups.

* Thu Aug 11 2016 Fabio Valentini <decathorpe@gmail.com> - 0.3.1~rev139-1
- Update to latest snapshot.

* Sun Aug 07 2016 Fabio Valentini <decathorpe@gmail.com> - 0.3.1~rev138-5
- Update for packaging changes.

* Wed Jul 06 2016 Fabio Valentini <decathorpe@gmail.com> - 0.3.1~rev138-4
- Update for packaging changes.

* Mon May 30 2016 Fabio Valentini <decathorpe@gmail.com> - 0.3.1~rev138-3
- Update for packaging changes.

* Sun May 29 2016 Fabio Valentini <decathorpe@gmail.com> - 0.3.1~rev138-2
- Update for packaging changes.

* Wed May 04 2016 Fabio Valentini <decathorpe@gmail.com> - 0.3.1~rev138-1
- Update to latest snapshot.

* Sun Feb 21 2016 Fabio Valentini <decathorpe@gmail.com> - 0.3.1~rev138-1
- Update to new upstream snapshot.

* Mon Sep 21 2015 Fabio Valentini <decathorpe@gmail.com> - 0.3.1~rev137-1
- Update to new upstream snapshot.

* Fri Jul 24 2015 Fabio Valentini <decathorpe@gmail.com> - 0.3.1~rev136-3
- Fix build, oops ...

* Fri Jul 24 2015 Fabio Valentini <decathorpe@gmail.com> - 0.3.1~rev136-2
- Update spec file to use more macros.

* Sat Jul 18 2015 Fabio Valentini <decathorpe@gmail.com> - 0.3.1~rev136-1
- Initial package.


