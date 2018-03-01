Summary:        Stupidly simple Dock
Name:           plank
Version:        0.11.4+git%{date}.%{commit}
Release:        1%{?dist}
License:        GPLv3
URL:            http://launchpad.net/plank

Source0:        %{name}-%{version}.tar.gz
Source1:        %{name}.conf

BuildRequires:  desktop-file-utils
BuildRequires:  gettext
BuildRequires:  intltool
BuildRequires:  libappstream-glib
BuildRequires:  libtool
BuildRequires:  vala
BuildRequires:  vala-tools

BuildRequires:  pkgconfig(cairo) >= 1.13
BuildRequires:  pkgconfig(dbusmenu-glib-0.4) >= 0.4
BuildRequires:  pkgconfig(dbusmenu-gtk3-0.4)
BuildRequires:  pkgconfig(gdk-pixbuf-2.0) >= 2.26.0
BuildRequires:  pkgconfig(gee-0.8)
BuildRequires:  pkgconfig(glib-2.0) >= 2.40.0
BuildRequires:  pkgconfig(libgnome-menu-3.0)
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.10.0
BuildRequires:  pkgconfig(libbamf3) >= 0.2.92
BuildRequires:  pkgconfig(libwnck-3.0)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xi) >= 1.6.99.1
BuildRequires:  pkgconfig(xfixes) >= 5.0

Requires:       bamf-daemon
Requires:       hicolor-icon-theme


%description
Plank is meant to be the simplest dock on the planet. The goal is to
provide just what a dock needs and absolutely nothing more. It is,
however, a library which can be extended to create other dock programs
with more advanced features.

Thus, Plank is the underlying technology for Docky (starting in version
3.0.0) and aims to provide all the core features while Docky extends it
to add fancier things like Docklets, painters, settings dialogs, etc.


%package        libs
Summary:        Stupidly simple Dock (shared libraries)
%description    libs
Plank is meant to be the simplest dock on the planet. The goal is to
provide just what a dock needs and absolutely nothing more. It is,
however, a library which can be extended to create other dock programs
with more advanced features.

Thus, Plank is the underlying technology for Docky (starting in version
3.0.0) and aims to provide all the core features while Docky extends it
to add fancier things like Docklets, painters, settings dialogs, etc.

This package contains the shared libraries.


%package        devel
Summary:        Stupidly simple Dock (development files)
%description    devel
Plank is meant to be the simplest dock on the planet. The goal is to
provide just what a dock needs and absolutely nothing more. It is,
however, a library which can be extended to create other dock programs
with more advanced features.

Thus, Plank is the underlying technology for Docky (starting in version
3.0.0) and aims to provide all the core features while Docky extends it
to add fancier things like Docklets, painters, settings dialogs, etc.

This package contains development headers and files.


%prep
%autosetup


%build
./autogen.sh
%configure --disable-apport
%make_build


%install
%make_install
%find_lang plank

rm -f %{buildroot}/%{_libdir}/*.la
rm -f %{buildroot}/%{_libdir}/plank/*.la


%check
desktop-file-validate \
    %{buildroot}/%{_datadir}/applications/*.desktop

appstream-util validate-relax --nonet \
    %{buildroot}/%{_datadir}/appdata/*.appdata.xml


%post   libs -p /sbin/ldconfig
%postun libs -p /sbin/ldconfig


%files -f plank.lang
%{_bindir}/plank

%{_libdir}/plank/

%{_datadir}/appdata/plank.appdata.xml
%{_datadir}/applications/plank.desktop
%{_datadir}/glib-2.0/schemas/net.launchpad.plank.gschema.xml
%{_datadir}/icons/hicolor/*/apps/plank.svg
%{_datadir}/plank/

%{_mandir}/man1/plank.1.gz


%files libs
%{_libdir}/libplank.so.1
%{_libdir}/libplank.so.1.0.0


%files devel
%{_libdir}/libplank.so
%{_libdir}/pkgconfig/plank.pc

%{_includedir}/plank/

%{_datadir}/vala/vapi/plank.deps
%{_datadir}/vala/vapi/plank.vapi


%changelog
* Thu Mar 01 2018 Fabio Valentini <decathorpe@gmail.com> - 0.11.4+git180301.204817.a640d9d5-1
- Update to latest snapshot.

* Thu Mar 01 2018 Fabio Valentini <decathorpe@gmail.com> - 0.11.4+git180301.093452.109f790c-1
- Update to latest snapshot.

* Mon Feb 12 2018 Fabio Valentini <decathorpe@gmail.com> - 0.11.4+git180212.074842.ca7bcfa5-2
- Adapt to upstream dependency changes.

* Mon Feb 12 2018 Fabio Valentini <decathorpe@gmail.com> - 0.11.4+git180212.074842.ca7bcfa5-1
- Update to latest snapshot.

* Sat Jan 06 2018 Fabio Valentini <decathorpe@gmail.com> - 0.11.4+git171010.160931.c845f12e-2
- Remove icon cache scriptlets.

* Wed Oct 11 2017 Fabio Valentini <decathorpe@gmail.com> - 0.11.4+git171010.160931.c845f12e-1
- Update to latest snapshot.

* Sat Sep 16 2017 Fabio Valentini <decathorpe@gmail.com> - 0.11.4+git170721.121624.753badc6-1
- Update to version 0.11.4.

* Wed Mar 29 2017 Fabio Valentini <decathorpe@gmail.com> - 0.11.3+rev1598-1
- Update to latest snapshot.

* Mon Mar 27 2017 Fabio Valentini <decathorpe@gmail.com> - 0.11.3+rev1597-1
- Update to latest snapshot.

* Sun Mar 26 2017 Fabio Valentini <decathorpe@gmail.com> - 0.11.3+rev1596-1
- Update to latest snapshot.

* Sun Mar 19 2017 Fabio Valentini <decathorpe@gmail.com> - 0.11.3+rev1592-1
- Update to latest snapshot.

* Sun Mar 05 2017 Fabio Valentini <decathorpe@gmail.com> - 0.11.3+rev1591-1
- Update to latest snapshot.

* Sun Feb 19 2017 Fabio Valentini <decathorpe@gmail.com> - 0.11.3+rev1588-1
- Update to latest snapshot.

* Thu Feb 09 2017 Fabio Valentini <decathorpe@gmail.com> - 0.11.3+rev1587-1
- Update to latest snapshot.

* Mon Jan 16 2017 Fabio Valentini <decathorpe@gmail.com> - 0.11.3+rev1584-1
- Update to latest snapshot.

* Tue Dec 06 2016 Fabio Valentini <decathorpe@gmail.com> - 0.11.3+rev1582-1
- Update to version 0.11.3.

* Tue Dec 06 2016 Fabio Valentini <decathorpe@gmail.com> - 0.11.2+rev1582-1
- Update to latest snapshot.

* Wed Nov 30 2016 Fabio Valentini <decathorpe@gmail.com> - 0.11.2+rev1581-1
- Update to latest snapshot.

* Sun Nov 20 2016 Fabio Valentini <decathorpe@gmail.com> - 0.11.2+rev1580-1
- Update to latest snapshot.

* Sat Nov 19 2016 Fabio Valentini <decathorpe@gmail.com> - 0.11.2+rev1579-1
- Update to latest snapshot.

* Sun Nov 06 2016 Fabio Valentini <decathorpe@gmail.com> - 0.11.2+rev1578-1
- Update to latest snapshot.

* Sat Nov 05 2016 Fabio Valentini <decathorpe@gmail.com> - 0.11.2+rev1577-1
- Update to latest snapshot.

* Fri Nov 04 2016 Fabio Valentini <decathorpe@gmail.com> - 0.11.2+rev1575-1
- Update to latest snapshot.

* Thu Nov 03 2016 Fabio Valentini <decathorpe@gmail.com> - 0.11.2+rev1573-1
- Update to latest snapshot.

* Fri Oct 28 2016 Fabio Valentini <decathorpe@gmail.com> - 0.11.2+rev1572-1
- Update to latest snapshot.

* Thu Oct 06 2016 Fabio Valentini <decathorpe@gmail.com> - 0.11.2+rev1568-3
- Spurious rebuild.

* Thu Sep 29 2016 Fabio Valentini <decathorpe@gmail.com> - 0.11.2+rev1568-2
- Fix build by adding missing BR: intltool.

* Thu Sep 29 2016 Fabio Valentini <decathorpe@gmail.com> - 0.11.2+rev1568-1
- Update to version 0.11.2.

* Thu Sep 29 2016 Fabio Valentini <decathorpe@gmail.com> - 0.11.2~rev1568-2
- Spec file cleanups.

* Wed Sep 14 2016 Fabio Valentini <decathorpe@gmail.com> - 0.11.2~rev1568-1
- Update to version 0.11.2.

* Thu Aug 11 2016 Fabio Valentini <decathorpe@gmail.com> - 0.11.1~rev1567-1
- Update to latest snapshot.

* Wed Aug 10 2016 Fabio Valentini <decathorpe@gmail.com> - 0.11.1~rev1566-1
- Update to latest snapshot.

* Sun Aug 07 2016 Fabio Valentini <decathorpe@gmail.com> - 0.11.1~rev1564-2
- Update for packaging changes.

* Thu Jul 07 2016 Fabio Valentini <decathorpe@gmail.com> - 0.11.1~rev1564-1
- Update to latest snapshot.

* Wed Jul 06 2016 Fabio Valentini <decathorpe@gmail.com> - 0.11.1~rev1562-2
- Update for packaging changes.

* Mon Jun 06 2016 Fabio Valentini <decathorpe@gmail.com> - 0.11.1~rev1562-1
- Update to latest snapshot.

* Wed Jun 01 2016 Fabio Valentini <decathorpe@gmail.com> - 0.11.1~rev1559-1
- Update to latest snapshot.

* Tue May 31 2016 Fabio Valentini <decathorpe@gmail.com> - 0.11.1~rev1556-1
- Update to latest snapshot.

* Mon May 30 2016 Fabio Valentini <decathorpe@gmail.com> - 0.11.1~rev1555-3
- Update for packaging changes.

* Sun May 29 2016 Fabio Valentini <decathorpe@gmail.com> - 0.11.1~rev1555-2
- Update for packaging changes.

* Thu May 12 2016 Fabio Valentini <decathorpe@gmail.com> - 0.11.1~rev1555-1
- Update to latest snapshot.

* Wed May 11 2016 Fabio Valentini <decathorpe@gmail.com> - 0.11.1~rev1554-1
- Update to latest snapshot.

* Wed May 04 2016 Fabio Valentini <decathorpe@gmail.com> - 0.11.1~rev1551-2
- Update for packaging changes.

* Wed May 04 2016 Fabio Valentini <decathorpe@gmail.com> - 0.11.1~rev1551-1
- Update to latest snapshot.


