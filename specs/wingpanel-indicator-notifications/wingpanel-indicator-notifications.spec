%global __provides_exclude_from ^%{_libdir}/wingpanel/.*\\.so$

Name:           wingpanel-indicator-notifications
Summary:        Notifications Indicator for wingpanel
Version:        2.0.2+git%{date}.%{commit}
Release:        1%{?dist}
License:        LGPLv2+

URL:            https://github.com/elementary/%{name}
Source0:        %{name}-%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  gettext
BuildRequires:  vala >= 0.22.0
BuildRequires:  vala-tools

BuildRequires:  pkgconfig(gdk-pixbuf-2.0)
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(granite)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(libwnck-3.0)
BuildRequires:  pkgconfig(wingpanel-2.0)

Supplements:    wingpanel%{?_isa}


%description
A notifications indicator for wingpanel.


%prep
%autosetup


%build
mkdir build && pushd build
%cmake ..
%make_build
popd


%install
pushd build
%make_install
popd

%find_lang notifications-indicator


%files -f notifications-indicator.lang
%doc README.md
%license COPYING

%{_libdir}/wingpanel/libnotifications-indicator.so


%changelog
* Tue Feb 13 2018 Fabio Valentini <decathorpe@gmail.com> - 2.0.2+git180213.095250.c6294836-1
- Update to latest snapshot.

* Tue Feb 06 2018 Fabio Valentini <decathorpe@gmail.com> - 2.0.2+git180206.202826.f278ea11-1
- Update to latest snapshot.

* Fri Jan 05 2018 Fabio Valentini <decathorpe@gmail.com> - 2.0.2+git180102.235703.cc7b6431-2
- Merge .spec file from fedora.

* Wed Jan 03 2018 Fabio Valentini <decathorpe@gmail.com> - 2.0.2+git180102.235703.cc7b6431-1
- Update to latest snapshot.

* Tue Jan 02 2018 Fabio Valentini <decathorpe@gmail.com> - 2.0.2+git180102.221034.60bc930f-1
- Update to latest snapshot.

* Mon Jan 01 2018 Fabio Valentini <decathorpe@gmail.com> - 2.0.2+git180101.154957.7c2bca4b-1
- Update to latest snapshot.

* Wed Oct 04 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0.2+git171004.022804.833dc8e3-1
- Update to latest snapshot.

* Tue Sep 12 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0.2+git170907.203755.6c5f310b-1
- Update to latest snapshot.

* Tue Aug 01 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0.2+git170801.024102.3c5f2ed7-1
- Update to version 2.0.2.

* Tue Aug 01 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0.1+git170801.024102.3c5f2ed7-1
- Update to latest snapshot.

* Mon Jul 31 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0.1+git170731.153924.a63bf1f1-1
- Update to latest snapshot.

* Sat Jul 15 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0.1+git170706.080620.37ce52fe-1
- Update to latest snapshot.

* Sun Jul 02 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0.1+git170702.102902.64fa740b-1
- Update to latest snapshot.

* Sun Jun 18 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0.1+git170617.173958.f6899482-1
- Update to latest snapshot.

* Fri Jun 02 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0.1+git170602.173816.8f0fb268-1
- Update to latest snapshot.

* Mon May 22 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0.1+git170521.220711.03d613b0-1
- Update to version 2.0.1.

* Mon May 22 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0+rev156-1
- Update to latest snapshot.

* Thu May 18 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0+rev155-1
- Update to latest snapshot.

* Wed May 17 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0+rev154-1
- Update to latest snapshot.

* Tue Apr 25 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0+rev153-1
- Update to latest snapshot.

* Wed Apr 05 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0+rev151-1
- Update to latest snapshot.

* Sun Mar 19 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0+rev150-1
- Update to latest snapshot.

* Wed Mar 15 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0+rev149-1
- Update to latest snapshot.

* Tue Mar 14 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0+rev148-1
- Update to latest snapshot.

* Sat Mar 04 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0+rev147-1
- Update to latest snapshot.

* Tue Feb 28 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0+rev146-1
- Update to latest snapshot.

* Wed Feb 22 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0+rev145-1
- Update to latest snapshot.

* Mon Feb 20 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0+rev144-1
- Update to latest snapshot.

* Sun Feb 19 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0+rev143-1
- Update to latest snapshot.

* Sat Feb 18 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0+rev142-1
- Update to latest snapshot.

* Fri Feb 17 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0+rev141-1
- Update to latest snapshot.

* Thu Feb 16 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0+rev140-1
- Update to latest snapshot.

* Wed Feb 15 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0+rev139-1
- Update to latest snapshot.

* Sun Feb 12 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0+rev138-1
- Update to latest snapshot.

* Fri Feb 10 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0+rev137-1
- Update to latest snapshot.

* Thu Feb 02 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0+rev136-1
- Update to latest snapshot.

* Sun Jan 29 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0+rev135-1
- Update to latest snapshot.

* Sat Jan 28 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0+rev134-1
- Update to latest snapshot.

* Wed Jan 18 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0+rev133-1
- Update to latest snapshot.

* Sat Jan 07 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0+rev132-1
- Update to version 2.0.

* Mon Dec 19 2016 Fabio Valentini <decathorpe@gmail.com> - 2.0+rev131-1
- Update to latest snapshot.

* Sun Dec 18 2016 Fabio Valentini <decathorpe@gmail.com> - 2.0+rev130-1
- Update to latest snapshot.

* Thu Dec 15 2016 Fabio Valentini <decathorpe@gmail.com> - 2.0+rev128-1
- Update to latest snapshot.

* Wed Dec 14 2016 Fabio Valentini <decathorpe@gmail.com> - 2.0+rev127-1
- Update to latest snapshot.

* Mon Dec 12 2016 Fabio Valentini <decathorpe@gmail.com> - 2.0+rev126-1
- Update to latest snapshot.

* Sun Dec 11 2016 Fabio Valentini <decathorpe@gmail.com> - 2.0+rev125-1
- Update to latest snapshot.

* Mon Dec 05 2016 Fabio Valentini <decathorpe@gmail.com> - 2.0+rev124-1
- Update to latest snapshot.

* Sun Dec 04 2016 Fabio Valentini <decathorpe@gmail.com> - 2.0+rev123-1
- Update to latest snapshot.

* Sun Oct 09 2016 Fabio Valentini <decathorpe@gmail.com> - 2.0+rev122-1
- Update to latest snapshot.

* Sat Oct 08 2016 Fabio Valentini <decathorpe@gmail.com> - 2.0+rev121-1
- Update to latest snapshot.

* Sat Sep 24 2016 Fabio Valentini <decathorpe@gmail.com> - 2.0+rev120-1
- Update to latest snapshot.

* Fri Sep 23 2016 Fabio Valentini <decathorpe@gmail.com> - 2.0+rev119-1
- Update to version 2.0.

* Wed Sep 14 2016 Fabio Valentini <decathorpe@gmail.com> - 2.0~rev118-1
- Update to latest snapshot.

* Mon Aug 22 2016 Fabio Valentini <decathorpe@gmail.com> - 2.0~rev117-1
- Update to version 2.0.

* Sun Aug 14 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev116-1
- Update to latest snapshot.

* Tue Aug 09 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev115-1
- Update to latest snapshot.

* Sun Aug 07 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev114-2
- Update for packaging changes.

* Sat Aug 06 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev114-1
- Update to latest snapshot.

* Fri Aug 05 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev113-1
- Update to latest snapshot.

* Thu Aug 04 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev112-1
- Update to latest snapshot.

* Tue Aug 02 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev110-1
- Update to latest snapshot.

* Tue Aug 02 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev109-1
- Update to latest snapshot.

* Tue Aug 02 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev108-1
- Update to latest snapshot.

* Sun Jul 31 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev107-1
- Update to latest snapshot.

* Fri Jul 29 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev106-1
- Update to latest snapshot.

* Tue Jul 26 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev105-1
- Update to latest snapshot.

* Tue Jul 19 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev104-1
- Update to latest snapshot.

* Mon Jul 18 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev103-1
- Update to latest snapshot.

* Sun Jul 17 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev102-1
- Update to latest snapshot.

* Mon Jul 11 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev101-1
- Update to latest snapshot.

* Sun Jul 10 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev100-1
- Update to latest snapshot.

* Wed Jul 06 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev99-2
- Update for packaging changes.

* Mon Jun 20 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev96-1
- Update to latest snapshot.

* Mon Jun 20 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev95-1
- Update to latest snapshot.

* Mon Jun 13 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev94-1
- Update to latest snapshot.

* Fri Jun 03 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev93-1
- Update to latest snapshot.

* Mon May 30 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev92-3
- Update for packaging changes.

* Sun May 29 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev92-2
- Update for packaging changes.

* Sat May 28 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev92-1
- Update to latest snapshot.

* Thu May 26 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev91-1
- Update to latest snapshot.

* Wed May 25 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev90-1
- Update to latest snapshot.

* Tue May 24 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev89-1
- Update to latest snapshot.

* Sat May 21 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev86-1
- Update to latest snapshot.

* Thu May 12 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev85-1
- Update to latest snapshot.

* Tue May 10 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev84-2
- Update for packaging changes.

* Tue May 10 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev84-1
- Initial package.


