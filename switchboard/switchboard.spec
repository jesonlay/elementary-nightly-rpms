%define rev 565

Summary: Switchboard System Settings
Name: switchboard
Version: 2.0.1~rev%{rev}
Release: 1%{?dist}
License: LGPLv2.1, LGPLv3
URL: http://launchpad.net/switchboard

Source0: %{name}-%{version}.tar.gz
Source1: %{name}.conf

BuildRequires: cmake pkgconfig
BuildRequires: vala gettext
BuildRequires: desktop-file-utils

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


%install
make install DESTDIR=$RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%{_libdir}/switchboard/system
mkdir -p $RPM_BUILD_ROOT/%{_libdir}/switchboard/personal
mkdir -p $RPM_BUILD_ROOT/%{_libdir}/switchboard/hardware

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
