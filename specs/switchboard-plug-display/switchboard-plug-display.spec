%global __provides_exclude_from ^%{_libdir}/switchboard/.*\\.so$

Name:           switchboard-plug-display
Summary:        Switchboard Display plug
Version:        0.1.4+git%{date}.%{commit}
Release:        1%{?dist}
License:        GPLv3+

URL:            https://github.com/elementary/%{name}
Source0:        %{name}-%{version}.tar.gz

BuildRequires:  gettext
BuildRequires:  meson
BuildRequires:  vala >= 0.22.0
BuildRequires:  vala-tools

BuildRequires:  pkgconfig(glib-2.0) >= 2.32
BuildRequires:  pkgconfig(gnome-desktop-3.0)
BuildRequires:  pkgconfig(granite)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(switchboard-2.0)

Supplements:    switchboard%{?_isa}


%description
A switchboard plug to show information about displays and to configure
them.


%prep
%autosetup


%build
%meson
%meson_build


%install
%meson_install

%find_lang display-plug


%files -f display-plug.lang
%doc README.md
%license COPYING

%{_libdir}/switchboard/hardware/libdisplay.so


%changelog
* Wed Aug 15 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.4+git180815.000905.f3c80943-1
- Update to latest snapshot.

* Mon Aug 13 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.4+git180813.000337.6b2c7b66-1
- Update to latest snapshot.

* Thu Jul 26 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.4+git180726.145600.f7c133e1-1
- Update to latest snapshot.

* Sat Jul 21 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.4+git180721.000740.b10dc6d1-1
- Update to latest snapshot.

* Tue Jul 17 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.4+git180717.000314.d18a6ce2-1
- Update to latest snapshot.

* Thu Jul 05 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.4+git180703.193119.89025527-1
- Update to version 0.1.4.

* Wed Jul 04 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.3+git180703.193119.89025527-1
- Update to latest snapshot.

* Wed Jun 13 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.3+git180613.165855.7bc152b7-1
- Update to latest snapshot.

* Thu Jun 07 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.3+git180607.000931.a19f7e6e-1
- Update to latest snapshot.

* Wed Jun 06 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.3+git180606.060231.48a99ca6-1
- Update to latest snapshot.

* Mon Jun 04 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.3+git180604.024152.42f033e7-1
- Update to latest snapshot.

* Sun Jun 03 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.3+git180603.175644.a69189ec-1
- Update to latest snapshot.

* Sat Jun 02 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.3+git180602.195324.7d209e13-1
- Update to latest snapshot.

* Sat Jun 02 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.3+git180602.000609.c56775e4-1
- Update to latest snapshot.

* Fri Jun 01 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.3+git180601.144706.fc0f0e7d-1
- Update to latest snapshot.

* Fri Jun 01 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.3+git180601.000755.5c2da170-1
- Update to latest snapshot.

* Thu May 31 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.3+git180531.055228.e5a31d64-1
- Update to latest snapshot.

* Wed May 30 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.3+git180530.124905.ab4cc85f-1
- Update to latest snapshot.

* Wed May 30 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.3+git180530.091446.8dbe64ad-1
- Update to latest snapshot.

* Tue May 29 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.3+git180529.151558.85e9391f-1
- Update to latest snapshot.
- Adapt to upstream file changes.

* Tue May 29 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.3+git180529.135235.f529c00e-1
- Update to latest snapshot.

* Mon May 28 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.3+git180527.215947.1904f252-1
- Update to latest snapshot.

* Sun May 27 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.3+git180527.130035.d34d9299-1
- Update to latest snapshot.

* Fri May 11 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.3+git180511.000618.680fcff9-1
- Update to latest snapshot.

* Sun May 06 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.3+git180504.000617.52cd5adb-1
- Update to latest snapshot.

* Tue May 01 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.3+git180429.142436.619d74f3-1
- Update to latest snapshot.

* Thu Apr 26 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.3+git180426.000335.ed966e11-1
- Update to latest snapshot.

* Wed Apr 25 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.3+git180425.000334.d06d42ca-1
- Update to latest snapshot.

* Tue Apr 03 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.3+git180401.000515.d7ab9837-1
- Update to latest snapshot.

* Tue Mar 27 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.3+git180327.000223.e521da68-1
- Update to latest snapshot.

* Fri Feb 23 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.3+git180223.182919.ea629027-1
- Update to latest snapshot.

* Wed Feb 14 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.3+git180214.203405.5c5bed71-1
- Update to latest snapshot.

* Wed Feb 07 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.3+git180207.033038.6445598e-1
- Update to latest snapshot.

* Mon Feb 05 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.3+git180205.001145.6b4b5606-1
- Update to latest snapshot.

* Mon Jan 22 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.3+git180122.145550.97de7c27-1
- Update to latest snapshot.

* Thu Jan 04 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.3+git180102.234041.dfaae03c-2
- Merge .spec file from fedora.

* Wed Jan 03 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.3+git180102.234041.dfaae03c-1
- Update to latest snapshot.

* Wed Dec 27 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.3+git171227.174638.840d2ee7-1
- Update to latest snapshot.

* Thu Dec 14 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.3+git171214.173931.79d16a7c-1
- Update to latest snapshot.

* Wed Dec 13 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.3+git171213.051138.523f92a1-1
- Update to latest snapshot.

* Tue Dec 12 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.3+git171212.023220.c3c00ba1-1
- Update to latest snapshot.

* Mon Dec 11 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.3+git171211.224020.178cdcf4-1
- Update to latest snapshot.

* Mon Nov 20 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.3+git171118.231526.4c968719-1
- Update to latest snapshot.

* Sat Oct 28 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.3+git171027.230155.ae79a6e3-1
- Update to latest snapshot.

* Sat Sep 23 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.3+git170923.185520.f18dcb95-1
- Update to latest snapshot.

* Sat Aug 19 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.3+git170817.000741.268df478-1
- Update to latest snapshot.

* Wed Jul 12 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.3+git170712.005905.92447c2c-1
- Update to latest snapshot.

* Sun Jul 02 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.3+git170702.180402.110a28c0-1
- Update to latest snapshot.

* Sun Jun 18 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.3+git170617.152617.418671fe-1
- Update to latest snapshot.

* Sat Jun 03 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.3+git170603.092900.3f52803d-1
- Update to latest snapshot.

* Wed May 03 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.3+git170502.152618.00cc5a7d-1
- Update to version 0.1.3.

* Tue May 02 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.2.1+rev192-1
- Update to latest snapshot.

* Wed Apr 26 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.2.1+rev191-1
- Update to latest snapshot.

* Wed Mar 22 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.2.1+rev189-1
- Update to latest snapshot.

* Wed Mar 15 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.2.1+rev188-1
- Update to latest snapshot.

* Thu Feb 23 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.2.1+rev187-1
- Update to latest snapshot.

* Wed Feb 22 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.2.1+rev186-1
- Update to latest snapshot.

* Sat Feb 18 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.2.1+rev185-1
- Update to latest snapshot.

* Wed Feb 15 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.2.1+rev184-1
- Update to latest snapshot.

* Sun Jan 29 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.2.1+rev183-1
- Update to latest snapshot.

* Sat Jan 28 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.2.1+rev182-1
- Update to latest snapshot.

* Tue Jan 17 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.2.1+rev181-1
- Update to latest snapshot.

* Sat Jan 07 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.2.1+rev180-1
- Update to version 0.1.2.1.

* Fri Jan 06 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.2.1+rev179-1
- Update to version 0.1.2.1.

* Tue Jan 03 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.2.1+rev178-1
- Update to version 0.1.2.1.

* Mon Jan 02 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.2.1+rev177-1
- Update to latest snapshot.

* Thu Dec 22 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.2.1+rev176-1
- Update to latest snapshot.

* Wed Dec 14 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.2.1+rev175-1
- Update to latest snapshot.

* Wed Nov 23 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.2.1+rev174-1
- Update to version 0.1.2.1.


