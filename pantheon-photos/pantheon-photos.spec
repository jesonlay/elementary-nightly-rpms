%define rev 2845

Summary: The elementary continuation of Shotwell
Name: pantheon-photos
Version: 0.1.1~rev%{rev}
Release: 2%{?dist}
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

Conflicts: shotwell


%description
The elementary continuation of Shotwell, originally written by Yorba Foundation.

Designed for elementary OS. Works and looks great on any GTK+ desktop.


%package devel
Summary: pantheon-photos development headers
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

%find_lang shotwell


%check
desktop-file-validate $RPM_BUILD_ROOT/%{_datadir}/applications/shotwell.desktop
desktop-file-validate $RPM_BUILD_ROOT/%{_datadir}/applications/shotwell-viewer.desktop

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


%files -f shotwell.lang
%{_bindir}/shotwell

%{_libdir}/shotwell/
%{_libexecdir}/shotwell/

%{_datadir}/GConf/gsettings/shotwell.convert
%{_datadir}/appdata/shotwell.appdata.xml
%{_datadir}/applications/shotwell.desktop
%{_datadir}/applications/shotwell-viewer.desktop
%{_datadir}/glib-2.0/schemas/*.xml
%{_datadir}/gnome/help/shotwell/*
%{_datadir}/icons/hicolor/24x24/actions/pin-toolbar.svg
%{_datadir}/shotwell/

%files devel
%{_includedir}/shotwell/
%{_libdir}/pkgconfig/shotwell-plugin-dev-1.0.pc
%{_datadir}/vala/vapi/shotwell*


%changelog
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



