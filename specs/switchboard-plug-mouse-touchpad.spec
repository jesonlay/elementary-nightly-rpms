%global debug_package %{nil}

Summary:        Mouse and Touchpad configuration management
Name:           switchboard-plug-mouse-touchpad
Version:        0.1.1~rev%{rev}
Release:        1%{?dist}
License:        GPLv3
URL:            http://launchpad.net/switchboard-plug-mouse-touchpad

Source0:        %{name}-%{version}.tar.gz
Source1:        %{name}.conf

Patch0:         00-gschema-path.patch

BuildRequires:  cmake
BuildRequires:  gettext
BuildRequires:  pkgconfig
BuildRequires:  vala >= 0.22.0
BuildRequires:  vala-tools

BuildRequires:  pkgconfig(glib-2.0) >= 2.32
BuildRequires:  pkgconfig(granite)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(switchboard-2.0)


%description
This is a swtichboard plug for elementary os.


%prep
%setup -q
%patch0 -p0


%build
%cmake
%make_build


%install
%make_install
%find_lang pantheon-mouse-touchpad


%clean
rm -rf %{buildroot}


%files -f pantheon-mouse-touchpad.lang
%{_libdir}/switchboard/hardware/pantheon-mouse-touchpad/


%changelog
* Sat Sep 17 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.1~rev113-1
- Update to latest snapshot.

* Fri Sep 16 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.1~rev112-1
- Update to latest snapshot.

* Fri Sep 16 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.1~rev110-1
- Update to latest snapshot.

* Thu Sep 15 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.1~rev107-1
- Update to latest snapshot.

* Sat Aug 20 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.1~rev97-4
- Update for packaging changes.

* Sat Aug 20 2016 Fabio Valentini <decathorpe@gmail.com>
- Fix applying patch.

* Sat Aug 20 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.1~rev97-3
- Update for packaging changes.

* Sat Aug 20 2016 Fabio Valentini <decathorpe@gmail.com>
- Fix applying patch.

* Sat Aug 20 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.1~rev97-2
- Update for packaging changes.

* Sun Aug 14 2016 Fabio Valentini <decathorpe@gmail.com>
- Add patch to fix SEGFAULT (wrong gsettings path).

* Sun Aug 14 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.1~rev97-1
- Update to latest snapshot.

* Fri Aug 12 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.1~rev96-1
- Update to latest snapshot.

* Thu Aug 11 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.1~rev95-1
- Update to latest snapshot.

* Wed Aug 10 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.1~rev94-1
- Update to latest snapshot.

* Mon Aug 08 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.1~rev93-1
- Update to latest snapshot.

* Sun Aug 07 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.1~rev92-2
- Update for packaging changes.

* Sun Aug 07 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.1~rev92-1
- Update to latest snapshot.

* Fri Aug 05 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.1~rev91-1
- Update to latest snapshot.

* Thu Aug 04 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.1~rev90-1
- Update to latest snapshot.

* Tue Aug 02 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.1~rev88-1
- Update to latest snapshot.

* Mon Aug 01 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.1~rev87-1
- Update to latest snapshot.

* Wed Jul 27 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.1~rev83-1
- Update to latest snapshot.

* Tue Jul 26 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.1~rev82-1
- Update to latest snapshot.

* Mon Jul 25 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.1~rev81-1
- Update to latest snapshot.

* Fri Jul 22 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.1~rev78-1
- Update to latest snapshot.

* Thu Jul 21 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.1~rev77-1
- Update to latest snapshot.

* Tue Jul 19 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.1~rev75-1
- Update to latest snapshot.

* Mon Jul 18 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.1~rev74-1
- Update to latest snapshot.

* Sun Jul 17 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.1~rev73-1
- Update to latest snapshot.

* Thu Jul 14 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.1~rev72-1
- Update to latest snapshot.

* Fri Jul 08 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.1~rev71-1
- Update to latest snapshot.

* Wed Jul 06 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.1~rev70-2
- Update for packaging changes.

* Tue Jun 21 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.1~rev65-1
- Update to latest snapshot.

* Mon Jun 20 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.1~rev64-1
- Update to latest snapshot.

* Sun Jun 19 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.1~rev63-1
- Update to latest snapshot.

* Sat Jun 18 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.1~rev60-1
- Update to latest snapshot.

* Sat Jun 18 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.1~rev59-1
- Update to latest snapshot.

* Fri Jun 17 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.1~rev58-1
- Update to latest snapshot.

* Tue Jun 14 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.1~rev57-1
- Update to latest snapshot.

* Mon May 30 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.1~rev56-4
- Update for packaging changes.

* Sun May 29 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.1~rev56-3
- Update for packaging changes.

* Fri May 13 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.1~rev56-2
- Update for packaging changes.

* Tue May 10 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev56-1
- Initial package.

