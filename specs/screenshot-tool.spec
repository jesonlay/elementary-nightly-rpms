Summary:        simple screen capture tool
Name:           screenshot-tool
Version:        0.1.0.3+rev%{rev}
Release:        3%{?dist}
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


