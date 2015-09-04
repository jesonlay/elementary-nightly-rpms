%define rev 32
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


