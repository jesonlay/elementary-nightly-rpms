%define rev 69
%define debug_package %{nil}

Summary: A sound indicator for wingpanel
Name: wingpanel-indicator-sound
Version: 0.1~rev%{rev}
Release: 1%{?dist}
License: GPLv3
URL: http://launchpad.net/wingpanel-indicator-sound

Source0: %{name}-%{version}.tar.gz
Source1: %{name}.conf

BuildRequires: cmake pkgconfig
BuildRequires: vala gettext

BuildRequires: pkgconfig(granite)
BuildRequires: pkgconfig(libcanberra)
BuildRequires: pkgconfig(libcanberra-gtk3)
BuildRequires: pkgconfig(libnotify)
BuildRequires: pkgconfig(libpulse)
BuildRequires: pkgconfig(libpulse-mainloop-glib)
BuildRequires: pkgconfig(wingpanel-2.0)


%description
A sound indicator for wingpanel.


%prep
%setup -q


%build
%cmake
%make_build


%install
%make_install
%find_lang sound-indicator


%clean
rm -rf $RPM_BUILD_ROOT


%post
/usr/bin/glib-compile-schemas %{_datadir}/glib-2.0/schemas &> /dev/null


%postun
/usr/bin/glib-compile-schemas %{_datadir}/glib-2.0/schemas &> /dev/null


%files -f sound-indicator.lang
%{_libdir}/wingpanel/libsound.so
%{_datadir}/glib-2.0/schemas/org.pantheon.desktop.wingpanel.indicators.sound.gschema.xml


%changelog
* Sun Jan 24 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev69-1
- Update to new upstream snapshot.

* Sat Jan 16 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev68-1
- Update to new upstream snapshot.

* Mon Jan 11 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev67-1
- Update to new upstream snapshot.

* Sun Jan 03 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev66-1
- Update to new upstream snapshot.

* Thu Dec 24 2015 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev65-1
- Update to new upstream snapshot.

* Thu Dec 17 2015 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev64-1
- Update to new upstream snapshot.

* Tue Dec 08 2015 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev63-1
- Update to new upstream snapshot.

* Mon Dec 07 2015 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev62-1
- Update to new upstream snapshot.

* Sun Dec 06 2015 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev61-1
- Update to new upstream snapshot.

* Mon Nov 30 2015 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev60-1
- Update to new upstream snapshot.

* Sat Nov 28 2015 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev59-1
- Update to new upstream snapshot.

* Thu Nov 26 2015 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev58-1
- Update to new upstream snapshot.

* Sun Nov 15 2015 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev57-1
- Update to new upstream snapshot.

* Tue Nov 10 2015 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev56-1
- Update to new upstream snapshot.

* Mon Nov 09 2015 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev55-1
- Update to new upstream snapshot.

* Sat Oct 31 2015 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev54-1
- Update to new upstream snapshot.

* Sun Oct 25 2015 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev52-1
- Update to new upstream snapshot.

* Sat Oct 24 2015 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev51-1
- Update to new upstream snapshot.

* Thu Oct 22 2015 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev48-1
- Update to new upstream snapshot.

* Tue Oct 20 2015 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev47-1
- Update to new upstream snapshot.

* Thu Oct 15 2015 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev46-1
- Update to new upstream snapshot.

* Wed Oct 14 2015 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev45-1
- Update to new upstream snapshot.

* Mon Oct 05 2015 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev44-1
- Update to new upstream snapshot.

* Fri Oct 02 2015 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev42-1
- Update to new upstream snapshot.

* Tue Sep 29 2015 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev41-1
- Update to new upstream snapshot.

* Mon Sep 28 2015 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev40-1
- Update to new upstream snapshot.

* Wed Sep 23 2015 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev39-1
- Update to new upstream snapshot.

* Sat Sep 19 2015 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev38-1
- Update to new upstream snapshot.

* Tue Sep 15 2015 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev37-1
- Update to new upstream snapshot.

* Mon Sep 14 2015 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev36-1
- Update to new upstream snapshot.

* Fri Sep 11 2015 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev34-1
- Update to new upstream snapshot.

* Thu Sep 10 2015 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev33-1
- Update to new upstream snapshot.

* Thu Sep 10 2015 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev32-2
- Release bump for wingpanel soname change.

* Fri Sep 04 2015 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev32-1
- rebuild trigger for granite soname bump

* Tue Sep 01 2015 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev32-1
- Update to new upstream snapshot.

* Sun Aug 23 2015 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev29-1
- Update to new upstream snapshot.

* Sat Aug 22 2015 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev28-1
- Update to new upstream snapshot.

* Fri Aug 21 2015 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev27-2
- Update .spec file to account for new translations.

* Fri Aug 21 2015 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev27-1
- Update to new upstream snapshot.

* Mon Aug 17 2015 Fabio Valentini - 0.1~rev25-1
- Update to new upstream snapshot.

* Tue Jul 14 2015 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev24-1
- Initial package.


