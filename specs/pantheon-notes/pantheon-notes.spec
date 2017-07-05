Summary:        Simple note taking app for elementary OS
Name:           pantheon-notes
Version:        0.7+rev%{rev}
Release:        1%{?dist}
License:        GPLv3
URL:            http://launchpad.net/pantheon-notes

Source0:        %{name}-%{version}.tar.gz
Source1:        %{name}.conf

BuildRequires:  cmake
BuildRequires:  desktop-file-utils
BuildRequires:  gettext
BuildRequires:  vala >= 0.26.0
BuildRequires:  vala-tools

BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gmime-2.6) >= 2.6.14
BuildRequires:  pkgconfig(granite) >= 0.3
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.9.10
BuildRequires:  pkgconfig(gtksourceview-3.0) >= 3.10


%description
Simple note taking app for elementary OS


%prep
%autosetup


%build
CFLAGS="$RPM_OPT_FLAGS -fPIC"
LDFLAGS="$RPM_OPT_FLAGS -fPIC"

%cmake
%make_build


%install
%make_install
%find_lang pantheon-notes


%check
desktop-file-validate %{buildroot}/%{_datadir}/applications/*.desktop


%clean
rm -rf %{buildroot}


%if %{?fedora} < 25
%post
/usr/bin/update-desktop-database &> /dev/null || :

%postun
/usr/bin/update-desktop-database &> /dev/null || :
%endif


%files -f pantheon-notes.lang
%{_bindir}/pantheon-notes

%{_datadir}/applications/pantheon-notes.desktop
%{_datadir}/glib-2.0/schemas/org.pantheon.notes.gschema.xml
%{_datadir}/pixmaps/pantheon-notes.svg


%changelog
* Wed Jul 05 2017 Fabio Valentini <decathorpe@gmail.com> - 0.7+rev71-1
- Update to latest snapshot.

* Sun Jul 02 2017 Fabio Valentini <decathorpe@gmail.com> - 0.7+rev70-1
- Update to latest snapshot.

* Fri May 19 2017 Fabio Valentini <decathorpe@gmail.com> - 0.7+rev69-1
- Update to latest snapshot.

* Wed May 17 2017 Fabio Valentini <decathorpe@gmail.com> - 0.7+rev68-1
- Update to latest snapshot.

* Sat May 06 2017 Fabio Valentini <decathorpe@gmail.com> - 0.7+rev67-1
- Update to latest snapshot.

* Fri Apr 14 2017 Fabio Valentini <decathorpe@gmail.com> - 0.7+rev66-1
- Update to latest snapshot.

* Sun Mar 19 2017 Fabio Valentini <decathorpe@gmail.com> - 0.7+rev65-1
- Update to latest snapshot.

* Wed Mar 15 2017 Fabio Valentini <decathorpe@gmail.com> - 0.7+rev64-1
- Update to latest snapshot.

* Sat Feb 11 2017 Fabio Valentini <decathorpe@gmail.com> - 0.7+rev63-1
- Update to latest snapshot.

* Sun Jan 29 2017 Fabio Valentini <decathorpe@gmail.com> - 0.7+rev62-1
- Update to latest snapshot.

* Sat Jan 28 2017 Fabio Valentini <decathorpe@gmail.com> - 0.7+rev61-1
- Update to latest snapshot.

* Fri Jan 27 2017 Fabio Valentini <decathorpe@gmail.com> - 0.7+rev60-1
- Update to latest snapshot.

* Wed Jan 25 2017 Fabio Valentini <decathorpe@gmail.com> - 0.7+rev59-1
- Update to latest snapshot.

* Sat Jan 07 2017 Fabio Valentini <decathorpe@gmail.com> - 0.7+rev58-1
- Update to version 0.7.

* Mon Dec 26 2016 Fabio Valentini <decathorpe@gmail.com> - 0.7+rev57-1
- Update to latest snapshot.

* Mon Dec 12 2016 Fabio Valentini <decathorpe@gmail.com> - 0.7+rev56-1
- Update to latest snapshot.

* Sun Dec 04 2016 Fabio Valentini <decathorpe@gmail.com> - 0.7+rev55-1
- Update to latest snapshot.

* Fri Oct 21 2016 Fabio Valentini <decathorpe@gmail.com> - 0.7+rev54-1
- Update to latest snapshot.

* Tue Oct 18 2016 Fabio Valentini <decathorpe@gmail.com> - 0.7+rev53-1
- Update to latest snapshot.

* Tue Oct 04 2016 Fabio Valentini <decathorpe@gmail.com> - 0.7+rev52-1
- Update to latest snapshot.

* Thu Sep 29 2016 Fabio Valentini <decathorpe@gmail.com> - 0.7+rev51-1
- Update to version 0.7.

* Thu Sep 29 2016 Fabio Valentini <decathorpe@gmail.com> - 0.7~rev51-2
- Spec file cleanups.

* Tue Aug 23 2016 Fabio Valentini <decathorpe@gmail.com> - 0.7~rev51-1
- Update to latest snapshot.

* Sun Aug 14 2016 Fabio Valentini <decathorpe@gmail.com> - 0.7~rev50-1
- Update to latest snapshot.

* Sat Aug 13 2016 Fabio Valentini <decathorpe@gmail.com> - 0.7~rev49-1
- Update to latest snapshot.

* Fri Aug 12 2016 Fabio Valentini <decathorpe@gmail.com> - 0.7~rev48-1
- Update to latest snapshot.

* Thu Aug 11 2016 Fabio Valentini <decathorpe@gmail.com> - 0.7~rev47-1
- Update to latest snapshot.

* Tue Aug 09 2016 Fabio Valentini <decathorpe@gmail.com> - 0.7~rev46-1
- Update to latest snapshot.

* Sun Aug 07 2016 Fabio Valentini <decathorpe@gmail.com> - 0.7~rev45-2
- Update for packaging changes.

* Sun Aug 07 2016 Fabio Valentini <decathorpe@gmail.com> - 0.7~rev45-1
- Update to latest snapshot.

* Sat Aug 06 2016 Fabio Valentini <decathorpe@gmail.com> - 0.7~rev44-1
- Update to latest snapshot.

* Fri Aug 05 2016 Fabio Valentini <decathorpe@gmail.com> - 0.7~rev43-1
- Update to latest snapshot.

* Thu Aug 04 2016 Fabio Valentini <decathorpe@gmail.com> - 0.7~rev42-1
- Update to latest snapshot.

* Tue Aug 02 2016 Fabio Valentini <decathorpe@gmail.com> - 0.7~rev40-1
- Update to latest snapshot.

* Mon Jul 25 2016 Fabio Valentini <decathorpe@gmail.com> - 0.7~rev39-1
- Update to latest snapshot.

* Tue Jul 19 2016 Fabio Valentini <decathorpe@gmail.com> - 0.7~rev37-1
- Update to latest snapshot.

* Fri Jul 08 2016 Fabio Valentini <decathorpe@gmail.com> - 0.7~rev36-1
- Update to latest snapshot.

* Wed Jul 06 2016 Fabio Valentini <decathorpe@gmail.com> - 0.7~rev35-2
- Update for packaging changes.

* Tue Jul 05 2016 Fabio Valentini <decathorpe@gmail.com> - 0.7~rev35-1
- Update to latest snapshot.

* Mon Jul 04 2016 Fabio Valentini <decathorpe@gmail.com> - 0.7~rev34-1
- Update to latest snapshot.

* Sun Jul 03 2016 Fabio Valentini <decathorpe@gmail.com> - 0.7~rev33-1
- Update to latest snapshot.

* Sat Jul 02 2016 Fabio Valentini <decathorpe@gmail.com> - 0.7~rev32-1
- Update to latest snapshot.

* Fri Jul 01 2016 Fabio Valentini <decathorpe@gmail.com> - 0.7~rev31-1
- Update to latest snapshot.

* Thu Jun 30 2016 Fabio Valentini <decathorpe@gmail.com> - 0.7~rev30-1
- Update to latest snapshot.

* Wed Jun 15 2016 Fabio Valentini <decathorpe@gmail.com> - 0.7~rev29-1
- Update to latest snapshot.

* Tue Jun 14 2016 Fabio Valentini <decathorpe@gmail.com> - 0.7~rev28-1
- Update to latest snapshot.

* Mon May 30 2016 Fabio Valentini <decathorpe@gmail.com> - 0.7~rev27-3
- Update for packaging changes.

* Sun May 29 2016 Fabio Valentini <decathorpe@gmail.com> - 0.7~rev27-2
- Update for packaging changes.

* Fri May 27 2016 Fabio Valentini <decathorpe@gmail.com> - 0.7~rev27-1
- Update to latest snapshot.

* Mon May 23 2016 Fabio Valentini <decathorpe@gmail.com> - 0.7~rev26-1
- Update to latest snapshot.

* Fri May 13 2016 Fabio Valentini <decathorpe@gmail.com> - 0.7~rev25-1
- Update to latest snapshot.

* Thu May 05 2016 Fabio Valentini <decathorpe@gmail.com> - 0.7~rev24-2
- Update for packaging changes.

* Thu May 05 2016 Fabio Valentini <decathorpe@gmail.com> - 0.7-1
- Initial package.


