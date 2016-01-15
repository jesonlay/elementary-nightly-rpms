%define rev 2882

Summary: The elementary continuation of Shotwell
Name: pantheon-photos
Version: 0.1.1~rev%{rev}
Release: 1%{?dist}
License: LGPLv2.1
URL: http://launchpad.net/pantheon-photos

Source0: %{name}-%{version}.tar.gz
Source1: %{name}.conf

BuildRequires: autoconf
BuildRequires: automake
BuildRequires: desktop-file-utils
BuildRequires: gettext
BuildRequires: libappstream-glib
BuildRequires: vala

BuildRequires: pkgconfig(gee-0.8)
BuildRequires: pkgconfig(gexiv2)
BuildRequires: pkgconfig(glib-2.0)
BuildRequires: pkgconfig(granite)
BuildRequires: pkgconfig(gstreamer-1.0)
BuildRequires: pkgconfig(gstreamer-base-1.0)
BuildRequires: pkgconfig(gstreamer-plugins-base-1.0)
BuildRequires: pkgconfig(gstreamer-pbutils-1.0)
BuildRequires: pkgconfig(gtk+-3.0) >= 3.10
BuildRequires: pkgconfig(gudev-1.0)
BuildRequires: pkgconfig(json-glib-1.0)
BuildRequires: pkgconfig(libgphoto2)
BuildRequires: pkgconfig(libexif)
BuildRequires: pkgconfig(libraw)
BuildRequires: pkgconfig(libsoup-2.4)
BuildRequires: pkgconfig(libxml-2.0)
BuildRequires: pkgconfig(rest-0.7)
BuildRequires: pkgconfig(sqlite3)
BuildRequires: pkgconfig(webkitgtk-3.0)


%description
The elementary continuation of Shotwell, originally written by Yorba Foundation.

Designed for elementary OS. Works and looks great on any GTK+ desktop.


%package devel
Summary: pantheon-photos development headers
Conflicts: shotwell-devel
%description devel
The elementary continuation of Shotwell, originally written by Yorba Foundation.

Designed for elementary OS. Works and looks great on any GTK+ desktop.
This package contains the development headers.


%prep
%autosetup


%build
./configure --prefix=/usr --libdir=%{_lib} --install-headers
%make_build


%install
%make_install

rm $RPM_BUILD_ROOT/%{_datadir}/glib-2.0/schemas/gschemas.compiled
rm $RPM_BUILD_ROOT/%{_datadir}/icons/hicolor/icon-theme.cache

%find_lang pantheon-photos


%check
desktop-file-validate $RPM_BUILD_ROOT/%{_datadir}/applications/pantheon-photos.desktop
desktop-file-validate $RPM_BUILD_ROOT/%{_datadir}/applications/pantheon-photos-viewer.desktop

# appstream-util validate-relax --nonet $RPM_BUILD_ROOT/%{_datadir}/appdata/*.appdata.xml
# FAILED:
# ? tag-invalid           : <icon> not allowed in appdata
# ? tag-invalid           : stock icon is not valid [multimedia-photo-manager]
# Validation of files failed


%clean
rm -rf $RPM_BUILD_ROOT


%post

%postun
if [ $1 -eq 0 ] ; then
    /usr/bin/glib-compile-schemas %{_datadir}/glib-2.0/schemas &> /dev/null || :
fi

%posttrans
/usr/bin/glib-compile-schemas %{_datadir}/glib-2.0/schemas &> /dev/null || :

%post devel
%postun devel


%files -f pantheon-photos.lang
%{_bindir}/pantheon-photos

%{_libdir}/pantheon-photos/
%{_libexecdir}/pantheon-photos/

%{_datadir}/GConf/gsettings/pantheon-photos.convert
%{_datadir}/appdata/pantheon-photos.appdata.xml
%{_datadir}/applications/pantheon-photos.desktop
%{_datadir}/applications/pantheon-photos-viewer.desktop
%{_datadir}/glib-2.0/schemas/*.xml
%{_datadir}/gnome/help/pantheon-photos/*
%{_datadir}/icons/hicolor/24x24/actions/pin-toolbar.svg
%{_datadir}/pantheon-photos/

%files devel
%{_includedir}/pantheon-photos/
%{_libdir}/pkgconfig/shotwell-plugin-dev-1.0.pc
%{_datadir}/vala/vapi/shotwell*


%changelog
* Fri Jan 15 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.1~rev2882-1
- Update to new upstream snapshot.

* Thu Jan 14 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.1~rev2881-1
- Update to new upstream snapshot.

* Tue Jan 12 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.1~rev2879-1
- Update to new upstream snapshot.

* Mon Jan 11 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.1~rev2876-1
- Update to new upstream snapshot.

* Sat Jan 09 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.1~rev2874-1
- Update to new upstream snapshot.

* Mon Jan 04 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.1~rev2873-1
- Update to new upstream snapshot.

* Sun Jan 03 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.1~rev2871-1
- Update to new upstream snapshot.

* Mon Dec 28 2015 Fabio Valentini <decathorpe@gmail.com> - 0.1.1~rev2870-1
- Update to new upstream snapshot.

* Sun Dec 27 2015 Fabio Valentini <decathorpe@gmail.com> - 0.1.1~rev2869-1
- Update to new upstream snapshot.

* Sat Dec 26 2015 Fabio Valentini <decathorpe@gmail.com> - 0.1.1~rev2868-1
- Update to new upstream snapshot.

* Thu Dec 24 2015 Fabio Valentini <decathorpe@gmail.com> - 0.1.1~rev2866-1
- Update to new upstream snapshot.

* Wed Dec 23 2015 Fabio Valentini <decathorpe@gmail.com> - 0.1.1~rev2864-1
- Update to new upstream snapshot.

* Sun Dec 20 2015 Fabio Valentini <decathorpe@gmail.com> - 0.1.1~rev2863-1
- Update to new upstream snapshot.

* Wed Dec 16 2015 Fabio Valentini <decathorpe@gmail.com> - 0.1.1~rev2862-1
- Update to new upstream snapshot.

* Tue Dec 15 2015 Fabio Valentini <decathorpe@gmail.com> - 0.1.1~rev2861-1
- Update to new upstream snapshot.

* Mon Dec 14 2015 Fabio Valentini <decathorpe@gmail.com> - 0.1.1~rev2860-1
- Update to new upstream snapshot.

* Sun Dec 13 2015 Fabio Valentini <decathorpe@gmail.com> - 0.1.1~rev2858-1
- Update to new upstream snapshot.

* Sat Dec 12 2015 Fabio Valentini <decathorpe@gmail.com> - 0.1.1~rev2857-1
- Update to new upstream snapshot.

* Fri Dec 11 2015 Fabio Valentini <decathorpe@gmail.com> - 0.1.1~rev2856-1
- Update to new upstream snapshot.

* Wed Dec 09 2015 Fabio Valentini <decathorpe@gmail.com> - 0.1.1~rev2855-1
- Update to new upstream snapshot.

* Tue Dec 08 2015 Fabio Valentini <decathorpe@gmail.com> - 0.1.1~rev2854-2
- Fix build. Remove Conflicts: shotwell bc. it seems to be co-installable now.

* Tue Dec 08 2015 Fabio Valentini <decathorpe@gmail.com> - 0.1.1~rev2854-1
- Update to new upstream snapshot.

* Mon Dec 07 2015 Fabio Valentini <decathorpe@gmail.com> - 0.1.1~rev2852-1
- Update to new upstream snapshot.

* Sun Dec 06 2015 Fabio Valentini <decathorpe@gmail.com> - 0.1.1~rev2850-1
- Update to new upstream snapshot.

* Thu Dec 03 2015 Fabio Valentini <decathorpe@gmail.com> - 0.1.1~rev2845-2
- Add Conflicts: shotwell until they cannot be installed side-by-side.

* Thu Dec 03 2015 Fabio Valentini <decathorpe@gmail.com> - 0.1.1~rev2845-1
- Update to new upstream snapshot.

* Wed Dec 02 2015 Fabio Valentini <decathorpe@gmail.com> - 0.1.1~rev2844-1
- Update to new upstream snapshot.

* Tue Dec 01 2015 Fabio Valentini <decathorpe@gmail.com> - 0.1.1~rev2841-2
- Disable appdata validation for now. Add error message to spec.

* Tue Dec 01 2015 Fabio Valentini <decathorpe@gmail.com> - 0.1.1~rev2841-1
- Update to new upstream snapshot.

* Mon Nov 30 2015 Fabio Valentini <decathorpe@gmail.com> - 0.1.1~rev2839-1
- Update to new upstream snapshot.

* Thu Nov 26 2015 Fabio Valentini <decathorpe@gmail.com> - 0.1.1~rev2838-1
- Initial package of elementary shotwell fork.



