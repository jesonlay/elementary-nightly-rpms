Name:           granite
Summary:        elementary Development Library
Version:        5.0+git%{date}.%{commit}
Release:        1%{?dist}
License:        LGPLv3+

URL:            https://github.com/elementary/%{name}
Source0:        %{name}-%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  desktop-file-utils
BuildRequires:  gettext
BuildRequires:  vala

BuildRequires:  pkgconfig(gee-0.8)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(gobject-introspection-1.0)

# granite provides and needs some generic icons
Requires:       hicolor-icon-theme


%description
An extension to GTK+ that provides several useful widgets and classes
to ease application development.


%package        devel
Summary:        Granite Toolkit development headers
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description    devel
An extension to GTK+ that provides several useful widgets and classes
to ease application development.

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

%find_lang granite


%check
desktop-file-validate \
    %{buildroot}/%{_datadir}/applications/granite-demo.desktop


%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig


%files -f granite.lang
%doc AUTHORS README.md
%license COPYING

%{_libdir}/libgranite.so.5
%{_libdir}/libgranite.so.5.0
%{_libdir}/girepository-1.0/Granite-1.0.typelib

%{_datadir}/icons/hicolor/*/actions/appointment.svg
%{_datadir}/icons/hicolor/*/actions/open-menu.svg
%{_datadir}/icons/hicolor/scalable/actions/open-menu-symbolic.svg


%files devel
%{_bindir}/granite-demo

%{_libdir}/libgranite.so
%{_libdir}/pkgconfig/granite.pc

%{_includedir}/granite/

%{_datadir}/applications/granite-demo.desktop
%{_datadir}/gir-1.0/Granite-1.0.gir
%{_datadir}/vala/vapi/granite.deps
%{_datadir}/vala/vapi/granite.vapi


%changelog
* Sat Aug 18 2018 Fabio Valentini <decathorpe@gmail.com> - 5.0+git180818.125611.07a83494-1
- Update to latest snapshot.

* Thu Aug 16 2018 Fabio Valentini <decathorpe@gmail.com> - 5.0+git180815.000856.f24caa6d-2
- Occasional mass rebuild.

* Wed Aug 15 2018 Fabio Valentini <decathorpe@gmail.com> - 5.0+git180815.000856.f24caa6d-1
- Update to latest snapshot.

* Mon Aug 13 2018 Fabio Valentini <decathorpe@gmail.com> - 5.0+git180813.000253.84b0ab03-1
- Update to latest snapshot.

* Tue Aug 07 2018 Fabio Valentini <decathorpe@gmail.com> - 5.0+git180807.000315.053713c7-1
- Update to latest snapshot.

* Tue Aug 07 2018 Fabio Valentini <decathorpe@gmail.com> - 5.0+git180806.082653.716dee35-1
- Update to latest snapshot.

* Tue Aug 07 2018 Fabio Valentini <decathorpe@gmail.com> - 5.0+git180806.080129.1d7a0adc-1
- Update to latest snapshot.

* Mon Aug 06 2018 Fabio Valentini <decathorpe@gmail.com> - 5.0+git180806.005355.877d6f1b-1
- Update to latest snapshot.

* Sun Aug 05 2018 Fabio Valentini <decathorpe@gmail.com> - 5.0+git180805.070951.9d17f78a-1
- Update to latest snapshot.

* Sat Aug 04 2018 Fabio Valentini <decathorpe@gmail.com> - 5.0+git180804.110918.cb2783ca-1
- Update to latest snapshot.

* Sat Aug 04 2018 Fabio Valentini <decathorpe@gmail.com> - 5.0+git180804.093245.4bcd849d-1
- Update to latest snapshot.

* Fri Aug 03 2018 Fabio Valentini <decathorpe@gmail.com> - 5.0+git180803.001652.16d6be7a-1
- Update to latest snapshot.

* Thu Aug 02 2018 Fabio Valentini <decathorpe@gmail.com> - 5.0+git180802.141910.91362cdb-1
- Update to latest snapshot.

* Thu Aug 02 2018 Fabio Valentini <decathorpe@gmail.com> - 5.0+git180802.071105.ee33a96a-1
- Update to latest snapshot.

* Wed Aug 01 2018 Fabio Valentini <decathorpe@gmail.com> - 5.0+git180801.000449.92cca84b-1
- Update to latest snapshot.

* Tue Jul 31 2018 Fabio Valentini <decathorpe@gmail.com> - 5.0+git180731.223332.4fbd94ac-1
- Update to latest snapshot.

* Tue Jul 31 2018 Fabio Valentini <decathorpe@gmail.com> - 5.0+git180731.210044.54af9d95-1
- Update to latest snapshot.

* Tue Jul 31 2018 Fabio Valentini <decathorpe@gmail.com> - 5.0+git180731.125652.f74fe517-1
- Update to latest snapshot.

* Tue Jul 31 2018 Fabio Valentini <decathorpe@gmail.com> - 5.0+git180731.062546.e39811a6-1
- Update to latest snapshot.

* Mon Jul 30 2018 Fabio Valentini <decathorpe@gmail.com> - 5.0+git180730.155249.b0389592-1
- Update to latest snapshot.

* Tue Jul 24 2018 Fabio Valentini <decathorpe@gmail.com> - 5.0+git180724.030643.5256fb9c-1
- Update to latest snapshot.

* Fri Jul 20 2018 Fabio Valentini <decathorpe@gmail.com> - 5.0+git180720.000657.64c5b285-1
- Update to latest snapshot.

* Tue Jul 17 2018 Fabio Valentini <decathorpe@gmail.com> - 5.0+git180717.161042.0625195d-1
- Update to latest snapshot.

* Fri Jul 13 2018 Fabio Valentini <decathorpe@gmail.com> - 5.0+git180713.000334.557d5105-1
- Update to latest snapshot.

* Wed Jul 11 2018 Fabio Valentini <decathorpe@gmail.com> - 5.0+git180711.000838.dc2becbe-1
- Update to latest snapshot.

* Wed Jul 04 2018 Fabio Valentini <decathorpe@gmail.com> - 5.0+git180627.172801.07ff49fa-1
- Update to latest snapshot.

* Fri Jun 15 2018 Fabio Valentini <decathorpe@gmail.com> - 5.0+git180615.001012.ea50e289-1
- Update to latest snapshot.

* Thu Jun 14 2018 Fabio Valentini <decathorpe@gmail.com> - 5.0+git180614.083012.135a2397-1
- Update to latest snapshot.

* Wed Jun 13 2018 Fabio Valentini <decathorpe@gmail.com> - 5.0+git180613.000656.a8a37cac-1
- Update to latest snapshot.

* Sat Jun 09 2018 Fabio Valentini <decathorpe@gmail.com> - 5.0+git180609.185905.57707304-1
- Update to latest snapshot.

* Sat Jun 09 2018 Fabio Valentini <decathorpe@gmail.com> - 5.0+git180608.001121.965d3231-1
- Update to version 5.0.

* Fri Jun 08 2018 Fabio Valentini <decathorpe@gmail.com> - 0.5+git180608.001121.965d3231-1
- Update to latest snapshot.

* Wed Jun 06 2018 Fabio Valentini <decathorpe@gmail.com> - 0.5+git180606.000808.eb43621e-1
- Update to latest snapshot.

* Tue Jun 05 2018 Fabio Valentini <decathorpe@gmail.com> - 0.5+git180605.174910.d576af74-1
- Update to latest snapshot.

* Tue Jun 05 2018 Fabio Valentini <decathorpe@gmail.com> - 0.5+git180605.075934.adcf2c5c-1
- Update to latest snapshot.

* Tue Jun 05 2018 Fabio Valentini <decathorpe@gmail.com> - 0.5+git180605.000529.256b50c0-1
- Update to latest snapshot.

* Mon Jun 04 2018 Fabio Valentini <decathorpe@gmail.com> - 0.5+git180531.181042.9bb3295d-1
- Update to latest snapshot.

* Tue May 29 2018 Fabio Valentini <decathorpe@gmail.com> - 0.5+git180529.090403.7f1dcb2e-1
- Update to latest snapshot.

* Mon May 28 2018 Fabio Valentini <decathorpe@gmail.com> - 0.5+git180528.084417.2620b9f0-1
- Update to latest snapshot.

* Thu May 24 2018 Fabio Valentini <decathorpe@gmail.com> - 0.5+git180523.154618.d708dd47-1
- Update to latest snapshot.

* Wed May 09 2018 Fabio Valentini <decathorpe@gmail.com> - 0.5+git180509.184630.30ed300d-1
- Update to latest snapshot.

* Mon May 07 2018 Fabio Valentini <decathorpe@gmail.com> - 0.5+git180507.000227.5a3e0f53-1
- Update to latest snapshot.

* Sun May 06 2018 Fabio Valentini <decathorpe@gmail.com> - 0.5+git180504.000514.f8ab101d-1
- Update to latest snapshot.

* Wed Apr 25 2018 Fabio Valentini <decathorpe@gmail.com> - 0.5+git180425.183159.0cb393b2-1
- Update to latest snapshot.

* Tue Apr 24 2018 Fabio Valentini <decathorpe@gmail.com> - 0.5+git180424.184216.6959711b-1
- Update to latest snapshot.

* Sat Apr 21 2018 Fabio Valentini <decathorpe@gmail.com> - 0.5+git180421.001037.f4eb3ddc-1
- Update to latest snapshot.

* Fri Apr 13 2018 Fabio Valentini <decathorpe@gmail.com> - 0.5+git180413.202911.9529e2a2-1
- Update to latest snapshot.

* Tue Apr 10 2018 Fabio Valentini <decathorpe@gmail.com> - 0.5+git180410.161310.4c67358f-1
- Update to latest snapshot.

* Tue Apr 03 2018 Fabio Valentini <decathorpe@gmail.com> - 0.5+git180329.195947.c867872b-1
- Update to latest snapshot.

* Mon Mar 26 2018 Fabio Valentini <decathorpe@gmail.com> - 0.5+git180326.175245.dfd374f7-1
- Update to latest snapshot.

* Tue Mar 20 2018 Fabio Valentini <decathorpe@gmail.com> - 0.5+git180320.092747.9fd8fb63-1
- Update to latest snapshot.

* Thu Mar 15 2018 Fabio Valentini <decathorpe@gmail.com> - 0.5+git180315.194617.b3db1a33-1
- Update to latest snapshot.

* Sat Feb 24 2018 Fabio Valentini <decathorpe@gmail.com> - 0.5+git180223.205653.65569147-1
- Update to latest snapshot.

* Mon Feb 19 2018 Fabio Valentini <decathorpe@gmail.com> - 0.5+git180219.175116.6c28945b-1
- Update to latest snapshot.

* Mon Feb 12 2018 Fabio Valentini <decathorpe@gmail.com> - 0.5+git180211.175919.19cbaf09-1
- Update to latest snapshot.

* Mon Feb 05 2018 Fabio Valentini <decathorpe@gmail.com> - 0.5+git180205.001056.f93df945-1
- Update to latest snapshot.

* Tue Jan 30 2018 Fabio Valentini <decathorpe@gmail.com> - 0.5+git180130.180322.3d5a7416-1
- Update to latest snapshot.

* Fri Jan 26 2018 Fabio Valentini <decathorpe@gmail.com> - 0.5+git180126.201505.f50fe6c4-1
- Update to latest snapshot.

* Fri Jan 26 2018 Fabio Valentini <decathorpe@gmail.com> - 0.5+git180126.194350.c5794dcb-1
- Update to latest snapshot.

* Sat Jan 06 2018 Fabio Valentini <decathorpe@gmail.com> - 0.5+git180106.001654.6cd164a7-2
- Remove icon cache scriptlets.

* Sat Jan 06 2018 Fabio Valentini <decathorpe@gmail.com> - 0.5+git180106.001654.6cd164a7-1
- Update to latest snapshot.

* Sun Dec 31 2017 Fabio Valentini <decathorpe@gmail.com> - 0.5+git171230.000836.61ca3f67-2
- Clean up .spec file.

* Sat Dec 30 2017 Fabio Valentini <decathorpe@gmail.com> - 0.5+git171230.000836.61ca3f67-1
- Update to latest snapshot.

* Tue Dec 19 2017 Fabio Valentini <decathorpe@gmail.com> - 0.5+git171219.193238.d1b78ca7-1
- Update to latest snapshot.

* Mon Dec 18 2017 Fabio Valentini <decathorpe@gmail.com> - 0.5+git171218.205809.6d0f960f-1
- Update to latest snapshot.

* Fri Dec 15 2017 Fabio Valentini <decathorpe@gmail.com> - 0.5+git171215.001049.104776ed-1
- Update to latest snapshot.

* Wed Dec 06 2017 Fabio Valentini <decathorpe@gmail.com> - 0.5+git171206.054123.cfc52bd8-1
- Update to latest snapshot.

* Tue Nov 21 2017 Fabio Valentini <decathorpe@gmail.com> - 0.5+git171121.061615.0bbacfba-1
- Update to latest snapshot.

* Mon Nov 20 2017 Fabio Valentini <decathorpe@gmail.com> - 0.5+git171118.234137.401e79ff-1
- Update to latest snapshot.

* Fri Nov 17 2017 Fabio Valentini <decathorpe@gmail.com> - 0.5+git171117.205816.56f0725f-1
- Update to latest snapshot.

* Tue Nov 14 2017 Fabio Valentini <decathorpe@gmail.com> - 0.5+git171113.211441.79c50183-1
- Update to latest snapshot.

* Sun Nov 12 2017 Fabio Valentini <decathorpe@gmail.com> - 0.5+git171112.000500.ae60cafe-1
- Update to latest snapshot.

* Sat Nov 11 2017 Fabio Valentini <decathorpe@gmail.com> - 0.5+git171111.162716.da50ea3c-1
- Update to latest snapshot.

* Fri Nov 10 2017 Fabio Valentini <decathorpe@gmail.com> - 0.5+git171110.182604.fc81493c-1
- Update to latest snapshot.

* Thu Nov 09 2017 Fabio Valentini <decathorpe@gmail.com> - 0.5+git171109.004405.73389baf-1
- Update to latest snapshot.

* Sat Nov 04 2017 Fabio Valentini <decathorpe@gmail.com> - 0.5+git171103.123516.fd298ea6-1
- Update to version 0.5.

* Fri Nov 03 2017 Fabio Valentini <decathorpe@gmail.com> - 0.4.1+git171103.123516.fd298ea6-1
- Update to latest snapshot.

* Thu Nov 02 2017 Fabio Valentini <decathorpe@gmail.com> - 0.4.1+git171102.161738.d9a2b5ae-1
- Update to latest snapshot.

* Thu Nov 02 2017 Fabio Valentini <decathorpe@gmail.com> - 0.4.1+git171102.030851.4c3c936a-1
- Update to latest snapshot.

* Wed Nov 01 2017 Fabio Valentini <decathorpe@gmail.com> - 0.4.1+git171101.000336.2f18cff4-1
- Update to latest snapshot.

* Tue Oct 31 2017 Fabio Valentini <decathorpe@gmail.com> - 0.4.1+git171030.222136.62d426b4-2
- Adapt to upstream file changes.

* Tue Oct 31 2017 Fabio Valentini <decathorpe@gmail.com> - 0.4.1+git171030.222136.62d426b4-1
- Update to latest snapshot.

* Tue Oct 24 2017 Fabio Valentini <decathorpe@gmail.com> - 0.4.1+git171024.005516.cc42d66f-1
- Update to latest snapshot.

* Tue Oct 17 2017 Fabio Valentini <decathorpe@gmail.com> - 0.4.1+git171017.184723.73d232fc-1
- Update to latest snapshot.

* Tue Oct 17 2017 Fabio Valentini <decathorpe@gmail.com> - 0.4.1+git171017.020452.92dbf6db-1
- Update to latest snapshot.

* Mon Oct 16 2017 Fabio Valentini <decathorpe@gmail.com> - 0.4.1+git171016.144105.b3ad24b3-1
- Update to latest snapshot.

* Fri Oct 13 2017 Fabio Valentini <decathorpe@gmail.com> - 0.4.1+git171013.171010.ea8e2721-1
- Update to latest snapshot.

* Wed Oct 11 2017 Fabio Valentini <decathorpe@gmail.com> - 0.4.1+git171010.201052.d4b62d26-1
- Update to latest snapshot.

* Sun Oct 08 2017 Fabio Valentini <decathorpe@gmail.com> - 0.4.1+git171008.095053.afcf79a8-1
- Update to latest snapshot.

* Wed Sep 20 2017 Fabio Valentini <decathorpe@gmail.com> - 0.4.1+git170920.165059.f761f279-1
- Update to latest snapshot.

* Tue Sep 12 2017 Fabio Valentini <decathorpe@gmail.com> - 0.4.1+git170911.172216.d63a98ad-1
- Update to latest snapshot.

* Mon Sep 04 2017 Fabio Valentini <decathorpe@gmail.com> - 0.4.1+git170904.000706.943f65f8-1
- Update to latest snapshot.

* Wed Aug 23 2017 Fabio Valentini <decathorpe@gmail.com> - 0.4.1+git170823.153421.36952bc9-1
- Update to latest snapshot.

* Wed Aug 23 2017 Fabio Valentini <decathorpe@gmail.com> - 0.4.1+git170823.001019.546e4db0-1
- Update to latest snapshot.

* Thu Aug 17 2017 Fabio Valentini <decathorpe@gmail.com> - 0.4.1+git170817.000726.1f812004-1
- Update to latest snapshot.

* Fri Aug 04 2017 Fabio Valentini <decathorpe@gmail.com> - 0.4.1+git170803.183649.ab03e783-1
- Update to latest snapshot.

* Tue Aug 01 2017 Fabio Valentini <decathorpe@gmail.com> - 0.4.1+git170801.173646.a3c083e5-1
- Update to latest snapshot.

* Tue Jul 25 2017 Fabio Valentini <decathorpe@gmail.com> - 0.4.1+git170725.181903.682a49a9-1
- Update to latest snapshot.

* Mon Jul 24 2017 Fabio Valentini <decathorpe@gmail.com> - 0.4.1+git170724.022913.c3be3689-1
- Update to latest snapshot.

* Tue Jul 18 2017 Fabio Valentini <decathorpe@gmail.com> - 0.4.1+git170718.175313.36d6e2c8-1
- Update to latest snapshot.

* Tue Jul 18 2017 Fabio Valentini <decathorpe@gmail.com> - 0.4.1+git170718.165220.94bfe0a5-1
- Update to latest snapshot.

* Fri Jul 14 2017 Fabio Valentini <decathorpe@gmail.com> - 0.4.1+git170714.005227.c6c51f8d-1
- Update to latest snapshot.

* Wed Jul 12 2017 Fabio Valentini <decathorpe@gmail.com> - 0.4.1+git170711.221450.4d3fe7a0-1
- Update to latest snapshot.

* Tue Jul 11 2017 Fabio Valentini <decathorpe@gmail.com> - 0.4.1+git170711.180302.0e06749b-1
- Update to latest snapshot.

* Tue Jul 11 2017 Fabio Valentini <decathorpe@gmail.com> - 0.4.1+git170711.172846.8f7434d7-1
- Update to latest snapshot.

* Sat Jul 08 2017 Fabio Valentini <decathorpe@gmail.com> - 0.4.1+git170708.034235.e2809410-1
- Update to latest snapshot.

* Wed Jul 05 2017 Fabio Valentini <decathorpe@gmail.com> - 0.4.1+git170705.205850.c8760971-1
- Update to latest snapshot.

* Mon Jul 03 2017 Fabio Valentini <decathorpe@gmail.com> - 0.4.1+git170703.175437.068e2043-1
- Update to latest snapshot.

* Sat Jul 01 2017 Fabio Valentini <decathorpe@gmail.com> - 0.4.1+git170701.181426.1d7ba487-1
- Update to latest snapshot.

* Thu Jun 29 2017 Fabio Valentini <decathorpe@gmail.com> - 0.4.1+git170628.220323.436a54d8-1
- Update to latest snapshot.

* Wed Jun 21 2017 Fabio Valentini <decathorpe@gmail.com> - 0.4.1+git170621.155312.f9a5b1a4-1
- Update to latest snapshot.

* Wed Jun 21 2017 Fabio Valentini <decathorpe@gmail.com> - 0.4.1+git170621.093638.33563477-1
- Update to latest snapshot.

* Tue Jun 20 2017 Fabio Valentini <decathorpe@gmail.com> - 0.4.1+git170620.180946.bd7c06d9-1
- Update to latest snapshot.

* Tue Jun 20 2017 Fabio Valentini <decathorpe@gmail.com> - 0.4.1+git170620.160714.a2ca374b-1
- Update to latest snapshot.

* Tue Jun 20 2017 Fabio Valentini <decathorpe@gmail.com> - 0.4.1+git170620.155429.fdb1aab1-1
- Update to latest snapshot.

* Sat Jun 17 2017 Fabio Valentini <decathorpe@gmail.com> - 0.4.1+git170616.232056.1b3620c3-1
- Update to latest snapshot.

* Fri Jun 16 2017 Fabio Valentini <decathorpe@gmail.com> - 0.4.1+git170615.210618.8cd0caa7-1
- Update to latest snapshot.

* Thu Jun 01 2017 Fabio Valentini <decathorpe@gmail.com> - 0.4.1+git170531.221351.f502a49c-1
- Update to latest snapshot.

* Sun May 28 2017 Fabio Valentini <decathorpe@gmail.com> - 0.4.1+git170528.110056.51eb2dc8-1
- Update to latest snapshot.

* Sat May 27 2017 Fabio Valentini <decathorpe@gmail.com> - 0.4.1+git170527.130252.3a2b06ce-1
- Update to latest snapshot.

* Tue May 23 2017 Fabio Valentini <decathorpe@gmail.com> - 0.4.1+git170523.174839.3463b033-1
- Update to latest snapshot.

* Tue May 23 2017 Fabio Valentini <decathorpe@gmail.com> - 0.4.1+git170523.101838.0fa76962-1
- Update to latest snapshot.

* Sun May 21 2017 Fabio Valentini <decathorpe@gmail.com> - 0.4.1+git170521.211512.efaa3ece-1
- Update to latest snapshot.

* Fri May 19 2017 Fabio Valentini <decathorpe@gmail.com> - 0.4.1+git170519.013047.e0cf7e93-1
- Update to latest snapshot.

* Fri May 12 2017 Fabio Valentini <decathorpe@gmail.com> - 0.4.1+git170511.190041.adf67c23-1
- Update to latest snapshot.

* Thu May 11 2017 Fabio Valentini <decathorpe@gmail.com> - 0.4.1+git170511.214950.e2cff0b0-1
- Update to latest snapshot.

* Thu May 11 2017 Fabio Valentini <decathorpe@gmail.com> - 0.4.1+git170511.101208.7b27ac97-1
- Update to latest snapshot.

* Thu May 11 2017 Fabio Valentini <decathorpe@gmail.com> - 0.4.1+git170511.091111.bbeac353-1
- Update to latest snapshot.

* Thu May 11 2017 Fabio Valentini <decathorpe@gmail.com> - 0.4.1+git170511.105251.10741ff2-1
- Update to latest snapshot.

* Wed May 10 2017 Fabio Valentini <decathorpe@gmail.com> - 0.4.1+git170509.225855.831bcbe8-1
- Update to latest snapshot.

* Tue May 09 2017 Fabio Valentini <decathorpe@gmail.com> - 0.4.1+git170509.094246.323596dd-1
- Update to latest snapshot.

* Mon May 08 2017 Fabio Valentini <decathorpe@gmail.com> - 0.4.1+git170508.124418.14aee76b-1
- Update to latest snapshot.

* Mon May 08 2017 Fabio Valentini <decathorpe@gmail.com> - 0.4.1+git170508.194643.ff046522-1
- Update to latest snapshot.

* Sun May 07 2017 Fabio Valentini <decathorpe@gmail.com> - 0.4.1+git170506.210852.9e74f966-1
- Update to version 0.4.1.

* Sun May 07 2017 Fabio Valentini <decathorpe@gmail.com> - 0.4.0.1+rev1068-1
- Update to latest snapshot.

* Sat May 06 2017 Fabio Valentini <decathorpe@gmail.com> - 0.4.0.1+rev1063-1
- Update to latest snapshot.

* Fri May 05 2017 Fabio Valentini <decathorpe@gmail.com> - 0.4.0.1+rev1062-1
- Update to latest snapshot.

* Fri May 05 2017 Fabio Valentini <decathorpe@gmail.com> - 0.4.0.1+rev1063-1
- Update to latest snapshot.

* Thu May 04 2017 Fabio Valentini <decathorpe@gmail.com> - 0.4.0.1+rev1061-1
- Update to latest snapshot.

* Wed May 03 2017 Fabio Valentini <decathorpe@gmail.com> - 0.4.0.1+rev1060-1
- Update to latest snapshot.

* Wed May 03 2017 Fabio Valentini <decathorpe@gmail.com> - 0.4.0.1+rev1056-1
- Update to latest snapshot.

* Sun Apr 30 2017 Fabio Valentini <decathorpe@gmail.com> - 0.4.0.1+rev1055-1
- Update to latest snapshot.

* Sat Apr 29 2017 Fabio Valentini <decathorpe@gmail.com> - 0.4.0.1+rev1054-1
- Update to latest snapshot.

* Sat Apr 29 2017 Fabio Valentini <decathorpe@gmail.com> - 0.4.0.1+rev1052-1
- Update to latest snapshot.

* Fri Apr 28 2017 Fabio Valentini <decathorpe@gmail.com> - 0.4.0.1+rev1051-1
- Update to latest snapshot.

* Wed Apr 26 2017 Fabio Valentini <decathorpe@gmail.com> - 0.4.0.1+rev1050-1
- Update to latest snapshot.

* Mon Apr 24 2017 Fabio Valentini <decathorpe@gmail.com> - 0.4.0.1+rev1049-2
- Adapt to upstream changes.

* Fri Apr 21 2017 Fabio Valentini <decathorpe@gmail.com> - 0.4.0.1+rev1045-1
- Update to latest snapshot.

* Wed Apr 05 2017 Fabio Valentini <decathorpe@gmail.com> - 0.4.0.1+rev1043-1
- Update to latest snapshot.

* Wed Mar 22 2017 Fabio Valentini <decathorpe@gmail.com> - 0.4.0.1+rev1042-1
- Update to latest snapshot.

* Sun Mar 19 2017 Fabio Valentini <decathorpe@gmail.com> - 0.4.0.1+rev1041-1
- Update to latest snapshot.

* Wed Mar 15 2017 Fabio Valentini <decathorpe@gmail.com> - 0.4.0.1+rev1040-1
- Update to latest snapshot.

* Tue Mar 14 2017 Fabio Valentini <decathorpe@gmail.com> - 0.4.0.1+rev1039-1
- Update to latest snapshot.

* Tue Mar 07 2017 Fabio Valentini <decathorpe@gmail.com> - 0.4.0.1+rev1038-1
- Update to latest snapshot.

* Mon Feb 27 2017 Fabio Valentini <decathorpe@gmail.com> - 0.4.0.1+rev1037-1
- Update to latest snapshot.

* Sun Feb 19 2017 Fabio Valentini <decathorpe@gmail.com> - 0.4.0.1+rev1035-1
- Update to latest snapshot.

* Wed Feb 15 2017 Fabio Valentini <decathorpe@gmail.com> - 0.4.0.1+rev1034-1
- Update to latest snapshot.

* Mon Feb 13 2017 Fabio Valentini <decathorpe@gmail.com> - 0.4.0.1+rev1033-1
- Update to latest snapshot.

* Sat Feb 11 2017 Fabio Valentini <decathorpe@gmail.com> - 0.4.0.1+rev1032-1
- Update to latest snapshot.

* Thu Feb 09 2017 Fabio Valentini <decathorpe@gmail.com> - 0.4.0.1+rev1031-1
- Update to latest snapshot.

* Wed Feb 08 2017 Fabio Valentini <decathorpe@gmail.com> - 0.4.0.1+rev1030-2
- Sync spec with the fedora package.

* Wed Feb 01 2017 Fabio Valentini <decathorpe@gmail.com> - 0.4.0.1+rev1030-1
- Update to latest snapshot.

* Sat Jan 28 2017 Fabio Valentini <decathorpe@gmail.com> - 0.4.0.1+rev1029-1
- Update to latest snapshot.

* Thu Jan 26 2017 Fabio Valentini <decathorpe@gmail.com> - 0.4.0.1+rev1028-1
- Update to latest snapshot.

* Sat Jan 21 2017 Fabio Valentini <decathorpe@gmail.com> - 0.4.0.1+rev1027-1
- Update to latest snapshot.

* Mon Jan 09 2017 Fabio Valentini <decathorpe@gmail.com> - 0.4.0.1+rev1026-1
- Update to latest snapshot.

* Fri Jan 06 2017 Fabio Valentini <decathorpe@gmail.com> - 0.4.0.1+rev1025-1
- Update to latest snapshot.

* Thu Jan 05 2017 Fabio Valentini <decathorpe@gmail.com> - 0.4.0.1+rev1024-1
- Update to latest snapshot.

* Tue Jan 03 2017 Fabio Valentini <decathorpe@gmail.com> - 0.4.0.1+rev1023-1
- Update to latest snapshot.

* Tue Jan 03 2017 Fabio Valentini <decathorpe@gmail.com> - 0.4.0.1+rev1022-1
- Update to latest snapshot.

* Sun Jan 01 2017 Fabio Valentini <decathorpe@gmail.com> - 0.4.0.1+rev1021-1
- Update to latest snapshot.

* Sat Dec 31 2016 Fabio Valentini <decathorpe@gmail.com> - 0.4.0.1+rev1020-1
- Update to latest snapshot.

* Tue Dec 27 2016 Fabio Valentini <decathorpe@gmail.com> - 0.4.0.1+rev1019-1
- Update to latest snapshot.

* Tue Dec 27 2016 Fabio Valentini <decathorpe@gmail.com> - 0.4.0.1+rev1018-1
- Update to latest snapshot.

* Wed Dec 21 2016 Fabio Valentini <decathorpe@gmail.com> - 0.4.0.1+rev1017-1
- Update to latest snapshot.

* Tue Dec 20 2016 Fabio Valentini <decathorpe@gmail.com> - 0.4.0.1+rev1016-1
- Update to latest snapshot.

* Fri Dec 16 2016 Fabio Valentini <decathorpe@gmail.com> - 0.4.0.1+rev1015-1
- Update to latest snapshot.

* Thu Dec 15 2016 Fabio Valentini <decathorpe@gmail.com> - 0.4.0.1+rev1014-1
- Update to latest snapshot.

* Mon Nov 28 2016 Fabio Valentini <decathorpe@gmail.com> - 0.4.0.1+rev1013-1
- Update to latest snapshot.

* Sat Nov 12 2016 Fabio Valentini <decathorpe@gmail.com> - 0.4.0.1+rev1012-1
- Update to latest snapshot.

* Mon Nov 07 2016 Fabio Valentini <decathorpe@gmail.com> - 0.4.0.1+rev1011-1
- Update to latest snapshot.

* Thu Nov 03 2016 Fabio Valentini <decathorpe@gmail.com> - 0.4.0.1+rev1010-1
- Update to latest snapshot.

* Mon Oct 31 2016 Fabio Valentini <decathorpe@gmail.com> - 0.4.0.1+rev1009-1
- Update to latest snapshot.

* Fri Oct 28 2016 Fabio Valentini <decathorpe@gmail.com> - 0.4.0.1+rev1008-1
- Update to latest snapshot.

* Thu Oct 27 2016 Fabio Valentini <decathorpe@gmail.com> - 0.4.0.1+rev1007-1
- Update to latest snapshot.

* Thu Oct 20 2016 Fabio Valentini <decathorpe@gmail.com> - 0.4.0.1+rev1006-1
- Update to latest snapshot.

* Sun Oct 16 2016 Fabio Valentini <decathorpe@gmail.com> - 0.4.0.1+rev1005-1
- Update to latest snapshot.

* Sat Oct 15 2016 Fabio Valentini <decathorpe@gmail.com> - 0.4.0.1+rev1004-1
- Update to latest snapshot.

* Fri Oct 14 2016 Fabio Valentini <decathorpe@gmail.com> - 0.4.0.1+rev1003-1
- Update to latest snapshot.

* Thu Oct 13 2016 Fabio Valentini <decathorpe@gmail.com> - 0.4.0.1+rev1002-1
- Update to latest snapshot.

* Sun Oct 09 2016 Fabio Valentini <decathorpe@gmail.com> - 0.4.0.1+rev1001-1
- Update to latest snapshot.

* Sat Oct 08 2016 Fabio Valentini <decathorpe@gmail.com> - 0.4.0.1+rev1000-1
- Update to latest snapshot.

* Fri Oct 07 2016 Fabio Valentini <decathorpe@gmail.com> - 0.4.0.1+rev999-1
- Update to latest snapshot.

* Sat Oct 01 2016 Fabio Valentini <decathorpe@gmail.com> - 0.4.0.1+rev998-1
- Update to latest snapshot.

* Fri Sep 30 2016 Fabio Valentini <decathorpe@gmail.com> - 0.4.0.1+rev997-1
- Update to latest snapshot.

* Thu Sep 29 2016 Fabio Valentini <decathorpe@gmail.com> - 0.4.0.1+rev996-2
- Spec file cleanups.

* Thu Sep 29 2016 Fabio Valentini <decathorpe@gmail.com> - 0.4.0.1+rev996-1
- Update to latest snapshot.

* Wed Sep 28 2016 Fabio Valentini <decathorpe@gmail.com> - 0.4.0.1+rev994-1
- Update to latest snapshot.

* Wed Sep 28 2016 Fabio Valentini <decathorpe@gmail.com> - 0.4.0.1+rev992-1
- Update to latest snapshot.

* Sat Sep 24 2016 Fabio Valentini <decathorpe@gmail.com> - 0.4.0.1+rev991-1
- Update to latest snapshot.

* Thu Sep 22 2016 Fabio Valentini <decathorpe@gmail.com> - 0.4.0.1+rev990-1
- Update to latest snapshot.

* Wed Sep 21 2016 Fabio Valentini <decathorpe@gmail.com> - 0.4.0.1+rev989-1
- Update to version 0.4.0.1.

* Mon Sep 12 2016 Fabio Valentini <decathorpe@gmail.com> - 0.4.0.1~rev988-1
- Update to latest snapshot.

* Wed Aug 31 2016 Fabio Valentini <decathorpe@gmail.com> - 0.4.0.1~rev987-1
- Update to latest snapshot.

* Thu Aug 18 2016 Fabio Valentini <decathorpe@gmail.com> - 0.4.0.1~rev986-1
- Update to version 0.4.0.1.

* Thu Aug 11 2016 Fabio Valentini <decathorpe@gmail.com> - 0.4~rev985-1
- Update to latest snapshot.

* Wed Aug 10 2016 Fabio Valentini <decathorpe@gmail.com> - 0.4~rev984-1
- Update to latest snapshot.

* Tue Aug 09 2016 Fabio Valentini <decathorpe@gmail.com> - 0.4~rev983-1
- Update to latest snapshot.

* Mon Aug 08 2016 Fabio Valentini <decathorpe@gmail.com> - 0.4~rev982-1
- Update to latest snapshot.

* Sun Aug 07 2016 Fabio Valentini <decathorpe@gmail.com> - 0.4~rev981-2
- Update for packaging changes.

* Sun Aug 07 2016 Fabio Valentini <decathorpe@gmail.com> - 0.4~rev981-1
- Update to latest snapshot.

* Sat Aug 06 2016 Fabio Valentini <decathorpe@gmail.com> - 0.4~rev979-1
- Update to latest snapshot.

* Fri Aug 05 2016 Fabio Valentini <decathorpe@gmail.com> - 0.4~rev978-1
- Update to latest snapshot.

* Thu Aug 04 2016 Fabio Valentini <decathorpe@gmail.com> - 0.4~rev977-1
- Update to latest snapshot.

* Tue Aug 02 2016 Fabio Valentini <decathorpe@gmail.com> - 0.4~rev975-1
- Update to latest snapshot.

* Mon Aug 01 2016 Fabio Valentini <decathorpe@gmail.com> - 0.4~rev974-1
- Update to latest snapshot.

* Mon Aug 01 2016 Fabio Valentini <decathorpe@gmail.com> - 0.4~rev973-1
- Update to latest snapshot.

* Mon Aug 01 2016 Fabio Valentini <decathorpe@gmail.com> - 0.4~rev972-1
- Update to latest snapshot.

* Sun Jul 31 2016 Fabio Valentini <decathorpe@gmail.com> - 0.4~rev971-1
- Update to latest snapshot.

* Sat Jul 30 2016 Fabio Valentini <decathorpe@gmail.com> - 0.4~rev970-1
- Update to latest snapshot.

* Thu Jul 28 2016 Fabio Valentini <decathorpe@gmail.com> - 0.4~rev969-1
- Update to latest snapshot.

* Tue Jul 26 2016 Fabio Valentini <decathorpe@gmail.com> - 0.4~rev968-1
- Update to latest snapshot.

* Mon Jul 25 2016 Fabio Valentini <decathorpe@gmail.com> - 0.4~rev967-1
- Update to latest snapshot.

* Fri Jul 22 2016 Fabio Valentini <decathorpe@gmail.com> - 0.4~rev966-1
- Update to latest snapshot.

* Thu Jul 21 2016 Fabio Valentini <decathorpe@gmail.com> - 0.4~rev965-1
- Update to latest snapshot.

* Mon Jul 18 2016 Fabio Valentini <decathorpe@gmail.com> - 0.4~rev964-1
- Update to latest snapshot.

* Sun Jul 17 2016 Fabio Valentini <decathorpe@gmail.com> - 0.4~rev963-1
- Update to latest snapshot.

* Fri Jul 08 2016 Fabio Valentini <decathorpe@gmail.com> - 0.4~rev962-1
- Update to latest snapshot.

* Wed Jul 06 2016 Fabio Valentini <decathorpe@gmail.com> - 0.4~rev961-2
- Update for packaging changes.

* Sat Jun 25 2016 Fabio Valentini <decathorpe@gmail.com> - 0.4~rev954-1
- Update to latest snapshot.

* Wed Jun 22 2016 Fabio Valentini <decathorpe@gmail.com> - 0.4~rev952-1
- Update to latest snapshot.

* Sat Jun 18 2016 Fabio Valentini <decathorpe@gmail.com> - 0.4~rev950-1
- Update to latest snapshot.

* Thu Jun 16 2016 Fabio Valentini <decathorpe@gmail.com> - 0.4~rev949-1
- Update to latest snapshot.

* Wed Jun 15 2016 Fabio Valentini <decathorpe@gmail.com> - 0.4~rev948-1
- Update to version 0.4.

* Mon Jun 13 2016 Fabio Valentini <decathorpe@gmail.com> - 0.3.1~rev948-1
- Update to latest snapshot.

* Thu Jun 09 2016 Fabio Valentini <decathorpe@gmail.com> - 0.3.1~rev947-1
- Update to latest snapshot.

* Fri Jun 03 2016 Fabio Valentini <decathorpe@gmail.com> - 0.3.1~rev945-1
- Update to latest snapshot.

* Wed Jun 01 2016 Fabio Valentini <decathorpe@gmail.com> - 0.3.1~rev944-1
- Update to latest snapshot.

* Mon May 30 2016 Fabio Valentini <decathorpe@gmail.com> - 0.3.1~rev943-3
- Update for packaging changes.

* Sun May 29 2016 Fabio Valentini <decathorpe@gmail.com> - 0.3.1~rev943-2
- Update for packaging changes.

* Sat May 21 2016 Fabio Valentini <decathorpe@gmail.com> - 0.3.1~rev943-1
- Update to latest snapshot.

* Wed May 11 2016 Fabio Valentini <decathorpe@gmail.com> - 0.3.1~rev942-1
- Update to latest snapshot.

* Wed May 04 2016 Fabio Valentini <decathorpe@gmail.com> - 0.3.1~rev941-1
- Update to latest snapshot.

* Wed May 04 2016 Fabio Valentini <decathorpe@gmail.com> - 0.3.1~rev941-1
- Update to latest snapshot.

* Mon May 02 2016 Fabio Valentini <decathorpe@gmail.com> - 0.3.1~rev940-2
- Update for packaging changes.

* Mon May 02 2016 Fabio Valentini <decathorpe@gmail.com> - 0.3.1~rev940-1
- Update to new upstream snapshot.

* Sun May 01 2016 Fabio Valentini <decathorpe@gmail.com> - 0.3.1~rev939-1
- Update to new upstream snapshot.

* Sat Apr 30 2016 Fabio Valentini <decathorpe@gmail.com> - 0.3.1~rev938-1
- Update to new upstream snapshot.

* Wed Apr 20 2016 Fabio Valentini <decathorpe@gmail.com> - 0.3.1~rev937-1
- Update to new upstream snapshot.

* Wed Apr 13 2016 Fabio Valentini <decathorpe@gmail.com> - 0.3.1~rev936-1
- Update to new upstream snapshot.

* Tue Apr 12 2016 Fabio Valentini <decathorpe@gmail.com> - 0.3.1~rev935-1
- Update to new upstream snapshot.

* Tue Mar 29 2016 Fabio Valentini <decathorpe@gmail.com> - 0.3.1~rev934-1
- Update to new upstream snapshot.

* Mon Mar 21 2016 Fabio Valentini <decathorpe@gmail.com> - 0.3.1~rev933-1
- Update to new upstream snapshot.

* Sun Mar 13 2016 Fabio Valentini <decathorpe@gmail.com> - 0.3.1~rev931-1
- Update to new upstream snapshot.

* Thu Feb 18 2016 Fabio Valentini <decathorpe@gmail.com> - 0.3.1~rev930-1
- Update to new upstream snapshot.

* Wed Feb 10 2016 Fabio Valentini <decathorpe@gmail.com> - 0.3.1~rev929-1
- Update to new upstream snapshot.

* Wed Feb 03 2016 Fabio Valentini <decathorpe@gmail.com> - 0.3.1~rev928-1
- Update to new upstream snapshot.

* Tue Feb 02 2016 Fabio Valentini <decathorpe@gmail.com> - 0.3.1~rev927-1
- Update to new upstream snapshot.

* Mon Feb 01 2016 Fabio Valentini <decathorpe@gmail.com> - 0.3.1~rev926-1
- Update to new upstream snapshot.

* Fri Jan 29 2016 Fabio Valentini <decathorpe@gmail.com> - 0.3.1~rev925-1
- Update to new upstream snapshot.

* Mon Jan 11 2016 Fabio Valentini <decathorpe@gmail.com> - 0.3.1~rev924-1
- Update to new upstream snapshot.

* Fri Jan 08 2016 Fabio Valentini <decathorpe@gmail.com> - 0.3.1~rev922-1
- Update to new upstream snapshot.

* Fri Jan 01 2016 Fabio Valentini <decathorpe@gmail.com> - 0.3.1~rev920-1
- Update to new upstream snapshot.

* Tue Dec 22 2015 Fabio Valentini <decathorpe@gmail.com> - 0.3.1~rev918-1
- Update to new upstream snapshot.

* Wed Dec 16 2015 Fabio Valentini <decathorpe@gmail.com> - 0.3.1~rev917-1
- Update to new upstream snapshot.

* Tue Dec 15 2015 Fabio Valentini <decathorpe@gmail.com> - 0.3.1~rev916-1
- Update to new upstream snapshot.

* Sun Dec 13 2015 Fabio Valentini <decathorpe@gmail.com> - 0.3.1~rev914-1
- Update to new upstream snapshot.

* Sat Dec 12 2015 Fabio Valentini <decathorpe@gmail.com> - 0.3.1~rev913-1
- Update to new upstream snapshot.

* Tue Dec 08 2015 Fabio Valentini <decathorpe@gmail.com> - 0.3.1~rev912-1
- Update to new upstream snapshot.

* Sun Dec 06 2015 Fabio Valentini <decathorpe@gmail.com> - 0.3.1~rev911-1
- Update to new upstream snapshot.

* Thu Dec 03 2015 Fabio Valentini <decathorpe@gmail.com> - 0.3.1~rev907-1
- Update to new upstream snapshot.

* Mon Nov 30 2015 Fabio Valentini <decathorpe@gmail.com> - 0.3.1~rev906-1
- Update to new upstream snapshot.

* Sat Nov 28 2015 Fabio Valentini <decathorpe@gmail.com> - 0.3.1~rev905-1
- Update to new upstream snapshot.

* Fri Nov 27 2015 Fabio Valentini <decathorpe@gmail.com> - 0.3.1~rev904-1
- Update to new upstream snapshot.

* Thu Nov 26 2015 Fabio Valentini <decathorpe@gmail.com> - 0.3.1~rev902-1
- Update to new upstream snapshot.

* Fri Nov 20 2015 Fabio Valentini <decathorpe@gmail.com> - 0.3.1~rev900-1
- Update to new upstream snapshot.

* Thu Nov 19 2015 Fabio Valentini <decathorpe@gmail.com> - 0.3.1~rev899-1
- Update to new upstream snapshot.

* Sun Nov 15 2015 Fabio Valentini <decathorpe@gmail.com> - 0.3.1~rev894-1
- Update to new upstream snapshot.

* Fri Nov 13 2015 Fabio Valentini <decathorpe@gmail.com> - 0.3.1~rev893-1
- Update to new upstream snapshot.

* Wed Nov 11 2015 Fabio Valentini <decathorpe@gmail.com> - 0.3.1~rev892-1
- Update to new upstream snapshot.

* Tue Nov 03 2015 Fabio Valentini <decathorpe@gmail.com> - 0.3.1~rev891-1
- Update to new upstream snapshot.

* Mon Oct 26 2015 Fabio Valentini <decathorpe@gmail.com> - 0.3.1~rev890-1
- Update to new upstream snapshot.

* Fri Oct 23 2015 Fabio Valentini <decathorpe@gmail.com> - 0.3.1~rev889-1
- Update to new upstream snapshot.

* Thu Oct 22 2015 Fabio Valentini <decathorpe@gmail.com> - 0.3.1~rev888-1
- Update to new upstream snapshot.

* Tue Oct 20 2015 Fabio Valentini <decathorpe@gmail.com> - 0.3.1~rev887-1
- Update to new upstream snapshot.

* Sat Oct 17 2015 Fabio Valentini <decathorpe@gmail.com> - 0.3.1~rev886-1
- Update to new upstream snapshot.

* Wed Oct 14 2015 Fabio Valentini <decathorpe@gmail.com> - 0.3.1~rev885-1
- Update to new upstream snapshot.

* Mon Oct 12 2015 Fabio Valentini <decathorpe@gmail.com> - 0.3.1~rev883-1
- Update to new upstream snapshot.

* Sat Oct 10 2015 Fabio Valentini <decathorpe@gmail.com> - 0.3.1~rev882-1
- Update to new upstream snapshot.

* Thu Oct 08 2015 Fabio Valentini <decathorpe@gmail.com> - 0.3.1~rev880-1
- Update to new upstream snapshot.

* Wed Oct 07 2015 Fabio Valentini <decathorpe@gmail.com> - 0.3.1~rev879-1
- Update to new upstream snapshot.

* Sat Oct 03 2015 Fabio Valentini <decathorpe@gmail.com> - 0.3.1~rev878-1
- Update to new upstream snapshot.

* Fri Oct 02 2015 Fabio Valentini <decathorpe@gmail.com> - 0.3.1~rev877-1
- Update to new upstream snapshot.

* Tue Sep 29 2015 Fabio Valentini <decathorpe@gmail.com> - 0.3.1~rev876-1
- Update to new upstream snapshot.

* Mon Sep 21 2015 Fabio Valentini <decathorpe@gmail.com> - 0.3.1~rev875-1
- Update to new upstream snapshot.

* Mon Sep 07 2015 Fabio Valentini <decathorpe@gmail.com> - 0.3.1~rev874-1
- Update to new upstream snapshot.

* Sun Sep 06 2015 Fabio Valentini <decathorpe@gmail.com> - 0.3.1~rev873-1
- Update to new upstream snapshot.

* Thu Sep 03 2015 Fabio Valentini <decathorpe@gmail.com> - 0.3.1~rev872-2
- Update spec for soname bump.

* Thu Sep 03 2015 Fabio Valentini <decathorpe@gmail.com> - 0.3.1~rev872-1
- Bump version to 0.3.1.

* Thu Sep 03 2015 Fabio Valentini <decathorpe@gmail.com> - 0.3.0~rev872-1
- Update to new upstream snapshot.

* Tue Sep 01 2015 Fabio Valentini <decathorpe@gmail.com> - 0.3.0~rev871-1
- Update to new upstream snapshot.

* Wed Aug 26 2015 Fabio Valentini <decathorpe@gmail.com> - 0.3.0~rev866-1
- Update to new upstream snapshot.

* Mon Aug 24 2015 Fabio Valentini <decathorpe@gmail.com> - 0.3.0~rev865-1
- Update to new upstream snapshot.

* Thu Aug 20 2015 Fabio Valentini <decathorpe@gmail.com> - 0.3.0~rev864-1
- Update to new upstream snapshot.

* Thu Jun 25 2015 Fabio Valentini <decathorpe@gmail.com> - 0.3.0~rev861-1
- Update to bzr snapshot revno861.

* Sat Mar 07 2015 Fabio Valentini <decathorpe@gmail.com> - 0.3.0~rev839-5
- Update to latest bzr snapshot.

* Sun Feb 08 2015 Fabio Valentini <decathorpe@gmail.com> - 0.3.0~rev831-4
- Update to latest bzr snapshot.

* Sun Feb 01 2015 Fabio Valentini <decathorpe@gmail.com> - 0.3.0~rev829-3
- Update to latest bzr snapshot.

* Thu Jan 08 2015 Fabio Valentini <fafatheone@gmail.com> - 0.3.0~rev826-2
- Update to latest bzr snapshot.

* Mon Jan 05 2015 Fabio Valentini <fafatheone@gmail.com> - 0.3.0~rev825-1
- Fix upstream version.

* Sat Jan 03 2015 Fabio Valentini <fafatheone@gmail.com> - 0.2.3~rev825-1
- Initial package (new).


