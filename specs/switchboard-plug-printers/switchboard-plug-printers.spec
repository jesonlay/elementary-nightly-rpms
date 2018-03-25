%global __provides_exclude_from ^%{_libdir}/switchboard/.*\\.so$

Name:           switchboard-plug-printers
Summary:        Switchboard Printers Plug
Version:        0.1.2+git%{date}.%{commit}
Release:        1%{?dist}
License:        GPLv3+

URL:            https://github.com/elementary/%{name}
Source0:        %{name}-%{version}.tar.gz

BuildRequires:  gettext
BuildRequires:  meson
BuildRequires:  vala >= 0.22.0
BuildRequires:  vala-tools

BuildRequires:  cups-devel

BuildRequires:  pkgconfig(glib-2.0) >= 2.32
BuildRequires:  pkgconfig(granite)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(switchboard-2.0)

Requires:       cups%{?_isa}
Requires:       switchboard%{?_isa}

Supplements:    (switchboard%{?_isa} and cups%{?_isa})


%description
A printers plug for Switchboard.


%prep
%autosetup


%build
%meson
%meson_build


%install
%meson_install

%find_lang printers-plug


%files -f printers-plug.lang
%doc README.md
%license COPYING

%{_libdir}/switchboard/hardware/libprinters.so


%changelog
* Sun Mar 25 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.2+git180324.213819.8051a03e-1
- Update to latest snapshot.

* Thu Mar 22 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.2+git180322.000545.6eea6329-1
- Update to latest snapshot.

* Tue Mar 20 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.2+git180320.001209.a1a8cbe0-1
- Update to latest snapshot.

* Mon Mar 05 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.2+git180303.000258.9b0ae68c-1
- Update to latest snapshot.

* Mon Feb 26 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.2+git180226.213740.c6bbf92b-1
- Update to latest snapshot.

* Mon Feb 26 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.2+git180226.180349.22faadf0-1
- Update to latest snapshot.

* Mon Feb 26 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.2+git180226.000902.865e514d-1
- Update to latest snapshot.

* Sun Feb 25 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.2+git180225.000949.9ad87c0b-1
- Update to latest snapshot.

* Sat Feb 24 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.2+git180224.114556.59e0df0c-2
- Adapt to cmake -> meson switch.

* Sat Feb 24 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.2+git180224.114556.59e0df0c-1
- Update to latest snapshot.

* Sat Feb 24 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.2+git180224.000440.0e5c4c2d-1
- Update to latest snapshot.

* Fri Feb 23 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.2+git180223.184949.7a9f0150-1
- Update to latest snapshot.

* Fri Feb 23 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.2+git180223.000508.d045acc0-1
- Update to latest snapshot.

* Thu Feb 22 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.2+git180222.140827.ea172e85-1
- Update to latest snapshot.

* Thu Feb 22 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.2+git180222.011959.e45b63c5-1
- Update to latest snapshot.

* Wed Feb 21 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.2+git180221.004917.97a1fb6d-1
- Update to latest snapshot.

* Mon Feb 12 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.2+git180211.000907.271d4514-1
- Update to latest snapshot.

* Mon Feb 05 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.2+git180205.001159.0e9d981a-1
- Update to latest snapshot.

* Sat Feb 03 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.2+git180203.000657.280fe1ad-1
- Update to latest snapshot.

* Sat Jan 27 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.2+git180127.000726.7ee3abdc-1
- Update to latest snapshot.

* Fri Jan 05 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.2+git171218.230950.452845c5-2
- Merge .spec file from fedora.

* Tue Dec 19 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.2+git171218.230950.452845c5-1
- Update to latest snapshot.

* Mon Nov 20 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.2+git171118.235335.098c8981-1
- Update to latest snapshot.

* Fri Nov 17 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.2+git171117.184122.3de2fd73-1
- Update to latest snapshot.

* Tue Nov 14 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.2+git171113.183857.d60829b5-1
- Update to latest snapshot.

* Sun Nov 12 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.2+git171111.220215.5d1e6697-1
- Update to latest snapshot.

* Sun Oct 22 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.2+git171022.211713.f6c95c9b-1
- Update to latest snapshot.

* Sun Oct 22 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.2+git171021.121714.ac664dae-1
- Update to latest snapshot.

* Mon Oct 16 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.2+git171016.155512.1c469f83-1
- Update to version 0.1.2.

* Mon Oct 16 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+git171016.155512.1c469f83-1
- Update to latest snapshot.

* Fri Oct 13 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+git171012.222816.f534f9b8-1
- Update to latest snapshot.

* Thu Oct 12 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+git171012.195257.909dad0f-1
- Update to latest snapshot.

* Wed Oct 11 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+git171011.095554.cc0ba708-1
- Update to latest snapshot.

* Sat Aug 19 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+git170801.000335.d02e1add-1
- Update to latest snapshot.

* Sat Jul 15 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+git170715.161109.cc50385c-1
- Update to latest snapshot.

* Fri Jul 14 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+git170712.193634.298383d5-1
- Update to version 0.1.1.

* Wed Jul 12 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1+rev177-1
- Update to latest snapshot.

* Tue Jul 04 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1+rev173-1
- Update to latest snapshot.

* Sun Jun 18 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1+rev169-1
- Update to latest snapshot.

* Sat Jun 03 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1+rev168-1
- Update to latest snapshot.

* Sat Apr 29 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1+rev142-1
- Update to latest snapshot.

* Thu Apr 27 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1+rev141-1
- Update to latest snapshot.

* Sat Apr 15 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1+rev140-1
- Update to latest snapshot.

* Wed Apr 05 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1+rev139-1
- Update to latest snapshot.

* Sun Mar 19 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1+rev138-1
- Update to latest snapshot.

* Tue Mar 07 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1+rev137-1
- Update to latest snapshot.

* Mon Feb 27 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1+rev136-1
- Update to latest snapshot.

* Wed Feb 22 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1+rev134-1
- Update to latest snapshot.

* Mon Feb 20 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1+rev133-1
- Update to latest snapshot.

* Sat Feb 18 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1+rev132-1
- Update to latest snapshot.

* Wed Feb 15 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1+rev131-1
- Update to latest snapshot.

* Sun Feb 12 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1+rev130-1
- Update to latest snapshot.

* Sat Feb 11 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1+rev129-1
- Update to latest snapshot.

* Thu Feb 09 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1+rev128-1
- Update to latest snapshot.

* Sat Jan 28 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1+rev127-1
- Update to latest snapshot.

* Fri Jan 27 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1+rev126-1
- Update to latest snapshot.

* Thu Jan 26 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1+rev125-1
- Update to latest snapshot.

* Sat Jan 21 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1+rev124-1
- Update to latest snapshot.

* Mon Jan 09 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1+rev123-1
- Update to version 0.1.

* Sun Jan 08 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1+rev122-1
- Update to version 0.1.

* Fri Jan 06 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1+rev121-1
- Update to version 0.1.

* Tue Jan 03 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1+rev120-1
- Update to version 0.1.

* Mon Jan 02 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1+rev119-1
- Update to latest snapshot.

* Thu Dec 22 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1+rev118-1
- Update to latest snapshot.

* Wed Dec 14 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1+rev117-1
- Update to latest snapshot.

* Wed Nov 23 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1+rev116-1
- Update to version 0.1.


