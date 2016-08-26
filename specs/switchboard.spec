Summary:        Modular Desktop Settings Hub
Name:           switchboard
Version:        2.1.0~rev%{rev}
Release:        1%{?dist}
License:        LGPLv2.1, LGPLv3
URL:            http://launchpad.net/switchboard

Source0:        %{name}-%{version}.tar.gz
Source1:        %{name}.conf

BuildRequires:  cmake
BuildRequires:  desktop-file-utils
BuildRequires:  gettext
BuildRequires:  intltool
BuildRequires:  vala >= 0.21.0

BuildRequires:  pkgconfig(clutter-gtk-1.0)
BuildRequires:  pkgconfig(gee-0.8)
BuildRequires:  pkgconfig(glib-2.0) >= 2.32
BuildRequires:  pkgconfig(granite)
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.10


%description
This project is about the container app only and its library. For plugins that handle the settings, please refer to https://launchpad.net/pantheon-plugs.

Designed for elementary OS.


%package        devel
Summary:        Modular Desktop Settings Hub (development files)
%description    devel
This project is about the container app only and its library. For plugins that handle the settings, please refer to https://launchpad.net/pantheon-plugs.

Designed for elementary OS.

This package contains the files required for developing for switchboard.


%prep
%autosetup


%build
%cmake -DUSE_UNITY:BOOL=OFF
%make_build


%install
%make_install
%find_lang switchboard

mkdir -p %{buildroot}/%{_libdir}/switchboard/hardware
mkdir -p %{buildroot}/%{_libdir}/switchboard/personal


%check
desktop-file-validate %{buildroot}/%{_datadir}/applications/switchboard.desktop

# appstream-util validate-relax --nonet $RPM_BUILD_ROOT/%{_datadir}/appdata/*.appdata.xml


%clean
rm -rf %{buildroot}


%post
/sbin/ldconfig
/usr/bin/update-desktop-database &> /dev/null || :

%postun
/sbin/ldconfig
/usr/bin/update-desktop-database &> /dev/null || :
if [ $1 -eq 0 ] ; then
    /usr/bin/glib-compile-schemas %{_datadir}/glib-2.0/schemas &> /dev/null || :
fi

%posttrans
/usr/bin/glib-compile-schemas %{_datadir}/glib-2.0/schemas &> /dev/null || :


%post           devel -p /sbin/ldconfig
%postun         devel -p /sbin/ldconfig


%files -f switchboard.lang
%license COPYING

%{_bindir}/switchboard

%{_libdir}/libswitchboard-2.0.so.0
%{_libdir}/libswitchboard-2.0.so.2.0
%{_libdir}/switchboard

%{_datadir}/appdata/switchboard.appdata.xml
%{_datadir}/applications/switchboard.desktop
%{_datadir}/glib-2.0/schemas/org.pantheon.switchboard.gschema.xml


%files          devel
%{_includedir}/switchboard-2.0/

%{_libdir}/libswitchboard-2.0.so
%{_libdir}/pkgconfig/switchboard-2.0.pc

%{_datadir}/vala/vapi/switchboard-2.0.deps
%{_datadir}/vala/vapi/switchboard-2.0.vapi


%changelog
* Fri Aug 26 2016 Fabio Valentini <decathorpe@gmail.com> - 2.1.0~rev676-1
- Update to latest snapshot.

* Thu Aug 25 2016 Fabio Valentini <decathorpe@gmail.com> - 2.1.0~rev675-1
- Update to latest snapshot.

* Tue Aug 16 2016 Fabio Valentini <decathorpe@gmail.com> - 2.1.0~rev674-1
- Update to latest snapshot.

* Mon Aug 15 2016 Fabio Valentini <decathorpe@gmail.com> - 2.1.0~rev673-1
- Update to latest snapshot.

* Sun Aug 14 2016 Fabio Valentini <decathorpe@gmail.com> - 2.1.0~rev672-1
- Update to latest snapshot.

* Fri Aug 12 2016 Fabio Valentini <decathorpe@gmail.com> - 2.1.0~rev671-1
- Update to version 2.1.0.

* Thu Aug 11 2016 Fabio Valentini <decathorpe@gmail.com> - 2.0.2~rev670-1
- Update to latest snapshot.

* Wed Aug 10 2016 Fabio Valentini <decathorpe@gmail.com> - 2.0.2~rev669-1
- Update to latest snapshot.

* Tue Aug 09 2016 Fabio Valentini <decathorpe@gmail.com> - 2.0.2~rev667-1
- Update to latest snapshot.

* Sun Aug 07 2016 Fabio Valentini <decathorpe@gmail.com> - 2.0.2~rev666-2
- Update for packaging changes.

* Sun Aug 07 2016 Fabio Valentini <decathorpe@gmail.com> - 2.0.2~rev666-1
- Update to latest snapshot.

* Sat Aug 06 2016 Fabio Valentini <decathorpe@gmail.com> - 2.0.2~rev665-1
- Update to latest snapshot.

* Fri Aug 05 2016 Fabio Valentini <decathorpe@gmail.com> - 2.0.2~rev664-3
- Update for packaging changes.

* Fri Aug 05 2016 Fabio Valentini <decathorpe@gmail.com>
- Add new appdata file to spec.

* Fri Aug 05 2016 Fabio Valentini <decathorpe@gmail.com> - 2.0.2~rev664-2
- Update for packaging changes.

* Fri Aug 05 2016 Fabio Valentini <decathorpe@gmail.com>
- Add BR: intltool to fix build.

* Fri Aug 05 2016 Fabio Valentini <decathorpe@gmail.com> - 2.0.2~rev664-1
- Update to latest snapshot.

* Thu Aug 04 2016 Fabio Valentini <decathorpe@gmail.com> - 2.0.2~rev663-1
- Update to latest snapshot.

* Tue Aug 02 2016 Fabio Valentini <decathorpe@gmail.com> - 2.0.2~rev656-1
- Update to latest snapshot.

* Sun Jul 31 2016 Fabio Valentini <decathorpe@gmail.com> - 2.0.2~rev655-1
- Update to latest snapshot.

* Sat Jul 30 2016 Fabio Valentini <decathorpe@gmail.com> - 2.0.2~rev654-1
- Update to latest snapshot.

* Wed Jul 27 2016 Fabio Valentini <decathorpe@gmail.com> - 2.0.2~rev653-1
- Update to latest snapshot.

* Mon Jul 25 2016 Fabio Valentini <decathorpe@gmail.com> - 2.0.2~rev652-1
- Update to latest snapshot.

* Sun Jul 17 2016 Fabio Valentini <decathorpe@gmail.com> - 2.0.2~rev650-1
- Update to latest snapshot.

* Thu Jul 14 2016 Fabio Valentini <decathorpe@gmail.com> - 2.0.2~rev649-1
- Update to latest snapshot.

* Thu Jul 07 2016 Fabio Valentini <decathorpe@gmail.com> - 2.0.2~rev648-1
- Update to latest snapshot.

* Wed Jul 06 2016 Fabio Valentini <decathorpe@gmail.com> - 2.0.2~rev647-2
- Update for packaging changes.

* Sun Jun 19 2016 Fabio Valentini <decathorpe@gmail.com> - 2.0.2~rev639-1
- Update to latest snapshot.

* Sat Jun 18 2016 Fabio Valentini <decathorpe@gmail.com> - 2.0.2~rev638-1
- Update to latest snapshot.

* Sat Jun 18 2016 Fabio Valentini <decathorpe@gmail.com> - 2.0.2~rev637-1
- Update to latest snapshot.

* Fri Jun 17 2016 Fabio Valentini <decathorpe@gmail.com> - 2.0.2~rev636-1
- Update to latest snapshot.

* Wed Jun 15 2016 Fabio Valentini <decathorpe@gmail.com> - 2.0.2~rev635-1
- Update to latest snapshot.

* Tue Jun 14 2016 Fabio Valentini <decathorpe@gmail.com> - 2.0.2~rev633-1
- Update to latest snapshot.

* Mon May 30 2016 Fabio Valentini <decathorpe@gmail.com> - 2.0.2~rev632-1
- Update to latest snapshot.

* Sun May 29 2016 Fabio Valentini <decathorpe@gmail.com> - 2.0.2~rev631-2
- Update for packaging changes.

* Thu May 26 2016 Fabio Valentini <decathorpe@gmail.com> - 2.0.2~rev631-1
- Update to latest snapshot.

* Wed May 25 2016 Fabio Valentini <decathorpe@gmail.com> - 2.0.2~rev630-1
- Update to latest snapshot.

* Sat May 14 2016 Fabio Valentini <decathorpe@gmail.com> - 2.0.2~rev629-1
- Update to latest snapshot.

* Thu May 12 2016 Fabio Valentini <decathorpe@gmail.com> - 2.0.2~rev628-1
- Update to latest snapshot.

* Wed May 11 2016 Fabio Valentini <decathorpe@gmail.com> - 2.0.2~rev627-1
- Update to latest snapshot.

* Tue May 10 2016 Fabio Valentini <decathorpe@gmail.com> - 2.0.2~rev626-1
- Update to latest snapshot.

* Sun May 08 2016 Fabio Valentini <decathorpe@gmail.com> - 2.0.2~rev625-1
- Update to latest snapshot.

* Sat May 07 2016 Fabio Valentini <decathorpe@gmail.com> - 2.0.2~rev624-1
- Update for packaging changes.


