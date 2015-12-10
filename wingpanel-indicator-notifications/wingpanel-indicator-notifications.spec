%define rev 65
%define debug_package %{nil}

Summary: A notifications indicator for wingpanel
Name: wingpanel-indicator-notifications
Version: 0.1~rev%{rev}
Release: 1%{?dist}
License: GPLv3
URL: http://launchpad.net/wingpanel-indicator-notifications

Source0: %{name}-%{version}.tar.gz
Source1: %{name}.conf

BuildRequires: cmake pkgconfig
BuildRequires: vala gettext

BuildRequires: pkgconfig(dbus-glib-1)
BuildRequires: pkgconfig(gdk-pixbuf-2.0)
BuildRequires: pkgconfig(gio-2.0)
BuildRequires: pkgconfig(granite)
BuildRequires: pkgconfig(libwnck-3.0)
BuildRequires: pkgconfig(wingpanel-2.0)


%description
A notifications indicator for wingpanel.


%prep
%setup -q


%build
%cmake
%make_build


%install
%make_install
%find_lang notifications-indicator


%clean
rm -rf $RPM_BUILD_ROOT


%post
/sbin/ldconfig
/usr/bin/glib-compile-schemas %{_datadir}/glib-2.0/schemas &> /dev/null


%postun
/sbin/ldconfig
/usr/bin/glib-compile-schemas %{_datadir}/glib-2.0/schemas &> /dev/null


%files -f notifications-indicator.lang
%{_libdir}/wingpanel/libnotifications-indicator.so


%changelog
* Wed Dec 09 2015 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev65-1
- Update to new upstream snapshot.

* Tue Dec 08 2015 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev64-1
- Update to new upstream snapshot.

* Mon Dec 07 2015 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev63-1
- Update to new upstream snapshot.

* Mon Nov 30 2015 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev62-1
- Update to new upstream snapshot.

* Thu Nov 26 2015 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev61-1
- Update to new upstream snapshot.

* Sat Nov 21 2015 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev60-1
- Update to new upstream snapshot.

* Thu Nov 19 2015 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev59-1
- Update to new upstream snapshot.

* Wed Nov 18 2015 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev58-1
- Update to new upstream snapshot.

* Tue Nov 17 2015 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev57-1
- Update to new upstream snapshot.

* Fri Nov 13 2015 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev55-1
- Update to new upstream snapshot.

* Thu Nov 05 2015 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev54-1
- Update to new upstream snapshot.

* Wed Nov 04 2015 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev53-1
- Update to new upstream snapshot.

* Mon Nov 02 2015 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev52-1
- Update to new upstream snapshot.

* Sat Oct 31 2015 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev51-1
- Update to new upstream snapshot.

* Wed Oct 28 2015 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev49-1
- Update to new upstream snapshot.

* Tue Oct 27 2015 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev48-2
- Fix language file names. Modernize spec.

* Mon Oct 26 2015 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev48-1
- Update to new upstream snapshot.

* Thu Oct 22 2015 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev47-2
- Remove gschema file.

* Thu Oct 22 2015 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev47-1
- Update to new upstream snapshot.

* Fri Oct 02 2015 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev46-1
- Update to new upstream snapshot.

* Thu Sep 24 2015 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev45-1
- Update to new upstream snapshot.

* Thu Sep 10 2015 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev43-2
- Release bump for wingpanel soname change.

* Fri Sep 04 2015 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev43-1
- rebuild trigger for granite soname bump

* Sun Aug 23 2015 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev43-1
- Update to new upstream snapshot.

* Fri Aug 21 2015 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev42-2
- Add BR:dbus-glib-1.

* Fri Aug 21 2015 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev42-1
- Update to new upstream snapshot.

* Mon Aug 17 2015 Fabio Valentini - 0.1~rev39-1
- Update to new upstream snapshot.

* Sat Aug 01 2015 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev38-1
- Update to bzr snapshot revno 38.

* Thu Jul 16 2015 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev36-1
- Update to bzr snapshot revno 36.

* Tue Jul 14 2015 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev35-1
- Initial package.


