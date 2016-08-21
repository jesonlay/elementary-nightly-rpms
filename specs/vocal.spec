Summary:        Vocal Podcatcher
Name:           vocal
Version:        2.0~git%{date}~%{rev}
Release:        1%{?dist}
License:        GPLv3
URL:            http://launchpad.net/vocal

Source0:        %{name}-%{version}.tar.gz
Source1:        %{name}.conf

Patch0:         00-webkitdeps.patch

BuildRequires:  cmake
BuildRequires:  desktop-file-utils
BuildRequires:  gettext
BuildRequires:  intltool
BuildRequires:  libappstream-glib
BuildRequires:  pkgconfig
BuildRequires:  vala

BuildRequires:  pkgconfig(clutter-gst-3.0)
BuildRequires:  pkgconfig(clutter-gtk-1.0)
BuildRequires:  pkgconfig(gee-0.8)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(granite)
BuildRequires:  pkgconfig(gstreamer-1.0)
BuildRequires:  pkgconfig(gstreamer-pbutils-1.0)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(json-glib-1.0)
BuildRequires:  pkgconfig(libnotify)
BuildRequires:  pkgconfig(libsoup-2.4)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(sqlite3)
BuildRequires:  pkgconfig(webkit2gtk-4.0)

Requires:       hicolor-icon-theme


%description
Vocal is a podcatcher designed for elementaryOS.


%prep
%autosetup


%build
%cmake
%make_build


%install
%make_install

mv %{buildroot}/%{_datadir}/locale-langpack %{buildroot}/%{_datadir}/locale

%find_lang vocal


%check
desktop-file-validate %{buildroot}/%{_datadir}/applications/vocal.desktop

# appstream-util validate-relax --nonet %{buildroot}/%{_datadir}/appdata/*.appdata.xml


%clean
rm -rf %{buildroot}


%post
/usr/bin/update-desktop-database &> /dev/null || :
/bin/touch --no-create %{_datadir}/icons/hicolor &>/dev/null || :

%postun
/usr/bin/update-desktop-database &> /dev/null || :
if [ $1 -eq 0 ] ; then
    /usr/bin/glib-compile-schemas %{_datadir}/glib-2.0/schemas &> /dev/null || :
    /bin/touch --no-create %{_datadir}/icons/hicolor &>/dev/null
    /usr/bin/gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :
fi

%posttrans
/usr/bin/glib-compile-schemas %{_datadir}/glib-2.0/schemas &> /dev/null || :
/usr/bin/gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :


%files -f vocal.lang
%doc AUTHORS README.md
%license COPYING

%{_bindir}/vocal

%{_datadir}/appdata/vocal.desktop.appdata.xml
%{_datadir}/applications/vocal.desktop
%{_datadir}/glib-2.0/schemas/net.launchpad.vocal.gschema.xml
%{_datadir}/icons/hicolor/*/apps/vocal.svg
%{_datadir}/icons/hicolor/*/apps/vocal-symbolic.svg
%{_datadir}/vocal


%changelog
* Sun Aug 21 2016 Fabio Valentini <decathorpe@gmail.com> - 2.0~git160821.115944~f0be5cb9-1
- Update to latest snapshot.

* Wed Aug 17 2016 Fabio Valentini <decathorpe@gmail.com> - 2.0~git160717.205159~c1578ed5-3
- Update for packaging changes.

* Sun Aug 07 2016 Fabio Valentini <decathorpe@gmail.com>
- Add BR: intltool.

* Sun Aug 07 2016 Fabio Valentini <decathorpe@gmail.com> - 2.0~git160717.205159~c1578ed5-2
- Update for packaging changes.

* Mon Jul 18 2016 Fabio Valentini <decathorpe@gmail.com> - 2.0~git160717.205159~c1578ed5-1
- Update to latest snapshot.

* Sat Jul 09 2016 Fabio Valentini <decathorpe@gmail.com> - 2.0~git160708.223110~f3e10a7a-1
- Update to latest snapshot.

* Wed Jul 06 2016 Fabio Valentini <decathorpe@gmail.com> - 2.0~git160605.162430~2f421206-2
- Update for packaging changes.

* Sun Jun 05 2016 Fabio Valentini <decathorpe@gmail.com> - 2.0~git160605.162430~2f421206-1
- Update to latest snapshot.

* Sun Jun 05 2016 Fabio Valentini <decathorpe@gmail.com> - 2.0~git160605.141839~bf964015-1
- Update to latest snapshot.

* Mon May 30 2016 Fabio Valentini <decathorpe@gmail.com> - 2.0~git160528.151223~88581fc1-3
- Update for packaging changes.

* Sun May 29 2016 Fabio Valentini <decathorpe@gmail.com> - 2.0~git160528.151223~88581fc1-2
- Update for packaging changes.

* Sat May 28 2016 Fabio Valentini <decathorpe@gmail.com> - 2.0~git160528.151223~88581fc1-1
- Update to latest snapshot.

* Tue May 24 2016 Fabio Valentini <decathorpe@gmail.com> - 2.0~git160524.094634~b7329b0f-1
- Update to latest snapshot.

* Wed May 04 2016 Fabio Valentini <decathorpe@gmail.com> - 2.0~git160417.205452~951a90c2-1
- Update to latest snapshot.

* Mon Apr 18 2016 Fabio Valentini <decathorpe@gmail.com> - 2.0~git160418~951a90c2-1
- Update to new upstream snapshot.

* Fri Mar 25 2016 Fabio Valentini <decathorpe@gmail.com> - 2.0~git160325~98398fff-1
- Update to new upstream snapshot.

* Sun Mar 13 2016 Fabio Valentini <decathorpe@gmail.com> - 2.0~git160313~13a99508-3
- Add BR: clutter-gst-3.0.

* Sun Mar 13 2016 Fabio Valentini <decathorpe@gmail.com> - 2.0~git160308~a5b01d25-2
- Renew patch for webkitgtk2-4.0

* Tue Mar 08 2016 Fabio Valentini <decathorpe@gmail.com> - 2.0~git160308~a5b01d25-1
- Update to new upstream snapshot.

* Mon Mar 07 2016 Fabio Valentini <decathorpe@gmail.com> - 2.0~git160307~8d302c97-1
- Update to new upstream snapshot.

* Tue Feb 23 2016 Fabio Valentini <decathorpe@gmail.com> - 2.0~git160223~45d9135e-1
- Update to new upstream snapshot.

* Thu Feb 18 2016 Fabio Valentini <decathorpe@gmail.com> - 2.0~git160218~f3b06e58-1
- Update to new upstream snapshot.

* Mon Feb 15 2016 Fabio Valentini <decathorpe@gmail.com> - 2.0~git160215~c43321eb-1
- Update to new upstream snapshot.

* Sun Feb 07 2016 Fabio Valentini <decathorpe@gmail.com> - 2.0~git160207~ae1f0d39-1
- Update to new upstream snapshot.

* Sat Jan 23 2016 Fabio Valentini <decathorpe@gmail.com> - 2.0~git160123~57c4e54b-1
- Update to 2.0 git snapshots.

* Sun Nov 22 2015 Fabio Valentini <decathorpe@gmail.com> - 1.0-1
- Unretire vocal package. Downgrade to version 1.0. Git snapshots coming soon.

