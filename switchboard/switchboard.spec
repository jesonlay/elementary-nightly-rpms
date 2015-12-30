%define rev 583

Summary: Switchboard System Settings
Name: switchboard
Version: 2.0.1~rev%{rev}
Release: 1%{?dist}
License: LGPLv2.1, LGPLv3
URL: http://launchpad.net/switchboard

Source0: %{name}-%{version}.tar.gz
Source1: %{name}.conf

BuildRequires: cmake
BuildRequires: gettext
BuildRequires: desktop-file-utils
BuildRequires: vala

BuildRequires: pkgconfig(cheese)
BuildRequires: pkgconfig(gee-0.8)
BuildRequires: pkgconfig(glib-2.0)
BuildRequires: pkgconfig(granite)
BuildRequires: pkgconfig(gtk+-3.0)


%description
Modular Desktop Settings Hub


%package devel
Summary: Modular Desktop Settings Hub development headers
%description devel
Modular Desktop Settings Hub. This package contains the development headers.


%prep
%setup -q


%build
%cmake -DUSE_UNITY=OFF
%make_build


%install
%make_install

mkdir -p $RPM_BUILD_ROOT/%{_libdir}/switchboard/hardware
mkdir -p $RPM_BUILD_ROOT/%{_libdir}/switchboard/network
mkdir -p $RPM_BUILD_ROOT/%{_libdir}/switchboard/personal
mkdir -p $RPM_BUILD_ROOT/%{_libdir}/switchboard/system

desktop-file-validate $RPM_BUILD_ROOT/%{_datadir}/applications/switchboard.desktop

%find_lang switchboard


%clean
rm -rf $RPM_BUILD_ROOT


%post
/sbin/ldconfig
/usr/bin/glib-compile-schemas %{_datadir}/glib-2.0/schemas &> /dev/null

%postun
/sbin/ldconfig
/usr/bin/glib-compile-schemas %{_datadir}/glib-2.0/schemas &> /dev/null


%post devel
/sbin/ldconfig

%postun devel
/sbin/ldconfig


%files -f switchboard.lang
%{_bindir}/switchboard
%{_libdir}/libswitchboard-2.0.so.0
%{_libdir}/libswitchboard-2.0.so.2.0

%{_libdir}/switchboard/

%{_datadir}/applications/switchboard.desktop
%{_datadir}/glib-2.0/schemas/org.pantheon.switchboard.gschema.xml


%files devel
%{_libdir}/libswitchboard-2.0.so
%{_libdir}/pkgconfig/switchboard-2.0.pc

%{_includedir}/switchboard-2.0/

%{_datadir}/vala/vapi/switchboard-2.0.deps
%{_datadir}/vala/vapi/switchboard-2.0.vapi


%changelog
* Wed Dec 30 2015 Fabio Valentini <decathorpe@gmail.com> - 2.0.1~rev583-1
- Update to new upstream snapshot.

* Tue Dec 29 2015 Fabio Valentini <decathorpe@gmail.com> - 2.0.1~rev582-1
- Update to new upstream snapshot.

* Mon Dec 07 2015 Fabio Valentini <decathorpe@gmail.com> - 2.0.1~rev581-1
- Update to new upstream snapshot.

* Sun Dec 06 2015 Fabio Valentini <decathorpe@gmail.com> - 2.0.1~rev580-1
- Update to new upstream snapshot.

* Wed Dec 02 2015 Fabio Valentini <decathorpe@gmail.com> - 2.0.1~rev577-1
- Update to new upstream snapshot.

* Thu Nov 26 2015 Fabio Valentini <decathorpe@gmail.com> - 2.0.1~rev576-1
- Update to new upstream snapshot.

* Tue Nov 24 2015 Fabio Valentini <decathorpe@gmail.com> - 2.0.1~rev575-1
- Update to new upstream snapshot.

* Tue Nov 17 2015 Fabio Valentini <decathorpe@gmail.com> - 2.0.1~rev574-1
- Update to new upstream snapshot.

* Sun Nov 15 2015 Fabio Valentini <decathorpe@gmail.com> - 2.0.1~rev573-1
- Update to new upstream snapshot.

* Thu Oct 22 2015 Fabio Valentini <decathorpe@gmail.com> - 2.0.1~rev572-1
- Update to new upstream snapshot.

* Wed Oct 21 2015 Fabio Valentini <decathorpe@gmail.com> - 2.0.1~rev571-1
- Update to new upstream snapshot.

* Thu Oct 15 2015 Fabio Valentini <decathorpe@gmail.com> - 2.0.1~rev570-1
- Update to new upstream snapshot.

* Wed Oct 14 2015 Fabio Valentini <decathorpe@gmail.com> - 2.0.1~rev569-1
- Update to new upstream snapshot.

* Sat Sep 26 2015 Fabio Valentini <decathorpe@gmail.com> - 2.0.1~rev568-1
- Update to new upstream snapshot.

* Wed Sep 23 2015 Fabio Valentini <decathorpe@gmail.com> - 2.0.1~rev567-1
- Update to new upstream snapshot.

* Fri Sep 04 2015 Fabio Valentini <decathorpe@gmail.com> - 2.0.1~rev566-3
- rebuild trigger for granite soname bump

* Thu Sep 03 2015 Fabio Valentini <decathorpe@gmail.com> - 2.0.1~rev566-2
- Release bump for granite soname change.

* Fri Aug 21 2015 Fabio Valentini <decathorpe@gmail.com> - 2.0.1~rev566-1
- Update to new bzr snapshot.

* Fri Aug 21 2015 Fabio Valentini <decathorpe@gmail.com> - 2.0.1~rev565-2
- Add network plug directory.
- Clean up spec file.

* Mon Aug 17 2015 Fabio Valentini - 2.0.1~rev565-1
- Update to new upstream snapshot.

* Mon Aug 17 2015 Fabio Valentini - 2.0.1~rev565-1
- Update to new upstream snapshot.

* Mon Jul 13 2015 Fabio Valentini <decathorpe@gmail.com> - 2.0.1~rev564-1
- Update to bzr snapshot revno 564.

* Sun Jul 05 2015 Fabio Valentini <decathorpe@gmail.com> - 2.0.1~rev563-2
- Add BR desktop-file-utils.

* Sun Jul 05 2015 Fabio Valentini <decathorpe@gmail.com> - 2.0.1~rev563-1
- Clean up spec file. Validate .desktop file. Update to new bzr snapshot.

* Sat Mar 07 2015 Fabio Valentini <decathorpe@gmail.com> - 2.0.0~rev545-10
- Update to latest bzr snapshot.

* Sun Feb 08 2015 Fabio Valentini <decathorpe@gmail.com> - 2.0.0~rev535-9
- Update to latest bzr snapshot.

* Mon Jan 05 2015 Fabio Valentini <fafatheone@gmail.com> - 2.0.0~rev534-8
- Fix upstream version.

* Sat Jan 03 2015 Fabio Valentini <fafatheone@gmail.com> - 2.0~rev534-7
- Cleaned up spec file.

* Wed Dec 31 2014 Fabio Valentini <fafatheone@gmail.com> - 2.0~rev534-6
- Include and own hardware plugs directory.

* Wed Dec 31 2014 Fabio Valentini <fafatheone@gmail.com> - 2.0~rev534-5
- Own personal plugs directory.

* Wed Dec 31 2014 Fabio Valentini <fafatheone@gmail.com> - 2.0~rev534-4
- Use pkgconfig BuildRequires.

* Wed Dec 31 2014 Fabio Valentini <fafatheone@gmail.com> - 2.0~rev534-3
- Own system plugs directory.

* Wed Dec 31 2014 Fabio Valentini <fafatheone@gmail.com> - 2.0~rev534-2
- Ship and own /usr/%{_lib}/switchboard/ directory.

* Wed Dec 31 2014 Fabio Valentini <fafatheone@gmail.com> - 2.0~rev534-1
- Initial package.
