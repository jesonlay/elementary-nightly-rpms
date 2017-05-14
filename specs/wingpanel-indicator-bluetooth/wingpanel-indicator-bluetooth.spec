%global debug_package %{nil}

Summary:        a bluetooth indicator for wingpanel
Name:           wingpanel-indicator-bluetooth
Version:        2.0+rev%{rev}
Release:        1%{?dist}
License:        GPLv3
URL:            http://launchpad.net/wingpanel-indicator-bluetooth

Source0:        %{name}-%{version}.tar.gz
Source1:        %{name}.conf

BuildRequires:  cmake
BuildRequires:  gettext
BuildRequires:  pkgconfig
BuildRequires:  vala >= 0.22.0
BuildRequires:  vala-tools

BuildRequires:  pkgconfig(glib-2.0) >= 2.32
BuildRequires:  pkgconfig(granite)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(libnotify)
BuildRequires:  pkgconfig(wingpanel-2.0)


%description
a bluetooth indicator for wingpanel


%prep
%autosetup


%build
%cmake
%make_build


%install
%make_install
%find_lang bluetooth-indicator


%clean
rm -rf %{buildroot}


%files -f bluetooth-indicator.lang
%{_libdir}/wingpanel/libbluetooth.so

%{_datadir}/glib-2.0/schemas/org.pantheon.desktop.wingpanel.indicators.bluetooth.gschema.xml


%changelog
* Sun May 14 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0+rev86-1
- Update to latest snapshot.

* Wed May 03 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0+rev85-1
- Update to latest snapshot.

* Wed Apr 05 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0+rev82-1
- Update to latest snapshot.

* Tue Mar 21 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0+rev81-1
- Update to latest snapshot.

* Sun Mar 19 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0+rev80-1
- Update to latest snapshot.

* Wed Mar 15 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0+rev79-1
- Update to latest snapshot.

* Sat Feb 25 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0+rev78-1
- Update to latest snapshot.

* Fri Feb 10 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0+rev77-1
- Update to latest snapshot.

* Fri Feb 03 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0+rev76-1
- Update to latest snapshot.

* Sat Jan 28 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0+rev75-1
- Update to latest snapshot.

* Mon Jan 23 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0+rev74-1
- Update to latest snapshot.

* Sun Jan 22 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0+rev73-1
- Update to latest snapshot.

* Sat Jan 07 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0+rev72-1
- Update to version 2.0.

* Fri Jan 06 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0+rev71-1
- Update to version 2.0.

* Sat Dec 31 2016 Fabio Valentini <decathorpe@gmail.com> - 2.0+rev70-1
- Update to latest snapshot.

* Mon Dec 26 2016 Fabio Valentini <decathorpe@gmail.com> - 2.0+rev69-1
- Update to latest snapshot.

* Mon Dec 19 2016 Fabio Valentini <decathorpe@gmail.com> - 2.0+rev68-1
- Update to latest snapshot.

* Thu Dec 15 2016 Fabio Valentini <decathorpe@gmail.com> - 2.0+rev67-1
- Update to latest snapshot.

* Thu Sep 29 2016 Fabio Valentini <decathorpe@gmail.com> - 2.0+rev66-1
- Update to version 2.0.

* Thu Sep 29 2016 Fabio Valentini <decathorpe@gmail.com> - 2.0~rev66-2
- Spec file cleanups.

* Tue Aug 16 2016 Fabio Valentini <decathorpe@gmail.com> - 2.0~rev66-1
- Update to version 2.0.

* Sun Aug 14 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev65-1
- Update to latest snapshot.

* Fri Aug 12 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev63-1
- Update to latest snapshot.

* Mon Aug 08 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev62-1
- Update to latest snapshot.

* Sun Aug 07 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev61-2
- Update for packaging changes.

* Sun Aug 07 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev61-1
- Update to latest snapshot.

* Fri Aug 05 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev60-1
- Update to latest snapshot.

* Thu Aug 04 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev59-1
- Update to latest snapshot.

* Tue Aug 02 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev58-1
- Update to latest snapshot.

* Thu Jul 28 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev57-1
- Update to latest snapshot.

* Mon Jul 25 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev56-1
- Update to latest snapshot.

* Tue Jul 19 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev55-1
- Update to latest snapshot.

* Sun Jul 17 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev54-1
- Update to latest snapshot.

* Fri Jul 08 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev53-1
- Update to latest snapshot.

* Wed Jul 06 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev52-2
- Update for packaging changes.

* Sat Jun 18 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev48-1
- Update to latest snapshot.

* Wed Jun 15 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev47-1
- Update to latest snapshot.

* Tue Jun 14 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev46-1
- Update to latest snapshot.

* Wed Jun 08 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev45-1
- Update to latest snapshot.

* Tue Jun 07 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev43-1
- Update to latest snapshot.

* Thu Jun 02 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev42-1
- Update to latest snapshot.

* Wed Jun 01 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev41-1
- Update to latest snapshot.

* Mon May 30 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev40-3
- Update for packaging changes.

* Sun May 29 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev40-2
- Update for packaging changes.

* Thu May 26 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev40-1
- Update to latest snapshot.

* Wed May 25 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev39-1
- Update to latest snapshot.

* Tue May 24 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev37-1
- Update to latest snapshot.

* Wed May 11 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev36-2
- Update for packaging changes.

* Tue May 10 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev36-1
- Initial package.


