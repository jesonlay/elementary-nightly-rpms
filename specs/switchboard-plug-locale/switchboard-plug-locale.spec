%global __provides_exclude_from ^%{_libdir}/switchboard/.*\\.so$

Name:           switchboard-plug-locale
Summary:        Adjust Locale settings from Switchboard
Version:        0.2.3+git%{date}.%{commit}
Release:        1%{?dist}
License:        LGPLv3

URL:            https://github.com/elementary/%{name}
Source0:        %{name}-%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  gettext
BuildRequires:  vala >= 0.34.1
BuildRequires:  vala-tools

BuildRequires:  pkgconfig(accountsservice)
BuildRequires:  pkgconfig(glib-2.0) >= 2.32
BuildRequires:  pkgconfig(gnome-desktop-3.0)
BuildRequires:  pkgconfig(granite)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(ibus-1.0)
BuildRequires:  pkgconfig(polkit-gobject-1)
BuildRequires:  pkgconfig(switchboard-2.0)

Supplements:    switchboard%{?_isa}


%description
Adjust Locale settings from Switchboard.


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

%find_lang locale-plug


%files -f locale-plug.lang
%doc README.md
%license COPYING

%{_libdir}/switchboard/personal/pantheon-locale/

%{_datadir}/glib-2.0/schemas/org.pantheon.switchboard.plug.locale.gschema.xml
%{_datadir}/polkit-1/actions/org.pantheon.switchboard.locale.policy


%changelog
* Tue Feb 20 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.3+git180219.231907.9cf8d3a5-1
- Update to latest snapshot.

* Sun Feb 18 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.3+git180218.194144.8d8d0438-1
- Update to latest snapshot.

* Mon Feb 12 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.3+git180211.000847.1e769869-1
- Update to latest snapshot.

* Sat Feb 03 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.3+git180203.000646.df6c497f-1
- Update to latest snapshot.

* Thu Feb 01 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.3+git180201.000921.90a803fe-1
- Update to latest snapshot.

* Wed Jan 31 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.3+git180131.000944.a8b6d65d-1
- Update to latest snapshot.

* Tue Jan 30 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.3+git180130.142127.d53e8369-1
- Update to latest snapshot.

* Mon Jan 29 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.3+git180129.175630.a5d04db7-1
- Update to latest snapshot.

* Mon Jan 29 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.3+git180129.000238.4febb8d8-1
- Update to latest snapshot.

* Sun Jan 28 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.3+git180128.201228.d1a47e57-1
- Update to latest snapshot.

* Sun Jan 28 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.3+git180128.111747.28f52106-1
- Update to latest snapshot.

* Sun Jan 28 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.3+git180128.053700.a0c64ff4-1
- Update to latest snapshot.

* Sat Jan 27 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.3+git180127.221806.0ba7b9cc-1
- Update to latest snapshot.

* Sat Jan 27 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.3+git180127.213622.8d496160-1
- Update to latest snapshot.

* Thu Jan 04 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.3+git171219.192024.6e16c70c-2
- Merge .spec file from elementary-stable.

* Tue Dec 19 2017 Fabio Valentini <decathorpe@gmail.com> - 0.2.3+git171219.192024.6e16c70c-1
- Update to latest snapshot.

* Mon Aug 14 2017 Fabio Valentini <decathorpe@gmail.com> - 0.2.3+git170814.163340.086807f3-1
- Update to latest snapshot.

* Sun Aug 13 2017 Fabio Valentini <decathorpe@gmail.com> - 0.2.3+git170813.153855.b4a2d7f9-1
- Update to latest snapshot.

* Sat Aug 12 2017 Fabio Valentini <decathorpe@gmail.com> - 0.2.3+git170811.180121.cdc28d92-1
- Update to latest snapshot.

* Wed Aug 09 2017 Fabio Valentini <decathorpe@gmail.com> - 0.2.3+git170808.221018.3b365b80-1
- Update to latest snapshot.

* Mon Jul 10 2017 Fabio Valentini <decathorpe@gmail.com> - 0.2.3+git170710.120718.c4e78781-1
- Update to latest snapshot.

* Sun Jul 02 2017 Fabio Valentini <decathorpe@gmail.com> - 0.2.3+git170702.103137.4c41d70a-1
- Update to latest snapshot.

* Sun Jun 18 2017 Fabio Valentini <decathorpe@gmail.com> - 0.2.3+git170617.152806.e7be9338-1
- Update to latest snapshot.

* Sat Jun 03 2017 Fabio Valentini <decathorpe@gmail.com> - 0.2.3+git170603.093034.7ace420d-1
- Update to latest snapshot.

* Fri May 26 2017 Fabio Valentini <decathorpe@gmail.com> - 0.2.3+git170526.015458.e934568b-1
- Update to latest snapshot.

* Thu May 25 2017 Fabio Valentini <decathorpe@gmail.com> - 0.2.3+git170525.150628.71678239-1
- Update to latest snapshot.

* Thu May 25 2017 Fabio Valentini <decathorpe@gmail.com> - 0.2.3+git170525.145607.ab92cbb8-1
- Update to latest snapshot.

* Mon May 22 2017 Fabio Valentini <decathorpe@gmail.com> - 0.2.3+git170522.201926.743d6cfb-1
- Update to version 0.2.3.

* Mon May 22 2017 Fabio Valentini <decathorpe@gmail.com> - 0.2.2+git170522.201926.743d6cfb-1
- Update to latest snapshot.

* Fri May 12 2017 Fabio Valentini <decathorpe@gmail.com> - 0.2.2+git170512.082701.e6084aec-1
- Update to version 0.2.2.

* Fri May 12 2017 Fabio Valentini <decathorpe@gmail.com> - 0.2.1+rev262-1
- Update to latest snapshot.

* Wed Apr 26 2017 Fabio Valentini <decathorpe@gmail.com> - 0.2.1+rev261-1
- Update to latest snapshot.

* Tue Apr 18 2017 Fabio Valentini <decathorpe@gmail.com> - 0.2.1+rev260-1
- Update to latest snapshot.

* Wed Mar 15 2017 Fabio Valentini <decathorpe@gmail.com> - 0.2.1+rev259-1
- Update to latest snapshot.

* Fri Mar 03 2017 Fabio Valentini <decathorpe@gmail.com> - 0.2.1+rev258-1
- Update to latest snapshot.

* Wed Feb 22 2017 Fabio Valentini <decathorpe@gmail.com> - 0.2.1+rev257-1
- Update to latest snapshot.

* Sat Feb 18 2017 Fabio Valentini <decathorpe@gmail.com> - 0.2.1+rev256-1
- Update to latest snapshot.

* Wed Feb 15 2017 Fabio Valentini <decathorpe@gmail.com> - 0.2.1+rev255-1
- Update to latest snapshot.

* Sun Feb 12 2017 Fabio Valentini <decathorpe@gmail.com> - 0.2.1+rev254-1
- Update to latest snapshot.

* Sat Feb 11 2017 Fabio Valentini <decathorpe@gmail.com> - 0.2.1+rev253-1
- Update to latest snapshot.

* Thu Feb 09 2017 Fabio Valentini <decathorpe@gmail.com> - 0.2.1+rev252-1
- Update to latest snapshot.

* Sat Jan 28 2017 Fabio Valentini <decathorpe@gmail.com> - 0.2.1+rev251-1
- Update to latest snapshot.

* Fri Jan 27 2017 Fabio Valentini <decathorpe@gmail.com> - 0.2.1+rev250-1
- Update to latest snapshot.

* Sat Jan 21 2017 Fabio Valentini <decathorpe@gmail.com> - 0.2.1+rev249-1
- Update to latest snapshot.

* Sat Jan 07 2017 Fabio Valentini <decathorpe@gmail.com> - 0.2.1+rev248-1
- Update to version 0.2.1.

* Fri Jan 06 2017 Fabio Valentini <decathorpe@gmail.com> - 0.2.1+rev247-1
- Update to version 0.2.1.

* Tue Jan 03 2017 Fabio Valentini <decathorpe@gmail.com> - 0.2.1+rev246-1
- Update to version 0.2.1.

* Mon Jan 02 2017 Fabio Valentini <decathorpe@gmail.com> - 0.2.1+rev245-1
- Update to latest snapshot.

* Wed Dec 21 2016 Fabio Valentini <decathorpe@gmail.com> - 0.2.1+rev244-1
- Update to latest snapshot.

* Sat Dec 17 2016 Fabio Valentini <decathorpe@gmail.com> - 0.2.1+rev243-1
- Update to latest snapshot.

* Wed Dec 14 2016 Fabio Valentini <decathorpe@gmail.com> - 0.2.1+rev242-1
- Update to latest snapshot.

* Fri Dec 09 2016 Fabio Valentini <decathorpe@gmail.com> - 0.2.1+rev241-1
- Update to latest snapshot.

* Tue Dec 06 2016 Fabio Valentini <decathorpe@gmail.com> - 0.2.1+rev240-1
- Update to latest snapshot.

* Mon Nov 28 2016 Fabio Valentini <decathorpe@gmail.com> - 0.2.1+rev239-1
- Update to latest snapshot.

* Wed Nov 23 2016 Fabio Valentini <decathorpe@gmail.com> - 0.2.1+rev238-1
- Update to version 0.2.1.


