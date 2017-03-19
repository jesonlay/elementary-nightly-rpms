%global debug_package %{nil}

Summary:        a sound indicator for wingpanel
Name:           wingpanel-indicator-sound
Version:        2.0.3+rev%{rev}
Release:        1%{?dist}
License:        GPLv3
URL:            http://launchpad.net/wingpanel-indicator-sound

# The tarball is generated from a checkout of the specified branch and
# by executing 'bzr export' and has the usual format
# ('%{name}-%{version}.tar.gz'), where %{version} contains the upstream
# version number with a '+bzr%{rev}' suffix specifying the bzr revision.
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


%files -f sound-indicator.lang
%{_libdir}/wingpanel/libsound.so

%{_datadir}/glib-2.0/schemas/org.pantheon.desktop.wingpanel.indicators.sound.gschema.xml


%changelog
* Sun Mar 19 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0.3+rev152-1
- Update to latest snapshot.

* Sun Mar 05 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0.3+rev151-1
- Update to latest snapshot.

* Sun Feb 19 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0.3+rev150-1
- Update to latest snapshot.

* Mon Feb 06 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0.3+rev149-1
- Update to latest snapshot.

* Sat Feb 04 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0.3+rev148-1
- Update to latest snapshot.

* Thu Feb 02 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0.3+rev147-1
- Update to latest snapshot.

* Fri Jan 27 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0.3+rev146-1
- Update to latest snapshot.

* Thu Jan 26 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0.3+rev145-1
- Update to latest snapshot.

* Wed Jan 25 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0.3+rev144-1
- Update to latest snapshot.

* Wed Jan 18 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0.3+rev143-1
- Update to latest snapshot.

* Sat Jan 07 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0.3+rev142-1
- Update to version 2.0.3.

* Thu Jan 05 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0.3+rev141-1
- Update to version 2.0.3.

* Thu Dec 29 2016 Fabio Valentini <decathorpe@gmail.com> - 2.0.3+rev140-1
- Update to latest snapshot.

* Wed Dec 28 2016 Fabio Valentini <decathorpe@gmail.com> - 2.0.3+rev139-1
- Update to latest snapshot.

* Thu Dec 22 2016 Fabio Valentini <decathorpe@gmail.com> - 2.0.3+rev138-1
- Update to latest snapshot.

* Thu Dec 22 2016 Fabio Valentini <decathorpe@gmail.com> - 2.0.3+rev137-1
- Update to latest snapshot.

* Wed Dec 21 2016 Fabio Valentini <decathorpe@gmail.com> - 2.0.3+rev136-1
- Update to latest snapshot.

* Wed Dec 14 2016 Fabio Valentini <decathorpe@gmail.com> - 2.0.3+rev135-1
- Update to latest snapshot.

* Thu Dec 08 2016 Fabio Valentini <decathorpe@gmail.com> - 2.0.3+rev134-1
- Update to latest snapshot.

* Sun Dec 04 2016 Fabio Valentini <decathorpe@gmail.com> - 2.0.3+rev133-1
- Update to latest snapshot.

* Tue Nov 29 2016 Fabio Valentini <decathorpe@gmail.com> - 2.0.3+rev132-1
- Update to latest snapshot.

* Sat Nov 19 2016 Fabio Valentini <decathorpe@gmail.com> - 2.0.3+rev131-1
- Update to latest snapshot.

* Mon Nov 14 2016 Fabio Valentini <decathorpe@gmail.com> - 2.0.3+rev130-1
- Update to latest snapshot.

* Mon Nov 07 2016 Fabio Valentini <decathorpe@gmail.com> - 2.0.3+rev129-1
- Update to latest snapshot.

* Sun Nov 06 2016 Fabio Valentini <decathorpe@gmail.com> - 2.0.3+rev128-1
- Update to latest snapshot.

* Sun Nov 06 2016 Fabio Valentini <decathorpe@gmail.com> - 2.0.3+rev127-1
- Update to latest snapshot.

* Sun Nov 06 2016 Fabio Valentini <decathorpe@gmail.com> - 2.0.3+rev126-1
- Update to latest snapshot.

* Mon Oct 31 2016 Fabio Valentini <decathorpe@gmail.com> - 2.0.3+rev125-1
- Update to version 2.0.3.

* Mon Oct 24 2016 Fabio Valentini <decathorpe@gmail.com> - 2.0.2+rev123-1
- Update to latest snapshot.

* Sun Oct 09 2016 Fabio Valentini <decathorpe@gmail.com> - 2.0.2+rev121-1
- Update to latest snapshot.

* Thu Oct 06 2016 Fabio Valentini <decathorpe@gmail.com> - 2.0.2+rev120-1
- Update to latest snapshot.

* Tue Oct 04 2016 Fabio Valentini <decathorpe@gmail.com> - 2.0.2+rev119-1
- Update to version 2.0.2.

* Tue Oct 04 2016 Fabio Valentini <decathorpe@gmail.com> - 2.0.1+rev119-1
- Update to latest snapshot.

* Thu Sep 29 2016 Fabio Valentini <decathorpe@gmail.com> - 2.0.1+rev118-2
- Spec file cleanups.

* Thu Sep 29 2016 Fabio Valentini <decathorpe@gmail.com> - 2.0.1+rev118-1
- Update to latest snapshot.

* Thu Sep 22 2016 Fabio Valentini <decathorpe@gmail.com> - 2.0.1+rev117-1
- Update to version 2.0.1.

* Wed Sep 14 2016 Fabio Valentini <decathorpe@gmail.com> - 2.0.1~rev116-1
- Update to version 2.0.1.

* Sun Sep 11 2016 Fabio Valentini <decathorpe@gmail.com> - 2.0~rev115-1
- Update to latest snapshot.

* Fri Sep 09 2016 Fabio Valentini <decathorpe@gmail.com> - 2.0~rev114-1
- Update to latest snapshot.

* Sun Sep 04 2016 Fabio Valentini <decathorpe@gmail.com> - 2.0~rev113-1
- Update to latest snapshot.

* Sat Sep 03 2016 Fabio Valentini <decathorpe@gmail.com> - 2.0~rev112-1
- Update to latest snapshot.

* Mon Aug 22 2016 Fabio Valentini <decathorpe@gmail.com> - 2.0~rev111-1
- Update to version 2.0.

* Sun Aug 14 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev110-1
- Update to latest snapshot.

* Mon Aug 08 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev109-1
- Update to latest snapshot.

* Sun Aug 07 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev108-2
- Update for packaging changes.

* Sun Aug 07 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev108-1
- Update to latest snapshot.

* Sat Aug 06 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev107-1
- Update to latest snapshot.

* Fri Aug 05 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev106-1
- Update to latest snapshot.

* Thu Aug 04 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev105-1
- Update to latest snapshot.

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

* Tue May 10 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev85-1
- Initial package.


