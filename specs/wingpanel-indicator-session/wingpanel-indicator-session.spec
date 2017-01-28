%global debug_package %{nil}

Summary:        a session Indicator for wingpanel
Name:           wingpanel-indicator-session
Version:        2.0.1+rev%{rev}
Release:        1%{?dist}
License:        GPLv3, LGPLv3
URL:            http://launchpad.net/wingpanel-indicator-session

Source0:        %{name}-%{version}.tar.gz
Source1:        %{name}.conf

BuildRequires:  cmake
BuildRequires:  gettext
BuildRequires:  pkgconfig
BuildRequires:  vala >= 0.22.0
BuildRequires:  vala-tools

BuildRequires:  pkgconfig(accountsservice)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(granite)
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.12.0
BuildRequires:  pkgconfig(wingpanel-2.0)


%description
a session Indicator for wingpanel


%prep
%autosetup


%build
%cmake
%make_build


%install
%make_install
%find_lang session-indicator


%clean
rm -rf %{buildroot}


%files -f session-indicator.lang
%license COPYING

%{_libdir}/wingpanel/libsession.so


%changelog
* Sat Jan 28 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0.1+rev114-1
- Update to latest snapshot.

* Fri Jan 27 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0.1+rev113-1
- Update to latest snapshot.

* Fri Jan 27 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0.1+rev112-1
- Update to latest snapshot.

* Mon Jan 23 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0.1+rev111-1
- Update to latest snapshot.

* Fri Jan 06 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0.1+rev110-1
- Update to version 2.0.1.

* Wed Dec 28 2016 Fabio Valentini <decathorpe@gmail.com> - 2.0.1+rev109-1
- Update to latest snapshot.

* Wed Dec 21 2016 Fabio Valentini <decathorpe@gmail.com> - 2.0.1+rev108-1
- Update to latest snapshot.

* Tue Dec 13 2016 Fabio Valentini <decathorpe@gmail.com> - 2.0.1+rev107-1
- Update to latest snapshot.

* Thu Dec 08 2016 Fabio Valentini <decathorpe@gmail.com> - 2.0.1+rev106-1
- Update to latest snapshot.

* Thu Dec 01 2016 Fabio Valentini <decathorpe@gmail.com> - 2.0.1+rev105-1
- Update to version 2.0.1.

* Thu Dec 01 2016 Fabio Valentini <decathorpe@gmail.com> - 2.0+rev105-1
- Update to latest snapshot.

* Wed Nov 16 2016 Fabio Valentini <decathorpe@gmail.com> - 2.0+rev104-1
- Update to latest snapshot.

* Mon Nov 07 2016 Fabio Valentini <decathorpe@gmail.com> - 2.0+rev103-1
- Update to latest snapshot.

* Sun Oct 30 2016 Fabio Valentini <decathorpe@gmail.com> - 2.0+rev102-1
- Update to version 2.0.

* Wed Sep 21 2016 Fabio Valentini <decathorpe@gmail.com> - 2.0~rev101-1
- Update to latest snapshot.

* Sat Sep 17 2016 Fabio Valentini <decathorpe@gmail.com> - 2.0~rev100-1
- Update to latest snapshot.

* Thu Sep 01 2016 Fabio Valentini <decathorpe@gmail.com> - 2.0~rev99-1
- Update to latest snapshot.

* Wed Aug 31 2016 Fabio Valentini <decathorpe@gmail.com> - 2.0~rev98-1
- Update to latest snapshot.

* Mon Aug 22 2016 Fabio Valentini <decathorpe@gmail.com> - 2.0~rev97-1
- Update to version 2.0.

* Sun Aug 14 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev96-1
- Update to latest snapshot.

* Mon Aug 08 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev94-1
- Update to latest snapshot.

* Sun Aug 07 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev92-2
- Update for packaging changes.

* Sun Aug 07 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev92-1
- Update to latest snapshot.

* Thu Aug 04 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev91-1
- Update to latest snapshot.

* Tue Aug 02 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev90-1
- Update to latest snapshot.

* Thu Jul 28 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev89-1
- Update to latest snapshot.

* Mon Jul 25 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev88-1
- Update to latest snapshot.

* Thu Jul 21 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev87-1
- Update to latest snapshot.

* Tue Jul 12 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev85-1
- Update to latest snapshot.

* Fri Jul 08 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev84-1
- Update to latest snapshot.

* Wed Jul 06 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev83-2
- Update for packaging changes.

* Tue Jul 05 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev83-1
- Update to latest snapshot.

* Mon Jul 04 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev82-1
- Update to latest snapshot.

* Mon Jun 27 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev81-1
- Update to latest snapshot.

* Sat Jun 18 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev80-1
- Update to latest snapshot.

* Fri Jun 17 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev79-1
- Update to latest snapshot.

* Wed Jun 08 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev78-1
- Update to latest snapshot.

* Tue Jun 07 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev77-1
- Update to latest snapshot.

* Mon May 30 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev76-2
- Update for packaging changes.

* Sun May 29 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev76-1
- Update to latest snapshot.

* Mon May 23 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev75-1
- Update to latest snapshot.

* Sat May 21 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev74-1
- Update to latest snapshot.

* Tue May 10 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev73-1
- Update to latest snapshot.

* Mon May 09 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev72-2
- Update for packaging changes.

* Mon May 09 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev72-1
- Initial package.


