%global __provides_exclude_from ^%{_libdir}/io.elementary.photos/.*\\.so$

Summary:        The elementary continuation of Shotwell
Name:           pantheon-photos
Version:        0.2.4+git%{date}.%{commit}
Release:        2%{?dist}
License:        LGPLv2.1

URL:            http://github.com/elementary/photos
Source0:        %{name}-%{version}.tar.gz
Source1:        %{name}.conf

BuildRequires:  cmake
BuildRequires:  desktop-file-utils
BuildRequires:  gettext
BuildRequires:  intltool
BuildRequires:  libappstream-glib
BuildRequires:  vala

BuildRequires:  pkgconfig(gee-0.8)
BuildRequires:  pkgconfig(geocode-glib-1.0)
BuildRequires:  pkgconfig(gexiv2)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(granite)
BuildRequires:  pkgconfig(gstreamer-1.0)
BuildRequires:  pkgconfig(gstreamer-base-1.0)
BuildRequires:  pkgconfig(gstreamer-plugins-base-1.0)
BuildRequires:  pkgconfig(gstreamer-pbutils-1.0)
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.10
BuildRequires:  pkgconfig(gudev-1.0) >= 145
BuildRequires:  pkgconfig(json-glib-1.0)
BuildRequires:  pkgconfig(libgphoto2) >= 2.4.2
BuildRequires:  pkgconfig(libexif) >= 0.6.16
BuildRequires:  pkgconfig(libraw) >= 0.13.2
BuildRequires:  pkgconfig(libsoup-2.4) >= 2.26.0
BuildRequires:  pkgconfig(libwebp) >= 0.4.4
BuildRequires:  pkgconfig(libxml-2.0) >= 2.6.32
BuildRequires:  pkgconfig(rest-0.7) >= 0.7
BuildRequires:  pkgconfig(sqlite3) >= 3.5.9
BuildRequires:  pkgconfig(unity) >= 4.0.0
BuildRequires:  pkgconfig(webkit2gtk-4.0) >= 2.0.0


%description
The elementary continuation of Shotwell, originally written by Yorba
Foundation.

Designed for elementary OS. Works and looks great on any GTK+ desktop.


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

%find_lang io.elementary.photos


%check
desktop-file-validate \
    %{buildroot}/%{_datadir}/applications/*.desktop

appstream-util validate-relax --nonet \
    %{buildroot}/%{_datadir}/appdata/*.appdata.xml || :


%files -f io.elementary.photos.lang
%doc AUTHORS README.md THANKS
%license COPYING

%{_bindir}/io.elementary.photos

%{_libdir}/io.elementary.photos/

%{_libexecdir}/io.elementary.photos/

%{_datadir}/applications/org.pantheon.photos.desktop
%{_datadir}/applications/org.pantheon.photos-viewer.desktop
%{_datadir}/glib-2.0/schemas/org.pantheon.photos.gschema.xml
%{_datadir}/glib-2.0/schemas/org.pantheon.photos-extras.gschema.xml
%{_datadir}/metainfo/io.elementary.photos.appdata.xml
%{_datadir}/io.elementary.photos/


%changelog
* Sat Dec 30 2017 Fabio Valentini <decathorpe@gmail.com> - 0.2.4+git171229.222002.65512d02-2
- Adapt to upstream file changes.

* Sat Dec 30 2017 Fabio Valentini <decathorpe@gmail.com> - 0.2.4+git171229.222002.65512d02-1
- Update to latest snapshot.

* Sun Dec 24 2017 Fabio Valentini <decathorpe@gmail.com> - 0.2.4+git171221.202056.81c23195-1
- Update to latest snapshot.

* Wed Dec 20 2017 Fabio Valentini <decathorpe@gmail.com> - 0.2.4+git171220.211427.7a2cf3e8-1
- Update to latest snapshot.

* Wed Dec 20 2017 Fabio Valentini <decathorpe@gmail.com> - 0.2.4+git171220.171907.7a219b7e-1
- Update to latest snapshot.

* Wed Dec 20 2017 Fabio Valentini <decathorpe@gmail.com> - 0.2.4+git171220.132050.f232e93e-1
- Update to latest snapshot.

* Wed Dec 20 2017 Fabio Valentini <decathorpe@gmail.com> - 0.2.4+git171220.114416.c48e6d9f-1
- Update to latest snapshot.

* Wed Dec 20 2017 Fabio Valentini <decathorpe@gmail.com> - 0.2.4+git171219.234735.fddf8aa9-1
- Update to latest snapshot.

* Tue Dec 19 2017 Fabio Valentini <decathorpe@gmail.com> - 0.2.4+git171219.194839.6806746e-1
- Update to latest snapshot.

* Tue Dec 19 2017 Fabio Valentini <decathorpe@gmail.com> - 0.2.4+git171219.184123.c04e75c1-1
- Update to latest snapshot.

* Tue Dec 19 2017 Fabio Valentini <decathorpe@gmail.com> - 0.2.4+git171219.174050.417132ab-1
- Update to latest snapshot.

* Mon Dec 18 2017 Fabio Valentini <decathorpe@gmail.com> - 0.2.4+git171218.020954.148cd06b-1
- Update to latest snapshot.

* Sun Dec 17 2017 Fabio Valentini <decathorpe@gmail.com> - 0.2.4+git171217.012405.313c8b13-1
- Update to latest snapshot.

* Tue Dec 12 2017 Fabio Valentini <decathorpe@gmail.com> - 0.2.4+git171212.005334.6887d8e4-1
- Update to latest snapshot.

* Sun Dec 10 2017 Fabio Valentini <decathorpe@gmail.com> - 0.2.4+git171210.200206.765a68d9-1
- Update to latest snapshot.

* Sun Dec 10 2017 Fabio Valentini <decathorpe@gmail.com> - 0.2.4+git171210.194954.efac2a41-1
- Update to latest snapshot.

* Sun Dec 10 2017 Fabio Valentini <decathorpe@gmail.com> - 0.2.4+git171210.175204.bb4cd589-1
- Update to latest snapshot.

* Sun Dec 10 2017 Fabio Valentini <decathorpe@gmail.com> - 0.2.4+git171210.010039.b9b1afae-1
- Update to latest snapshot.

* Wed Dec 06 2017 Fabio Valentini <decathorpe@gmail.com> - 0.2.4+git171205.235618.97f2a985-1
- Update to latest snapshot.

* Tue Dec 05 2017 Fabio Valentini <decathorpe@gmail.com> - 0.2.4+git171205.170741.5411b705-1
- Update to latest snapshot.

* Tue Dec 05 2017 Fabio Valentini <decathorpe@gmail.com> - 0.2.4+git171205.165802.586b9b0a-1
- Update to latest snapshot.

* Sun Dec 03 2017 Fabio Valentini <decathorpe@gmail.com> - 0.2.4+git171203.041147.0351a943-1
- Update to latest snapshot.

* Sat Dec 02 2017 Fabio Valentini <decathorpe@gmail.com> - 0.2.4+git171202.020128.eab61375-1
- Update to latest snapshot.

* Fri Dec 01 2017 Fabio Valentini <decathorpe@gmail.com> - 0.2.4+git171201.061855.de6763a9-1
- Update to latest snapshot.

* Wed Nov 29 2017 Fabio Valentini <decathorpe@gmail.com> - 0.2.4+git171129.184233.f4d96967-1
- Update to latest snapshot.

* Mon Nov 27 2017 Fabio Valentini <decathorpe@gmail.com> - 0.2.4+git171127.180808.41676b07-1
- Update to latest snapshot.

* Mon Nov 20 2017 Fabio Valentini <decathorpe@gmail.com> - 0.2.4+git171120.111908.172f55b5-1
- Update to latest snapshot.

* Sat Nov 18 2017 Fabio Valentini <decathorpe@gmail.com> - 0.2.4+git171118.184318.4c6ef1c7-1
- Update to latest snapshot.

* Fri Nov 17 2017 Fabio Valentini <decathorpe@gmail.com> - 0.2.4+git171116.234109.7081ab92-1
- Update to latest snapshot.

* Tue Nov 14 2017 Fabio Valentini <decathorpe@gmail.com> - 0.2.4+git171114.004000.1753a7c6-1
- Update to latest snapshot.

* Mon Nov 13 2017 Fabio Valentini <decathorpe@gmail.com> - 0.2.4+git171113.115355.2f9602d6-1
- Update to latest snapshot.

* Mon Nov 13 2017 Fabio Valentini <decathorpe@gmail.com> - 0.2.4+git171112.220933.7849b2bb-1
- Update to latest snapshot.

* Sun Nov 12 2017 Fabio Valentini <decathorpe@gmail.com> - 0.2.4+git171112.175623.f0ca2641-1
- Update to latest snapshot.

* Thu Nov 09 2017 Fabio Valentini <decathorpe@gmail.com> - 0.2.4+git171109.005629.ed5e8b71-1
- Update to latest snapshot.

* Tue Nov 07 2017 Fabio Valentini <decathorpe@gmail.com> - 0.2.4+git171107.171552.ac4fe399-1
- Update to latest snapshot.

* Tue Nov 07 2017 Fabio Valentini <decathorpe@gmail.com> - 0.2.4+git171106.214452.e1f063e2-1
- Update to latest snapshot.

* Mon Nov 06 2017 Fabio Valentini <decathorpe@gmail.com> - 0.2.4+git171106.012938.5823f7f6-1
- Update to latest snapshot.

* Thu Nov 02 2017 Fabio Valentini <decathorpe@gmail.com> - 0.2.4+git171101.210854.d608fa59-1
- Update to latest snapshot.

* Tue Oct 24 2017 Fabio Valentini <decathorpe@gmail.com> - 0.2.4+git171024.160335.7ef493de-1
- Update to latest snapshot.

* Sun Oct 22 2017 Fabio Valentini <decathorpe@gmail.com> - 0.2.4+git171021.183729.b5504040-1
- Update to latest snapshot.

* Wed Oct 18 2017 Fabio Valentini <decathorpe@gmail.com> - 0.2.4+git171017.231508.0abaea16-2
- Adapt to upstream dependency changes.

* Wed Oct 18 2017 Fabio Valentini <decathorpe@gmail.com> - 0.2.4+git171017.231508.0abaea16-1
- Update to latest snapshot.

* Tue Oct 17 2017 Fabio Valentini <decathorpe@gmail.com> - 0.2.4+git171016.235439.364c72ac-1
- Update to latest snapshot.

* Mon Oct 16 2017 Fabio Valentini <decathorpe@gmail.com> - 0.2.4+git171015.204943.1f4a4235-1
- Update to latest snapshot.

* Sun Oct 15 2017 Fabio Valentini <decathorpe@gmail.com> - 0.2.4+git171015.162627.8b4bc2d3-1
- Update to latest snapshot.

* Sun Oct 15 2017 Fabio Valentini <decathorpe@gmail.com> - 0.2.4+git171015.114421.71bac91e-1
- Update to latest snapshot.

* Thu Oct 12 2017 Fabio Valentini <decathorpe@gmail.com> - 0.2.4+git171011.233232.7ad9e613-1
- Update to latest snapshot.

* Wed Aug 30 2017 Fabio Valentini <decathorpe@gmail.com> - 0.2.4+git170830.162226.bbe7e06d-1
- Update to latest snapshot.

* Thu Aug 24 2017 Fabio Valentini <decathorpe@gmail.com> - 0.2.4+git170823.210739.0a8c7bbb-1
- Update to latest snapshot.

* Wed Aug 23 2017 Fabio Valentini <decathorpe@gmail.com> - 0.2.4+git170823.032728.e2876555-1
- Update to latest snapshot.

* Fri Aug 18 2017 Fabio Valentini <decathorpe@gmail.com> - 0.2.4+git170817.221850.ea8e1906-1
- Update to latest snapshot.

* Wed Aug 16 2017 Fabio Valentini <decathorpe@gmail.com> - 0.2.4+git170816.171538.189833c6-1
- Update to latest snapshot.

* Wed Aug 16 2017 Fabio Valentini <decathorpe@gmail.com> - 0.2.4+git170815.205907.f118913e-1
- Update to latest snapshot.

* Tue Aug 15 2017 Fabio Valentini <decathorpe@gmail.com> - 0.2.4+git170815.191523.cfedf03e-1
- Update to latest snapshot.

* Fri Jul 28 2017 Fabio Valentini <decathorpe@gmail.com> - 0.2.4+git170728.022623.e093c8d5-1
- Update to version 0.2.4.

* Fri Jul 28 2017 Fabio Valentini <decathorpe@gmail.com> - 0.2.2+rev3250-1
- Update to latest snapshot.

* Sat Jul 08 2017 Fabio Valentini <decathorpe@gmail.com> - 0.2.2+rev3244-1
- Update to latest snapshot.

* Fri Jul 07 2017 Fabio Valentini <decathorpe@gmail.com> - 0.2.2+rev3237-1
- Update to latest snapshot.

* Sun Jul 02 2017 Fabio Valentini <decathorpe@gmail.com> - 0.2.2+rev3233-1
- Update to latest snapshot.

* Sun Jun 18 2017 Fabio Valentini <decathorpe@gmail.com> - 0.2.2+rev3227-1
- Update to latest snapshot.

* Thu May 04 2017 Fabio Valentini <decathorpe@gmail.com> - 0.2.2+rev3209-1
- Update to latest snapshot.

* Tue May 02 2017 Fabio Valentini <decathorpe@gmail.com> - 0.2.2+rev3193-1
- Update to latest snapshot.

* Fri Apr 28 2017 Fabio Valentini <decathorpe@gmail.com> - 0.2.2+rev3192-1
- Update to latest snapshot.

* Thu Apr 27 2017 Fabio Valentini <decathorpe@gmail.com> - 0.2.2+rev3191-1
- Update to latest snapshot.

* Tue Apr 25 2017 Fabio Valentini <decathorpe@gmail.com> - 0.2.2+rev3190-1
- Update to latest snapshot.

* Mon Apr 24 2017 Fabio Valentini <decathorpe@gmail.com> - 0.2.2+rev3189-2
- Adapt to upstream changes.

* Mon Apr 17 2017 Fabio Valentini <decathorpe@gmail.com> - 0.2.2+rev3188-1
- Update to latest snapshot.

* Sat Apr 15 2017 Fabio Valentini <decathorpe@gmail.com> - 0.2.2+rev3187-1
- Update to latest snapshot.

* Fri Apr 14 2017 Fabio Valentini <decathorpe@gmail.com> - 0.2.2+rev3186-1
- Update to latest snapshot.

* Sat Apr 08 2017 Fabio Valentini <decathorpe@gmail.com> - 0.2.2+rev3185-1
- Update to latest snapshot.

* Fri Apr 07 2017 Fabio Valentini <decathorpe@gmail.com> - 0.2.2+rev3184-1
- Update to latest snapshot.

* Wed Apr 05 2017 Fabio Valentini <decathorpe@gmail.com> - 0.2.2+rev3183-1
- Update to latest snapshot.

* Wed Mar 29 2017 Fabio Valentini <decathorpe@gmail.com> - 0.2.2+rev3182-1
- Update to latest snapshot.

* Wed Mar 22 2017 Fabio Valentini <decathorpe@gmail.com> - 0.2.2+rev3181-1
- Update to latest snapshot.

* Mon Mar 20 2017 Fabio Valentini <decathorpe@gmail.com> - 0.2.2+rev3180-1
- Update to latest snapshot.

* Sun Mar 19 2017 Fabio Valentini <decathorpe@gmail.com> - 0.2.2+rev3179-1
- Update to version 0.2.2.

* Sun Mar 19 2017 Fabio Valentini <decathorpe@gmail.com> - 0.2.1+rev3179-1
- Update to latest snapshot.

* Sun Mar 19 2017 Fabio Valentini <decathorpe@gmail.com> - 0.2.1+rev3177-1
- Update to latest snapshot.

* Wed Mar 15 2017 Fabio Valentini <decathorpe@gmail.com> - 0.2.1+rev3176-1
- Update to latest snapshot.

* Tue Mar 14 2017 Fabio Valentini <decathorpe@gmail.com> - 0.2.1+rev3175-1
- Update to latest snapshot.

* Mon Mar 13 2017 Fabio Valentini <decathorpe@gmail.com> - 0.2.1+rev3174-1
- Update to latest snapshot.

* Thu Mar 02 2017 Fabio Valentini <decathorpe@gmail.com> - 0.2.1+rev3173-1
- Update to latest snapshot.

* Tue Feb 28 2017 Fabio Valentini <decathorpe@gmail.com> - 0.2.1+rev3172-1
- Update to latest snapshot.

* Mon Feb 27 2017 Fabio Valentini <decathorpe@gmail.com> - 0.2.1+rev3171-1
- Update to latest snapshot.

* Sat Feb 25 2017 Fabio Valentini <decathorpe@gmail.com> - 0.2.1+rev3170-1
- Update to latest snapshot.

* Thu Feb 23 2017 Fabio Valentini <decathorpe@gmail.com> - 0.2.1+rev3169-1
- Update to latest snapshot.

* Wed Feb 22 2017 Fabio Valentini <decathorpe@gmail.com> - 0.2.1+rev3168-1
- Update to latest snapshot.

* Mon Feb 20 2017 Fabio Valentini <decathorpe@gmail.com> - 0.2.1+rev3167-1
- Update to latest snapshot.

* Sat Feb 18 2017 Fabio Valentini <decathorpe@gmail.com> - 0.2.1+rev3166-1
- Update to latest snapshot.

* Fri Feb 17 2017 Fabio Valentini <decathorpe@gmail.com> - 0.2.1+rev3163-1
- Update to latest snapshot.

* Wed Feb 15 2017 Fabio Valentini <decathorpe@gmail.com> - 0.2.1+rev3161-1
- Update to latest snapshot.

* Wed Feb 15 2017 Fabio Valentini <decathorpe@gmail.com> - 0.2.1+rev3160-1
- Update to latest snapshot.

* Mon Feb 13 2017 Fabio Valentini <decathorpe@gmail.com> - 0.2.1+rev3159-1
- Update to latest snapshot.

* Sun Feb 12 2017 Fabio Valentini <decathorpe@gmail.com> - 0.2.1+rev3158-1
- Update to latest snapshot.

* Sat Feb 11 2017 Fabio Valentini <decathorpe@gmail.com> - 0.2.1+rev3156-3
- Fix build: Add new binary in libexec.

* Sat Feb 11 2017 Fabio Valentini <decathorpe@gmail.com> - 0.2.1+rev3156-2
- Fix build: Move appdata to approved location.

* Sat Feb 11 2017 Fabio Valentini <decathorpe@gmail.com> - 0.2.1+rev3156-1
- Update to latest snapshot.

* Fri Feb 10 2017 Fabio Valentini <decathorpe@gmail.com> - 0.2.1+rev3155-1
- Update to latest snapshot.

* Thu Feb 09 2017 Fabio Valentini <decathorpe@gmail.com> - 0.2.1+rev3154-1
- Update to latest snapshot.

* Wed Feb 08 2017 Fabio Valentini <decathorpe@gmail.com> - 0.2.1+rev3153-1
- Update to latest snapshot.

* Tue Feb 07 2017 Fabio Valentini <decathorpe@gmail.com> - 0.2.1+rev3152-1
- Update to latest snapshot.

* Mon Feb 06 2017 Fabio Valentini <decathorpe@gmail.com> - 0.2.1+rev3151-1
- Update to latest snapshot.

* Sat Feb 04 2017 Fabio Valentini <decathorpe@gmail.com> - 0.2.1+rev3150-1
- Update to latest snapshot.

* Thu Feb 02 2017 Fabio Valentini <decathorpe@gmail.com> - 0.2.1+rev3149-1
- Update to latest snapshot.

* Wed Feb 01 2017 Fabio Valentini <decathorpe@gmail.com> - 0.2.1+rev3148-1
- Update to latest snapshot.

* Tue Jan 31 2017 Fabio Valentini <decathorpe@gmail.com> - 0.2.1+rev3147-1
- Update to latest snapshot.

* Mon Jan 30 2017 Fabio Valentini <decathorpe@gmail.com> - 0.2.1+rev3146-1
- Update to latest snapshot.

* Mon Jan 30 2017 Fabio Valentini <decathorpe@gmail.com> - 0.2.1+rev3145-1
- Update to latest snapshot.

* Mon Jan 30 2017 Fabio Valentini <decathorpe@gmail.com> - 0.2.1+rev3143-1
- Update to latest snapshot.

* Sun Jan 29 2017 Fabio Valentini <decathorpe@gmail.com> - 0.2.1+rev3142-1
- Update to latest snapshot.

* Sat Jan 28 2017 Fabio Valentini <decathorpe@gmail.com> - 0.2.1+rev3141-1
- Update to latest snapshot.

* Fri Jan 27 2017 Fabio Valentini <decathorpe@gmail.com> - 0.2.1+rev3139-1
- Update to latest snapshot.

* Thu Jan 26 2017 Fabio Valentini <decathorpe@gmail.com> - 0.2.1+rev3134-1
- Update to latest snapshot.

* Thu Jan 26 2017 Fabio Valentini <decathorpe@gmail.com> - 0.2.1+rev3133-1
- Update to latest snapshot.

* Thu Jan 26 2017 Fabio Valentini <decathorpe@gmail.com> - 0.2.1+rev3132-1
- Update to latest snapshot.

* Thu Jan 26 2017 Fabio Valentini <decathorpe@gmail.com> - 0.2.1+rev3130-1
- Update to latest snapshot.

* Wed Jan 25 2017 Fabio Valentini <decathorpe@gmail.com> - 0.2.1+rev3129-1
- Update to latest snapshot.

* Wed Jan 25 2017 Fabio Valentini <decathorpe@gmail.com> - 0.2.1+rev3127-1
- Update to latest snapshot.

* Mon Jan 23 2017 Fabio Valentini <decathorpe@gmail.com> - 0.2.1+rev3124-1
- Update to latest snapshot.

* Sun Jan 22 2017 Fabio Valentini <decathorpe@gmail.com> - 0.2.1+rev3123-1
- Update to latest snapshot.

* Sat Jan 21 2017 Fabio Valentini <decathorpe@gmail.com> - 0.2.1+rev3121-1
- Update to latest snapshot.

* Wed Jan 18 2017 Fabio Valentini <decathorpe@gmail.com> - 0.2.1+rev3120-1
- Update to latest snapshot.

* Tue Jan 17 2017 Fabio Valentini <decathorpe@gmail.com> - 0.2.1+rev3119-1
- Update to version 0.2.1.

* Tue Jan 17 2017 Fabio Valentini <decathorpe@gmail.com> - 0.2+rev3119-1
- Update to latest snapshot.

* Mon Jan 16 2017 Fabio Valentini <decathorpe@gmail.com> - 0.2+rev3118-1
- Update to latest snapshot.

* Sun Jan 15 2017 Fabio Valentini <decathorpe@gmail.com> - 0.2+rev3115-1
- Update to latest snapshot.

* Sat Jan 14 2017 Fabio Valentini <decathorpe@gmail.com> - 0.2+rev3111-1
- Update to latest snapshot.

* Sat Jan 14 2017 Fabio Valentini <decathorpe@gmail.com> - 0.2+rev3110-1
- Update to latest snapshot.

* Sat Jan 14 2017 Fabio Valentini <decathorpe@gmail.com> - 0.2+rev3109-1
- Update to latest snapshot.

* Thu Jan 12 2017 Fabio Valentini <decathorpe@gmail.com> - 0.2+rev3108-1
- Update to latest snapshot.

* Wed Jan 11 2017 Fabio Valentini <decathorpe@gmail.com> - 0.2+rev3107-1
- Update to latest snapshot.

* Sun Jan 08 2017 Fabio Valentini <decathorpe@gmail.com> - 0.2+rev3106-1
- Update to latest snapshot.

* Sat Jan 07 2017 Fabio Valentini <decathorpe@gmail.com> - 0.2+rev3105-1
- Update to latest snapshot.

* Fri Jan 06 2017 Fabio Valentini <decathorpe@gmail.com> - 0.2+rev3104-1
- Update to latest snapshot.

* Wed Jan 04 2017 Fabio Valentini <decathorpe@gmail.com> - 0.2+rev3103-1
- Update to latest snapshot.

* Tue Jan 03 2017 Fabio Valentini <decathorpe@gmail.com> - 0.2+rev3102-1
- Update to latest snapshot.

* Tue Jan 03 2017 Fabio Valentini <decathorpe@gmail.com> - 0.2+rev3101-1
- Update to latest snapshot.

* Tue Jan 03 2017 Fabio Valentini <decathorpe@gmail.com> - 0.2+rev3100-1
- Update to latest snapshot.

* Mon Jan 02 2017 Fabio Valentini <decathorpe@gmail.com> - 0.2+rev3098-1
- Update to latest snapshot.

* Sun Jan 01 2017 Fabio Valentini <decathorpe@gmail.com> - 0.2+rev3096-1
- Update to latest snapshot.

* Sat Dec 31 2016 Fabio Valentini <decathorpe@gmail.com> - 0.2+rev3095-1
- Update to latest snapshot.

* Thu Dec 29 2016 Fabio Valentini <decathorpe@gmail.com> - 0.2+rev3094-1
- Update to latest snapshot.

* Wed Dec 28 2016 Fabio Valentini <decathorpe@gmail.com> - 0.2+rev3093-1
- Update to latest snapshot.

* Tue Dec 27 2016 Fabio Valentini <decathorpe@gmail.com> - 0.2+rev3092-1
- Update to latest snapshot.

* Mon Dec 26 2016 Fabio Valentini <decathorpe@gmail.com> - 0.2+rev3091-1
- Update to latest snapshot.

* Sun Dec 25 2016 Fabio Valentini <decathorpe@gmail.com> - 0.2+rev3090-1
- Update to latest snapshot.

* Sat Dec 24 2016 Fabio Valentini <decathorpe@gmail.com> - 0.2+rev3089-2
- Add libunity support.

* Wed Dec 21 2016 Fabio Valentini <decathorpe@gmail.com> - 0.2+rev3089-1
- Update to latest snapshot.

* Tue Dec 20 2016 Fabio Valentini <decathorpe@gmail.com> - 0.2+rev3088-1
- Update to latest snapshot.

* Sun Dec 18 2016 Fabio Valentini <decathorpe@gmail.com> - 0.2+rev3087-1
- Update to latest snapshot.

* Sat Dec 17 2016 Fabio Valentini <decathorpe@gmail.com> - 0.2+rev3086-1
- Update to latest snapshot.

* Fri Dec 16 2016 Fabio Valentini <decathorpe@gmail.com> - 0.2+rev3085-1
- Update to latest snapshot.

* Thu Dec 15 2016 Fabio Valentini <decathorpe@gmail.com> - 0.2+rev3084-1
- Update to latest snapshot.

* Wed Dec 14 2016 Fabio Valentini <decathorpe@gmail.com> - 0.2+rev3083-1
- Update to latest snapshot.

* Tue Dec 13 2016 Fabio Valentini <decathorpe@gmail.com> - 0.2+rev3082-1
- Update to latest snapshot.

* Fri Dec 09 2016 Fabio Valentini <decathorpe@gmail.com> - 0.2+rev3081-1
- Update to latest snapshot.

* Sun Dec 04 2016 Fabio Valentini <decathorpe@gmail.com> - 0.2+rev3080-1
- Update to latest snapshot.

* Fri Dec 02 2016 Fabio Valentini <decathorpe@gmail.com> - 0.2+rev3079-1
- Update to latest snapshot.

* Thu Dec 01 2016 Fabio Valentini <decathorpe@gmail.com> - 0.2+rev3078-1
- Update to latest snapshot.

* Wed Nov 30 2016 Fabio Valentini <decathorpe@gmail.com> - 0.2+rev3076-1
- Update to latest snapshot.

* Tue Nov 29 2016 Fabio Valentini <decathorpe@gmail.com> - 0.2+rev3075-1
- Update to latest snapshot.

* Mon Nov 28 2016 Fabio Valentini <decathorpe@gmail.com> - 0.2+rev3074-1
- Update to latest snapshot.

* Sat Nov 26 2016 Fabio Valentini <decathorpe@gmail.com> - 0.2+rev3073-1
- Update to latest snapshot.

* Wed Nov 23 2016 Fabio Valentini <decathorpe@gmail.com> - 0.2+rev3071-1
- Update to latest snapshot.

* Tue Nov 22 2016 Fabio Valentini <decathorpe@gmail.com> - 0.2+rev3070-1
- Update to latest snapshot.

* Mon Nov 21 2016 Fabio Valentini <decathorpe@gmail.com> - 0.2+rev3067-1
- Update to latest snapshot.

* Sun Nov 20 2016 Fabio Valentini <decathorpe@gmail.com> - 0.2+rev3064-1
- Update to latest snapshot.

* Sat Nov 19 2016 Fabio Valentini <decathorpe@gmail.com> - 0.2+rev3063-1
- Update to latest snapshot.

* Sat Nov 19 2016 Fabio Valentini <decathorpe@gmail.com> - 0.2+rev3062-2
- Add missing new BR: geocode-glib-1.0.

* Sat Nov 19 2016 Fabio Valentini <decathorpe@gmail.com> - 0.2+rev3062-1
- Update to latest snapshot.

* Thu Nov 17 2016 Fabio Valentini <decathorpe@gmail.com> - 0.2+rev3058-1
- Update to latest snapshot.

* Thu Nov 17 2016 Fabio Valentini <decathorpe@gmail.com> - 0.2+rev3057-1
- Update to latest snapshot.

* Tue Nov 15 2016 Fabio Valentini <decathorpe@gmail.com> - 0.2+rev3056-1
- Update to latest snapshot.

* Mon Nov 14 2016 Fabio Valentini <decathorpe@gmail.com> - 0.2+rev3055-1
- Update to latest snapshot.

* Sat Nov 12 2016 Fabio Valentini <decathorpe@gmail.com> - 0.2+rev3054-1
- Update to latest snapshot.

* Fri Nov 11 2016 Fabio Valentini <decathorpe@gmail.com> - 0.2+rev3052-1
- Update to latest snapshot.

* Wed Nov 09 2016 Fabio Valentini <decathorpe@gmail.com> - 0.2+rev3051-1
- Update to latest snapshot.

* Tue Nov 08 2016 Fabio Valentini <decathorpe@gmail.com> - 0.2+rev3050-1
- Update to latest snapshot.

* Mon Nov 07 2016 Fabio Valentini <decathorpe@gmail.com> - 0.2+rev3049-1
- Update to latest snapshot.

* Sun Nov 06 2016 Fabio Valentini <decathorpe@gmail.com> - 0.2+rev3043-1
- Update to latest snapshot.

* Sun Nov 06 2016 Fabio Valentini <decathorpe@gmail.com> - 0.2+rev3039-1
- Update to latest snapshot.

* Sun Nov 06 2016 Fabio Valentini <decathorpe@gmail.com> - 0.2+rev3038-1
- Update to latest snapshot.

* Sat Nov 05 2016 Fabio Valentini <decathorpe@gmail.com> - 0.2+rev3036-1
- Update to latest snapshot.

* Thu Nov 03 2016 Fabio Valentini <decathorpe@gmail.com> - 0.2+rev3031-1
- Update to latest snapshot.

* Tue Nov 01 2016 Fabio Valentini <decathorpe@gmail.com> - 0.2+rev3030-1
- Update to latest snapshot.

* Fri Oct 21 2016 Fabio Valentini <decathorpe@gmail.com> - 0.2+rev3029-1
- Update to latest snapshot.

* Sun Oct 16 2016 Fabio Valentini <decathorpe@gmail.com> - 0.2+rev3028-1
- Update to latest snapshot.

* Sat Oct 15 2016 Fabio Valentini <decathorpe@gmail.com> - 0.2+rev3027-1
- Update to latest snapshot.

* Fri Oct 14 2016 Fabio Valentini <decathorpe@gmail.com> - 0.2+rev3026-1
- Update to latest snapshot.

* Thu Oct 13 2016 Fabio Valentini <decathorpe@gmail.com> - 0.2+rev3025-1
- Update to latest snapshot.

* Sat Oct 08 2016 Fabio Valentini <decathorpe@gmail.com> - 0.2+rev3024-1
- Update to latest snapshot.

* Fri Oct 07 2016 Fabio Valentini <decathorpe@gmail.com> - 0.2+rev3023-1
- Update to latest snapshot.

* Fri Sep 30 2016 Fabio Valentini <decathorpe@gmail.com> - 0.2+rev3022-1
- Update to latest snapshot.

* Thu Sep 29 2016 Fabio Valentini <decathorpe@gmail.com> - 0.2+rev3021-3
- Ignore appdata validation results.

* Thu Sep 29 2016 Fabio Valentini <decathorpe@gmail.com> - 0.2+rev3021-2
- Spec file cleanups.

* Thu Sep 29 2016 Fabio Valentini <decathorpe@gmail.com> - 0.2+rev3021-1
- Update to latest snapshot.

* Wed Sep 28 2016 Fabio Valentini <decathorpe@gmail.com> - 0.2+rev3020-1
- Update to latest snapshot.

* Mon Sep 26 2016 Fabio Valentini <decathorpe@gmail.com> - 0.2+rev3019-1
- Update to latest snapshot.

* Sun Sep 25 2016 Fabio Valentini <decathorpe@gmail.com> - 0.2+rev3018-1
- Update to latest snapshot.

* Sat Sep 24 2016 Fabio Valentini <decathorpe@gmail.com> - 0.2+rev3017-1
- Update to latest snapshot.

* Sat Sep 24 2016 Fabio Valentini <decathorpe@gmail.com> - 0.2+rev3016-1
- Update to latest snapshot.

* Sat Sep 24 2016 Fabio Valentini <decathorpe@gmail.com> - 0.2+rev3015-1
- Update to latest snapshot.

* Sat Sep 24 2016 Fabio Valentini <decathorpe@gmail.com> - 0.2+rev3014-1
- Update to latest snapshot.

* Tue Sep 20 2016 Fabio Valentini <decathorpe@gmail.com> - 0.2~rev3010-1
- Update to latest snapshot.

* Wed Sep 14 2016 Fabio Valentini <decathorpe@gmail.com> - 0.2~rev3009-1
- Update to latest snapshot.

* Tue Sep 13 2016 Fabio Valentini <decathorpe@gmail.com> - 0.2~rev3008-1
- Update to latest snapshot.

* Mon Sep 12 2016 Fabio Valentini <decathorpe@gmail.com> - 0.2~rev3007-1
- Update to latest snapshot.

* Sun Sep 11 2016 Fabio Valentini <decathorpe@gmail.com> - 0.2~rev3006-1
- Update to latest snapshot.

* Thu Sep 01 2016 Fabio Valentini <decathorpe@gmail.com> - 0.2~rev3005-1
- Update to latest snapshot.

* Wed Aug 31 2016 Fabio Valentini <decathorpe@gmail.com> - 0.2~rev3004-1
- Update to latest snapshot.

* Mon Aug 29 2016 Fabio Valentini <decathorpe@gmail.com> - 0.2~rev3003-2
- Update for packaging changes.

* Mon Aug 29 2016 Fabio Valentini <decathorpe@gmail.com>
- Adapt spec to .desktop and .appdata file renames.

* Mon Aug 29 2016 Fabio Valentini <decathorpe@gmail.com> - 0.2~rev3003-1
- Update to latest snapshot.

* Sat Aug 27 2016 Fabio Valentini <decathorpe@gmail.com> - 0.2~rev3002-1
- Update to latest snapshot.

* Fri Aug 26 2016 Fabio Valentini <decathorpe@gmail.com> - 0.2~rev3001-1
- Update to latest snapshot.

* Wed Aug 24 2016 Fabio Valentini <decathorpe@gmail.com> - 0.2~rev3000-1
- Update to latest snapshot.

* Tue Aug 23 2016 Fabio Valentini <decathorpe@gmail.com> - 0.2~rev2999-1
- Update to latest snapshot.

* Mon Aug 22 2016 Fabio Valentini <decathorpe@gmail.com> - 0.2~rev2998-1
- Update to latest snapshot.

* Tue Aug 16 2016 Fabio Valentini <decathorpe@gmail.com> - 0.2~rev2997-1
- Update to latest snapshot.

* Mon Aug 15 2016 Fabio Valentini <decathorpe@gmail.com> - 0.2~rev2996-1
- Update to version 0.2.

* Sun Aug 14 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.2~rev2995-1
- Update to latest snapshot.

* Sat Aug 13 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.2~rev2994-1
- Update to latest snapshot.

* Fri Aug 12 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.2~rev2993-1
- Update to latest snapshot.

* Thu Aug 11 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.2~rev2992-1
- Update to latest snapshot.

* Thu Aug 11 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.2~rev2991-1
- Update to latest snapshot.

* Wed Aug 10 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.2~rev2990-1
- Update to latest snapshot.

* Tue Aug 09 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.2~rev2989-1
- Update to latest snapshot.

* Mon Aug 08 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.2~rev2988-1
- Update to latest snapshot.

* Sun Aug 07 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.2~rev2987-2
- Update for packaging changes.

* Sun Aug 07 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.2~rev2987-1
- Update to latest snapshot.

* Sat Aug 06 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.2~rev2985-1
- Update to latest snapshot.

* Fri Aug 05 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.2~rev2984-1
- Update to latest snapshot.

* Thu Aug 04 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.2~rev2983-1
- Update to latest snapshot.

* Tue Aug 02 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.2~rev2981-1
- Update to latest snapshot.

* Mon Aug 01 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.2~rev2980-1
- Update to latest snapshot.

* Sat Jul 30 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.2~rev2978-1
- Update to latest snapshot.

* Tue Jul 26 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.2~rev2977-1
- Update to latest snapshot.

* Mon Jul 25 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.2~rev2976-1
- Update to latest snapshot.

* Fri Jul 22 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.2~rev2973-1
- Update to latest snapshot.

* Thu Jul 21 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.2~rev2972-1
- Update to latest snapshot.

* Thu Jul 14 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.2~rev2971-1
- Update to latest snapshot.

* Wed Jul 13 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.2~rev2970-1
- Update to latest snapshot.

* Tue Jul 12 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.2~rev2969-1
- Update to latest snapshot.

* Sun Jul 10 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.2~rev2968-1
- Update to latest snapshot.

* Sat Jul 09 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.2~rev2967-1
- Update to latest snapshot.

* Fri Jul 08 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.2~rev2966-1
- Update to latest snapshot.

* Thu Jul 07 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.2~rev2965-1
- Update to latest snapshot.

* Wed Jul 06 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.2~rev2964-2
- Update for packaging changes.

* Thu Jun 23 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.2~rev2953-1
- Update to latest snapshot.

* Wed Jun 22 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.2~rev2952-1
- Update to latest snapshot.

* Tue Jun 21 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.2~rev2951-1
- Update to latest snapshot.

* Mon Jun 20 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.2~rev2950-1
- Update to latest snapshot.

* Mon Jun 20 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.2~rev2949-1
- Update to latest snapshot.

* Sun Jun 19 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.2~rev2948-1
- Update to latest snapshot.

* Sat Jun 18 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.2~rev2947-1
- Update to latest snapshot.

* Fri Jun 17 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.2~rev2946-1
- Update to latest snapshot.

* Thu Jun 16 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.2~rev2945-1
- Update to latest snapshot.

* Wed Jun 15 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.2~rev2944-1
- Update to latest snapshot.

* Tue Jun 14 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.2~rev2942-1
- Update to latest snapshot.

* Mon Jun 13 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.2~rev2941-1
- Update to latest snapshot.

* Sat Jun 11 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.2~rev2940-1
- Update to latest snapshot.

* Wed Jun 08 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.2~rev2939-1
- Update to latest snapshot.

* Tue Jun 07 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.2~rev2938-1
- Update to latest snapshot.

* Fri Jun 03 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.2~rev2937-1
- Update to latest snapshot.

* Mon May 30 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.2~rev2936-3
- Update for packaging changes.

* Sun May 29 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.2~rev2936-2
- Update for packaging changes.

* Sat May 28 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.2~rev2936-1
- Update to latest snapshot.

* Fri May 27 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.2~rev2935-1
- Update to latest snapshot.

* Tue May 17 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.2~rev2934-1
- Update to latest snapshot.

* Mon May 16 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.2~rev2933-1
- Update to latest snapshot.

* Wed May 11 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.2~rev2932-1
- Update to latest snapshot.

* Tue May 10 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.2~rev2931-1
- Update to latest snapshot.

* Mon May 09 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.2~rev2930-1
- Update to latest snapshot.

* Sun May 08 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.2~rev2930-1
- Update to latest snapshot.

* Sat May 07 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.2~rev2929-1
- Update to latest snapshot.

* Fri May 06 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.2~rev2928-1
- Update to latest snapshot.

* Wed May 04 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.2~rev2927-1
- Update to latest snapshot.

* Wed May 04 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.2~rev2927-1
- Update to latest snapshot.

* Tue May 03 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.2~rev2926-1
- Update to new upstream snapshot.

* Mon May 02 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.2~rev2925-1
- Update to new upstream snapshot.

* Sun May 01 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.2~rev2924-1
- Update to new upstream snapshot.

* Sat Apr 30 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.2~rev2923-1
- Update to new upstream snapshot.

* Fri Apr 29 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.2~rev2922-1
- Update to new upstream snapshot.

* Thu Apr 28 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.2~rev2921-1
- Update to new upstream snapshot.

* Tue Apr 26 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.2~rev2919-1
- Update to new upstream snapshot.

* Mon Apr 25 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.2~rev2917-1
- Update to new upstream snapshot.

* Sun Apr 24 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.2~rev2916-1
- Update to new upstream snapshot.

* Sat Apr 23 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.2~rev2915-1
- Update to new upstream snapshot.

* Fri Apr 22 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.2~rev2914-1
- Update to new upstream snapshot.

* Wed Apr 20 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.2~rev2912-1
- Update to new upstream snapshot.

* Mon Apr 18 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.2~rev2910-1
- Update to new upstream snapshot.

* Wed Apr 13 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.2~rev2909-1
- Update to new upstream snapshot.

* Sat Apr 09 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.2~rev2908-1
- Update to new upstream snapshot.

* Sun Mar 27 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.2~rev2906-1
- Update to new upstream snapshot.

* Thu Mar 24 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.2~rev2905-1
- Update to new upstream snapshot.

* Tue Mar 22 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.2~rev2904-1
- Update to new upstream snapshot.

* Mon Mar 21 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.2~rev2903-1
- Update to new upstream snapshot.

* Tue Mar 15 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.2~rev2902-1
- Update to new upstream snapshot.

* Sun Mar 13 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.2~rev2901-1
- Update to new upstream snapshot.

* Sat Mar 12 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.2~rev2900-1
- Update to new upstream snapshot.

* Wed Mar 09 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.2~rev2899-1
- Update to new upstream snapshot.

* Tue Mar 08 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.2~rev2898-1
- Update to new upstream snapshot.

* Fri Mar 04 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.2~rev2897-1
- Update to new upstream snapshot.

* Mon Feb 22 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.2~rev2896-1
- Update to new upstream snapshot.

* Sat Feb 20 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.2~rev2895-1
- Update to new upstream snapshot.

* Thu Feb 18 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.2~rev2893-1
- Update to new upstream snapshot.

* Wed Feb 10 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.2~rev2892-1
- Update to new upstream snapshot.

* Wed Feb 03 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.1~rev2891-1
- Update to new upstream snapshot.

* Tue Feb 02 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.1~rev2890-1
- Update to new upstream snapshot.

* Fri Jan 29 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.1~rev2889-1
- Update to new upstream snapshot.

* Thu Jan 28 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.1~rev2887-1
- Update to new upstream snapshot.

* Thu Jan 28 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.1~rev2886-1
- Update to new upstream snapshot.

* Tue Jan 26 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.1~rev2885-1
- Update to new upstream snapshot. Fix build.

* Tue Jan 26 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.1~rev2882-3
- Add BR: intltool.

* Fri Jan 15 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.1~rev2882-2
- Switch to CMake build.

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


