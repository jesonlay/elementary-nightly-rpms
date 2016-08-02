%global debug_package %{nil}

Summary:        a sound indicator for wingpanel
Name:           wingpanel-indicator-sound
Version:        0.1~rev%{rev}
Release:        1%{?dist}
License:        GPLv3
URL:            http://launchpad.net/wingpanel-indicator-sound

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
BuildRequires:  pkgconfig(libcanberra)
BuildRequires:  pkgconfig(libcanberra-gtk)
BuildRequires:  pkgconfig(libnotify)
BuildRequires:  pkgconfig(libpulse)
BuildRequires:  pkgconfig(libpulse-mainloop-glib)
BuildRequires:  pkgconfig(wingpanel-2.0)


%description
a sound indicator for wingpanel


%prep
%autosetup


%build
%cmake
%make_build


%install
%make_install
%find_lang sound-indicator


%clean
rm -rf %{buildroot}


%postun
if [ $1 -eq 0 ] ; then
    /usr/bin/glib-compile-schemas %{_datadir}/glib-2.0/schemas &> /dev/null || :
fi

%posttrans
/usr/bin/glib-compile-schemas %{_datadir}/glib-2.0/schemas &> /dev/null || :


%files -f sound-indicator.lang
%{_libdir}/wingpanel/libsound.so

%{_datadir}/glib-2.0/schemas/org.pantheon.desktop.wingpanel.indicators.sound.gschema.xml


%changelog
* Tue Aug 02 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev103-1
- Update to latest snapshot.

* Sun Jul 31 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev102-1
- Update to latest snapshot.

* Tue Jul 26 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev101-1
- Update to latest snapshot.

* Mon Jul 25 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev100-1
- Update to latest snapshot.

* Fri Jul 22 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev98-1
- Update to latest snapshot.

* Thu Jul 21 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev97-1
- Update to latest snapshot.

* Fri Jul 15 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev96-1
- Update to latest snapshot.

* Wed Jul 06 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev95-2
- Update for packaging changes.

* Sun Jun 19 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev91-1
- Update to latest snapshot.

* Sat Jun 18 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev90-1
- Update to latest snapshot.

* Fri Jun 17 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev89-1
- Update to latest snapshot.

* Mon Jun 13 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev88-1
- Update to latest snapshot.

* Mon May 30 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev87-3
- Update for packaging changes.

* Sun May 29 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev87-2
- Update for packaging changes.

* Wed May 25 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev87-1
- Update to latest snapshot.

* Sat May 21 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev86-1
- Update to latest snapshot.

* Tue May 10 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev85-2
- Update for packaging changes.

* Tue May 10 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev%{rev}-1
- Initial package.

