Summary:        The elementary continuation of Shotwell
Name:           pantheon-photos
Version:        0.2+rev%{rev}
Release:        1%{?dist}
License:        LGPLv2.1
URL:            http://launchpad.net/pantheon-photos

Source0:        %{name}-%{version}.tar.gz
Source1:        %{name}.conf

BuildRequires:  cmake
BuildRequires:  desktop-file-utils
BuildRequires:  gettext
BuildRequires:  intltool
BuildRequires:  libappstream-glib
BuildRequires:  vala

BuildRequires:  pkgconfig(gee-0.8)
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
BuildRequires:  pkgconfig(libxml-2.0) >= 2.6.32
BuildRequires:  pkgconfig(rest-0.7) >= 0.7
BuildRequires:  pkgconfig(sqlite3) >= 3.5.9
BuildRequires:  pkgconfig(webkit2gtk-4.0) >= 2.0.0


%description
The elementary continuation of Shotwell, originally written by Yorba
Foundation.

Designed for elementary OS. Works and looks great on any GTK+ desktop.


%prep
%autosetup


%build
%cmake
%make_build


%install
%make_install
%find_lang pantheon-photos


%check
desktop-file-validate %{buildroot}/%{_datadir}/applications/*.desktop
appstream-util validate-relax --nonet %{buildroot}/%{_datadir}/appdata/*.appdata.xml || :


%clean
rm -rf %{buildroot}


%if %{?fedora} < 25
%post
/usr/bin/update-desktop-database &> /dev/null || :

%postun
/usr/bin/update-desktop-database &> /dev/null || :
%endif


%files -f pantheon-photos.lang
%doc AUTHORS MAINTAINERS NEWS README THANKS
%license COPYING

%{_bindir}/pantheon-photos

%{_libdir}/pantheon-photos/

%{_datadir}/appdata/org.pantheon.photos.appdata.xml
%{_datadir}/applications/org.pantheon.photos.desktop
%{_datadir}/applications/org.pantheon.photos-viewer.desktop
%{_datadir}/glib-2.0/schemas/*.xml
%{_datadir}/pantheon-photos/


%changelog
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
- Update to version 0.2.

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



