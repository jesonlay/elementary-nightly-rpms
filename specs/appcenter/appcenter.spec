Name:           appcenter
Summary:        Software Center for the Pantheon desktop
Version:        0.1.3+rev%{rev}
Release:        1%{?dist}
License:        GPLv3
URL:            https://launchpad.net/appcenter

# The tarball is generated from a checkout of the specified branch and
# by executing 'bzr export' and has the usual format
# ('%{name}-%{version}.tar.gz'), where %{version} contains the upstream
# version number with a '+bzr%{rev}' suffix specifying the bzr revision.
Source0:        %{name}-%{version}.tar.gz

# Include the appropriate icon from elementary-icon-theme so appdata metadata generation works.
# A Bug about the missing icon is reported upstream:
# https://bugs.launchpad.net/appcenter/+bug/1658325

Source1:        system-software-install.svg

Source2:        %{name}.conf

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
BuildRequires:  pkgconfig(packagekit-glib2)
BuildRequires:  pkgconfig(unity) >= 4.0.0

Requires:       PackageKit
Requires:       hicolor-icon-theme


%description
Get apps for elementary OS.

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

mkdir -p %{buildroot}/%{_datadir}/icons/hicolor/scalable/apps
cp -p %{SOURCE1} %{buildroot}/%{_datadir}/icons/hicolor/scalable/apps/


%check
desktop-file-validate %{buildroot}/%{_datadir}/applications/org.pantheon.appcenter.desktop
desktop-file-validate %{buildroot}/%{_datadir}/applications/org.pantheon.appcenter-daemon.desktop

appstream-util validate-relax --nonet %{buildroot}/%{_datadir}/appdata/appcenter.appdata.xml


%post
/bin/touch --no-create %{_datadir}/icons/hicolor &>/dev/null || :

%postun
if [ $1 -eq 0 ] ; then
    /bin/touch --no-create %{_datadir}/icons/hicolor &>/dev/null
    /usr/bin/gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :
fi

%posttrans
/usr/bin/gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :


%files -f appcenter.lang
%doc AUTHORS
%license COPYING

%{_bindir}/appcenter

%{_datadir}/appdata/appcenter.appdata.xml
%{_datadir}/applications/org.pantheon.appcenter.desktop
%{_datadir}/applications/org.pantheon.appcenter-daemon.desktop
%{_datadir}/glib-2.0/schemas/org.pantheon.appcenter.gschema.xml
%{_datadir}/icons/hicolor/scalable/apps/system-software-install.svg


%changelog
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


