%global debug_package %{nil}

Summary:        a network indicator for wingpanel
Name:           wingpanel-indicator-network
Version:        2.0.2+rev%{rev}
Release:        1%{?dist}
License:        GPLv3
URL:            http://launchpad.net/wingpanel-indicator-network

Source0:        %{name}-%{version}.tar.gz
Source1:        %{name}.conf

BuildRequires:  cmake
BuildRequires:  gettext
BuildRequires:  pkgconfig
BuildRequires:  vala >= 0.22.0
BuildRequires:  vala-tools

BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(granite)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(libnm-glib)
BuildRequires:  pkgconfig(libnm-gtk)
BuildRequires:  pkgconfig(libnm-util)
BuildRequires:  pkgconfig(wingpanel-2.0)


%description
a network indicator for wingpanel


%prep
%autosetup


%build
%cmake
%make_build


%install
%make_install
%find_lang network-indicator


%clean
rm -rf %{buildroot}


%files -f network-indicator.lang
%{_libdir}/wingpanel/libnetwork.so

%{_datadir}/glib-2.0/schemas/org.pantheon.desktop.wingpanel.indicators.network.gschema.xml


%changelog
* Sun Mar 19 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0.2+rev228-1
- Update to latest snapshot.

* Wed Mar 15 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0.2+rev227-1
- Update to latest snapshot.

* Wed Mar 08 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0.2+rev226-1
- Update to latest snapshot.

* Sun Mar 05 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0.2+rev225-1
- Update to latest snapshot.

* Sat Feb 25 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0.2+rev224-1
- Update to latest snapshot.

* Sun Feb 19 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0.2+rev223-1
- Update to latest snapshot.

* Sat Feb 18 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0.2+rev222-1
- Update to latest snapshot.

* Tue Feb 14 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0.2+rev221-1
- Update to latest snapshot.

* Sat Feb 11 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0.2+rev220-1
- Update to latest snapshot.

* Thu Feb 09 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0.2+rev219-1
- Update to latest snapshot.

* Wed Feb 08 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0.2+rev218-1
- Update to latest snapshot.

* Sat Jan 28 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0.2+rev217-1
- Update to latest snapshot.

* Fri Jan 27 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0.2+rev216-1
- Update to latest snapshot.

* Tue Jan 24 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0.2+rev215-1
- Update to latest snapshot.

* Mon Jan 23 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0.2+rev214-1
- Update to latest snapshot.

* Sat Jan 07 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0.2+rev213-1
- Update to version 2.0.2.

* Tue Jan 03 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0.2+rev212-1
- Update to version 2.0.2.

* Tue Jan 03 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0.1+rev212-1
- Update to version 2.0.1.

* Mon Jan 02 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0.1+rev211-1
- Update to latest snapshot.

* Sun Jan 01 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0.1+rev210-1
- Update to latest snapshot.

* Tue Dec 20 2016 Fabio Valentini <decathorpe@gmail.com> - 2.0.1+rev209-1
- Update to latest snapshot.

* Mon Dec 19 2016 Fabio Valentini <decathorpe@gmail.com> - 2.0.1+rev208-1
- Update to latest snapshot.

* Fri Dec 09 2016 Fabio Valentini <decathorpe@gmail.com> - 2.0.1+rev207-1
- Update to latest snapshot.

* Tue Nov 29 2016 Fabio Valentini <decathorpe@gmail.com> - 2.0.1+rev206-1
- Update to latest snapshot.

* Mon Nov 21 2016 Fabio Valentini <decathorpe@gmail.com> - 2.0.1+rev205-1
- Update to latest snapshot.

* Sun Nov 20 2016 Fabio Valentini <decathorpe@gmail.com> - 2.0.1+rev204-1
- Update to latest snapshot.

* Sat Nov 19 2016 Fabio Valentini <decathorpe@gmail.com> - 2.0.1+rev203-1
- Update to latest snapshot.

* Sat Nov 19 2016 Fabio Valentini <decathorpe@gmail.com> - 2.0.1+rev202-1
- Update to latest snapshot.

* Wed Nov 16 2016 Fabio Valentini <decathorpe@gmail.com> - 2.0.1+rev201-1
- Update to latest snapshot.

* Fri Nov 11 2016 Fabio Valentini <decathorpe@gmail.com> - 2.0.1+rev200-1
- Update to latest snapshot.

* Fri Nov 04 2016 Fabio Valentini <decathorpe@gmail.com> - 2.0.1+rev199-1
- Update to latest snapshot.

* Fri Nov 04 2016 Fabio Valentini <decathorpe@gmail.com> - 2.0.1+rev198-1
- Update to latest snapshot.

* Thu Nov 03 2016 Fabio Valentini <decathorpe@gmail.com> - 2.0.1+rev197-1
- Update to latest snapshot.

* Thu Nov 03 2016 Fabio Valentini <decathorpe@gmail.com> - 2.0.1+rev196-1
- Update to latest snapshot.

* Sun Oct 16 2016 Fabio Valentini <decathorpe@gmail.com> - 2.0.1+rev195-1
- Update to latest snapshot.

* Sat Oct 08 2016 Fabio Valentini <decathorpe@gmail.com> - 2.0.1+rev194-1
- Update to latest snapshot.

* Thu Sep 29 2016 Fabio Valentini <decathorpe@gmail.com> - 2.0.1+rev193-1
- Update to version 2.0.1.

* Thu Sep 29 2016 Fabio Valentini <decathorpe@gmail.com> - 2.0.1~rev193-2
- Spec file cleanups.

* Fri Sep 16 2016 Fabio Valentini <decathorpe@gmail.com> - 2.0.1~rev193-1
- Update to version 2.0.1.

* Fri Sep 09 2016 Fabio Valentini <decathorpe@gmail.com> - 2.0~rev192-1
- Update to latest snapshot.

* Thu Aug 18 2016 Fabio Valentini <decathorpe@gmail.com> - 2.0~rev190-1
- Update to version 2.0.

* Sun Aug 14 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev189-1
- Update to latest snapshot.

* Fri Aug 12 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev188-1
- Update to latest snapshot.

* Thu Aug 11 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev187-1
- Update to latest snapshot.

* Mon Aug 08 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev186-1
- Update to latest snapshot.

* Sun Aug 07 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev185-2
- Update for packaging changes.

* Sun Aug 07 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev185-1
- Update to latest snapshot.

* Sat Aug 06 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev184-1
- Update to latest snapshot.

* Fri Aug 05 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev183-1
- Update to latest snapshot.

* Thu Aug 04 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev182-1
- Update to latest snapshot.

* Tue Aug 02 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev180-1
- Update to latest snapshot.

* Fri Jul 29 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev179-1
- Update to latest snapshot.

* Mon Jul 25 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev178-1
- Update to latest snapshot.

* Mon Jul 25 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev177-1
- Update to latest snapshot.

* Thu Jul 21 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev176-1
- Update to latest snapshot.

* Mon Jul 11 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev175-1
- Update to latest snapshot.

* Wed Jul 06 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev174-2
- Update for packaging changes.

* Wed Jul 06 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev174-1
- Update to latest snapshot.

* Mon Jul 04 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev173-1
- Update to latest snapshot.

* Sun Jul 03 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev172-1
- Update to latest snapshot.

* Sat Jul 02 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev171-1
- Update to latest snapshot.

* Fri Jul 01 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev170-1
- Update to latest snapshot.

* Tue Jun 28 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev169-1
- Update to latest snapshot.

* Thu Jun 23 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev168-1
- Update to latest snapshot.

* Tue Jun 21 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev167-1
- Update to latest snapshot.

* Mon Jun 20 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev166-1
- Update to latest snapshot.

* Sat Jun 18 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev165-1
- Update to latest snapshot.

* Fri Jun 17 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev164-1
- Update to latest snapshot.

* Tue Jun 14 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev163-1
- Update to latest snapshot.

* Sat Jun 11 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev162-1
- Update to latest snapshot.

* Sat Jun 04 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev161-1
- Update to latest snapshot.

* Mon May 30 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev160-3
- Update for packaging changes.

* Sun May 29 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev160-2
- Update for packaging changes.

* Sat May 28 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev160-1
- Update to latest snapshot.

* Thu May 12 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev159-1
- Update to latest snapshot.

* Tue May 10 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev158-2
- Update for packaging changes.

* Tue May 10 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev158-1
- Initial package.


