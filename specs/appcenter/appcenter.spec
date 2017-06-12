Name:           appcenter
Summary:        Software Center for the Pantheon desktop
Version:        0.2.3+git%{date}.%{commit}
Release:        1%{?dist}
License:        GPLv3
URL:            https://launchpad.net/appcenter

Source0:        %{name}-%{version}.tar.gz
Source1:        %{name}.conf

BuildRequires:  cmake
BuildRequires:  cmake-elementary
BuildRequires:  desktop-file-utils
BuildRequires:  gettext
BuildRequires:  intltool
BuildRequires:  libappstream-glib
BuildRequires:  vala >= 0.26

BuildRequires:  appstream-vala

BuildRequires:  pkgconfig(appstream) >= 0.10.0
BuildRequires:  pkgconfig(gee-0.8)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(granite)
BuildRequires:  pkgconfig(gthread-2.0)
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.10
BuildRequires:  pkgconfig(json-glib-1.0)
BuildRequires:  pkgconfig(libsoup-2.4)
BuildRequires:  pkgconfig(packagekit-glib2)
BuildRequires:  pkgconfig(unity) >= 4.0.0

Requires:       PackageKit
Requires:       hicolor-icon-theme


%description
AppCenter is a native Gtk+ app store built on AppStream and Packagekit.


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

%find_lang appcenter

# move appdata to approved location
mv %{buildroot}/%{_datadir}/metainfo %{buildroot}/%{_datadir}/appdata


%check
desktop-file-validate %{buildroot}/%{_datadir}/applications/io.elementary.appcenter.desktop
desktop-file-validate %{buildroot}/%{_datadir}/applications/io.elementary.appcenter-daemon.desktop

appstream-util validate-relax --nonet %{buildroot}/%{_datadir}/appdata/appcenter.appdata.xml


%files -f appcenter.lang
%doc AUTHORS
%license COPYING

%{_bindir}/appcenter

%{_datadir}/appdata/appcenter.appdata.xml
%{_datadir}/applications/io.elementary.appcenter.desktop
%{_datadir}/applications/io.elementary.appcenter-daemon.desktop
%{_datadir}/glib-2.0/schemas/io.elementary.appcenter.gschema.xml


%changelog
* Mon Jun 12 2017 Fabio Valentini <decathorpe@gmail.com> - 0.2.3+git170612.165127.7f4cf6a7-1
- Update to latest snapshot.

* Thu Jun 08 2017 Fabio Valentini <decathorpe@gmail.com> - 0.2.3+git170607.162037.dfeda7bb-1
- Update to latest snapshot.

* Thu Jun 01 2017 Fabio Valentini <decathorpe@gmail.com> - 0.2.3+git170531.221524.125e08de-1
- Update to version 0.2.3.

* Thu Jun 01 2017 Fabio Valentini <decathorpe@gmail.com> - 0.2.2+git170531.221524.125e08de-1
- Update to latest snapshot.

* Tue May 30 2017 Fabio Valentini <decathorpe@gmail.com> - 0.2.2+git170530.015919.616ab29a-1
- Update to latest snapshot.

* Sat May 27 2017 Fabio Valentini <decathorpe@gmail.com> - 0.2.2+git170527.161220.d0507512-1
- Update to latest snapshot.

* Fri May 26 2017 Fabio Valentini <decathorpe@gmail.com> - 0.2.2+git170526.014646.7b3948b0-1
- Update to latest snapshot.

* Thu May 25 2017 Fabio Valentini <decathorpe@gmail.com> - 0.2.2+git170525.173221.baa7a2f0-1
- Update to latest snapshot.

* Thu May 25 2017 Fabio Valentini <decathorpe@gmail.com> - 0.2.2+git170525.153047.6e2bc083-1
- Update to latest snapshot.

* Wed May 24 2017 Fabio Valentini <decathorpe@gmail.com> - 0.2.2+git170523.211034.125f06aa-1
- Update to latest snapshot.

* Tue May 23 2017 Fabio Valentini <decathorpe@gmail.com> - 0.2.2+git170523.072723.789f1fdf-1
- Update to latest snapshot.

* Mon May 22 2017 Fabio Valentini <decathorpe@gmail.com> - 0.2.2+git170522.152445.73b8f3b7-1
- Update to version 0.2.2.

* Mon May 22 2017 Fabio Valentini <decathorpe@gmail.com> - 0.2.1+git170522.152445.73b8f3b7-1
- Update to latest snapshot.

* Mon May 22 2017 Fabio Valentini <decathorpe@gmail.com> - 0.2.1+git170522.061740.586c1690-1
- Update to latest snapshot.

* Sun May 21 2017 Fabio Valentini <decathorpe@gmail.com> - 0.2.1+git170521.214503.dfefe9d8-1
- Update to latest snapshot.

* Sun May 21 2017 Fabio Valentini <decathorpe@gmail.com> - 0.2.1+git170521.161028.fb2287e5-1
- Update to latest snapshot.

* Sat May 20 2017 Fabio Valentini <decathorpe@gmail.com> - 0.2.1+git170520.165836.1598debe-1
- Update to version 0.2.1.

* Sat May 20 2017 Fabio Valentini <decathorpe@gmail.com> - 0.2+git170520.165836.1598debe-1
- Update to latest snapshot.

* Sat May 20 2017 Fabio Valentini <decathorpe@gmail.com> - 0.2+git170520.145331.f89bc0bb-1
- Update to latest snapshot.

* Sat May 20 2017 Fabio Valentini <decathorpe@gmail.com> - 0.2+git170520.023328.c45c11ee-1
- Update to latest snapshot.

* Fri May 19 2017 Fabio Valentini <decathorpe@gmail.com> - 0.2+git170519.193742.00c3fe0f-1
- Update to latest snapshot.

* Thu May 18 2017 Fabio Valentini <decathorpe@gmail.com> - 0.2+git170518.142122.a1f3e3f5-1
- Update to latest snapshot.

* Thu May 18 2017 Fabio Valentini <decathorpe@gmail.com> - 0.2+git170517.113513.8e5c70f9-1
- Update to version 0.2.

* Wed May 17 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.4+rev628-1
- Update to latest snapshot.

* Wed May 17 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.4+rev627-1
- Update to latest snapshot.

* Tue May 16 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.4+rev623-1
- Update to latest snapshot.

* Tue May 09 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.4+rev621-1
- Update to latest snapshot.

* Sun May 07 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.4+rev658-1
- Update to latest snapshot.

* Sun May 07 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.4+rev651-1
- Update to latest snapshot.

* Fri May 05 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.4+rev650-1
- Update to latest snapshot.

* Sun Apr 30 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.4+rev592-1
- Update to latest snapshot.

* Thu Apr 27 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.4+rev591-1
- Update to latest snapshot.

* Tue Apr 25 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.4+rev588-1
- Update to latest snapshot.

* Fri Apr 21 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.4+rev587-1
- Update to latest snapshot.

* Fri Apr 21 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.4+rev585-1
- Update to latest snapshot.

* Tue Apr 18 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.4+rev584-1
- Update to latest snapshot.

* Sun Apr 16 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.4+rev583-1
- Update to latest snapshot.

* Sun Apr 16 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.4+rev582-1
- Update to latest snapshot.

* Sat Apr 15 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.4+rev581-1
- Update to latest snapshot.

* Sat Apr 15 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.4+rev580-1
- Update to latest snapshot.

* Tue Apr 11 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.4+rev564-1
- Update to latest snapshot.

* Mon Apr 10 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.4+rev557-1
- Update to latest snapshot.

* Mon Apr 10 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.4+rev555-1
- Update to latest snapshot.

* Sun Apr 09 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.4+rev538-1
- Update to latest snapshot.

* Sun Apr 09 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.4+rev535-1
- Update to latest snapshot.

* Sun Apr 09 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.4+rev525-1
- Update to latest snapshot.

* Sat Apr 08 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.4+rev509-1
- Update to latest snapshot.

* Sat Apr 08 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.4+rev501-1
- Update to latest snapshot.

* Sat Apr 08 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.4+rev481-1
- Update to latest snapshot.

* Fri Apr 07 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.4+rev477-1
- Update to latest snapshot.

* Fri Apr 07 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.4+rev475-1
- Update to latest snapshot.

* Thu Apr 06 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.4+rev471-1
- Update to latest snapshot.

* Tue Apr 04 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.4+rev466-1
- Update to latest snapshot.

* Mon Apr 03 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.4+rev464-1
- Update to latest snapshot.

* Sat Apr 01 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.4+rev456-1
- Update to latest snapshot.

* Thu Mar 30 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.4+rev454-1
- Update to latest snapshot.

* Thu Mar 30 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.4+rev452-1
- Update to latest snapshot.

* Thu Mar 30 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.4+rev448-1
- Update to latest snapshot.

* Wed Mar 29 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.4+rev446-1
- Update to latest snapshot.

* Tue Mar 28 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.4+rev445-2
- Adapt to upstream file name changes.

* Tue Mar 28 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.4+rev445-1
- Update to latest snapshot.

* Mon Mar 27 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.4+rev444-1
- Update to latest snapshot.

* Sun Mar 26 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.4+rev443-1
- Update to latest snapshot.

* Sun Mar 26 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.4+rev441-1
- Update to latest snapshot.

* Wed Mar 22 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.4+rev437-1
- Update to latest snapshot.

* Wed Mar 22 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.4+rev433-1
- Update to latest snapshot.

* Tue Mar 21 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.4+rev431-1
- Update to latest snapshot.

* Tue Mar 21 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.4+rev430-2
- Add new missing BRs json-glib and libsoup.

* Tue Mar 21 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.4+rev430-1
- Update to latest snapshot.

* Thu Mar 16 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.4+rev415-1
- Update to version 0.1.4.

* Thu Mar 16 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.3+rev415-1
- Update to latest snapshot.

* Thu Mar 16 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.3+rev414-1
- Update to latest snapshot.

* Wed Mar 15 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.3+rev413-1
- Update to latest snapshot.

* Tue Mar 14 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.3+rev412-1
- Update to latest snapshot.

* Thu Mar 09 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.3+rev411-1
- Update to latest snapshot.

* Wed Mar 08 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.3+rev410-2
- Move appdata to approved location.

* Tue Mar 07 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.3+rev410-1
- Update to latest snapshot.

* Thu Mar 02 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.3+rev409-1
- Update to latest snapshot.

* Tue Feb 28 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.3+rev408-1
- Update to latest snapshot.

* Mon Feb 27 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.3+rev407-1
- Update to latest snapshot.

* Sat Feb 25 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.3+rev406-1
- Update to latest snapshot.

* Mon Feb 20 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.3+rev405-1
- Update to latest snapshot.

* Mon Feb 20 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.3+rev404-1
- Update to latest snapshot.

* Sat Feb 18 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.3+rev403-1
- Update to latest snapshot.

* Sat Feb 18 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.3+rev402-1
- Update to latest snapshot.

* Thu Feb 16 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.3+rev401-1
- Update to latest snapshot.

* Wed Feb 15 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.3+rev400-1
- Update to latest snapshot.

* Mon Feb 13 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.3+rev399-1
- Update to latest snapshot.

* Sun Feb 12 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.3+rev398-1
- Update to latest snapshot.

* Sat Feb 11 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.3+rev397-1
- Update to latest snapshot.

* Fri Feb 10 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.3+rev394-1
- Update to latest snapshot.

* Thu Feb 09 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.3+rev393-1
- Update to latest snapshot.

* Mon Feb 06 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.3+rev392-1
- Update to latest snapshot.

* Sun Feb 05 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.3+rev391-1
- Update to latest snapshot.

* Sat Feb 04 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.3+rev390-1
- Update to latest snapshot.

* Thu Feb 02 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.3+rev388-1
- Update to latest snapshot.

* Mon Jan 30 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.3+rev387-1
- Update to latest snapshot.

* Sun Jan 29 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.3+rev386-1
- Update to latest snapshot.

* Sat Jan 28 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.3+rev385-1
- Update to latest snapshot.

* Fri Jan 27 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.3+rev384-1
- Update to latest snapshot.

* Thu Jan 26 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.3+rev383-2
- Sync with fedora packaging.

* Thu Jan 26 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.3+rev383-1
- Update to latest snapshot.

* Wed Jan 25 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.3+rev382-1
- Update to latest snapshot.

* Tue Jan 24 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.3+rev381-1
- Update to latest snapshot.

* Mon Jan 23 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.3+rev379-1
- Update to latest snapshot.

* Sat Jan 21 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.3+rev378-1
- Update to latest snapshot.

* Thu Jan 19 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.3+rev377-1
- Update to latest snapshot.

* Wed Jan 18 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.3+rev376-1
- Update to latest snapshot.

* Tue Jan 17 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.3+rev375-1
- Update to latest snapshot.

* Thu Jan 12 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.3+rev374-1
- Update to latest snapshot.

* Wed Jan 11 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.3+rev373-1
- Update to latest snapshot.

* Tue Jan 10 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.3+rev372-1
- Update to latest snapshot.

* Mon Jan 09 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.3+rev371-1
- Update to latest snapshot.

* Sun Jan 08 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.3+rev370-1
- Update to latest snapshot.

* Sat Jan 07 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.3+rev369-1
- Update to latest snapshot.

* Fri Jan 06 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.3+rev368-1
- Update to latest snapshot.

* Wed Jan 04 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.3+rev367-1
- Update to latest snapshot.

* Tue Jan 03 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.3+rev366-1
- Update to latest snapshot.

* Mon Jan 02 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.3+rev365-1
- Update to latest snapshot.

* Sun Jan 01 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.3+rev364-1
- Update to latest snapshot.

* Sat Dec 31 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.3+rev362-1
- Update to latest snapshot.

* Fri Dec 30 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.3+rev361-1
- Update to latest snapshot.

* Wed Dec 28 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.3+rev358-1
- Update to latest snapshot.

* Tue Dec 27 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.3+rev355-1
- Update to latest snapshot.

* Sat Dec 24 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.3+rev354-2
- Enable libunity support.

* Thu Dec 22 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.3+rev354-1
- Update to latest snapshot.

* Wed Dec 21 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.3+rev353-1
- Update to latest snapshot.

* Sun Dec 18 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.3+rev352-1
- Update to latest snapshot.

* Sat Dec 17 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.3+rev351-1
- Update to latest snapshot.

* Fri Dec 09 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.3+rev350-1
- Update to latest snapshot.

* Thu Dec 08 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.3+rev349-1
- Update to latest snapshot.

* Wed Dec 07 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.3+rev348-1
- Update to latest snapshot.

* Tue Dec 06 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.3+rev347-1
- Update to latest snapshot.

* Mon Dec 05 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.3+rev346-1
- Update to version 0.1.3.

* Mon Dec 05 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+rev346-1
- Update to latest snapshot.

* Sun Dec 04 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+rev344-1
- Update to latest snapshot.

* Fri Dec 02 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+rev343-1
- Update to latest snapshot.

* Fri Dec 02 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+rev342-1
- Update to latest snapshot.

* Fri Nov 25 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+rev341-1
- Update to latest snapshot.

* Wed Nov 23 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+rev340-1
- Update to latest snapshot.

* Tue Nov 22 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+rev339-1
- Update to latest snapshot.

* Sun Nov 20 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+rev338-1
- Update to latest snapshot.

* Fri Nov 18 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+rev337-1
- Update to latest snapshot.

* Wed Nov 16 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+rev336-1
- Update to latest snapshot.

* Mon Nov 07 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+rev335-1
- Update to latest snapshot.

* Sun Nov 06 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+rev334-1
- Update to latest snapshot.

* Sat Nov 05 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+rev333-1
- Update to latest snapshot.

* Fri Nov 04 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+rev332-1
- Update to latest snapshot.

* Tue Nov 01 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+rev331-1
- Update to latest snapshot.

* Sat Oct 29 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+rev330-1
- Update to latest snapshot.

* Fri Oct 28 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+rev329-1
- Update to latest snapshot.

* Thu Oct 27 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+rev328-2
- Remove patch. Only build on f25 now.

* Wed Oct 26 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+rev328-1
- Update to latest snapshot.

* Sun Oct 23 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+rev327-1
- Update to latest snapshot.

* Sat Oct 22 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+rev326-1
- Update to latest snapshot.

* Fri Oct 21 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+rev325-1
- Update to latest snapshot.

* Mon Oct 17 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+rev324-1
- Update to latest snapshot.

* Sun Oct 16 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+rev323-1
- Update to latest snapshot.

* Sat Oct 15 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+rev322-1
- Update to version 0.1.1.


