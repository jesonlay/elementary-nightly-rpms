%global appname com.github.needle-and-thread.vocal

Name:           vocal
Summary:        Powerful, beautiful, and simple podcast client
Version:        2.2.0+git%{date}.%{commit}
Release:        1%{?dist}
License:        GPLv3

URL:            https://github.com/needle-and-thread/%{name}
Source0:        %{name}-%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  desktop-file-utils
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  gettext
BuildRequires:  intltool
BuildRequires:  libappstream-glib
BuildRequires:  vala >= 0.26.2

BuildRequires:  pkgconfig(clutter-gst-3.0)
BuildRequires:  pkgconfig(clutter-gtk-1.0)
BuildRequires:  pkgconfig(glib-2.0) >= 2.32
BuildRequires:  pkgconfig(gdk-x11-3.0)
BuildRequires:  pkgconfig(gee-0.8)
BuildRequires:  pkgconfig(granite)
BuildRequires:  pkgconfig(gstreamer-1.0)
BuildRequires:  pkgconfig(gstreamer-pbutils-1.0)
BuildRequires:  pkgconfig(gthread-2.0)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(json-glib-1.0)
BuildRequires:  pkgconfig(libnotify)
BuildRequires:  pkgconfig(libsoup-2.4)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(sqlite3)
BuildRequires:  pkgconfig(unity)
BuildRequires:  pkgconfig(webkit2gtk-4.0)

Requires:       hicolor-icon-theme


%description
Vocal is a powerful, fast, and intuitive application that helps users
find new podcasts, manage their libraries, and enjoy the best that
independent audio and video publishing has to offer. Vocal features full
support for both episode downloading and streaming, native system
integration, iTunes store search and top 100 charts (with international
results support), iTunes link parsing, OPML importing and exporting, and
so much more. Plus, it has great smart features like automatically
keeping your library clean from old files, and the ability to set custom
skip intervals.


%prep
%autosetup


%build
# mark sources files and docs as NOT executable
for i in $(find -name "*.vala"); do chmod a-x $i; done
chmod a-x AUTHORS README.md COPYING

mkdir build && pushd build
%cmake ..
%make_build
popd


%install
pushd build
%make_install
popd

%find_lang vocal


%check
desktop-file-validate \
    %{buildroot}/%{_datadir}/applications/%{appname}.desktop

appstream-util validate-relax --nonet \
    %{buildroot}/%{_datadir}/metainfo/%{appname}.appdata.xml


%files -f vocal.lang
%doc AUTHORS README.md
%license COPYING

%{_bindir}/%{appname}

%{_datadir}/applications/%{appname}.desktop
%{_datadir}/glib-2.0/schemas/%{appname}.gschema.xml
%{_datadir}/icons/hicolor/*/apps/%{appname}*.svg
%{_datadir}/metainfo/%{appname}.appdata.xml
%{_datadir}/vocal/


%changelog
* Sat Oct 13 2018 Fabio Valentini <decathorpe@gmail.com> - 2.2.0+git181013.171510.c9ce8758-1
- Update to latest snapshot.

* Sat Oct 13 2018 Fabio Valentini <decathorpe@gmail.com> - 2.2.0+git181013.165349.0dd8bc96-1
- Update to latest snapshot.

* Thu Oct 11 2018 Fabio Valentini <decathorpe@gmail.com> - 2.2.0+git181011.184858.ea7dae93-1
- Update to latest snapshot.

* Fri Aug 17 2018 Fabio Valentini <decathorpe@gmail.com> - 2.2.0+git180704.211347.92567324-3
- Add missing BR: gcc, gcc-c++.

* Thu Aug 16 2018 Fabio Valentini <decathorpe@gmail.com> - 2.2.0+git180704.211347.92567324-2
- Occasional mass rebuild.

* Thu Jul 05 2018 Fabio Valentini <decathorpe@gmail.com> - 2.2.0+git180704.211347.92567324-1
- Update to latest snapshot.

* Wed Jul 04 2018 Fabio Valentini <decathorpe@gmail.com> - 2.2.0+git180702.173527.b5eb46fb-1
- Update to latest snapshot.

* Tue May 29 2018 Fabio Valentini <decathorpe@gmail.com> - 2.2.0+git180528.164146.8ef82433-1
- Update to latest snapshot.

* Mon May 07 2018 Fabio Valentini <decathorpe@gmail.com> - 2.2.0+git180507.011529.63397a9b-1
- Update to latest snapshot.

* Mon Apr 23 2018 Fabio Valentini <decathorpe@gmail.com> - 2.2.0+git180422.194240.2fd81567-1
- Update to version 2.2.0.

* Sun Apr 22 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.5+git180422.190029.d7c981d0-1
- Update to latest snapshot.

* Sun Apr 22 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.5+git180422.163026.edad62e6-1
- Update to latest snapshot.

* Sat Apr 21 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.5+git180421.005249.3b5eab4e-1
- Update to latest snapshot.

* Fri Apr 20 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.5+git180420.134353.bba64f59-1
- Update to latest snapshot.

* Tue Apr 17 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.5+git180417.142530.572fe070-1
- Update to latest snapshot.

* Tue Apr 10 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.5+git180409.232445.270fa459-1
- Update to latest snapshot.

* Mon Apr 09 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.5+git180409.120429.54487b24-1
- Update to latest snapshot.

* Sun Apr 08 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.5+git180406.150122.276de53f-1
- Update to latest snapshot.

* Thu Apr 05 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.5+git180405.203634.32f85270-1
- Update to latest snapshot.

* Thu Apr 05 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.5+git180405.182106.8000aa8b-1
- Update to latest snapshot.

* Thu Apr 05 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.5+git180405.142627.959e9a24-1
- Update to latest snapshot.

* Fri Feb 02 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.5+git180202.154603.f598ae14-1
- Update to latest snapshot.

* Thu Feb 01 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.5+git180201.002338.efc12c33-1
- Update to latest snapshot.

* Sat Jan 06 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.5+git180103.145139.30277f40-2
- Remove icon cache scriptlets.

* Thu Jan 04 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.5+git180103.145139.30277f40-1
- Update to latest snapshot.

* Mon Jan 01 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.5+git180101.003653.cab7185f-1
- Update to version 2.1.5.

* Mon Jan 01 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.0+git180101.003653.cab7185f-1
- Update to latest snapshot.

* Sun Dec 31 2017 Fabio Valentini <decathorpe@gmail.com> - 2.1.0+git171230.172457.0a4d8903-1
- Update to version 2.1.0.

* Sat Dec 30 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0.20+git171230.172457.0a4d8903-1
- Update to latest snapshot.

* Sat Dec 30 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0.20+git171230.165435.e4d64f27-1
- Update to latest snapshot.

* Sat Dec 30 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0.20+git171230.152508.678fee74-1
- Update to latest snapshot.

* Tue Dec 12 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0.20+git171212.210526.647f1fc3-1
- Update to latest snapshot.

* Tue Dec 12 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0.20+git171212.024458.d9c1df3d-1
- Update to latest snapshot.

* Mon Dec 11 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0.20+git171211.142348.dc83ad7e-1
- Update to latest snapshot.

* Tue Nov 21 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0.20+git171121.131311.897241a7-1
- Update to latest snapshot.

* Wed Nov 08 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0.20+git171022.233729.93af560d-1
- Initial snapshot build.

* Sat Nov 04 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0.20-4
- Rebuild for granite soname bump.

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.20-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.20-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Jun 10 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0.20-1
- Update to version 2.0.20.

* Sun May 28 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0.19-1
- Initial package.


