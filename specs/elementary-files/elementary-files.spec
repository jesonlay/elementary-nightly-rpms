%global __provides_exclude_from ^%{_libdir}/(gtk-3.0)|(io.elementary.files)/.*\\.so$

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
    %{buildroot}/%{_datadir}/metainfo/%{appname}.appdata.xml || :


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

%{_datadir}/applications/%{appname}.desktop
%{_datadir}/dbus-1/services/%{appname}.service
%{_datadir}/dbus-1/services/%{appname}.FileManager1.service
%{_datadir}/glib-2.0/schemas/%{appname}.gschema.xml
%{_datadir}/%{appname}/
%{_datadir}/metainfo/%{appname}.appdata.xml
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
* Tue Jun 12 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.5+git180612.061502.219164b1-1
- Update to latest snapshot.

* Mon Jun 11 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.5+git180611.194224.2f7cd057-1
- Update to latest snapshot.

* Mon Jun 11 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.5+git180611.183116.f7b23818-1
- Update to latest snapshot.

* Sun Jun 10 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.5+git180610.154713.7c9cf111-1
- Update to latest snapshot.

* Sun Jun 10 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.5+git180610.001125.319e2b9c-1
- Update to latest snapshot.

* Fri Jun 08 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.5+git180608.001139.a243922e-1
- Update to latest snapshot.

* Thu Jun 07 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.5+git180607.000905.ea750f1a-1
- Update to latest snapshot.

* Wed Jun 06 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.5+git180606.000827.8ed5a93f-1
- Update to latest snapshot.

* Tue Jun 05 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.5+git180605.004029.71a09e25-1
- Update to latest snapshot.

* Mon Jun 04 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.5+git180604.000848.c203d79d-1
- Update to latest snapshot.

* Sun Jun 03 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.5+git180603.064815.6d36c1d8-1
- Update to latest snapshot.

* Sat Jun 02 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.5+git180602.192150.398dcb8a-1
- Update to latest snapshot.

* Sat Jun 02 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.5+git180602.160207.2ed7bd4e-1
- Update to latest snapshot.

* Sat Jun 02 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.5+git180602.011635.481c5814-1
- Update to latest snapshot.

* Fri Jun 01 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.5+git180601.163845.b29748e2-1
- Update to latest snapshot.

* Fri Jun 01 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.5+git180601.000715.361d0f2b-1
- Update to latest snapshot.

* Thu May 31 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.5+git180531.000223.d8b82118-1
- Update to latest snapshot.

* Wed May 30 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.5+git180530.125715.97bcddc4-1
- Update to latest snapshot.

* Wed May 30 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.5+git180530.091728.67524a54-1
- Update to latest snapshot.

* Tue May 29 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.5+git180529.134005.d96277c8-1
- Update to latest snapshot.

* Mon May 28 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.5+git180528.093854.df33b1da-1
- Update to latest snapshot.

* Mon May 28 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.5+git180528.000035.c76f01fd-1
- Update to latest snapshot.

* Sun May 27 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.5+git180527.091253.48572692-1
- Update to latest snapshot.

* Sat May 26 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.5+git180525.222952.f9e2b4df-1
- Update to latest snapshot.

* Thu May 24 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.5+git180524.155638.c6fb4c82-1
- Update to latest snapshot.

* Fri May 18 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.5+git180518.000720.e44a0e5f-1
- Update to latest snapshot.

* Tue May 15 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.5+git180515.173433.2950ae9f-1
- Update to latest snapshot.

* Mon May 14 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.5+git180513.221801.ecfeb272-1
- Update to latest snapshot.

* Sat May 12 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.5+git180512.000240.1334c4b9-1
- Update to latest snapshot.

* Fri May 11 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.5+git180511.101029.16587420-1
- Update to latest snapshot.

* Fri May 11 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.5+git180511.094814.42e17f65-1
- Update to latest snapshot.

* Fri May 11 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.5+git180511.055226.64252e30-1
- Update to latest snapshot.

* Thu May 10 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.5+git180510.171517.8042badc-1
- Update to latest snapshot.

* Thu May 10 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.5+git180510.115634.21f81806-1
- Update to latest snapshot.

* Thu May 10 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.5+git180510.000855.d219795d-1
- Update to latest snapshot.

* Wed May 09 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.5+git180509.143136.433d5824-1
- Update to latest snapshot.

* Tue May 08 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.5+git180508.182518.44c8e49d-1
- Update to latest snapshot.

* Tue May 08 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.5+git180508.143025.94feb0d8-1
- Update to latest snapshot.

* Tue May 08 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.5+git180507.175319.c3e40a22-1
- Update to latest snapshot.

* Mon May 07 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.5+git180507.000235.de34dd6a-1
- Update to latest snapshot.

* Sun May 06 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.5+git180505.001029.1c3cc11c-1
- Update to latest snapshot.

* Thu May 03 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.5+git180503.174827.3ae8c272-1
- Update to latest snapshot.

* Thu May 03 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.5+git180503.165744.a76dfcc1-1
- Update to latest snapshot.

* Wed May 02 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.5+git180502.181326.76da6ca1-1
- Update to latest snapshot.

* Tue May 01 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.5+git180501.000326.ddd79748-2
- Fix bogus changelog dates.

* Sun Apr 22 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.5+git180421.165835.f61d26c6-1
- Update to latest snapshot.

* Sat Apr 21 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.5+git180421.001057.74b8c888-1
- Update to latest snapshot.

* Fri Apr 20 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.5+git180420.165621.dd490bd4-1
- Update to latest snapshot.

* Fri Apr 20 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.5+git180420.001132.7b75433d-1
- Update to latest snapshot.

* Fri Apr 13 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.5+git180413.180300.ee9f9fd0-1
- Update to latest snapshot.

* Thu Apr 12 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.5+git180412.164505.138dd28b-1
- Update to latest snapshot.

* Wed Apr 11 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.5+git180411.192641.2a2956fb-1
- Update to latest snapshot.

* Tue Apr 10 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.5+git180410.190608.fccfa34f-1
- Update to latest snapshot.

* Tue Apr 10 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.5+git180410.175649.054291d3-1
- Update to latest snapshot.

* Tue Apr 10 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.5+git180410.085903.9cc80804-1
- Update to latest snapshot.

* Wed Apr 04 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.5+git180404.211441.393e726a-1
- Update to latest snapshot.

* Tue Apr 03 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.5+git180401.092955.cfe80985-1
- Update to latest snapshot.

* Wed Mar 28 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.5+git180328.183611.1409f029-1
- Update to latest snapshot.

* Tue Mar 27 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.5+git180327.175037.e1f30613-1
- Update to latest snapshot.

* Tue Mar 27 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.5+git180327.000154.3cb86e1a-1
- Update to latest snapshot.

* Mon Mar 26 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.5+git180326.000844.9974320e-1
- Update to latest snapshot.

* Sun Mar 25 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.5+git180325.182528.d6a78d0d-1
- Update to latest snapshot.

* Thu Mar 22 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.5+git180322.215431.66d7d37f-1
- Update to latest snapshot.

* Wed Mar 21 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.5+git180321.203955.82b5647c-1
- Update to latest snapshot.

* Wed Mar 21 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.5+git180321.014843.37eec518-1
- Update to latest snapshot.

* Tue Mar 20 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.5+git180320.035526.4b07cd27-1
- Update to latest snapshot.

* Mon Mar 19 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.5+git180319.205928.0a025b01-1
- Update to latest snapshot.

* Mon Mar 19 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.5+git180319.182633.9c1bec60-1
- Update to latest snapshot.

* Mon Mar 19 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.5+git180319.094901.7542e769-1
- Update to latest snapshot.

* Sun Mar 18 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.5+git180318.012205.c434ef95-2
- Adapt to upstream file changes.

* Sun Mar 18 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.5+git180318.012205.c434ef95-1
- Update to latest snapshot.

* Fri Mar 16 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.5+git180316.000347.1c84ea9c-1
- Update to latest snapshot.

* Wed Mar 14 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.5+git180314.000210.4ecd1eb3-1
- Update to latest snapshot.

* Mon Mar 12 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.5+git180312.004723.d3d34317-1
- Update to latest snapshot.

* Sat Mar 10 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.5+git180310.000347.e2056d65-1
- Update to latest snapshot.

* Fri Mar 09 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.5+git180309.112333.ccb71951-1
- Update to latest snapshot.

* Wed Mar 07 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.5+git180307.000940.cd195430-2
- Adapt to upstream file changes.

* Wed Mar 07 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.5+git180307.000940.cd195430-1
- Update to latest snapshot.

* Mon Mar 05 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.5+git180305.171632.35e2e890-1
- Update to latest snapshot.

* Wed Feb 28 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.5+git180228.105717.893872c5-1
- Update to latest snapshot.

* Thu Feb 22 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.5+git180222.000807.571556c5-1
- Update to latest snapshot.

* Sat Feb 17 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.5+git180217.193046.43d16f21-1
- Update to latest snapshot.

* Sat Feb 17 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.5+git180217.183017.d82a4e74-1
- Update to latest snapshot.

* Sat Feb 17 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.5+git180216.195606.7f7a88f9-1
- Update to latest snapshot.

* Thu Feb 15 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.5+git180215.000105.57089717-1
- Update to latest snapshot.

* Wed Feb 14 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.5+git180214.174649.724e3ffa-1
- Update to latest snapshot.

* Tue Feb 13 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.5+git180213.093014.a3cc3db4-1
- Update to latest snapshot.

* Mon Feb 12 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.5+git180210.173952.e7b108ea-1
- Update to latest snapshot.

* Fri Feb 09 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.5+git180209.000233.9f83c54b-1
- Update to latest snapshot.

* Thu Feb 08 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.5+git180208.220536.dae8895e-1
- Update to latest snapshot.

* Thu Feb 08 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.5+git180208.091554.a9329380-1
- Update to latest snapshot.

* Mon Feb 05 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.5+git180205.001109.df7f56d3-1
- Update to latest snapshot.

* Thu Feb 01 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.5+git180201.000905.20d0fb9e-1
- Update to latest snapshot.

* Tue Jan 30 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.5+git180130.180731.16a545ee-1
- Update to latest snapshot.

* Mon Jan 29 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.5+git180129.000213.3955ab26-1
- Update to latest snapshot.

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


