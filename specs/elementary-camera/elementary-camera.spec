%global srcname camera
%global appname io.elementary.camera

Name:           elementary-camera
Summary:        Fast and beautiful camera app
Version:        0.3.0.1+git%{date}.%{commit}
Release:        1%{?dist}
License:        GPLv3

URL:            https://github.com/elementary/%{srcname}
Source0:        %{name}-%{version}.tar.gz


BuildRequires:  appstream
BuildRequires:  desktop-file-utils
BuildRequires:  gettext
BuildRequires:  libappstream-glib
BuildRequires:  meson
BuildRequires:  pkgconfig
BuildRequires:  vala >= 0.24
BuildRequires:  vala-tools

BuildRequires:  pkgconfig(clutter-gst-3.0)
BuildRequires:  pkgconfig(clutter-gtk-1.0)
BuildRequires:  pkgconfig(gee-0.8)
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(granite)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(libcanberra)

Provides:       snap-photobooth
Obsoletes:      snap-photobooth


%description
A fast and beautiful camera app.


%prep
%autosetup


%build
%meson
%meson_build


%install
%meson_install

%find_lang %{appname}


%check
desktop-file-validate \
    %{buildroot}/%{_datadir}/applications/%{appname}.desktop

appstream-util validate-relax --nonet \
    %{buildroot}/%{_datadir}/metainfo/%{appname}.appdata.xml


%files -f %{appname}.lang
%{_bindir}/%{appname}

%{_datadir}/applications/%{appname}.desktop
%{_datadir}/glib-2.0/schemas/%{appname}.gschema.xml
%{_datadir}/metainfo/%{appname}.appdata.xml


%changelog
* Sun Jun 10 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.0.1+git180610.001058.be6c6af5-1
- Update to latest snapshot.

* Sat Jun 09 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.0.1+git180609.145039.7a082d5d-1
- Update to latest snapshot.

* Wed Jun 06 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.0.1+git180606.115631.2b77e38f-1
- Update to latest snapshot.

* Wed Jun 06 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.0.1+git180606.000753.6016f021-1
- Update to latest snapshot.

* Tue Jun 05 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.0.1+git180605.085423.c37c8e27-1
- Update to latest snapshot.

* Sun Jun 03 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.0.1+git180603.061218.4b39ab34-1
- Update to latest snapshot.

* Sat Jun 02 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.0.1+git180602.184954.92ca85c3-1
- Update to latest snapshot.

* Sat Jun 02 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.0.1+git180602.000427.7d65e743-1
- Update to latest snapshot.

* Fri Jun 01 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.0.1+git180601.143941.310d24e3-1
- Update to latest snapshot.

* Fri Jun 01 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.0.1+git180531.175159.a5a74472-1
- Update to latest snapshot.

* Thu May 31 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.0.1+git180531.163017.d056e8a6-1
- Update to latest snapshot.

* Thu May 31 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.0.1+git180531.154652.e56f2ce9-1
- Update to latest snapshot.

* Thu May 31 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.0.1+git180531.061746.d3950773-1
- Update to latest snapshot.

* Wed May 30 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.0.1+git180529.235843.dbce6564-1
- Update to latest snapshot.

* Tue May 29 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.0.1+git180529.133554.dd192bde-2
- Adapt to upstream file changes.

* Tue May 29 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.0.1+git180529.133554.dd192bde-1
- Update to latest snapshot.

* Mon May 28 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.0.1+git180528.072615.3dbfecdc-1
- Update to latest snapshot.

* Sun May 27 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.0.1+git180527.000438.a42769ed-1
- Update to latest snapshot.

* Sat May 26 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.0.1+git180525.195708.927d1c47-1
- Update to latest snapshot.

* Sun May 13 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.0.1+git180513.001054.a1a701be-1
- Update to latest snapshot.

* Sat May 12 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.0.1+git180512.001051.c338a167-1
- Update to latest snapshot.

* Fri Apr 20 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.0.1+git180420.001111.7502d749-1
- Update to latest snapshot.

* Sun Mar 25 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.0.1+git180324.152420.ed76e8ab-1
- Update to latest snapshot.

* Sat Feb 24 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.0.1+git180223.210831.d0fef5ff-1
- Update to latest snapshot.

* Mon Feb 05 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.0.1+git180205.001051.c1aebde1-1
- Update to latest snapshot.

* Sun Jan 28 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.0.1+git180120.193909.9f6838a3-1
- Update to latest snapshot.

* Tue Jan 09 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.0.1+git180109.120659.3b8fb5ff-1
- Update to latest snapshot.

* Sun Dec 31 2017 Fabio Valentini <decathorpe@gmail.com> - 0.3.0.1+git171010.092010.3494a051-3
- Clean up .spec file.

* Wed Oct 11 2017 Fabio Valentini <decathorpe@gmail.com> - 0.3.0.1+git171010.092010.3494a051-2
- Adapt to upstream file changes.

* Tue Oct 10 2017 Fabio Valentini <decathorpe@gmail.com> - 0.3.0.1+git171010.092010.3494a051-1
- Update to latest snapshot.

* Mon Sep 25 2017 Fabio Valentini <decathorpe@gmail.com> - 0.3.0.1+git170925.094829.b4e015e7-1
- Update to latest snapshot.

* Tue Sep 19 2017 Fabio Valentini <decathorpe@gmail.com> - 0.3.0.1+git170704.192116.7bb3dae9-1
- Update to version 0.3.0.1.


