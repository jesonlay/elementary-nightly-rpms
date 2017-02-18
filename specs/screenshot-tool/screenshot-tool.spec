Summary:        simple screen capture tool
Name:           screenshot-tool
Version:        0.1.1+rev%{rev}
Release:        1%{?dist}
License:        GPLv3
URL:            http://launchpad.net/screenshot-tool

Source0:        %{name}-%{version}.tar.gz
Source1:        %{name}.conf

BuildRequires:  cmake
BuildRequires:  desktop-file-utils
BuildRequires:  gettext
BuildRequires:  intltool
BuildRequires:  libappstream-glib
BuildRequires:  pkgconfig
BuildRequires:  vala >= 0.24
BuildRequires:  vala-tools

BuildRequires:  pkgconfig(gdk-pixbuf-2.0)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(granite)
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.12


%description
A simple screen capture tool made for elementary OS.


%prep
%autosetup


%build
%cmake
%make_build


%install
%make_install
%find_lang screenshot-tool


%check
desktop-file-validate %{buildroot}/%{_datadir}/applications/*.desktop
appstream-util validate-relax --nonet %{buildroot}/%{_datadir}/appdata/*.appdata.xml


%clean
rm -rf %{buildroot}


%files -f screenshot-tool.lang
%{_bindir}/screenshot-tool

%{_datadir}/appdata/screenshot-tool.appdata.xml
%{_datadir}/applications/screenshot-tool.desktop
%{_datadir}/glib-2.0/schemas/net.launchpad.screenshot.gschema.xml


%changelog
* Sat Feb 18 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+rev300-1
- Update to latest snapshot.

* Fri Feb 17 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+rev298-1
- Update to latest snapshot.

* Thu Feb 16 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+rev297-1
- Update to latest snapshot.

* Wed Feb 15 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+rev295-1
- Update to latest snapshot.

* Mon Feb 13 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+rev294-1
- Update to latest snapshot.

* Sun Feb 12 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+rev293-1
- Update to latest snapshot.

* Sun Feb 12 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+rev292-1
- Update to latest snapshot.

* Sat Feb 11 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+rev291-1
- Update to latest snapshot.

* Thu Feb 09 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+rev289-1
- Update to latest snapshot.

* Tue Feb 07 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+rev288-1
- Update to latest snapshot.

* Mon Feb 06 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+rev287-1
- Update to latest snapshot.

* Sun Feb 05 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+rev286-1
- Update to latest snapshot.

* Sun Feb 05 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+rev285-1
- Update to latest snapshot.

* Sat Feb 04 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+rev284-1
- Update to latest snapshot.

* Fri Feb 03 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+rev283-1
- Update to latest snapshot.

* Fri Feb 03 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+rev282-1
- Update to latest snapshot.

* Fri Feb 03 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+rev280-1
- Update to latest snapshot.

* Thu Feb 02 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+rev279-1
- Update to latest snapshot.

* Tue Jan 31 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+rev278-1
- Update to latest snapshot.

* Mon Jan 30 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+rev277-1
- Update to latest snapshot.

* Sun Jan 29 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+rev276-1
- Update to latest snapshot.

* Sat Jan 28 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+rev275-1
- Update to latest snapshot.

* Fri Jan 27 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+rev274-1
- Update to latest snapshot.

* Thu Jan 26 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+rev273-1
- Update to latest snapshot.

* Tue Jan 24 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+rev272-1
- Update to latest snapshot.

* Sun Jan 22 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+rev271-1
- Update to latest snapshot.

* Sat Jan 21 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+rev270-1
- Update to latest snapshot.

* Sun Jan 08 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+rev269-1
- Update to version 0.1.1.

* Sat Jan 07 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+rev268-1
- Update to version 0.1.1.

* Sun Jan 01 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+rev267-1
- Update to latest snapshot.

* Sat Dec 31 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+rev266-1
- Update to latest snapshot.

* Wed Dec 21 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+rev265-1
- Update to latest snapshot.

* Tue Dec 20 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+rev264-1
- Update to latest snapshot.

* Sat Dec 17 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+rev263-1
- Update to latest snapshot.

* Fri Dec 16 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+rev262-1
- Update to latest snapshot.

* Thu Dec 15 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+rev261-1
- Update to latest snapshot.

* Wed Dec 14 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+rev260-1
- Update to latest snapshot.

* Tue Dec 13 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+rev259-1
- Update to latest snapshot.

* Thu Dec 08 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+rev258-1
- Update to latest snapshot.

* Sun Dec 04 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+rev257-1
- Update to latest snapshot.

* Fri Dec 02 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+rev256-1
- Update to latest snapshot.

* Sat Nov 26 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+rev255-1
- Update to latest snapshot.

* Thu Nov 24 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+rev254-1
- Update to version 0.1.1.

* Thu Nov 24 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.3+rev254-1
- Update to latest snapshot.

* Wed Nov 23 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.3+rev253-1
- Update to latest snapshot.

* Tue Nov 22 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.3+rev252-1
- Update to latest snapshot.

* Tue Nov 15 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.3+rev251-1
- Update to latest snapshot.

* Mon Nov 14 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.3+rev250-1
- Update to latest snapshot.

* Sun Nov 13 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.3+rev249-1
- Update to latest snapshot.

* Sun Nov 13 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.3+rev248-1
- Update to latest snapshot.

* Sat Oct 22 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.3+rev247-1
- Update to latest snapshot.

* Fri Oct 21 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.3+rev246-1
- Update to latest snapshot.

* Mon Oct 17 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.3+rev245-1
- Update to latest snapshot.

* Sun Oct 16 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.3+rev244-1
- Update to latest snapshot.

* Sat Oct 15 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.3+rev243-1
- Update to latest snapshot.

* Fri Oct 14 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.3+rev242-1
- Update to latest snapshot.

* Thu Oct 13 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.3+rev241-1
- Update to latest snapshot.

* Wed Oct 12 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.3+rev240-1
- Update to latest snapshot.

* Tue Oct 11 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.3+rev239-1
- Update to latest snapshot.

* Sat Oct 08 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.3+rev238-1
- Update to latest snapshot.

* Fri Oct 07 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.3+rev237-1
- Update to latest snapshot.

* Sat Oct 01 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.3+rev234-1
- Update to latest snapshot.

* Thu Sep 29 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.3+rev233-1
- Update to latest snapshot.

* Thu Sep 29 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.3+rev232-3
- Fix build by adding missing BR: libappstream-glib.

* Thu Sep 29 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.3+rev232-2
- Spec file cleanups.

* Thu Sep 29 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.3+rev232-1
- Update to latest snapshot.

* Wed Sep 28 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.3+rev231-3
- Also add missing BR: desktop-file-utils.

* Wed Sep 28 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.3+rev231-2
- Add BR: intltool to hopefully fix f25 build.

* Wed Sep 28 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.3+rev231-1
- Update to version 0.1.0.3.

* Wed Sep 28 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.2+rev231-1
- Update to latest snapshot.

* Fri Sep 23 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.2+rev228-1
- Update to latest snapshot.

* Thu Sep 22 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.2+rev227-1
- Update to version 0.1.0.2.

* Wed Sep 14 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.2~rev226-1
- Update to latest snapshot.

* Tue Sep 13 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.2~rev225-1
- Update to version 0.1.0.2.

* Mon Sep 12 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.1~rev224-1
- Update to latest snapshot.

* Sun Sep 11 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.1~rev223-1
- Update to latest snapshot.

* Sat Sep 10 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.1~rev221-1
- Update to version 0.1.0.1.

* Wed Sep 07 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev220-1
- Update to latest snapshot.

* Sat Sep 03 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev219-1
- Update to latest snapshot.

* Sun Aug 28 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev218-1
- Update to latest snapshot.

* Sat Aug 27 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev217-1
- Update to latest snapshot.

* Sun Aug 14 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev216-1
- Update to version 0.1.

* Sun Aug 14 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1-1
- Update to version 0.1.


