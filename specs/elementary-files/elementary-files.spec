%global __provides_exclude_from ^%{_libdir}/(gtk-3.0)|(io.elementary.files)/.*\\.so$
%undefine _strict_symbol_defs_build

%global srcname files
%global appname io.elementary.files

Name:           elementary-files
Summary:        File manager from elementary
Version:        0.3.5+git%{date}.%{commit}
Release:        1%{?dist}
License:        GPLv3

URL:            https://github.com/elementary/%{srcname}
Source0:        %{name}-%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  desktop-file-utils
BuildRequires:  gettext
BuildRequires:  intltool
BuildRequires:  libappstream-glib
BuildRequires:  vala >= 0.34.0

BuildRequires:  pkgconfig(dbus-glib-1)
BuildRequires:  pkgconfig(gail-3.0)
BuildRequires:  pkgconfig(gee-0.8)
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(gio-unix-2.0)
BuildRequires:  pkgconfig(glib-2.0) >= 2.29
BuildRequires:  pkgconfig(gmodule-2.0)
BuildRequires:  pkgconfig(granite) >= 0.3.0
BuildRequires:  pkgconfig(gthread-2.0)
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.10
BuildRequires:  pkgconfig(libcanberra) >= 0.30
BuildRequires:  pkgconfig(libnotify) >= 0.7.2
BuildRequires:  pkgconfig(pango) >= 1.1.2
BuildRequires:  pkgconfig(plank)
BuildRequires:  pkgconfig(sqlite3)
BuildRequires:  pkgconfig(unity) >= 4.0.0
BuildRequires:  pkgconfig(zeitgeist-2.0)

Provides:       pantheon-files
Obsoletes:      pantheon-files


%description
The simple, powerful, and sexy file manager from elementary.


%package        devel
Summary:        Pantheon file manager (development headers)
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description    devel
The simple, powerful, and sexy file manager from elementary.

This package contains the development headers.


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

%find_lang %{appname}


%check
desktop-file-validate \
    %{buildroot}/%{_datadir}/applications/%{appname}.desktop

appstream-util validate-relax --nonet \
    %{buildroot}/%{_datadir}/appdata/%{appname}.appdata.xml || :


%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig


%files -f %{appname}.lang
%doc AUTHORS README.md
%license COPYING

%{_bindir}/%{appname}
%{_bindir}/%{appname}-daemon
%{_bindir}/%{appname}-pkexec

%{_libdir}/gtk-3.0/modules/libpantheon-filechooser-module.so
%{_libdir}/%{appname}/
%{_libdir}/libpantheon-files-core.so.0
%{_libdir}/libpantheon-files-core.so.0.1
%{_libdir}/libpantheon-files-widgets.so.0
%{_libdir}/libpantheon-files-widgets.so.0.1

%{_datadir}/appdata/%{appname}.appdata.xml
%{_datadir}/applications/%{appname}.desktop
%{_datadir}/dbus-1/services/%{appname}.FileManager1.service
%{_datadir}/glib-2.0/schemas/%{appname}.gschema.xml
%{_datadir}/%{appname}/
%{_datadir}/pixmaps/%{appname}/
%{_datadir}/polkit-1/actions/%{appname}.policy


%files      devel
%{_includedir}/pantheon-files-core/
%{_includedir}/pantheon-files-widgets/

%{_libdir}/libpantheon-files-core.so
%{_libdir}/libpantheon-files-widgets.so

%{_libdir}/pkgconfig/pantheon-files-core.pc
%{_libdir}/pkgconfig/pantheon-files-widgets.pc

%{_datadir}/vala/vapi/pantheon-files-core-C.vapi
%{_datadir}/vala/vapi/pantheon-files-core.deps
%{_datadir}/vala/vapi/pantheon-files-core.vapi
%{_datadir}/vala/vapi/pantheon-files-widgets.deps
%{_datadir}/vala/vapi/pantheon-files-widgets.vapi


%changelog
* Sun Jan 28 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.5+git180127.230240.087bef40-1
- Update to latest snapshot.

* Sat Jan 27 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.5+git180127.211145.935bd662-1
- Update to latest snapshot.

* Sat Jan 27 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.5+git180127.000247.34dd9845-1
- Update to latest snapshot.

* Fri Jan 26 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.5+git180126.172006.33b40939-1
- Update to latest snapshot.

* Fri Jan 26 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.5+git180125.183753.39e4e386-2
- Be lazy about undefined symbols in plugins.

* Thu Jan 25 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.5+git180125.183753.39e4e386-1
- Update to latest snapshot.

* Wed Jan 24 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.5+git180124.171932.982a30cb-1
- Update to latest snapshot.

* Wed Jan 24 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.5+git180124.000352.d17099fe-1
- Update to latest snapshot.

* Tue Jan 23 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.5+git180123.172756.6c046866-1
- Update to latest snapshot.

* Sun Jan 21 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.5+git180121.000519.d93398b1-1
- Update to latest snapshot.

* Sat Jan 20 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.5+git180120.114454.d631383f-1
- Update to latest snapshot.

* Fri Jan 19 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.5+git180119.194807.d569ae2d-1
- Update to latest snapshot.

* Fri Jan 19 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.5+git180119.183832.aed6bc92-1
- Update to latest snapshot.

* Fri Jan 19 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.5+git180119.100436.c59ced2b-1
- Update to latest snapshot.

* Mon Jan 15 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.5+git180113.201114.b657781e-1
- Update to latest snapshot.

* Thu Jan 11 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.5+git180111.175854.cba1186c-1
- Update to latest snapshot.

* Thu Jan 11 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.5+git180111.103557.64389f27-1
- Update to latest snapshot.

* Wed Jan 10 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.5+git180110.000139.29695198-1
- Update to latest snapshot.

* Tue Jan 09 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.5+git180109.180210.93df5413-1
- Update to latest snapshot.

* Tue Jan 09 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.5+git180109.173424.8e59915b-1
- Update to latest snapshot.

* Sun Dec 31 2017 Fabio Valentini <decathorpe@gmail.com> - 0.3.5+git171231.000534.edfb165e-1
- Initial package.


