%define rev 96

Summary: Stylish top panel that holds indicators and spawns an application launcher
Name: wingpanel
Version: 0.4.0~rev%{rev}
Release: 1%{?dist}
License: GPLv3
URL: http://launchpad.net/wingpanel

Source0: %{name}-%{version}.tar.gz
Source1: %{name}.conf

BuildRequires: cmake pkgconfig
BuildRequires: vala gettext

BuildRequires: desktop-file-utils

BuildRequires: pkgconfig(gala)
BuildRequires: pkgconfig(gee-0.8)
BuildRequires: pkgconfig(gio-2.0)
BuildRequires: pkgconfig(glib-2.0)
BuildRequires: pkgconfig(gmodule-2.0)
BuildRequires: pkgconfig(gobject-introspection-1.0)
BuildRequires: pkgconfig(granite)
BuildRequires: pkgconfig(gtk+-3.0) >= 3.14
BuildRequires: pkgconfig(libnotify)


%description
Wingpanel is the panel from the elementary project, used in its pantheon shell.


%package devel
Summary: Stylish top panel that holds indicators and spawns an application launcher
%description devel
Wingpanel is the panel from the elementary project, used in its pantheon shell. This package contains the development headers.


%prep
%setup -q


%build
%cmake


%install
make install DESTDIR=$RPM_BUILD_ROOT

desktop-file-validate $RPM_BUILD_ROOT/%{_datadir}/applications/wingpanel.desktop

mkdir -p $RPM_BUILD_ROOT/%{_libdir}/gala/plugins

mv $RPM_BUILD_ROOT/usr/lib/x86_64-linux-gnu/gala/plugins/libwingpanel-interface.so $RPM_BUILD_ROOT/%{_libdir}/gala/plugins/libwingpanel-interface.so

%ifarch x86_64
rm -rf $RPM_BUILD_ROOT/usr/lib
%endif

%find_lang wingpanel


%clean
rm -rf $RPM_BUILD_ROOT


%post
/sbin/ldconfig
/usr/bin/glib-compile-schemas %{_datarootdir}/glib-2.0/schemas &> /dev/null

%postun
/sbin/ldconfig
/usr/bin/glib-compile-schemas %{_datarootdir}/glib-2.0/schemas &> /dev/null


%files -f wingpanel.lang
%{_bindir}/wingpanel

%{_libdir}/libwingpanel-2.0.so.0
%{_libdir}/libwingpanel-2.0.so.0.2.0

%{_libdir}/gala/plugins/libwingpanel-interface.so

%{_datarootdir}/applications/wingpanel.desktop
%{_datarootdir}/glib-2.0/schemas/org.pantheon.desktop.wingpanel.gschema.xml


%files devel
%{_libdir}/libwingpanel-2.0.so
%{_libdir}/pkgconfig/wingpanel-2.0.pc

%{_includedir}/wingpanel-2.0

%{_datadir}/vala/vapi/wingpanel-2.0.deps
%{_datadir}/vala/vapi/wingpanel-2.0.vapi


%changelog
* Thu Dec 03 2015 Fabio Valentini <decathorpe@gmail.com> - 0.4.0~rev96-1
- Update to new upstream snapshot.

* Sun Sep 13 2015 Fabio Valentini <decathorpe@gmail.com> - 0.4.0~rev93-3
- Fix Build on non-x86_64 arch.

* Thu Sep 10 2015 Fabio Valentini <decathorpe@gmail.com> - 0.4.0~rev93-2
- Fix spec for soname change.

* Thu Sep 10 2015 Fabio Valentini <decathorpe@gmail.com> - 0.4~rev93-1
- Update to new upstream snapshot.

* Fri Sep 04 2015 Fabio Valentini <decathorpe@gmail.com> - 0.4~rev90-2
- rebuild trigger for granite soname bump

* Mon Aug 17 2015 Fabio Valentini - 0.4~rev90-1
- Update to new upstream snapshot.

* Tue Jul 14 2015 Fabio Valentini <decathorpe@gmail.com> - 0.4.0~rev86-1
- Update to bzr branch for 0.4, snapshot revno 86.

* Mon Jul 13 2015 Fabio Valentini <decathorpe@gmail.com> - 0.3.0.1~rev230-1
- Update to bzr snapshot revno 230.

* Wed Jul 08 2015 Fabio Valentini <decathorpe@gmail.com> - 0.3.0.1~rev229-1
- Update to bzr revno 229.

* Sat Mar 07 2015 Fabio Valentini <decathorpe@gmail.com> - 0.3~rev208-8
- Update to latest bzr snapshot.

* Sun Feb 01 2015 Fabio Valentini (fafa) <decathorpe@gmail.com> - 0.3~rev201-7
- Update to latest bzr snapshot.

* Fri Jan 23 2015 Fabio Valentini <decathorpe@gmail.com> - 0.3~rev200-6
- Update to latest bzr snapshot.

* Sun Jan 18 2015 Fabio Valentini <decathorpe@gmail.com> - 0.3~rev198-5
- Update to latest bzr snapshot.

* Tue Jan 13 2015 Fabio Valentini <fafatheone@gmail.com> - 0.3~rev196-4
- Update to latest bzr snapshot.

* Mon Jan 05 2015 Fabio Valentini <fafatheone@gmail.com> - 0.3~rev195-3
- Fix upstream version.

* Sat Jan 03 2015 Fabio Valentini <fafatheone@gmail.com> - 0.3.0~rev195-2
- Cleaned up spec file.

* Fri Jan 02 2015 Fabio Valentini <fafatheone@gmail.com> - 0.3.0~rev195-1
- Initial package.
