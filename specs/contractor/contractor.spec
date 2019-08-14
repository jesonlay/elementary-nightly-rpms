Name:           contractor
Summary:        Desktop-wide extension service
Version:        0.3.4+git%{date}.%{commit}
Release:        1%{?dist}
License:        GPLv3+

URL:            https://github.com/elementary/%{name}
Source0:        %{name}-%{version}.tar.gz

BuildRequires:  gettext
BuildRequires:  meson
BuildRequires:  vala

BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  pkgconfig(gee-0.8)
BuildRequires:  pkgconfig(glib-2.0)

Requires:       dbus


%description
An extension service that allows apps to use the exposed functionality
of registered apps. This way, apps don't have to have the functions hard
coded into them.


%prep
%autosetup


%build
%meson
%meson_build


%install
%meson_install

# Create the the directory where other programs put their contracts
mkdir -p %{buildroot}/%{_datadir}/contractor


%files
%doc README.md
%license COPYING

%{_bindir}/contractor

%dir %{_datadir}/contractor
%{_datadir}/dbus-1/services/org.elementary.contractor.service


%changelog
* Wed Aug 14 2019 Fabio Valentini <decathorpe@gmail.com> - 0.3.4+git190814.131839.73372b49-1
- Update to latest snapshot.

* Thu Jan 24 2019 Fabio Valentini <decathorpe@gmail.com> - 0.3.4+git190124.125456.79d8168f-1
- Update to latest snapshot.

* Fri Nov 02 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.4+git181004.182005.250e4279-2
- Occasional mass rebuild.

* Thu Oct 04 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.4+git181004.182005.250e4279-1
- Update to latest snapshot.

* Thu Aug 16 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.4+git180802.144621.b0549607-2
- Occasional mass rebuild.

* Fri Aug 03 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.4+git180802.144621.b0549607-1
- Update to version 0.3.4.

* Thu Aug 02 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.3+git180802.144621.b0549607-1
- Update to latest snapshot.

* Sat May 26 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.3+git180524.211656.fe6f23e1-1
- Update to version 0.3.3.

* Sat May 26 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.2.99+git180524.211656.fe6f23e1-1
- Update to latest snapshot.

* Fri May 18 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.2.99+git180518.120340.d3178bce-1
- Update to latest snapshot.

* Fri Feb 02 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.2.99+git180202.085030.26e78a89-1
- Update to latest snapshot.

* Fri Jan 26 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.2.99+git180126.160520.1021e36a-1
- Update to latest snapshot.

* Tue Jan 16 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.2.99+git180116.191246.77e95066-1
- Update to latest snapshot.

* Sun Dec 31 2017 Fabio Valentini <decathorpe@gmail.com> - 0.3.2.99+git171118.235115.61083363-2
- Merge .spec file from fedora.

* Thu Nov 23 2017 Fabio Valentini <decathorpe@gmail.com> - 0.3.2.99+git171118.235115.61083363-1
- Switch to git snapshots.

* Mon Nov 20 2017 Fabio Valentini <decathorpe@gmail.com> - 0.3.2+rev149-1
- Update to latest snapshot.

* Sat Nov 18 2017 Fabio Valentini <decathorpe@gmail.com> - 0.3.2+rev148-1
- Update to latest snapshot.

* Tue Jul 04 2017 Fabio Valentini <decathorpe@gmail.com> - 0.3.2+rev147-1
- Update to latest snapshot.

* Sun Jun 18 2017 Fabio Valentini <decathorpe@gmail.com> - 0.3.2+rev146-1
- Update to latest snapshot.

* Sun Jun 11 2017 Fabio Valentini <decathorpe@gmail.com> - 0.3.2+rev145-1
- Update to latest snapshot.

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


